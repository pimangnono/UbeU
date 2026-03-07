import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine import (
    SimulationAblationConfig,
    SimulationScript,
    SimulationStateLedger,
    StakeholderActor,
    StakeholderSimulationRuntime,
)


class _DummyClient:
    pass


def _sample_script_dict() -> dict:
    return {
        "simulation_id": "policy_youth_001",
        "title": "Youth Policy A Simulation",
        "objective": "Measure direct and indirect stakeholder reactions",
        "brief": "Policy A changes youth employment support eligibility and administrative burden.",
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Jiho",
                "role": "Primary affected youth worker",
                "identity_core": {
                    "age_band": "20s",
                    "occupation": "contract designer",
                },
                "personality_prior": {"O": 0.62, "C": 0.48, "E": 0.41, "A": 0.57, "N": 0.61},
                "incentives": ["income stability", "career mobility"],
                "concerns": ["short-term cash flow", "administrative friction"],
                "communication_style": {"tone": "pragmatic", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_2",
                "display_name": "Mr. Park",
                "role": "Adjacent local merchant",
                "identity_core": {"age_band": "50s", "occupation": "restaurant owner"},
                "personality_prior": {"O": 0.34, "C": 0.72, "E": 0.39, "A": 0.44, "N": 0.46},
                "incentives": ["customer traffic"],
                "concerns": ["staffing stability"],
            },
            {
                "actor_id": "actor_3",
                "display_name": "Officer Kim",
                "role": "Program administrator",
                "identity_core": {"age_band": "40s", "occupation": "district operations lead"},
                "personality_prior": {"O": 0.45, "C": 0.78, "E": 0.52, "A": 0.49, "N": 0.38},
                "incentives": ["smooth implementation"],
                "concerns": ["compliance risk"],
            },
        ],
        "phases": [
            {
                "name": "OPENING",
                "goal": "Surface direct first-order effects",
                "style": "neutral",
                "max_turns": 3,
            },
            {
                "name": "TENSION",
                "goal": "Reveal conflicts and spillovers",
                "style": "disagreement",
                "max_turns": 4,
            },
        ],
        "world_events": [
            {
                "event_id": "evt_budget_cap",
                "title": "Budget cap rumor",
                "description": "A rumored cap reduces expected policy funding.",
                "trigger_phase": "TENSION",
                "visibility": "public",
            }
        ],
    }


def test_simulation_script_builds_default_personality_envelopes():
    script = SimulationScript.from_dict(_sample_script_dict())

    assert script.simulation_id == "policy_youth_001"
    assert len(script.stakeholders) == 3
    assert len(script.phases) == 2
    assert script.get_actor("actor_1").personality_envelope["O"] == (0.44, 0.8)


def test_state_ledger_tracks_commitments_and_relationships():
    script = SimulationScript.from_dict(_sample_script_dict())
    ledger = SimulationStateLedger(script)

    turn = ledger.append_turn(
        actor_id="actor_1",
        content="Mr. Park, good point. I will share a clearer timeline so we can plan around the policy rollout.",
        phase_name="OPENING",
    )

    assert turn.turn_index == 1
    assert ledger.actor_states["actor_1"].open_commitments
    relationship = ledger.relationships[("actor_1", "actor_2")]
    assert relationship.sentiment == "positive"
    assert relationship.trust > 0.5


def test_stakeholder_actor_builds_stateful_prompt_context():
    script = SimulationScript.from_dict(_sample_script_dict())
    actor = StakeholderActor(
        client=_DummyClient(),
        actor_spec=script.get_actor("actor_1"),
        world_brief=script.brief,
    )
    snapshot = {
        "actor_state": {
            "stress": 0.3,
            "beliefs": {"policy_access": 0.8},
            "rolling_trait_estimate": {"O": 0.58, "C": 0.46},
            "drift_score": 0.18,
            "trait_drift_map": {"O": 0.04, "E": 0.12},
            "sycophancy_risk": 0.12,
            "unfulfilled_persona_acts": {"O": ["alternative_generation"]},
            "goals": ["income stability"],
        },
        "open_commitments": [{"content": "share a clearer timeline"}],
        "relationships": [{"target_actor_id": "actor_2", "sentiment": "positive", "trust": 0.62}],
        "recent_event_exposures": [{"event_id": "evt_budget_cap"}],
    }

    state_context = actor.build_state_context(snapshot)

    assert "Primary affected youth worker" in actor.system_prompt
    assert "income stability" in actor.system_prompt
    assert "Stable Expression Prior" in actor.system_prompt
    assert "Extraversion:" in actor.system_prompt
    assert "stress=0.30" in state_context
    assert "drift_score=0.18" in state_context
    assert "trait_drift_map=O=0.04, E=0.12" in state_context
    assert "unfulfilled_persona_acts=O:alternative_generation" in state_context
    assert "evt_budget_cap" in state_context


def test_runtime_scaffold_bootstraps_actor_symmetric_context():
    runtime = StakeholderSimulationRuntime.from_dict(
        _sample_script_dict(),
        gen_client=_DummyClient(),
    )

    next_actor_id = runtime.select_next_actor_round_robin()
    runtime.append_actor_turn(
        actor_id=next_actor_id,
        content="I think the policy could help, but we need clarity on timing.",
    )
    context = runtime.actor_context("actor_2")

    assert runtime.bootstrap_state()["phase_name"] == "OPENING"
    assert next_actor_id == "actor_1"
    assert context["phase"]["name"] == "OPENING"
    assert context["turns"][0].speaker_name == "Jiho"


def test_stakeholder_actor_omits_extended_ledger_context_when_ablated():
    script = SimulationScript.from_dict(_sample_script_dict())
    actor = StakeholderActor(
        client=_DummyClient(),
        actor_spec=script.get_actor("actor_1"),
        world_brief=script.brief,
        ablation_config=SimulationAblationConfig(use_extended_ledger_context=False),
    )
    snapshot = {
        "actor_state": {
            "stress": 0.2,
            "beliefs": {"policy_access": 0.8},
            "rolling_trait_estimate": {"O": 0.58, "C": 0.46},
            "drift_score": 0.18,
            "trait_drift_map": {"O": 0.04, "E": 0.12},
            "sycophancy_risk": 0.12,
            "unfulfilled_persona_acts": {"O": ["alternative_generation"]},
            "goals": ["income stability"],
        },
        "open_commitments": [{"content": "share a clearer timeline"}],
        "relationships": [{"target_actor_id": "actor_2", "sentiment": "positive", "trust": 0.62}],
        "recent_event_exposures": [{"event_id": "evt_budget_cap"}],
    }

    state_context = actor.build_state_context(snapshot)

    assert "open_commitments=share a clearer timeline" in state_context
    assert "relationships=actor_2:positive trust=0.62" in state_context
    assert "recent_event_exposures=evt_budget_cap" in state_context
    assert "drift_score=" not in state_context
    assert "trait_drift_map=" not in state_context
    assert "sycophancy_risk=" not in state_context
