"""
02_run_lfs.py
--------------

Runs all labeling functions (LFs) over filtered Reddit posts
and produces an LF label matrix.

Inputs:
- filtered_posts.json

Outputs:
- lf_outputs.json (readable)
- lf_matrix.npy (numeric matrix)
"""

import json
import importlib
import inspect
from pathlib import Path

import numpy as np

from config.pillars import ABSTAIN


# =========================================================
# Load posts
# =========================================================

def load_posts(path="data/pilot_filtered_posts.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================================================
# Discover labeling functions
# =========================================================

def load_labeling_functions():
    lf_dir = Path("lfs")
    lf_functions = []

    for lf_file in lf_dir.glob("*.py"):
        module_name = f"lfs.{lf_file.stem}"
        module = importlib.import_module(module_name)

        for name, func in inspect.getmembers(module, inspect.isfunction):
            if name.startswith("lf_"):
                lf_functions.append(func)

    return lf_functions


# =========================================================
# Run LFs
# =========================================================

def run_lfs(posts, lf_functions):
    lf_outputs = []
    matrix = np.full((len(posts), len(lf_functions)), ABSTAIN, dtype=int)

    for i, post in enumerate(posts):
        row = {}
        for j, lf in enumerate(lf_functions):
            try:
                label = lf(post)
            except Exception:
                label = ABSTAIN

            matrix[i, j] = int(label)
            row[lf.__name__] = int(label)

        lf_outputs.append({
            "post_id": post.get("id"),
            "labels": row
        })

    return lf_outputs, matrix


# =========================================================
# Save outputs
# =========================================================

def save_outputs(lf_outputs, matrix):
    with open("lf_outputs.json", "w", encoding="utf-8") as f:
        json.dump(lf_outputs, f, indent=2)

    np.save("lf_matrix.npy", matrix)


# =========================================================
# Main
# =========================================================

def main():
    print("Loading posts...")
    posts = load_posts()

    print("Discovering labeling functions...")
    lf_functions = load_labeling_functions()
    print(f"Found {len(lf_functions)} labeling functions.")

    print("Running labeling functions...")
    lf_outputs, matrix = run_lfs(posts, lf_functions)

    print("Saving outputs...")
    save_outputs(lf_outputs, matrix)

    print("Done.")
    print(f"LF matrix shape: {matrix.shape}")


if __name__ == "__main__":
    main()
