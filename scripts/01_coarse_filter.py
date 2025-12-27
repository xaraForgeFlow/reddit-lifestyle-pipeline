"""
01_coarse_filter.py
--------------------

High-recall coarse filtering for Reddit submissions.

Logic:
- Hard subreddit blacklist
- Hard exclusion keywords
- Always-keep seed subreddits
- Graylist + unknown subreddits require lifestyle signal

This stage prioritizes RECALL.
Precision is handled later by LFs + NLI.
"""

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
# Helpers
# =========================================================

def contains_any(text: str, keywords: Iterable[str]) -> bool:
    """Return True if any keyword appears in text."""
    if not text:
        return False
    text = text.lower()
    return any(k in text for k in keywords)


def normalize_text(post: dict) -> str:
    """
    Combine title + selftext if available.
    Pushshift submissions often store both.
    """
    title = post.get("title", "") or ""
    body = post.get("selftext", "") or post.get("text", "") or ""
    return f"{title}\n{body}".lower()


# =========================================================
# Core filter
# =========================================================

def coarse_filter(post: dict) -> bool:
    """
    Decide whether to KEEP a post.

    Returns:
        True  -> keep
        False -> drop
    """
    subreddit = (post.get("subreddit") or "").lower()
    text = normalize_text(post)

    # -----------------------------------------------------
    # 1. Hard blacklist
    # -----------------------------------------------------
    if subreddit in BLACKLIST_SUBREDDITS:
        return False

    if contains_any(text, COARSE_EXCLUSION_KEYWORDS):
        return False

    # -----------------------------------------------------
    # 2. Always-keep seed subreddits
    # -----------------------------------------------------
    if subreddit in SEED_WHITELIST:
        return True

    # -----------------------------------------------------
    # 3. Graylist: require lifestyle signal
    # -----------------------------------------------------
    if subreddit in GRAYLIST_SUBREDDITS:
        return contains_any(text, COARSE_LIFESTYLE_KEYWORDS)

    # -----------------------------------------------------
    # 4. Unknown subreddits: conservative keep
    # -----------------------------------------------------
    # Keep if:
    # - lifestyle keyword appears
    # OR
    # - complaint-like language appears (high recall)
    return (
     contains_any(text, COARSE_LIFESTYLE_KEYWORDS)
     or any(p in text for p in [
        "i feel",
        "i am",
        "i'm",
        "i have been",
        "i've been",
        "struggling",
        "hard for me",
        "can't",
        "cannot",
        "dealing with",
        "suffering from",
     ])
    )


# =========================================================
# Main
# =========================================================

def main():
    """
    Expected input format:
    - JSON file containing a list of posts
      OR
    - JSONL (one post per line)

    Each post should minimally contain:
    - subreddit
    - title and/or selftext
    """

    input_path = Path("data/pilot_raw_posts.json")
    output_path = Path("data/pilot_filtered_posts.json")


    kept = []
    total = 0

    print("Starting coarse filtering...")
    print(f"Input:  {input_path.resolve()}")
    print(f"Output: {output_path.resolve()}")

    # -----------------------------------------------------
    # Load input (JSON or JSONL)
    # -----------------------------------------------------
    with input_path.open("r", encoding="utf-8") as f:
        first_char = f.read(1)
        f.seek(0)

        if first_char == "[":
            # JSON array
            posts = json.load(f)
            iterable = posts
        else:
            # JSONL
            iterable = (json.loads(line) for line in f)

        for post in iterable:
            total += 1
            if coarse_filter(post):
                kept.append(post)

            if total % 100_000 == 0:
                print(f"Processed {total:,} posts...")

    # -----------------------------------------------------
    # Save output
    # -----------------------------------------------------
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(kept, f, ensure_ascii=False)

    print("Done.")
    print(f"Kept {len(kept):,} / {total:,} posts "
          f"({len(kept) / max(total, 1):.2%})")


if __name__ == "__main__":
    main()
