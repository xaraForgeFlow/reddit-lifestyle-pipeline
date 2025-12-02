"""
05_sampling_and_eval.py
------------------------

Creates a small evaluation set using:
- random sampling
- LF-based sampling
- NLI-based sampling

"""

import json
import random
from pathlib import Path

def main():
    if not Path("pillar_probs.json").exists():
        print("Run 04_fit_label_model.py first.")
        return

    with open("filtered_posts.json", "r") as f:
        posts = json.load(f)

    with open("pillar_probs.json", "r") as f:
        probs = json.load(f)

    # Random 2 posts as example
    random_sample = random.sample(posts, k=min(2, len(posts)))

    # Save evaluation sample
    with open("eval_sample.json", "w") as f:
        json.dump(random_sample, f, indent=4)

    print("Saved small eval sample.")

if __name__ == "__main__":
    main()
