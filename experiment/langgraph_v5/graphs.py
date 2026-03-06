"""LangGraph graphs for BCFC v5 runtime."""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
import time
from typing import Any

from langgraph.graph import END, START, StateGraph

from config.group_scenarios import create_scenario
from engines.group_engine import GroupEngine
from evaluation.rule_based_evaluator import evaluate_rule_based
from evaluation.trajectory_judge import evaluate_perceived_pressure, evaluate_trajectory
from evaluation.trait_evaluator import evaluate_group_session
from experiment.bcfc_config import DEFAULT_CONFIG
from experiment.behavioral_features import extract_features
from experiment.candidate_agent import ExperimentCandidateAgent
from experiment.fidelity_controller import ConstraintViolation, FidelityController
from experiment.memory_backend import (
    InMemoryBackend,
    build_memory_context,
    extract_commitments,
    extract_relationship_signal,
)
from experiment.persona_compiler import compile_contract
from experiment.profiles import (
    EXPERIMENT_PROFILES,
    build_baseline_a_prompt,
    build_baseline_b_prompt,
)
from experiment.trajectory_metrics import (
    compute_contradiction_rate,
    compute_direct_question_answer_rate,
    compute_over_verbosity_rate,
    compute_stress_index,
    compute_unsolicited_structure_rate,
)
from utils.models import SessionState, SpeakerRole

from .state import BCFCV5GraphState


class BCFCV5LangGraphNodes:
    """Node implementations for the BCFC v5 LangGraph runtime."""

    async def bootstrap_session(self, state: BCFCV5GraphState) -> dict[str, Any]:
        spec = state["spec"]
        gen_client = state["gen_client"]
        eval_client = state["eval_client"]

        if hasattr(gen_client, "reset_usage"):
            gen_client.reset_usage()
        if hasattr(eval_client, "reset_usage"):
            eval_client.reset_usage()

        scenario = create_scenario(spec.scenario_id)
        system_prompt = None
        assigned_vector = None

        if spec.condition in ("main", "mini_v5", "mini_v5_langgraph"):
            profile = EXPERIMENT_PROFILES[spec.profile_id]
            system_prompt = profile.build_system_prompt(scenario.brief)
            assigned_vector = profile.get_vector()
        elif spec.condition == "baseline_a":
            system_prompt = build_baseline_a_prompt(scenario.brief)
        elif spec.condition == "baseline_b":
            profile = EXPERIMENT_PROFILES[spec.profile_id]
            system_prompt, shuffled_vec = build_baseline_b_prompt(scenario.brief, profile)
            assigned_vector = shuffled_vec
            spec.assigned_vector = shuffled_vec

        return {
            "scenario": scenario,
            "system_prompt": system_prompt,
            "assigned_vector": assigned_vector,
            "session_start": time.time(),
            "candidate_turn_count": 0,
            "candidate_pool_logs": [],
            "uncertain_rows": [],
        }

    async def compile_contract_node(self, state: BCFCV5GraphState) -> dict[str, Any]:
        spec = state["spec"]
        assigned_vector = state.get("assigned_vector")
        if not assigned_vector:
            raise ValueError("LangGraph v5 runtime requires an assigned personality vector")

        contract = compile_contract(spec.profile_id, assigned_vector)
        controller = FidelityController(contract, spec.session_key)
        return {"controller": controller}

    async def init_runtime_state(self, state: BCFCV5GraphState) -> dict[str, Any]:
        spec = state["spec"]
        scenario = state["scenario"]
        system_prompt = state["system_prompt"]

        engine = GroupEngine(
            client=state["gen_client"],
            participant_id=f"exp_{spec.session_key}",
            participant_name="Candidate",
            scenario=scenario,
        )
        candidate = ExperimentCandidateAgent(
            client=state["gen_client"],
            system_prompt=system_prompt,
            candidate_name="Candidate",
        )
        memory_backend = InMemoryBackend()
        total_phase_turns = sum(phase.turns for phase in scenario.phases)
        max_candidate_turns = max(total_phase_turns // 2, 8)

        return {
            "engine": engine,
            "candidate": candidate,
            "memory_backend": memory_backend,
            "max_candidate_turns": max_candidate_turns,
        }

    async def environment_opening_turn(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        memory_backend = state["memory_backend"]

        await engine.generate_opening()
        opening_phase = engine.current_phase_config.name
        for turn in engine.turns:
            memory_backend.append_turn(turn.turn_number, turn.speaker_name, turn.content, opening_phase)
        return {}

    def route_session_loop(self, state: BCFCV5GraphState) -> str:
        engine = state["engine"]
        controller = state["controller"]
        candidate_turn_count = state.get("candidate_turn_count", 0)
        max_candidate_turns = state["max_candidate_turns"]

        controller.log.total_candidate_turns = candidate_turn_count
        if engine.state == SessionState.ENDED or candidate_turn_count >= max_candidate_turns:
            if engine.state != SessionState.ENDED:
                engine.end_session()
            return "finalize_session_artifacts"
        return "candidate_actor_subgraph"

    async def prepare_candidate_turn(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        phase_cfg = engine.current_phase_config
        style_slots = DEFAULT_CONFIG.v5_phase_slots.get(
            phase_cfg.name, DEFAULT_CONFIG.v4_style_slots
        )
        return {
            "phase_name": phase_cfg.name,
            "phase_style": phase_cfg.style,
            "phase_cues": list(phase_cfg.cues) if getattr(phase_cfg, "cues", None) else [],
            "target_traits": list(phase_cfg.target_traits) if getattr(phase_cfg, "target_traits", None) else [],
            "style_slots": style_slots,
            "slot_candidates": [],
            "scored_candidates": [],
            "selection_audit": {},
            "selected_candidate": {},
            "selected_candidate_text": "",
            "selected_candidate_index": -1,
            "environment_turns": [],
        }

    async def drift_check_and_nudge(self, state: BCFCV5GraphState) -> dict[str, Any]:
        controller = state["controller"]
        engine = state["engine"]
        candidate = state["candidate"]
        nudge = controller.check_and_nudge(
            engine.turns,
            state.get("candidate_turn_count", 0),
            "Candidate",
        )
        candidate.update_nudge(nudge)
        return {"current_nudge": nudge}

    async def build_candidate_memory_context(self, state: BCFCV5GraphState) -> dict[str, Any]:
        return {"memory_context": build_memory_context(state["memory_backend"])}

    async def infer_opportunity_scores(self, state: BCFCV5GraphState) -> dict[str, Any]:
        controller = state["controller"]
        engine = state["engine"]
        phase_context = {
            "phase_name": state["phase_name"],
            "phase_style": state["phase_style"],
            "phase_cues": state["phase_cues"],
            "target_traits": state["target_traits"],
        }
        opportunity_scores = controller._trait_opportunity_scores(engine.turns, phase_context)
        activation_mask = controller._build_activation_mask(
            opportunities=opportunity_scores,
            target_traits=state["target_traits"],
            apply_floor=True,
        )
        return {
            "opportunity_scores": opportunity_scores,
            "activation_mask": activation_mask,
        }

    async def plan_candidate_policy(self, state: BCFCV5GraphState) -> dict[str, Any]:
        candidate = state["candidate"]
        scenario = state["scenario"]
        engine = state["engine"]
        policy_plan = await candidate.generate_policy_plan(
            turns=engine.turns,
            scenario_brief=scenario.brief,
            phase_name=state["phase_name"],
            phase_cues=state["phase_cues"],
            target_traits=state["target_traits"],
        )
        return {"policy_plan": policy_plan}

    async def generate_slot_candidates(self, state: BCFCV5GraphState) -> dict[str, Any]:
        candidate = state["candidate"]
        scenario = state["scenario"]
        engine = state["engine"]
        slot_candidates = await candidate.generate_candidate_pool_styles(
            turns=engine.turns,
            scenario_brief=scenario.brief,
            phase_style=state["phase_style"],
            style_slots=state["style_slots"],
            phase_name=state["phase_name"],
            phase_cues=state["phase_cues"],
            target_traits=state["target_traits"],
            policy_plan=state["policy_plan"],
            enable_trait_execution=True,
        )
        return {"slot_candidates": slot_candidates}

    async def score_candidate_pool(self, state: BCFCV5GraphState) -> dict[str, Any]:
        controller = state["controller"]
        engine = state["engine"]
        memory_context = state["memory_context"]
        candidates = [candidate["text"] for candidate in state["slot_candidates"]]
        phase_context = {
            "phase_name": state["phase_name"],
            "phase_style": state["phase_style"],
            "phase_cues": state["phase_cues"],
            "target_traits": state["target_traits"],
        }
        scored = controller.score_candidates_policy(
            engine.turns,
            candidates,
            policy_plan=state["policy_plan"],
            phase_context=phase_context,
            memory_context=memory_context,
            candidate_name="Candidate",
            scoring_version="v5",
        )
        return {"scored_candidates": scored}

    async def select_candidate_response(self, state: BCFCV5GraphState) -> dict[str, Any]:
        controller = state["controller"]
        memory_context = state["memory_context"]
        phase_context = {
            "phase_name": state["phase_name"],
            "phase_style": state["phase_style"],
            "phase_cues": state["phase_cues"],
            "target_traits": state["target_traits"],
        }
        scored = state["scored_candidates"]

        if not scored:
            text = "I think we should consider all options before deciding."
            selected_idx = -1
            selected = {
                "text": text,
                "score": 0.0,
                "policy_match": 0.0,
                "situational_adequacy": 0.0,
                "trait_execution": 0.0,
                "activation_weighted_contract_distance": 1.0,
                "violations": [],
            }
            selection_audit = {
                "turn_number": state["candidate_turn_count"] + 1,
                "phase_name": state["phase_name"],
                "selection_mode": "two_stage_v5",
                "error": "empty_scored_pool",
            }
            controller.log.selection_audit.append(selection_audit)
        else:
            selection = controller.select_candidate_policy_v5(
                scored=scored,
                phase_context=phase_context,
                turn_number=state["candidate_turn_count"] + 1,
            )
            selected = selection.get("selected")
            selected_idx = int(selection.get("selected_index", -1))
            selection_audit = selection.get("audit", {})
            if not selected:
                selected = max(scored, key=lambda row: row.get("score", 0.0))
                selected_idx = scored.index(selected)

        pool_log = {
            "turn_number": state["candidate_turn_count"] + 1,
            "selection_mode": "two_stage_v5",
            "phase_name": state["phase_name"],
            "phase_cues": state["phase_cues"],
            "phase_target_traits": state["target_traits"],
            "selected_index": selected_idx,
            "style_slots": [candidate["slot"] for candidate in state["slot_candidates"]],
            "policy_plan": state["policy_plan"],
            "selection_audit": selection_audit,
            "memory_snapshot": {
                "commitments": [commitment.__dict__ for commitment in memory_context.get("commitments", [])],
                "relationships": [rel.__dict__ for rel in memory_context.get("relationships", [])],
            },
            "candidates": scored,
        }

        candidate_pool_logs = list(state.get("candidate_pool_logs", []))
        candidate_pool_logs.append(pool_log)

        for violation in selected.get("violations", []):
            controller.record_violation(
                ConstraintViolation(
                    turn_number=state["candidate_turn_count"] + 1,
                    constraint=violation.get("constraint", ""),
                    violation_type=violation.get("violation_type", ""),
                    original_text=violation.get("original_text", ""),
                    retry_count=0,
                    final_text=selected["text"],
                )
            )

        return {
            "candidate_pool_logs": candidate_pool_logs,
            "selection_audit": selection_audit,
            "selected_candidate": selected,
            "selected_candidate_text": selected["text"],
            "selected_candidate_index": selected_idx,
        }

    async def append_candidate_turn(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        await engine.submit_candidate_turn(state["selected_candidate_text"])
        return {"candidate_turn_count": state["candidate_turn_count"] + 1}

    async def update_memory_after_candidate(self, state: BCFCV5GraphState) -> dict[str, Any]:
        memory_backend = state["memory_backend"]
        text = state["selected_candidate_text"]
        turn_number = state["candidate_turn_count"]
        phase_name = state["phase_name"]

        memory_backend.append_turn(turn_number, "Candidate", text, phase_name)
        memory_backend.add_commitments(extract_commitments(text, turn_number, phase_name))
        relationship_signal = extract_relationship_signal(text)
        if relationship_signal:
            counterpart, sentiment, strength = relationship_signal
            memory_backend.update_relationship(counterpart, sentiment, strength, turn_number)
        return {}

    async def prepare_environment_turn(self, state: BCFCV5GraphState) -> dict[str, Any]:
        return {
            "environment_action": "prepare",
            "environment_turns": [],
            "environment_primary_speaker": None,
        }

    def route_environment_action(self, state: BCFCV5GraphState) -> str:
        engine = state["engine"]
        if engine.should_warn_time:
            return "emit_time_warning"
        if engine.should_wrap_up:
            return "emit_closing_turn"
        if engine.is_time_expired:
            return "expire_session"
        return "dispatch_primary_environment_response"

    async def emit_time_warning(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        minutes_left = int(engine.remaining_seconds / 60)
        warning = (
            f"Just a heads up, we have about {minutes_left} minutes left. "
            "We should start wrapping up our discussion."
        )
        turn = engine._create_turn(SpeakerRole.JORDAN, "Jordan", warning)
        engine.turns.append(turn)
        engine._sync_agent_histories()
        engine.mark_warned()
        return {"environment_turns": [turn]}

    def route_after_warning(self, state: BCFCV5GraphState) -> str:
        engine = state["engine"]
        if engine.should_wrap_up:
            return "emit_closing_turn"
        if engine.is_time_expired:
            return "expire_session"
        return "dispatch_primary_environment_response"

    async def emit_closing_turn(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        closing = await engine._generate_closing_turn()
        engine.turns.append(closing)
        engine._sync_agent_histories()
        engine.mark_wrapping_up()
        return {"environment_turns": [closing]}

    async def expire_session(self, state: BCFCV5GraphState) -> dict[str, Any]:
        state["engine"].end_session()
        return {}

    async def dispatch_primary_environment_response(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        phase_cfg = engine.current_phase_config
        speaker_name, response_text, latency = await engine.moderator.dispatch_turn(
            turns=engine.turns,
            current_phase=engine.current_phase,
            phase_style=phase_cfg.style,
            phase_goal=phase_cfg.goal,
        )
        engine.add_llm_wait_time(latency)
        role = SpeakerRole[speaker_name.upper()]
        turn = engine._create_turn(role, speaker_name, response_text)
        engine.turns.append(turn)
        engine._sync_agent_histories()
        return {
            "environment_primary_speaker": speaker_name,
            "environment_turns": [turn],
        }

    async def maybe_dispatch_second_environment_response(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        primary_speaker = state.get("environment_primary_speaker")
        if not primary_speaker:
            return {}

        second_speaker = engine.moderator.should_add_second_response(
            primary_speaker,
            engine.turns,
            engine.current_phase_config.style,
        )
        if not second_speaker:
            return {}

        engine._sync_agent_histories()
        second_response, second_latency = await engine.moderator.dispatch_second_turn(
            second_speaker, engine.turns
        )
        if not second_response:
            return {}

        engine.add_llm_wait_time(second_latency)
        second_role = SpeakerRole[second_speaker.upper()]
        second_turn = engine._create_turn(second_role, second_speaker, second_response)
        engine.turns.append(second_turn)
        engine._sync_agent_histories()

        environment_turns = list(state.get("environment_turns", []))
        environment_turns.append(second_turn)
        return {"environment_turns": environment_turns}

    async def finalize_session_artifacts(self, state: BCFCV5GraphState) -> dict[str, Any]:
        engine = state["engine"]
        controller = state["controller"]
        controller.log.total_candidate_turns = state["candidate_turn_count"]
        stats = engine.compute_session_stats()
        features = extract_features(engine.turns, candidate_name="Candidate")
        rule_based_vector = evaluate_rule_based(features)
        return {
            "stats": stats,
            "features": features,
            "rule_based_vector": rule_based_vector,
        }

    async def run_personality_assessment(self, state: BCFCV5GraphState) -> dict[str, Any]:
        assessment = await evaluate_group_session(
            client=state["eval_client"],
            turns=state["engine"].turns,
            candidate_name="Candidate",
            stats=state["stats"],
            use_ensemble=True,
            escalate=True,
        )
        inferred_vector = assessment.to_vector().to_dict()
        judge_diagnostics = assessment.judge_diagnostics or {}

        uncertain_rows: list[dict[str, Any]] = []
        if judge_diagnostics.get("uncertain_traits"):
            for trait_abbrev in judge_diagnostics["uncertain_traits"]:
                reasons = judge_diagnostics.get("uncertain_reasons", {}).get(trait_abbrev, [])
                uncertain_rows.append({
                    "session_key": state["spec"].session_key,
                    "trait": trait_abbrev,
                    "reason": ",".join(reasons),
                    "assigned": state["assigned_vector"].get(trait_abbrev) if state.get("assigned_vector") else None,
                    "inferred": inferred_vector.get(trait_abbrev),
                    "scenario_id": state["spec"].scenario_id,
                    "profile_id": state["spec"].profile_id,
                })

        return {
            "assessment": assessment,
            "inferred_vector": inferred_vector,
            "judge_diagnostics": judge_diagnostics,
            "uncertain_rows": uncertain_rows,
        }

    async def run_trajectory_audit(self, state: BCFCV5GraphState) -> dict[str, Any]:
        trajectory_scores = await evaluate_trajectory(
            client=state["eval_client"],
            turns=state["engine"].turns,
            candidate_name="Candidate",
            context_turns=DEFAULT_CONFIG.trajectory_context_turns,
        )
        return {"trajectory_scores": trajectory_scores}

    async def run_pressure_audit(self, state: BCFCV5GraphState) -> dict[str, Any]:
        perceived_pressure = await evaluate_perceived_pressure(
            client=state["eval_client"],
            turns=state["engine"].turns,
            scenario_brief=state["scenario"].brief,
        )
        pressure_metrics = {
            "perceived_pressure": perceived_pressure,
            "stress_index": compute_stress_index(state["engine"].turns),
        }
        return {"pressure_metrics": pressure_metrics}

    async def build_result_record(self, state: BCFCV5GraphState) -> dict[str, Any]:
        spec = state["spec"]
        engine = state["engine"]
        assessment = state["assessment"]
        judge_diagnostics = state["judge_diagnostics"]
        controller = state["controller"]
        gen_usage = state["gen_client"].get_usage() if hasattr(state["gen_client"], "get_usage") else {}
        eval_usage = state["eval_client"].get_usage() if hasattr(state["eval_client"], "get_usage") else {}
        wall_clock = round(time.time() - state["session_start"], 2)

        trajectory_diagnostics = {
            "direct_question_answer_rate": compute_direct_question_answer_rate(engine.turns),
            "contradiction_rate": compute_contradiction_rate(engine.turns),
            "unsolicited_structure_rate": compute_unsolicited_structure_rate(engine.turns),
            "over_verbosity_rate": compute_over_verbosity_rate(engine.turns),
        }

        escalation = judge_diagnostics.get("escalation", {}) if isinstance(judge_diagnostics, dict) else {}
        esc_extra_tokens = escalation.get("extra_total_tokens")
        if esc_extra_tokens is None:
            esc_extra_tokens = None if escalation.get("triggered") else 0

        transcript = [
            {
                "turn": turn.turn_number,
                "speaker": turn.speaker_name,
                "content": turn.content,
            }
            for turn in engine.turns
        ]
        turns = [
            {
                "turn_number": turn.turn_number,
                "speaker_role": turn.speaker_role.value,
                "speaker_name": turn.speaker_name,
                "content": turn.content,
                "timestamp": turn.timestamp.isoformat(),
                "word_count": turn.word_count,
                "is_question": turn.is_question,
            }
            for turn in engine.turns
        ]

        result = {
            "schema_version": 5,
            "runtime_architecture": "langgraph_bcfc_v5",
            "session_key": spec.session_key,
            "condition": spec.condition,
            "intervention": spec.intervention,
            "profile_id": spec.profile_id,
            "profile_name": (
                EXPERIMENT_PROFILES[spec.profile_id].name
                if spec.profile_id in EXPERIMENT_PROFILES
                else "none"
            ),
            "scenario_id": spec.scenario_id,
            "rep": spec.rep,
            "assigned_vector": state["assigned_vector"],
            "inferred_vector": state["inferred_vector"],
            "escalated_vector": judge_diagnostics.get("escalation", {}).get("inferred_vector"),
            "rule_based_vector": state["rule_based_vector"],
            "per_model_scores": assessment.per_model_scores,
            "per_model_order_scores": assessment.per_model_order_scores,
            "overall_confidence": assessment.overall_confidence,
            "quality_audit": state["quality_audit"],
            "judge_diagnostics": judge_diagnostics,
            "features": state["features"].to_dict(),
            "candidate_pool": state["candidate_pool_logs"],
            "trajectory_scores": state["trajectory_scores"],
            "pressure_metrics": state["pressure_metrics"],
            "trajectory_diagnostics": trajectory_diagnostics,
            "controller_log": controller.log.to_dict(),
            "usage": {
                "candidate_generation_input_tokens": gen_usage.get("prompt_tokens"),
                "candidate_generation_output_tokens": gen_usage.get("completion_tokens"),
                "judge_input_tokens": eval_usage.get("prompt_tokens"),
                "judge_output_tokens": eval_usage.get("completion_tokens"),
                "escalation_extra_tokens": esc_extra_tokens,
                "total_session_cost_usd": round(
                    (gen_usage.get("total_cost_usd", 0.0) or 0.0)
                    + (eval_usage.get("total_cost_usd", 0.0) or 0.0),
                    6,
                ),
                "wall_clock_seconds": wall_clock,
            },
            "stats": asdict(state["stats"]),
            "assessment_summary": assessment.behavioral_summary,
            "transcript": transcript,
            "turns": turns,
            "timestamp": datetime.now().isoformat(),
        }
        return {
            "trajectory_diagnostics": trajectory_diagnostics,
            "result": result,
        }


def build_candidate_actor_subgraph(nodes: BCFCV5LangGraphNodes):
    """Build the candidate-side LangGraph subgraph."""
    builder = StateGraph(BCFCV5GraphState)
    builder.add_node("prepare_candidate_turn", nodes.prepare_candidate_turn)
    builder.add_node("drift_check_and_nudge", nodes.drift_check_and_nudge)
    builder.add_node("build_candidate_memory_context", nodes.build_candidate_memory_context)
    builder.add_node("infer_opportunity_scores", nodes.infer_opportunity_scores)
    builder.add_node("plan_candidate_policy", nodes.plan_candidate_policy)
    builder.add_node("generate_slot_candidates", nodes.generate_slot_candidates)
    builder.add_node("score_candidate_pool", nodes.score_candidate_pool)
    builder.add_node("select_candidate_response", nodes.select_candidate_response)
    builder.add_node("append_candidate_turn", nodes.append_candidate_turn)
    builder.add_node("update_memory_after_candidate", nodes.update_memory_after_candidate)

    builder.add_edge(START, "prepare_candidate_turn")
    builder.add_edge("prepare_candidate_turn", "drift_check_and_nudge")
    builder.add_edge("drift_check_and_nudge", "build_candidate_memory_context")
    builder.add_edge("build_candidate_memory_context", "infer_opportunity_scores")
    builder.add_edge("infer_opportunity_scores", "plan_candidate_policy")
    builder.add_edge("plan_candidate_policy", "generate_slot_candidates")
    builder.add_edge("generate_slot_candidates", "score_candidate_pool")
    builder.add_edge("score_candidate_pool", "select_candidate_response")
    builder.add_edge("select_candidate_response", "append_candidate_turn")
    builder.add_edge("append_candidate_turn", "update_memory_after_candidate")
    builder.add_edge("update_memory_after_candidate", END)
    return builder.compile()


def build_environment_subgraph(nodes: BCFCV5LangGraphNodes):
    """Build the environment-side LangGraph subgraph."""
    builder = StateGraph(BCFCV5GraphState)
    builder.add_node("prepare_environment_turn", nodes.prepare_environment_turn)
    builder.add_node("emit_time_warning", nodes.emit_time_warning)
    builder.add_node("emit_closing_turn", nodes.emit_closing_turn)
    builder.add_node("expire_session", nodes.expire_session)
    builder.add_node(
        "dispatch_primary_environment_response",
        nodes.dispatch_primary_environment_response,
    )
    builder.add_node(
        "maybe_dispatch_second_environment_response",
        nodes.maybe_dispatch_second_environment_response,
    )

    builder.add_edge(START, "prepare_environment_turn")
    builder.add_conditional_edges(
        "prepare_environment_turn",
        nodes.route_environment_action,
        {
            "emit_time_warning": "emit_time_warning",
            "emit_closing_turn": "emit_closing_turn",
            "expire_session": "expire_session",
            "dispatch_primary_environment_response": "dispatch_primary_environment_response",
        },
    )
    builder.add_conditional_edges(
        "emit_time_warning",
        nodes.route_after_warning,
        {
            "emit_closing_turn": "emit_closing_turn",
            "expire_session": "expire_session",
            "dispatch_primary_environment_response": "dispatch_primary_environment_response",
        },
    )
    builder.add_edge("emit_closing_turn", END)
    builder.add_edge("expire_session", END)
    builder.add_edge(
        "dispatch_primary_environment_response",
        "maybe_dispatch_second_environment_response",
    )
    builder.add_edge("maybe_dispatch_second_environment_response", END)
    return builder.compile()


def build_post_session_audit_subgraph(nodes: BCFCV5LangGraphNodes):
    """Build the post-session audit LangGraph subgraph."""
    builder = StateGraph(BCFCV5GraphState)
    builder.add_node("run_personality_assessment", nodes.run_personality_assessment)
    builder.add_node("run_trajectory_audit", nodes.run_trajectory_audit)
    builder.add_node("run_pressure_audit", nodes.run_pressure_audit)
    builder.add_node("build_result_record", nodes.build_result_record)

    builder.add_edge(START, "run_personality_assessment")
    builder.add_edge("run_personality_assessment", "run_trajectory_audit")
    builder.add_edge("run_trajectory_audit", "run_pressure_audit")
    builder.add_edge("run_pressure_audit", "build_result_record")
    builder.add_edge("build_result_record", END)
    return builder.compile()


def build_bcfc_v5_session_graph():
    """Build the top-level BCFC v5 LangGraph session runtime."""
    nodes = BCFCV5LangGraphNodes()
    candidate_subgraph = build_candidate_actor_subgraph(nodes)
    environment_subgraph = build_environment_subgraph(nodes)
    audit_subgraph = build_post_session_audit_subgraph(nodes)

    builder = StateGraph(BCFCV5GraphState)
    builder.add_node("bootstrap_session", nodes.bootstrap_session)
    builder.add_node("compile_contract", nodes.compile_contract_node)
    builder.add_node("init_runtime_state", nodes.init_runtime_state)
    builder.add_node("environment_opening_turn", nodes.environment_opening_turn)
    builder.add_node("candidate_actor_subgraph", candidate_subgraph)
    builder.add_node("environment_subgraph", environment_subgraph)
    builder.add_node("finalize_session_artifacts", nodes.finalize_session_artifacts)
    builder.add_node("post_session_audit_subgraph", audit_subgraph)

    builder.add_edge(START, "bootstrap_session")
    builder.add_edge("bootstrap_session", "compile_contract")
    builder.add_edge("compile_contract", "init_runtime_state")
    builder.add_edge("init_runtime_state", "environment_opening_turn")
    builder.add_conditional_edges(
        "environment_opening_turn",
        nodes.route_session_loop,
        {
            "candidate_actor_subgraph": "candidate_actor_subgraph",
            "finalize_session_artifacts": "finalize_session_artifacts",
        },
    )
    builder.add_edge("candidate_actor_subgraph", "environment_subgraph")
    builder.add_conditional_edges(
        "environment_subgraph",
        nodes.route_session_loop,
        {
            "candidate_actor_subgraph": "candidate_actor_subgraph",
            "finalize_session_artifacts": "finalize_session_artifacts",
        },
    )
    builder.add_edge("finalize_session_artifacts", "post_session_audit_subgraph")
    builder.add_edge("post_session_audit_subgraph", END)
    return builder.compile()
