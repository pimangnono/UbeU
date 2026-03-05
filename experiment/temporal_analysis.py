"""
Temporal Analysis: Phase-to-window mapping and per-window evaluation.

Splits sessions into Early/Peak/Late windows based on discussion phases,
then evaluates personality signals within each window to detect temporal decay.

Phase-to-window mapping (all 4 scenarios):
- Early (Window 1): INTRODUCTION, EXPLORATION, WELCOME, CONTEXT_SHARING, IDEATION, CRISIS_REVEAL
- Peak (Window 2): CONFLICT, DEFENSE, EVALUATION, INITIAL_REACTION, PROBLEM_SOLVING, STRESS_TEST, ROLE_NEGOTIATION
- Late (Window 3): RESOLUTION, CLOSING
"""

import json
import logging
from pathlib import Path
from typing import Optional, TYPE_CHECKING

from experiment.behavioral_features import extract_features
from utils.models import Turn, GroupSessionStats, SpeakerRole

if TYPE_CHECKING:
    from clients.llm_client import LLMClient

logger = logging.getLogger(__name__)


# Phase-to-window mapping
EARLY_PHASES = {
    "INTRODUCTION", "EXPLORATION", "WELCOME", "CONTEXT_SHARING",
    "IDEATION", "CRISIS_REVEAL",
}
PEAK_PHASES = {
    "CONFLICT", "DEFENSE", "EVALUATION", "INITIAL_REACTION",
    "PROBLEM_SOLVING", "STRESS_TEST", "ROLE_NEGOTIATION",
}
LATE_PHASES = {
    "RESOLUTION", "CLOSING",
}


def _get_phase_turn_ranges(scenario_phases) -> list[tuple[str, int, int]]:
    """
    Compute (phase_name, start_turn, end_turn) ranges from scenario phase configs.

    Each phase has a 'turns' count. We map cumulative turn ranges.
    """
    ranges = []
    cursor = 1  # Turns are 1-indexed
    for phase in scenario_phases:
        # Each phase contributes roughly 2x its turn count (candidate + AI)
        # But we use the raw turn count as the phase's share of the total
        phase_turns = phase.turns * 2  # Approximate: each "turn" = 1 candidate + 1 AI
        ranges.append((phase.name, cursor, cursor + phase_turns - 1))
        cursor += phase_turns
    return ranges


def split_into_windows(
    turns: list[Turn],
    scenario_phases,
) -> dict[str, list[Turn]]:
    """
    Split turns into early/peak/late windows based on scenario phases.

    Args:
        turns: Full session transcript.
        scenario_phases: List of GroupScenarioPhase from the scenario.

    Returns:
        Dict with keys "early", "peak", "late" mapping to lists of turns.
    """
    windows = {"early": [], "peak": [], "late": []}

    # Build phase ranges
    phase_ranges = _get_phase_turn_ranges(scenario_phases)

    for turn in turns:
        # Find which phase this turn belongs to
        phase_name = None
        for pname, start, end in phase_ranges:
            if start <= turn.turn_number <= end:
                phase_name = pname
                break

        if phase_name is None:
            # Turn exceeds all phase ranges -> late window
            phase_name = "CLOSING"

        # Map phase to window
        if phase_name in EARLY_PHASES:
            windows["early"].append(turn)
        elif phase_name in PEAK_PHASES:
            windows["peak"].append(turn)
        else:
            windows["late"].append(turn)

    return windows


def compute_window_stats(
    window_turns: list[Turn],
    candidate_name: str = "Candidate",
) -> GroupSessionStats:
    """
    Compute behavioral statistics for a single window's turns.

    Uses the shared behavioral_features module for consistent extraction.
    """
    features = extract_features(window_turns, candidate_name)
    candidate_turn_count = sum(1 for t in window_turns if t.speaker_name == candidate_name)
    candidate_word_count = sum(
        len(t.content.split()) for t in window_turns if t.speaker_name == candidate_name
    )

    return GroupSessionStats(
        total_turns=len(window_turns),
        candidate_turns=candidate_turn_count,
        candidate_word_count=candidate_word_count,
        candidate_avg_words_per_turn=features.avg_words_per_turn,
        times_addressed_others_by_name=features.name_mention_count,
        times_asked_questions=int(features.question_ratio * candidate_turn_count) if candidate_turn_count else 0,
        times_expressed_disagreement=features.disagreement_count,
        times_acknowledged_others=features.acknowledgment_count,
        times_proposed_new_ideas=features.idea_count,
    )


def _split_into_phases(
    turns: list[Turn],
    scenario_phases,
) -> list[dict]:
    """
    Split turns into individual phases and compute normalized position.

    Returns a list of dicts, each with:
    - phase_name, phase_index, phase_pos_norm (0..1), turns
    """
    phase_ranges = _get_phase_turn_ranges(scenario_phases)
    total_phases = len(phase_ranges)

    phases = []
    for idx, (pname, start, end) in enumerate(phase_ranges):
        phase_turns = [t for t in turns if start <= t.turn_number <= end]
        phases.append({
            "phase_name": pname,
            "phase_index": idx + 1,
            "phase_pos_norm": round((idx + 0.5) / total_phases, 4) if total_phases > 0 else 0.0,
            "turns": phase_turns,
        })

    # Assign overflow turns to the last phase
    if phase_ranges:
        last_end = phase_ranges[-1][2]
        overflow = [t for t in turns if t.turn_number > last_end]
        if overflow and phases:
            phases[-1]["turns"].extend(overflow)

    return phases


async def evaluate_per_window(
    eval_client: "LLMClient",
    turns: list[Turn],
    scenario_phases,
    candidate_name: str = "Candidate",
) -> dict:
    """
    Evaluate personality signals per temporal window (early/peak/late)
    and per individual phase.

    Args:
        eval_client: LLM client for evaluation.
        turns: Full session transcript (as Turn objects).
        scenario_phases: Scenario phase configuration.
        candidate_name: Name of the candidate.

    Returns:
        Dict with per-window and per-phase inferred vectors and stats.
    """
    from evaluation.trait_evaluator import evaluate_group_session

    windows = split_into_windows(turns, scenario_phases)
    result = {}

    for window_name, window_turns in windows.items():
        if not window_turns or not any(t.speaker_name == candidate_name for t in window_turns):
            result[window_name] = {
                "inferred_vector": None,
                "confidence": 0.0,
                "candidate_turns": 0,
                "stats": None,
            }
            continue

        stats = compute_window_stats(window_turns, candidate_name)

        try:
            assessment = await evaluate_group_session(
                client=eval_client,
                turns=window_turns,
                candidate_name=candidate_name,
                stats=stats,
                use_ensemble=True,
            )

            result[window_name] = {
                "inferred_vector": assessment.to_vector().to_dict(),
                "confidence": assessment.overall_confidence,
                "candidate_turns": stats.candidate_turns,
                "stats": {
                    "candidate_word_count": stats.candidate_word_count,
                    "candidate_avg_words_per_turn": stats.candidate_avg_words_per_turn,
                    "times_expressed_disagreement": stats.times_expressed_disagreement,
                    "times_acknowledged_others": stats.times_acknowledged_others,
                    "times_proposed_new_ideas": stats.times_proposed_new_ideas,
                },
            }
        except Exception as e:
            logger.error(f"Window {window_name} evaluation failed: {e}")
            result[window_name] = {
                "inferred_vector": None,
                "confidence": 0.0,
                "candidate_turns": stats.candidate_turns,
                "error": str(e),
            }

    # Per-phase evaluation (V5.1: Phase-controlled RQ3)
    phases_data = _split_into_phases(turns, scenario_phases)
    phase_results = []
    for phase_info in phases_data:
        phase_turns = phase_info["turns"]
        candidate_in_phase = [t for t in phase_turns if t.speaker_name == candidate_name]
        if len(candidate_in_phase) < 2:
            phase_results.append({
                "phase_name": phase_info["phase_name"],
                "phase_index": phase_info["phase_index"],
                "phase_pos_norm": phase_info["phase_pos_norm"],
                "inferred_vector": None,
                "candidate_turns": len(candidate_in_phase),
            })
            continue

        stats = compute_window_stats(phase_turns, candidate_name)
        try:
            assessment = await evaluate_group_session(
                client=eval_client,
                turns=phase_turns,
                candidate_name=candidate_name,
                stats=stats,
                use_ensemble=True,
            )
            phase_results.append({
                "phase_name": phase_info["phase_name"],
                "phase_index": phase_info["phase_index"],
                "phase_pos_norm": phase_info["phase_pos_norm"],
                "inferred_vector": assessment.to_vector().to_dict(),
                "candidate_turns": stats.candidate_turns,
            })
        except Exception as e:
            logger.error(f"Phase {phase_info['phase_name']} evaluation failed: {e}")
            phase_results.append({
                "phase_name": phase_info["phase_name"],
                "phase_index": phase_info["phase_index"],
                "phase_pos_norm": phase_info["phase_pos_norm"],
                "inferred_vector": None,
                "candidate_turns": len(candidate_in_phase),
                "error": str(e),
            })

    result["phases"] = phase_results
    return result


def _reconstruct_turns(transcript: list[dict]) -> list[Turn]:
    """Reconstruct Turn objects from saved transcript dicts."""
    from datetime import datetime

    turns = []
    for t in transcript:
        speaker = t["speaker"]
        # Map speaker name to role
        role_map = {
            "Candidate": SpeakerRole.CANDIDATE,
            "Alex": SpeakerRole.ALEX,
            "Jordan": SpeakerRole.JORDAN,
            "Riley": SpeakerRole.RILEY,
        }
        role = role_map.get(speaker, SpeakerRole.CANDIDATE)

        turns.append(Turn(
            turn_number=t["turn"],
            speaker_role=role,
            speaker_name=speaker,
            content=t["content"],
            timestamp=datetime.now(),
        ))
    return turns


async def run_temporal_analysis_batch(
    eval_client: "LLMClient",
    results_dir: str,
    output_path: str,
):
    """
    Run temporal analysis on all main condition sessions.

    Processes all 144 main sessions (skips baselines), evaluates personality
    per window, and saves results.
    """
    from config.group_scenarios import GROUP_SCENARIOS

    results_path = Path(results_dir)
    output = []
    session_files = sorted(results_path.glob("session_*.json"))

    print(f"\nTemporal Analysis: processing {len(session_files)} session files...")

    for i, filepath in enumerate(session_files):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to read {filepath}: {e}")
            continue

        # Only process main condition sessions
        if data.get("condition") != "main":
            continue

        scenario_id = data.get("scenario_id")
        if scenario_id not in GROUP_SCENARIOS:
            logger.warning(f"Unknown scenario {scenario_id} in {filepath}")
            continue

        scenario = GROUP_SCENARIOS[scenario_id]
        transcript = data.get("transcript", [])
        if not transcript:
            continue

        turns = _reconstruct_turns(transcript)

        print(f"  [{i+1}/{len(session_files)}] {data.get('session_key', '?')}...", end=" ")

        try:
            window_results = await evaluate_per_window(
                eval_client=eval_client,
                turns=turns,
                scenario_phases=scenario.phases,
                candidate_name="Candidate",
            )

            output.append({
                "session_key": data["session_key"],
                "profile_id": data.get("profile_id"),
                "scenario_id": scenario_id,
                "assigned_vector": data.get("assigned_vector"),
                "full_inferred_vector": data.get("inferred_vector"),
                "windows": window_results,
            })
            print("done")
        except Exception as e:
            logger.error(f"Temporal analysis failed for {data.get('session_key')}: {e}")
            print(f"FAILED: {e}")

    # Save results
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nTemporal analysis saved to {output_path}")
    print(f"Processed {len(output)} main sessions")
