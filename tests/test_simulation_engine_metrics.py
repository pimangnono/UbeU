import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine.metrics import relationship_inconsistency_rate
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
