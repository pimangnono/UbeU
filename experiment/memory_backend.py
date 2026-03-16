"""
Lightweight memory backend for BCFC v4.

Provides:
- commitment store
- relationship signals
- simple extraction + scoring helpers

Designed to be API-only and laptop-friendly (in-memory).
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Optional


@dataclass
class Commitment:
    commitment_id: str
    type: str
    content: str
    status: str = "open"
    created_turn: int = 0
    due_phase: Optional[str] = None
    counterparty: Optional[str] = None


@dataclass
class RelationshipSignal:
    counterpart: str
    sentiment: str  # positive/negative/neutral
    strength: float = 0.5
    last_turn: int = 0


class MemoryBackend:
    """Abstract memory backend."""

    def append_turn(self, turn_number: int, speaker: str, content: str, phase: str | None = None):
        raise NotImplementedError

    def add_commitments(self, commitments: list[Commitment]):
        raise NotImplementedError

    def resolve_commitment(self, commitment_id: str):
        raise NotImplementedError

    def query_commitments(self, status: str = "open") -> list[Commitment]:
        raise NotImplementedError

    def update_relationship(self, counterpart: str, sentiment: str, strength: float, turn_number: int):
        raise NotImplementedError

    def query_relationships(self) -> list[RelationshipSignal]:
        raise NotImplementedError


class InMemoryBackend(MemoryBackend):
    """Simple in-memory backend for experiments."""

    def __init__(self):
        self.turns: list[dict] = []
        self.commitments: list[Commitment] = []
        self.relationships: dict[str, RelationshipSignal] = {}

    def append_turn(self, turn_number: int, speaker: str, content: str, phase: str | None = None):
        self.turns.append({
            "turn_number": turn_number,
            "speaker": speaker,
            "content": content,
            "phase": phase,
        })

    def add_commitments(self, commitments: list[Commitment]):
        self.commitments.extend(commitments)

    def resolve_commitment(self, commitment_id: str):
        for c in self.commitments:
            if c.commitment_id == commitment_id:
                c.status = "resolved"
                break

    def query_commitments(self, status: str = "open") -> list[Commitment]:
        if status == "all":
            return list(self.commitments)
        return [c for c in self.commitments if c.status == status]

    def update_relationship(self, counterpart: str, sentiment: str, strength: float, turn_number: int):
        existing = self.relationships.get(counterpart)
        if existing:
            # simple momentum update
            if sentiment == existing.sentiment:
                existing.strength = min(1.0, existing.strength + 0.1 * strength)
            elif sentiment != "neutral":
                existing.strength = max(0.0, existing.strength - 0.2 * strength)
                existing.sentiment = sentiment
            existing.last_turn = turn_number
        else:
            self.relationships[counterpart] = RelationshipSignal(
                counterpart=counterpart,
                sentiment=sentiment,
                strength=strength,
                last_turn=turn_number,
            )

    def query_relationships(self) -> list[RelationshipSignal]:
        return list(self.relationships.values())


# ---------------------------------------------------------------------------
# Extraction and scoring helpers
# ---------------------------------------------------------------------------

_COMMITMENT_PATTERNS = [
    r"\bI will\b",
    r"\bI'll\b",
    r"\bwe will\b",
    r"\bwe'll\b",
    r"\bI can\b",
    r"\bwe can\b",
    r"\bwe should\b",
    r"\blet's\b",
    r"\bI can take\b",
    r"\bI'll take\b",
    r"\bI will take\b",
]

_POSITIVE_REL = [
    "good point", "agree", "you're right", "makes sense", "thanks", "appreciate",
    "love that", "great idea", "build on", "aligned",
]
_NEGATIVE_REL = [
    "disagree", "that's wrong", "not true", "no way", "doesn't work", "problem with",
    "push back", "i'd challenge", "i don't think", "i'm not sure",
]


def extract_commitments(text: str, turn_number: int, phase_name: str | None = None) -> list[Commitment]:
    lower = text.lower()
    if not any(re.search(p, text, flags=re.IGNORECASE) for p in _COMMITMENT_PATTERNS):
        return []
    # keep a short fragment as content
    snippet = " ".join(text.strip().split()[:18])
    commitment_id = f"cmt_{turn_number:03d}_{abs(hash(snippet)) % 10000}"
    return [Commitment(
        commitment_id=commitment_id,
        type="action_commitment",
        content=snippet,
        created_turn=turn_number,
        due_phase=phase_name,
    )]


def extract_relationship_signal(text: str) -> Optional[tuple[str, str, float]]:
    lower = text.lower()
    counterparts = ["alex", "jordan", "riley"]
    mentioned = [c for c in counterparts if c in lower]
    if not mentioned:
        return None
    sentiment = "neutral"
    strength = 0.5
    if any(p in lower for p in _POSITIVE_REL):
        sentiment = "positive"
        strength = 0.7
    if any(n in lower for n in _NEGATIVE_REL):
        sentiment = "negative"
        strength = 0.7
    # choose first mentioned counterpart
    return (mentioned[0].title(), sentiment, strength)


def score_commitment_continuity(candidate_text: str, commitments: list[Commitment]) -> float:
    if not commitments:
        return 0.5
    cand_tokens = set(re.findall(r"[a-zA-Z]{3,}", candidate_text.lower()))
    overlaps = []
    for c in commitments:
        ct = set(re.findall(r"[a-zA-Z]{3,}", c.content.lower()))
        if not ct:
            continue
        overlap = len(cand_tokens & ct) / max(1, len(ct))
        overlaps.append(overlap)
    if not overlaps:
        return 0.4
    best = max(overlaps)
    if best > 0.5:
        return 1.0
    if best > 0.25:
        return 0.7
    return 0.5


def detect_commitment_contradiction(candidate_text: str, commitments: list[Commitment]) -> bool:
    if not commitments:
        return False
    lower = candidate_text.lower()
    if not any(neg in lower for neg in ["won't", "can't", "not going to", "no longer"]):
        return False
    cand_tokens = set(re.findall(r"[a-zA-Z]{3,}", lower))
    for c in commitments:
        ct = set(re.findall(r"[a-zA-Z]{3,}", c.content.lower()))
        if cand_tokens & ct:
            return True
    return False


def check_commitment_fulfilled(
    turn_text: str,
    commitment: Commitment,
    min_overlap: float = 0.6,
) -> bool:
    """Return True if *turn_text* fulfils *commitment* (high token overlap, no negation)."""
    lower = turn_text.lower()
    if any(neg in lower for neg in ["won't", "can't", "not going to", "no longer"]):
        return False
    cand_tokens = set(re.findall(r"[a-zA-Z]{3,}", lower))
    ct = set(re.findall(r"[a-zA-Z]{3,}", commitment.content.lower()))
    if not ct:
        return False
    overlap = len(cand_tokens & ct) / len(ct)
    return overlap >= min_overlap


def is_commitment_stale(
    commitment: Commitment,
    current_turn: int,
    max_age: int = 8,
) -> bool:
    """Return True if commitment is older than *max_age* turns."""
    return (current_turn - commitment.created_turn) >= max_age


def format_commitment_context(commitments: list[Commitment]) -> str:
    """Build a concise commitment summary for injection into the generation prompt."""
    if not commitments:
        return ""
    lines = []
    for c in commitments[:5]:
        phase_tag = f" ({c.due_phase})" if c.due_phase else ""
        lines.append(f"- \"{c.content}\"{phase_tag}")
    return (
        "\nYour prior positions:\n"
        + "\n".join(lines)
    )


def score_relationship_consistency(candidate_text: str, relationships: list[RelationshipSignal]) -> float:
    if not relationships:
        return 0.5
    rel_map = {r.counterpart.lower(): r for r in relationships}
    lower = candidate_text.lower()
    mentioned = None
    for name in rel_map:
        if name in lower:
            mentioned = name
            break
    if not mentioned:
        return 0.5
    rel = rel_map[mentioned]
    # infer current sentiment
    current = "neutral"
    if any(p in lower for p in _POSITIVE_REL):
        current = "positive"
    if any(n in lower for n in _NEGATIVE_REL):
        current = "negative"
    if current == "neutral":
        return 0.6
    if current == rel.sentiment:
        return 0.9
    return 0.3


def build_memory_context(mem: MemoryBackend) -> dict:
    return {
        "commitments": mem.query_commitments(status="open"),
        "relationships": mem.query_relationships(),
    }
