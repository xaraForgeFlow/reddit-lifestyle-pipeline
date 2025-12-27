"""
03_run_nli_lfs.py
-----------------
Runs zero-shot NLI scoring for each pillar hypothesis over filtered posts.

Input:
- filtered_posts.json

Output:
- nli_scores.json  (per post, per pillar, aggregated entailment score)
"""

import json
from pathlib import Path
from typing import Dict, Any, List

from config.hypotheses import HYPOTHESES
from config.pillars import Pillar
from nli.nli_runner import NLIRunner


def load_posts(path="filtered_posts.json") -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def aggregate(scores: List[float], method: str = "max") -> float:
    if not scores:
        return 0.0
    if method == "mean":
        return float(sum(scores) / len(scores))
    return float(max(scores))  # default: max


def main():
    in_path = Path("filtered_posts.json")
    if not in_path.exists():
        print("Missing filtered_posts.json. Run 01_coarse_filter.py first.")
        return

    # You can swap models later without changing logic.
    # Common options: "facebook/bart-large-mnli", "roberta-large-mnli"
    model_name = "facebook/bart-large-mnli"
    runner = NLIRunner(model_name=model_name, max_length=256)

    posts = load_posts()
    premises = [(p.get("text") or "") for p in posts]

    out = []
    for idx, post in enumerate(posts):
        out.append({"post_id": post.get("id"), "scores": {}})

    # Score per pillar
    for pillar, hyps in HYPOTHESES.items():
        pillar_scores_per_post: List[float] = [0.0] * len(posts)

        # Combine multiple hypotheses
        all_hyp_scores = []
        for hyp in hyps:
            hyp_scores = runner.score_entailment_batch(premises, hyp, batch_size=32)
            all_hyp_scores.append(hyp_scores)

        # Aggregate across hypotheses per post
        for i in range(len(posts)):
            per_hyp = [all_hyp_scores[h][i] for h in range(len(all_hyp_scores))]
            pillar_scores_per_post[i] = aggregate(per_hyp, method="max")

        # Save
        for i in range(len(posts)):
            out[i]["scores"][pillar.name] = pillar_scores_per_post[i]

        print(f"Scored {pillar.name} with {len(hyps)} hypotheses.")

    with open("nli_scores.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("Done. Saved nli_scores.json")


if __name__ == "__main__":
    main()
