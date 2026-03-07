import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine import PersonaStateController, SimulationBenchmarkRunner, load_mvp_policy_scripts
from simulation_engine.ablation import SimulationAblationConfig, resolve_benchmark_condition


class _DummyClient:
    pass


def test_persona_state_controller_prefers_stakeholder_consistent_candidate():
    script = load_mvp_policy_scripts()[0]
    actor = script.get_actor("actor_1")
    name_map = {item.actor_id: item.display_name for item in script.stakeholders}
    controller = PersonaStateController(actor, actor_name_map=name_map)

    visible_turns = [
        type("Turn", (), {"turn_number": 1, "speaker_name": "Mr. Park", "content": "I am worried the rollout will hurt staffing and neighborhood demand."})(),
    ]
    actor_snapshot = {
        "actor_state": {"last_inferred_traits": {"O": 0.62, "C": 0.48, "E": 0.41, "A": 0.57, "N": 0.61}},
        "open_commitments": [],
        "relationships": [
            {"target_actor_id": "actor_2", "sentiment": "neutral", "trust": 0.5, "last_turn": 0}
        ],
    }
    phase = script.phases[1]
    candidate_pool = [
        {
            "slot": "generic",
            "text": "We should think carefully and get more information before deciding anything.",
        },
        {
            "slot": "targeted",
            "text": (
                "Mr. Park, good point. If the paperwork delays income stability, I will map a simpler timeline "
                "so the rollout does not hurt staffing or neighborhood demand."
            ),
        },
    ]

    scored = controller.score_candidate_pool(
        candidate_pool=candidate_pool,
        visible_turns=visible_turns,
        actor_snapshot=actor_snapshot,
        phase=phase,
        policy_plan={"goal_mode": "coordinate", "stance": "synthesize"},
    )

    assert scored[0]["slot"] == "targeted"
    assert scored[0]["score"] > scored[1]["score"]


def test_persona_state_controller_prefers_low_openness_signal_for_low_o_actor():
    script = load_mvp_policy_scripts()[0]
    actor = script.get_actor("actor_2")
    name_map = {item.actor_id: item.display_name for item in script.stakeholders}
    controller = PersonaStateController(actor, actor_name_map=name_map)

    visible_turns = [
        type("Turn", (), {"turn_number": 1, "speaker_name": "Jiho", "content": "What if we redesign the whole program around a new neighborhood model?"})(),
    ]
    actor_snapshot = {
        "actor_state": {"last_inferred_traits": actor.personality_prior},
        "open_commitments": [],
        "relationships": [{"target_actor_id": "actor_1", "sentiment": "neutral", "trust": 0.5, "last_turn": 0}],
    }
    phase = script.phases[1]
    candidate_pool = [
        {
            "slot": "challenger",
            "text": "What if we create a third option and reframe the entire rollout around an experimental neighborhood pilot?",
        },
        {
            "slot": "planner",
            "text": "Before we expand, I want evidence on staffing and demand. Start small, keep the scope narrow, and use a proven option first.",
        },
    ]

    scored = controller.score_candidate_pool(
        candidate_pool=candidate_pool,
        visible_turns=visible_turns,
        actor_snapshot=actor_snapshot,
        phase=phase,
        policy_plan={"goal_mode": "coordinate", "stance": "probe"},
    )

    assert scored[0]["slot"] == "planner"
    assert scored[0]["trait_target_alignment"] > scored[1]["trait_target_alignment"]


def test_persona_state_controller_uses_trait_aware_tie_break():
    script = load_mvp_policy_scripts()[0]
    actor = script.get_actor("actor_2")
    controller = PersonaStateController(actor)
    phase = script.phases[1]
    scored_candidates = [
        {
            "slot": "challenger",
            "text": "Option A",
            "score": 0.81,
            "persona_drift": 0.15,
            "identity_consistency": 0.72,
            "relationship_consistency": 0.5,
            "trait_target_alignment": 0.73,
            "genericity_penalty": 0.0,
            "redundancy_penalty": 0.0,
            "opportunity_scores": {"O": 0.62, "C": 0.41},
        },
        {
            "slot": "planner",
            "text": "Option B",
            "score": 0.797,
            "persona_drift": 0.14,
            "identity_consistency": 0.72,
            "relationship_consistency": 0.5,
            "trait_target_alignment": 0.73,
            "genericity_penalty": 0.0,
            "redundancy_penalty": 0.0,
            "opportunity_scores": {"O": 0.62, "C": 0.41},
        },
    ]

    selection = controller.select_candidate(scored_candidates, phase=phase, turn_index=2)

    assert selection["selected"]["slot"] == "planner"
    assert selection["audit"]["tie_detected"] is True
    assert selection["audit"]["tie_break_axis"] == "O_low"


def test_persona_state_controller_can_disable_tie_routing():
    script = load_mvp_policy_scripts()[0]
    actor = script.get_actor("actor_2")
    controller = PersonaStateController(
        actor,
        ablation_config=SimulationAblationConfig(use_tie_routing=False),
    )
    phase = script.phases[1]
    scored_candidates = [
        {
            "slot": "challenger",
            "text": "Option A",
            "score": 0.81,
            "persona_drift": 0.15,
            "identity_consistency": 0.72,
            "relationship_consistency": 0.5,
            "trait_target_alignment": 0.73,
            "social_trait_alignment": 0.71,
            "genericity_penalty": 0.0,
            "redundancy_penalty": 0.0,
            "opportunity_scores": {"O": 0.62, "C": 0.41},
        },
        {
            "slot": "planner",
            "text": "Option B",
            "score": 0.797,
            "persona_drift": 0.14,
            "identity_consistency": 0.72,
            "relationship_consistency": 0.5,
            "trait_target_alignment": 0.73,
            "social_trait_alignment": 0.71,
            "genericity_penalty": 0.0,
            "redundancy_penalty": 0.0,
            "opportunity_scores": {"O": 0.62, "C": 0.41},
        },
    ]

    selection = controller.select_candidate(scored_candidates, phase=phase, turn_index=2)

    assert selection["selected"]["slot"] == "challenger"
    assert selection["audit"]["tie_detected"] is False


def test_resolve_benchmark_condition_maps_ablation_modes():
    base, config = resolve_benchmark_condition("engine_controller_no_extended_ledger")

    assert base == "engine_controller"
    assert config.use_extended_ledger_context is False
    assert config.use_banded_target_matching is True


def test_benchmark_runner_executes_with_monkeypatched_generation(monkeypatch):
    async def _fake_generate_response(
        self,
        turns,
        phase_style,
        actor_snapshot=None,
        constraint_suffix=None,
        style_directive=None,
        policy_plan=None,
        phase_name=None,
        phase_cues=None,
        target_traits=None,
        enable_trait_execution=False,
    ):
        return f"{self.display_name} thinks the policy needs careful tradeoff review."

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
            {"slot": "generic", "text": "We should think carefully and get more information."},
            {
                "slot": "targeted",
                "text": (
                    f"{self.display_name} says we should assign an owner and timeline so the policy rollout "
                    "addresses the stakeholder tradeoffs."
                ),
            },
        ]

    monkeypatch.setattr("simulation_engine.actor.StakeholderActor.generate_response", _fake_generate_response)
    monkeypatch.setattr("simulation_engine.actor.StakeholderActor.generate_policy_plan", _fake_generate_policy_plan)
    monkeypatch.setattr(
        "simulation_engine.actor.StakeholderActor.generate_candidate_pool_styles",
        _fake_generate_candidate_pool_styles,
    )

    runner = SimulationBenchmarkRunner(gen_client=_DummyClient())
    script = load_mvp_policy_scripts()[0]

    engine_result = asyncio.run(runner.run_single(script, "engine"))
    controlled_result = asyncio.run(runner.run_single(script, "engine_controller"))
    ablated_result = asyncio.run(runner.run_single(script, "engine_controller_no_tie_routing"))

    assert engine_result.condition == "engine"
    assert controlled_result.condition == "engine_controller"
    assert ablated_result.condition == "engine_controller_no_tie_routing"
    assert controlled_result.selection_audits
    assert ablated_result.selection_audits
    assert "persona_drift_mae" in controlled_result.metrics.to_dict()
