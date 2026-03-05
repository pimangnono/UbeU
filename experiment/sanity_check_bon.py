"""
Offline BoN sanity check: rescore existing candidate pools with current logic.

Usage:
  PYTHONPATH=. python3 experiment/sanity_check_bon.py --results-dir experiment/results_bcfc_freeze_pilot
"""

from __future__ import annotations

import argparse
import glob
import json
import statistics
from typing import List

from experiment.persona_compiler import compile_contract
from experiment.fidelity_controller import FidelityController
from experiment.profiles import EXPERIMENT_PROFILES
from utils.models import Turn, SpeakerRole


ROLE_MAP = {
    "Candidate": SpeakerRole.CANDIDATE,
    "Alex": SpeakerRole.ALEX,
    "Jordan": SpeakerRole.JORDAN,
    "Riley": SpeakerRole.RILEY,
}


def _build_turns(transcript: list[dict]) -> list[Turn]:
    turns = []
    for t in transcript:
        name = t.get("speaker")
        role = ROLE_MAP.get(name, SpeakerRole.FACILITATOR)
        turns.append(Turn(
            turn_number=t.get("turn"),
            speaker_role=role,
            speaker_name=name,
            content=t.get("content", ""),
        ))
    return turns


def _history_before_candidate_turn(turns: list[Turn], candidate_turn_idx: int, candidate_name: str = "Candidate") -> list[Turn]:
    count = 0
    history: list[Turn] = []
    for t in turns:
        if t.speaker_name == candidate_name:
            count += 1
            if count == candidate_turn_idx:
                break
        history.append(t)
    return history


def _mean(values: List[float]) -> float | None:
    if not values:
        return None
    return float(statistics.mean(values))


def rescore_pools(results_dir: str) -> dict:
    files = sorted(glob.glob(f"{results_dir}/session_*.json"))
    if not files:
        return {"error": "no sessions found"}

    contract_vals = {k: [] for k in ["full_score", "first", "random_expected", "contract_only", "relevance_only"]}
    adequacy_vals = {k: [] for k in contract_vals.keys()}
    all_contract_distances: list[float] = []
    pools_used = 0

    for f in files:
        data = json.load(open(f))
        pools = data.get("candidate_pool") or []
        if not pools:
            continue
        profile_id = data.get("profile_id")
        if profile_id not in EXPERIMENT_PROFILES:
            continue

        profile = EXPERIMENT_PROFILES[profile_id]
        vector = {"O": profile.O, "C": profile.C, "E": profile.E, "A": profile.A, "N": profile.N}
        contract = compile_contract(profile_id, vector)
        controller = FidelityController(contract, session_key=data.get("session_key", "sanity"))

        turns = _build_turns(data.get("transcript", []))

        for pool in pools:
            candidate_turn_idx = pool.get("turn_number")
            if not candidate_turn_idx:
                continue
            history = _history_before_candidate_turn(turns, candidate_turn_idx)
            candidates_raw = pool.get("candidates") or []

            candidates = []
            for c in candidates_raw:
                if isinstance(c, dict):
                    text = c.get("text")
                else:
                    text = c
                if text:
                    candidates.append(text)

            if not candidates:
                continue

            scored = controller.score_candidates(history, candidates, "Candidate")
            if not scored:
                continue

            pools_used += 1

            # Aggregate global contract distances
            for s in scored:
                all_contract_distances.append(s.get("contract_distance", 0.0))

            full_idx = max(range(len(scored)), key=lambda i: scored[i].get("score", 0))
            first_idx = 0
            contract_idx = min(range(len(scored)), key=lambda i: scored[i].get("contract_distance", 1.0))
            relevance_idx = min(range(len(scored)), key=lambda i: scored[i].get("relevance_penalty", 1.0))

            avg_contract = float(statistics.mean([s.get("contract_distance", 0.0) for s in scored]))
            avg_adequacy = float(statistics.mean([s.get("adequacy_penalty", 0.0) for s in scored]))

            def _push(label: str, idx: int):
                contract_vals[label].append(scored[idx].get("contract_distance", 0.0))
                adequacy_vals[label].append(scored[idx].get("adequacy_penalty", 0.0))

            _push("full_score", full_idx)
            _push("first", first_idx)
            _push("contract_only", contract_idx)
            _push("relevance_only", relevance_idx)
            contract_vals["random_expected"].append(avg_contract)
            adequacy_vals["random_expected"].append(avg_adequacy)

    if pools_used == 0:
        return {"error": "no candidate pools to rescore"}

    summary = {
        "pools_used": pools_used,
        "contract_distance": {k: round(_mean(v), 4) for k, v in contract_vals.items()},
        "adequacy_penalty": {k: round(_mean(v), 4) for k, v in adequacy_vals.items()},
        "contract_distance_distribution": {
            "mean": round(_mean(all_contract_distances), 4),
            "median": round(float(statistics.median(all_contract_distances)), 4),
            "p95": round(float(sorted(all_contract_distances)[int(0.95 * (len(all_contract_distances) - 1))]), 4),
        },
    }
    return summary


def main():
    parser = argparse.ArgumentParser(description="Offline BoN sanity check")
    parser.add_argument("--results-dir", type=str, required=True)
    args = parser.parse_args()

    result = rescore_pools(args.results_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
