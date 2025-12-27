"""
05_sampling_and_eval.py
----------------------

Creates representative evaluation samples for manual annotation using:
1. High-entropy (uncertain) sampling
2. Pillar disagreement sampling
3. Rare-pillar oversampling

Outputs annotation-ready CSV files.
"""

import json
import math
import random
import csv
from pathlib import Path
from typing import List, Dict


# -----------------------
# Config
# -----------------------

N_ENTROPY = 200
N_DISAGREE = 200
N_RARE = 200

RARE_PILLARS = {
    "PURPOSE",
    "NATURE",
    "RISK",
}

OUTPUT_DIR = Path("sampling")
OUTPUT_DIR.mkdir(exist_ok=True)


# -----------------------
# Helpers
# -----------------------

def entropy(probs: Dict[str, float]) -> float:
    """Shannon entropy over pillar probabilities."""
    eps = 1e-12
    return -sum(p * math.log(p + eps) for p in probs.values())


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_csv(path: Path, rows: List[Dict]):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


# -----------------------
# Sampling strategies
# -----------------------

def sample_high_entropy(posts, probs, n):
    scored = []
    for post, prob in zip(posts, probs):
        e = entropy(prob["probabilities"])
        scored.append((e, post, prob))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:n]


def sample_disagreement(posts, probs, n):
    scored = []
    for post, prob in zip(posts, probs):
        values = list(prob["probabilities"].values())
        if len(values) < 2:
            continue
        gap = abs(sorted(values, reverse=True)[0] - sorted(values, reverse=True)[1])
        scored.append((gap, post, prob))
    scored.sort(key=lambda x: x[0])  # small gap = disagreement
    return scored[:n]


def sample_rare_pillars(posts, probs, n):
    selected = []
    for post, prob in zip(posts, probs):
        for pillar in RARE_PILLARS:
            if prob["probabilities"].get(pillar, 0) > 0.6:
                selected.append((post, prob))
                break
    random.shuffle(selected)
    return selected[:n]


# -----------------------
# Main
# -----------------------

def main():
    if not Path("final_probabilities.json").exists():
        print("Run pipeline up to Phase 4.5 first.")
        return

    posts = load_json("filtered_posts.json")
    probs = load_json("final_probabilities.json")

    # --- Sampling ---
    entropy_samples = sample_high_entropy(posts, probs, N_ENTROPY)
    disagree_samples = sample_disagreement(posts, probs, N_DISAGREE)
    rare_samples = sample_rare_pillars(posts, probs, N_RARE)

    # --- Format rows ---
    def format_row(post, prob):
        row = {
            "post_id": post.get("id"),
            "text": post.get("text"),
            "subreddit": post.get("subreddit"),
        }
        for pillar, p in prob["probabilities"].items():
            row[f"pred_{pillar}"] = round(p, 3)
            row[f"label_{pillar}"] = ""  # for human annotation
        row["comments"] = ""
        return row

    entropy_rows = [format_row(p, pr) for _, p, pr in entropy_samples]
    disagree_rows = [format_row(p, pr) for _, p, pr in disagree_samples]
    rare_rows = [format_row(p, pr) for p, pr in rare_samples]

    # --- Write CSVs ---
    write_csv(OUTPUT_DIR / "eval_entropy.csv", entropy_rows)
    write_csv(OUTPUT_DIR / "eval_disagreement.csv", disagree_rows)
    write_csv(OUTPUT_DIR / "eval_rare_pillars.csv", rare_rows)

    # Combined master file
    write_csv(
        OUTPUT_DIR / "eval_master.csv",
        entropy_rows + disagree_rows + rare_rows,
    )

    print("Sampling complete.")
    print("Files written to /sampling")


if __name__ == "__main__":
    main()
