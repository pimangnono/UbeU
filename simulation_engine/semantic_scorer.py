"""Local embedding-based supplementary scoring for stakeholder simulations.

Uses sentence-transformers (all-MiniLM-L6-v2, 80M params, CPU-only, deterministic)
to add semantic similarity signals that augment existing keyword-based scoring.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer


# Canonical trait pole prototype sentences (NOT scenario-specific)
TRAIT_PROTOTYPE_SENTENCES = {
    "O": {
        "high": (
            "What if we tried a completely different approach? Let me reframe this problem. "
            "There's an interesting tradeoff we haven't explored. Consider this alternative."
        ),
        "low": (
            "Let's stick with what's proven. The data supports the standard approach. "
            "We should verify with evidence before changing anything. Start small and validate."
        ),
    },
    "C": {
        "high": (
            "I'll take ownership of this. First we do X, then Y. Let me set a deadline. "
            "Who is responsible for each step? We need a structured plan with clear accountability."
        ),
        "low": (
            "Let's stay flexible and adapt as we go. We can iterate on this. "
            "No need to lock everything down yet. Take a lightweight approach first."
        ),
    },
}

# Sentiment prototype sentences for relationship scoring
SENTIMENT_PROTOTYPES = {
    "positive": (
        "I agree with your approach. That's a great point. "
        "Your proposal makes sense and I support moving forward with it. "
        "I appreciate your perspective and think we're aligned."
    ),
    "negative": (
        "I fundamentally disagree. This approach is wrong and dangerous. "
        "I reject this proposal. It threatens our core interests. "
        "This is unacceptable and I refuse to support it."
    ),
    "challenging": (
        "I see your point, but I have serious reservations. "
        "While I understand the rationale, the risks haven't been addressed. "
        "I need more evidence before I can support this. My position hasn't changed."
    ),
}


class SemanticScorer:
    """Local embedding-based supplementary scoring. Deterministic."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self._cache: dict[str, np.ndarray] = {}

    def _embed(self, text: str) -> np.ndarray:
        if text not in self._cache:
            self._cache[text] = self.model.encode(text, normalize_embeddings=True)
        return self._cache[text]

    def clear_response_cache(self) -> None:
        """Clear cached response embeddings between runs to prevent memory leak.

        Preserves prototype embeddings (identity:*, trait:*, sentiment prototypes)
        which are small and reused across runs.
        """
        prototype_prefixes = ("identity:", "trait:")
        prototype_keys = {
            k for k in self._cache
            if k.startswith(prototype_prefixes) or k in (
                SENTIMENT_PROTOTYPES["positive"],
                SENTIMENT_PROTOTYPES["negative"],
                SENTIMENT_PROTOTYPES["challenging"],
            )
        }
        self._cache = {k: v for k, v in self._cache.items() if k in prototype_keys}
        # Free MPS/CUDA tensor memory
        try:
            import torch
            if hasattr(torch, "mps") and hasattr(torch.mps, "empty_cache"):
                torch.mps.empty_cache()
        except ImportError:
            pass

    def _cosine(self, a: np.ndarray, b: np.ndarray) -> float:
        return float(np.dot(a, b))  # already normalized

    # ── Area 1: Identity Consistency ──

    def init_for_actor(self, actor_spec: Any) -> None:
        """Pre-compute prototype embeddings at simulation init (once per actor)."""
        identity_text = (
            f"{actor_spec.role}. "
            f"{'. '.join(actor_spec.incentives)}. "
            f"{'. '.join(actor_spec.concerns)}"
        )
        self._cache[f"identity:{actor_spec.actor_id}"] = self._embed(identity_text)

        # Trait pole prototypes
        for trait, pole_texts in TRAIT_PROTOTYPE_SENTENCES.items():
            prior = actor_spec.personality_prior.get(trait, 0.5)
            if prior >= 0.55:
                pole = "high"
            elif prior <= 0.45:
                pole = "low"
            else:
                continue
            self._cache[f"trait:{actor_spec.actor_id}:{trait}:{pole}"] = self._embed(pole_texts[pole])

    def identity_similarity(self, actor_id: str, response_text: str) -> float:
        """Cosine similarity between response and actor identity prototype."""
        key = f"identity:{actor_id}"
        if key not in self._cache:
            return 0.5
        return self._cosine(self._embed(response_text), self._cache[key])

    # ── Area 2: Trait Target Alignment ──

    def trait_alignment(self, actor_id: str, response_text: str, trait: str, pole: str) -> float:
        """Cosine similarity between response and trait pole prototype."""
        key = f"trait:{actor_id}:{trait}:{pole}"
        if key not in self._cache:
            return 0.5
        return self._cosine(self._embed(response_text), self._cache[key])

    # ── Area 3: Relationship Sentiment ──

    def sentiment_score(self, text: str) -> dict[str, float]:
        """Score text against positive/negative/challenging prototypes."""
        text_emb = self._embed(text)
        return {
            "positive": self._cosine(text_emb, self._embed(SENTIMENT_PROTOTYPES["positive"])),
            "negative": self._cosine(text_emb, self._embed(SENTIMENT_PROTOTYPES["negative"])),
            "challenging": self._cosine(text_emb, self._embed(SENTIMENT_PROTOTYPES["challenging"])),
        }
