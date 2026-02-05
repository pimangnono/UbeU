"""
Senior Analyst: Post-Session Logic Validation (Claude Haiku 4.5 via OpenRouter).

Runs AFTER the session ends — NOT a live participant.
Analyzes the full conversation transcript against the full case data
to validate the candidate's analytical reasoning.
"""

import json
from typing import TYPE_CHECKING

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from clients.llm_client import ModelTier
from utils.models import Turn
from step2.case_data import CaseStudy

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


VALIDATOR_SYSTEM_PROMPT = """You are a Senior Analyst reviewing a consulting case discussion transcript.

Your job is to evaluate the candidate's analytical reasoning during a business case study discussion. The candidate was given a problem statement and could request data from the facilitator. Two AI analysts (Jordan, a skeptic, and Sam, a mediator) also participated.

Evaluate the candidate's performance on these dimensions:
1. **Assumptions**: What key assumptions did the candidate make? Were they valid or invalid given the available data?
2. **Logical Gaps**: Where was the candidate's reasoning weak, incomplete, or missing?
3. **Analytical Depth**: How thoroughly did they analyze the problem? (1-5 scale)
4. **Data Utilization**: Which data categories were used effectively vs. ignored?
5. **Recommendation Quality**: How actionable and well-supported was the final recommendation? (1-5 scale)

Respond ONLY with valid JSON in this exact format:
{
    "assumptions_made": [
        {"assumption": "...", "valid": true/false, "explanation": "..."}
    ],
    "logical_gaps": ["..."],
    "analytical_depth": <1-5>,
    "data_utilization": {
        "used_effectively": ["category1", "category2"],
        "mentioned_but_shallow": ["category3"],
        "ignored": ["category4", "category5"]
    },
    "recommendation_quality": <1-5>,
    "summary": "2-3 sentence overall assessment"
}"""


def _format_transcript(transcript: list[Turn]) -> str:
    """Format conversation transcript for the validator."""
    lines = []
    for turn in transcript:
        role_label = turn.speaker_name
        lines.append(f"[{role_label}]: {turn.content}")
    return "\n\n".join(lines)


def _format_case_data(case_study: CaseStudy) -> str:
    """Format full case data (all categories) for the validator."""
    parts = [
        f"Company: {case_study.company_name}",
        f"Industry: {case_study.industry}",
        f"Problem: {case_study.problem_statement}",
        "",
        "=== FULL CASE DATA (all categories) ===",
    ]
    for item in case_study.data_items:
        parts.append(f"\n--- {item.label} ({item.category}) ---")
        parts.append(item.detail)
    return "\n".join(parts)


async def validate_session(
    transcript: list[Turn],
    case_study: CaseStudy,
    client: "LLMClient",
) -> dict:
    """
    Run post-session logic validation using the Senior Analyst (Claude Haiku 4.5).

    Args:
        transcript: Full conversation transcript from the session.
        case_study: The case study used in the session.
        client: LLMClient configured with Claude Haiku 4.5 model.

    Returns:
        Structured validation report as a dict.
    """
    formatted_transcript = _format_transcript(transcript)
    formatted_case = _format_case_data(case_study)

    prompt = (
        f"Here is the full case data:\n\n{formatted_case}\n\n"
        f"---\n\n"
        f"Here is the discussion transcript:\n\n{formatted_transcript}\n\n"
        f"---\n\n"
        f"Analyze the CANDIDATE's (human participant's) analytical reasoning. "
        f"Focus only on what the candidate said and asked, not the AI participants."
    )

    response = await client.generate(
        prompt=prompt,
        tier=ModelTier.PRO,  # Uses whatever model this client is configured with
        system_instruction=VALIDATOR_SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )

    # Parse JSON response
    try:
        # Strip markdown code fences if present
        text = response.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text[3:]
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()
        result = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        # If parsing fails, return raw response wrapped in a structured format
        result = {
            "assumptions_made": [],
            "logical_gaps": ["Unable to parse structured validation — see raw_response"],
            "analytical_depth": 0,
            "data_utilization": {
                "used_effectively": [],
                "mentioned_but_shallow": [],
                "ignored": [],
            },
            "recommendation_quality": 0,
            "summary": "Validation response could not be parsed as structured JSON.",
            "raw_response": response,
        }

    return result
