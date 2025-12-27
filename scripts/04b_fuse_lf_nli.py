"""
04b_fuse_lf_nli.py
-----------------

Fuses LF-based probabilities with NLI-based probabilities
into final pillar probabilities.

Inputs:
- label_probabilities.json   (from Phase 3)
- nli_scores.json            (from Phase 4)

Output:
- final_probabilities.json
"""

import json
from pathlib import Path


ALPHA = 0.6  # weight for LF-based probabilities


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    lf_probs = load_json("label_probabilities.json")
    nli_scores = load_json("nli_scores.json")

    # nli_scores is a list aligned by post index
    n_posts = len(nli_scores)

    final = []

    for i in range(n_posts):
        fused = {
            "post_id": nli_scores[i]["post_id"],
            "probabilities": {}
        }

        for pillar, lf_values in lf_probs.items():
            p_lf = lf_values[i]
            p_nli = nli_scores[i]["scores"].get(pillar, 0.0)

            p_final = ALPHA * p_lf + (1 - ALPHA) * p_nli
            fused["probabilities"][pillar] = round(p_final, 4)

        final.append(fused)

    out_path = Path("final_probabilities.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(final, f, indent=2)

    print("Done.")
    print(f"Saved fused probabilities to {out_path.resolve()}")


if __name__ == "__main__":
    main()
