import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from simulation_engine.action_priors import action_role_fit_score, infer_role_action_prior


def test_marketing_role_prior_prefers_publish_update_and_message_alignment():
    prior = infer_role_action_prior(
        role="Marketing lead",
        incentives=["Protect brand message"],
        concerns=["Narrative confusion"],
        phase_name="OPENING",
        phase_cues=["alignment"],
        allowed_action_types=["publish_update", "request_evidence", "assign_owner"],
        valid_target_keys=["message_alignment", "alignment", "trust"],
    )

    assert prior.preferred_action_types[0] == "publish_update"
    assert prior.preferred_target_keys[0] == "message_alignment"


def test_ops_role_prior_prefers_evidence_or_pilot_over_publish_update():
    prior = infer_role_action_prior(
        role="Operations and reliability lead",
        incentives=["Reduce incident risk"],
        concerns=["Operational regression"],
        phase_name="TENSION",
        phase_cues=["fallback", "mitigation"],
        allowed_action_types=["publish_update", "request_evidence", "pilot", "narrow_scope"],
        valid_target_keys=["risk", "incident_risk", "uncertainty"],
    )

    assert prior.preferred_action_types[0] in {"request_evidence", "pilot", "narrow_scope"}
    assert prior.preferred_target_keys[0] in {"risk", "incident_risk", "uncertainty"}


def test_action_role_fit_rewards_role_appropriate_action():
    prior = infer_role_action_prior(
        role="Product launch lead",
        incentives=["Ship a credible launch"],
        concerns=["Slipping timeline"],
        phase_name="NEGOTIATION",
        phase_cues=["owner", "fallback"],
        allowed_action_types=["assign_owner", "publish_update", "request_evidence"],
        valid_target_keys=["execution_confidence", "launch_readiness", "alignment"],
    )
    fit_score, _ = action_role_fit_score(
        action_type="assign_owner",
        target_key="execution_confidence",
        prior=prior,
    )
    weak_score, _ = action_role_fit_score(
        action_type="publish_update",
        target_key="alignment",
        prior=prior,
    )

    assert fit_score > weak_score
