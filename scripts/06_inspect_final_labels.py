"""
06_inspect_final_labels.py
--------------------------

Quick inspection of final fused labels.
Prints counts and a few example post IDs per pillar.
"""

import json
from collections import defaultdict
from pathlib import Path

FINAL_PATH = Path("data/final_labels.jsonl")
N_EXAMPLES = 5


def main():
    buckets = defaultdict(list)

    with FINAL_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            for label in row["labels"]:
                buckets[label].append(row["post_id"])

    print("Label counts:")
    for label, posts in buckets.items():
        print(f"{label:<10} {len(posts):,}")

    print("\nSample post_ids per label:")
    for label, posts in buckets.items():
        print(f"\n{label}:")
        for pid in posts[:N_EXAMPLES]:
            print(f"  {pid}")


if __name__ == "__main__":
    main()
