"""Game Theory Post-Hoc Analysis Module.

Classifies actor interactions as cooperate/defect/conditional, matches
iterated-game strategies (tit-for-tat, pavlov, …), and computes rationality
/ exploitability metrics.  Designed to run on benchmark output directories
produced by ``run_final_benchmark.py``.

Standalone usage::

    python3 -m simulation_engine.game_theory_analysis simulation_engine/results_thesis_final
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from statistics import mean, pstdev
from typing import Any

# ── Data classes ─────────────────────────────────────────────────────────────


@dataclass
class TurnClassification:
    run_id: str
    actor_id: str
    target_actor_id: str
    turn_index: int
    phase_name: str
    move: str  # "cooperate" | "defect" | "conditional"
    confidence: float
    signal_breakdown: dict[str, float]


@dataclass
class ActorPairStrategy:
    run_id: str
    actor_id: str
    target_actor_id: str
    condition: str
    move_sequence: list[str]
    best_match_strategy: str
    match_confidence: float
    all_strategy_scores: dict[str, float]


@dataclass
class RunGameTheoryResult:
    run_id: str
    condition: str
    simulation_id: str
    actor_count: int
    pair_strategies: list[ActorPairStrategy]
    dominant_strategy_distribution: dict[str, int]
    cooperation_rate: float
    conditional_cooperation_rate: float
    rationality_score: float
    exploitability: float


@dataclass
class GameTheoryAnalysisResults:
    per_run: list[RunGameTheoryResult]
    aggregate_by_condition: dict[str, dict]
    aggregate_by_actor_count: dict[str, dict]
    strategy_distribution_by_condition: dict[str, dict[str, float]]
    statistical_tests: dict[str, dict[str, float]]
    # Scenario-level analysis
    aggregate_by_scenario: dict[str, dict] = field(default_factory=dict)
    scenario_statistical_tests: dict[str, dict] = field(default_factory=dict)


# ── Constants ────────────────────────────────────────────────────────────────

# Cooperative / defecting intent keywords from policy_plan
_COOPERATE_STANCES = {"support", "synthesize", "coordinate", "collaborate", "align"}
_DEFECT_STANCES = {"oppose", "protect", "challenge", "resist", "block"}

_COOPERATE_ACTIONS = {
    "commit_resource", "publish_update", "assign_owner", "propose_outcome",
    "share_data", "endorse", "accept_proposal", "coordinate",
}
_DEFECT_ACTIONS = {
    "escalate", "preserve_autonomy", "narrow_scope", "reject_proposal",
    "block", "withdraw", "veto", "request_evidence",
}

_COOPERATE_SENTIMENTS = {"positive"}
_DEFECT_SENTIMENTS = {"negative", "challenging"}

# Payoff matrices  (R, S, T, P)
PAYOFF_POLICY = {"R": 3, "S": 0, "T": 5, "P": 1}       # high stakes
PAYOFF_NON_POLICY = {"R": 4, "S": 1, "T": 5, "P": 2}   # collaboration upside

# Policy-related scenario families
_POLICY_FAMILIES = {
    "government_algorithm_failure", "public_safety_failure",
    "environmental_policy", "labor_rights", "housing_policy",
    "transportation_policy", "immigration_policy", "gig_economy_regulation",
    "data_privacy_regulation", "nuclear_energy_policy", "homelessness_policy",
    "congestion_pricing",
}

# ── Data loading ─────────────────────────────────────────────────────────────


def _load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file into a list of dicts.  Returns [] if missing."""
    if not path.exists():
        return []
    items: list[dict] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    items.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return items


def _load_trace_data(results_dir: Path) -> dict[str, list[dict]]:
    """Load trace_views JSONL files into keyed lists."""
    tv = results_dir / "trace_views"
    return {
        "turn_decisions": _load_jsonl(tv / "turn_decisions.jsonl"),
        "action_events": _load_jsonl(tv / "action_events.jsonl"),
        "relationship_events": _load_jsonl(tv / "relationship_events.jsonl"),
        "candidate_scores": _load_jsonl(tv / "candidate_scores.jsonl"),
    }


def _load_run_data(results_dir: Path) -> list[dict]:
    """Load run data from benchmark_runs.json or run_outcomes.json fallback.

    Checkpoint resume can produce duplicate entries with the same run_id.
    We keep the last occurrence of each run_id (most up-to-date metrics).

    When benchmark_runs.json is absent (e.g. excluded from git due to size),
    falls back to run_outcomes.json, extracting condition from run_id and
    mapping headline_metrics → metrics.
    """
    path = results_dir / "benchmark_runs.json"
    if path.exists():
        with open(path) as f:
            data = json.load(f)
        raw_runs = data.get("runs", [])
    else:
        # Fallback: run_outcomes.json
        fallback = results_dir / "run_outcomes.json"
        if not fallback.exists():
            raise FileNotFoundError(
                f"Neither benchmark_runs.json nor run_outcomes.json found in {results_dir}"
            )
        print("  [game_theory] benchmark_runs.json not found, using run_outcomes.json fallback", flush=True)
        with open(fallback) as f:
            outcomes = json.load(f)
        raw_runs = []
        for o in outcomes:
            run_id = o.get("run_id", "")
            parts = run_id.split(":")
            condition = parts[3] if len(parts) >= 4 else "unknown"
            raw_runs.append({
                "run_id": run_id,
                "condition": condition,
                "simulation_id": o.get("simulation_id", ""),
                "suite_id": o.get("suite_id", ""),
                "track_id": o.get("track_id", ""),
                "metrics": o.get("headline_metrics", {}),
            })

    # Deduplicate by run_id, keeping last occurrence
    seen: dict[str, dict] = {}
    for run in raw_runs:
        rid = run.get("run_id", "")
        if rid:
            seen[rid] = run
    deduped = list(seen.values())

    if len(deduped) < len(raw_runs):
        print(f"  [game_theory] Deduplicated {len(raw_runs)} → {len(deduped)} runs", flush=True)

    return deduped


# ── Index builders ───────────────────────────────────────────────────────────


def _build_relationship_index(
    events: list[dict],
) -> dict[str, list[dict]]:
    """Index relationship_events by run_id → list of events."""
    idx: dict[str, list[dict]] = {}
    for ev in events:
        # Extract run_id from turn_trace_id
        ttid = ev.get("turn_trace_id", "")
        # run_id = everything before the simulation_id repetition
        # Format: suite:track:sim_id:condition:rep:sim_id:PHASE:turn:actor
        parts = ttid.split(":")
        if len(parts) >= 5:
            run_id = ":".join(parts[:5])
        else:
            continue
        idx.setdefault(run_id, []).append(ev)
    return idx


def _build_turn_decision_index(
    decisions: list[dict],
) -> dict[str, list[dict]]:
    """Index turn_decisions by run_id → list of decisions."""
    idx: dict[str, list[dict]] = {}
    for td in decisions:
        run_id = td.get("run_id", "")
        if run_id:
            idx.setdefault(run_id, []).append(td)
    return idx


def _build_action_event_index(
    events: list[dict],
) -> dict[str, list[dict]]:
    """Index action_events by run_id (derived from turn_trace_id)."""
    idx: dict[str, list[dict]] = {}
    for ev in events:
        ttid = ev.get("turn_trace_id", "")
        parts = ttid.split(":")
        if len(parts) >= 5:
            run_id = ":".join(parts[:5])
        else:
            continue
        idx.setdefault(run_id, []).append(ev)
    return idx


def _build_candidate_score_index(
    scores: list[dict],
) -> dict[str, list[dict]]:
    """Index candidate_scores by run_id (derived from turn_trace_id).
    Only keeps selected candidates to save memory."""
    idx: dict[str, list[dict]] = {}
    for cs in scores:
        if not cs.get("selected", False):
            continue
        ttid = cs.get("turn_trace_id", "")
        parts = ttid.split(":")
        if len(parts) >= 5:
            run_id = ":".join(parts[:5])
        else:
            continue
        idx.setdefault(run_id, []).append(cs)
    return idx


# ── Turn classification ─────────────────────────────────────────────────────


def _intent_signal(policy_plan: dict) -> tuple[float, float]:
    """Return (cooperate_score, defect_score) from policy_plan intent."""
    stance = (policy_plan.get("stance") or "").lower()
    goal = (policy_plan.get("goal_mode") or "").lower()

    coop = 0.0
    defect = 0.0

    if stance in _COOPERATE_STANCES:
        coop += 0.6
    elif stance in _DEFECT_STANCES:
        defect += 0.6

    if goal in {"synthesize", "promote", "coordinate", "collaborate"}:
        coop += 0.4
    elif goal in {"protect", "oppose", "block", "resist"}:
        defect += 0.4

    return (min(coop, 1.0), min(defect, 1.0))


def _action_signal(action_events: list[dict], actor_id: str, turn_index: int) -> tuple[float, float]:
    """Return (cooperate_score, defect_score) from action_events."""
    relevant = [
        ae for ae in action_events
        if ae.get("actor_id") == actor_id
        and ae.get("compiled_proposal", {}).get("turn_index") == turn_index
    ]
    if not relevant:
        return (0.5, 0.5)  # neutral when no data

    coop_count = 0
    defect_count = 0
    for ae in relevant:
        action_type = (ae.get("compiled_proposal", {}).get("action_type") or "").lower()
        if action_type in _COOPERATE_ACTIONS:
            coop_count += 1
        elif action_type in _DEFECT_ACTIONS:
            defect_count += 1

    total = coop_count + defect_count
    if total == 0:
        return (0.5, 0.5)
    return (coop_count / total, defect_count / total)


def _relational_signal(
    rel_events: list[dict],
    actor_id: str,
    target_id: str,
    turn_index: int,
) -> tuple[float, float]:
    """Return (cooperate_score, defect_score) from relationship_events."""
    relevant = [
        re for re in rel_events
        if re.get("source_actor_id") == actor_id
        and re.get("target_actor_id") == target_id
        and re.get("turn_index") == turn_index
    ]
    if not relevant:
        return (0.5, 0.5)

    coop_signals = 0.0
    defect_signals = 0.0
    for re in relevant:
        sentiment = (re.get("new_sentiment") or "neutral").lower()
        trust_delta = re.get("trust_delta", 0.0)

        if sentiment in _COOPERATE_SENTIMENTS:
            coop_signals += 0.5
        elif sentiment in _DEFECT_SENTIMENTS:
            defect_signals += 0.5

        if trust_delta > 0:
            coop_signals += 0.5
        elif trust_delta < 0:
            defect_signals += 0.5

    total = coop_signals + defect_signals
    if total == 0:
        return (0.5, 0.5)
    return (coop_signals / total, defect_signals / total)


def _linguistic_signal(feature_counts: dict) -> tuple[float, float]:
    """Return (cooperate_score, defect_score) from behavioral feature counts."""
    ack = feature_counts.get("acknowledgment_count", 0) or 0
    inclusive = feature_counts.get("inclusive_pronoun_ratio", 0) or 0
    disagree = feature_counts.get("disagreement_count", 0) or 0
    negation = feature_counts.get("negation_count", 0) or 0

    coop = 0.0
    defect = 0.0

    if ack > 0:
        coop += 0.4
    if inclusive > 0.03:
        coop += 0.3
    if disagree > 0:
        defect += 0.4
    if negation > 2:
        defect += 0.3

    # Add softer signals
    positive_emo = feature_counts.get("positive_emotion_count", 0) or 0
    if positive_emo > 0:
        coop += 0.15
    reference_back = feature_counts.get("reference_back_count", 0) or 0
    if reference_back > 0:
        coop += 0.15

    total = coop + defect
    if total == 0:
        return (0.5, 0.5)
    return (min(coop / max(total, 0.01), 1.0), min(defect / max(total, 0.01), 1.0))


def classify_turn_pairwise(
    run_id: str,
    actor_id: str,
    target_id: str,
    turn_index: int,
    phase_name: str,
    is_engine: bool,
    *,
    policy_plan: dict | None = None,
    action_events: list[dict] | None = None,
    rel_events: list[dict] | None = None,
    feature_counts: dict | None = None,
) -> TurnClassification:
    """Classify a single turn as cooperate / defect / conditional."""
    breakdown: dict[str, float] = {}
    coop_total = 0.0
    defect_total = 0.0

    if is_engine:
        # 4-signal classification
        # Intent (0.30)
        if policy_plan:
            ic, id_ = _intent_signal(policy_plan)
            breakdown["intent_coop"] = round(ic, 3)
            breakdown["intent_defect"] = round(id_, 3)
            coop_total += 0.30 * ic
            defect_total += 0.30 * id_
        else:
            coop_total += 0.30 * 0.5
            defect_total += 0.30 * 0.5

        # Action (0.25)
        if action_events is not None:
            ac, ad = _action_signal(action_events, actor_id, turn_index)
            breakdown["action_coop"] = round(ac, 3)
            breakdown["action_defect"] = round(ad, 3)
            coop_total += 0.25 * ac
            defect_total += 0.25 * ad
        else:
            coop_total += 0.25 * 0.5
            defect_total += 0.25 * 0.5

        # Relational (0.25)
        if rel_events is not None:
            rc, rd = _relational_signal(rel_events, actor_id, target_id, turn_index)
            breakdown["relational_coop"] = round(rc, 3)
            breakdown["relational_defect"] = round(rd, 3)
            coop_total += 0.25 * rc
            defect_total += 0.25 * rd
        else:
            coop_total += 0.25 * 0.5
            defect_total += 0.25 * 0.5

        # Linguistic (0.20)
        if feature_counts:
            lc, ld = _linguistic_signal(feature_counts)
            breakdown["linguistic_coop"] = round(lc, 3)
            breakdown["linguistic_defect"] = round(ld, 3)
            coop_total += 0.20 * lc
            defect_total += 0.20 * ld
        else:
            coop_total += 0.20 * 0.5
            defect_total += 0.20 * 0.5
    else:
        # Naive: 2-signal classification (relational 0.55 + linguistic 0.45)
        if rel_events is not None:
            rc, rd = _relational_signal(rel_events, actor_id, target_id, turn_index)
            breakdown["relational_coop"] = round(rc, 3)
            breakdown["relational_defect"] = round(rd, 3)
            coop_total += 0.55 * rc
            defect_total += 0.55 * rd
        else:
            coop_total += 0.55 * 0.5
            defect_total += 0.55 * 0.5

        if feature_counts:
            lc, ld = _linguistic_signal(feature_counts)
            breakdown["linguistic_coop"] = round(lc, 3)
            breakdown["linguistic_defect"] = round(ld, 3)
            coop_total += 0.45 * lc
            defect_total += 0.45 * ld
        else:
            coop_total += 0.45 * 0.5
            defect_total += 0.45 * 0.5

    # Threshold decision
    total = coop_total + defect_total
    if total > 0:
        coop_score = coop_total / total
    else:
        coop_score = 0.5

    if coop_score >= 0.60:
        move = "cooperate"
        confidence = coop_score
    elif coop_score <= 0.40:
        move = "defect"
        confidence = 1.0 - coop_score
    else:
        move = "conditional"
        confidence = 1.0 - abs(coop_score - 0.5) * 2  # lower confidence near 0.5

    return TurnClassification(
        run_id=run_id,
        actor_id=actor_id,
        target_actor_id=target_id,
        turn_index=turn_index,
        phase_name=phase_name,
        move=move,
        confidence=round(confidence, 3),
        signal_breakdown=breakdown,
    )


def classify_all_turns(
    runs: list[dict],
    td_index: dict[str, list[dict]],
    rel_index: dict[str, list[dict]],
    ae_index: dict[str, list[dict]],
    cs_index: dict[str, list[dict]],
) -> dict[str, list[TurnClassification]]:
    """Classify all turns across all runs. Returns {run_id: [TurnClassification]}."""
    all_classifications: dict[str, list[TurnClassification]] = {}
    skipped_runs = 0

    for run in runs:
        run_id = run.get("run_id", "")
        condition = run.get("condition", "")
        is_engine = "engine" in condition

        # Get turn decisions for this run
        turn_decs = td_index.get(run_id, [])
        if not turn_decs:
            skipped_runs += 1
            continue

        # Get relationship events for this run
        run_rel_events = rel_index.get(run_id, [])

        # Get action events (engine only)
        run_action_events = ae_index.get(run_id, []) if is_engine else []

        # Build per-actor feature counts from benchmark_runs.json
        actor_features: dict[str, dict] = {}
        metrics = run.get("metrics", {})
        breakdowns = metrics.get("actor_feature_breakdowns", {})
        for actor_id, bd in breakdowns.items():
            actor_features[actor_id] = bd.get("raw_features", {})

        # Get candidate scores (engine only, for linguistic backup)
        run_cs = cs_index.get(run_id, []) if is_engine else []
        # Index candidate scores by (actor_id, turn_index)
        cs_by_turn: dict[tuple[str, int], dict] = {}
        for cs in run_cs:
            ttid = cs.get("turn_trace_id", "")
            # Extract actor_id and turn_index from turn_trace_id
            cs_parts = ttid.split(":")
            if len(cs_parts) >= 2:
                cs_actor = cs_parts[-1]
                try:
                    cs_turn = int(cs_parts[-3]) if len(cs_parts) >= 3 else 0
                except (ValueError, IndexError):
                    continue
                fc = cs.get("feature_counts", {})
                if fc:
                    cs_by_turn[(cs_actor, cs_turn)] = fc

        # Determine all actor IDs in this run
        actor_ids = sorted(set(td.get("actor_id", "") for td in turn_decs if td.get("actor_id")))

        # Get relationship pairs that actually interact (bidirectional)
        interacting_pairs: set[tuple[str, str]] = set()
        for re in run_rel_events:
            src = re.get("source_actor_id", "")
            tgt = re.get("target_actor_id", "")
            if src and tgt:
                interacting_pairs.add((src, tgt))
                interacting_pairs.add((tgt, src))  # bidirectional

        # If no relationship events, create all possible pairs
        if not interacting_pairs:
            for a in actor_ids:
                for b in actor_ids:
                    if a != b:
                        interacting_pairs.add((a, b))

        classifications: list[TurnClassification] = []

        for td in turn_decs:
            actor_id = td.get("actor_id", "")
            turn_index = td.get("turn_index", 0)
            phase_name = td.get("phase_name", "")
            policy_plan = td.get("policy_plan") or {}

            # Per-turn feature counts: prefer candidate_scores, fallback to run-level
            turn_features = cs_by_turn.get((actor_id, turn_index), {})
            if not turn_features:
                turn_features = actor_features.get(actor_id, {})

            # Classify against each target actor this actor interacts with
            for target_id in actor_ids:
                if target_id == actor_id:
                    continue
                if (actor_id, target_id) not in interacting_pairs:
                    continue

                tc = classify_turn_pairwise(
                    run_id=run_id,
                    actor_id=actor_id,
                    target_id=target_id,
                    turn_index=turn_index,
                    phase_name=phase_name,
                    is_engine=is_engine,
                    policy_plan=policy_plan if is_engine else None,
                    action_events=run_action_events if is_engine else None,
                    rel_events=run_rel_events,
                    feature_counts=turn_features,
                )
                classifications.append(tc)

        all_classifications[run_id] = classifications

    if skipped_runs:
        print(f"  [game_theory] Skipped {skipped_runs} runs with no turn decisions", flush=True)

    return all_classifications


# ── Strategy matching ────────────────────────────────────────────────────────

STRATEGIES = [
    "always_cooperate",
    "always_defect",
    "tit_for_tat",
    "grudger",
    "pavlov",
    "generous_tft",
    "gradual",
]

RATIONAL_STRATEGIES = {"tit_for_tat", "pavlov", "generous_tft"}


def _predict_always_cooperate(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    return ["cooperate"] * len(actor_moves)


def _predict_always_defect(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    return ["defect"] * len(actor_moves)


def _predict_tit_for_tat(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    pred = ["cooperate"]
    for i in range(1, len(actor_moves)):
        pred.append(opponent_moves[i - 1])
    return pred


def _predict_grudger(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    pred: list[str] = []
    defected = False
    for i in range(len(actor_moves)):
        if defected:
            pred.append("defect")
        else:
            pred.append("cooperate")
        if i < len(opponent_moves) and opponent_moves[i] == "defect":
            defected = True
    return pred


def _predict_pavlov(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    pred = ["cooperate"]
    for i in range(1, len(actor_moves)):
        # If both made same move last round → cooperate, else switch
        if actor_moves[i - 1] == opponent_moves[i - 1]:
            pred.append("cooperate")
        else:
            pred.append("defect")
    return pred


def _predict_generous_tft(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    """TFT with forgiveness: if opponent defected but actor cooperated anyway,
    that counts as forgiveness (10-40% rate)."""
    pred = ["cooperate"]
    for i in range(1, len(actor_moves)):
        if opponent_moves[i - 1] == "defect":
            # generous_tft sometimes forgives — predict cooperate if actor
            # historically forgives defection
            pred.append("cooperate")  # we'll measure match rate
        else:
            pred.append("cooperate")
    return pred


def _predict_gradual(actor_moves: list[str], opponent_moves: list[str]) -> list[str]:
    """Retaliate proportionally, then reconcile."""
    pred: list[str] = []
    defect_count = 0
    retaliation_remaining = 0
    reconciliation_remaining = 0

    for i in range(len(actor_moves)):
        if reconciliation_remaining > 0:
            pred.append("cooperate")
            reconciliation_remaining -= 1
        elif retaliation_remaining > 0:
            pred.append("defect")
            retaliation_remaining -= 1
            if retaliation_remaining == 0:
                reconciliation_remaining = 2
        else:
            pred.append("cooperate")

        if i < len(opponent_moves) and opponent_moves[i] == "defect":
            defect_count += 1
            retaliation_remaining = defect_count
    return pred


_STRATEGY_PREDICTORS = {
    "always_cooperate": _predict_always_cooperate,
    "always_defect": _predict_always_defect,
    "tit_for_tat": _predict_tit_for_tat,
    "grudger": _predict_grudger,
    "pavlov": _predict_pavlov,
    "generous_tft": _predict_generous_tft,
    "gradual": _predict_gradual,
}


def match_strategy(
    actor_moves: list[str],
    opponent_moves: list[str],
) -> tuple[str, float, dict[str, float]]:
    """Match move sequence to closest iterated-game strategy.

    Returns (best_strategy, confidence, {strategy: score}).
    """
    if len(actor_moves) < 2:
        # Not enough data to distinguish strategies
        if actor_moves and actor_moves[0] == "cooperate":
            return ("always_cooperate", 0.5, {"always_cooperate": 0.5})
        elif actor_moves and actor_moves[0] == "defect":
            return ("always_defect", 0.5, {"always_defect": 0.5})
        return ("mixed", 0.0, {})

    scores: dict[str, float] = {}
    n = len(actor_moves)

    for strat_name, predictor in _STRATEGY_PREDICTORS.items():
        predicted = predictor(actor_moves, opponent_moves)
        # For generous_tft, use a looser match: count forgiveness separately
        if strat_name == "generous_tft":
            matches = 0
            forgiveness_events = 0
            for i in range(n):
                if actor_moves[i] == predicted[i]:
                    matches += 1
                elif (i > 0 and opponent_moves[i - 1] == "defect"
                      and actor_moves[i] == "cooperate"):
                    forgiveness_events += 1
                    # Count forgiveness as partial match
                    matches += 0.5
            forgiveness_rate = forgiveness_events / max(1, sum(1 for j in range(1, n) if opponent_moves[j-1] == "defect"))
            # generous_tft requires 10-40% forgiveness rate
            if 0.10 <= forgiveness_rate <= 0.40:
                scores[strat_name] = matches / n
            else:
                scores[strat_name] = (matches / n) * 0.7  # penalty for wrong forgiveness rate
        else:
            matches = sum(1 for i in range(n) if actor_moves[i] == predicted[i])
            # "conditional" moves count as 0.5 match for any prediction
            conditional_bonus = sum(
                0.5 for i in range(n)
                if actor_moves[i] == "conditional" and predicted[i] != actor_moves[i]
            )
            scores[strat_name] = (matches + conditional_bonus) / n

    best = max(scores, key=lambda k: scores[k])
    if scores[best] >= 0.50:
        return (best, round(scores[best], 3), {k: round(v, 3) for k, v in scores.items()})
    return ("mixed", round(scores.get(best, 0.0), 3), {k: round(v, 3) for k, v in scores.items()})


def _extract_actor_count(simulation_id: str) -> int:
    """Extract actor count from simulation_id like 'australia_robodebt_10actor'."""
    parts = simulation_id.rsplit("_", 1)
    if len(parts) == 2 and parts[1].endswith("actor"):
        try:
            return int(parts[1].replace("actor", ""))
        except ValueError:
            pass
    return 0


def _extract_base_scenario(simulation_id: str) -> str:
    """Extract base scenario from simulation_id like 'australia_robodebt_10actor' → 'australia_robodebt'."""
    parts = simulation_id.rsplit("_", 1)
    if len(parts) == 2 and parts[1].endswith("actor"):
        return parts[0]
    return simulation_id


def _is_policy_scenario(simulation_id: str) -> bool:
    """Heuristic: check if scenario is policy-related."""
    base = simulation_id.rsplit("_", 1)[0] if "_" in simulation_id else simulation_id
    # Check direct family match
    if base in _POLICY_FAMILIES:
        return True
    # Keyword heuristic
    policy_keywords = {"policy", "regulation", "crisis", "reform", "pricing", "gdpr", "ab5"}
    return any(kw in base.lower() for kw in policy_keywords)


def analyze_run_strategies(
    run_id: str,
    condition: str,
    simulation_id: str,
    classifications: list[TurnClassification],
) -> RunGameTheoryResult:
    """Analyze all actor-pair strategies for a single run."""
    # Group classifications by (actor_id, target_id)
    pair_cls: dict[tuple[str, str], list[TurnClassification]] = {}
    for tc in classifications:
        key = (tc.actor_id, tc.target_actor_id)
        pair_cls.setdefault(key, []).append(tc)

    pair_strategies: list[ActorPairStrategy] = []
    all_moves: list[str] = []

    for (actor_id, target_id), tcs in pair_cls.items():
        # Sort by turn_index
        tcs.sort(key=lambda x: x.turn_index)
        actor_moves = [tc.move for tc in tcs]
        all_moves.extend(actor_moves)

        # Get opponent's moves toward this actor
        opponent_key = (target_id, actor_id)
        opponent_tcs = pair_cls.get(opponent_key, [])
        opponent_tcs_sorted = sorted(opponent_tcs, key=lambda x: x.turn_index)
        opponent_moves = [tc.move for tc in opponent_tcs_sorted]

        # Align by sequential round (Nth move), not turn_index,
        # because actors speak in round-robin at different turn indices.
        n_rounds = min(len(actor_moves), len(opponent_moves)) if opponent_moves else 0
        if n_rounds > 0:
            aligned_actor = actor_moves[:n_rounds]
            aligned_opponent = opponent_moves[:n_rounds]
        else:
            aligned_actor = actor_moves
            aligned_opponent = ["cooperate"] * len(actor_moves)

        best_strat, confidence, all_scores = match_strategy(aligned_actor, aligned_opponent)

        pair_strategies.append(ActorPairStrategy(
            run_id=run_id,
            actor_id=actor_id,
            target_actor_id=target_id,
            condition=condition,
            move_sequence=actor_moves,
            best_match_strategy=best_strat,
            match_confidence=confidence,
            all_strategy_scores=all_scores,
        ))

    # Strategy distribution
    strat_dist: dict[str, int] = {}
    for ps in pair_strategies:
        strat_dist[ps.best_match_strategy] = strat_dist.get(ps.best_match_strategy, 0) + 1

    # Cooperation rate
    coop_count = sum(1 for m in all_moves if m == "cooperate")
    cond_count = sum(1 for m in all_moves if m == "conditional")
    total_moves = len(all_moves)
    cooperation_rate = coop_count / max(total_moves, 1)
    conditional_cooperation_rate = (coop_count + cond_count) / max(total_moves, 1)

    # Rationality & exploitability
    actor_count = _extract_actor_count(simulation_id)
    is_policy = _is_policy_scenario(simulation_id)
    rationality = compute_rationality_score(pair_strategies, is_policy)
    exploitability = compute_exploitability_for_run(pair_cls)

    return RunGameTheoryResult(
        run_id=run_id,
        condition=condition,
        simulation_id=simulation_id,
        actor_count=actor_count,
        pair_strategies=pair_strategies,
        dominant_strategy_distribution=strat_dist,
        cooperation_rate=round(cooperation_rate, 4),
        conditional_cooperation_rate=round(conditional_cooperation_rate, 4),
        rationality_score=round(rationality, 4),
        exploitability=round(exploitability, 4),
    )


# ── Nash equilibrium / Rationality ───────────────────────────────────────────


def compute_rationality_score(
    pair_strategies: list[ActorPairStrategy],
    is_policy: bool,
) -> float:
    """Compute how close actual payoffs are to cooperative equilibrium.

    rationality_score = 1.0 - |actual_payoff - R| / |R - P|
    where R = mutual cooperation payoff, P = mutual defection payoff.
    """
    payoff = PAYOFF_POLICY if is_policy else PAYOFF_NON_POLICY
    R, S, T, P = payoff["R"], payoff["S"], payoff["T"], payoff["P"]

    if not pair_strategies:
        return 0.0

    total_payoff = 0.0
    total_turns = 0

    for ps in pair_strategies:
        for move in ps.move_sequence:
            if move == "cooperate":
                # Approximate: assume opponent cooperates with the run's cooperation rate
                total_payoff += R * 0.7 + S * 0.3  # weighted estimate
            elif move == "defect":
                total_payoff += T * 0.3 + P * 0.7
            else:  # conditional
                total_payoff += R * 0.5 + P * 0.5
            total_turns += 1

    if total_turns == 0:
        return 0.0

    actual_avg = total_payoff / total_turns
    coop_eq = float(R)
    nash_one_shot = float(P)

    denom = abs(coop_eq - nash_one_shot)
    if denom < 0.001:
        return 1.0

    score = 1.0 - abs(actual_avg - coop_eq) / denom
    return max(0.0, min(1.0, score))


def compute_exploitability(
    actor_moves: list[str],
    opponent_moves: list[str],
) -> float:
    """Fraction of cooperative turns where opponent defected."""
    exploited = 0
    cooperative_turns = 0
    for i in range(min(len(actor_moves), len(opponent_moves))):
        if actor_moves[i] == "cooperate":
            cooperative_turns += 1
            if opponent_moves[i] == "defect":
                exploited += 1
    if cooperative_turns == 0:
        return 0.0
    return exploited / cooperative_turns


def compute_exploitability_for_run(
    pair_cls: dict[tuple[str, str], list[TurnClassification]],
) -> float:
    """Average exploitability across all actor pairs in a run.

    Actors speak in round-robin (different turn indices), so we align by
    sequential round number (Nth move), not absolute turn index.
    """
    exploitabilities: list[float] = []

    for (actor_id, target_id), tcs in pair_cls.items():
        opponent_key = (target_id, actor_id)
        opponent_tcs = pair_cls.get(opponent_key, [])
        if not opponent_tcs:
            continue

        # Align by sequential round (Nth move for each actor)
        a_sorted = sorted(tcs, key=lambda x: x.turn_index)
        o_sorted = sorted(opponent_tcs, key=lambda x: x.turn_index)
        n_rounds = min(len(a_sorted), len(o_sorted))
        if n_rounds == 0:
            continue

        a_moves = [tc.move for tc in a_sorted[:n_rounds]]
        o_moves = [tc.move for tc in o_sorted[:n_rounds]]
        exploitabilities.append(compute_exploitability(a_moves, o_moves))

    return mean(exploitabilities) if exploitabilities else 0.0


# ── Aggregation & statistics ─────────────────────────────────────────────────


def _summarize_runs(runs: list[RunGameTheoryResult]) -> dict:
    """Compute summary statistics for a group of runs."""
    if not runs:
        return {}

    def _strat_dist(runs: list[RunGameTheoryResult]) -> dict[str, float]:
        total = 0
        counts: dict[str, int] = {}
        for r in runs:
            for s, c in r.dominant_strategy_distribution.items():
                counts[s] = counts.get(s, 0) + c
                total += c
        if total == 0:
            return {}
        return {s: round(c / total, 4) for s, c in sorted(counts.items())}

    return {
        "num_runs": len(runs),
        "cooperation_rate_mean": round(mean([r.cooperation_rate for r in runs]), 4),
        "cooperation_rate_std": round(pstdev([r.cooperation_rate for r in runs]), 4) if len(runs) > 1 else 0.0,
        "conditional_cooperation_rate_mean": round(mean([r.conditional_cooperation_rate for r in runs]), 4),
        "rationality_score_mean": round(mean([r.rationality_score for r in runs]), 4),
        "rationality_score_std": round(pstdev([r.rationality_score for r in runs]), 4) if len(runs) > 1 else 0.0,
        "exploitability_mean": round(mean([r.exploitability for r in runs]), 4),
        "exploitability_std": round(pstdev([r.exploitability for r in runs]), 4) if len(runs) > 1 else 0.0,
        "strategy_distribution": _strat_dist(runs),
    }


def aggregate_results(
    per_run: list[RunGameTheoryResult],
) -> tuple[dict[str, dict], dict[str, dict], dict[str, dict[str, float]]]:
    """Aggregate results by condition and actor count.

    Returns (by_condition, by_actor_count, strategy_dist_by_condition).
    """
    # Group by condition
    by_cond: dict[str, list[RunGameTheoryResult]] = {}
    for r in per_run:
        by_cond.setdefault(r.condition, []).append(r)

    # Group by actor count
    by_ac: dict[str, list[RunGameTheoryResult]] = {}
    for r in per_run:
        ac_key = f"{r.actor_count}actor"
        by_ac.setdefault(ac_key, []).append(r)

    agg_cond = {c: _summarize_runs(rs) for c, rs in by_cond.items()}
    agg_ac = {ac: _summarize_runs(rs) for ac, rs in by_ac.items()}

    # Strategy distribution by condition
    strat_dist: dict[str, dict[str, float]] = {}
    for cond, summary in agg_cond.items():
        strat_dist[cond] = summary.get("strategy_distribution", {})

    return agg_cond, agg_ac, strat_dist


def aggregate_by_scenario(
    per_run: list[RunGameTheoryResult],
) -> dict[str, dict]:
    """Aggregate results by base scenario, with per-condition breakdown.

    Returns {scenario: {condition: summary, ...}}.
    """
    # Group by (base_scenario, condition)
    grouped: dict[str, dict[str, list[RunGameTheoryResult]]] = {}
    for r in per_run:
        base = _extract_base_scenario(r.simulation_id)
        grouped.setdefault(base, {}).setdefault(r.condition, []).append(r)

    result: dict[str, dict] = {}
    for scenario, cond_runs in sorted(grouped.items()):
        scenario_data: dict[str, Any] = {}
        for cond, runs in sorted(cond_runs.items()):
            scenario_data[cond] = _summarize_runs(runs)
        result[scenario] = scenario_data
    return result


def compute_scenario_statistical_tests(
    per_run: list[RunGameTheoryResult],
) -> dict[str, dict]:
    """Per-scenario Welch t-test + Cohen's d for engine vs naive.

    Returns {scenario: {metric: {t, p, d, engine_mean, naive_mean}}}.
    """
    # Identify engine and naive condition names
    conditions = set(r.condition for r in per_run)
    engine_cond = next((c for c in conditions if "engine" in c), None)
    naive_conds = [c for c in conditions if c not in (engine_cond,)]

    if not engine_cond or not naive_conds:
        return {}

    grouped: dict[str, dict[str, list[RunGameTheoryResult]]] = {}
    for r in per_run:
        base = _extract_base_scenario(r.simulation_id)
        grouped.setdefault(base, {}).setdefault(r.condition, []).append(r)

    metrics_keys = ["cooperation_rate", "rationality_score", "exploitability"]

    result: dict[str, dict] = {}
    for scenario, cond_runs in sorted(grouped.items()):
        engine_runs = cond_runs.get(engine_cond, [])
        # Merge all naive variants
        naive_runs: list[RunGameTheoryResult] = []
        for nc in naive_conds:
            naive_runs.extend(cond_runs.get(nc, []))

        if len(engine_runs) < 2 or len(naive_runs) < 2:
            continue

        scenario_stats: dict[str, dict] = {}
        for mk in metrics_keys:
            e_vals = [getattr(r, mk) for r in engine_runs]
            n_vals = [getattr(r, mk) for r in naive_runs]
            t_stat, p_val = _welch_t_test(e_vals, n_vals)
            d = _cohens_d(e_vals, n_vals)
            scenario_stats[mk] = {
                "engine_mean": round(mean(e_vals), 4),
                "naive_mean": round(mean(n_vals), 4),
                "delta": round(mean(e_vals) - mean(n_vals), 4),
                "t_statistic": t_stat,
                "p_value": p_val,
                "cohens_d": d,
                "engine_n": len(e_vals),
                "naive_n": len(n_vals),
            }
        result[scenario] = scenario_stats
    return result


def _welch_t_test(a: list[float], b: list[float]) -> tuple[float, float]:
    """Welch's t-test.  Returns (t_statistic, p_value).

    Uses scipy if available, otherwise a manual approximation.
    """
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        return (0.0, 1.0)

    m1, m2 = mean(a), mean(b)
    v1 = sum((x - m1) ** 2 for x in a) / (n1 - 1)
    v2 = sum((x - m2) ** 2 for x in b) / (n2 - 1)

    se = math.sqrt(v1 / n1 + v2 / n2)
    if se < 1e-12:
        return (0.0, 1.0)

    t_stat = (m1 - m2) / se

    # Welch-Satterthwaite degrees of freedom
    num = (v1 / n1 + v2 / n2) ** 2
    denom = ((v1 / n1) ** 2 / (n1 - 1)) + ((v2 / n2) ** 2 / (n2 - 1))
    df = num / denom if denom > 0 else 1.0

    # Approximate p-value using t-distribution CDF
    # Use scipy if available, otherwise a simple normal approximation for large df
    try:
        from scipy.stats import t as t_dist
        p_value = 2 * t_dist.sf(abs(t_stat), df)
    except ImportError:
        # Normal approximation (good for df > 30)
        import math as _math
        z = abs(t_stat)
        # Abramowitz & Stegun approximation
        p_value = 2 * (1.0 - 0.5 * (1.0 + _math.erf(z / _math.sqrt(2))))

    return (round(t_stat, 4), round(p_value, 6))


def _cohens_d(a: list[float], b: list[float]) -> float:
    """Cohen's d effect size (pooled SD)."""
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        return 0.0
    m1, m2 = mean(a), mean(b)
    v1 = sum((x - m1) ** 2 for x in a) / (n1 - 1)
    v2 = sum((x - m2) ** 2 for x in b) / (n2 - 1)
    pooled_sd = math.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    if pooled_sd < 1e-12:
        return 0.0
    return round((m1 - m2) / pooled_sd, 4)


def compute_statistical_tests(
    per_run: list[RunGameTheoryResult],
) -> dict[str, dict[str, float]]:
    """Welch t-test + Cohen's d for engine vs naive on key metrics."""
    engine_runs = [r for r in per_run if "engine" in r.condition]
    naive_runs = [r for r in per_run if r.condition == "naive"]

    if not engine_runs or not naive_runs:
        return {"error": {"message": "Need both engine and naive runs for comparison"}}

    metrics_to_test = {
        "cooperation_rate": (
            [r.cooperation_rate for r in engine_runs],
            [r.cooperation_rate for r in naive_runs],
        ),
        "conditional_cooperation_rate": (
            [r.conditional_cooperation_rate for r in engine_runs],
            [r.conditional_cooperation_rate for r in naive_runs],
        ),
        "rationality_score": (
            [r.rationality_score for r in engine_runs],
            [r.rationality_score for r in naive_runs],
        ),
        "exploitability": (
            [r.exploitability for r in engine_runs],
            [r.exploitability for r in naive_runs],
        ),
    }

    results: dict[str, dict[str, float]] = {}
    for metric_name, (engine_vals, naive_vals) in metrics_to_test.items():
        t_stat, p_val = _welch_t_test(engine_vals, naive_vals)
        d = _cohens_d(engine_vals, naive_vals)
        results[metric_name] = {
            "engine_mean": round(mean(engine_vals), 4),
            "naive_mean": round(mean(naive_vals), 4),
            "t_statistic": t_stat,
            "p_value": p_val,
            "cohens_d": d,
            "engine_n": len(engine_vals),
            "naive_n": len(naive_vals),
        }

    # Strategy distribution chi-square-like test
    engine_strats: dict[str, int] = {}
    naive_strats: dict[str, int] = {}
    for r in engine_runs:
        for s, c in r.dominant_strategy_distribution.items():
            engine_strats[s] = engine_strats.get(s, 0) + c
    for r in naive_runs:
        for s, c in r.dominant_strategy_distribution.items():
            naive_strats[s] = naive_strats.get(s, 0) + c

    # Rational strategy proportion test
    engine_total = sum(engine_strats.values())
    naive_total = sum(naive_strats.values())
    engine_rational = sum(engine_strats.get(s, 0) for s in RATIONAL_STRATEGIES)
    naive_rational = sum(naive_strats.get(s, 0) for s in RATIONAL_STRATEGIES)

    if engine_total > 0 and naive_total > 0:
        e_prop = engine_rational / engine_total
        n_prop = naive_rational / naive_total
        # Z-test for two proportions
        p_pool = (engine_rational + naive_rational) / (engine_total + naive_total)
        se_prop = math.sqrt(p_pool * (1 - p_pool) * (1 / engine_total + 1 / naive_total)) if 0 < p_pool < 1 else 1.0
        z_stat = (e_prop - n_prop) / se_prop if se_prop > 0 else 0.0
        try:
            from scipy.stats import norm
            p_prop = 2 * norm.sf(abs(z_stat))
        except ImportError:
            p_prop = 2 * (1.0 - 0.5 * (1.0 + math.erf(abs(z_stat) / math.sqrt(2))))

        results["rational_strategy_proportion"] = {
            "engine_proportion": round(e_prop, 4),
            "naive_proportion": round(n_prop, 4),
            "z_statistic": round(z_stat, 4),
            "p_value": round(p_prop, 6),
            "engine_rational_pairs": engine_rational,
            "naive_rational_pairs": naive_rational,
            "engine_total_pairs": engine_total,
            "naive_total_pairs": naive_total,
        }

    return results


# ── Report generation ────────────────────────────────────────────────────────


def _phase_dynamics(per_run: list[RunGameTheoryResult], all_classifications: dict[str, list[TurnClassification]]) -> str:
    """Build phase-level cooperation dynamics section."""
    phase_order = ["OPENING", "ESCALATION", "NEGOTIATION", "RESOLUTION", "CLOSING"]

    # Group by (condition, phase)
    by_cond_phase: dict[str, dict[str, list[str]]] = {}
    for run_id, tcs in all_classifications.items():
        # Extract condition from run_id (suite:track:sim:condition:rep)
        parts = run_id.split(":")
        condition = parts[3] if len(parts) >= 4 else "unknown"
        cond_data = by_cond_phase.setdefault(condition, {})
        for tc in tcs:
            phase = tc.phase_name
            cond_data.setdefault(phase, []).append(tc.move)

    lines = ["## 5. Phase-Level Dynamics\n"]

    all_conds = sorted(by_cond_phase.keys())
    cond_headers = " | ".join(f"{c} Coop%" for c in all_conds)
    defect_headers = " | ".join(f"{c} Defect%" for c in all_conds)
    lines.append(f"| Phase | {cond_headers} | {defect_headers} |")
    lines.append("|" + "|".join(["-------"] * (1 + 2 * len(all_conds))) + "|")

    all_phases = set()
    for cond_data in by_cond_phase.values():
        all_phases.update(cond_data.keys())
    ordered_phases = [p for p in phase_order if p in all_phases]
    ordered_phases += sorted(all_phases - set(phase_order))

    for phase in ordered_phases:
        row = f"| {phase} |"
        for c in all_conds:
            moves = by_cond_phase.get(c, {}).get(phase, [])
            coop = sum(1 for m in moves if m == "cooperate") / len(moves) * 100 if moves else 0.0
            row += f" {coop:.1f}% |"
        for c in all_conds:
            moves = by_cond_phase.get(c, {}).get(phase, [])
            defect = sum(1 for m in moves if m == "defect") / len(moves) * 100 if moves else 0.0
            row += f" {defect:.1f}% |"
        lines.append(row)

    return "\n".join(lines)


def build_game_theory_report(
    results: GameTheoryAnalysisResults,
    all_classifications: dict[str, list[TurnClassification]] | None = None,
) -> str:
    """Build markdown report."""
    lines: list[str] = []
    lines.append("# Game Theory Analysis Report\n")

    # Executive summary
    total = len(results.per_run)
    engine_n = sum(1 for r in results.per_run if "engine" in r.condition)
    naive_n = sum(1 for r in results.per_run if r.condition == "naive")
    lines.append("## Executive Summary\n")
    lines.append(f"- **{total} runs analyzed** (engine: {engine_n}, naive: {naive_n})")

    # Key finding from statistical tests
    stat = results.statistical_tests
    if "cooperation_rate" in stat:
        cr = stat["cooperation_rate"]
        lines.append(f"- Engine cooperation rate: {cr.get('engine_mean', 0):.3f} vs Naive: {cr.get('naive_mean', 0):.3f} "
                      f"(p={cr.get('p_value', 1):.4f}, d={cr.get('cohens_d', 0):.3f})")
    if "rational_strategy_proportion" in stat:
        rsp = stat["rational_strategy_proportion"]
        lines.append(f"- Rational strategy adoption: Engine {rsp.get('engine_proportion', 0):.1%} vs "
                      f"Naive {rsp.get('naive_proportion', 0):.1%} (p={rsp.get('p_value', 1):.4f})")
    lines.append("")

    # 1. Strategy Distribution
    lines.append("## 1. Strategy Distribution by Condition\n")
    all_strats = sorted(set().union(
        *(set(d.keys()) for d in results.strategy_distribution_by_condition.values())
    ))
    header = "| Strategy | " + " | ".join(
        f"{c} (%)" for c in sorted(results.strategy_distribution_by_condition.keys())
    ) + " |"
    sep = "|" + "|".join(["--------"] * (len(results.strategy_distribution_by_condition) + 1)) + "|"
    lines.append(header)
    lines.append(sep)
    for strat in all_strats:
        rational_marker = " *" if strat in RATIONAL_STRATEGIES else ""
        row = f"| {strat}{rational_marker} |"
        for cond in sorted(results.strategy_distribution_by_condition.keys()):
            val = results.strategy_distribution_by_condition[cond].get(strat, 0.0)
            row += f" {val:.1%} |"
        lines.append(row)
    lines.append("\n\\* = rational strategy (Axelrod-optimal)\n")

    # 2. Cooperation & Rationality Metrics
    lines.append("## 2. Cooperation & Rationality Metrics\n")
    lines.append("| Metric | Engine | Naive | Cohen's d | p-value |")
    lines.append("|--------|--------|-------|-----------|---------|")
    for metric_key in ["cooperation_rate", "conditional_cooperation_rate", "rationality_score", "exploitability"]:
        if metric_key in stat:
            s = stat[metric_key]
            lines.append(
                f"| {metric_key} | {s.get('engine_mean', 0):.4f} | {s.get('naive_mean', 0):.4f} | "
                f"{s.get('cohens_d', 0):.3f} | {s.get('p_value', 1):.4f} |"
            )
    lines.append("")

    # 3. By Actor Count
    lines.append("## 3. By Actor Count\n")
    lines.append("| Actor Count | Condition | N | Coop Rate | Rationality | Exploitability |")
    lines.append("|-------------|-----------|---|-----------|-------------|----------------|")

    # Cross-tabulate by (actor_count, condition)
    by_ac_cond: dict[tuple[int, str], list[RunGameTheoryResult]] = {}
    for r in results.per_run:
        key = (r.actor_count, r.condition)
        by_ac_cond.setdefault(key, []).append(r)

    for (ac, cond), runs in sorted(by_ac_cond.items()):
        cr = mean([r.cooperation_rate for r in runs])
        rat = mean([r.rationality_score for r in runs])
        exp = mean([r.exploitability for r in runs])
        lines.append(f"| {ac} | {cond} | {len(runs)} | {cr:.4f} | {rat:.4f} | {exp:.4f} |")
    lines.append("")

    # 4. Per-Scenario Breakdown
    if results.aggregate_by_scenario:
        lines.append("## 4. Per-Scenario Breakdown\n")

        # Identify conditions
        all_conds = sorted(set(r.condition for r in results.per_run))
        engine_cond = next((c for c in all_conds if "engine" in c), None)
        naive_conds = [c for c in all_conds if c != engine_cond]

        # Summary table
        lines.append("### 4a. Cooperation Rate by Scenario\n")
        cond_headers = " | ".join(f"{c}" for c in all_conds)
        lines.append(f"| Scenario | {cond_headers} | Delta | p-value |")
        lines.append("|" + "|".join(["----------"] * (len(all_conds) + 3)) + "|")

        for scenario, cond_data in sorted(results.aggregate_by_scenario.items()):
            row = f"| {scenario} |"
            for c in all_conds:
                s = cond_data.get(c, {})
                cr = s.get("cooperation_rate_mean", 0.0)
                row += f" {cr:.3f} |"
            # Delta and p-value from scenario tests
            sc_test = results.scenario_statistical_tests.get(scenario, {}).get("cooperation_rate", {})
            delta = sc_test.get("delta", 0.0)
            p = sc_test.get("p_value", 1.0)
            sig = "*" if p < 0.05 else ""
            row += f" {delta:+.3f} | {p:.3f}{sig} |"
            lines.append(row)
        lines.append("")

        # Strategy distribution per scenario
        lines.append("### 4b. Dominant Strategy by Scenario\n")
        lines.append(f"| Scenario | Condition | Top Strategy | % | 2nd Strategy | % |")
        lines.append("|----------|-----------|-------------|---|-------------|---|")

        for scenario, cond_data in sorted(results.aggregate_by_scenario.items()):
            for cond in all_conds:
                s = cond_data.get(cond, {})
                sd = s.get("strategy_distribution", {})
                if not sd:
                    continue
                ranked = sorted(sd.items(), key=lambda x: -x[1])
                top = ranked[0] if ranked else ("—", 0)
                second = ranked[1] if len(ranked) > 1 else ("—", 0)
                lines.append(
                    f"| {scenario} | {cond} | {top[0]} | {top[1]:.0%} | {second[0]} | {second[1]:.0%} |"
                )
        lines.append("")

        # Per-scenario detailed stats
        if results.scenario_statistical_tests:
            lines.append("### 4c. Per-Scenario Statistical Tests (Engine vs Naive)\n")
            lines.append("| Scenario | Metric | Engine | Naive | Delta | Cohen's d | p-value |")
            lines.append("|----------|--------|--------|-------|-------|-----------|---------|")
            for scenario, metrics in sorted(results.scenario_statistical_tests.items()):
                for mk in ["cooperation_rate", "rationality_score", "exploitability"]:
                    if mk not in metrics:
                        continue
                    m = metrics[mk]
                    sig = "*" if m["p_value"] < 0.05 else ""
                    lines.append(
                        f"| {scenario} | {mk} | {m['engine_mean']:.3f} | {m['naive_mean']:.3f} | "
                        f"{m['delta']:+.3f} | {m['cohens_d']:.2f} | {m['p_value']:.3f}{sig} |"
                    )
            lines.append("")

    # 5. Phase dynamics
    if all_classifications:
        lines.append(_phase_dynamics(results.per_run, all_classifications))
        lines.append("")

    # 6. Statistical Tests (aggregate)
    lines.append("## 6. Aggregate Statistical Tests\n")
    lines.append("### Welch t-test + Cohen's d (Engine vs Naive)\n")
    lines.append("| Metric | t-stat | p-value | Cohen's d | Significant? |")
    lines.append("|--------|--------|---------|-----------|-------------|")
    for metric_key, s in stat.items():
        if isinstance(s, dict) and "t_statistic" in s:
            sig = "Yes" if s.get("p_value", 1) < 0.05 else "No"
            lines.append(
                f"| {metric_key} | {s['t_statistic']:.3f} | {s['p_value']:.4f} | "
                f"{s.get('cohens_d', 0):.3f} | {sig} |"
            )
    lines.append("")

    if "rational_strategy_proportion" in stat:
        rsp = stat["rational_strategy_proportion"]
        lines.append("### Rational Strategy Proportion (Z-test)\n")
        lines.append(f"- Engine: {rsp.get('engine_rational_pairs', 0)}/{rsp.get('engine_total_pairs', 0)} "
                      f"= {rsp.get('engine_proportion', 0):.1%}")
        lines.append(f"- Naive: {rsp.get('naive_rational_pairs', 0)}/{rsp.get('naive_total_pairs', 0)} "
                      f"= {rsp.get('naive_proportion', 0):.1%}")
        sig = "Yes" if rsp.get("p_value", 1) < 0.05 else "No"
        lines.append(f"- z = {rsp.get('z_statistic', 0):.3f}, p = {rsp.get('p_value', 1):.4f} ({sig})")
        lines.append("")

    return "\n".join(lines)


def save_game_theory_report(results: GameTheoryAnalysisResults, path: Path,
                             all_classifications: dict[str, list[TurnClassification]] | None = None) -> None:
    """Write markdown report to disk."""
    report = build_game_theory_report(results, all_classifications)
    path.write_text(report)


def save_game_theory_json(results: GameTheoryAnalysisResults, path: Path) -> None:
    """Write JSON results to disk."""
    # Convert dataclasses to dicts, but keep pair_strategies compact
    output: dict[str, Any] = {
        "num_runs": len(results.per_run),
        "aggregate_by_condition": results.aggregate_by_condition,
        "aggregate_by_actor_count": results.aggregate_by_actor_count,
        "strategy_distribution_by_condition": results.strategy_distribution_by_condition,
        "statistical_tests": results.statistical_tests,
        "aggregate_by_scenario": results.aggregate_by_scenario,
        "scenario_statistical_tests": results.scenario_statistical_tests,
        "per_run_summary": [],
    }
    for r in results.per_run:
        output["per_run_summary"].append({
            "run_id": r.run_id,
            "condition": r.condition,
            "simulation_id": r.simulation_id,
            "base_scenario": _extract_base_scenario(r.simulation_id),
            "actor_count": r.actor_count,
            "cooperation_rate": r.cooperation_rate,
            "conditional_cooperation_rate": r.conditional_cooperation_rate,
            "rationality_score": r.rationality_score,
            "exploitability": r.exploitability,
            "dominant_strategy_distribution": r.dominant_strategy_distribution,
            "num_pairs": len(r.pair_strategies),
        })

    with open(path, "w") as f:
        json.dump(output, f, indent=2, default=str)


# ── Main entry point ─────────────────────────────────────────────────────────


def run_game_theory_analysis(
    results_dir: Path,
) -> tuple[GameTheoryAnalysisResults, dict[str, list[TurnClassification]]]:
    """Run the full game theory analysis on a benchmark results directory.

    Returns (results, all_classifications) — classifications are needed
    for phase-dynamics in the report.
    """
    results_dir = Path(results_dir)
    print(f"  [game_theory] Loading data from {results_dir}...", flush=True)

    # Load data
    runs = _load_run_data(results_dir)
    trace = _load_trace_data(results_dir)
    print(f"  [game_theory] Loaded {len(runs)} runs, "
          f"{len(trace['turn_decisions'])} turn decisions, "
          f"{len(trace['relationship_events'])} relationship events, "
          f"{len(trace['action_events'])} action events", flush=True)

    # Build indexes
    td_index = _build_turn_decision_index(trace["turn_decisions"])
    rel_index = _build_relationship_index(trace["relationship_events"])
    ae_index = _build_action_event_index(trace["action_events"])
    cs_index = _build_candidate_score_index(trace["candidate_scores"])

    # Classify all turns
    print("  [game_theory] Classifying turns...", flush=True)
    all_classifications = classify_all_turns(runs, td_index, rel_index, ae_index, cs_index)
    total_cls = sum(len(v) for v in all_classifications.values())
    print(f"  [game_theory] Classified {total_cls} turn-pair interactions across "
          f"{len(all_classifications)} runs", flush=True)

    # Analyze strategies per run
    print("  [game_theory] Matching strategies...", flush=True)
    per_run: list[RunGameTheoryResult] = []
    for run in runs:
        run_id = run.get("run_id", "")
        condition = run.get("condition", "")
        simulation_id = run.get("simulation_id", "")
        cls = all_classifications.get(run_id, [])
        if not cls:
            continue
        result = analyze_run_strategies(run_id, condition, simulation_id, cls)
        per_run.append(result)

    print(f"  [game_theory] Analyzed {len(per_run)} runs", flush=True)

    # Aggregate
    agg_cond, agg_ac, strat_dist = aggregate_results(per_run)

    # Scenario-level aggregation
    agg_scenario = aggregate_by_scenario(per_run)
    scenario_tests = compute_scenario_statistical_tests(per_run)

    # Statistical tests
    stat_tests = compute_statistical_tests(per_run)

    n_scenarios = len(agg_scenario)
    print(f"  [game_theory] {n_scenarios} scenarios analyzed", flush=True)

    results = GameTheoryAnalysisResults(
        per_run=per_run,
        aggregate_by_condition=agg_cond,
        aggregate_by_actor_count=agg_ac,
        strategy_distribution_by_condition=strat_dist,
        statistical_tests=stat_tests,
        aggregate_by_scenario=agg_scenario,
        scenario_statistical_tests=scenario_tests,
    )

    return results, all_classifications


# ── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Game Theory Post-Hoc Analysis on benchmark results",
    )
    parser.add_argument(
        "results_dir",
        type=str,
        help="Path to benchmark results directory (e.g. simulation_engine/results_thesis_final)",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    if not results_dir.exists():
        print(f"ERROR: {results_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    gt_results, all_cls = run_game_theory_analysis(results_dir)

    report_path = results_dir / "game_theory_report.md"
    json_path = results_dir / "game_theory_analysis.json"
    save_game_theory_report(gt_results, report_path, all_cls)
    save_game_theory_json(gt_results, json_path)

    print(f"\nSaved: {report_path}")
    print(f"Saved: {json_path}")

    # Print summary
    print("\n" + "=" * 60)
    print("GAME THEORY SUMMARY")
    print("=" * 60)
    for cond, agg in sorted(gt_results.aggregate_by_condition.items()):
        print(f"\n  {cond} (n={agg.get('num_runs', 0)}):")
        print(f"    cooperation_rate = {agg.get('cooperation_rate_mean', 0):.4f}")
        print(f"    rationality_score = {agg.get('rationality_score_mean', 0):.4f}")
        print(f"    exploitability = {agg.get('exploitability_mean', 0):.4f}")
    print("\n  Strategy Distribution:")
    for cond, dist in sorted(gt_results.strategy_distribution_by_condition.items()):
        print(f"    {cond}: {dist}")
    stat = gt_results.statistical_tests
    if "cooperation_rate" in stat:
        cr = stat["cooperation_rate"]
        print(f"\n  Cooperation rate p-value: {cr.get('p_value', 'N/A')}")
    if "rational_strategy_proportion" in stat:
        rsp = stat["rational_strategy_proportion"]
        print(f"  Rational strategy proportion p-value: {rsp.get('p_value', 'N/A')}")
