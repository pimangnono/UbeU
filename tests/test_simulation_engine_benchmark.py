import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine import PersonaStateController, SimulationBenchmarkRunner, load_mvp_policy_scripts
from simulation_engine.metrics import BenchmarkRunMetrics
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


def test_resolve_benchmark_condition_maps_action_modes():
    base, config = resolve_benchmark_condition("engine_action_v0")

    assert base == "engine_controller"
    assert config.use_action_layer is True
    assert config.use_action_aware_scoring is True


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
        **kwargs,
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
        **kwargs,
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
    metrics_payload = controlled_result.metrics.to_dict()
    assert "persona_drift_mae" in metrics_payload
    assert "fallback_utterance_rate" in metrics_payload
    assert "fallback_type_rates" in metrics_payload
    assert metrics_payload["actor_labels"]["actor_1"] == "Primary affected youth worker"


def test_benchmark_runner_resumes_from_checkpoint(monkeypatch, tmp_path):
    script = load_mvp_policy_scripts()[0]
    conditions = ["naive_action_baseline"]
    style_slots = ["integrator", "planner", "challenger", "skeptic"]
    checkpoint_dir = tmp_path / "checkpoint"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    prior_metrics = BenchmarkRunMetrics(
        persona_drift_mae=0.11,
        relationship_inconsistency=0.0,
        commitment_contradiction_rate=0.0,
        envelope_violations=1,
        per_trait_error_mean={"O": 0.1, "C": 0.1, "E": 0.1, "A": 0.1, "N": 0.1},
        actor_labels={"actor_1": "A"},
        actor_display_names={"actor_1": "A"},
        actor_trait_estimates={"actor_1": {"O": 0.1, "C": 0.1, "E": 0.1, "A": 0.1, "N": 0.1}},
        actor_trait_errors={"actor_1": {"O": 0.0, "C": 0.0, "E": 0.0, "A": 0.0, "N": 0.0}},
    )
    prior_run = {
        "condition": "naive_action_baseline",
        "simulation_id": script.simulation_id,
        "runtime_summary": {"simulation_id": script.simulation_id, "turn_count": 11},
        "metrics": prior_metrics.to_dict(),
        "selection_audits": [],
    }
    (checkpoint_dir / "benchmark_runs.json").write_text(
        json.dumps(
            {
                "config": {
                    "conditions": conditions,
                    "repetitions": 2,
                    "script_ids": [script.simulation_id],
                    "style_slots": style_slots,
                },
                "runs": [prior_run],
            }
        )
    )

    call_counter = {"count": 0}

    async def _fake_run_single(_script, condition):
        call_counter["count"] += 1
        assert condition == "naive_action_baseline"
        return type(
            "Result",
            (),
            {
                "to_dict": lambda self: prior_run,
                "condition": condition,
                "simulation_id": _script.simulation_id,
                "runtime_summary": {"simulation_id": _script.simulation_id, "turn_count": 11},
                "metrics": prior_metrics,
                "selection_audits": [],
            },
        )()

    monkeypatch.setattr("simulation_engine.benchmark.load_mvp_policy_scripts", lambda: [script])
    runner = SimulationBenchmarkRunner(gen_client=_DummyClient(), style_slots=style_slots)
    monkeypatch.setattr(runner, "run_single", _fake_run_single)

    results = asyncio.run(
        runner.run_suite(
            conditions=conditions,
            repetitions=2,
            script_ids=[script.simulation_id],
            checkpoint_dir=str(checkpoint_dir),
        )
    )

    assert call_counter["count"] == 1
    assert len(results["runs"]) == 2
    assert "clean_run_count" in results["aggregate"]["naive_action_baseline"]
    assert "contaminated_run_count" in results["aggregate"]["naive_action_baseline"]
