import json
from pathlib import Path
from typing import Dict, List, Any, Tuple

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def softmax_entailment_scores(logits, entailment_id: int) -> List[float]:
    probs = torch.softmax(logits, dim=-1)
    return probs[:, entailment_id].detach().cpu().tolist()


class NLIRunner:
    """
    Zero-shot NLI runner for entailment scoring:
    premise = post text
    hypothesis = hypothesis string
    score = P(entailment)
    """

    def __init__(self, model_name: str, device: str = None, max_length: int = 256):
        self.model_name = model_name
        self.max_length = max_length

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device)

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)
        self.model.eval()

        # Most MNLI models use labels: contradiction, neutral, entailment (order varies sometimes)
        # We'll infer entailment index from config if present; otherwise assume MNLI standard.
        label2id = getattr(self.model.config, "label2id", None) or {}
        if "ENTAILMENT" in label2id:
            self.entailment_id = int(label2id["ENTAILMENT"])
        else:
            # Common default for MNLI heads: [contradiction=0, neutral=1, entailment=2]
            self.entailment_id = 2

    @torch.no_grad()
    def score_entailment_batch(self, premises: List[str], hypothesis: str, batch_size: int = 32) -> List[float]:
        scores: List[float] = []
        for i in range(0, len(premises), batch_size):
            batch_premises = premises[i:i + batch_size]
            enc = self.tokenizer(
                batch_premises,
                [hypothesis] * len(batch_premises),
                truncation=True,
                padding=True,
                max_length=self.max_length,
                return_tensors="pt",
            ).to(self.device)

            logits = self.model(**enc).logits
            scores.extend(softmax_entailment_scores(logits, self.entailment_id))
        return scores
