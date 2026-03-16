"""Post-hoc influence attribution from simulation trace data.

Detects decision points (commitment creation, stance reversals, trait drift
spikes, sentiment flips) and measures which actors influenced those decisions
using relationship trust/tension deltas, content alignment, trait pull, and
direct address frequency.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any


# ── Weight vector for composite influence score ──────────────────────────────

_INFLUENCE_WEIGHTS = {
    "trust_delta": 0.30,
    "content_alignment": 0.25,
    "trait_pull": 0.20,
    "direct_address_count": 0.15,
    "tension_delta": 0.10,
}


# ── Step 1: Detect Decision Points ──────────────────────────────────────────

def detect_decision_points(runtime_summary: dict[str, Any]) -> list[dict[str, Any]]:
    """Scan actor_state_events for significant state changes.

    A decision point is detected when any of:
    1. New commitment created (open_commitments count increased)
    2. Stance reversal (stance_map sign change)
    3. Large trait drift spike (drift_delta > 0.05 in single turn)
    4. Sentiment flip in relationship
    """
    actor_state_events = runtime_summary.get("actor_state_events") or []
    relationship_events = runtime_summary.get("relationship_events") or []
    decision_points: list[dict[str, Any]] = []

    for event in actor_state_events:
        actor_id = event.get("actor_id", "")
        turn_index = int(event.get("turn_index", 0))
        phase_name = event.get("phase_name", "")
        prior_state = event.get("prior_state") or {}
        new_state = event.get("new_state") or {}

        # 1. Commitment created
        prior_commitments = len(prior_state.get("open_commitments", []))
        new_commitments = len(new_state.get("open_commitments", []))
        if new_commitments > prior_commitments:
            decision_points.append({
                "actor_id": actor_id,
                "turn_index": turn_index,
                "phase_name": phase_name,
                "decision_type": "commitment_created",
                "description": f"{actor_id} created {new_commitments - prior_commitments} new commitment(s)",
                "prior_state_snapshot": _compact_state(prior_state),
                "new_state_snapshot": _compact_state(new_state),
            })

        # 2. Stance reversal (check stance_map for sign changes)
        prior_stance = prior_state.get("stance_map") or {}
        new_stance = new_state.get("stance_map") or {}
        for target, old_val in prior_stance.items():
            new_val = new_stance.get(target)
            if new_val is not None:
                try:
                    old_f, new_f = float(old_val), float(new_val)
                    if old_f * new_f < 0 and abs(old_f) > 0.1 and abs(new_f) > 0.1:
                        decision_points.append({
                            "actor_id": actor_id,
                            "turn_index": turn_index,
                            "phase_name": phase_name,
                            "decision_type": "stance_reversal",
                            "description": f"{actor_id} reversed stance toward {target} ({old_f:+.2f} → {new_f:+.2f})",
                            "prior_state_snapshot": _compact_state(prior_state),
                            "new_state_snapshot": _compact_state(new_state),
                        })
                except (TypeError, ValueError):
                    pass

        # 3. Trait drift spike
        prior_drift = _safe_float(prior_state.get("drift_score"))
        new_drift = _safe_float(new_state.get("drift_score"))
        if prior_drift is not None and new_drift is not None:
            drift_delta = new_drift - prior_drift
            if abs(drift_delta) > 0.05:
                decision_points.append({
                    "actor_id": actor_id,
                    "turn_index": turn_index,
                    "phase_name": phase_name,
                    "decision_type": "trait_drift_spike",
                    "description": f"{actor_id} drift spike {drift_delta:+.3f} (→{new_drift:.3f})",
                    "prior_state_snapshot": _compact_state(prior_state),
                    "new_state_snapshot": _compact_state(new_state),
                })

    # 4. Sentiment flip from relationship events
    rel_by_edge: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for event in relationship_events:
        source = event.get("source_actor_id", "")
        target = event.get("target_actor_id", "")
        rel_by_edge[(source, target)].append(event)

    _POSITIVE = {"positive"}
    _NEGATIVE = {"negative", "challenging"}
    for (source, target), events in rel_by_edge.items():
        sorted_events = sorted(events, key=lambda e: int(e.get("turn_index", 0)))
        for i in range(1, len(sorted_events)):
            prev_sent = sorted_events[i - 1].get("new_sentiment") or sorted_events[i - 1].get("sentiment", "neutral")
            curr_sent = sorted_events[i].get("new_sentiment") or sorted_events[i].get("sentiment", "neutral")
            if (prev_sent in _POSITIVE and curr_sent in _NEGATIVE) or (prev_sent in _NEGATIVE and curr_sent in _POSITIVE):
                decision_points.append({
                    "actor_id": source,
                    "turn_index": int(sorted_events[i].get("turn_index", 0)),
                    "phase_name": sorted_events[i].get("phase_name", ""),
                    "decision_type": "sentiment_flip",
                    "description": f"{source} sentiment toward {target} flipped: {prev_sent} → {curr_sent}",
                    "prior_state_snapshot": {},
                    "new_state_snapshot": {},
                })

    return decision_points


# ── Step 2: Compute Influence Signals ────────────────────────────────────────

def compute_influence_signals(
    decision_point: dict[str, Any],
    relationship_events: list[dict[str, Any]],
    actor_state_events: list[dict[str, Any]],
    turns: list[dict[str, Any]],
    lookback_window: int = 5,
) -> list[dict[str, Any]]:
    """For each other actor, compute influence strength on the decision."""
    actor_id = decision_point["actor_id"]
    turn_index = decision_point["turn_index"]
    min_turn = max(0, turn_index - lookback_window)

    # Identify all other actors from turns
    all_actors = {t.get("actor_id") or t.get("speaker_name", "") for t in turns}
    all_actors.discard(actor_id)
    all_actors.discard("")

    # Content of the decision turn (for alignment measurement)
    decision_content = ""
    for t in turns:
        t_idx = int(t.get("turn_index") or t.get("turn_number", 0))
        t_actor = t.get("actor_id") or t.get("speaker_name", "")
        if t_idx == turn_index and t_actor == actor_id:
            decision_content = (t.get("content") or "").lower()
            break

    decision_tokens = set(decision_content.split()) if decision_content else set()

    influences: list[dict[str, Any]] = []
    for influencer_id in all_actors:
        # 1. Trust delta in lookback window
        trust_delta = 0.0
        tension_delta_val = 0.0
        for rel_event in relationship_events:
            if int(rel_event.get("turn_index", 0)) < min_turn or int(rel_event.get("turn_index", 0)) > turn_index:
                continue
            source = rel_event.get("source_actor_id", "")
            target = rel_event.get("target_actor_id", "")
            if source == influencer_id and target == actor_id:
                trust_delta += float(rel_event.get("trust_delta", 0.0) or 0.0)
                tension_delta_val += float(rel_event.get("tension_delta", 0.0) or 0.0)
            elif source == actor_id and target == influencer_id:
                # Also consider the reverse — how the decider's trust in the influencer changed
                new_trust = _safe_float(rel_event.get("new_trust"))
                prior_trust = _safe_float(rel_event.get("prior_trust"))
                if new_trust is not None and prior_trust is not None:
                    trust_delta += new_trust - prior_trust
                new_tension = _safe_float(rel_event.get("new_tension"))
                prior_tension = _safe_float(rel_event.get("prior_tension"))
                if new_tension is not None and prior_tension is not None:
                    tension_delta_val += new_tension - prior_tension

        # 2. Content alignment (token overlap)
        influencer_content = ""
        direct_address_count = 0
        for t in turns:
            t_idx = int(t.get("turn_index") or t.get("turn_number", 0))
            t_actor = t.get("actor_id") or t.get("speaker_name", "")
            if t_actor == influencer_id and min_turn <= t_idx <= turn_index:
                content = (t.get("content") or "").lower()
                influencer_content += " " + content
                # Direct address: check if influencer mentions the decider's name
                actor_display = _display_name_for_id(actor_id, turns)
                if actor_display and actor_display.lower() in content:
                    direct_address_count += 1

        influencer_tokens = set(influencer_content.split()) if influencer_content else set()
        if decision_tokens and influencer_tokens:
            overlap = len(decision_tokens & influencer_tokens)
            union = len(decision_tokens | influencer_tokens)
            content_alignment = overlap / max(union, 1)
        else:
            content_alignment = 0.0

        # 3. Trait pull: did the influencer's personality direction match the decider's drift?
        trait_pull = 0.0
        influencer_traits = _latest_traits_before(influencer_id, turn_index, actor_state_events)
        decider_prior_traits = _latest_traits_before(actor_id, min_turn, actor_state_events)
        decider_new_traits = _latest_traits_before(actor_id, turn_index + 1, actor_state_events)
        if influencer_traits and decider_prior_traits and decider_new_traits:
            alignment_score = 0.0
            count = 0
            for trait_key in ("O", "C", "E", "A", "N"):
                inf_val = influencer_traits.get(trait_key)
                prior_val = decider_prior_traits.get(trait_key)
                new_val = decider_new_traits.get(trait_key)
                if inf_val is not None and prior_val is not None and new_val is not None:
                    drift_direction = new_val - prior_val
                    pull_direction = inf_val - prior_val
                    if abs(pull_direction) > 0.01:
                        alignment_score += 1.0 if (drift_direction * pull_direction > 0) else -0.5
                        count += 1
            trait_pull = (alignment_score / max(count, 1)) * 0.5 + 0.5 if count else 0.0

        # Composite influence score
        raw_signals = {
            "trust_delta": abs(trust_delta),
            "content_alignment": content_alignment,
            "trait_pull": max(0.0, trait_pull),
            "direct_address_count": min(direct_address_count, 5) / 5.0,
            "tension_delta": abs(tension_delta_val),
        }
        influence_score = sum(
            raw_signals[signal] * weight
            for signal, weight in _INFLUENCE_WEIGHTS.items()
        )
        influence_score = min(1.0, influence_score)

        # Extract evidence excerpts
        evidence_excerpts = _extract_evidence_excerpts(influencer_id, min_turn, turn_index, turns)

        influences.append({
            "influencer_actor_id": influencer_id,
            "influence_score": round(influence_score, 4),
            "signal_breakdown": {
                "trust_delta": round(trust_delta, 4),
                "tension_delta": round(tension_delta_val, 4),
                "content_alignment": round(content_alignment, 4),
                "trait_pull": round(trait_pull, 4),
                "direct_address_count": direct_address_count,
            },
            "evidence_excerpts": evidence_excerpts[:2],
        })

    # Sort by influence score descending
    influences.sort(key=lambda x: x["influence_score"], reverse=True)
    for rank, inf in enumerate(influences, 1):
        inf["rank"] = rank

    return influences


# ── Step 3: Build Influence Attribution ──────────────────────────────────────

def build_influence_attribution(runtime_summary: dict[str, Any]) -> dict[str, Any]:
    """Top-level function. Returns influence attribution for all decision points."""
    decision_points = detect_decision_points(runtime_summary)
    relationship_events = runtime_summary.get("relationship_events") or []
    actor_state_events = runtime_summary.get("actor_state_events") or []
    turns = runtime_summary.get("turns") or []

    enriched_points: list[dict[str, Any]] = []
    for dp in decision_points:
        influences = compute_influence_signals(
            decision_point=dp,
            relationship_events=relationship_events,
            actor_state_events=actor_state_events,
            turns=turns,
        )
        # Generate narrative for top-2 influences
        narrative = _generate_narrative(dp, influences[:2])
        enriched_points.append({
            **dp,
            "influences": influences[:5],  # Top 5 influencers
            "narrative": narrative,
        })

    # Summary statistics
    most_influential: str = ""
    influence_counts: dict[str, int] = defaultdict(int)
    concentration_values: list[float] = []
    type_counts: dict[str, int] = defaultdict(int)

    for ep in enriched_points:
        type_counts[ep["decision_type"]] = type_counts.get(ep["decision_type"], 0) + 1
        if ep["influences"]:
            top = ep["influences"][0]
            influence_counts[top["influencer_actor_id"]] += 1
            # Concentration: how much the top influencer dominates
            total_score = sum(inf["influence_score"] for inf in ep["influences"])
            if total_score > 0:
                concentration_values.append(top["influence_score"] / total_score)

    if influence_counts:
        most_influential = max(influence_counts, key=influence_counts.get)

    return {
        "decision_points": enriched_points[:20],  # Cap to keep payload manageable
        "summary": {
            "total_decision_points": len(decision_points),
            "most_influential_actor": most_influential,
            "mean_influence_concentration": round(
                sum(concentration_values) / max(len(concentration_values), 1), 4
            ),
            "decision_type_counts": dict(type_counts),
        },
    }


# ── Helpers ──────────────────────────────────────────────────────────────────

def _safe_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _compact_state(state: dict[str, Any]) -> dict[str, Any]:
    """Extract only the fields useful for decision point display."""
    keep_keys = (
        "drift_score", "stance_map", "trust_map",
        "rolling_trait_estimate", "open_commitments", "beliefs",
    )
    return {k: v for k, v in state.items() if k in keep_keys and v}


def _display_name_for_id(actor_id: str, turns: list[dict[str, Any]]) -> str:
    """Find display name for an actor_id from turns."""
    for t in turns:
        if (t.get("actor_id") or "") == actor_id:
            return t.get("display_name") or t.get("speaker_name") or ""
    return ""


def _latest_traits_before(
    actor_id: str,
    before_turn: int,
    actor_state_events: list[dict[str, Any]],
) -> dict[str, float] | None:
    """Find the latest rolling_trait_estimate for an actor before a given turn."""
    best: dict[str, float] | None = None
    best_turn = -1
    for event in actor_state_events:
        if event.get("actor_id") != actor_id:
            continue
        turn_idx = int(event.get("turn_index", 0))
        if turn_idx >= before_turn:
            continue
        new_state = event.get("new_state") or {}
        traits = new_state.get("rolling_trait_estimate")
        if traits and turn_idx > best_turn:
            best = dict(traits)
            best_turn = turn_idx
    return best


def _extract_evidence_excerpts(
    actor_id: str,
    min_turn: int,
    max_turn: int,
    turns: list[dict[str, Any]],
) -> list[str]:
    """Extract short content excerpts from an actor's turns in the window."""
    excerpts: list[str] = []
    for t in turns:
        t_actor = t.get("actor_id") or t.get("speaker_name", "")
        t_idx = int(t.get("turn_index") or t.get("turn_number", 0))
        if t_actor == actor_id and min_turn <= t_idx <= max_turn:
            content = (t.get("content") or "").strip()
            if content:
                excerpts.append(content[:200])
    return excerpts


def _generate_narrative(
    decision_point: dict[str, Any],
    top_influences: list[dict[str, Any]],
) -> str:
    """Generate a human-readable narrative for a decision point."""
    actor = decision_point["actor_id"]
    decision_type = decision_point["decision_type"]
    description = decision_point.get("description", "")

    if not top_influences:
        return f"{actor}: {description}. No measurable external influence detected."

    parts = [f"{actor}: {description}."]
    for inf in top_influences:
        influencer = inf["influencer_actor_id"]
        score = inf["influence_score"]
        signals = inf["signal_breakdown"]
        # Pick the dominant signal
        signal_items = [
            ("trust", abs(signals.get("trust_delta", 0.0))),
            ("content alignment", signals.get("content_alignment", 0.0)),
            ("trait pull", signals.get("trait_pull", 0.0)),
            ("direct address", signals.get("direct_address_count", 0) / 5.0),
            ("tension", abs(signals.get("tension_delta", 0.0))),
        ]
        signal_items.sort(key=lambda x: x[1], reverse=True)
        dominant = signal_items[0][0] if signal_items else "unknown"
        parts.append(f"{influencer} (score={score:.2f}, key signal: {dominant})")

    return " ".join(parts)
