"""Outcome analysis: compare simulation results against real-world ground truth.

Reads benchmark output + ground truth, produces comparison metrics,
diagnostic correlations, and actionable engine parameter recommendations.
"""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .ground_truth import (
    GROUND_TRUTH,
    ScenarioGroundTruth,
    StakeholderOutcome,
    get_ground_truth,
)

# ── Constants ────────────────────────────────────────────────────────────────

TRAIT_KEYS = ("O", "C", "E", "A", "N")

ACTION_FAMILIES = (
    "ownership", "evidence", "communication", "scope",
    "resourcing", "timing", "governance",
)

DIRECTION_NUMERIC = {
    "high": 1.0, "increase": 1.0,
    "low": -1.0, "decrease": -1.0,
    "unchanged": 0.0,
    "volatile": 0.0,
    "sharp_increase": 1.0, "sharp_decrease": -1.0,
}

METRIC_WEIGHTS = {
    "resolution_type_match": 0.20,
    "stakeholder_position_alignment": 0.25,
    "dynamics_surfacing": 0.20,
    "turning_point_coverage": 0.10,
    "world_state_direction_accuracy": 0.15,
    "action_distribution_alignment": 0.10,
}

EXPECTED_DIST_NUMERIC = {"high": 0.35, "medium": 0.20, "low": 0.08, "absent": 0.0}


# ── Data classes ─────────────────────────────────────────────────────────────

@dataclass
class ScenarioOutcomeMetrics:
    """Per-scenario outcome fidelity metrics."""

    scenario_id: str
    num_runs: int = 0
    resolution_type_match: float = 0.0
    stakeholder_position_alignment: float = 0.0
    dynamics_surfacing: float = 0.0
    turning_point_coverage: float = 0.0
    world_state_direction_accuracy: float = 0.0
    action_distribution_alignment: float = 0.0
    outcome_fidelity_score: float = 0.0
    condition: str = ""
    actor_count: int = 0
    simulation_mode: str = ""
    scenario_type: str = ""
    difficulty_index: float = 0.0
    adjusted_drift: float = 0.0


@dataclass
class DiagnosticResult:
    """A single diagnostic finding."""

    diagnostic_id: str
    title: str
    finding: str
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass
class ParameterRecommendation:
    """A concrete engine parameter change recommendation."""

    finding: str
    parameter: str
    file: str
    recommendation: str
    confidence: str  # high | medium | low
    rationale: str
    supporting_evidence: dict[str, Any] = field(default_factory=dict)


@dataclass
class OutcomeAnalysisResults:
    """Complete analysis output."""

    per_scenario: list[ScenarioOutcomeMetrics] = field(default_factory=list)
    aggregate_by_mode: dict[str, dict[str, float]] = field(default_factory=dict)
    aggregate_by_condition: dict[str, dict[str, float]] = field(default_factory=dict)
    aggregate_by_actor_count: dict[str, dict[str, float]] = field(default_factory=dict)
    diagnostics: list[DiagnosticResult] = field(default_factory=list)
    recommendations: list[ParameterRecommendation] = field(default_factory=list)


# ── Data loading ─────────────────────────────────────────────────────────────

def _load_json(path: Path) -> Any:
    with open(path) as f:
        return json.load(f)


def _load_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return rows


def load_benchmark_data(results_dir: Path) -> dict[str, Any]:
    """Load all benchmark output files into a unified dict."""
    data: dict[str, Any] = {}
    runs_path = results_dir / "benchmark_runs.json"
    if runs_path.exists():
        raw = _load_json(runs_path)
        data["runs"] = raw.get("runs", [])
        data["config"] = raw.get("config", {})
    else:
        data["runs"] = []
        data["config"] = {}

    outcomes_path = results_dir / "run_outcomes.json"
    data["run_outcomes"] = _load_json(outcomes_path) if outcomes_path.exists() else []

    trace_dir = results_dir / "trace_views"
    data["action_events"] = _load_jsonl(trace_dir / "action_events.jsonl")
    data["turn_decisions"] = _load_jsonl(trace_dir / "turn_decisions.jsonl")
    data["relationship_events"] = _load_jsonl(trace_dir / "relationship_events.jsonl")
    data["world_state_deltas"] = _load_jsonl(trace_dir / "world_state_deltas.jsonl")

    scripts_dir = results_dir / "generated_scripts"
    data["scripts"] = {}
    if scripts_dir.exists():
        for p in scripts_dir.glob("*.json"):
            data["scripts"][p.stem] = _load_json(p)

    return data


# ── Helper functions ─────────────────────────────────────────────────────────

def _extract_base_scenario(simulation_id: str) -> str:
    """Strip actor count suffix to get base scenario id."""
    for suffix in ("_3actor", "_5actor", "_10actor"):
        if simulation_id.endswith(suffix):
            return simulation_id[: -len(suffix)]
    return simulation_id


def _extract_actor_count(simulation_id: str) -> int:
    m = re.search(r"_(\d+)actor$", simulation_id)
    return int(m.group(1)) if m else 0


def _direction_to_numeric(direction: str) -> float:
    return DIRECTION_NUMERIC.get(direction, 0.0)


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na < 1e-9 or nb < 1e-9:
        return 0.0
    return dot / (na * nb)


def _pearson_r(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 3:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx < 1e-9 or sy < 1e-9:
        return 0.0
    return cov / (sx * sy)


def _parse_world_state_line(ws_line: str) -> dict[str, float]:
    """Parse 'world_state=key val, key val, ...' into a dict."""
    result: dict[str, float] = {}
    # Strip prefix
    text = ws_line
    if "=" in text:
        text = text.split("=", 1)[1]
    for pair in text.split(","):
        pair = pair.strip()
        parts = pair.rsplit(" ", 1)
        if len(parts) == 2:
            try:
                result[parts[0].strip()] = float(parts[1].strip())
            except ValueError:
                continue
    return result


def _safe_mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _group_runs_by_key(runs: list[dict], key_fn) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for run in runs:
        k = key_fn(run)
        if k:
            groups[k].append(run)
    return dict(groups)


def _welch_t_test_with_effect(
    values_a: list[float], values_b: list[float]
) -> tuple[float, float, float, float]:
    """Return (t_stat, df, p_value, cohens_d)."""
    na, nb = len(values_a), len(values_b)
    if na < 2 or nb < 2:
        return 0.0, 0.0, 1.0, 0.0
    ma = sum(values_a) / na
    mb = sum(values_b) / nb
    va = sum((x - ma) ** 2 for x in values_a) / (na - 1)
    vb = sum((x - mb) ** 2 for x in values_b) / (nb - 1)
    pooled_se_sq = va / na + vb / nb
    if pooled_se_sq < 1e-15:
        return 0.0, 0.0, 1.0, 0.0
    se = math.sqrt(pooled_se_sq)
    t_stat = (ma - mb) / se
    num = pooled_se_sq ** 2
    denom = (va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1)
    df = num / denom if denom > 1e-15 else 1.0
    # Normal approximation for p-value
    x = abs(t_stat)
    if df < 120:
        x = x * (1.0 - 1.0 / (4.0 * df))
    a1, a2, a3 = 0.4361836, -0.1201676, 0.9372980
    t_val = 1.0 / (1.0 + 0.33267 * x)
    phi = 1.0 - (1.0 / math.sqrt(2 * math.pi)) * math.exp(-x * x / 2) * (
        a1 * t_val + a2 * t_val ** 2 + a3 * t_val ** 3
    )
    p_value = min(1.0, 2.0 * (1.0 - phi))
    # Cohen's d
    pooled_sd = ((va * (na - 1) + vb * (nb - 1)) / (na + nb - 2)) ** 0.5
    d = (ma - mb) / pooled_sd if pooled_sd > 1e-12 else 0.0
    return t_stat, df, p_value, d


def _effect_size_label(d: float) -> str:
    """Interpret Cohen's d magnitude."""
    ad = abs(d)
    if ad < 0.2:
        return "negligible"
    if ad < 0.5:
        return "small"
    if ad < 0.8:
        return "medium"
    return "large"


# ── Part A: Outcome Comparison Metrics ───────────────────────────────────────

def _classify_simulation_resolution(run: dict) -> str:
    """Heuristic: classify a simulation run's resolution type from final state + relationships."""
    rs = run.get("runtime_summary", {})
    ws = rs.get("latest_world_state", {})
    alignment = ws.get("alignment", 0.5)
    trust = ws.get("trust", 0.5)
    uncertainty = ws.get("uncertainty", 0.5)
    execution_confidence = ws.get("execution_confidence", 0.5)

    # Use relationship polarity from action histograms as proxy
    action_hist = rs.get("phase_action_family_histogram", {})
    closing_actions = action_hist.get("CLOSING", {})
    negotiation_actions = action_hist.get("NEGOTIATION", {})

    # Heuristic classification
    if alignment >= 0.65 and trust >= 0.55:
        if execution_confidence >= 0.6:
            return "compromise"
        return "collaborative_resolution"
    if alignment <= 0.35 and trust <= 0.35:
        if uncertainty >= 0.6:
            return "collapse"
        return "stalemate"
    if alignment >= 0.6 and trust <= 0.4:
        return "one_side_won"
    if uncertainty >= 0.65:
        return "collapse"
    # Market force: collapse-like dynamics driven by financial/market factors
    if alignment <= 0.45 and uncertainty >= 0.5 and execution_confidence <= 0.45:
        return "market_force"
    governance_total = sum(
        negotiation_actions.get(f, 0) + closing_actions.get(f, 0)
        for f in ("governance", "ownership")
    )
    if governance_total >= 4:
        return "regulatory_override"
    evidence_total = sum(
        negotiation_actions.get(f, 0) + closing_actions.get(f, 0)
        for f in ("evidence",)
    )
    if evidence_total >= 3 and trust <= 0.4:
        return "whistleblower_exposure"
    return "compromise"


_RESOLUTION_COMPATIBILITY = {
    "compromise": {"compromise", "collaborative_resolution"},
    "one_side_won": {"one_side_won"},
    "collapse": {"collapse", "stalemate"},
    "stalemate": {"stalemate", "collapse"},
    "regulatory_override": {"regulatory_override", "one_side_won"},
    "market_force": {"collapse", "one_side_won", "market_force"},
    "whistleblower_exposure": {"whistleblower_exposure", "collapse"},
    "delayed_justice": {"delayed_justice", "compromise", "regulatory_override"},
    "institutional_failure": {"institutional_failure", "collapse", "stalemate"},
}


def _score_resolution_type_match(sim_resolution: str, gt: ScenarioGroundTruth) -> float:
    compatible = _RESOLUTION_COMPATIBILITY.get(gt.resolution_type, {gt.resolution_type})
    if sim_resolution == gt.resolution_type:
        return 1.0
    if sim_resolution in compatible:
        return 0.6
    return 0.0


def _match_archetype_to_actor(
    archetype: str,
    actor_labels: dict[str, str],
    actor_display_names: dict[str, str],
) -> str | None:
    """Fuzzy-match a ground truth archetype to a simulation actor via role string.

    Requires either: (a) >= 2 keyword matches, or (b) >= 50% keyword match ratio,
    or (c) 1 keyword match if archetype has only 1 keyword.
    """
    archetype_keywords = set(archetype.lower().replace("_", " ").split())
    num_keywords = len(archetype_keywords)
    best_score = 0
    best_actor = None
    for actor_id, label in actor_labels.items():
        label_lower = label.lower()
        # Also check display name
        display_name = actor_display_names.get(actor_id, "").lower()
        combined = label_lower + " " + display_name
        score = sum(1 for kw in archetype_keywords if kw in combined)
        if score > best_score:
            best_score = score
            best_actor = actor_id
    # Minimum threshold: 2 matches, or 50% of keywords, or 1 if only 1 keyword
    min_required = max(1, min(2, num_keywords))
    match_ratio = best_score / num_keywords if num_keywords > 0 else 0
    if best_score >= min_required or match_ratio >= 0.5:
        return best_actor
    return None


def _score_stakeholder_position(
    run: dict,
    gt: ScenarioGroundTruth,
    action_events_for_run: list[dict],
    relationship_events_for_run: list[dict],
) -> float:
    """Score how well simulation actors' positions match ground truth stakeholders."""
    rs = run.get("runtime_summary", {})
    actor_labels = rs.get("actor_labels", {})
    actor_display_names = rs.get("actor_display_names", {})
    ws = rs.get("latest_world_state", {})
    initial_ws = {}
    # Infer initial state from script if available
    script_data = run.get("_script_data", {})
    if script_data:
        initial_ws = script_data.get("initial_world_state", {})

    scores = []
    for so in gt.stakeholder_outcomes:
        actor_id = _match_archetype_to_actor(so.archetype, actor_labels, actor_display_names)
        if not actor_id:
            scores.append(0.3)  # partial credit for unmatched
            continue

        sub_scores = []

        # State direction match (direction 0.6 + magnitude bonus 0.4)
        if so.expected_state_direction and ws:
            dir_scores = []
            for key, expected_dir in so.expected_state_direction.items():
                if key in ws:
                    initial_val = initial_ws.get(key, 0.5)
                    actual_delta = ws[key] - initial_val
                    expected_sign = _direction_to_numeric(expected_dir)
                    if abs(expected_sign) < 0.01:
                        # "unchanged": tighter threshold (6% range)
                        dir_scores.append(1.0 if abs(actual_delta) < 0.06 else 0.0)
                    else:
                        if (actual_delta * expected_sign) > 0:
                            # Direction correct: 0.6 + magnitude bonus up to 0.4
                            magnitude_bonus = 0.4 * min(abs(actual_delta), 0.3) / 0.3
                            dir_scores.append(0.6 + magnitude_bonus)
                        else:
                            dir_scores.append(0.0)
            if dir_scores:
                sub_scores.append(_safe_mean(dir_scores))

        # Action family usage match
        actor_actions = [e for e in action_events_for_run if e.get("actor_id") == actor_id]
        if so.expected_action_families and actor_actions:
            used_families = set()
            for ae in actor_actions:
                cp = ae.get("compiled_proposal") or ae.get("executed_action") or {}
                at = cp.get("action_type", "")
                from .action_layer import ACTION_FAMILIES as AF_MAP
                used_families.add(AF_MAP.get(at, at))
            expected_set = set(so.expected_action_families)
            overlap = len(used_families & expected_set)
            union = len(used_families | expected_set)
            sub_scores.append(overlap / union if union > 0 else 0.0)

        # Relationship stance match
        if so.expected_relationships:
            rel_matches = 0
            rel_total = 0
            for other_archetype, expected_rel in so.expected_relationships.items():
                other_id = _match_archetype_to_actor(other_archetype, actor_labels, actor_display_names)
                if not other_id:
                    continue
                # Find final relationship from events
                final_sentiment = _find_final_relationship(
                    actor_id, other_id, relationship_events_for_run
                )
                if final_sentiment:
                    rel_matches += 1 if _sentiment_matches(final_sentiment, expected_rel) else 0
                    rel_total += 1
            if rel_total > 0:
                sub_scores.append(rel_matches / rel_total)

        scores.append(_safe_mean(sub_scores) if sub_scores else 0.3)

    return _safe_mean(scores)


def _find_final_relationship(source_id: str, target_id: str, events: list[dict]) -> str | None:
    """Find the last known sentiment between two actors."""
    final = None
    for e in events:
        if e.get("source_actor_id") == source_id and e.get("target_actor_id") == target_id:
            final = e.get("new_sentiment") or e.get("sentiment")
        elif e.get("source_actor_id") == target_id and e.get("target_actor_id") == source_id:
            final = e.get("new_sentiment") or e.get("sentiment")
    return final


def _sentiment_matches(actual: str, expected: str) -> bool:
    """Check if actual sentiment is compatible with expected."""
    if actual == expected:
        return True
    compatible = {
        "positive": {"positive"},
        "challenging": {"challenging", "negative"},
        "negative": {"negative", "challenging"},
        "neutral": {"neutral", "unchanged"},
    }
    return actual in compatible.get(expected, set())


def _score_dynamics_surfacing(run: dict, gt: ScenarioGroundTruth, relationship_events_for_run: list[dict]) -> float:
    """Score relationship polarity + tension + phase dynamics match."""
    sub_scores = []

    # Relationship polarity match
    sentiments = [e.get("new_sentiment", "neutral") for e in relationship_events_for_run]
    neg_count = sum(1 for s in sentiments if s in ("negative", "challenging"))
    pos_count = sum(1 for s in sentiments if s == "positive")
    total = len(sentiments) or 1

    sim_polarity = "mixed"
    if neg_count / total > 0.6:
        sim_polarity = "adversarial"
    elif pos_count / total > 0.6:
        sim_polarity = "collaborative"
    elif neg_count / total > 0.4 and pos_count / total > 0.3:
        sim_polarity = "fragmented"

    sub_scores.append(1.0 if sim_polarity == gt.expected_relationship_polarity else 0.3)

    # Tension level match
    tensions = [e.get("new_tension", 0.0) for e in relationship_events_for_run]
    mean_tension = _safe_mean(tensions)
    sim_tension = "low" if mean_tension < 0.1 else ("medium" if mean_tension < 0.25 else "high")
    sub_scores.append(1.0 if sim_tension == gt.expected_tension_level else 0.3)

    # Phase dynamics match
    if gt.phase_dynamics:
        rs = run.get("runtime_summary", {})
        phase_order = rs.get("phase_order", [])
        ws_history_count = rs.get("world_state_history_count", 0)
        action_hist = rs.get("phase_action_family_histogram", {})

        phase_matches = 0
        phase_total = 0
        for phase_name, expected_dynamic in gt.phase_dynamics.items():
            if phase_name not in action_hist:
                continue
            phase_total += 1
            # Simple heuristic: classify phase from action profile
            ph = action_hist.get(phase_name, {})
            total_actions = sum(ph.values())
            if total_actions == 0:
                phase_matches += 0.3 if expected_dynamic in ("stalemate", "collapse") else 0
                continue
            evidence_frac = ph.get("evidence", 0) / total_actions
            governance_frac = (ph.get("governance", 0) + ph.get("ownership", 0)) / total_actions
            scope_frac = ph.get("scope", 0) / total_actions
            comm_frac = ph.get("communication", 0) / total_actions

            if expected_dynamic == "escalation" and (evidence_frac > 0.2 or comm_frac > 0.3):
                phase_matches += 1
            elif expected_dynamic in ("compromise", "resolution") and governance_frac > 0.2:
                phase_matches += 1
            elif expected_dynamic in ("stalemate", "collapse") and scope_frac > 0.2:
                phase_matches += 0.7
            elif expected_dynamic == "one_side_dominates" and governance_frac > 0.3:
                phase_matches += 0.7
            else:
                phase_matches += 0.2

        if phase_total > 0:
            sub_scores.append(phase_matches / phase_total)

    return _safe_mean(sub_scores)


def _score_turning_point_coverage(
    gt: ScenarioGroundTruth,
    action_events_for_run: list[dict],
    world_state_deltas_for_run: list[dict],
    relationship_events_for_run: list[dict] | None = None,
) -> float:
    """Fraction of ground truth turning points with matching trace evidence.

    Uses three evidence channels (any match counts):
    1. Action type family match
    2. World state effect direction match (>= 1 key matching)
    3. Significant world state delta or relationship sentiment shift in timing window
    """
    if not gt.turning_points:
        return 0.5  # neutral score if no turning points defined

    covered = 0
    for tp in gt.turning_points:
        tp_score = 0.0

        # Channel 1: Action type match
        if tp.action_type_analog:
            from .action_layer import ACTION_FAMILIES as AF_MAP
            expected_family = AF_MAP.get(tp.action_type_analog, tp.action_type_analog)
            for ae in action_events_for_run:
                cp = ae.get("compiled_proposal") or ae.get("executed_action") or {}
                at = cp.get("action_type", "")
                if AF_MAP.get(at, at) == expected_family:
                    tp_score = max(tp_score, 1.0)
                    break

        # Channel 2: World state effect match (relaxed: >= 1 key matching)
        if tp.world_state_effect and world_state_deltas_for_run:
            for wsd in world_state_deltas_for_run:
                delta = wsd.get("delta", {})
                effect_matches = 0
                for key, expected_dir in tp.world_state_effect.items():
                    delta_val = delta.get(key, 0.0)
                    expected_sign = _direction_to_numeric(expected_dir)
                    if abs(expected_sign) < 0.01:
                        effect_matches += 1 if abs(delta_val) < 0.05 else 0
                    else:
                        effect_matches += 1 if (delta_val * expected_sign) > 0 else 0
                if effect_matches >= 1:
                    tp_score = max(tp_score, effect_matches / len(tp.world_state_effect))
                    if effect_matches >= len(tp.world_state_effect):
                        break

        # Channel 3: Significant world state change (large delta in any key)
        if tp_score < 0.5 and world_state_deltas_for_run:
            for wsd in world_state_deltas_for_run:
                delta = wsd.get("delta", {})
                if any(abs(v) >= 0.10 for v in delta.values()):
                    tp_score = max(tp_score, 0.5)
                    break

        # Channel 4: Relationship sentiment shift
        if tp_score < 0.5 and relationship_events_for_run:
            sentiments = [e.get("new_sentiment", "neutral") for e in relationship_events_for_run]
            if any(s in ("negative", "challenging") for s in sentiments):
                tp_score = max(tp_score, 0.3)

        covered += min(tp_score, 1.0)

    return covered / len(gt.turning_points)


def _score_world_state_direction(run: dict, gt: ScenarioGroundTruth) -> float:
    """Score world state direction match with magnitude bonus.

    Direction match: 0.6 base + 0.4 magnitude bonus (proportional to delta size).
    """
    if not gt.expected_final_state_direction:
        return 0.5

    rs = run.get("runtime_summary", {})
    ws = rs.get("latest_world_state", {})
    script_data = run.get("_script_data", {})
    initial_ws = script_data.get("initial_world_state", {}) if script_data else {}

    scores = []
    for key, expected_level in gt.expected_final_state_direction.items():
        if key not in ws:
            continue
        actual_val = ws[key]
        initial_val = initial_ws.get(key, 0.5)
        actual_delta = actual_val - initial_val

        if expected_level in ("high", "increase"):
            if actual_val > 0.55 or actual_delta > 0.05:
                magnitude_bonus = 0.4 * min(abs(actual_delta), 0.3) / 0.3
                scores.append(0.6 + magnitude_bonus)
            else:
                scores.append(0.0)
        elif expected_level in ("low", "decrease"):
            if actual_val < 0.45 or actual_delta < -0.05:
                magnitude_bonus = 0.4 * min(abs(actual_delta), 0.3) / 0.3
                scores.append(0.6 + magnitude_bonus)
            else:
                scores.append(0.0)
        elif expected_level in ("unchanged",):
            scores.append(1.0 if abs(actual_delta) < 0.06 else 0.0)
        elif expected_level in ("volatile",):
            scores.append(0.5)

    return _safe_mean(scores) if scores else 0.5


def _score_action_distribution(run: dict, gt: ScenarioGroundTruth) -> float:
    """Cosine similarity between sim action family frequency and expected distribution."""
    if not gt.expected_action_distribution:
        return 0.5

    rs = run.get("runtime_summary", {})
    action_hist = rs.get("phase_action_family_histogram", {})
    sim_totals: dict[str, int] = defaultdict(int)
    for phase_hist in action_hist.values():
        for family, count in phase_hist.items():
            sim_totals[family] += count

    total_actions = sum(sim_totals.values())
    if total_actions == 0:
        return 0.0

    sim_vec = []
    gt_vec = []
    for family in ACTION_FAMILIES:
        sim_vec.append(sim_totals.get(family, 0) / total_actions)
        gt_level = gt.expected_action_distribution.get(family, "low")
        gt_vec.append(EXPECTED_DIST_NUMERIC.get(gt_level, 0.1))

    return max(0.0, _cosine_similarity(sim_vec, gt_vec))


def compute_scenario_metrics(
    runs_for_scenario: list[dict],
    gt: ScenarioGroundTruth,
    action_events: list[dict],
    relationship_events: list[dict],
    world_state_deltas: list[dict],
    condition: str,
) -> ScenarioOutcomeMetrics:
    """Compute all 6 sub-scores + composite for one scenario x condition."""
    if not runs_for_scenario:
        return ScenarioOutcomeMetrics(scenario_id=gt.scenario_id, condition=condition)

    metric_lists: dict[str, list[float]] = {k: [] for k in METRIC_WEIGHTS}
    actor_count = _extract_actor_count(runs_for_scenario[0].get("simulation_id", ""))

    for run in runs_for_scenario:
        run_id = run.get("run_id", "")
        ae_for_run = [e for e in action_events if e.get("turn_trace_id", "").startswith(run_id)]
        re_for_run = [e for e in relationship_events if e.get("turn_trace_id", "").startswith(run_id)]
        wsd_for_run = [e for e in world_state_deltas if e.get("turn_trace_id", "").startswith(run_id)]

        sim_resolution = _classify_simulation_resolution(run)
        metric_lists["resolution_type_match"].append(
            _score_resolution_type_match(sim_resolution, gt)
        )
        metric_lists["stakeholder_position_alignment"].append(
            _score_stakeholder_position(run, gt, ae_for_run, re_for_run)
        )
        metric_lists["dynamics_surfacing"].append(
            _score_dynamics_surfacing(run, gt, re_for_run)
        )
        metric_lists["turning_point_coverage"].append(
            _score_turning_point_coverage(gt, ae_for_run, wsd_for_run, re_for_run)
        )
        metric_lists["world_state_direction_accuracy"].append(
            _score_world_state_direction(run, gt)
        )
        metric_lists["action_distribution_alignment"].append(
            _score_action_distribution(run, gt)
        )

    means = {k: _safe_mean(v) for k, v in metric_lists.items()}
    composite = sum(means[k] * w for k, w in METRIC_WEIGHTS.items())

    difficulty = scenario_difficulty_index(gt)
    # Compute mean raw drift across runs
    raw_drifts = [
        r.get("metrics", {}).get("persona_drift_mae", 0.0)
        for r in runs_for_scenario
    ]
    mean_drift = _safe_mean(raw_drifts)
    adjusted_drift = round(mean_drift / max(difficulty, 0.2), 4) if difficulty > 0 else mean_drift

    return ScenarioOutcomeMetrics(
        scenario_id=gt.scenario_id,
        num_runs=len(runs_for_scenario),
        resolution_type_match=round(means["resolution_type_match"], 4),
        stakeholder_position_alignment=round(means["stakeholder_position_alignment"], 4),
        dynamics_surfacing=round(means["dynamics_surfacing"], 4),
        turning_point_coverage=round(means["turning_point_coverage"], 4),
        world_state_direction_accuracy=round(means["world_state_direction_accuracy"], 4),
        action_distribution_alignment=round(means["action_distribution_alignment"], 4),
        outcome_fidelity_score=round(composite, 4),
        condition=condition,
        actor_count=actor_count,
        simulation_mode=gt.simulation_mode,
        scenario_type=gt.scenario_type,
        difficulty_index=difficulty,
        adjusted_drift=adjusted_drift,
    )


# ── Part B: Diagnostics ─────────────────────────────────────────────────────

def _diagnostic_trait_error_outcome_correlation(
    runs: list[dict],
    scenario_scores: dict[str, float],
) -> DiagnosticResult:
    """B1: Pearson r between per-trait error and outcome fidelity."""
    trait_errors_by_run: dict[str, dict[str, float]] = {}
    outcome_by_run: dict[str, float] = {}

    for run in runs:
        run_id = run.get("run_id", "")
        sim_id = run.get("simulation_id", "")
        metrics = run.get("metrics", {})
        per_trait = metrics.get("per_trait_error_mean", {})
        if per_trait and sim_id in scenario_scores:
            trait_errors_by_run[run_id] = per_trait
            outcome_by_run[run_id] = scenario_scores[sim_id]

    correlations = {}
    for trait in TRAIT_KEYS:
        xs = []
        ys = []
        for run_id in trait_errors_by_run:
            if run_id in outcome_by_run:
                xs.append(trait_errors_by_run[run_id].get(trait, 0.0))
                ys.append(outcome_by_run[run_id])
        correlations[trait] = round(_pearson_r(xs, ys), 4)

    # Overall drift
    xs_drift = []
    ys_drift = []
    for run in runs:
        run_id = run.get("run_id", "")
        sim_id = run.get("simulation_id", "")
        metrics = run.get("metrics", {})
        drift = metrics.get("persona_drift_mae", 0.0)
        if sim_id in scenario_scores:
            xs_drift.append(drift)
            ys_drift.append(scenario_scores[sim_id])
    drift_r = round(_pearson_r(xs_drift, ys_drift), 4)

    worst_trait = min(correlations, key=lambda t: correlations[t]) if correlations else "N/A"

    return DiagnosticResult(
        diagnostic_id="B1_trait_error_outcome_correlation",
        title="Trait Error → Outcome Correlation",
        finding=(
            f"Per-trait error correlations with outcome fidelity: "
            f"{', '.join(f'{t}={correlations.get(t, 0):.3f}' for t in TRAIT_KEYS)}. "
            f"Overall drift r={drift_r}. "
            f"Most negative trait: {worst_trait} (r={correlations.get(worst_trait, 0):.3f})."
        ),
        evidence={"per_trait_r": correlations, "drift_r": drift_r, "n": len(xs_drift)},
    )


def _diagnostic_action_type_bias(
    runs: list[dict],
    all_action_events: list[dict],
) -> DiagnosticResult:
    """B2: Overused/underused action families vs ground truth expectations."""
    sim_family_counts: dict[str, int] = defaultdict(int)
    gt_expected: dict[str, list[float]] = defaultdict(list)

    for run in runs:
        sim_id = run.get("simulation_id", "")
        base = _extract_base_scenario(sim_id)
        gt_entry = get_ground_truth(base)
        if not gt_entry:
            continue

        rs = run.get("runtime_summary", {})
        action_hist = rs.get("phase_action_family_histogram", {})
        for phase_hist in action_hist.values():
            for family, count in phase_hist.items():
                sim_family_counts[family] += count

        for family in ACTION_FAMILIES:
            gt_level = gt_entry.expected_action_distribution.get(family, "low")
            gt_expected[family].append(EXPECTED_DIST_NUMERIC.get(gt_level, 0.1))

    total_actions = sum(sim_family_counts.values()) or 1
    sim_freq = {f: sim_family_counts.get(f, 0) / total_actions for f in ACTION_FAMILIES}
    gt_mean = {f: _safe_mean(gt_expected.get(f, [0.1])) for f in ACTION_FAMILIES}

    biases = {}
    for f in ACTION_FAMILIES:
        biases[f] = round(sim_freq.get(f, 0) - gt_mean.get(f, 0), 4)

    overused = [f for f in ACTION_FAMILIES if biases.get(f, 0) > 0.05]
    underused = [f for f in ACTION_FAMILIES if biases.get(f, 0) < -0.05]

    return DiagnosticResult(
        diagnostic_id="B2_action_type_bias",
        title="Action Type Bias Analysis",
        finding=(
            f"Overused families: {', '.join(overused) or 'none'}. "
            f"Underused families: {', '.join(underused) or 'none'}. "
            f"Bias vector: {biases}."
        ),
        evidence={"sim_freq": sim_freq, "gt_mean": gt_mean, "bias": biases},
    )


def _diagnostic_phase_attribution(
    runs: list[dict],
) -> DiagnosticResult:
    """B3: Per-phase fraction of world state keys moving in correct direction."""
    phase_correct: dict[str, list[float]] = defaultdict(list)

    for run in runs:
        sim_id = run.get("simulation_id", "")
        base = _extract_base_scenario(sim_id)
        gt_entry = get_ground_truth(base)
        if not gt_entry or not gt_entry.expected_final_state_direction:
            continue

        rs = run.get("runtime_summary", {})
        psf = rs.get("phase_state_feedback", {})
        script_data = run.get("_script_data", {})
        initial_ws = script_data.get("initial_world_state", {}) if script_data else {}

        for phase_name, feedback in psf.items():
            if not isinstance(feedback, dict):
                continue
            # Extract world state from text format: "world_state=key val, key val, ..."
            # feedback is keyed by actor_id; take any actor's world_state_line
            state_at_phase: dict[str, float] = {}
            for _actor_id, actor_fb in feedback.items():
                if isinstance(actor_fb, dict) and "world_state_line" in actor_fb:
                    state_at_phase = _parse_world_state_line(actor_fb["world_state_line"])
                    break  # all actors see the same global world state
            if not state_at_phase:
                continue

            correct = 0
            total = 0
            for key, expected_level in gt_entry.expected_final_state_direction.items():
                if key in state_at_phase:
                    total += 1
                    init_val = initial_ws.get(key, 0.5)
                    delta = state_at_phase[key] - init_val
                    if expected_level in ("high", "increase") and delta > 0.02:
                        correct += 1
                    elif expected_level in ("low", "decrease") and delta < -0.02:
                        correct += 1
                    elif expected_level in ("unchanged",) and abs(delta) < 0.15:
                        correct += 1
                    elif expected_level in ("volatile",):
                        correct += 0.5

            if total > 0:
                phase_correct[phase_name].append(correct / total)

    phase_accuracy = {p: round(_safe_mean(v), 4) for p, v in phase_correct.items()}
    best_phase = max(phase_accuracy, key=phase_accuracy.get) if phase_accuracy else "N/A"
    worst_phase = min(phase_accuracy, key=phase_accuracy.get) if phase_accuracy else "N/A"

    return DiagnosticResult(
        diagnostic_id="B3_phase_attribution",
        title="Phase Attribution",
        finding=(
            f"Phase accuracy: {phase_accuracy}. "
            f"Best phase: {best_phase}. Worst phase: {worst_phase}."
        ),
        evidence={"phase_accuracy": phase_accuracy, "n_runs": len(runs)},
    )


def _diagnostic_convergence_outcome(
    runs: list[dict],
    scenario_scores: dict[str, float],
) -> DiagnosticResult:
    """B4: Bin runs by convergence, compute mean outcome fidelity per bin."""
    pairs = []
    for run in runs:
        sim_id = run.get("simulation_id", "")
        metrics = run.get("metrics", {})
        convergence = metrics.get("action_family_convergence_rate", 0.0)
        if sim_id in scenario_scores:
            pairs.append((convergence, scenario_scores[sim_id]))

    if not pairs:
        return DiagnosticResult(
            diagnostic_id="B4_convergence_outcome",
            title="Convergence → Outcome Correlation",
            finding="Insufficient data for convergence-outcome analysis.",
            evidence={},
        )

    pairs.sort(key=lambda x: x[0])
    n = len(pairs)
    q_size = max(1, n // 4)
    quartiles = {}
    for i, label in enumerate(["Q1_low", "Q2", "Q3", "Q4_high"]):
        start = i * q_size
        end = (i + 1) * q_size if i < 3 else n
        q_pairs = pairs[start:end]
        if q_pairs:
            quartiles[label] = {
                "convergence_range": [round(q_pairs[0][0], 4), round(q_pairs[-1][0], 4)],
                "mean_outcome_fidelity": round(_safe_mean([p[1] for p in q_pairs]), 4),
                "n": len(q_pairs),
            }

    r = _pearson_r([p[0] for p in pairs], [p[1] for p in pairs])

    return DiagnosticResult(
        diagnostic_id="B4_convergence_outcome",
        title="Convergence → Outcome Correlation",
        finding=(
            f"Convergence-outcome Pearson r={r:.3f} (n={len(pairs)}). "
            f"Q1 fidelity: {quartiles.get('Q1_low', {}).get('mean_outcome_fidelity', 'N/A')}, "
            f"Q4 fidelity: {quartiles.get('Q4_high', {}).get('mean_outcome_fidelity', 'N/A')}."
        ),
        evidence={"pearson_r": round(r, 4), "quartiles": quartiles},
    )


def _diagnostic_relationship_dynamics_gap(
    runs: list[dict],
    relationship_events: list[dict],
) -> DiagnosticResult:
    """B5: Compare final relationship polarity/tension vs ground truth."""
    gt_adversarial_scenarios: list[str] = []
    sim_final_polarities: dict[str, list[str]] = defaultdict(list)

    for run in runs:
        sim_id = run.get("simulation_id", "")
        base = _extract_base_scenario(sim_id)
        gt_entry = get_ground_truth(base)
        if not gt_entry:
            continue
        if gt_entry.expected_relationship_polarity == "adversarial":
            gt_adversarial_scenarios.append(sim_id)

        run_id = run.get("run_id", "")
        run_rel_events = [
            e for e in relationship_events
            if e.get("turn_trace_id", "").startswith(run_id)
        ]
        sentiments = [e.get("new_sentiment", "neutral") for e in run_rel_events]
        neg = sum(1 for s in sentiments if s in ("negative", "challenging"))
        total = len(sentiments) or 1
        if neg / total > 0.5:
            sim_final_polarities[sim_id].append("adversarial")
        else:
            sim_final_polarities[sim_id].append("non_adversarial")

    # De-escalation bias: among scenarios that should be adversarial, how often is sim non-adversarial?
    deescalation_count = 0
    adversarial_total = 0
    for sim_id in gt_adversarial_scenarios:
        for pol in sim_final_polarities.get(sim_id, []):
            adversarial_total += 1
            if pol == "non_adversarial":
                deescalation_count += 1

    deescalation_rate = deescalation_count / adversarial_total if adversarial_total > 0 else 0.0

    # Tension analysis
    tensions_in_adversarial = []
    tensions_in_non_adversarial = []
    for run in runs:
        sim_id = run.get("simulation_id", "")
        base = _extract_base_scenario(sim_id)
        gt_entry = get_ground_truth(base)
        if not gt_entry:
            continue
        run_id = run.get("run_id", "")
        run_tensions = [
            e.get("new_tension", 0.0) for e in relationship_events
            if e.get("turn_trace_id", "").startswith(run_id)
        ]
        if gt_entry.expected_tension_level == "high":
            tensions_in_adversarial.extend(run_tensions)
        else:
            tensions_in_non_adversarial.extend(run_tensions)

    return DiagnosticResult(
        diagnostic_id="B5_relationship_dynamics_gap",
        title="Relationship Dynamics Gap",
        finding=(
            f"De-escalation bias: {deescalation_rate:.1%} of adversarial scenarios simulated as non-adversarial "
            f"(n={adversarial_total}). "
            f"Mean tension in expected-high scenarios: {_safe_mean(tensions_in_adversarial):.3f}. "
            f"Mean tension in expected-low/medium scenarios: {_safe_mean(tensions_in_non_adversarial):.3f}."
        ),
        evidence={
            "deescalation_rate": round(deescalation_rate, 4),
            "n_adversarial_runs": adversarial_total,
            "mean_tension_expected_high": round(_safe_mean(tensions_in_adversarial), 4),
            "mean_tension_expected_other": round(_safe_mean(tensions_in_non_adversarial), 4),
        },
    )


def _diagnostic_archetype_difficulty(
    runs: list[dict],
) -> DiagnosticResult:
    """B6: Compute mean trait error + position alignment per archetype."""
    archetype_errors: dict[str, list[float]] = defaultdict(list)

    for run in runs:
        sim_id = run.get("simulation_id", "")
        base = _extract_base_scenario(sim_id)
        gt_entry = get_ground_truth(base)
        if not gt_entry:
            continue

        metrics = run.get("metrics", {})
        actor_trait_errors = metrics.get("actor_trait_errors", {})
        rs = run.get("runtime_summary", {})
        actor_labels = rs.get("actor_labels", {})
        actor_display_names = rs.get("actor_display_names", {})

        for so in gt_entry.stakeholder_outcomes:
            actor_id = _match_archetype_to_actor(so.archetype, actor_labels, actor_display_names)
            if actor_id and actor_id in actor_trait_errors:
                errors = actor_trait_errors[actor_id]
                if errors:
                    mae = _safe_mean([errors.get(t, 0.0) for t in TRAIT_KEYS])
                    archetype_errors[so.archetype].append(mae)

    archetype_summary = {}
    for arch, errors in archetype_errors.items():
        archetype_summary[arch] = {
            "mean_trait_error": round(_safe_mean(errors), 4),
            "n": len(errors),
        }

    ranked = sorted(archetype_summary.items(), key=lambda x: -x[1]["mean_trait_error"])
    hardest = [a for a, _ in ranked[:5]]

    return DiagnosticResult(
        diagnostic_id="B6_archetype_difficulty",
        title="Archetype Difficulty Ranking",
        finding=(
            "Hardest archetypes to simulate (highest trait error): "
            + ", ".join(
                f"{a} ({archetype_summary[a]['mean_trait_error']:.3f})" for a in hardest
            )
            + "."
        ),
        evidence={"archetype_summary": archetype_summary, "ranked": [a for a, _ in ranked]},
    )


# ── Part C: Recommendations ─────────────────────────────────────────────────

def scenario_difficulty_index(gt: ScenarioGroundTruth) -> float:
    """Compute a difficulty index for a scenario based on ground truth characteristics.

    Components:
    - Number of adversarial stakeholder outcomes (won/lost/harmed vs compromised/unchanged)
    - Expected tension level (high=1.0, medium=0.7, low=0.4)
    - Resolution type complexity (collapse/institutional_failure = harder)

    Returns a normalized difficulty score in [0.2, 1.0].
    """
    # Adversarial stakeholder fraction
    adversarial_categories = {"lost", "harmed", "won"}
    adversarial_count = sum(
        1 for so in gt.stakeholder_outcomes
        if so.outcome_category in adversarial_categories
    )
    total_stakeholders = max(len(gt.stakeholder_outcomes), 1)
    adversarial_fraction = adversarial_count / total_stakeholders

    # Tension level
    tension_scores = {"high": 1.0, "medium": 0.7, "low": 0.4}
    tension = tension_scores.get(gt.expected_tension_level, 0.5)

    # Resolution complexity
    hard_resolutions = {"collapse", "institutional_failure", "stalemate", "whistleblower_exposure"}
    resolution_complexity = 1.0 if gt.resolution_type in hard_resolutions else 0.5

    # Weighted combination
    raw = 0.35 * adversarial_fraction + 0.35 * tension + 0.30 * resolution_complexity
    # Normalize to [0.2, 1.0]
    return round(max(0.2, min(1.0, raw)), 4)


def _generate_recommendations(diagnostics: list[DiagnosticResult]) -> list[ParameterRecommendation]:
    """Map diagnostic findings to concrete engine parameter changes."""
    recs = []
    diag_map = {d.diagnostic_id: d for d in diagnostics}

    # B1: Trait errors
    b1 = diag_map.get("B1_trait_error_outcome_correlation")
    if b1:
        per_trait_r = b1.evidence.get("per_trait_r", {})
        for trait in ("A", "N"):
            r_val = per_trait_r.get(trait, 0.0)
            if r_val < -0.1:
                recs.append(ParameterRecommendation(
                    finding=f"{trait}-trait error negatively correlated with outcome fidelity (r={r_val:.3f})",
                    parameter=f"sigmoid calibration for {trait}-trait estimation",
                    file="metrics.py",
                    recommendation=(
                        f"Adjust {trait}-trait sigmoid center/slope in estimate_actor_traits_from_turns() "
                        f"to reduce systematic {trait}-error. Consider widening personality envelope for {trait}."
                    ),
                    confidence="medium" if abs(r_val) > 0.15 else "low",
                    rationale=f"RLHF-constrained trait {trait} shows correlation between error and poor outcomes",
                    supporting_evidence={"pearson_r": r_val},
                ))

    # B2: Action bias
    b2 = diag_map.get("B2_action_type_bias")
    if b2:
        bias = b2.evidence.get("bias", {})
        for family, bias_val in bias.items():
            if abs(bias_val) > 0.08:
                direction = "overused" if bias_val > 0 else "underused"
                recs.append(ParameterRecommendation(
                    finding=f"Action family '{family}' is {direction} (bias={bias_val:+.3f})",
                    parameter="duplicate_penalty, family_cap" if bias_val > 0 else "action vocabulary rotation",
                    file="controller.py / script phases",
                    recommendation=(
                        f"{'Increase duplicate_penalty for' if bias_val > 0 else 'Add explicit cues for'} "
                        f"'{family}' family in generated scripts."
                    ),
                    confidence="medium",
                    rationale=f"Systematic {direction} bias across scenarios",
                    supporting_evidence={"bias": bias_val},
                ))

    # B3: Phase attribution
    b3 = diag_map.get("B3_phase_attribution")
    if b3:
        phase_acc = b3.evidence.get("phase_accuracy", {})
        closing_acc = phase_acc.get("CLOSING", 1.0)
        if closing_acc < 0.4:
            recs.append(ParameterRecommendation(
                finding=f"CLOSING phase has low state direction accuracy ({closing_acc:.3f})",
                parameter="CLOSING.max_turns",
                file="generated scripts",
                recommendation=(
                    "Reduce CLOSING phase max_turns to limit convergence magnet effect. "
                    "Consider adding phase-specific diversity cues to CLOSING prompts."
                ),
                confidence="high",
                rationale="CLOSING phase convergence magnet is a known issue from Arm A experiments",
                supporting_evidence={"closing_accuracy": closing_acc},
            ))

    # B5: Relationship gap
    b5 = diag_map.get("B5_relationship_dynamics_gap")
    if b5:
        deesc_rate = b5.evidence.get("deescalation_rate", 0.0)
        if deesc_rate > 0.3:
            recs.append(ParameterRecommendation(
                finding=f"De-escalation bias: {deesc_rate:.1%} of adversarial scenarios are too cooperative",
                parameter="NEGATIVE/CHALLENGE keyword sets, tension_delta values",
                file="state_ledger.py",
                recommendation=(
                    "Expand _NEGATIVE_REL and _CHALLENGE_REL keyword tuples in state_ledger.py. "
                    "Increase tension_delta magnitude for detected conflict. "
                    "Consider adding sycophancy penalty increase for high-tension scenarios."
                ),
                confidence="high" if deesc_rate > 0.5 else "medium",
                rationale="Engine systematically de-escalates when reality was adversarial (RLHF sycophancy)",
                supporting_evidence={"deescalation_rate": deesc_rate},
            ))

    # B4: Convergence
    b4 = diag_map.get("B4_convergence_outcome")
    if b4:
        r_val = b4.evidence.get("pearson_r", 0.0)
        if r_val < -0.15:
            recs.append(ParameterRecommendation(
                finding=f"High convergence predicts poor outcome fidelity (r={r_val:.3f})",
                parameter="sycophancy_penalty weight, diversity floor",
                file="controller.py",
                recommendation=(
                    "Increase sycophancy penalty weight for high-tension scenarios. "
                    "Add minimum diversity floor for action family selection per phase."
                ),
                confidence="medium",
                rationale="Convergence-outcome negative correlation suggests sycophancy drives poor outcomes",
                supporting_evidence={"pearson_r": r_val},
            ))

    return recs


# ── Main analysis pipeline ───────────────────────────────────────────────────

def run_outcome_analysis(results_dir: Path) -> OutcomeAnalysisResults:
    """Execute the full outcome analysis pipeline."""
    print(f"Loading benchmark data from {results_dir}...")
    data = load_benchmark_data(results_dir)
    runs = data["runs"]
    scripts = data["scripts"]
    action_events = data["action_events"]
    relationship_events = data["relationship_events"]
    world_state_deltas = data["world_state_deltas"]

    # Attach script data to runs for initial world state access
    for run in runs:
        sim_id = run.get("simulation_id", "")
        run["_script_data"] = scripts.get(sim_id, {})

    print(f"Loaded {len(runs)} runs, {len(scripts)} scripts, "
          f"{len(action_events)} action events, {len(relationship_events)} relationship events.")

    # ── Part A: Compute per-scenario metrics ──
    print("Computing per-scenario outcome metrics...")
    per_scenario: list[ScenarioOutcomeMetrics] = []
    scenario_scores: dict[str, float] = {}

    # Group runs by (base_scenario, condition)
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for run in runs:
        sim_id = run.get("simulation_id", "")
        condition = run.get("condition", "")
        base = _extract_base_scenario(sim_id)
        grouped[(base, condition)].append(run)

    for (base, condition), group_runs in grouped.items():
        gt = get_ground_truth(base)
        if not gt:
            continue
        metrics = compute_scenario_metrics(
            group_runs, gt, action_events, relationship_events, world_state_deltas, condition
        )
        per_scenario.append(metrics)
        # Store per-simulation_id scores for diagnostics
        for run in group_runs:
            scenario_scores[run.get("simulation_id", "")] = metrics.outcome_fidelity_score

    print(f"Computed metrics for {len(per_scenario)} scenario-condition pairs.")

    # ── Aggregations ──
    agg_by_mode: dict[str, list[float]] = defaultdict(list)
    agg_by_condition: dict[str, list[float]] = defaultdict(list)
    agg_by_actor_count: dict[str, list[float]] = defaultdict(list)

    for m in per_scenario:
        agg_by_mode[f"{m.simulation_mode}:{m.condition}"].append(m.outcome_fidelity_score)
        agg_by_condition[m.condition].append(m.outcome_fidelity_score)
        if m.actor_count:
            agg_by_actor_count[f"{m.actor_count}:{m.condition}"].append(m.outcome_fidelity_score)

    aggregate_by_mode = {k: {"mean": round(_safe_mean(v), 4), "n": len(v)} for k, v in agg_by_mode.items()}
    aggregate_by_condition = {k: {"mean": round(_safe_mean(v), 4), "n": len(v)} for k, v in agg_by_condition.items()}
    aggregate_by_actor_count = {k: {"mean": round(_safe_mean(v), 4), "n": len(v)} for k, v in agg_by_actor_count.items()}

    # ── Part B: Diagnostics ──
    print("Running diagnostics...")
    diagnostics = [
        _diagnostic_trait_error_outcome_correlation(runs, scenario_scores),
        _diagnostic_action_type_bias(runs, action_events),
        _diagnostic_phase_attribution(runs),
        _diagnostic_convergence_outcome(runs, scenario_scores),
        _diagnostic_relationship_dynamics_gap(runs, relationship_events),
        _diagnostic_archetype_difficulty(runs),
    ]

    # ── Part C: Recommendations ──
    print("Generating recommendations...")
    recommendations = _generate_recommendations(diagnostics)

    return OutcomeAnalysisResults(
        per_scenario=per_scenario,
        aggregate_by_mode=aggregate_by_mode,
        aggregate_by_condition=aggregate_by_condition,
        aggregate_by_actor_count=aggregate_by_actor_count,
        diagnostics=diagnostics,
        recommendations=recommendations,
    )


# ── Output ───────────────────────────────────────────────────────────────────

def save_results_json(results: OutcomeAnalysisResults, output_path: Path) -> None:
    """Write machine-readable JSON output."""

    def _to_dict(obj: Any) -> Any:
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        return obj

    payload = {
        "per_scenario": [_to_dict(m) for m in results.per_scenario],
        "aggregate_by_mode": results.aggregate_by_mode,
        "aggregate_by_condition": results.aggregate_by_condition,
        "aggregate_by_actor_count": results.aggregate_by_actor_count,
        "diagnostics": [_to_dict(d) for d in results.diagnostics],
        "recommendations": [_to_dict(r) for r in results.recommendations],
    }
    with open(output_path, "w") as f:
        json.dump(payload, f, indent=2, default=str)
    print(f"Saved JSON results to {output_path}")


def build_outcome_report(results: OutcomeAnalysisResults) -> str:
    """Build the human-readable markdown report."""
    lines: list[str] = []

    # ── Executive Summary ──
    all_scores = [m.outcome_fidelity_score for m in results.per_scenario]
    mean_fidelity = _safe_mean(all_scores)
    n_scenarios = len(results.per_scenario)

    lines.extend([
        "# Outcome Analysis Report",
        "",
        "## Executive Summary",
        "",
        f"Analyzed **{n_scenarios}** scenario-condition pairs across **{sum(m.num_runs for m in results.per_scenario)}** simulation runs.",
        f"Mean outcome fidelity score: **{mean_fidelity:.3f}** (0 = no match, 1 = perfect match with reality).",
        "",
    ])

    # Condition comparison
    for cond, agg in sorted(results.aggregate_by_condition.items()):
        lines.append(f"- **{cond}**: mean fidelity = {agg['mean']:.3f} (n={agg['n']})")
    lines.append("")

    # ── Section 1: Per-Scenario Outcome vs Reality ──
    lines.extend(["## 1. Per-Scenario Outcome vs Reality", ""])

    categories = [
        ("1.1 Guided Policy", "guided", "policy"),
        ("1.2 Guided Non-Policy", "guided", "non_policy"),
        ("1.3 Exploratory Policy", "exploratory", "policy"),
        ("1.4 Exploratory Non-Policy", "exploratory", "non_policy"),
    ]
    for section_title, mode, stype in categories:
        lines.extend([f"### {section_title}", ""])
        matching = [
            m for m in results.per_scenario
            if m.simulation_mode == mode and m.scenario_type == stype
        ]
        if not matching:
            lines.append("No data available.")
            lines.append("")
            continue

        lines.append("| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |")
        lines.append("|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|")
        for m in sorted(matching, key=lambda x: (-x.outcome_fidelity_score, x.scenario_id)):
            lines.append(
                f"| {m.scenario_id} | {m.condition} | {m.num_runs} | "
                f"{m.resolution_type_match:.2f} | {m.stakeholder_position_alignment:.2f} | "
                f"{m.dynamics_surfacing:.2f} | {m.turning_point_coverage:.2f} | "
                f"{m.world_state_direction_accuracy:.2f} | {m.action_distribution_alignment:.2f} | "
                f"**{m.outcome_fidelity_score:.3f}** | {m.difficulty_index:.3f} | {m.adjusted_drift:.4f} |"
            )
        lines.append("")

    # ── Section 2: Guided vs Exploratory ──
    lines.extend(["## 2. Guided vs Exploratory: Does Outcome Anchoring Help?", ""])
    guided_scores = [m.outcome_fidelity_score for m in results.per_scenario if m.simulation_mode == "guided"]
    exploratory_scores = [m.outcome_fidelity_score for m in results.per_scenario if m.simulation_mode == "exploratory"]
    lines.append(f"- Guided mean fidelity: {_safe_mean(guided_scores):.3f} (n={len(guided_scores)})")
    lines.append(f"- Exploratory mean fidelity: {_safe_mean(exploratory_scores):.3f} (n={len(exploratory_scores)})")
    diff = _safe_mean(guided_scores) - _safe_mean(exploratory_scores)
    if abs(diff) > 0.02:
        better = "guided" if diff > 0 else "exploratory"
        lines.append(f"- **{better.capitalize()}** produces {abs(diff):.3f} higher outcome fidelity.")
    else:
        lines.append("- No meaningful difference between guided and exploratory modes.")
    lines.append("")

    # ── Section 3: Actor Count Effect ──
    lines.extend(["## 3. Actor Count Effect on Outcome Quality", ""])
    for key, agg in sorted(results.aggregate_by_actor_count.items()):
        lines.append(f"- {key}: mean fidelity = {agg['mean']:.3f} (n={agg['n']})")
    lines.append("")

    # ── Section 4: Engine vs Naive ──
    lines.extend(["## 4. Engine vs Naive: Does Better Fidelity = Better Outcomes?", ""])
    # Find engine and naive conditions dynamically
    engine_cond = None
    naive_cond = None
    for cond_name in results.aggregate_by_condition:
        if "engine" in cond_name:
            engine_cond = cond_name
        elif "naive" in cond_name and naive_cond is None:
            naive_cond = cond_name
    engine_data = results.aggregate_by_condition.get(engine_cond, {}) if engine_cond else {}
    naive_data = results.aggregate_by_condition.get(naive_cond, {}) if naive_cond else {}
    if engine_data and naive_data:
        delta = engine_data.get("mean", 0) - naive_data.get("mean", 0)
        lines.append(f"- Engine ({engine_cond}) mean fidelity: {engine_data.get('mean', 0):.3f} (n={engine_data.get('n', 0)})")
        lines.append(f"- Naive ({naive_cond}) mean fidelity: {naive_data.get('mean', 0):.3f} (n={naive_data.get('n', 0)})")
        lines.append(f"- Delta (engine - naive): {delta:+.3f}")
        if delta > 0.02:
            lines.append("- **Yes**: Better persona fidelity (engine) produces more realistic outcomes.")
        elif delta < -0.02:
            lines.append("- **No**: Naive condition produces more realistic outcomes despite worse persona fidelity.")
        else:
            lines.append("- **Inconclusive**: No meaningful difference in outcome fidelity between conditions.")

        # Statistical test: Welch's t-test + Cohen's d + 95% CI
        engine_scores = [
            m.outcome_fidelity_score for m in results.per_scenario if m.condition == engine_cond
        ]
        naive_scores = [
            m.outcome_fidelity_score for m in results.per_scenario if m.condition == naive_cond
        ]
        if len(engine_scores) >= 2 and len(naive_scores) >= 2:
            t_stat, df, p_value, d = _welch_t_test_with_effect(engine_scores, naive_scores)
            d_label = _effect_size_label(d)
            lines.append("")
            lines.append(f"- Welch's t-test: t={t_stat:.3f}, df={df:.1f}, p={p_value:.4f}")
            lines.append(f"- Cohen's d: {d:+.3f} ({d_label})")
            e_mean = sum(engine_scores) / len(engine_scores)
            n_mean = sum(naive_scores) / len(naive_scores)
            e_se = (sum((x - e_mean) ** 2 for x in engine_scores) / (len(engine_scores) - 1) / len(engine_scores)) ** 0.5
            n_se = (sum((x - n_mean) ** 2 for x in naive_scores) / (len(naive_scores) - 1) / len(naive_scores)) ** 0.5
            diff_se = (e_se ** 2 + n_se ** 2) ** 0.5
            lines.append(f"- 95% CI for delta: [{delta - 1.96 * diff_se:+.3f}, {delta + 1.96 * diff_se:+.3f}]")
    else:
        lines.append("- Insufficient data for engine vs naive comparison.")
    lines.append("")

    # ── Section 5: Diagnostics ──
    lines.extend(["## 5. Diagnostic Findings", ""])
    diag_sections = [
        ("5.1 Trait Errors Predicting Outcome Failures", "B1_trait_error_outcome_correlation"),
        ("5.2 Action Type Biases", "B2_action_type_bias"),
        ("5.3 Phase Attribution", "B3_phase_attribution"),
        ("5.4 Convergence-Outcome Relationship", "B4_convergence_outcome"),
        ("5.5 Relationship Dynamics Gap", "B5_relationship_dynamics_gap"),
        ("5.6 Archetype Difficulty Ranking", "B6_archetype_difficulty"),
    ]
    for section_title, diag_id in diag_sections:
        lines.append(f"### {section_title}")
        lines.append("")
        diag = next((d for d in results.diagnostics if d.diagnostic_id == diag_id), None)
        if diag:
            lines.append(diag.finding)
            lines.append("")
        else:
            lines.append("No data available.")
            lines.append("")

    # ── Section 6: Recommendations ──
    lines.extend(["## 6. Engine Parameter Recommendations", ""])
    if results.recommendations:
        lines.append("| # | Finding | Parameter | File | Confidence |")
        lines.append("|---|---------|-----------|------|-----------|")
        for i, rec in enumerate(results.recommendations, 1):
            lines.append(f"| {i} | {rec.finding[:80]} | `{rec.parameter}` | `{rec.file}` | {rec.confidence} |")
        lines.append("")
        for i, rec in enumerate(results.recommendations, 1):
            lines.extend([
                f"### Recommendation {i}: {rec.parameter}",
                "",
                f"**Finding**: {rec.finding}",
                "",
                f"**Recommendation**: {rec.recommendation}",
                "",
                f"**Rationale**: {rec.rationale}",
                "",
                f"**Confidence**: {rec.confidence}",
                "",
            ])
    else:
        lines.append("No parameter recommendations generated.")
        lines.append("")

    return "\n".join(lines)


def save_outcome_report(results: OutcomeAnalysisResults, output_path: Path) -> None:
    """Write the markdown report."""
    report = build_outcome_report(results)
    with open(output_path, "w") as f:
        f.write(report)
    print(f"Saved report to {output_path}")
