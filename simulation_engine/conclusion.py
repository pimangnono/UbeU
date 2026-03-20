"""Generate structured conclusions from completed simulations via LLM."""

from __future__ import annotations

import json
import logging
from typing import Any

logger = logging.getLogger(__name__)


GUIDED_SYSTEM = """You are an expert simulation analyst. Given a completed stakeholder simulation's data, produce a structured JSON conclusion.

The simulation had a defined outcome target. Assess whether it was achieved, partially achieved, or not achieved based on the dialogue, actions, and world state changes.

Respond ONLY with valid JSON matching this schema:
{
  "mode": "guided",
  "outcome_achieved": "achieved" | "partial" | "not_achieved",
  "outcome_summary": "2-3 sentence summary of what happened and the final resolution",
  "contributing_factors": ["factor 1", "factor 2", ...],
  "actor_arcs": [{"actor_id": "...", "role": "...", "arc": "1-2 sentence narrative of this actor's journey"}],
  "unresolved_tensions": ["tension 1", ...]
}"""

EXPLORATORY_SYSTEM = """You are an expert simulation analyst. Given a completed exploratory stakeholder simulation's data, produce a structured JSON conclusion.

This simulation had no predetermined outcome — it explored stakeholder dynamics openly. Identify what emerged from the discussion.

Respond ONLY with valid JSON matching this schema:
{
  "mode": "exploratory",
  "outcome_summary": "2-3 sentence summary of the overall discussion arc and where it landed",
  "key_discoveries": ["discovery 1", "discovery 2", ...],
  "actor_arcs": [{"actor_id": "...", "role": "...", "arc": "1-2 sentence narrative of this actor's journey"}],
  "unresolved_tensions": ["tension 1", ...],
  "emergent_patterns": ["pattern 1", ...]
}"""


def _build_conclusion_prompt(
    runtime_summary: dict[str, Any],
    key_moments: list[dict[str, Any]],
    script: dict[str, Any],
) -> str:
    """Build the user prompt with simulation context for conclusion generation."""
    turns = runtime_summary.get("turns", [])
    actor_names = runtime_summary.get("actor_display_names", {})
    executed_actions = runtime_summary.get("executed_actions", [])
    relationship_events = runtime_summary.get("relationship_events", [])
    world_state_history = runtime_summary.get("world_state_history", [])
    phase_order = runtime_summary.get("phase_order", [])

    # Stakeholder summary
    stakeholders_text = ""
    for actor in script.get("stakeholders", []):
        aid = actor.get("actor_id", "")
        role = actor.get("role", "")
        disposition = actor.get("strategic_disposition", "neutral")
        stakeholders_text += f"- {aid} ({role}, {disposition})\n"

    # Last phase dialogue (last 6 turns for context)
    last_turns = turns[-6:] if len(turns) > 6 else turns
    dialogue_text = ""
    for t in last_turns:
        name = actor_names.get(t.get("actor_id", ""), t.get("display_name", ""))
        dialogue_text += f"[{t.get('phase_name', '')}] {name}: {t.get('content', '')[:300]}\n"

    # Key moments summary
    moments_text = ""
    for m in key_moments[:5]:
        moments_text += f"- Turn {m.get('turn_index', 0)}: {m.get('title', '')} — {m.get('description', '')}\n"

    # Executed actions
    actions_text = ""
    for a in executed_actions[:8]:
        actor = actor_names.get(a.get("owner_actor_id", ""), "")
        actions_text += f"- {actor} → {a.get('action_type', '')} (target: {a.get('target_key', '')}, deltas: {a.get('applied_delta', {})})\n"

    # Relationship shifts
    rel_text = ""
    significant_rels = [r for r in relationship_events if abs(r.get("trust_delta", 0)) > 0.05]
    for r in significant_rels[:6]:
        src = actor_names.get(r.get("source_actor_id", r.get("source", "")), "")
        tgt = actor_names.get(r.get("target_actor_id", r.get("target", "")), "")
        rel_text += f"- {src} → {tgt}: trust {r.get('trust_delta', 0):+.2f} ({r.get('evidence', '')[:100]})\n"

    # World state changes
    ws_text = ""
    if world_state_history:
        initial = world_state_history[0].get("global_state", {}) if world_state_history else {}
        final = world_state_history[-1].get("global_state", {}) if world_state_history else {}
        for key in final:
            delta = final.get(key, 0.5) - initial.get(key, 0.5)
            if abs(delta) > 0.02:
                ws_text += f"- {key}: {initial.get(key, 0.5):.2f} → {final.get(key, 0.5):.2f} ({delta:+.2f})\n"

    # Outcome spec for guided mode
    outcome_text = ""
    outcome_spec = script.get("outcome_spec", {})
    if outcome_spec:
        outcome_text = f"Target outcome: {json.dumps(outcome_spec)}\n"

    prompt = f"""## Simulation: {script.get('title', '')}
Objective: {script.get('objective', '')}
Mode: {script.get('simulation_mode', 'guided')}
Phases: {' → '.join(phase_order)}
{outcome_text}
## Stakeholders
{stakeholders_text}
## Final Dialogue (last turns)
{dialogue_text}
## Key Moments
{moments_text}
## Executed Actions
{actions_text or '(none)'}
## Significant Relationship Shifts
{rel_text or '(none)'}
## World State Changes
{ws_text or '(no significant changes)'}

Based on this data, generate the structured conclusion JSON."""

    return prompt


async def generate_conclusion(
    client,
    runtime_summary: dict[str, Any],
    key_moments: list[dict[str, Any]],
    script: dict[str, Any],
) -> dict[str, Any]:
    """Generate a structured conclusion for a completed simulation.

    Args:
        client: LLMClient instance with generate() method.
        runtime_summary: Full runtime summary from the graph runner.
        key_moments: Extracted key moments list.
        script: The simulation script dict.

    Returns:
        Conclusion dict with mode-specific fields.
    """
    mode = script.get("simulation_mode", "guided")
    system = GUIDED_SYSTEM if mode == "guided" else EXPLORATORY_SYSTEM
    prompt = _build_conclusion_prompt(runtime_summary, key_moments, script)

    try:
        raw = await client.generate(
            prompt=prompt,
            system_instruction=system,
            temperature=0.4,
            max_tokens=1200,
        )

        # Strip markdown code fences if present
        text = raw.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        conclusion = json.loads(text)
        conclusion["mode"] = mode
        return conclusion

    except (json.JSONDecodeError, Exception) as exc:
        logger.warning("Conclusion generation failed: %s", exc)
        # Fallback: return a minimal conclusion from available data
        actor_names = runtime_summary.get("actor_display_names", {})
        arcs = []
        for actor in script.get("stakeholders", []):
            arcs.append({
                "actor_id": actor.get("actor_id", ""),
                "role": actor.get("role", ""),
                "arc": f"Participated in the simulation as {actor.get('role', '')}.",
            })

        if mode == "guided":
            return {
                "mode": "guided",
                "outcome_achieved": "partial",
                "outcome_summary": f"The simulation '{script.get('title', '')}' completed with {len(runtime_summary.get('turns', []))} turns across {len(runtime_summary.get('phase_order', []))} phases.",
                "contributing_factors": [],
                "actor_arcs": arcs,
                "unresolved_tensions": [],
            }
        else:
            return {
                "mode": "exploratory",
                "outcome_summary": f"The simulation '{script.get('title', '')}' explored stakeholder dynamics across {len(runtime_summary.get('turns', []))} turns.",
                "key_discoveries": [],
                "actor_arcs": arcs,
                "unresolved_tensions": [],
                "emergent_patterns": [],
            }
