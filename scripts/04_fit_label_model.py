"""
04_fit_label_model.py
--------------------

Combines LF outputs + NLI scores
and generates pillar probabilities.

Later, replace with:
- Snorkel LabelModel
- real probabilistic aggregation
"""

import json
from pathlib import Path

from config.pillars import Pillar

def make_fake_probability(lf_outputs, nli_score):
    """
    Placeholder for real label model.
    For now:
    - If LF or NLI fires strongly → high probability
    - Else → low probability
    """
    if max(lf_outputs) == Pillar.SLEEP or nli_score > 0.7:
        return {"sleep": 0.85, "stress": 0.2, "diet": 0.1}
    return {"sleep": 0.1, "stress": 0.1, "diet": 0.1}

def main():
    if not Path("lf_outputs.json").exists():
        print("Run 02_run_lfs.py first.")
        return
    if not Path("nli_outputs.json").exists():
        print("Run 03_run_nli_lfs.py first.")
        return

    with open("lf_outputs.json", "r", encoding="utf-8") as f:
        lfs = json.load(f)
    with open("nli_outputs.json", "r", encoding="utf-8") as f:
        nlis = json.load(f)

    nli_map = {item["id"]: item["nli_sleep_score"] for item in nlis}

    results = []
    for item in lfs:
        pid = item["id"]
        nli_score = nli_map.get(pid, 0)
        lf_outputs = item["lf_outputs"]
        probs = make_fake_probability(lf_outputs, nli_score)
        results.append({"id": pid, "probs": probs})

    with open("pillar_probs.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("Saved fake pillar probabilities.")

if __name__ == "__main__":
    main()
