"""
Behavioral Features: Shared 22-feature extraction module.

Extracts per-turn and per-session behavioral features from conversation
transcripts. Used by GroupEngine, temporal analysis, rule-based evaluator,
and batch runner.

Features map to Big Five personality traits via established psycholinguistic
research on verbal behavior correlates.
"""

import re
import statistics
from dataclasses import dataclass, field, asdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from utils.models import Turn


# =============================================================================
# PHRASE LISTS
# =============================================================================

HEDGE_PHRASES = [
    "maybe", "perhaps", "i think", "not sure", "i guess",
    "possibly", "might be", "could be", "i'm not certain",
]

CERTAINTY_PHRASES = [
    "definitely", "absolutely", "clearly", "obviously",
    "certainly", "without a doubt", "no question",
]

DISAGREEMENT_PHRASES = [
    "i disagree", "i don't think", "that won't work", "no,", "but actually",
    "i'd push back", "not quite", "i'm not sure that", "let's reconsider",
    "i'd challenge", "that's not", "we shouldn't", "i wouldn't",
    "the problem with", "however,", "on the contrary", "but i think",
]

ACKNOWLEDGMENT_PHRASES = [
    "good point", "i agree", "that's right", "exactly", "i like that",
    "great idea", "you're right", "fair point", "makes sense",
    "well said", "i see your point", "that's fair", "absolutely",
    "building on", "love that",
]

IDEA_PHRASES = [
    "what if", "we could", "how about", "another option", "alternatively",
    "what about", "imagine if", "one idea", "my suggestion", "i propose",
    "here's a thought", "consider this", "let me suggest", "why don't we",
]

PLANNING_PHRASES = [
    "first", "then", "step", "plan", "schedule", "prioritize",
    "next we", "after that", "before we", "the order",
]

EMOTIONAL_WORDS = [
    "worried", "anxious", "stressed", "frustrated", "upset",
    "nervous", "concerned", "overwhelmed", "afraid", "fearful",
]

POSITIVE_EMOTION_WORDS = [
    "excited", "happy", "great", "wonderful", "love",
    "fantastic", "amazing", "excellent", "thrilled", "glad",
]

CONDITIONAL_PATTERNS = [
    r"\bif\b.*\bthen\b", r"\bshould\b", r"\bwould need to\b",
    r"\bcould\b.*\bif\b", r"\bassuming\b", r"\bprovided that\b",
]

AGENT_NAMES = ["alex", "jordan", "riley"]


# =============================================================================
# DATACLASS
# =============================================================================

@dataclass
class BehavioralFeatures:
    """All 22 behavioral features extracted from a session or window."""
    avg_words_per_turn: float = 0.0
    max_words_in_turn: int = 0
    min_words_in_turn: int = 0
    word_count_variance: float = 0.0
    question_ratio: float = 0.0
    exclamation_ratio: float = 0.0
    hedge_count: int = 0
    certainty_count: int = 0
    first_person_ratio: float = 0.0
    inclusive_pronoun_ratio: float = 0.0
    disagreement_count: int = 0
    acknowledgment_count: int = 0
    idea_count: int = 0
    name_mention_count: int = 0
    conditional_ratio: float = 0.0
    planning_count: int = 0
    emotional_word_count: int = 0
    positive_emotion_count: int = 0
    turn_initiation_ratio: float = 0.0
    avg_response_latency_rank: float = 0.0
    unique_word_ratio: float = 0.0
    long_sentence_ratio: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)


# =============================================================================
# EXTRACTION
# =============================================================================

def _count_phrases(text_lower: str, phrases: list[str]) -> int:
    """Count how many phrases from the list appear in the text."""
    return sum(1 for p in phrases if p in text_lower)


def _count_pattern_matches(text_lower: str, patterns: list[str]) -> int:
    """Count how many regex patterns match in the text."""
    return sum(1 for p in patterns if re.search(p, text_lower))


def _count_words(text: str, word_set: set[str]) -> int:
    """Count occurrences of words from a set in the text."""
    words = text.lower().split()
    return sum(1 for w in words if w.strip(".,!?;:'\"()") in word_set)


def _split_sentences(text: str) -> list[str]:
    """Split text into sentences."""
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]


def extract_features(
    turns: list["Turn"],
    candidate_name: str = "Candidate",
) -> BehavioralFeatures:
    """
    Extract all 22 behavioral features from a list of turns.

    Args:
        turns: Full conversation turns (all speakers).
        candidate_name: Name of the candidate speaker to analyze.

    Returns:
        BehavioralFeatures with all 22 fields populated.
    """
    # Filter candidate turns
    candidate_turns = [t for t in turns if t.speaker_name == candidate_name]

    if not candidate_turns:
        return BehavioralFeatures()

    n_turns = len(candidate_turns)

    # Per-turn word counts
    word_counts = []
    total_words = 0
    all_words = []
    total_questions = 0
    total_exclamations = 0
    total_hedges = 0
    total_certainty = 0
    total_disagreements = 0
    total_acknowledgments = 0
    total_ideas = 0
    total_name_mentions = 0
    total_conditionals = 0
    total_planning = 0
    total_emotional = 0
    total_positive = 0
    total_first_person = 0
    total_inclusive = 0
    total_long_sentences = 0
    total_sentences = 0
    initiations = 0

    first_person_words = {"i", "me", "my", "mine", "myself"}
    inclusive_words = {"we", "our", "us", "ours", "ourselves"}

    for i, turn in enumerate(candidate_turns):
        content = turn.content
        content_lower = content.lower()
        words = content.split()
        wc = len(words)
        word_counts.append(wc)
        total_words += wc
        all_words.extend(w.lower().strip(".,!?;:'\"()") for w in words)

        # Questions and exclamations
        if "?" in content:
            total_questions += 1
        if "!" in content:
            total_exclamations += 1

        # Phrase counts
        total_hedges += _count_phrases(content_lower, HEDGE_PHRASES)
        total_certainty += _count_phrases(content_lower, CERTAINTY_PHRASES)
        total_disagreements += _count_phrases(content_lower, DISAGREEMENT_PHRASES)
        total_acknowledgments += _count_phrases(content_lower, ACKNOWLEDGMENT_PHRASES)
        total_ideas += _count_phrases(content_lower, IDEA_PHRASES)
        total_planning += _count_phrases(content_lower, PLANNING_PHRASES)
        total_conditionals += _count_pattern_matches(content_lower, CONDITIONAL_PATTERNS)

        # Word-level counts
        total_emotional += _count_words(content, set(EMOTIONAL_WORDS))
        total_positive += _count_words(content, set(POSITIVE_EMOTION_WORDS))
        total_first_person += _count_words(content, first_person_words)
        total_inclusive += _count_words(content, inclusive_words)

        # Name mentions
        for name in AGENT_NAMES:
            if name in content_lower:
                total_name_mentions += 1

        # Sentences
        sentences = _split_sentences(content)
        total_sentences += len(sentences)
        total_long_sentences += sum(1 for s in sentences if len(s.split()) > 20)

        # Turn initiation: check if candidate speaks first after an AI turn
        # or introduces a new topic (heuristic: starts with a question or new subject)
        if i == 0:
            initiations += 1
        else:
            # Check if previous turn in the full transcript was from a different speaker
            # and this turn introduces new content (not just responding)
            turn_idx = turns.index(turn)
            if turn_idx > 0 and turns[turn_idx - 1].speaker_name != candidate_name:
                # Heuristic: if starts with a question or "I think we should" type phrase
                if content.strip().endswith("?") or any(
                    content_lower.startswith(p) for p in ["i think we", "what about", "how about", "let's", "we should"]
                ):
                    initiations += 1

    # Compute response latency ranks
    # For each candidate turn, find its position among responses after the previous AI turn
    latency_ranks = []
    for turn in candidate_turns:
        turn_idx = turns.index(turn)
        # Look backwards to find the last non-candidate turn
        prev_ai_idx = None
        for j in range(turn_idx - 1, -1, -1):
            if turns[j].speaker_name != candidate_name:
                prev_ai_idx = j
                break
        if prev_ai_idx is not None:
            # Count how many turns between the AI turn and this candidate turn
            gap = turn_idx - prev_ai_idx
            latency_ranks.append(gap)

    # Build features
    avg_words = total_words / n_turns if n_turns else 0.0
    word_variance = statistics.pstdev(word_counts) if len(word_counts) > 1 else 0.0
    unique_words = set(all_words)
    unique_ratio = len(unique_words) / total_words if total_words > 0 else 0.0

    return BehavioralFeatures(
        avg_words_per_turn=round(avg_words, 2),
        max_words_in_turn=max(word_counts) if word_counts else 0,
        min_words_in_turn=min(word_counts) if word_counts else 0,
        word_count_variance=round(word_variance, 2),
        question_ratio=round(total_questions / n_turns, 3) if n_turns else 0.0,
        exclamation_ratio=round(total_exclamations / n_turns, 3) if n_turns else 0.0,
        hedge_count=total_hedges,
        certainty_count=total_certainty,
        first_person_ratio=round(total_first_person / total_words, 4) if total_words else 0.0,
        inclusive_pronoun_ratio=round(total_inclusive / total_words, 4) if total_words else 0.0,
        disagreement_count=total_disagreements,
        acknowledgment_count=total_acknowledgments,
        idea_count=total_ideas,
        name_mention_count=total_name_mentions,
        conditional_ratio=round(total_conditionals / n_turns, 3) if n_turns else 0.0,
        planning_count=total_planning,
        emotional_word_count=total_emotional,
        positive_emotion_count=total_positive,
        turn_initiation_ratio=round(initiations / n_turns, 3) if n_turns else 0.0,
        avg_response_latency_rank=round(
            statistics.mean(latency_ranks), 2
        ) if latency_ranks else 1.0,
        unique_word_ratio=round(unique_ratio, 4),
        long_sentence_ratio=round(
            total_long_sentences / total_sentences, 3
        ) if total_sentences else 0.0,
    )
