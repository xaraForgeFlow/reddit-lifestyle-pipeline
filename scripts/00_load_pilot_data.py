import json
import random
from pathlib import Path
from typing import Optional, Dict, List

from datasets import load_dataset
from tqdm import tqdm

# ======================================================
# CONFIG
# ======================================================

TARGET_N_POSTS = 500_000
DATASET_NAME = "fddemarco/pushshift-reddit"
OUTPUT_PATH = Path("data/pilot_raw_posts.json")

# Early window for fast access
MIN_UTC = 1356998400   # 2013-01-01
MAX_UTC = 1514764800   # 2018-01-01

RANDOM_SEED = 42
ACCEPT_PROB = 0.25     # tune if needed (0.2–0.3 is safe)

# ======================================================


def normalize_row(row: Dict) -> Optional[Dict]:
    text = row.get("selftext")
    if not text:
        return None

    text = text.strip()
    if text in {"", "[deleted]", "[removed]"}:
        return None

    subreddit = row.get("subreddit")
    if not subreddit:
        return None

    created = row.get("created_utc")
    if created is None or not (MIN_UTC <= created <= MAX_UTC):
        return None

    return {
        "id": row.get("id"),
        "text": text,
        "subreddit": subreddit.lower(),
        "created_utc": created,
    }


def main():
    random.seed(RANDOM_SEED)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("SCRIPT 00 — Fast Pushshift Pilot (Early-window + Random)")
    print(f"Target posts : {TARGET_N_POSTS}")
    print(f"Time window  : 2013–2017")
    print(f"Accept prob  : {ACCEPT_PROB}")
    print(f"Output       : {OUTPUT_PATH}")
    print("=" * 70)

    posts: List[Dict] = []
    seen = 0
    skipped = 0

    dataset = load_dataset(
        DATASET_NAME,
        split="train",
        streaming=True,
    )

    for row in tqdm(dataset, desc="Streaming early Reddit"):
        seen += 1

        norm = normalize_row(row)
        if norm is None:
            skipped += 1
            continue

        # random subsampling for diversity
        if random.random() > ACCEPT_PROB:
            skipped += 1
            continue

        posts.append(norm)

        if len(posts) >= TARGET_N_POSTS:
            break

    # -----------------------
    # SAFETY CHECKS
    # -----------------------
    assert len(posts) > 0, "❌ No valid posts collected"
    assert all("text" in p for p in posts)
    assert all("subreddit" in p for p in posts)

    # -----------------------
    # SAVE OUTPUT
    # -----------------------
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False)

    print("=" * 70)
    print(f"✅ Saved {len(posts):,} pilot posts")
    print(f"👀 Rows scanned: {seen:,}")
    print(f"⏭️  Skipped     : {skipped:,}")
    print(f"📁 Output → {OUTPUT_PATH.resolve()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
