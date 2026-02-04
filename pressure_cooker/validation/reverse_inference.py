"""
Reverse Inference Validation for Pressure Cooker Framework.
Uses LLM to infer personality traits from generated conversations
and compares with ground truth profiles.
"""

import json
from typing import TYPE_CHECKING

from utils.models import (
    PersonalityVector,
    SessionOutput,
    ValidationResult,
    Turn,
    SpeakerRole,
)

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient


INFERENCE_PROMPT = """You are an expert psychologist trained in the Big Five personality model.
Analyze the following group discussion and infer the personality traits of the person named "{candidate_name}".

## Conversation
{conversation}

## Behavioral Statistics for {candidate_name}
{behavioral_stats}

## Scoring Guide

Rate each trait on a 0.0 to 1.0 scale. Use the FULL range — 0.1-0.2 for very low, 0.8-0.9 for very high.

**Openness to Experience** (0.0 = conventional, 1.0 = highly curious):
- HIGH signals: proposes novel ideas, uses metaphors/analogies, explores hypotheticals ("what if..."), builds on creative suggestions, asks exploratory questions
- LOW signals: dismisses new ideas, demands proven methods, avoids abstract thinking, redirects to concrete/practical matters, shows no curiosity about alternatives
- CAUTION: Simply participating in a discussion is NOT a sign of openness. Look for active idea exploration vs. sticking to known approaches.

**Conscientiousness** (0.0 = spontaneous/disorganized, 1.0 = highly organized):
- HIGH signals: proposes plans/checklists, references deadlines, uses structured language ("first... second... third"), documents decisions, follows up on action items
- LOW signals: goes off-topic, loses track of discussion, informal/casual language, no references to process or timelines, comfortable with ambiguity, does not propose structure
- CAUTION: In a structured group discussion, most people sound somewhat organized by default. Only rate HIGH (>0.7) if {candidate_name} actively imposes additional structure beyond what the conversation demands. Rate LOW (<0.4) if responses are notably scattered, informal, or process-averse.

**Extraversion** (0.0 = very reserved, 1.0 = very outgoing):
- HIGH signals: long/elaborate responses, initiates topics, addresses others by name, expresses enthusiasm, builds rapport, high energy language
- LOW signals: SHORT responses (1-2 sentences), speaks only when necessary, does not elaborate, does not initiate topics, does not engage others socially, minimal/terse language
- CAUTION: Response LENGTH is a critical signal. Count the words: if {candidate_name}'s responses are consistently under 20 words, this strongly suggests low extraversion (0.1-0.3) regardless of content. If responses are 50+ words with elaboration, this suggests higher extraversion.

**Agreeableness** (0.0 = competitive/challenging, 1.0 = cooperative/warm):
- HIGH signals: validates others' feelings, seeks consensus, uses "we" language, avoids confrontation, offers to help, acknowledges others' contributions
- LOW signals: blunt disagreement, dismisses others' views, focuses on own interests, challenges without softening, does not build rapport, skeptical of others' motives
- CAUTION: Politeness alone is not high agreeableness. Look for genuine warmth, accommodation, and conflict avoidance vs. directness and self-interest.

**Neuroticism** (0.0 = very calm/stable, 1.0 = very emotionally reactive):
- HIGH signals: expresses worry/anxiety, reacts emotionally to challenges, uses hedging language ("I'm not sure if..."), defensive when challenged, catastrophizes problems
- LOW signals: calm under provocation, unbothered by criticism, does not acknowledge stress, task-focused without emotional language, flat affect, no empathetic preambles
- CAUTION: Not expressing emotions is different from being calm. Very low neuroticism (0.1-0.2) means the person shows almost NO emotional reaction even when directly provoked or when others are stressed.

## Response Format
Respond ONLY in this JSON format:
{{
    "openness": 0.0-1.0,
    "conscientiousness": 0.0-1.0,
    "extraversion": 0.0-1.0,
    "agreeableness": 0.0-1.0,
    "neuroticism": 0.0-1.0,
    "reasoning": "brief explanation citing specific behavioral evidence for each trait score"
}}"""


def format_conversation_for_inference(
    turns: list[Turn],
    candidate_name: str = "Alex",
) -> str:
    """
    Format conversation turns for inference prompt.

    Args:
        turns: List of conversation turns.
        candidate_name: Name of the candidate to highlight.

    Returns:
        Formatted conversation string.
    """
    lines = []

    for turn in turns:
        # Highlight candidate's turns
        if turn.speaker == SpeakerRole.CANDIDATE:
            lines.append(f">>> {turn.speaker_name}: {turn.content}")
        else:
            lines.append(f"{turn.speaker_name}: {turn.content}")

    return "\n".join(lines)


def compute_behavioral_stats(
    turns: list[Turn],
    candidate_name: str = "Alex",
) -> str:
    """
    Compute observable behavioral statistics for the candidate.

    Provides the judge with quantitative signals about response patterns
    that are hard to assess from reading alone (word counts, turn frequency).
    """
    candidate_turns = [t for t in turns if t.speaker == SpeakerRole.CANDIDATE]
    other_turns = [t for t in turns if t.speaker != SpeakerRole.CANDIDATE]

    if not candidate_turns:
        return "No candidate turns found."

    word_counts = [len(t.content.split()) for t in candidate_turns]
    avg_words = sum(word_counts) / len(word_counts)
    min_words = min(word_counts)
    max_words = max(word_counts)

    # Count questions asked by candidate
    questions = sum(1 for t in candidate_turns if "?" in t.content)

    # Count times candidate addresses others by name
    other_names = set(t.speaker_name for t in other_turns)
    name_mentions = sum(
        sum(1 for name in other_names if name in t.content)
        for t in candidate_turns
    )

    total_turns = len(turns)
    candidate_pct = len(candidate_turns) / total_turns * 100 if total_turns else 0

    lines = [
        f"- Total conversation turns: {total_turns}",
        f"- {candidate_name}'s turns: {len(candidate_turns)} ({candidate_pct:.0f}% of total)",
        f"- Average words per response: {avg_words:.0f}",
        f"- Response length range: {min_words}-{max_words} words",
        f"- Questions asked: {questions}",
        f"- Times addressing others by name: {name_mentions}",
    ]

    return "\n".join(lines)


async def infer_personality(
    session: SessionOutput,
    client: "GeminiClient | MockGeminiClient",
    candidate_name: str = "Alex",
) -> PersonalityVector:
    """
    Use LLM to infer personality from conversation.

    Args:
        session: The completed session output.
        client: LLM client for inference.
        candidate_name: Name of the candidate in conversation.

    Returns:
        Inferred PersonalityVector.
    """
    from clients.llm_client import ModelTier

    conversation = format_conversation_for_inference(
        session.conversation,
        candidate_name,
    )

    behavioral_stats = compute_behavioral_stats(
        session.conversation,
        candidate_name,
    )

    prompt = INFERENCE_PROMPT.format(
        candidate_name=candidate_name,
        conversation=conversation,
        behavioral_stats=behavioral_stats,
    )

    response = await client.generate(
        prompt=prompt,
        tier=ModelTier.PRO,  # Use Pro for nuanced inference
        temperature=0.3,  # Lower temperature for more consistent inference
        max_tokens=512,
    )

    # Parse JSON response
    try:
        # Extract JSON from response (handle potential markdown code blocks)
        json_str = response.strip()
        if "```json" in json_str:
            json_str = json_str.split("```json")[1].split("```")[0]
        elif "```" in json_str:
            json_str = json_str.split("```")[1].split("```")[0]

        data = json.loads(json_str)

        return PersonalityVector(
            openness=float(data.get("openness", 0.5)),
            conscientiousness=float(data.get("conscientiousness", 0.5)),
            extraversion=float(data.get("extraversion", 0.5)),
            agreeableness=float(data.get("agreeableness", 0.5)),
            neuroticism=float(data.get("neuroticism", 0.5)),
        )

    except (json.JSONDecodeError, KeyError, ValueError) as e:
        # Return middle-of-road values as fallback
        print(f"Warning: Failed to parse inference response: {e}")
        return PersonalityVector(
            openness=0.5,
            conscientiousness=0.5,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.5,
        )


def calculate_accuracy(
    inferred: PersonalityVector,
    ground_truth: PersonalityVector,
) -> dict[str, float]:
    """
    Calculate per-trait accuracy between inferred and ground truth.

    Uses absolute error approach where accuracy = 1 - |inferred - truth|.

    Args:
        inferred: Inferred personality vector.
        ground_truth: Ground truth personality vector.

    Returns:
        Dict with accuracy per trait and overall.
    """
    traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]

    accuracies = {}
    total_accuracy = 0.0

    for trait in traits:
        inferred_val = getattr(inferred, trait)
        truth_val = getattr(ground_truth, trait)

        # Accuracy = 1 - absolute error
        error = abs(inferred_val - truth_val)
        accuracy = 1.0 - error

        accuracies[trait] = round(accuracy, 3)
        total_accuracy += accuracy

    accuracies["overall"] = round(total_accuracy / len(traits), 3)

    return accuracies


async def validate_session(
    session: SessionOutput,
    client: "GeminiClient | MockGeminiClient",
) -> ValidationResult:
    """
    Run full reverse inference validation on a session.

    Args:
        session: The completed session to validate.
        client: LLM client for inference.

    Returns:
        ValidationResult with accuracy metrics.
    """
    # Get ground truth from session profile
    ground_truth = session.profile.vector

    # Infer personality from conversation
    inferred = await infer_personality(session, client)

    # Calculate accuracy
    accuracy_scores = calculate_accuracy(inferred, ground_truth)

    return ValidationResult(
        session_id=session.metadata.session_id,
        validation_type="reverse_inference",
        inferred_profile=inferred,
        ground_truth_profile=ground_truth,
        accuracy_scores=accuracy_scores,
        overall_accuracy=accuracy_scores["overall"],
        notes=f"Inferred from {len(session.conversation)} turns of conversation.",
    )


async def batch_validate(
    sessions: list[SessionOutput],
    client: "GeminiClient | MockGeminiClient",
    verbose: bool = False,
) -> list[ValidationResult]:
    """
    Validate multiple sessions.

    Args:
        sessions: List of sessions to validate.
        client: LLM client for inference.
        verbose: Print progress during validation.

    Returns:
        List of ValidationResults.
    """
    results = []

    for i, session in enumerate(sessions):
        if verbose:
            print(f"Validating session {i+1}/{len(sessions)}: {session.metadata.session_id}")

        max_retries = 3
        for attempt in range(max_retries):
            try:
                result = await validate_session(session, client)
                results.append(result)
                if verbose:
                    print(f"  Overall accuracy: {result.overall_accuracy:.1%}")
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    wait = 10 * (attempt + 1)
                    if verbose:
                        print(f"  Attempt {attempt+1} failed: {e}. Retrying in {wait}s...")
                    await asyncio.sleep(wait)
                else:
                    if verbose:
                        print(f"  SKIPPED after {max_retries} attempts: {e}")
                    # Skip this session rather than crashing

    return results


def summarize_validation_results(results: list[ValidationResult]) -> dict:
    """
    Summarize validation results across multiple sessions.

    Args:
        results: List of validation results.

    Returns:
        Summary statistics dict.
    """
    if not results:
        return {"error": "No results to summarize"}

    traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism", "overall"]

    summary = {
        "total_sessions": len(results),
        "mean_accuracy": {},
        "min_accuracy": {},
        "max_accuracy": {},
    }

    for trait in traits:
        trait_scores = [r.accuracy_scores.get(trait, 0) for r in results]
        summary["mean_accuracy"][trait] = round(sum(trait_scores) / len(trait_scores), 3)
        summary["min_accuracy"][trait] = round(min(trait_scores), 3)
        summary["max_accuracy"][trait] = round(max(trait_scores), 3)

    return summary
