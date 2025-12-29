import json
from pathlib import Path
from typing import Iterable

from config.keywords import (
    COARSE_LIFESTYLE_KEYWORDS,
    COARSE_EXCLUSION_KEYWORDS,
)
from config.subreddits import (
    SEED_WHITELIST,
    GRAYLIST_SUBREDDITS,
    BLACKLIST_SUBREDDITS,
)

# =========================================================
# Config
# =========================================================

INPUT_PATH = Path("data/pilot_raw_posts.json")
OUTPUT_PATH = Path("data/pilot_filtered_posts.jsonl")
LOG_EVERY = 50_000

# =========================================================
# Helpers
# =========================================================

def contains_any(text: str, keywords: Iterable[str]) -> bool:
    if not text:
        return False
    text = text.lower()
    return any(k in text for k in keywords)


def normalize_text(post: dict) -> str:
    # Script 00 guarantees "text"
    return (post.get("text") or "").lower()

# =========================================================
# Core filter
# =========================================================

def coarse_filter(post: dict) -> bool:
    subreddit = (post.get("subreddit") or "").lower()
    text = normalize_text(post)

    if not subreddit or not text:
        return False

    # 1. Hard blacklist
    if subreddit in BLACKLIST_SUBREDDITS:
        return False

    if contains_any(text, COARSE_EXCLUSION_KEYWORDS):
        return False

    # 2. Always-keep seed subreddits
    if subreddit in SEED_WHITELIST:
        return True

    # 3. Graylist
    if subreddit in GRAYLIST_SUBREDDITS:
        return contains_any(text, COARSE_LIFESTYLE_KEYWORDS)

    # 4. Unknown
    return contains_any(text, COARSE_LIFESTYLE_KEYWORDS)

# =========================================================
# Main
# =========================================================

def main():
    kept = 0
    total = 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("Starting coarse filtering...")
    print(f"Input:  {INPUT_PATH.resolve()}")
    print(f"Output: {OUTPUT_PATH.resolve()}")

    with INPUT_PATH.open("r", encoding="utf-8") as fin, \
         OUTPUT_PATH.open("w", encoding="utf-8") as fout:

        posts = json.load(fin)

        for post in posts:
            total += 1

            if coarse_filter(post):
                fout.write(json.dumps(post, ensure_ascii=False) + "\n")
                kept += 1

            if total % LOG_EVERY == 0:
                print(f"Processed {total:,} posts — kept {kept:,}")

    print("Done.")
    print(f"Kept {kept:,} / {total:,} posts ({kept / max(total,1):.2%})")


if __name__ == "__main__":
    main()
