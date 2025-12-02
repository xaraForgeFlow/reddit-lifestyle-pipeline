import json
from pathlib import Path

# Import all LFs
from lfs.sleep import lf_sleep_insomnia, lf_sleep_schedule, lf_sleep_subreddit
# Later: import diet, stress, social, etc.

ALL_LFS = [
    lf_sleep_insomnia,
    lf_sleep_schedule,
    lf_sleep_subreddit,
]

def run_lfs_on_post(post):
    """Return list of LF outputs for one post."""
    return [lf(post) for lf in ALL_LFS]

def main():
    if not Path("filtered_posts.json").exists():
        print("Run 01_coarse_filter.py first.")
        return

    with open("filtered_posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)

    results = []
    for post in posts:
        lf_output = run_lfs_on_post(post)
        results.append({
            "id": post["id"],
            "lf_outputs": lf_output
        })

    with open("lf_outputs.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"Processed {len(results)} posts with {len(ALL_LFS)} LFs.")

if __name__ == "__main__":
    main()
