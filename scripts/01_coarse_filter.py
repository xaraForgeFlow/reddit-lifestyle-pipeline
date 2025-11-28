import json

# Coarse lifestyle-related keywords (very simple for now)
LIFESTYLE_KEYWORDS = [
    "sleep", "insomnia",
    "diet", "calorie", "food",
    "stress", "anxiety",
    "exercise", "gym", "running",
    "lonely", "isolation",
    "smoking", "alcohol", "addiction",
    "memory", "focus", "brain fog",
]

EXCLUSION_KEYWORDS = [
    "meme", "lol", "lmao",
    "anime", "game", "gaming",
    "politics",
]


def contains_any(text, keywords):
    text = text.lower()
    return any(k in text for k in keywords)


def coarse_filter(post):
    """Return True if we keep this post, False if we drop it."""
    text = post["text"]

    # If it's obviously a meme / game / politics → drop
    if contains_any(text, EXCLUSION_KEYWORDS):
        return False

    # If it mentions any lifestyle keyword → keep
    if contains_any(text, LIFESTYLE_KEYWORDS):
        return True

    # Otherwise, drop
    return False


def main():
    # Dummy posts for now. Later: load real data here.
    sample_posts = [
        {"id": 1, "text": "I have terrible insomnia lately", "subreddit": "insomnia"},
        {"id": 2, "text": "LOL this game is so funny", "subreddit": "gaming"},
        {"id": 3, "text": "I'm stressed and can't eat properly", "subreddit": "offmychest"},
    ]

    filtered = [p for p in sample_posts if coarse_filter(p)]

    with open("filtered_posts.json", "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=4)

    print("Filtering complete.")
    print(f"Kept {len(filtered)} out of {len(sample_posts)} posts.")


if __name__ == "__main__":
    main()
