"""Extract the top-k key moments from a completed simulation.

Each key moment represents a turning point: the largest relationship shift,
highest drift spike, significant action, phase transition, or commitment event.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class KeyMoment:
    """A single pivotal moment in the simulation."""

    turn_index: int
    phase_name: str
    event_type: str  # relationship_shift | action | drift_spike | phase_change | commitment
    title: str  # auto-generated one-liner
    description: str  # longer explanation
    evidence: str  # the actual dialogue text or event detail
    impact: dict[str, Any] = field(default_factory=dict)  # state changes caused
    actors_involved: list[str] = field(default_factory=list)
    score: float = 0.0  # internal ranking score

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def extract_key_moments(runtime_summary: dict[str, Any], k: int = 5) -> list[dict[str, Any]]:
    """Extract the top-k pivotal moments from a runtime summary.

    Detection criteria (scored & ranked):
    1. Largest trust_delta in relationship_events (|delta| > 0.1)
    2. Largest world_state change from executed_actions
    3. Phase transition moments
    4. Significant action events (escalation, commitment)
    """
    candidates: list[KeyMoment] = []
    turns = runtime_summary.get("turns", [])
    relationship_events = runtime_summary.get("relationship_events", [])
    executed_actions = runtime_summary.get("executed_actions", [])
    actor_state_events = runtime_summary.get("actor_state_events", [])
    actor_names = runtime_summary.get("actor_display_names", {})
    phase_order = runtime_summary.get("phase_order", [])

    # Build turn lookup for evidence text
    turn_map: dict[int, dict[str, Any]] = {}
    for turn in turns:
        idx = turn.get("turn_index", -1)
        turn_map[idx] = turn

    # 1. Relationship shifts
    for evt in relationship_events:
        trust_delta = evt.get("trust_delta", 0.0)
        tension_delta = evt.get("tension_delta", 0.0)
        magnitude = abs(trust_delta) + abs(tension_delta) * 0.5
        if magnitude < 0.05:
            continue

        turn_idx = evt.get("turn_index", 0)
        source = evt.get("source_actor_id", evt.get("source", ""))
        target = evt.get("target_actor_id", evt.get("target", ""))
        source_name = actor_names.get(source, source)
        target_name = actor_names.get(target, target)
        phase = evt.get("phase_name", "")

        evidence_text = evt.get("evidence", "")
        if not evidence_text and turn_idx in turn_map:
            evidence_text = turn_map[turn_idx].get("content", "")[:200]

        direction = "dropped" if trust_delta < 0 else "rose"
        title = f"{source_name} → {target_name}: trust {direction} {trust_delta:+.2f}"

        candidates.append(KeyMoment(
            turn_index=turn_idx,
            phase_name=phase,
            event_type="relationship_shift",
            title=title,
            description=f"Trust between {source_name} and {target_name} shifted by {trust_delta:+.2f}",
            evidence=evidence_text[:300],
            impact={"trust_delta": trust_delta, "tension_delta": tension_delta},
            actors_involved=[source, target],
            score=magnitude * 10,
        ))

    # 2. Executed actions with large state deltas
    for action in executed_actions:
        delta = action.get("applied_delta", {})
        if not delta:
            continue
        magnitude = sum(abs(v) for v in delta.values())
        if magnitude < 0.05:
            continue

        actor_id = action.get("owner_actor_id", "")
        actor_name = actor_names.get(actor_id, actor_id)
        action_type = action.get("action_type", "unknown")
        target_key = action.get("target_key", "")
        phase = action.get("phase_name", "")

        # Find the turn closest to this action
        turn_idx = 0
        for t in turns:
            if t.get("actor_id") == actor_id:
                turn_idx = t.get("turn_index", 0)

        title = f"{actor_name} {action_type.replace('_', ' ')}"
        if target_key:
            title += f" → {target_key}"

        delta_desc = ", ".join(f"{k}: {v:+.2f}" for k_v in [(k, v) for k, v in delta.items()])
        evidence_text = f"Action: {action_type} | Deltas: {delta_desc}"

        candidates.append(KeyMoment(
            turn_index=turn_idx,
            phase_name=phase,
            event_type="action",
            title=title,
            description=f"{actor_name} performed {action_type.replace('_', ' ')}",
            evidence=evidence_text[:300],
            impact={"state_deltas": delta},
            actors_involved=[actor_id],
            score=magnitude * 8,
        ))

    # 3. Phase transitions
    for i, phase_name in enumerate(phase_order):
        if i == 0:
            continue
        prev_phase = phase_order[i - 1]
        # Find the first turn in this phase
        phase_turns = [t for t in turns if t.get("phase_name") == phase_name]
        turn_idx = phase_turns[0].get("turn_index", 0) if phase_turns else 0

        candidates.append(KeyMoment(
            turn_index=turn_idx,
            phase_name=phase_name,
            event_type="phase_change",
            title=f"Phase shift: {prev_phase} → {phase_name}",
            description=f"Simulation transitioned from {prev_phase} to {phase_name}",
            evidence=f"Phase boundary reached after turn {turn_idx}",
            impact={"from_phase": prev_phase, "to_phase": phase_name},
            actors_involved=[],
            score=3.0,
        ))

    # 4. Drift spikes from actor_state_events
    for evt in actor_state_events:
        drift = evt.get("drift_score", 0.0)
        if drift < 0.15:
            continue
        actor_id = evt.get("actor_id", "")
        actor_name = actor_names.get(actor_id, actor_id)
        turn_idx = evt.get("turn_index", 0)
        phase = evt.get("phase_name", "")

        evidence_text = ""
        if turn_idx in turn_map:
            evidence_text = turn_map[turn_idx].get("content", "")[:200]

        candidates.append(KeyMoment(
            turn_index=turn_idx,
            phase_name=phase,
            event_type="drift_spike",
            title=f"{actor_name} persona drift: {drift:.2f}",
            description=f"{actor_name} deviated significantly from target personality (drift={drift:.2f})",
            evidence=evidence_text[:300],
            impact={"drift_score": drift},
            actors_involved=[actor_id],
            score=drift * 15,
        ))

    # Sort by score descending and take top k
    candidates.sort(key=lambda m: m.score, reverse=True)

    # Deduplicate by turn_index (keep highest-scored per turn)
    seen_turns: set[int] = set()
    deduped: list[KeyMoment] = []
    for moment in candidates:
        if moment.turn_index not in seen_turns:
            deduped.append(moment)
            seen_turns.add(moment.turn_index)
        if len(deduped) >= k:
            break

    # Sort final list by turn_index for chronological presentation
    deduped.sort(key=lambda m: m.turn_index)

    return [m.to_dict() for m in deduped]
