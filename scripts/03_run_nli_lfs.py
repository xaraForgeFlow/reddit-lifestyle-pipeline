import json
from pathlib import Path

def fake_nli_score(text, hypothesis):
    """Simulated NLI score. Replace with real HF call later."""
    if "sleep" in text.lower() and "sleep" in hypothesis.lower():
        return 0.85
    return 0.10

def main():
    if not Path("filtered_posts.json").exists():
        print("Run 01_coarse_filter.py first.")
        return

    with open("filtered_posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)

    H_SLEEP = "The writer is struggling with sleep problems."

    nli_results = []
    for post in posts:
        score = fake_nli_score(post["text"], H_SLEEP)
        nli_results.append({
            "id": post["id"],
            "nli_sleep_score": score
        })

    with open("nli_outputs.json", "w", encoding="utf-8") as f:
        json.dump(nli_results, f, indent=4)

    print("Generated dummy NLI scores.")

if __name__ == "__main__":
    main()
