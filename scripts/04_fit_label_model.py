"""
04_fit_label_model.py
---------------------

Fits per-pillar label models using weak supervision.
Takes LF matrix as input and outputs probabilistic labels.

Inputs:
- lf_matrix.npy

Outputs:
- label_probabilities.json
"""

import json
import numpy as np
from pathlib import Path

from snorkel.labeling import LabelModel

from config.pillars import Pillar, ABSTAIN


# =========================================================
# Load LF matrix
# =========================================================

def load_lf_matrix(path="lf_matrix.npy"):
    return np.load(path)


# =========================================================
# Convert LF matrix to binary view for a pillar
# =========================================================

def make_binary_matrix(lf_matrix, pillar_value):
    """
    Converts multiclass LF matrix to binary:
    1 = this pillar
    0 = not this pillar
    -1 = abstain
    """
    binary = np.full_like(lf_matrix, ABSTAIN)

    binary[lf_matrix == pillar_value] = 1
    binary[(lf_matrix != pillar_value) & (lf_matrix != ABSTAIN)] = 0

    return binary


# =========================================================
# Fit label model for one pillar
# =========================================================

def fit_label_model(binary_matrix):
    label_model = LabelModel(cardinality=2, verbose=False)
    label_model.fit(
        binary_matrix,
        n_epochs=500,
        lr=0.01,
        log_freq=0,
    )
    return label_model


# =========================================================
# Main
# =========================================================

def main():
    print("Loading LF matrix...")
    lf_matrix = load_lf_matrix()

    results = {}

    for pillar in Pillar:
        if pillar == Pillar.NOT_LIFESTYLE:
            continue

        print(f"Fitting label model for {pillar.name}...")

        binary_matrix = make_binary_matrix(lf_matrix, int(pillar))
        label_model = fit_label_model(binary_matrix)

        probs = label_model.predict_proba(binary_matrix)
        results[pillar.name] = probs[:, 1].tolist()

    output_path = Path("label_probabilities.json")
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("Done.")
    print(f"Saved probabilities to {output_path.resolve()}")


if __name__ == "__main__":
    main()
