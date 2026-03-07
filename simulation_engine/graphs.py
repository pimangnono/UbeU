"""LangGraph runtime for actor-symmetric stakeholder simulations."""

from __future__ import annotations

from typing import Any

from langgraph.graph import END, START, StateGraph

from .ablation import DEFAULT_ABLATION_CONFIG
from .action_layer import (
    apply_transition_rule,
    arbitrate_phase_actions,
    compile_action_proposal,
)
from .controller import PersonaStateController
from .graph_state import StakeholderGraphState
from .metrics import compute_runtime_metrics, estimate_actor_traits_from_turns, persona_drift_mae
from .runtime import StakeholderSimulationRuntime


class StakeholderSimulationNodes:
    """Node implementations for the stakeholder simulation runtime graph."""

    async def bootstrap_runtime(self, state: StakeholderGraphState) -> dict[str, Any]:
        script = state["script"]
        ablation_config = state.get("ablation_config", DEFAULT_ABLATION_CONFIG)
        runtime = StakeholderSimulationRuntime(
            script=script,
            gen_client=state["gen_client"],
            ablation_config=ablation_config,
        )
        actor_name_map = {
            actor_id: actor.display_name
            for actor_id, actor in runtime.actors.items()
        }
        controllers = {
            actor_id: PersonaStateController(
                actor.actor_spec,
                actor_name_map=actor_name_map,
                ablation_config=ablation_config,
            )
            for actor_id, actor in runtime.actors.items()
        }
        return {
            "runtime": runtime,
            "controllers": controllers,
            "actor_name_map": actor_name_map,
            "phase_turn_index": 0,
            "last_turn_index": 0,
            "simulation_complete": False,
            "injected_events": [],
            "policy_plan": {},
            "candidate_pool": [],
            "scored_candidates": [],
            "selected_candidate": {},
            "selected_candidate_text": "",
            "selected_meta": {},
            "selected_action_proposal": None,
            "approved_phase_actions": [],
            "rejected_phase_actions": [],
            "executed_phase_actions": [],
            "phase_feedback": {},
            "phase_boundary_reached": False,
        }

    def route_turn_loop(self, state: StakeholderGraphState) -> str:
        return "finalize_run" if state.get("simulation_complete") else "inject_world_events"

    async def inject_world_events(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        script = state["script"]
        injected_events = set(state.get("injected_events", []))
        current_phase = runtime.current_phase
        pending: list[str] = []
        next_turn = runtime.turn_index + 1

        for event in script.world_events:
            if event.event_id in injected_events:
                continue
            phase_match = event.trigger_phase is None or event.trigger_phase == current_phase.name
            turn_match = event.trigger_turn is None or event.trigger_turn <= next_turn
            if not (phase_match and turn_match):
                continue
            runtime.record_world_event(
                event_id=event.event_id,
                actor_ids=event.affected_actor_ids or None,
                visibility=event.visibility,
            )
            pending.append(event.event_id)

        return {"injected_events": state.get("injected_events", []) + pending}

    async def prepare_actor_turn(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        actor_id = runtime.select_next_actor_round_robin()
        actor = runtime.actors[actor_id]
        return {
            "active_actor_id": actor_id,
            "active_actor_name": actor.display_name,
            "actor_context": runtime.actor_context(actor_id, max_turns=8),
            "drift_nudge": None,
            "policy_plan": {},
            "candidate_pool": [],
            "scored_candidates": [],
            "selected_candidate": {},
            "selected_candidate_text": "",
            "selected_meta": {},
            "selected_action_proposal": None,
        }

    def route_generation_mode(self, state: StakeholderGraphState) -> str:
        return "generate_naive_response" if state["base_condition"] == "naive" else "plan_policy"

    async def generate_naive_response(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        actor = runtime.actors[state["active_actor_id"]]
        phase = runtime.current_phase
        text = await actor.generate_response(
            turns=state["actor_context"]["turns"],
            phase_style=phase.style,
            actor_snapshot=state["actor_context"]["snapshot"] if state["ablation_config"].use_action_layer else None,
            phase_name=phase.name,
            phase_cues=phase.cues,
        )
        return {
            "selected_candidate": {"text": text},
            "selected_candidate_text": text,
            "selected_meta": {"mode": state["condition"]},
        }

    async def plan_policy(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        actor = runtime.actors[state["active_actor_id"]]
        controller = state["controllers"][state["active_actor_id"]]
        snapshot = state["actor_context"]["snapshot"]
        phase = runtime.current_phase
        drift_nudge = (
            controller.build_nudge(snapshot)
            if state["base_condition"] == "engine_controller"
            else None
        )
        actor.update_nudge(drift_nudge)
        policy_plan = await actor.generate_policy_plan(
            turns=state["actor_context"]["turns"],
            actor_snapshot=snapshot,
            phase_name=phase.name,
            phase_cues=phase.cues,
        )
        return {
            "drift_nudge": drift_nudge,
            "policy_plan": policy_plan,
        }

    async def generate_candidate_pool(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        actor = runtime.actors[state["active_actor_id"]]
        phase = runtime.current_phase
        pool = await actor.generate_candidate_pool_styles(
            turns=state["actor_context"]["turns"],
            phase_style=phase.style,
            style_slots=state["style_slots"],
            actor_snapshot=state["actor_context"]["snapshot"],
            phase_name=phase.name,
            phase_cues=phase.cues,
            policy_plan=state["policy_plan"],
            enable_trait_execution=(state["base_condition"] == "engine_controller"),
        )
        return {"candidate_pool": pool}

    def route_selection_mode(self, state: StakeholderGraphState) -> str:
        return "select_first_candidate" if state["base_condition"] == "engine" else "score_candidate_pool"

    async def select_first_candidate(self, state: StakeholderGraphState) -> dict[str, Any]:
        selected = state["candidate_pool"][0]
        return {
            "selected_candidate": selected,
            "selected_candidate_text": selected["text"],
            "selected_meta": {
                "mode": state["condition"],
                "policy_plan": state["policy_plan"],
                "slot": selected.get("slot"),
            },
        }

    async def score_candidate_pool(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        controller = state["controllers"][state["active_actor_id"]]
        phase = runtime.current_phase
        action_context = {
            "script": runtime.script,
            "valid_target_keys": list(runtime.script.world_state_schema),
            "allowed_action_types": list(runtime.script.allowed_action_types),
            "global_state": dict(runtime.ledger.latest_world_state().global_state),
            "turn_index": runtime.turn_index + 1,
            "use_action_aware_scoring": bool(state["ablation_config"].use_action_aware_scoring),
        }
        scored = controller.score_candidate_pool(
            candidate_pool=state["candidate_pool"],
            visible_turns=state["actor_context"]["turns"],
            actor_snapshot=state["actor_context"]["snapshot"],
            phase=phase,
            policy_plan=state["policy_plan"],
            action_context=action_context,
        )
        return {"scored_candidates": scored}

    async def select_scored_candidate(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        controller = state["controllers"][state["active_actor_id"]]
        phase = runtime.current_phase
        selection = controller.select_candidate(
            scored_candidates=state["scored_candidates"],
            phase=phase,
            turn_index=runtime.turn_index + 1,
            drift_nudge=state.get("drift_nudge"),
        )
        selected = selection["selected"]
        runtime.ledger.apply_state_delta(
            actor_id=state["active_actor_id"],
            last_inferred_traits=selected.get("inferred_traits"),
            rolling_trait_estimate=selected.get("inferred_traits"),
            drift_score=selected.get("persona_drift"),
            sycophancy_risk=selected.get("sycophancy_risk"),
            sycophancy_signals=selected.get("sycophancy_signals"),
            unfulfilled_persona_acts=selected.get("unfulfilled_persona_acts"),
            reflection=f"selected_score={selected.get('score', 0.0):.3f}",
        )
        return {
            "selected_candidate": selected,
            "selected_candidate_text": selected["text"],
            "selected_meta": {
                "mode": state["condition"],
                "policy_plan": state["policy_plan"],
                "audit": selection["audit"],
                "slot": selected.get("slot"),
                "action_hint": selected.get("action_hint"),
            },
        }

    async def commit_turn(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        actor_id = state["active_actor_id"]
        actor = runtime.actors[actor_id]
        turn = runtime.append_actor_turn(
            actor_id=actor_id,
            content=state["selected_candidate_text"],
            metadata=state["selected_meta"],
        )
        if state["base_condition"] != "engine_controller":
            inferred_traits = estimate_actor_traits_from_turns(
                runtime.visible_turns_for_actor(actor_id, max_turns=999),
                actor.display_name,
            )
            runtime.ledger.apply_state_delta(
                actor_id=actor_id,
                last_inferred_traits=inferred_traits,
                rolling_trait_estimate=inferred_traits,
                drift_score=persona_drift_mae(actor.actor_spec.personality_prior, inferred_traits),
            )
        return {"last_turn_index": turn.turn_index}

    async def compile_action_proposal(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        if not state["ablation_config"].use_action_layer:
            return {"selected_action_proposal": None}
        proposal = await compile_action_proposal(
            state["gen_client"],
            script=runtime.script,
            actor_id=state["active_actor_id"],
            actor_name_map=state["actor_name_map"],
            phase_name=runtime.current_phase.name,
            turn_index=state["last_turn_index"],
            selected_text=state["selected_candidate_text"],
            policy_plan=state.get("policy_plan", {}),
            actor_snapshot=state["actor_context"]["snapshot"],
        )
        return {
            "selected_action_proposal": proposal.to_dict() if proposal else None,
            "selected_meta": {
                **state.get("selected_meta", {}),
                "action_compilation": proposal.to_dict() if proposal else None,
            },
        }

    async def record_action_proposal(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        payload = state.get("selected_action_proposal")
        if not payload:
            return {"selected_action_proposal": None}
        from .action_layer import ActionProposal

        runtime.ledger.append_action_proposal(ActionProposal(**payload))
        return {"selected_action_proposal": payload}

    def route_phase_boundary(self, state: StakeholderGraphState) -> str:
        runtime = state["runtime"]
        phase_turn_index = state.get("phase_turn_index", 0) + 1
        boundary = phase_turn_index >= runtime.current_phase.max_turns
        if boundary and state["ablation_config"].use_action_layer:
            return "arbiter_phase_actions"
        return "advance_simulation"

    async def arbiter_phase_actions(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        approved, rejected = arbitrate_phase_actions(
            runtime.script,
            runtime.current_phase.name,
            runtime.ledger.phase_action_proposals(runtime.current_phase.name),
        )
        for proposal in approved:
            runtime.ledger.update_action_proposal_status(proposal.proposal_id, status="approved")
        for proposal in rejected:
            runtime.ledger.update_action_proposal_status(
                proposal.proposal_id,
                status="rejected",
                rejection_reason=proposal.rejection_reason,
            )
        return {
            "approved_phase_actions": [proposal.to_dict() for proposal in approved],
            "rejected_phase_actions": [proposal.to_dict() for proposal in rejected],
        }

    async def apply_state_transitions(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        from .action_layer import ActionProposal

        current_snapshot = runtime.ledger.latest_world_state()
        executed_rows = []
        for payload in state.get("approved_phase_actions", []):
            proposal = ActionProposal(**payload)
            executed, next_snapshot, rejection_reason = apply_transition_rule(
                runtime.script,
                proposal,
                current_snapshot,
            )
            if executed is None or next_snapshot is None:
                runtime.ledger.update_action_proposal_status(
                    proposal.proposal_id,
                    status="rejected",
                    rejection_reason=rejection_reason or "transition_failed",
                )
                continue
            runtime.ledger.apply_executed_action(executed, next_snapshot)
            current_snapshot = next_snapshot
            executed_rows.append(executed)
        return {
            "executed_phase_actions": [row.to_dict() for row in executed_rows],
        }

    async def summarize_state_feedback(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        if not state.get("executed_phase_actions"):
            return {"phase_feedback": {}}
        from .action_layer import ExecutedAction

        executed_rows = [ExecutedAction(**payload) for payload in state["executed_phase_actions"]]
        runtime.ledger.record_phase_feedback(
            runtime.current_phase.name,
            executed_rows,
            runtime.ledger.latest_world_state(),
        )
        return {
            "phase_feedback": {
                actor_id: runtime.ledger.latest_phase_feedback(actor_id)
                for actor_id in runtime.script.actor_ids
            }
        }

    async def advance_simulation(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        phase_turn_index = state.get("phase_turn_index", 0) + 1
        current_phase = runtime.current_phase
        simulation_complete = False
        phase_boundary = phase_turn_index >= current_phase.max_turns

        if phase_boundary:
            if runtime.phase_index >= len(runtime.script.phases) - 1:
                simulation_complete = True
            else:
                runtime.advance_phase()
                phase_turn_index = 0

        return {
            "phase_turn_index": phase_turn_index,
            "simulation_complete": simulation_complete,
            "phase_boundary_reached": phase_boundary,
        }

    async def finalize_run(self, state: StakeholderGraphState) -> dict[str, Any]:
        runtime = state["runtime"]
        controllers = state["controllers"]
        selection_audits = [
            audit
            for controller in controllers.values()
            for audit in controller.selection_audits
        ]
        result = {
            "condition": state["condition"],
            "simulation_id": runtime.script.simulation_id,
            "runtime_summary": runtime.to_runtime_summary(),
            "metrics": compute_runtime_metrics(runtime),
            "selection_audits": selection_audits,
        }
        return {"result": result}


def build_stakeholder_simulation_graph():
    """Compile the stakeholder simulation runtime graph."""
    nodes = StakeholderSimulationNodes()
    graph = StateGraph(StakeholderGraphState)

    graph.add_node("bootstrap_runtime", nodes.bootstrap_runtime)
    graph.add_node("inject_world_events", nodes.inject_world_events)
    graph.add_node("prepare_actor_turn", nodes.prepare_actor_turn)
    graph.add_node("generate_naive_response", nodes.generate_naive_response)
    graph.add_node("plan_policy", nodes.plan_policy)
    graph.add_node("generate_candidate_pool", nodes.generate_candidate_pool)
    graph.add_node("select_first_candidate", nodes.select_first_candidate)
    graph.add_node("score_candidate_pool", nodes.score_candidate_pool)
    graph.add_node("select_scored_candidate", nodes.select_scored_candidate)
    graph.add_node("commit_turn", nodes.commit_turn)
    graph.add_node("compile_action_proposal", nodes.compile_action_proposal)
    graph.add_node("record_action_proposal", nodes.record_action_proposal)
    graph.add_node("arbiter_phase_actions", nodes.arbiter_phase_actions)
    graph.add_node("apply_state_transitions", nodes.apply_state_transitions)
    graph.add_node("summarize_state_feedback", nodes.summarize_state_feedback)
    graph.add_node("advance_simulation", nodes.advance_simulation)
    graph.add_node("finalize_run", nodes.finalize_run)

    graph.add_edge(START, "bootstrap_runtime")
    graph.add_conditional_edges(
        "bootstrap_runtime",
        nodes.route_turn_loop,
        {
            "inject_world_events": "inject_world_events",
            "finalize_run": "finalize_run",
        },
    )
    graph.add_edge("inject_world_events", "prepare_actor_turn")
    graph.add_conditional_edges(
        "prepare_actor_turn",
        nodes.route_generation_mode,
        {
            "generate_naive_response": "generate_naive_response",
            "plan_policy": "plan_policy",
        },
    )
    graph.add_edge("generate_naive_response", "commit_turn")
    graph.add_edge("plan_policy", "generate_candidate_pool")
    graph.add_conditional_edges(
        "generate_candidate_pool",
        nodes.route_selection_mode,
        {
            "select_first_candidate": "select_first_candidate",
            "score_candidate_pool": "score_candidate_pool",
        },
    )
    graph.add_edge("select_first_candidate", "commit_turn")
    graph.add_edge("score_candidate_pool", "select_scored_candidate")
    graph.add_edge("select_scored_candidate", "commit_turn")
    graph.add_edge("commit_turn", "compile_action_proposal")
    graph.add_edge("compile_action_proposal", "record_action_proposal")
    graph.add_conditional_edges(
        "record_action_proposal",
        nodes.route_phase_boundary,
        {
            "arbiter_phase_actions": "arbiter_phase_actions",
            "advance_simulation": "advance_simulation",
        },
    )
    graph.add_edge("arbiter_phase_actions", "apply_state_transitions")
    graph.add_edge("apply_state_transitions", "summarize_state_feedback")
    graph.add_edge("summarize_state_feedback", "advance_simulation")
    graph.add_conditional_edges(
        "advance_simulation",
        nodes.route_turn_loop,
        {
            "inject_world_events": "inject_world_events",
            "finalize_run": "finalize_run",
        },
    )
    graph.add_edge("finalize_run", END)

    return graph.compile()
