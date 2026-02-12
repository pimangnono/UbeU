"""
BFI-44 Scoring: Compute Big Five personality scores from questionnaire responses.

The 44-item Big Five Inventory (John & Srivastava, 1999).
Some items are reverse-scored.
"""

from utils.models import PersonalityVector


# Item to trait mapping
# Reverse-scored items are marked with 'R'
BFI44_ITEMS = {
    # Extraversion (8 items)
    1: ("E", False),   # Is talkative
    6: ("E", True),    # Is reserved (R)
    11: ("E", False),  # Is full of energy
    16: ("E", False),  # Generates enthusiasm
    21: ("E", True),   # Tends to be quiet (R)
    26: ("E", False),  # Has an assertive personality
    31: ("E", True),   # Is sometimes shy, inhibited (R)
    36: ("E", False),  # Is outgoing, sociable

    # Agreeableness (9 items)
    2: ("A", True),    # Tends to find fault (R)
    7: ("A", False),   # Is helpful and unselfish
    12: ("A", True),   # Starts quarrels (R)
    17: ("A", False),  # Has a forgiving nature
    22: ("A", False),  # Is generally trusting
    27: ("A", True),   # Can be cold and aloof (R)
    32: ("A", False),  # Is considerate and kind
    37: ("A", True),   # Is sometimes rude (R)
    42: ("A", False),  # Likes to cooperate

    # Conscientiousness (9 items)
    3: ("C", False),   # Does a thorough job
    8: ("C", True),    # Can be somewhat careless (R)
    13: ("C", False),  # Is a reliable worker
    18: ("C", True),   # Tends to be disorganized (R)
    23: ("C", True),   # Tends to be lazy (R)
    28: ("C", False),  # Perseveres until task finished
    33: ("C", False),  # Does things efficiently
    38: ("C", False),  # Makes plans and follows through
    43: ("C", True),   # Is easily distracted (R)

    # Neuroticism (8 items)
    4: ("N", False),   # Is depressed, blue
    9: ("N", True),    # Is relaxed, handles stress (R)
    14: ("N", False),  # Can be tense
    19: ("N", False),  # Worries a lot
    24: ("N", True),   # Is emotionally stable (R)
    29: ("N", False),  # Can be moody
    34: ("N", True),   # Remains calm in tense situations (R)
    39: ("N", False),  # Gets nervous easily

    # Openness (10 items)
    5: ("O", False),   # Is original, comes up with new ideas
    10: ("O", False),  # Is curious about many things
    15: ("O", False),  # Is ingenious, a deep thinker
    20: ("O", False),  # Has an active imagination
    25: ("O", False),  # Is inventive
    30: ("O", False),  # Values artistic experiences
    35: ("O", True),   # Prefers routine work (R)
    40: ("O", False),  # Likes to reflect, play with ideas
    41: ("O", True),   # Has few artistic interests (R)
    44: ("O", False),  # Is sophisticated in art/music/literature
}


def score_bfi44(responses: dict[int, int]) -> PersonalityVector:
    """
    Score BFI-44 responses to produce Big Five personality vector.

    Args:
        responses: Dict mapping item number (1-44) to Likert response (1-5)

    Returns:
        PersonalityVector with scores normalized to 0.0-1.0 range

    Raises:
        ValueError: If responses are invalid or incomplete
    """
    # Validate responses
    if len(responses) != 44:
        raise ValueError(f"Expected 44 responses, got {len(responses)}")

    for item_num in range(1, 45):
        if item_num not in responses:
            raise ValueError(f"Missing response for item {item_num}")
        value = responses[item_num]
        if not isinstance(value, int) or value < 1 or value > 5:
            raise ValueError(f"Item {item_num} has invalid value: {value}")

    # Accumulate scores by trait
    trait_sums = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}
    trait_counts = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}

    for item_num, (trait, is_reversed) in BFI44_ITEMS.items():
        value = responses[item_num]

        # Reverse score if needed (1->5, 2->4, 3->3, 4->2, 5->1)
        if is_reversed:
            value = 6 - value

        trait_sums[trait] += value
        trait_counts[trait] += 1

    # Calculate averages and normalize to 0-1
    def normalize(total: int, count: int) -> float:
        """Convert sum of Likert (1-5) to 0-1 scale."""
        avg = total / count  # Will be 1.0-5.0
        return (avg - 1) / 4  # Normalize to 0.0-1.0

    return PersonalityVector(
        O=normalize(trait_sums["O"], trait_counts["O"]),
        C=normalize(trait_sums["C"], trait_counts["C"]),
        E=normalize(trait_sums["E"], trait_counts["E"]),
        A=normalize(trait_sums["A"], trait_counts["A"]),
        N=normalize(trait_sums["N"], trait_counts["N"]),
    )


def get_bfi44_items() -> list[dict]:
    """
    Get the 44 BFI items for display in the questionnaire.

    Returns:
        List of dicts with 'number', 'text', 'trait', 'reversed'
    """
    items_text = {
        1: "Is talkative",
        2: "Tends to find fault with others",
        3: "Does a thorough job",
        4: "Is depressed, blue",
        5: "Is original, comes up with new ideas",
        6: "Is reserved",
        7: "Is helpful and unselfish with others",
        8: "Can be somewhat careless",
        9: "Is relaxed, handles stress well",
        10: "Is curious about many different things",
        11: "Is full of energy",
        12: "Starts quarrels with others",
        13: "Is a reliable worker",
        14: "Can be tense",
        15: "Is ingenious, a deep thinker",
        16: "Generates a lot of enthusiasm",
        17: "Has a forgiving nature",
        18: "Tends to be disorganized",
        19: "Worries a lot",
        20: "Has an active imagination",
        21: "Tends to be quiet",
        22: "Is generally trusting",
        23: "Tends to be lazy",
        24: "Is emotionally stable, not easily upset",
        25: "Is inventive",
        26: "Has an assertive personality",
        27: "Can be cold and aloof",
        28: "Perseveres until the task is finished",
        29: "Can be moody",
        30: "Values artistic, aesthetic experiences",
        31: "Is sometimes shy, inhibited",
        32: "Is considerate and kind to almost everyone",
        33: "Does things efficiently",
        34: "Remains calm in tense situations",
        35: "Prefers work that is routine",
        36: "Is outgoing, sociable",
        37: "Is sometimes rude to others",
        38: "Makes plans and follows through with them",
        39: "Gets nervous easily",
        40: "Likes to reflect, play with ideas",
        41: "Has few artistic interests",
        42: "Likes to cooperate with others",
        43: "Is easily distracted",
        44: "Is sophisticated in art, music, or literature",
    }

    items = []
    for num in range(1, 45):
        trait, is_reversed = BFI44_ITEMS[num]
        items.append({
            "number": num,
            "text": f"I see myself as someone who {items_text[num].lower()}",
            "trait": trait,
            "reversed": is_reversed,
        })

    return items
