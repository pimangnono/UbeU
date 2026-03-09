import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine.action_layer import ActionProposal
from simulation_engine.metrics import (
    action_family_convergence_rate,
    fallback_type_rates,
    fallback_utterance_rate,
    negotiation_uniqueness_rate,
    relationship_inconsistency_rate,
    relationship_overshoot_rate,
    relationship_shift_rate,
    role_action_diversity_score,
)
from simulation_engine.runtime import StakeholderSimulationRuntime


class _DummyClient:
    pass


def _sample_script_dict() -> dict:
    return {
        "simulation_id": "relationship_metric_001",
        "title": "Relationship Metric",
        "objective": "Check relationship volatility",
        "brief": "A small policy discussion.",
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Jiho",
                "role": "Worker",
                "identity_core": {"age_band": "20s"},
                "personality_prior": {"O": 0.55, "C": 0.48, "E": 0.42, "A": 0.57, "N": 0.60},
                "incentives": ["income stability"],
                "concerns": ["timing"],
            },
            {
                "actor_id": "actor_2",
                "display_name": "Mr. Park",
                "role": "Merchant",
                "identity_core": {"age_band": "50s"},
                "personality_prior": {"O": 0.34, "C": 0.72, "E": 0.39, "A": 0.44, "N": 0.46},
                "incentives": ["predictable demand"],
                "concerns": ["staffing"],
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Discuss impact", "style": "neutral", "max_turns": 4},
        ],
    }


def test_relationship_inconsistency_rate_detects_sentiment_swings():
    runtime = StakeholderSimulationRuntime.from_dict(
        _sample_script_dict(),
        gen_client=_DummyClient(),
    )

    runtime.append_actor_turn(
        actor_id="actor_1",
        content="Mr. Park, good point. I see your point and appreciate the concern.",
    )
    runtime.append_actor_turn(
        actor_id="actor_1",
        content="Mr. Park, I see your point, but I still need evidence before we expand.",
    )
    runtime.append_actor_turn(
        actor_id="actor_1",
        content="Mr. Park, I disagree. That won't work for workers like me.",
    )

    assert relationship_inconsistency_rate(runtime) > 0.0
    assert relationship_shift_rate(runtime) > 0.0
    assert relationship_overshoot_rate(runtime) > 0.0


def test_action_family_metrics_detect_phase_convergence():
    runtime = StakeholderSimulationRuntime.from_dict(
        {
            **_sample_script_dict(),
            "phases": [
                {"name": "NEGOTIATION", "goal": "Choose a path", "style": "consensus", "max_turns": 3},
            ],
            "allowed_action_types": ["assign_owner", "request_evidence", "publish_update", "pilot"],
            "transition_rules": {
                "NEGOTIATION": {
                    "assign_owner": {"global_deltas": {"execution_confidence": 0.08}},
                    "request_evidence": {"global_deltas": {"uncertainty": -0.08}},
                    "publish_update": {"global_deltas": {"alignment": 0.08}},
                    "pilot": {"global_deltas": {"risk": -0.08}},
                }
            },
        },
        gen_client=_DummyClient(),
    )
    runtime.ledger.append_action_proposal(
        ActionProposal(
            proposal_id="p1",
            actor_id="actor_1",
            phase_name="NEGOTIATION",
            turn_index=1,
            action_type="pilot",
            target_key="risk",
            action_bearing=True,
            status="proposed",
        )
    )
    runtime.ledger.append_action_proposal(
        ActionProposal(
            proposal_id="p2",
            actor_id="actor_2",
            phase_name="NEGOTIATION",
            turn_index=2,
            action_type="pilot",
            target_key="risk",
            action_bearing=True,
            status="proposed",
        )
    )
    runtime.ledger.append_action_proposal(
        ActionProposal(
            proposal_id="p3",
            actor_id="actor_1",
            phase_name="NEGOTIATION",
            turn_index=1,
            action_type="pilot",
            target_key="risk",
            action_bearing=True,
            status="proposed",
        )
    )
    for idx, actor_id in enumerate(["actor_1", "actor_2", "actor_1"], start=1):
        runtime.ledger.upsert_action_audit(
            f"t{idx}",
            {
                "trace_id": f"t{idx}",
                "actor_id": actor_id,
                "phase_name": "NEGOTIATION",
                "turn_index": idx,
                "compiled_proposal": {"action_type": "pilot", "target_key": "risk"},
            },
        )

    assert action_family_convergence_rate(runtime) == 1.0
    assert role_action_diversity_score(runtime) == round(1 / 3, 4)
    assert negotiation_uniqueness_rate(runtime) == round(1 / 3, 4)


def test_fallback_utterance_rate_detects_generation_fallback():
    runtime = StakeholderSimulationRuntime.from_dict(
        _sample_script_dict(),
        gen_client=_DummyClient(),
    )
    runtime.append_actor_turn(
        actor_id="actor_1",
        content="I think we should consider all the options before deciding.",
    )
    runtime.append_actor_turn(
        actor_id="actor_2",
        content="Let's assign an owner and move this forward.",
    )

    assert fallback_utterance_rate(runtime) == 0.5


def test_fallback_type_rates_reads_generation_metadata():
    runtime = StakeholderSimulationRuntime.from_dict(
        _sample_script_dict(),
        gen_client=_DummyClient(),
    )
    runtime.append_actor_turn(
        actor_id="actor_1",
        content="I think we should consider all the options before deciding.",
        metadata={"generation_meta": {"used_fallback": True, "fallback_type": "timeout_fallback"}},
    )
    runtime.append_actor_turn(
        actor_id="actor_2",
        content="Let's assign an owner and move this forward.",
    )

    assert fallback_utterance_rate(runtime) == 0.5
    assert fallback_type_rates(runtime) == {"timeout_fallback": 0.5}
