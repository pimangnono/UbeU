"""
Trajectory Judge: Appropriateness + Coherence scoring per candidate turn.
Also provides perceived-pressure scoring for manipulation checks.
"""

from __future__ import annotations

import asyncio
import json
import statistics
from typing import Optional

from utils.models import Turn


_TRAJECTORY_SYSTEM = (
    "You are a rigorous conversation analyst. Score appropriateness and coherence "
    "from 0.0 to 1.0. Be strict and consistent. Return JSON only."
)

_TRAJECTORY_PROMPT = """Analyze the candidate's response in context.

Context (most recent turns):
{context}

Candidate response:
"{response}"

Return JSON:
{{
  "appropriateness": <0-1>,
  "coherence": <0-1>,
  "confidence": <0-1>
}}
"""

_PRESSURE_SYSTEM = (
    "You are a careful evaluator of perceived pressure in team discussions. "
    "Rate perceived pressure from 0.0 (no pressure) to 1.0 (extreme pressure). "
    "Return JSON only."
)

_PRESSURE_PROMPT = """Scenario brief:
{brief}

Transcript:
{transcript}

Return JSON:
{{
  "perceived_pressure": <0-1>,
  "confidence": <0-1>
}}
"""


def _format_context(turns: list[Turn], max_turns: int) -> str:
    ctx = turns[-max_turns:] if len(turns) > max_turns else turns
    lines = [f"[{t.turn_number}] {t.speaker_name}: {t.content}" for t in ctx]
    return "\n".join(lines)


def _safe_json(text: str) -> dict:
    try:
        return json.loads(text)
    except Exception:
        # Fallback: find first JSON-like block
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end+1])
            except Exception:
                pass
    return {}


def _median_score(values: list[float]) -> float:
    if not values:
        return 0.5
    return float(statistics.median(values))


async def evaluate_trajectory(
    client,
    turns: list[Turn],
    candidate_name: str = "Candidate",
    context_turns: int = 6,
) -> dict:
    """
    Score appropriateness + coherence for each candidate turn.
    Returns per-turn list and session averages.
    """
    candidate_turns = [t for t in turns if t.speaker_name == candidate_name]
    per_turn = []

    for t in candidate_turns:
        # Build context up to this turn
        idx = turns.index(t)
        context = _format_context(turns[:idx], context_turns)
        prompt = _TRAJECTORY_PROMPT.format(context=context, response=t.content)

        resp = await client.generate_ensemble(
            prompt=prompt,
            system_instruction=_TRAJECTORY_SYSTEM,
            temperature=0.2,
            max_tokens=400,
        )

        app_scores = []
        coh_scores = []
        conf_scores = []
        for _, text in resp:
            data = _safe_json(text)
            app_scores.append(float(data.get("appropriateness", 0.5)))
            coh_scores.append(float(data.get("coherence", 0.5)))
            conf_scores.append(float(data.get("confidence", 0.5)))

        per_turn.append({
            "turn_number": t.turn_number,
            "appropriateness": round(_median_score(app_scores), 4),
            "coherence": round(_median_score(coh_scores), 4),
            "confidence": round(_median_score(conf_scores), 4),
        })

    if not per_turn:
        return {"per_turn": [], "avg_appropriateness": 0.5, "avg_coherence": 0.5}

    avg_app = statistics.mean([p["appropriateness"] for p in per_turn])
    avg_coh = statistics.mean([p["coherence"] for p in per_turn])

    return {
        "per_turn": per_turn,
        "avg_appropriateness": round(avg_app, 4),
        "avg_coherence": round(avg_coh, 4),
    }


async def evaluate_perceived_pressure(
    client,
    turns: list[Turn],
    scenario_brief: str,
) -> dict:
    """Perceived pressure rating for manipulation check."""
    transcript = "\n".join([f"{t.speaker_name}: {t.content}" for t in turns])
    prompt = _PRESSURE_PROMPT.format(brief=scenario_brief, transcript=transcript)

    resp = await client.generate_ensemble(
        prompt=prompt,
        system_instruction=_PRESSURE_SYSTEM,
        temperature=0.2,
        max_tokens=300,
    )

    scores = []
    confs = []
    for _, text in resp:
        data = _safe_json(text)
        scores.append(float(data.get("perceived_pressure", 0.5)))
        confs.append(float(data.get("confidence", 0.5)))

    return {
        "perceived_pressure": round(_median_score(scores), 4),
        "confidence": round(_median_score(confs), 4),
    }

