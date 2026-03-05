"""
Deterministic trajectory diagnostics for BCFC v1.1.
"""

from __future__ import annotations

import re
from typing import List

from experiment.behavioral_features import STRUCTURE_MARKER_PATTERNS
from utils.models import Turn


_DIRECT_QUESTION_WORDS = [
    "why", "how", "what", "which", "who", "when",
]

_CONTRADICTION_MARKERS = [
    "actually", "on second thought", "i take that back", "scratch that",
    "i was wrong", "i retract", "correction",
]

_URGENCY_MARKERS = [
    "urgent", "asap", "immediately", "right now", "time pressure",
    "deadline", "due", "today", "tonight", "in 30 minutes", "now",
    "escalate", "critical", "emergency", "crisis",
]


def _last_non_candidate(turns: List[Turn], candidate_name: str = "Candidate") -> Turn | None:
    for t in reversed(turns):
        if t.speaker_name != candidate_name:
            return t
    return None


def compute_direct_question_answer_rate(turns: List[Turn], candidate_name: str = "Candidate") -> float:
    asked = 0
    answered = 0
    for i, t in enumerate(turns):
        if t.speaker_name != candidate_name and "?" in t.content:
            asked += 1
            # Find next candidate turn
            for j in range(i + 1, len(turns)):
                if turns[j].speaker_name == candidate_name:
                    response = turns[j].content
                    if len(response.split()) >= 6:
                        answered += 1
                    break
    return answered / max(asked, 1)


def compute_contradiction_rate(turns: List[Turn], candidate_name: str = "Candidate") -> float:
    candidate_turns = [t for t in turns if t.speaker_name == candidate_name]
    if len(candidate_turns) < 2:
        return 0.0

    contradictions = 0
    for t in candidate_turns[1:]:
        text = t.content.lower()
        if any(m in text for m in _CONTRADICTION_MARKERS):
            contradictions += 1
    return contradictions / max(len(candidate_turns), 1)


def compute_unsolicited_structure_rate(turns: List[Turn], candidate_name: str = "Candidate") -> float:
    candidate_turns = [t for t in turns if t.speaker_name == candidate_name]
    if not candidate_turns:
        return 0.0

    unsolicited = 0
    for t in candidate_turns:
        text = t.content.lower()
        if any(re.search(p, text) for p in STRUCTURE_MARKER_PATTERNS):
            asked = False
            # Check if any of last 2 non-candidate turns asked for structure
            for prior in turns:
                if prior.turn_number >= t.turn_number:
                    break
                if prior.speaker_name != candidate_name:
                    if any(w in prior.content.lower() for w in ["list", "outline", "organize", "structure", "steps"]):
                        asked = True
            if not asked:
                unsolicited += 1
    return unsolicited / max(len(candidate_turns), 1)


def compute_over_verbosity_rate(turns: List[Turn], candidate_name: str = "Candidate", threshold: int = 90) -> float:
    candidate_turns = [t for t in turns if t.speaker_name == candidate_name]
    if not candidate_turns:
        return 0.0
    too_long = sum(1 for t in candidate_turns if len(t.content.split()) > threshold)
    return too_long / max(len(candidate_turns), 1)


def compute_stress_index(turns: List[Turn]) -> float:
    """Deterministic stress index based on urgency markers."""
    if not turns:
        return 0.0
    total = 0
    hits = 0
    for t in turns:
        total += 1
        text = t.content.lower()
        if any(m in text for m in _URGENCY_MARKERS):
            hits += 1
    return hits / max(total, 1)

