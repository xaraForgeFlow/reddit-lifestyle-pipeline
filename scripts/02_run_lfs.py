import json
import importlib
import inspect
from pathlib import Path
from collections import Counter, defaultdict

import numpy as np

from config.pillars import ABSTAIN
from config.lf_allowlist import LF_ALLOWLIST

# =========================================================
# Config
# =========================================================

INPUT_PATH = Path("data/pilot_filtered_posts.jsonl")
OUTPUT_DIR = Path("data/lf_outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# Load posts (JSONL streaming)
# =========================================================

def iter_posts(path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)

# =========================================================
# Discover labeling functions
# =========================================================

def load_labeling_functions():
    lf_dir = Path("lfs")
    lf_functions = []

    for lf_file in sorted(lf_dir.glob("*.py")):
        module_name = f"lfs.{lf_file.stem}"
        module = importlib.import_module(module_name)

        for name, func in inspect.getmembers(module, inspect.isfunction):
            if name.startswith("lf_") and name in LF_ALLOWLIST:
                lf_functions.append(func)

    lf_functions.sort(key=lambda f: f.__name__)
    return lf_functions

# =========================================================
# Run LFs
# =========================================================

def run_lfs():
    lf_functions = load_labeling_functions()
    print(f"Found {len(lf_functions)} labeling functions.")

    lf_stats = Counter()
    lf_abstains = Counter()

    outputs_path = OUTPUT_DIR / "lf_outputs.jsonl"
    matrix_path = OUTPUT_DIR / "lf_matrix.npy"

    rows = []

    with outputs_path.open("w", encoding="utf-8") as fout:
        for i, post in enumerate(iter_posts(INPUT_PATH)):
            labels = []

            for lf in lf_functions:
                try:
                    label = lf(post)
                except Exception:
                    label = ABSTAIN

                labels.append(label)

                if label == ABSTAIN:
                    lf_abstains[lf.__name__] += 1
                else:
                    lf_stats[lf.__name__] += 1

            rows.append(labels)

            fout.write(json.dumps({
                "post_id": post.get("id"),
                "labels": dict(zip([lf.__name__ for lf in lf_functions], labels))
            }) + "\n")

            if (i + 1) % 10_000 == 0:
                print(f"Processed {i + 1:,} posts")

    matrix = np.array(rows, dtype=int)
    np.save(matrix_path, matrix)

    return lf_functions, matrix, lf_stats, lf_abstains

# =========================================================
# Main
# =========================================================

def main():
    lf_functions, matrix, stats, abstains = run_lfs()

    print("Done.")
    print(f"LF matrix shape: {matrix.shape}")

    print("\nLF coverage:")
    for lf in lf_functions:
        name = lf.__name__
        fired = stats[name]
        abst = abstains[name]
        print(f"{name:30s} fired={fired:6d} abstained={abst:6d}")

if __name__ == "__main__":
    main()
