"""
05_fuse_lf_nli.py
-----------------

Fuse LF-based aggregated labels with NLI validation scores.

Logic:
- LFs propose candidate lifestyle pillars
- NLI validates each pillar via entailment score
- Keep pillar if NLI score >= threshold

Output:
- final_labels.jsonl
"""

import json
from pathlib import Path
from collections import Counter

# =========================================================
# Config
# =========================================================

AGG_LABELS_PATH = Path("data/aggregated_labels.jsonl")
NLI_PATH = Path("data/nli_validated_labels.jsonl")
OUTPUT_PATH = Path("data/final_labels.jsonl")

NLI_THRESHOLD = 0.75  # adjust later if needed

# =========================================================
# Load helpers
# =========================================================

def load_jsonl(path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# =========================================================
# Main
# =========================================================

def main():
    print("Loading aggregated LF labels...")
    agg = {
        row["post_id"]: row["labels"]
        for row in load_jsonl(AGG_LABELS_PATH)
    }

    print("Loading NLI validation scores...")
    nli = {
        row["post_id"]: row["nli_scores"]
        for row in load_jsonl(NLI_PATH)
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    kept_posts = 0
    label_counter = Counter()

    print("Fusing LF + NLI...")
    with OUTPUT_PATH.open("w", encoding="utf-8") as fout:
        for post_id, lf_labels in agg.items():
            nli_scores = nli.get(post_id)
            if not nli_scores:
                continue

            final_labels = []

            for pillar in lf_labels:
                score = nli_scores.get(pillar)
                if score is not None and score >= NLI_THRESHOLD:
                    final_labels.append(pillar)
                    label_counter[pillar] += 1

            if final_labels:
                fout.write(json.dumps({
                    "post_id": post_id,
                    "labels": final_labels
                }) + "\n")
                kept_posts += 1

    print("Done.")
    print(f"Final labeled posts: {kept_posts:,}")
    print("Label distribution:")
    for k, v in label_counter.most_common():
        print(f"  {k:<12} {v:,}")

    print(f"Output → {OUTPUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
