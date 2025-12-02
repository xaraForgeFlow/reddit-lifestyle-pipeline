"""
01_coarse_filter.py
--------------------

Coarse filtering for Reddit posts using:
- keyword-based filtering
- subreddit whitelist/graylist/blacklist
- simple exclusion rules

"""

import json
from pathlib import Path

# ---- Import configs ----
from config.keywords import (
    COARSE_LIFESTYLE_KEYWORDS,
    COARSE_EXCLUSION_KEYWORDS,
)
from config.subreddits import (
    WHITELIST_SUBREDDITS,
    GRAYLIST_SUBREDDITS,
    BLACKLIST_SUBREDDITS,
)


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def contains_any(text: str, keywords):
    """Return True if any keyword appears in the text."""
    text = text.lower()
    return any(k in text for k in keywords)


def coarse_filter(post):
    """
    Decide whether to KEEP or DROP a post based on:
    - subreddit whitelist / blacklist
    - exclusion keywords
    - lifestyle keywords
    """

    text = post.get("text", "").lower()
    subreddit = post.get("subreddit", "").lower()

    # ----------------------------------------------
    # 1) Hard blacklist (always remove)
    # ----------------------------------------------
    if subreddit in BLACKLIST_SUBREDDITS:
        return False

    if contains_any(text, COARSE_EXCLUSION_KEYWORDS):
        return False

    # ----------------------------------------------
    # 2) Strong whitelist (always keep)
    # ----------------------------------------------
    if subreddit in WHITELIST_SUBREDDITS:
        return True

    # ----------------------------------------------
    # 3) Graylist logic (keep only if lifestyle keyword appears)
    # ----------------------------------------------
    if subreddit in GRAYLIST_SUBREDDITS:
        return contains_any(text, COARSE_LIFESTYLE_KEYWORDS)

    # ----------------------------------------------
    # 4) Default logic for unknown subreddits
    # Keep only if lifestyle keyword is found
    # ----------------------------------------------
    return contains_any(text, COARSE_LIFESTYLE_KEYWORDS)


# ---------------------------------------------------------
# Demo mode with dummy posts
# ---------------------------------------------------------

def load_dummy_data():
    """Temporary stub. Replace with real data later."""
    return [
        {"id": 1, "text": "I have terrible insomnia lately", "subreddit": "insomnia"},
        {"id": 2, "text": "LOL this game is so funny", "subreddit": "gaming"},
        {"id": 3, "text": "I'm stressed and can't eat properly", "subreddit": "offmychest"},
        {"id": 4, "text": "Feeling lonely recently", "subreddit": "askreddit"},
        {"id": 5, "text": "Vote for this political candidate!", "subreddit": "politics"},
    ]


# ---------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------

def main():

    print("Running coarse filtering using configs...")

    # In future: load real data instead of dummy
    posts = load_dummy_data()

    kept = []
    for post in posts:
        if coarse_filter(post):
            kept.append(post)

    # Save results
    output_path = Path("filtered_posts.json")
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(kept, f, indent=4)

    print(f"Done. Kept {len(kept)} of {len(posts)} posts.")
    print(f"Saved to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
