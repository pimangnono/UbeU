"""
Batch Runner: Orchestrates all 176 experiment sessions.

Session breakdown:
- 156 main sessions: 13 profiles x 4 scenarios x 3 reps
- 12 baseline_a sessions: 1 no-personality x 4 scenarios x 3 reps
- 8 baseline_b sessions: 2 profiles x 4 scenarios x 1 rep (shuffled OCEAN)

Features:
- Randomized session order (prevents systematic effects)
- Incremental JSON save after each session
- Resume: scans output_dir for completed session_keys, skips them
- Failures logged to failures.json
- Summary saved to experiment_summary.json
"""

import asyncio
import json
import logging
import os
import random
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional, TYPE_CHECKING

from config.group_scenarios import GROUP_SCENARIOS, create_scenario
from experiment.profiles import (
    EXPERIMENT_PROFILES,
    build_baseline_a_prompt,
    build_baseline_b_prompt,
)
from experiment.candidate_agent import ExperimentCandidateAgent
from experiment.behavioral_features import extract_features
from experiment.bcfc_config import DEFAULT_CONFIG
from experiment.trajectory_metrics import (
    compute_direct_question_answer_rate,
    compute_contradiction_rate,
    compute_unsolicited_structure_rate,
    compute_over_verbosity_rate,
    compute_stress_index,
)
from evaluation.trajectory_judge import evaluate_trajectory, evaluate_perceived_pressure
from experiment.validation.overlap_audit import run_full_audit
from engines.group_engine import GroupEngine
from evaluation.trait_evaluator import evaluate_group_session
from evaluation.rule_based_evaluator import evaluate_rule_based
from utils.models import SessionState

if TYPE_CHECKING:
    from clients.llm_client import LLMClient

logger = logging.getLogger(__name__)


@dataclass
class SessionSpec:
    """Specification for a single experiment session."""
    session_key: str       # Unique key for resume, e.g. "main_assertive_leader_resource_conflict_r1"
    condition: str         # "main" | "baseline_a" | "baseline_b" | "mini_v3" | "mini_v4" | "mini_v5" | "mini_v5_langgraph"
    profile_id: str        # Profile ID or "none" for baseline_a
    scenario_id: str       # Scenario ID
    rep: int               # Repetition number (1-based)
    assigned_vector: Optional[dict] = None  # For baseline_b: shuffled OCEAN vector
    intervention: str = "none"  # "none" | "bcfc" | "bcfc_v3" | "bcfc_v4" | "bcfc_v5" | "bcfc_v5_langgraph" | "bon_random"


# Profiles used for baseline_b (one extreme, one balanced)
BASELINE_B_PROFILES = ["assertive_leader", "neutral_observer"]


class BatchRunner:
    """
    Orchestrates all experiment sessions with resume capability.

    Usage:
        runner = BatchRunner(config, gen_client, eval_client)
        await runner.run_all()
    """

    def __init__(
        self,
        gen_client: "LLMClient",
        eval_client: "LLMClient",
        output_dir: str = "experiment/results",
        main_reps: int = 3,
        baseline_a_reps: int = 3,
        baseline_b_reps: int = 1,
        session_delay: float = 2.0,
        shuffle: bool = True,
    ):
        self.gen_client = gen_client
        self.eval_client = eval_client
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.main_reps = main_reps
        self.baseline_a_reps = baseline_a_reps
        self.baseline_b_reps = baseline_b_reps
        self.session_delay = session_delay
        self.shuffle = shuffle

        self.failures: list[dict] = []
        self.completed_count = 0
        self.start_time: Optional[float] = None
        self.uncertain_rows: list[dict] = []

        # Run overlap audit once at init (cached for all sessions)
        self._quality_audit = run_full_audit()

    def _build_session_list(self) -> list[SessionSpec]:
        """Build the full list of 176 sessions."""
        sessions = []
        scenario_ids = list(GROUP_SCENARIOS.keys())

        # Main sessions: 13 profiles x 4 scenarios x 3 reps = 156
        for profile_id in EXPERIMENT_PROFILES:
            for scenario_id in scenario_ids:
                for rep in range(1, self.main_reps + 1):
                    key = f"main_{profile_id}_{scenario_id}_r{rep}"
                    sessions.append(SessionSpec(
                        session_key=key,
                        condition="main",
                        profile_id=profile_id,
                        scenario_id=scenario_id,
                        rep=rep,
                    ))

        # Baseline A: no personality x 4 scenarios x 3 reps = 12
        for scenario_id in scenario_ids:
            for rep in range(1, self.baseline_a_reps + 1):
                key = f"baseline_a_none_{scenario_id}_r{rep}"
                sessions.append(SessionSpec(
                    session_key=key,
                    condition="baseline_a",
                    profile_id="none",
                    scenario_id=scenario_id,
                    rep=rep,
                ))

        # Baseline B: 2 profiles x 4 scenarios x 1 rep = 8
        for profile_id in BASELINE_B_PROFILES:
            for scenario_id in scenario_ids:
                for rep in range(1, self.baseline_b_reps + 1):
                    key = f"baseline_b_{profile_id}_{scenario_id}_r{rep}"
                    sessions.append(SessionSpec(
                        session_key=key,
                        condition="baseline_b",
                        profile_id=profile_id,
                        scenario_id=scenario_id,
                        rep=rep,
                    ))

        return sessions

    def _get_completed_keys(self) -> set[str]:
        """Scan output_dir for completed session keys."""
        completed = set()
        for path in self.output_dir.glob("session_*.json"):
            try:
                with open(path) as f:
                    data = json.load(f)
                if "session_key" in data:
                    completed.add(data["session_key"])
            except (json.JSONDecodeError, KeyError):
                continue
        return completed

    async def run_all(self) -> dict:
        """
        Run all experiment sessions, skipping completed ones.

        Returns:
            Summary dict with counts and timing.
        """
        self.start_time = time.time()
        all_sessions = self._build_session_list()
        completed_keys = self._get_completed_keys()

        remaining = [s for s in all_sessions if s.session_key not in completed_keys]
        self.completed_count = len(completed_keys)

        total = len(all_sessions)
        skipped = len(completed_keys)

        logger.info(f"Experiment: {total} total sessions, {skipped} already completed, {len(remaining)} remaining")
        print(f"\n{'='*60}")
        print(f"BEHAVIORAL FIDELITY EXPERIMENT")
        print(f"Total sessions: {total}")
        print(f"Already completed: {skipped}")
        print(f"Remaining: {len(remaining)}")
        print(f"{'='*60}\n")

        # Randomize order to prevent systematic effects
        if self.shuffle:
            random.shuffle(remaining)

        for i, spec in enumerate(remaining):
            session_num = skipped + i + 1
            print(f"\n[{session_num}/{total}] {spec.session_key}")
            print(f"  Condition: {spec.condition} | Profile: {spec.profile_id} | Scenario: {spec.scenario_id}")

            try:
                result = await self._run_single_session(spec)
                self._save_session_result(result, session_num)
                self.completed_count += 1
                print(f"  -> Completed ({result.get('stats', {}).get('candidate_turns', '?')} candidate turns)")
            except Exception as e:
                import traceback
                logger.error(f"Session {spec.session_key} failed: {e}\n{traceback.format_exc()}")
                print(f"  -> FAILED: {e}")
                self.failures.append({
                    "session_key": spec.session_key,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat(),
                })

            # Delay between sessions
            if i < len(remaining) - 1:
                await asyncio.sleep(self.session_delay)

        # Save summary and failures
        summary = self._build_summary(total)
        self._save_summary(summary)
        if self.failures:
            self._save_failures()

        # Save uncertain queue CSV (Phase 4)
        if self.uncertain_rows:
            self._save_uncertain_queue()

        print(f"\n{'='*60}")
        print(f"EXPERIMENT COMPLETE")
        print(f"Completed: {self.completed_count}/{total}")
        print(f"Failures: {len(self.failures)}")
        print(f"Uncertain trait evaluations: {len(self.uncertain_rows)}")
        print(f"Duration: {time.time() - self.start_time:.0f}s")
        print(f"{'='*60}\n")

        return summary

    async def _run_single_session(self, spec: SessionSpec) -> dict:
        """Run a single experiment session and return the result dict."""
        session_start = time.time()
        # Reset per-session usage counters
        if hasattr(self.gen_client, "reset_usage"):
            self.gen_client.reset_usage()
        if hasattr(self.eval_client, "reset_usage"):
            self.eval_client.reset_usage()

        scenario = create_scenario(spec.scenario_id)

        # Build candidate system prompt based on condition
        system_prompt = None
        assigned_vector = None

        if spec.condition in ("main", "mini_v3", "mini_v4", "mini_v5", "mini_v5_langgraph"):
            profile = EXPERIMENT_PROFILES[spec.profile_id]
            system_prompt = profile.build_system_prompt(scenario.brief)
            assigned_vector = profile.get_vector()

        elif spec.condition == "baseline_a":
            system_prompt = build_baseline_a_prompt(scenario.brief)
            assigned_vector = None

        elif spec.condition == "baseline_b":
            profile = EXPERIMENT_PROFILES[spec.profile_id]
            system_prompt, shuffled_vec = build_baseline_b_prompt(scenario.brief, profile)
            assigned_vector = shuffled_vec
            spec.assigned_vector = shuffled_vec

        # Create engine and candidate
        engine = GroupEngine(
            client=self.gen_client,
            participant_id=f"exp_{spec.session_key}",
            participant_name="Candidate",
            scenario=scenario,
        )

        candidate = ExperimentCandidateAgent(
            client=self.gen_client,
            system_prompt=system_prompt,
            candidate_name="Candidate",
        )

        # Run the session loop (BCFC / BoN-random / standard)
        controller = None
        candidate_pool_logs: list[dict] = []
        if spec.intervention == "bcfc" and assigned_vector:
            from experiment.persona_compiler import compile_contract
            from experiment.fidelity_controller import FidelityController

            contract = compile_contract(spec.profile_id, assigned_vector)
            controller = FidelityController(contract, spec.session_key)
            candidate_pool_logs = await self._run_bcfc_session_loop(
                engine, candidate, scenario, controller
            )
        elif spec.intervention == "bcfc_v3" and assigned_vector:
            from experiment.persona_compiler import compile_contract
            from experiment.fidelity_controller import FidelityController

            contract = compile_contract(spec.profile_id, assigned_vector)
            controller = FidelityController(contract, spec.session_key)
            candidate_pool_logs = await self._run_bcfc_v3_session_loop(
                engine, candidate, scenario, controller
            )
        elif spec.intervention == "bcfc_v4" and assigned_vector:
            from experiment.persona_compiler import compile_contract
            from experiment.fidelity_controller import FidelityController

            contract = compile_contract(spec.profile_id, assigned_vector)
            controller = FidelityController(contract, spec.session_key)
            candidate_pool_logs = await self._run_bcfc_v4_session_loop(
                engine, candidate, scenario, controller
            )
        elif spec.intervention == "bcfc_v5" and assigned_vector:
            from experiment.persona_compiler import compile_contract
            from experiment.fidelity_controller import FidelityController

            contract = compile_contract(spec.profile_id, assigned_vector)
            controller = FidelityController(contract, spec.session_key)
            candidate_pool_logs = await self._run_bcfc_v5_session_loop(
                engine, candidate, scenario, controller
            )
        elif spec.intervention == "bon_random":
            candidate_pool_logs = await self._run_bon_random_session_loop(
                engine, candidate, scenario
            )
        else:
            candidate_pool_logs = await self._run_session_loop(engine, candidate, scenario)

        # Compute stats and features
        stats = engine.compute_session_stats()
        features = extract_features(engine.turns, candidate_name="Candidate")

        # Run rule-based evaluation (deterministic, no LLM)
        rule_based_vector = evaluate_rule_based(features)

        # Run ensemble evaluation
        assessment = await evaluate_group_session(
            client=self.eval_client,
            turns=engine.turns,
            candidate_name="Candidate",
            stats=stats,
            use_ensemble=True,
            escalate=True,
        )

        # Trajectory metrics (appropriateness/coherence)
        trajectory_scores = await evaluate_trajectory(
            client=self.eval_client,
            turns=engine.turns,
            candidate_name="Candidate",
            context_turns=DEFAULT_CONFIG.trajectory_context_turns,
        )

        # Pressure manipulation checks
        perceived_pressure = await evaluate_perceived_pressure(
            client=self.eval_client,
            turns=engine.turns,
            scenario_brief=scenario.brief,
        )
        stress_index = compute_stress_index(engine.turns)

        # Deterministic trajectory diagnostics
        trajectory_diagnostics = {
            "direct_question_answer_rate": compute_direct_question_answer_rate(engine.turns),
            "contradiction_rate": compute_contradiction_rate(engine.turns),
            "unsolicited_structure_rate": compute_unsolicited_structure_rate(engine.turns),
            "over_verbosity_rate": compute_over_verbosity_rate(engine.turns),
        }

        # Build result
        inferred_vector = assessment.to_vector().to_dict()

        # Collect uncertain traits for escalation queue (Phase 4)
        judge_diag = assessment.judge_diagnostics
        if judge_diag.get("uncertain_traits"):
            for trait_abbrev in judge_diag["uncertain_traits"]:
                reasons = judge_diag.get("uncertain_reasons", {}).get(trait_abbrev, [])
                self.uncertain_rows.append({
                    "session_key": spec.session_key,
                    "trait": trait_abbrev,
                    "reason": ",".join(reasons),
                    "assigned": assigned_vector.get(trait_abbrev) if assigned_vector else None,
                    "inferred": inferred_vector.get(trait_abbrev),
                    "scenario_id": spec.scenario_id,
                    "profile_id": spec.profile_id,
                })

        gen_usage = self.gen_client.get_usage() if hasattr(self.gen_client, "get_usage") else {}
        eval_usage = self.eval_client.get_usage() if hasattr(self.eval_client, "get_usage") else {}
        wall_clock = round(time.time() - session_start, 2)

        esc = judge_diag.get("escalation", {}) if isinstance(judge_diag, dict) else {}
        esc_extra_tokens = esc.get("extra_total_tokens")
        if esc_extra_tokens is None:
            esc_extra_tokens = None if esc.get("triggered") else 0

        result = {
            "schema_version": 4,
            "session_key": spec.session_key,
            "condition": spec.condition,
            "intervention": spec.intervention,
            "profile_id": spec.profile_id,
            "profile_name": EXPERIMENT_PROFILES[spec.profile_id].name if spec.profile_id in EXPERIMENT_PROFILES else "none",
            "scenario_id": spec.scenario_id,
            "rep": spec.rep,
            "assigned_vector": assigned_vector,
            "inferred_vector": inferred_vector,
            "escalated_vector": assessment.judge_diagnostics.get("escalation", {}).get("inferred_vector"),
            "rule_based_vector": rule_based_vector,
            "per_model_scores": assessment.per_model_scores,
            "per_model_order_scores": assessment.per_model_order_scores,
            "overall_confidence": assessment.overall_confidence,
            "quality_audit": self._quality_audit,
            "judge_diagnostics": judge_diag,
            "features": features.to_dict(),
            "candidate_pool": candidate_pool_logs,
            "trajectory_scores": trajectory_scores,
            "trajectory_diagnostics": trajectory_diagnostics,
            "pressure_metrics": {
                "perceived_pressure": perceived_pressure,
                "stress_index": stress_index,
            },
            "usage": {
                "candidate_generation_input_tokens": gen_usage.get("prompt_tokens"),
                "candidate_generation_output_tokens": gen_usage.get("completion_tokens"),
                "judge_input_tokens": eval_usage.get("prompt_tokens"),
                "judge_output_tokens": eval_usage.get("completion_tokens"),
                "escalation_extra_tokens": esc_extra_tokens,
                "total_session_cost_usd": round((gen_usage.get("total_cost_usd", 0.0) + eval_usage.get("total_cost_usd", 0.0)), 6),
                "wall_clock_seconds": wall_clock,
            },
            "stats": {
                "total_turns": stats.total_turns,
                "candidate_turns": stats.candidate_turns,
                "candidate_word_count": stats.candidate_word_count,
                "candidate_avg_words_per_turn": stats.candidate_avg_words_per_turn,
                "times_addressed_others_by_name": stats.times_addressed_others_by_name,
                "times_asked_questions": stats.times_asked_questions,
                "times_expressed_disagreement": stats.times_expressed_disagreement,
                "times_acknowledged_others": stats.times_acknowledged_others,
                "times_proposed_new_ideas": stats.times_proposed_new_ideas,
            },
            "assessment_summary": assessment.behavioral_summary,
            "transcript": [
                {
                    "turn": t.turn_number,
                    "speaker": t.speaker_name,
                    "content": t.content,
                }
                for t in engine.turns
            ],
            "controller_log": controller.log.to_dict() if controller else None,
            "timestamp": datetime.now().isoformat(),
        }

        return result

    async def _run_session_loop(self, engine: GroupEngine, candidate: ExperimentCandidateAgent, scenario):
        """
        Run the session turn loop.

        Pattern:
        1. Engine generates opening
        2. Loop: candidate responds -> engine generates AI response
        3. Until session ends or max turns reached
        """
        candidate_pool_logs: list[dict] = []
        # Generate opening
        await engine.generate_opening()

        # Calculate total candidate turns from scenario phases
        total_phase_turns = sum(p.turns for p in scenario.phases)
        # Candidate gets roughly half the total turns (other half is AI agents)
        max_candidate_turns = max(total_phase_turns // 2, 8)

        for turn_idx in range(max_candidate_turns):
            # Check if session has ended
            if engine.state == SessionState.ENDED:
                break

            # Get current phase style for context
            phase_style = engine.current_phase_config.style

            # Candidate generates response
            text = await candidate.generate_response(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_style=phase_style,
            )

            # Submit to engine
            await engine.submit_candidate_turn(text)

            # Generate AI response(s)
            ai_turns = await engine.generate_ai_response()

            # Check if session ended after AI response
            if engine.state == SessionState.ENDED:
                break

        # If session didn't end naturally, end it
        if engine.state != SessionState.ENDED:
            engine.end_session()

        return candidate_pool_logs

    async def _run_bcfc_session_loop(
        self,
        engine: GroupEngine,
        candidate: ExperimentCandidateAgent,
        scenario,
        controller,
    ):
        """
        BCFC session loop with Fidelity Controller + Best-of-N selection.

        Differences from standard loop:
        - Every N candidate turns: controller checks features and injects nudge
        - Every candidate turn: BoN candidate pool scored against contract
        """
        from experiment.fidelity_controller import ConstraintViolation
        await engine.generate_opening()

        total_phase_turns = sum(p.turns for p in scenario.phases)
        max_candidate_turns = max(total_phase_turns // 2, 8)
        candidate_turn_count = 0
        candidate_pool_logs: list[dict] = []

        for turn_idx in range(max_candidate_turns):
            if engine.state == SessionState.ENDED:
                break

            phase_style = engine.current_phase_config.style

            # Fidelity check and nudge injection
            nudge = controller.check_and_nudge(
                engine.turns, candidate_turn_count, "Candidate"
            )
            candidate.update_nudge(nudge)

            # Generate candidate pool
            candidates = await candidate.generate_candidate_pool(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_style=phase_style,
                n=DEFAULT_CONFIG.bon_n,
            )

            scored = controller.score_candidates(engine.turns, candidates, "Candidate")
            if not scored:
                text = "I think we should consider all options before deciding."
                selected_idx = -1
            else:
                scored_sorted = sorted(scored, key=lambda x: x["score"], reverse=True)
                selected = scored_sorted[0]
                text = selected["text"]
                selected_idx = scored.index(selected)

                # Record violations for selected candidate
                for v in selected.get("violations", []):
                    controller.record_violation(
                        ConstraintViolation(
                            turn_number=candidate_turn_count + 1,
                            constraint=v.get("constraint", ""),
                            violation_type=v.get("violation_type", ""),
                            original_text=v.get("original_text", ""),
                            retry_count=0,
                            final_text=text,
                        )
                    )

            candidate_pool_logs.append({
                "turn_number": candidate_turn_count + 1,
                "selection_mode": "full_score",
                "selected_index": selected_idx,
                "candidates": scored,
            })

            # Submit to engine
            await engine.submit_candidate_turn(text)
            candidate_turn_count += 1

            # Generate AI response(s)
            await engine.generate_ai_response()

            if engine.state == SessionState.ENDED:
                break

        if engine.state != SessionState.ENDED:
            engine.end_session()

        controller.log.total_candidate_turns = candidate_turn_count
        return candidate_pool_logs

    async def _run_bon_random_session_loop(
        self,
        engine: GroupEngine,
        candidate: ExperimentCandidateAgent,
        scenario,
    ) -> list[dict]:
        """
        BoN-random loop: generate N candidates and select randomly.
        Used for compute-control subset (no contract, no nudges).
        """
        await engine.generate_opening()

        total_phase_turns = sum(p.turns for p in scenario.phases)
        max_candidate_turns = max(total_phase_turns // 2, 8)
        candidate_turn_count = 0
        candidate_pool_logs: list[dict] = []

        for turn_idx in range(max_candidate_turns):
            if engine.state == SessionState.ENDED:
                break

            phase_style = engine.current_phase_config.style

            candidates = await candidate.generate_candidate_pool(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_style=phase_style,
                n=DEFAULT_CONFIG.bon_n,
            )
            if not candidates:
                text = "I think we should consider all options before deciding."
                selected_idx = -1
            else:
                selected_idx = random.randint(0, len(candidates) - 1)
                text = candidates[selected_idx]

            candidate_pool_logs.append({
                "turn_number": candidate_turn_count + 1,
                "selection_mode": "random",
                "selected_index": selected_idx,
                "candidates": [{"text": t} for t in candidates],
            })

            await engine.submit_candidate_turn(text)
            candidate_turn_count += 1

            await engine.generate_ai_response()

            if engine.state == SessionState.ENDED:
                break

        if engine.state != SessionState.ENDED:
            engine.end_session()

        return candidate_pool_logs

    async def _run_bcfc_v3_session_loop(
        self,
        engine: GroupEngine,
        candidate: ExperimentCandidateAgent,
        scenario,
        controller,
    ):
        """
        BCFC v3 mini loop: best-of-styles + phase-conditioned scoring + hidden scaffold.
        """
        from experiment.fidelity_controller import ConstraintViolation
        await engine.generate_opening()

        total_phase_turns = sum(p.turns for p in scenario.phases)
        max_candidate_turns = max(total_phase_turns // 2, 8)
        candidate_turn_count = 0
        candidate_pool_logs: list[dict] = []

        for _ in range(max_candidate_turns):
            if engine.state == SessionState.ENDED:
                break

            phase_style = engine.current_phase_config.style
            phase_name = engine.current_phase_config.name
            phase_cues = engine.current_phase_config.cues if hasattr(engine.current_phase_config, "cues") else []
            target_traits = engine.current_phase_config.target_traits if hasattr(engine.current_phase_config, "target_traits") else []

            # Fidelity check and nudge injection
            nudge = controller.check_and_nudge(
                engine.turns, candidate_turn_count, "Candidate"
            )
            candidate.update_nudge(nudge)

            style_slots = DEFAULT_CONFIG.v3_style_slots
            slot_candidates = await candidate.generate_candidate_pool_styles(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_style=phase_style,
                style_slots=style_slots,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
            )
            candidates = [c["text"] for c in slot_candidates]

            scored = controller.score_candidates_phase(
                engine.turns, candidates, phase_name, "Candidate"
            )
            if not scored:
                text = "I think we should consider all options before deciding."
                selected_idx = -1
            else:
                scored_sorted = sorted(scored, key=lambda x: x["score"], reverse=True)
                selected = scored_sorted[0]
                text = selected["text"]
                selected_idx = scored.index(selected)

                for v in selected.get("violations", []):
                    controller.record_violation(
                        ConstraintViolation(
                            turn_number=candidate_turn_count + 1,
                            constraint=v.get("constraint", ""),
                            violation_type=v.get("violation_type", ""),
                            original_text=v.get("original_text", ""),
                            retry_count=0,
                            final_text=text,
                        )
                    )

            candidate_pool_logs.append({
                "turn_number": candidate_turn_count + 1,
                "selection_mode": "full_score_v3",
                "phase_name": phase_name,
                "selected_index": selected_idx,
                "style_slots": [c["slot"] for c in slot_candidates],
                "policy_plan": slot_candidates[0].get("policy_plan") if slot_candidates else None,
                "scaffold": slot_candidates[0].get("policy_plan") if slot_candidates else None,
                "candidates": scored,
            })

            await engine.submit_candidate_turn(text)
            candidate_turn_count += 1

            await engine.generate_ai_response()

            if engine.state == SessionState.ENDED:
                break

        if engine.state != SessionState.ENDED:
            engine.end_session()

        controller.log.total_candidate_turns = candidate_turn_count
        return candidate_pool_logs

    async def _run_bcfc_v4_session_loop(
        self,
        engine: GroupEngine,
        candidate: ExperimentCandidateAgent,
        scenario,
        controller,
    ):
        """
        BCFC v4 loop: policy planner + best-of-styles + phase-conditioned scoring.
        """
        from experiment.fidelity_controller import ConstraintViolation
        from experiment.memory_backend import (
            InMemoryBackend,
            extract_commitments,
            extract_relationship_signal,
            build_memory_context,
        )

        await engine.generate_opening()

        memory = InMemoryBackend()
        # Seed memory with opening turns
        for t in engine.turns:
            memory.append_turn(t.turn_number, t.speaker_name, t.content, engine.current_phase_config.name)

        total_phase_turns = sum(p.turns for p in scenario.phases)
        max_candidate_turns = max(total_phase_turns // 2, 8)
        candidate_turn_count = 0
        candidate_pool_logs: list[dict] = []

        for _ in range(max_candidate_turns):
            if engine.state == SessionState.ENDED:
                break

            phase_cfg = engine.current_phase_config
            phase_style = phase_cfg.style
            phase_name = phase_cfg.name
            phase_cues = phase_cfg.cues if hasattr(phase_cfg, "cues") else []
            target_traits = phase_cfg.target_traits if hasattr(phase_cfg, "target_traits") else []

            # Fidelity check and nudge injection
            nudge = controller.check_and_nudge(
                engine.turns, candidate_turn_count, "Candidate"
            )
            candidate.update_nudge(nudge)

            policy_plan = await candidate.generate_policy_plan(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
            )

            style_slots = DEFAULT_CONFIG.v4_phase_slots.get(phase_name, DEFAULT_CONFIG.v4_style_slots)
            slot_candidates = await candidate.generate_candidate_pool_styles(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_style=phase_style,
                style_slots=style_slots,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
                policy_plan=policy_plan,
            )
            candidates = [c["text"] for c in slot_candidates]

            memory_context = build_memory_context(memory)
            scored = controller.score_candidates_policy(
                engine.turns,
                candidates,
                policy_plan=policy_plan,
                phase_context={
                    "phase_name": phase_name,
                    "phase_style": phase_style,
                    "phase_cues": phase_cues,
                    "target_traits": target_traits,
                },
                memory_context=memory_context,
                candidate_name="Candidate",
            )

            if not scored:
                text = "I think we should consider all options before deciding."
                selected_idx = -1
            else:
                scored_sorted = sorted(scored, key=lambda x: x["score"], reverse=True)
                selected = scored_sorted[0]
                text = selected["text"]
                selected_idx = scored.index(selected)

                for v in selected.get("violations", []):
                    controller.record_violation(
                        ConstraintViolation(
                            turn_number=candidate_turn_count + 1,
                            constraint=v.get("constraint", ""),
                            violation_type=v.get("violation_type", ""),
                            original_text=v.get("original_text", ""),
                            retry_count=0,
                            final_text=text,
                        )
                    )

            candidate_pool_logs.append({
                "turn_number": candidate_turn_count + 1,
                "selection_mode": "full_score_v4",
                "phase_name": phase_name,
                "phase_cues": phase_cues,
                "phase_target_traits": target_traits,
                "selected_index": selected_idx,
                "style_slots": [c["slot"] for c in slot_candidates],
                "policy_plan": policy_plan,
                "memory_snapshot": {
                    "commitments": [c.__dict__ for c in memory_context.get("commitments", [])],
                    "relationships": [r.__dict__ for r in memory_context.get("relationships", [])],
                },
                "candidates": scored,
            })

            await engine.submit_candidate_turn(text)
            candidate_turn_count += 1

            # Update memory with candidate turn + commitments
            memory.append_turn(candidate_turn_count, "Candidate", text, phase_name)
            memory.add_commitments(extract_commitments(text, candidate_turn_count, phase_name))
            rel = extract_relationship_signal(text)
            if rel:
                counterpart, sentiment, strength = rel
                memory.update_relationship(counterpart, sentiment, strength, candidate_turn_count)

            await engine.generate_ai_response()

            if engine.state == SessionState.ENDED:
                break

        if engine.state != SessionState.ENDED:
            engine.end_session()

        controller.log.total_candidate_turns = candidate_turn_count
        return candidate_pool_logs

    async def _run_bcfc_v5_session_loop(
        self,
        engine: GroupEngine,
        candidate: ExperimentCandidateAgent,
        scenario,
        controller,
    ):
        """
        BCFC v5 loop: opportunity-gated O/C execution + policy bridge scoring.

        Relative to v4:
        - trait execution invariants are injected at generation time (when relevant)
        - candidate scoring uses v5 weights with opportunity-gated O/C execution
        """
        from experiment.fidelity_controller import ConstraintViolation
        from experiment.memory_backend import (
            InMemoryBackend,
            extract_commitments,
            extract_relationship_signal,
            build_memory_context,
        )

        await engine.generate_opening()

        memory = InMemoryBackend()
        for t in engine.turns:
            memory.append_turn(t.turn_number, t.speaker_name, t.content, engine.current_phase_config.name)

        total_phase_turns = sum(p.turns for p in scenario.phases)
        max_candidate_turns = max(total_phase_turns // 2, 8)
        candidate_turn_count = 0
        candidate_pool_logs: list[dict] = []

        for _ in range(max_candidate_turns):
            if engine.state == SessionState.ENDED:
                break

            phase_cfg = engine.current_phase_config
            phase_style = phase_cfg.style
            phase_name = phase_cfg.name
            phase_cues = phase_cfg.cues if hasattr(phase_cfg, "cues") else []
            target_traits = phase_cfg.target_traits if hasattr(phase_cfg, "target_traits") else []

            nudge = controller.check_and_nudge(
                engine.turns, candidate_turn_count, "Candidate"
            )
            candidate.update_nudge(nudge)

            policy_plan = await candidate.generate_policy_plan(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
            )

            style_slots = DEFAULT_CONFIG.v5_phase_slots.get(phase_name, DEFAULT_CONFIG.v4_style_slots)
            slot_candidates = await candidate.generate_candidate_pool_styles(
                turns=engine.turns,
                scenario_brief=scenario.brief,
                phase_style=phase_style,
                style_slots=style_slots,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
                policy_plan=policy_plan,
                enable_trait_execution=True,
            )
            candidates = [c["text"] for c in slot_candidates]

            memory_context = build_memory_context(memory)
            scored = controller.score_candidates_policy(
                engine.turns,
                candidates,
                policy_plan=policy_plan,
                phase_context={
                    "phase_name": phase_name,
                    "phase_style": phase_style,
                    "phase_cues": phase_cues,
                    "target_traits": target_traits,
                },
                memory_context=memory_context,
                candidate_name="Candidate",
                scoring_version="v5",
            )

            if not scored:
                text = "I think we should consider all options before deciding."
                selected_idx = -1
                selection_audit = {
                    "turn_number": candidate_turn_count + 1,
                    "phase_name": phase_name,
                    "selection_mode": "two_stage_v5",
                    "error": "empty_scored_pool",
                }
                controller.log.selection_audit.append(selection_audit)
            else:
                selection = controller.select_candidate_policy_v5(
                    scored=scored,
                    phase_context={
                        "phase_name": phase_name,
                        "phase_style": phase_style,
                        "phase_cues": phase_cues,
                        "target_traits": target_traits,
                    },
                    turn_number=candidate_turn_count + 1,
                )
                selected = selection.get("selected")
                selected_idx = int(selection.get("selected_index", -1))
                selection_audit = selection.get("audit", {})
                if not selected:
                    selected = max(scored, key=lambda x: x.get("score", 0.0))
                    selected_idx = scored.index(selected)
                text = selected["text"]

                for v in selected.get("violations", []):
                    controller.record_violation(
                        ConstraintViolation(
                            turn_number=candidate_turn_count + 1,
                            constraint=v.get("constraint", ""),
                            violation_type=v.get("violation_type", ""),
                            original_text=v.get("original_text", ""),
                            retry_count=0,
                            final_text=text,
                        )
                    )

            candidate_pool_logs.append({
                "turn_number": candidate_turn_count + 1,
                "selection_mode": "two_stage_v5",
                "phase_name": phase_name,
                "phase_cues": phase_cues,
                "phase_target_traits": target_traits,
                "selected_index": selected_idx,
                "style_slots": [c["slot"] for c in slot_candidates],
                "policy_plan": policy_plan,
                "selection_audit": selection_audit,
                "memory_snapshot": {
                    "commitments": [c.__dict__ for c in memory_context.get("commitments", [])],
                    "relationships": [r.__dict__ for r in memory_context.get("relationships", [])],
                },
                "candidates": scored,
            })

            await engine.submit_candidate_turn(text)
            candidate_turn_count += 1

            memory.append_turn(candidate_turn_count, "Candidate", text, phase_name)
            memory.add_commitments(extract_commitments(text, candidate_turn_count, phase_name))
            rel = extract_relationship_signal(text)
            if rel:
                counterpart, sentiment, strength = rel
                memory.update_relationship(counterpart, sentiment, strength, candidate_turn_count)

            await engine.generate_ai_response()

            if engine.state == SessionState.ENDED:
                break

        if engine.state != SessionState.ENDED:
            engine.end_session()

        controller.log.total_candidate_turns = candidate_turn_count
        return candidate_pool_logs

    def _save_session_result(self, result: dict, index: int):
        """Save a single session result to JSON."""
        filename = f"session_{index:04d}_{result['session_key']}.json"
        filepath = self.output_dir / filename
        with open(filepath, "w") as f:
            json.dump(result, f, indent=2, default=str)
        logger.info(f"Saved: {filepath}")

    def _save_failures(self):
        """Save failure log."""
        filepath = self.output_dir / "failures.json"
        with open(filepath, "w") as f:
            json.dump(self.failures, f, indent=2)

    def _save_uncertain_queue(self):
        """Save uncertain trait evaluations to CSV for human-anchor sampling (Phase 4)."""
        import csv
        filepath = self.output_dir / "uncertain_queue.csv"
        fieldnames = ["session_key", "trait", "reason", "assigned", "inferred", "scenario_id", "profile_id"]
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.uncertain_rows)
        print(f"Uncertain queue saved to {filepath} ({len(self.uncertain_rows)} rows)")

    def _build_summary(self, total: int) -> dict:
        """Build experiment summary."""
        elapsed = time.time() - self.start_time if self.start_time else 0
        return {
            "total_sessions": total,
            "completed": self.completed_count,
            "failed": len(self.failures),
            "duration_seconds": round(elapsed),
            "avg_session_seconds": round(elapsed / max(self.completed_count, 1)),
            "timestamp": datetime.now().isoformat(),
        }

    def _save_summary(self, summary: dict):
        """Save experiment summary."""
        filepath = self.output_dir / "experiment_summary.json"
        with open(filepath, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\nSummary saved to {filepath}")
