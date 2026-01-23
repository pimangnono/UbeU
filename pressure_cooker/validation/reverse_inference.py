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
Analyze the following conversation and infer the personality traits of the person named "{candidate_name}".

## Conversation
{conversation}

## Task
Based on {candidate_name}'s responses, estimate their Big Five personality scores on a scale of 0.0 to 1.0:

1. **Openness to Experience**: curiosity, creativity, preference for novelty vs. routine
2. **Conscientiousness**: organization, dependability, self-discipline vs. spontaneity
3. **Extraversion**: sociability, assertiveness, positive emotions vs. reserve
4. **Agreeableness**: cooperation, trust, empathy vs. competitiveness
5. **Neuroticism**: emotional reactivity, anxiety, moodiness vs. emotional stability

Respond ONLY in this JSON format:
{{
    "openness": 0.0-1.0,
    "conscientiousness": 0.0-1.0,
    "extraversion": 0.0-1.0,
    "agreeableness": 0.0-1.0,
    "neuroticism": 0.0-1.0,
    "reasoning": "brief explanation of key behavioral indicators observed"
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

    prompt = INFERENCE_PROMPT.format(
        candidate_name=candidate_name,
        conversation=conversation,
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

        result = await validate_session(session, client)
        results.append(result)

        if verbose:
            print(f"  Overall accuracy: {result.overall_accuracy:.1%}")

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
