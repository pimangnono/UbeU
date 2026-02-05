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

## 1. Assumptions
What key assumptions did the candidate make? Were they valid or invalid given the available data?

## 2. Logical Gaps
Where was the candidate's reasoning weak, incomplete, or missing?

## 3. Analytical Depth (1-5)
Use the following rubric:
- **1 — No analysis**: Candidate made no attempt to break down the problem. Stated opinions without reasoning or data requests.
- **2 — Surface-level**: Candidate identified the problem area but explored only 1 dimension. Asked for some data but did not connect findings to root causes.
- **3 — Moderate**: Candidate explored 2-3 dimensions of the problem. Requested relevant data and drew some logical connections, but missed key relationships or left significant areas unexplored.
- **4 — Thorough**: Candidate systematically explored most dimensions. Connected data across categories (e.g., linked cost trends to customer behavior). Identified root causes with supporting evidence. Minor gaps remain.
- **5 — Exceptional**: Candidate structured a comprehensive framework covering all major dimensions. Synthesized data from multiple categories into a coherent narrative. Identified non-obvious insights. Addressed trade-offs and second-order effects.

## 4. Data Utilization
Which data categories did the candidate request and use effectively vs. mention superficially vs. ignore entirely?

## 5. Recommendation Quality (1-5)
Use the following rubric:
- **1 — No recommendation**: Candidate did not propose a course of action, or stated a vague direction without any supporting logic.
- **2 — Weak**: Candidate proposed an action but with little or no supporting evidence. The recommendation does not clearly address the core problem, or ignores major constraints.
- **3 — Adequate**: Candidate proposed a relevant recommendation supported by some data. Addresses the core problem but lacks specificity in implementation or does not consider risks/trade-offs.
- **4 — Strong**: Candidate proposed a specific, data-backed recommendation that addresses the core problem. Considered at least one major risk or trade-off. Implementation direction is clear but may lack detail.
- **5 — Excellent**: Candidate proposed a prioritized, actionable recommendation with clear implementation steps. Backed by evidence from multiple data categories. Addressed risks, trade-offs, and competitive dynamics. Recommendation is realistic given the constraints.

## Response Format
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

# Number of independent scoring passes for multi-pass validation
NUM_PASSES = 3


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


def _parse_validator_response(response: str) -> dict | None:
    """Parse a single validator JSON response. Returns None on failure."""
    try:
        text = response.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text[3:]
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()
        result = json.loads(text)
        # Validate required numeric fields are in range
        if not (1 <= result.get("analytical_depth", 0) <= 5):
            return None
        if not (1 <= result.get("recommendation_quality", 0) <= 5):
            return None
        return result
    except (json.JSONDecodeError, ValueError, TypeError):
        return None


def _aggregate_passes(passes: list[dict]) -> dict:
    """
    Aggregate multiple scoring passes into a single result.

    Numeric scores: median.
    Lists (assumptions, gaps): union deduplicated by content similarity.
    Data utilization: union across passes.
    Summary: from the median-scoring pass.
    """
    if len(passes) == 1:
        result = passes[0].copy()
        result["scoring"] = {
            "num_passes": 1,
            "analytical_depth_scores": [result["analytical_depth"]],
            "recommendation_quality_scores": [result["recommendation_quality"]],
        }
        return result

    # Numeric scores — collect and take median
    depth_scores = sorted(p["analytical_depth"] for p in passes)
    rec_scores = sorted(p["recommendation_quality"] for p in passes)
    n = len(passes)
    median_depth = depth_scores[n // 2] if n % 2 == 1 else round((depth_scores[n // 2 - 1] + depth_scores[n // 2]) / 2)
    median_rec = rec_scores[n // 2] if n % 2 == 1 else round((rec_scores[n // 2 - 1] + rec_scores[n // 2]) / 2)

    # Find the pass closest to median scores (use as "representative" for qualitative fields)
    best_idx = 0
    best_dist = float("inf")
    for i, p in enumerate(passes):
        dist = abs(p["analytical_depth"] - median_depth) + abs(p["recommendation_quality"] - median_rec)
        if dist < best_dist:
            best_dist = dist
            best_idx = i
    representative = passes[best_idx]

    # Assumptions — union, deduplicate by checking substring overlap
    seen_assumptions = set()
    all_assumptions = []
    for p in passes:
        for a in p.get("assumptions_made", []):
            key = a.get("assumption", "")[:80].lower().strip()
            if key and key not in seen_assumptions:
                seen_assumptions.add(key)
                all_assumptions.append(a)

    # Logical gaps — union, deduplicate by substring
    seen_gaps = set()
    all_gaps = []
    for p in passes:
        for gap in p.get("logical_gaps", []):
            key = gap[:80].lower().strip()
            if key and key not in seen_gaps:
                seen_gaps.add(key)
                all_gaps.append(gap)

    # Data utilization — union across passes
    used = set()
    shallow = set()
    ignored = set()
    for p in passes:
        du = p.get("data_utilization", {})
        used.update(du.get("used_effectively", []))
        shallow.update(du.get("mentioned_but_shallow", []))
        ignored.update(du.get("ignored", []))
    # If a category appears in "used" in any pass, remove from shallow/ignored
    shallow -= used
    ignored -= used | shallow

    return {
        "assumptions_made": all_assumptions,
        "logical_gaps": all_gaps,
        "analytical_depth": median_depth,
        "data_utilization": {
            "used_effectively": sorted(used),
            "mentioned_but_shallow": sorted(shallow),
            "ignored": sorted(ignored),
        },
        "recommendation_quality": median_rec,
        "summary": representative.get("summary", ""),
        "scoring": {
            "num_passes": len(passes),
            "analytical_depth_scores": depth_scores,
            "recommendation_quality_scores": rec_scores,
            "depth_agreement": max(depth_scores) - min(depth_scores),
            "rec_agreement": max(rec_scores) - min(rec_scores),
        },
    }


async def _run_single_pass(
    prompt: str,
    client: "LLMClient",
    pass_number: int,
) -> dict | None:
    """Run a single validation pass and return parsed result or None."""
    response = await client.generate(
        prompt=prompt,
        tier=ModelTier.PRO,
        system_instruction=VALIDATOR_SYSTEM_PROMPT,
        temperature=0.4,  # Slightly higher than before to get scoring variance
        max_tokens=2048,
    )
    result = _parse_validator_response(response)
    if result:
        result["_pass"] = pass_number
    return result


async def validate_session(
    transcript: list[Turn],
    case_study: CaseStudy,
    client: "LLMClient",
    num_passes: int = NUM_PASSES,
) -> dict:
    """
    Run multi-pass post-session logic validation.

    Each pass independently scores the transcript. Results are aggregated:
    numeric scores use median, qualitative fields use union.

    Args:
        transcript: Full conversation transcript from the session.
        case_study: The case study used in the session.
        client: LLMClient configured with Claude Haiku 4.5 model.
        num_passes: Number of independent scoring passes (default: 3).

    Returns:
        Aggregated validation report as a dict, with per-pass scores
        in the "scoring" sub-dict for transparency.
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

    # Run passes concurrently
    import asyncio
    tasks = [_run_single_pass(prompt, client, i + 1) for i in range(num_passes)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Collect successful passes
    valid_passes = []
    for r in results:
        if isinstance(r, dict):
            valid_passes.append(r)

    if not valid_passes:
        return {
            "assumptions_made": [],
            "logical_gaps": ["All validation passes failed to produce valid output"],
            "analytical_depth": 0,
            "data_utilization": {
                "used_effectively": [],
                "mentioned_but_shallow": [],
                "ignored": [],
            },
            "recommendation_quality": 0,
            "summary": "Validation failed — no passes returned valid JSON.",
            "scoring": {"num_passes": num_passes, "successful_passes": 0},
        }

    return _aggregate_passes(valid_passes)
