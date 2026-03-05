"""
Overlap Audit: Detect instruction-evaluation phrase leakage.

Categorizes overlaps as:
- Hard: multi-word phrases (>= 2 tokens) or single words not in the soft allowlist.
  Hard overlaps MUST be zero before experiment runs.
- Soft: single-word overlaps on the allowlist (semantically broad words like "plan").
  Soft overlaps are logged but do not block runs.
"""

from experiment.profiles import BEHAVIORAL_INSTRUCTIONS
from experiment.behavioral_features import (
    HEDGE_PHRASES, CERTAINTY_PHRASES, DISAGREEMENT_PHRASES,
    ACKNOWLEDGMENT_PHRASES, IDEA_PHRASES, PLANNING_PHRASES,
    EMOTIONAL_WORDS, POSITIVE_EMOTION_WORDS,
    REFERENCE_BACK_PHRASES, ACTION_ITEM_PHRASES,
    HYPOTHETICAL_PHRASES, APOLOGY_PHRASES, SELF_DOUBT_PHRASES,
    REASSURANCE_SEEKING_PHRASES, NEGATION_WORDS,
)

MIN_HARD_NGRAM = 2
SOFT_WORD_ALLOWLIST = {
    "plan", "anxious", "nervous", "stress", "risk", "step", "concerned",
    # Basic negation words — ubiquitous in English, not meaningful leakage
    "no", "not", "don't", "won't", "can't", "shouldn't", "wouldn't",
    "couldn't", "isn't", "aren't", "wasn't", "weren't", "hasn't",
    "haven't", "hadn't", "doesn't", "didn't", "never",
}

# All detection phrase lists keyed by source name
PHRASE_LISTS: dict[str, list[str]] = {
    "HEDGE_PHRASES": list(HEDGE_PHRASES),
    "CERTAINTY_PHRASES": list(CERTAINTY_PHRASES),
    "DISAGREEMENT_PHRASES": list(DISAGREEMENT_PHRASES),
    "ACKNOWLEDGMENT_PHRASES": list(ACKNOWLEDGMENT_PHRASES),
    "IDEA_PHRASES": list(IDEA_PHRASES),
    "PLANNING_PHRASES": list(PLANNING_PHRASES),
    "EMOTIONAL_WORDS": list(EMOTIONAL_WORDS),
    "POSITIVE_EMOTION_WORDS": list(POSITIVE_EMOTION_WORDS),
    "REFERENCE_BACK_PHRASES": list(REFERENCE_BACK_PHRASES),
    "ACTION_ITEM_PHRASES": list(ACTION_ITEM_PHRASES),
    "HYPOTHETICAL_PHRASES": list(HYPOTHETICAL_PHRASES),
    "APOLOGY_PHRASES": list(APOLOGY_PHRASES),
    "SELF_DOUBT_PHRASES": list(SELF_DOUBT_PHRASES),
    "REASSURANCE_SEEKING_PHRASES": list(REASSURANCE_SEEKING_PHRASES),
    "NEGATION_WORDS": [w for w in NEGATION_WORDS],
}


def audit_overlap(instructions_text: str, phrase_lists: dict[str, list[str]]) -> dict:
    """
    Check for phrase leakage between instruction text and evaluator phrase lists.

    Args:
        instructions_text: Concatenated text of all behavioral instructions.
        phrase_lists: Dict mapping source name to list of detection phrases.

    Returns:
        Dict with hard/soft overlap counts, lists, and pass/fail status.
    """
    hard, soft = [], []
    text = instructions_text.lower()

    for src, phrases in phrase_lists.items():
        for p in phrases:
            p = p.strip().lower()
            if not p:
                continue
            if p not in text:
                continue
            token_count = len(p.split())
            if token_count >= MIN_HARD_NGRAM:
                hard.append((src, p))
            elif p not in SOFT_WORD_ALLOWLIST:
                hard.append((src, p))
            else:
                soft.append((src, p))

    return {
        "hard_overlap_count": len(hard),
        "soft_overlap_count": len(soft),
        "hard_overlaps": [f"{s}:{p}" for s, p in hard],
        "soft_overlaps": [f"{s}:{p}" for s, p in soft],
        "pass": len(hard) == 0,
    }


def run_full_audit() -> dict:
    """
    Run the full overlap audit against current BEHAVIORAL_INSTRUCTIONS.

    Returns audit result dict. Prints summary.
    """
    # Collect all instruction text
    all_text = ""
    for trait, levels in BEHAVIORAL_INSTRUCTIONS.items():
        for level, text in levels.items():
            all_text += " " + text

    result = audit_overlap(all_text, PHRASE_LISTS)

    print(f"{'='*50}")
    print(f"OVERLAP AUDIT RESULTS")
    print(f"{'='*50}")
    print(f"Hard overlaps: {result['hard_overlap_count']}")
    for h in result["hard_overlaps"]:
        print(f"  HARD: {h}")
    print(f"Soft overlaps: {result['soft_overlap_count']}")
    for s in result["soft_overlaps"]:
        print(f"  soft: {s}")
    print(f"Pass: {'YES' if result['pass'] else 'NO — hard overlaps must be fixed'}")
    print(f"{'='*50}")

    return result
