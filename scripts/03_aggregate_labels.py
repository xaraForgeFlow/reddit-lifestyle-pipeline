"""
03_aggregate_labels.py
----------------------

Aggregates LF outputs into multi-label lifestyle annotations.

Input:
- data/lf_outputs/lf_outputs.jsonl

Output:
- data/aggregated_labels.jsonl

Design:
- Multi-label per post
- High recall
- Precision refined later via NLI
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

from config.pillars import Pillar, ABSTAIN

# =========================================================
# Config
# =========================================================

INPUT_PATH = Path("data/lf_outputs/lf_outputs.jsonl")
OUTPUT_PATH = Path("data/aggregated_labels.jsonl")

MIN_LF_VOTES = 2   # >=2 LFs → strong signal
ALLOW_SINGLE_LF = True  # allow 1 LF if no contradiction

# =========================================================
# Helpers
# =========================================================

def aggregate_post(lf_labels: dict) -> list[str]:
    """
    Aggregate LF votes into pillar labels.
    """
    votes = defaultdict(int)

    for lf_name, label in lf_labels.items():
        if label == ABSTAIN:
            continue
        votes[Pillar(label).name] += 1

    assigned = []

    for pillar, count in votes.items():
        if count >= MIN_LF_VOTES:
            assigned.append(pillar)
        elif count == 1 and ALLOW_SINGLE_LF:
            assigned.append(pillar)

    return sorted(set(assigned))


# =========================================================
# Main
# =========================================================

def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    labeled = 0

    with INPUT_PATH.open("r", encoding="utf-8") as fin, \
         OUTPUT_PATH.open("w", encoding="utf-8") as fout:

        for line in fin:
            total += 1
            row = json.loads(line)

            labels = aggregate_post(row["labels"])

            if labels:
                labeled += 1

            fout.write(json.dumps({
                "post_id": row["post_id"],
                "labels": labels
            }) + "\n")

    print("Done.")
    print(f"Labeled posts: {labeled:,} / {total:,}")
    print(f"Coverage: {labeled / max(total, 1):.2%}")


if __name__ == "__main__":
    main()
