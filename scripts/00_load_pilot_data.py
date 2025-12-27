import json
import random
from pathlib import Path
from typing import Optional, Dict

from datasets import load_dataset
from tqdm import tqdm

# ======================================================
# RUNTIME CONFIG (pilot-scale only)
# ======================================================

PILOT_N_POSTS = 200000          
RANDOM_SEED = 42

# Choose ONE dataset and be explicit
DATASET_NAME = "socialgrelp/one-million-reddit-questions"
DATASET_SPLIT = "train"
USE_STREAMING = True         

OUTPUT_PATH = Path("data/pilot_raw_posts.json")

# ======================================================


def normalize_row(row: Dict) -> Optional[Dict]:
    """
    Normalize a raw Reddit row into the canonical pipeline schema.

    Required downstream fields:
      - id
      - text
      - subreddit
      - created_utc
    """

    # Handle different Reddit dataset conventions
    text = row.get("text") or row.get("body")
    if text is None:
        return None

    text = text.strip()
    if text == "":
        return None

    subreddit = row.get("subreddit")
    if subreddit is None:
        return None

    return {
        "id": row.get("id"),
        "text": text,
        "subreddit": subreddit.lower(),
        "created_utc": row.get("created_utc"),
    }


def main():
    random.seed(RANDOM_SEED)

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Running script 00 — load pilot Reddit data")
    print(f"Dataset      : {DATASET_NAME}")
    print(f"Pilot size   : {PILOT_N_POSTS}")
    print(f"Random seed  : {RANDOM_SEED}")
    print("=" * 60)

    dataset = load_dataset(
        DATASET_NAME,
        split=DATASET_SPLIT,
        streaming=USE_STREAMING,
    )

    posts = []
    skipped = 0

    for row in tqdm(dataset, desc="Collecting pilot posts"):
        norm = normalize_row(row)
        if norm is None:
            skipped += 1
            continue

        posts.append(norm)

        if len(posts) >= PILOT_N_POSTS:
            break

    # -----------------------
    # Hard safety checks
    # -----------------------

    assert len(posts) > 0, "❌ No valid posts collected"
    assert all("text" in p for p in posts), "❌ Missing text field"
    assert all("subreddit" in p for p in posts), "❌ Missing subreddit field"

    # -----------------------
    # Save output
    # -----------------------

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print(f"✅ Saved {len(posts)} pilot posts")
    print(f"⏭️  Skipped {skipped} invalid rows")
    print(f"📁 Output → {OUTPUT_PATH.resolve()}")
    print("=" * 60)


if __name__ == "__main__":
    main()
