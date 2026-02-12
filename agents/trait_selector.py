"""
Trait Elicitation Selector: Strategic speaker selection for Mode 2.

Selects the next AI speaker based on which personality traits have been
insufficiently observed so far. This maximizes trait coverage during the
limited discussion time.

Inspired by DialogLab's speaker selection in multi-party settings and
the competency-driven routing from Step 2.
"""

from typing import Optional
from dataclasses import dataclass, field

from utils.models import BigFiveTrait, DiscussionPhase


@dataclass
class TraitCoverage:
    """Tracks observation confidence for each Big Five trait."""
    openness: float = 0.0
    conscientiousness: float = 0.0
    extraversion: float = 0.0
    agreeableness: float = 0.0
    neuroticism: float = 0.0

    def get_weakest_trait(self) -> BigFiveTrait:
        """Get the trait with lowest observation confidence."""
        scores = {
            BigFiveTrait.OPENNESS: self.openness,
            BigFiveTrait.CONSCIENTIOUSNESS: self.conscientiousness,
            BigFiveTrait.EXTRAVERSION: self.extraversion,
            BigFiveTrait.AGREEABLENESS: self.agreeableness,
            BigFiveTrait.NEUROTICISM: self.neuroticism,
        }
        return min(scores, key=scores.get)

    def update(self, trait: BigFiveTrait, confidence: float):
        """Update observation confidence for a trait."""
        current = getattr(self, trait.value)
        # Use max to avoid reducing confidence
        setattr(self, trait.value, max(current, confidence))

    def get_coverage_summary(self) -> dict[str, float]:
        """Get coverage as a dictionary."""
        return {
            "openness": self.openness,
            "conscientiousness": self.conscientiousness,
            "extraversion": self.extraversion,
            "agreeableness": self.agreeableness,
            "neuroticism": self.neuroticism,
        }


# Mapping from traits to the agent that best elicits them
TRAIT_TO_AGENT = {
    BigFiveTrait.AGREEABLENESS: "Alex",    # Alex's disagreement reveals A
    BigFiveTrait.NEUROTICISM: "Alex",       # Alex's pressure reveals N
    BigFiveTrait.OPENNESS: "Jordan",        # Jordan's enthusiasm reveals O
    BigFiveTrait.EXTRAVERSION: "Riley",     # Riley's silence reveals E
    BigFiveTrait.CONSCIENTIOUSNESS: "Jordan",  # Jordan's collaboration reveals C
}

# Phase-appropriate default speakers
PHASE_DEFAULTS = {
    DiscussionPhase.INTRODUCTION: "Jordan",  # Warm opening
    DiscussionPhase.EXPLORATION: "Jordan",   # Build ideas
    DiscussionPhase.CONFLICT: "Alex",        # Challenge
    DiscussionPhase.RESOLUTION: "Jordan",    # Find consensus
    DiscussionPhase.CLOSING: "Jordan",       # Wrap up warmly
}


class TraitElicitationSelector:
    """
    Selects the next AI speaker based on trait coverage needs.

    Strategy:
    1. Find the least-observed trait
    2. Select the agent that best elicits that trait
    3. Avoid same speaker twice in a row
    4. Fall back to phase-appropriate default if needed
    """

    def __init__(self):
        self.coverage = TraitCoverage()
        self.last_speaker: Optional[str] = None
        self.speaker_history: list[str] = []

    def select_next_speaker(
        self,
        current_phase: DiscussionPhase,
        candidate_last_turn: Optional[str] = None,
    ) -> str:
        """
        Select the next AI speaker.

        Args:
            current_phase: Current discussion phase
            candidate_last_turn: The candidate's most recent message (for context)

        Returns:
            Name of the agent who should speak next ("Alex", "Jordan", or "Riley")
        """
        # Find least-observed trait
        weakest_trait = self.coverage.get_weakest_trait()

        # Get preferred agent for that trait
        preferred = TRAIT_TO_AGENT[weakest_trait]

        # Avoid same speaker twice in a row
        if preferred == self.last_speaker:
            # Try alternate agent for same trait if available
            preferred = self._get_alternate_for_trait(weakest_trait)

        # If still same speaker, use phase default
        if preferred == self.last_speaker:
            preferred = PHASE_DEFAULTS.get(current_phase, "Jordan")

        # Final check - if STILL same, rotate through agents
        if preferred == self.last_speaker:
            preferred = self._rotate_speaker()

        self.last_speaker = preferred
        self.speaker_history.append(preferred)
        return preferred

    def _get_alternate_for_trait(self, trait: BigFiveTrait) -> str:
        """Get an alternate agent that can also elicit the trait."""
        alternates = {
            BigFiveTrait.AGREEABLENESS: "Riley",   # Riley's skepticism also tests A
            BigFiveTrait.NEUROTICISM: "Riley",     # Riley's doubts also test N
            BigFiveTrait.OPENNESS: "Alex",         # Alex's challenges test O defense
            BigFiveTrait.EXTRAVERSION: "Alex",     # Alex's directness can prompt E
            BigFiveTrait.CONSCIENTIOUSNESS: "Riley",  # Riley's practicality tests C
        }
        return alternates.get(trait, "Jordan")

    def _rotate_speaker(self) -> str:
        """Rotate through agents to avoid repetition."""
        agents = ["Alex", "Jordan", "Riley"]
        if self.last_speaker in agents:
            idx = agents.index(self.last_speaker)
            return agents[(idx + 1) % 3]
        return "Jordan"

    def update_coverage(self, trait: BigFiveTrait, confidence: float):
        """Update trait coverage after observing behavior."""
        self.coverage.update(trait, confidence)

    def get_coverage_summary(self) -> dict[str, float]:
        """Get current trait coverage."""
        return self.coverage.get_coverage_summary()

    def get_speaker_distribution(self) -> dict[str, int]:
        """Get count of times each agent has spoken."""
        distribution = {"Alex": 0, "Jordan": 0, "Riley": 0}
        for speaker in self.speaker_history:
            if speaker in distribution:
                distribution[speaker] += 1
        return distribution

    def reset(self):
        """Reset the selector for a new session."""
        self.coverage = TraitCoverage()
        self.last_speaker = None
        self.speaker_history = []


def analyze_turn_for_traits(turn_content: str) -> list[tuple[BigFiveTrait, float]]:
    """
    Quick rule-based analysis of a turn for trait signals.

    Returns list of (trait, confidence) tuples for observed signals.
    This is a fast heuristic - deep analysis is done post-session.
    """
    signals = []
    content_lower = turn_content.lower()
    word_count = len(turn_content.split())

    # Extraversion signals
    if word_count > 40:
        signals.append((BigFiveTrait.EXTRAVERSION, 0.6))
    elif word_count < 15:
        signals.append((BigFiveTrait.EXTRAVERSION, 0.3))

    # Check for questions (engagement = E)
    if "?" in turn_content:
        signals.append((BigFiveTrait.EXTRAVERSION, 0.5))

    # Agreeableness signals
    agreement_phrases = ["i agree", "good point", "that makes sense", "you're right", "i like that"]
    disagreement_phrases = ["i disagree", "i don't think", "that won't work", "no,", "but actually"]

    if any(phrase in content_lower for phrase in agreement_phrases):
        signals.append((BigFiveTrait.AGREEABLENESS, 0.6))
    if any(phrase in content_lower for phrase in disagreement_phrases):
        signals.append((BigFiveTrait.AGREEABLENESS, 0.3))  # Low A signal

    # Openness signals
    creative_phrases = ["what if", "we could try", "another way", "alternatively", "imagine if"]
    practical_phrases = ["realistically", "practically", "the data shows", "based on"]

    if any(phrase in content_lower for phrase in creative_phrases):
        signals.append((BigFiveTrait.OPENNESS, 0.6))
    if any(phrase in content_lower for phrase in practical_phrases):
        signals.append((BigFiveTrait.OPENNESS, 0.4))

    # Conscientiousness signals
    organized_phrases = ["first,", "second,", "step by step", "let's organize", "to summarize"]
    if any(phrase in content_lower for phrase in organized_phrases):
        signals.append((BigFiveTrait.CONSCIENTIOUSNESS, 0.6))

    # Neuroticism signals (stress/anxiety)
    stress_phrases = ["i'm not sure", "this is difficult", "i'm worried", "what if we fail"]
    calm_phrases = ["no problem", "we can handle", "let's stay focused", "it's fine"]

    if any(phrase in content_lower for phrase in stress_phrases):
        signals.append((BigFiveTrait.NEUROTICISM, 0.6))
    if any(phrase in content_lower for phrase in calm_phrases):
        signals.append((BigFiveTrait.NEUROTICISM, 0.3))  # Low N signal

    return signals
