"""
07_condition_filtering.py
--------------------------

Filters posts based on a medical condition.
Later will:
- use keywords (diagnosed with, my doctor said)
- use NLI
- use symptoms
"""

import json
from pathlib import Path

CONDITION_KEYWORDS = ["diabetes", "blood sugar", "glucose"]

def contains_condition(text):
    text = text.lower()
    return any(k in text for k in CONDITION_KEYWORDS)

def main():
    if not Path("filtered_posts.json").exists():
        print("Run earlier pipeline steps first.")
        return

    with open("filtered_posts.json", "r") as f:
        posts = json.load(f)

    condition_posts = [p for p in posts if contains_condition(p["text"])]

    with open("condition_posts.json", "w") as f:
        json.dump(condition_posts, f, indent=4)

    print(f"Found {len(condition_posts)} posts about this condition.")

if __name__ == "__main__":
    main()
