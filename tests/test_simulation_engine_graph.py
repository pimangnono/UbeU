import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine import StakeholderSimulationGraphRunner, load_mvp_policy_scripts


class _DummyClient:
    pass


def test_graph_runner_executes_engine_controller_path(monkeypatch):
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
    ):
        return [
            {"slot": "generic", "text": "We should think carefully and collect more information."},
            {
                "slot": "targeted",
                "text": (
                    f"{self.display_name} says we should assign an owner and timeline so the rollout "
                    "addresses stakeholder tradeoffs without losing trust."
                ),
            },
        ]

    monkeypatch.setattr("simulation_engine.actor.StakeholderActor.generate_policy_plan", _fake_generate_policy_plan)
    monkeypatch.setattr(
        "simulation_engine.actor.StakeholderActor.generate_candidate_pool_styles",
        _fake_generate_candidate_pool_styles,
    )

    runner = StakeholderSimulationGraphRunner(gen_client=_DummyClient(), style_slots=["planner", "skeptic"])
    script = load_mvp_policy_scripts()[0]

    result = asyncio.run(runner.run(script, "engine_controller"))

    assert result["condition"] == "engine_controller"
    assert result["runtime_summary"]["turn_count"] == sum(phase.max_turns for phase in script.phases)
    assert result["selection_audits"]
    assert result["metrics"].persona_drift_mae >= 0.0


def test_graph_runner_executes_ablation_condition(monkeypatch):
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
    ):
        return [
            {"slot": "challenger", "text": "We should reframe the policy around a new district pilot."},
            {"slot": "planner", "text": "Assign an owner and a timeline before expanding the rollout."},
        ]

    monkeypatch.setattr("simulation_engine.actor.StakeholderActor.generate_policy_plan", _fake_generate_policy_plan)
    monkeypatch.setattr(
        "simulation_engine.actor.StakeholderActor.generate_candidate_pool_styles",
        _fake_generate_candidate_pool_styles,
    )

    runner = StakeholderSimulationGraphRunner(gen_client=_DummyClient(), style_slots=["challenger", "planner"])
    script = load_mvp_policy_scripts()[0]

    result = asyncio.run(runner.run(script, "engine_controller_no_tie_routing"))

    assert result["condition"] == "engine_controller_no_tie_routing"
    assert result["selection_audits"]


def test_graph_runner_executes_naive_path(monkeypatch):
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
        return f"{self.display_name} thinks the policy has tradeoffs and needs careful rollout."

    monkeypatch.setattr("simulation_engine.actor.StakeholderActor.generate_response", _fake_generate_response)

    runner = StakeholderSimulationGraphRunner(gen_client=_DummyClient(), style_slots=["planner"])
    script = load_mvp_policy_scripts()[0]

    result = asyncio.run(runner.run(script, "naive"))

    assert result["condition"] == "naive"
    assert result["runtime_summary"]["turn_count"] == sum(phase.max_turns for phase in script.phases)
    assert result["selection_audits"] == []
