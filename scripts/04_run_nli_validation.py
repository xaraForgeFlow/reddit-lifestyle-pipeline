"""
04_run_nli_validation.py
-----------------------

Validates rule-based aggregated lifestyle labels using NLI.

For each post:
- Take candidate pillars from aggregated labels
- Run NLI on ALL hypotheses for each pillar
- Use the MAX entailment score per pillar

LFs propose → NLI validates.
"""

import json
from pathlib import Path
from typing import Dict, List

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from config.hypotheses import HYPOTHESES
from config.pillars import Pillar

# =========================================================
# Config
# =========================================================

POSTS_PATH = Path("data/pilot_filtered_posts.jsonl")
AGG_LABELS_PATH = Path("data/aggregated_labels.jsonl")
OUTPUT_PATH = Path("data/nli_validated_labels.jsonl")

MODEL_NAME = "facebook/bart-large-mnli"
MAX_LENGTH = 512
BATCH_SIZE = 8
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# =========================================================
# Helpers
# =========================================================

def load_posts() -> Dict[str, dict]:
    """
    Load posts into dict keyed by post_id.
    Supports JSON array or JSONL.
    """
    posts = {}

    with POSTS_PATH.open("r", encoding="utf-8") as f:
        first_char = f.read(1)
        f.seek(0)

        if first_char == "[":
            data = json.load(f)
            for p in data:
                posts[str(p.get("id"))] = p
        else:
            for line in f:
                if not line.strip():
                    continue
                p = json.loads(line)
                posts[str(p.get("id"))] = p

    return posts


def normalize_text(post: dict) -> str:
    """
    Combine title + body safely.
    """
    title = post.get("title", "") or ""
    body = post.get("selftext", "") or post.get("text", "") or ""
    return f"{title}\n{body}".strip()


def batched(lst: List[str], n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

# =========================================================
# NLI Runner
# =========================================================

class NLIRunner:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.model.to(DEVICE)
        self.model.eval()

        self.entailment_idx = self.model.config.label2id["entailment"]

    @torch.no_grad()
    def score_batch(self, premises: List[str], hypotheses: List[str]) -> List[float]:
        """
        Score a batch of (premise, hypothesis) pairs.
        """
        inputs = self.tokenizer(
            premises,
            hypotheses,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_LENGTH,
        ).to(DEVICE)

        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)
        return probs[:, self.entailment_idx].tolist()

# =========================================================
# Main
# =========================================================

def main():
    print(f"Loading posts from {POSTS_PATH}")
    posts = load_posts()

    print("Loading aggregated labels...")
    with AGG_LABELS_PATH.open("r", encoding="utf-8") as f:
        agg_rows = [json.loads(line) for line in f]

    runner = NLIRunner()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    processed_posts = 0
    evaluated_pairs = 0

    with OUTPUT_PATH.open("w", encoding="utf-8") as fout:
        for row in agg_rows:
            post_id = str(row.get("post_id"))
            candidate_pillars = row.get("labels", [])

            post = posts.get(post_id)
            if not post or not candidate_pillars:
                continue

            text = normalize_text(post)

            result = {
                "post_id": post_id,
                "nli_scores": {}
            }

            for pillar_str in candidate_pillars:
                try:
                    pillar_enum = Pillar[pillar_str]
                except KeyError:
                    continue

                hypotheses = HYPOTHESES.get(pillar_enum)
                if not hypotheses:
                    continue

                scores = []

                for hyp_batch in batched(hypotheses, BATCH_SIZE):
                    premises = [text] * len(hyp_batch)
                    batch_scores = runner.score_batch(premises, hyp_batch)
                    scores.extend(batch_scores)
                    evaluated_pairs += len(batch_scores)

                # Max entailment = strongest support
                result["nli_scores"][pillar_str] = round(max(scores), 4)

            fout.write(json.dumps(result) + "\n")
            processed_posts += 1

            if processed_posts % 1000 == 0:
                print(f"Processed {processed_posts:,} posts")

    print("Done.")
    print(f"Processed posts: {processed_posts:,}")
    print(f"Evaluated (post, hypothesis) pairs: {evaluated_pairs:,}")
    print(f"Output → {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
