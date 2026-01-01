"""
07_sample_for_manual_labeling.py
--------------------------------

Randomly sample posts per pillar for expert manual labeling.
Outputs a CSV that non-technical experts can use.
"""

import json
import random
import csv
from pathlib import Path
from collections import defaultdict

# ======================
# Config
# ======================

FINAL_LABELS = Path("data/final_labels.jsonl")
POSTS_PATH = Path("data/pilot_filtered_posts.jsonl")
OUTPUT_CSV = Path("data/manual_labeling_sample.csv")

SAMPLES_PER_LABEL = 200   # adjust (e.g. 100–300)
RANDOM_SEED = 42

# ======================
# Helpers
# ======================

def normalize_text(post):
    title = post.get("title", "") or ""
    body = post.get("selftext", "") or post.get("text", "") or ""
    return f"{title}\n\n{body}".strip()


def load_posts():
    posts = {}
    with POSTS_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                p = json.loads(line)
                posts[str(p.get("id"))] = p
    return posts


# ======================
# Main
# ======================

def main():
    random.seed(RANDOM_SEED)

    print("Loading posts...")
    posts = load_posts()

    print("Loading final labels...")
    label_buckets = defaultdict(list)

    with FINAL_LABELS.open("r", encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            for label in row["labels"]:
                label_buckets[label].append(row["post_id"])

    sampled_rows = []

    for label, post_ids in label_buckets.items():
        n = min(SAMPLES_PER_LABEL, len(post_ids))
        sampled = random.sample(post_ids, n)

        print(f"Sampling {n} posts for {label}")

        for pid in sampled:
            post = posts.get(pid)
            if not post:
                continue

            sampled_rows.append({
                "post_id": pid,
                "proposed_label": label,
                "text": normalize_text(post),
                "expert_label": "",        # to be filled
                "notes": ""                # optional
            })

    print(f"Writing CSV → {OUTPUT_CSV}")
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["post_id", "proposed_label", "text", "expert_label", "notes"]
        )
        writer.writeheader()
        writer.writerows(sampled_rows)

    print(f"Done. Total samples: {len(sampled_rows)}")


if __name__ == "__main__":
    main()
