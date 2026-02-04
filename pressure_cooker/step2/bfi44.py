"""
BFI-44 Questionnaire: Items, Reverse Scoring, and Normalization.

The Big Five Inventory (John, Donahue, & Kentle, 1991) measures five
personality dimensions with 44 items on a 1-5 Likert scale.

Scoring:
  1. Reverse-score 16 designated items (score = 6 - raw).
  2. Average per trait (yields 1.0-5.0 mean).
  3. Normalize: (mean - 1.0) / 4.0 → 0.0-1.0 scale.

Output is a PersonalityVector compatible with the existing framework.
"""

from dataclasses import dataclass
from typing import Optional

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.models import PersonalityVector


@dataclass(frozen=True)
class BFI44Item:
    """A single BFI-44 questionnaire item."""
    number: int
    text: str
    trait: str  # E, A, C, N, O
    reverse: bool


# All 44 BFI items.
# Stem: "I see myself as someone who..."
BFI44_ITEMS: list[BFI44Item] = [
    # Extraversion (8 items: 1, 6R, 11, 16, 21R, 26, 31R, 36)
    BFI44Item(1,  "Is talkative",                                          "E", False),
    BFI44Item(6,  "Is reserved",                                           "E", True),
    BFI44Item(11, "Is full of energy",                                     "E", False),
    BFI44Item(16, "Generates a lot of enthusiasm",                         "E", False),
    BFI44Item(21, "Tends to be quiet",                                     "E", True),
    BFI44Item(26, "Has an assertive personality",                          "E", False),
    BFI44Item(31, "Is sometimes shy, inhibited",                           "E", True),
    BFI44Item(36, "Is outgoing, sociable",                                 "E", False),

    # Agreeableness (9 items: 2R, 7, 12R, 17, 22, 27R, 32, 37R, 42)
    BFI44Item(2,  "Tends to find fault with others",                       "A", True),
    BFI44Item(7,  "Is helpful and unselfish with others",                  "A", False),
    BFI44Item(12, "Starts quarrels with others",                           "A", True),
    BFI44Item(17, "Has a forgiving nature",                                "A", False),
    BFI44Item(22, "Is generally trusting",                                 "A", False),
    BFI44Item(27, "Can be cold and aloof",                                 "A", True),
    BFI44Item(32, "Is considerate and kind to almost everyone",            "A", False),
    BFI44Item(37, "Is sometimes rude to others",                           "A", True),
    BFI44Item(42, "Likes to cooperate with others",                        "A", False),

    # Conscientiousness (9 items: 3, 8R, 13, 18R, 23R, 28, 33, 38, 43R)
    BFI44Item(3,  "Does a thorough job",                                   "C", False),
    BFI44Item(8,  "Can be somewhat careless",                              "C", True),
    BFI44Item(13, "Is a reliable worker",                                  "C", False),
    BFI44Item(18, "Tends to be disorganized",                              "C", True),
    BFI44Item(23, "Tends to be lazy",                                      "C", True),
    BFI44Item(28, "Perseveres until the task is finished",                 "C", False),
    BFI44Item(33, "Does things efficiently",                               "C", False),
    BFI44Item(38, "Makes plans and follows through with them",             "C", False),
    BFI44Item(43, "Is easily distracted",                                  "C", True),

    # Neuroticism (8 items: 4, 9R, 14, 19, 24R, 29, 34R, 39)
    BFI44Item(4,  "Is depressed, blue",                                    "N", False),
    BFI44Item(9,  "Is relaxed, handles stress well",                       "N", True),
    BFI44Item(14, "Can be tense",                                          "N", False),
    BFI44Item(19, "Worries a lot",                                         "N", False),
    BFI44Item(24, "Is emotionally stable, not easily upset",               "N", True),
    BFI44Item(29, "Can be moody",                                          "N", False),
    BFI44Item(34, "Remains calm in tense situations",                      "N", True),
    BFI44Item(39, "Gets nervous easily",                                   "N", False),

    # Openness (10 items: 5, 10, 15, 20, 25, 30, 35R, 40, 41R, 44)
    BFI44Item(5,  "Is original, comes up with new ideas",                  "O", False),
    BFI44Item(10, "Is curious about many different things",                "O", False),
    BFI44Item(15, "Is ingenious, a deep thinker",                          "O", False),
    BFI44Item(20, "Has an active imagination",                             "O", False),
    BFI44Item(25, "Is inventive",                                          "O", False),
    BFI44Item(30, "Values artistic, aesthetic experiences",                "O", False),
    BFI44Item(35, "Prefers work that is routine",                          "O", True),
    BFI44Item(40, "Likes to reflect, play with ideas",                     "O", False),
    BFI44Item(41, "Has few artistic interests",                            "O", True),
    BFI44Item(44, "Is sophisticated in art, music, or literature",         "O", False),
]

# Quick lookup by item number
_ITEMS_BY_NUMBER: dict[int, BFI44Item] = {item.number: item for item in BFI44_ITEMS}

# Trait label to full name mapping
TRAIT_FULL_NAMES: dict[str, str] = {
    "E": "extraversion",
    "A": "agreeableness",
    "C": "conscientiousness",
    "N": "neuroticism",
    "O": "openness",
}

# BFI-44 stem displayed before each item
BFI44_STEM = "I see myself as someone who..."


def get_items_sorted() -> list[BFI44Item]:
    """Return all 44 items sorted by item number."""
    return sorted(BFI44_ITEMS, key=lambda x: x.number)


def score_bfi44(responses: dict[int, int]) -> PersonalityVector:
    """
    Score a complete BFI-44 response set.

    Args:
        responses: Mapping of item number (1-44) to Likert response (1-5).
                   1 = Disagree strongly, 5 = Agree strongly.

    Returns:
        PersonalityVector with trait scores normalized to 0.0-1.0.

    Raises:
        ValueError: If responses are missing items or have invalid values.
    """
    # Validate completeness
    expected = set(range(1, 45))
    provided = set(responses.keys())
    missing = expected - provided
    if missing:
        raise ValueError(f"Missing responses for items: {sorted(missing)}")

    # Validate range
    for item_num, value in responses.items():
        if not (1 <= value <= 5):
            raise ValueError(f"Item {item_num}: value {value} not in range 1-5")

    # Reverse-score and group by trait
    trait_scores: dict[str, list[float]] = {t: [] for t in TRAIT_FULL_NAMES}

    for item_num, raw in responses.items():
        item = _ITEMS_BY_NUMBER[item_num]
        score = (6 - raw) if item.reverse else raw
        trait_scores[item.trait].append(float(score))

    # Average per trait → 1.0-5.0, then normalize to 0.0-1.0
    normalized: dict[str, float] = {}
    for trait_code, scores in trait_scores.items():
        trait_mean = sum(scores) / len(scores)
        # Normalize: (mean - 1.0) / 4.0 → 0.0-1.0
        normalized[TRAIT_FULL_NAMES[trait_code]] = round((trait_mean - 1.0) / 4.0, 4)

    return PersonalityVector(
        openness=normalized["openness"],
        conscientiousness=normalized["conscientiousness"],
        extraversion=normalized["extraversion"],
        agreeableness=normalized["agreeableness"],
        neuroticism=normalized["neuroticism"],
    )


def get_trait_raw_means(responses: dict[int, int]) -> dict[str, float]:
    """
    Compute raw trait means (1.0-5.0 scale) without normalization.
    Useful for displaying scores in the original BFI scale.
    """
    trait_scores: dict[str, list[float]] = {t: [] for t in TRAIT_FULL_NAMES}

    for item_num, raw in responses.items():
        item = _ITEMS_BY_NUMBER[item_num]
        score = (6 - raw) if item.reverse else raw
        trait_scores[item.trait].append(float(score))

    return {
        TRAIT_FULL_NAMES[code]: round(sum(scores) / len(scores), 2)
        for code, scores in trait_scores.items()
    }
