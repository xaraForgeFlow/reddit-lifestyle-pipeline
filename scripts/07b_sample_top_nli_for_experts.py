"""
07b_sample_top_nli_for_experts.py
---------------------------------

Select top-N highest-confidence posts per pillar
based on NLI entailment scores, for expert labeling.
"""

import json
import csv
from pathlib import Path
from collections import defaultdict

# =========================================================
# Config
# =========================================================

FINAL_LABELS = Path("data/final_labels.jsonl")
NLI_PATH = Path("data/nli_validated_labels.jsonl")
POSTS_PATH = Path("data/pilot_filtered_posts.jsonl")

OUTPUT_CSV = Path("data/manual_labeling_top_nli.csv")

TOP_K_PER_LABEL = 200

# =========================================================
# Helpers
# =========================================================

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


def load_jsonl(path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# =========================================================
# Main
# =========================================================

def main():
    print("Loading posts...")
    posts = load_posts()

    print("Loading final fused labels...")
    final_labels = {
        row["post_id"]: row["labels"]
        for row in load_jsonl(FINAL_LABELS)
    }

    print("Loading NLI scores...")
    nli_scores = {
        row["post_id"]: row["nli_scores"]
        for row in load_jsonl(NLI_PATH)
    }

    # Collect (post_id, score) per pillar
    pillar_buckets = defaultdict(list)

    for post_id, labels in final_labels.items():
        scores = nli_scores.get(post_id)
        if not scores:
            continue

        for pillar in labels:
            score = scores.get(pillar)
            if score is not None:
                pillar_buckets[pillar].append((post_id, score))

    print("Selecting top-N per pillar...")
    sampled_rows = []

    for pillar, items in pillar_buckets.items():
        # sort by NLI score desc
        items_sorted = sorted(items, key=lambda x: x[1], reverse=True)
        top_items = items_sorted[:TOP_K_PER_LABEL]

        print(f"{pillar}: selected {len(top_items)}")

        for post_id, score in top_items:
            post = posts.get(post_id)
            if not post:
                continue

            sampled_rows.append({
                "post_id": post_id,
                "pillar": pillar,
                "nli_score": round(score, 4),
                "text": normalize_text(post),
                "expert_label": "",   # to be filled
                "notes": ""
            })

    print(f"Writing CSV → {OUTPUT_CSV}")
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "post_id",
                "pillar",
                "nli_score",
                "text",
                "expert_label",
                "notes",
            ]
        )
        writer.writeheader()
        writer.writerows(sampled_rows)

    print(f"Done. Total rows: {len(sampled_rows)}")


if __name__ == "__main__":
    main()
