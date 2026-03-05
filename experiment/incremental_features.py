"""
Incremental Features: Lightweight per-window feature extraction for BCFC.

Extracts behavioral features from recent candidate turns only, enabling
the Fidelity Controller to detect drift without processing the full
transcript. Reuses the same extraction logic as behavioral_features.py.
"""

from typing import TYPE_CHECKING
from experiment.behavioral_features import extract_features, BehavioralFeatures

if TYPE_CHECKING:
    from utils.models import Turn


def extract_incremental_features(
    turns: list["Turn"],
    candidate_name: str = "Candidate",
    window_size: int = 4,
) -> BehavioralFeatures:
    """
    Extract behavioral features from the most recent candidate turns.

    Uses the same extraction logic as extract_features() but operates
    on a sliding window of the last `window_size` candidate turns plus
    their surrounding context.

    Args:
        turns: Full conversation turns (all speakers).
        candidate_name: Name of the candidate speaker.
        window_size: Number of recent candidate turns to analyze.

    Returns:
        BehavioralFeatures computed over the recent window.
    """
    # Find indices of candidate turns
    candidate_indices = [
        i for i, t in enumerate(turns)
        if t.speaker_name == candidate_name
    ]

    if not candidate_indices:
        return BehavioralFeatures()

    # Take the last window_size candidate turns
    recent_indices = candidate_indices[-window_size:]

    # Include 1 turn of context before the earliest candidate turn
    start_idx = max(0, recent_indices[0] - 1)

    # Slice turns to the window
    window_turns = turns[start_idx:]

    return extract_features(window_turns, candidate_name)
