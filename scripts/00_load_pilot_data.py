import json
import random
from pathlib import Path
from typing import Dict, Optional

from datasets import load_dataset
from tqdm import tqdm

# ======================================================
# PILOT CONFIG
# ======================================================

PILOT_N_POSTS = 400_000      # larger pilot
RANDOM_SEED = 42

DATASET_NAME = "fddemarco/pushshift-reddit"
USE_STREAMING = True

OUTPUT_PATH = Path("data/pilot_raw_posts.json")

# ======================================================
# TIME WINDOW (DIFFERENT FROM PREVIOUS PILOT)
# ======================================================
# Newer slice: 2021–2023 (non-overlapping, different discourse)

MIN_UTC = 1609459200   # 2021-01-01
MAX_UTC = 1672531200   # 2023-01-01

# ======================================================


def normalize_row(row: Dict) -> Optional[Dict]:
    """
    Normalize Pushshift Reddit submission into pipeline schema.

    Required downstream fields:
      - id
      - text
      - subreddit
      - created_utc
    """

    # Pushshift uses 'selftext'
    text = row.get("selftext")
    if not text:
        return None

    text = text.strip()
    if text in {"", "[deleted]", "[removed]"}:
        return None

    subreddit = row.get("subreddit")
    if not subreddit:
        return None

    return {
        "id": row.get("id"),
        "text": text,
        "subreddit": subreddit.lower(),
        "created_utc": row.get("created_utc"),
    }


def main():
    random.seed(RANDOM_SEED)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("SCRIPT 00 — Load Pushshift Reddit Pilot")
    print(f"Dataset     : {DATASET_NAME}")
    print(f"Pilot size  : {PILOT_N_POSTS}")
    print(f"Streaming   : {USE_STREAMING}")
    print(f"Time window : {MIN_UTC} → {MAX_UTC}")
    print(f"Seed        : {RANDOM_SEED}")
    print("=" * 70)

    try:
        dataset = load_dataset(
            DATASET_NAME,
            streaming=USE_STREAMING,
        )
    except Exception as e:
        raise RuntimeError(
            f"Failed to load dataset '{DATASET_NAME}'. "
            f"Check dataset name or network access."
        ) from e

    posts = []
    skipped = 0

    # Pushshift dataset exposes a single iterable split
    split = next(iter(dataset.values()))

    for row in tqdm(split, desc="Collecting pilot posts"):
        created = row.get("created_utc")
        if not created or not (MIN_UTC <= created <= MAX_UTC):
            skipped += 1
            continue

        norm = normalize_row(row)
        if norm is None:
            skipped += 1
            continue

        posts.append(norm)

        if len(posts) >= PILOT_N_POSTS:
            break

    # -----------------------
    # HARD SAFETY CHECKS
    # -----------------------

    assert len(posts) > 0, "❌ No valid posts collected"
    assert all("text" in p for p in posts)
    assert all("subreddit" in p for p in posts)

    # -----------------------
    # SAVE OUTPUT
    # -----------------------

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print("=" * 70)
    print(f"✅ Saved {len(posts)} pilot posts")
    print(f"⏭️  Skipped {skipped} invalid rows")
    print(f"📁 Output → {OUTPUT_PATH.resolve()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
