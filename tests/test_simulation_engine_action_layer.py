import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine import (
    ActionProposal,
    StakeholderSimulationGraphRunner,
    apply_transition_rule,
    arbitrate_phase_actions,
    compile_action_proposal,
    load_mvp_policy_scripts,
)


class _DummyClient:
    pass


def test_compile_action_proposal_uses_heuristic_fallback():
    script = load_mvp_policy_scripts()[3]  # new_product_launch
    proposal = asyncio.run(
        compile_action_proposal(
            _DummyClient(),
            script=script,
            actor_id="actor_1",
            actor_name_map=script.actor_display_name_map,
            phase_name="NEGOTIATION",
            turn_index=4,
            selected_text="I will assign an owner and narrow scope to improve launch readiness before we ship.",
            policy_plan={"action_intent": "assign_owner", "target_state_key": "launch_readiness"},
            actor_snapshot={"actor_state": {"goals": ["credible launch"]}},
        )
    )

    assert proposal is not None
    assert proposal.status == "proposed"
    assert proposal.action_type == "assign_owner"
    assert proposal.target_key == "launch_readiness"
    assert proposal.compiler_source == "heuristic"


def test_arbitrate_phase_actions_keeps_latest_same_family_and_rejects_conflict():
    script = load_mvp_policy_scripts()[4]  # PMI
    first = ActionProposal(
        proposal_id="p1",
        actor_id="actor_1",
        phase_name="NEGOTIATION",
        turn_index=5,
        action_type="assign_owner",
        target_key="integration_clarity",
        confidence=0.55,
        evidence_text="Assign an owner.",
        action_bearing=True,
    )
    second = ActionProposal(
        proposal_id="p2",
        actor_id="actor_1",
        phase_name="NEGOTIATION",
        turn_index=6,
        action_type="assign_owner",
        target_key="execution_confidence",
        confidence=0.65,
        evidence_text="Assign a clearer owner.",
        action_bearing=True,
    )
    third = ActionProposal(
        proposal_id="p3",
        actor_id="actor_2",
        phase_name="NEGOTIATION",
        turn_index=7,
        action_type="preserve_autonomy",
        target_key="execution_confidence",
        confidence=0.72,
        evidence_text="Preserve autonomy instead.",
        action_bearing=True,
    )

    approved, rejected = arbitrate_phase_actions(script, "NEGOTIATION", [first, second, third])

    assert [row.proposal_id for row in approved] == ["p3"]
    assert {row.proposal_id for row in rejected} == {"p1", "p2"}
    assert any(row.rejection_reason == "superseded_by_later_same_family" for row in rejected)
    assert any(row.rejection_reason == "conflict" for row in rejected)


def test_apply_transition_rule_updates_world_state():
    script = load_mvp_policy_scripts()[2]  # commuting_support_policy
    snapshot = script.initial_world_state
    runtime_runner = StakeholderSimulationGraphRunner(gen_client=_DummyClient(), style_slots=["planner"])
    runtime = runtime_runner.graph  # only to avoid import lint; graph not used
    _ = runtime

    from simulation_engine.action_layer import WorldStateSnapshot, default_local_state

    pre_state = WorldStateSnapshot(
        phase_name="NEGOTIATION",
        turn_index=6,
        global_state=dict(snapshot),
        local_state_by_actor=default_local_state(script.actor_ids),
        executed_action_ids=[],
    )
    proposal = ActionProposal(
        proposal_id="p4",
        actor_id="actor_3",
        phase_name="NEGOTIATION",
        turn_index=6,
        action_type="assign_owner",
        target_key="execution_confidence",
        owner_actor_id="actor_3",
        confidence=0.8,
        evidence_text="Assign an owner and timeline.",
        action_bearing=True,
    )

    executed, post_state, rejection_reason = apply_transition_rule(script, proposal, pre_state)

    assert rejection_reason is None
    assert executed is not None
    assert post_state is not None
    assert post_state.global_state["execution_confidence"] > pre_state.global_state["execution_confidence"]
    assert post_state.global_state["alignment"] > pre_state.global_state["alignment"]


def test_graph_runner_executes_engine_action_v0_path(monkeypatch):
    async def _fake_generate_policy_plan(
        self,
        turns,
        actor_snapshot=None,
        phase_name=None,
        phase_cues=None,
        target_traits=None,
    ):
        return {
            "stance": "synthesize",
            "goal_mode": "coordinate",
            "planning_depth": "owner_deadline",
            "action_intent": "assign_owner",
            "target_state_key": "execution_confidence",
            "commitment_strength": "high",
            "expected_state_effect": "increase",
        }

    async def _fake_generate_candidate_pool_styles(
        self,
        turns,
        phase_style,
        style_slots,
        actor_snapshot=None,
        phase_name=None,
        phase_cues=None,
        target_traits=None,
        constraint_suffix=None,
        policy_plan=None,
        enable_trait_execution=False,
    ):
        return [
            {"slot": "generic", "text": "We should think carefully."},
            {
                "slot": "planner",
                "text": f"{self.display_name} will assign an owner and publish an update to improve execution confidence and alignment.",
            },
        ]

    monkeypatch.setattr("simulation_engine.actor.StakeholderActor.generate_policy_plan", _fake_generate_policy_plan)
    monkeypatch.setattr(
        "simulation_engine.actor.StakeholderActor.generate_candidate_pool_styles",
        _fake_generate_candidate_pool_styles,
    )

    runner = StakeholderSimulationGraphRunner(gen_client=_DummyClient(), style_slots=["planner", "skeptic"])
    script = load_mvp_policy_scripts()[0]

    result = asyncio.run(runner.run(script, "engine_action_v0"))

    assert result["condition"] == "engine_action_v0"
    assert result["runtime_summary"]["executed_action_count"] > 0
    assert result["metrics"].structured_action_validity_rate > 0.0
    assert result["metrics"].state_transition_coherence > 0.0
