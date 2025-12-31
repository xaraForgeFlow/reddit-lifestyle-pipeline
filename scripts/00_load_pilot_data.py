import json
from pathlib import Path
from typing import Optional, Dict, List

from datasets import load_dataset
from tqdm import tqdm

# ======================================================
# CONFIG
# ======================================================

PILOT_N_POSTS = 400_000
DATASET_NAME = "fddemarco/pushshift-reddit"
OUTPUT_PATH = Path("data/pilot_raw_posts.json")

MIN_UTC = 1609459200   # 2021-01-01
MAX_UTC = 1672531200   # 2023-01-01

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
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("SCRIPT 00 — Load Pushshift Reddit Pilot (STREAMING, CORRECT)")
    print(f"Dataset     : {DATASET_NAME}")
    print(f"Pilot size  : {PILOT_N_POSTS}")
    print(f"Time window : 2021–2023")
    print(f"Output      : {OUTPUT_PATH}")
    print("=" * 70)

    posts: List[Dict] = []
    skipped = 0
    seen = 0

    # ✅ THIS is the only correct way for this dataset
    dataset = load_dataset(
        DATASET_NAME,
        split="train",
        streaming=True,
    )

    for row in tqdm(dataset, desc="Streaming posts"):
        seen += 1

        norm = normalize_row(row)
        if norm is None:
            skipped += 1
            continue

        posts.append(norm)

        if len(posts) >= PILOT_N_POSTS:
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
    print(f"⏭️  Skipped {skipped:,} invalid rows")
    print(f"👀 Rows scanned: {seen:,}")
    print(f"📁 Output → {OUTPUT_PATH.resolve()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
