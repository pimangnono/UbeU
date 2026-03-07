"""Pre-injected MVP simulation scripts for benchmarking."""

from __future__ import annotations

import copy

from .script import SimulationScript


_MVP_POLICY_SCRIPTS = [
    {
        "simulation_id": "youth_employment_policy",
        "title": "Youth Employment Support Policy",
        "objective": "Understand first-order and spillover effects of youth employment support expansion.",
        "brief": (
            "Policy A expands employment support for people in their 20s and 30s, but adds documentation "
            "requirements and may reshape local labor demand. Stakeholders should discuss direct benefits, "
            "implementation friction, and second-order spillovers."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Jiho",
                "role": "Primary affected youth worker",
                "identity_core": {"age_band": "20s", "occupation": "contract designer", "location": "Seoul"},
                "personality_prior": {"O": 0.62, "C": 0.48, "E": 0.41, "A": 0.57, "N": 0.61},
                "incentives": ["income stability", "career mobility"],
                "concerns": ["cash flow gaps", "administrative burden"],
                "communication_style": {"tone": "pragmatic", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_2",
                "display_name": "Mr. Park",
                "role": "Adjacent local merchant",
                "identity_core": {"age_band": "50s", "occupation": "restaurant owner"},
                "personality_prior": {"O": 0.34, "C": 0.72, "E": 0.39, "A": 0.44, "N": 0.46},
                "incentives": ["stable staffing", "predictable neighborhood demand"],
                "concerns": ["worker churn", "reduced evening traffic"],
                "communication_style": {"tone": "plainspoken", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_3",
                "display_name": "Officer Kim",
                "role": "District policy administrator",
                "identity_core": {"age_band": "40s", "occupation": "operations lead"},
                "personality_prior": {"O": 0.45, "C": 0.78, "E": 0.52, "A": 0.49, "N": 0.38},
                "incentives": ["smooth implementation", "compliance"],
                "concerns": ["fraud risk", "processing backlog"],
                "communication_style": {"tone": "structured", "brevity": "moderate"},
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Surface direct expected effects", "style": "neutral", "max_turns": 3, "cues": ["direct_impact"]},
            {"name": "TENSION", "goal": "Expose spillovers and implementation tension", "style": "disagreement", "max_turns": 3, "cues": ["spillover", "administrative_friction"]},
            {"name": "NEGOTIATION", "goal": "Test compromise under pressure", "style": "consensus", "max_turns": 3, "cues": ["tradeoff", "coordination"]},
            {"name": "CLOSING", "goal": "Summarize stable agreements and unresolved issues", "style": "neutral", "max_turns": 2, "cues": ["summary", "commitment"]},
        ],
        "world_events": [
            {
                "event_id": "evt_budget_cap",
                "title": "Budget cap rumor",
                "description": "A rumor suggests the ministry may cap the total budget next quarter.",
                "trigger_phase": "TENSION",
            },
            {
                "event_id": "evt_merchant_feedback",
                "title": "Merchant association complaint",
                "description": "A local merchant association claims the policy shifts work hours away from neighborhood businesses.",
                "trigger_phase": "NEGOTIATION",
            },
        ],
    },
    {
        "simulation_id": "housing_support_policy",
        "title": "Housing Subsidy Expansion",
        "objective": "Explore direct benefits and rent market spillovers from a housing support policy.",
        "brief": (
            "Policy B expands rent support for young households. The intended goal is affordability, but stakeholders "
            "expect second-order effects on landlords, local merchants, and district administration."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Sora",
                "role": "Young renter",
                "identity_core": {"age_band": "30s", "occupation": "junior marketer"},
                "personality_prior": {"O": 0.55, "C": 0.46, "E": 0.45, "A": 0.61, "N": 0.58},
                "incentives": ["rent affordability", "residential stability"],
                "concerns": ["eligibility churn", "deposit pressure"],
            },
            {
                "actor_id": "actor_2",
                "display_name": "Ms. Han",
                "role": "Small property owner",
                "identity_core": {"age_band": "50s", "occupation": "landlord"},
                "personality_prior": {"O": 0.31, "C": 0.73, "E": 0.36, "A": 0.40, "N": 0.42},
                "incentives": ["stable rent payments", "predictable regulation"],
                "concerns": ["moral hazard", "rent control pressure"],
            },
            {
                "actor_id": "actor_3",
                "display_name": "Director Lee",
                "role": "District housing administrator",
                "identity_core": {"age_band": "40s", "occupation": "public housing lead"},
                "personality_prior": {"O": 0.43, "C": 0.80, "E": 0.47, "A": 0.51, "N": 0.34},
                "incentives": ["fair allocation", "budget integrity"],
                "concerns": ["verification load", "public backlash"],
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Identify intended benefits", "style": "neutral", "max_turns": 3, "cues": ["affordability"]},
            {"name": "TENSION", "goal": "Expose rent market spillovers", "style": "disagreement", "max_turns": 3, "cues": ["spillover", "supply_response"]},
            {"name": "NEGOTIATION", "goal": "Search for implementation safeguards", "style": "consensus", "max_turns": 3, "cues": ["safeguard", "tradeoff"]},
            {"name": "CLOSING", "goal": "Lock open questions and owners", "style": "neutral", "max_turns": 2, "cues": ["summary", "follow_up"]},
        ],
        "world_events": [
            {
                "event_id": "evt_landlord_signal",
                "title": "Landlord pricing response",
                "description": "Private landlord chats suggest some owners may raise rents preemptively.",
                "trigger_phase": "TENSION",
            }
        ],
    },
    {
        "simulation_id": "commuting_support_policy",
        "title": "Commuting Subsidy Policy",
        "objective": "Evaluate commuting subsidy effects on workers, small businesses, and local administration.",
        "brief": (
            "Policy C subsidizes public transit and commuting costs for younger workers. The goal is labor participation, "
            "but there may be spillovers in local retail demand, employer scheduling, and administrative complexity."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Minji",
                "role": "Early-career commuter",
                "identity_core": {"age_band": "20s", "occupation": "hospitality worker"},
                "personality_prior": {"O": 0.49, "C": 0.52, "E": 0.44, "A": 0.59, "N": 0.55},
                "incentives": ["lower transport costs", "stable work access"],
                "concerns": ["late reimbursement", "schedule mismatch"],
            },
            {
                "actor_id": "actor_2",
                "display_name": "Mr. Choi",
                "role": "Small retail employer",
                "identity_core": {"age_band": "50s", "occupation": "store owner"},
                "personality_prior": {"O": 0.33, "C": 0.69, "E": 0.42, "A": 0.43, "N": 0.40},
                "incentives": ["reliable staffing", "predictable shift coverage"],
                "concerns": ["peak-hour absenteeism", "compliance paperwork"],
            },
            {
                "actor_id": "actor_3",
                "display_name": "Planner Yoon",
                "role": "Transport policy coordinator",
                "identity_core": {"age_band": "40s", "occupation": "mobility planner"},
                "personality_prior": {"O": 0.50, "C": 0.77, "E": 0.50, "A": 0.47, "N": 0.35},
                "incentives": ["efficient uptake", "budget accountability"],
                "concerns": ["fraudulent claims", "low adoption"],
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Clarify direct labor participation benefits", "style": "neutral", "max_turns": 3, "cues": ["direct_impact"]},
            {"name": "TENSION", "goal": "Debate business and operational spillovers", "style": "disagreement", "max_turns": 3, "cues": ["spillover", "operational_risk"]},
            {"name": "NEGOTIATION", "goal": "Test mitigations and bounded influence", "style": "consensus", "max_turns": 3, "cues": ["mitigation", "coordination"]},
            {"name": "CLOSING", "goal": "Record what remains uncertain", "style": "neutral", "max_turns": 2, "cues": ["uncertainty", "summary"]},
        ],
        "world_events": [
            {
                "event_id": "evt_delay_notice",
                "title": "Reimbursement delay notice",
                "description": "A notice suggests reimbursements may be delayed by two weeks during rollout.",
                "trigger_phase": "TENSION",
            }
        ],
    },
    {
        "simulation_id": "new_product_launch",
        "title": "New Product Launch Pressure Test",
        "objective": "Stress-test launch readiness, messaging alignment, and operational risk under deadline pressure.",
        "brief": (
            "A company plans to launch a new consumer AI product in three weeks. Product, marketing, and operations "
            "leaders must decide whether to keep the date, narrow the scope, or delay. Stakeholders should surface "
            "brand upside, launch risk, execution bottlenecks, and who owns mitigation."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Daeun",
                "role": "Product launch lead",
                "identity_core": {"function": "product", "seniority": "director", "company_stage": "growth"},
                "personality_prior": {"O": 0.61, "C": 0.58, "E": 0.46, "A": 0.49, "N": 0.44},
                "incentives": ["credible launch", "clear feature positioning"],
                "concerns": ["scope creep", "unreliable demo experience"],
                "communication_style": {"tone": "focused", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_2",
                "display_name": "Mina",
                "role": "Marketing lead",
                "identity_core": {"function": "marketing", "seniority": "head", "company_stage": "growth"},
                "personality_prior": {"O": 0.68, "C": 0.47, "E": 0.64, "A": 0.55, "N": 0.49},
                "incentives": ["category impact", "strong launch narrative"],
                "concerns": ["weak differentiation", "last-minute positioning changes"],
                "communication_style": {"tone": "energetic", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_3",
                "display_name": "Victor",
                "role": "Operations and reliability lead",
                "identity_core": {"function": "ops", "seniority": "director", "company_stage": "growth"},
                "personality_prior": {"O": 0.32, "C": 0.81, "E": 0.37, "A": 0.41, "N": 0.38},
                "incentives": ["stable rollout", "supportable launch load"],
                "concerns": ["incident risk", "on-call overload"],
                "communication_style": {"tone": "plainspoken", "brevity": "moderate"},
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Clarify why the launch matters and what success means", "style": "neutral", "max_turns": 3, "cues": ["launch_goal", "success_metric"]},
            {"name": "TENSION", "goal": "Expose readiness gaps and go-to-market conflict", "style": "disagreement", "max_turns": 3, "cues": ["deadline_pressure", "readiness_risk", "brand_tradeoff"]},
            {"name": "NEGOTIATION", "goal": "Force a realistic launch decision and mitigation plan", "style": "consensus", "max_turns": 3, "cues": ["scope_cut", "owner", "fallback"]},
            {"name": "CLOSING", "goal": "Lock the final call, owners, and unresolved risks", "style": "neutral", "max_turns": 2, "cues": ["commitment", "residual_risk"]},
        ],
        "world_events": [
            {
                "event_id": "evt_qa_regression",
                "title": "QA regression report",
                "description": "QA reports a regression in the core onboarding flow that appears in the latest release candidate.",
                "trigger_phase": "TENSION",
            },
            {
                "event_id": "evt_press_leak",
                "title": "Press leak",
                "description": "A trade publication publishes an early article that sets expectations higher than the current product can support.",
                "trigger_phase": "NEGOTIATION",
            },
        ],
    },
    {
        "simulation_id": "post_merger_integration",
        "title": "Post-Merger Integration Pressure Test",
        "objective": "Stress-test trust, retention, and integration decisions after an acquisition announcement.",
        "brief": (
            "A larger company has acquired a smaller startup. Leaders now need to decide how aggressively to integrate "
            "teams, systems, and brand while retaining key people. Stakeholders should surface trust gaps, culture risk, "
            "retention pressure, and integration tradeoffs."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Arjun",
                "role": "Acquirer strategy lead",
                "identity_core": {"function": "strategy", "seniority": "VP", "company_type": "acquirer"},
                "personality_prior": {"O": 0.52, "C": 0.74, "E": 0.51, "A": 0.43, "N": 0.36},
                "incentives": ["captured synergies", "fast operating alignment"],
                "concerns": ["integration drift", "missed board targets"],
                "communication_style": {"tone": "structured", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_2",
                "display_name": "Soojin",
                "role": "Acquired company founder",
                "identity_core": {"function": "founder", "seniority": "CEO", "company_type": "acquired"},
                "personality_prior": {"O": 0.69, "C": 0.44, "E": 0.58, "A": 0.38, "N": 0.54},
                "incentives": ["team retention", "product autonomy"],
                "concerns": ["culture loss", "talent exits"],
                "communication_style": {"tone": "direct", "brevity": "moderate"},
            },
            {
                "actor_id": "actor_3",
                "display_name": "Elena",
                "role": "People and integration lead",
                "identity_core": {"function": "people", "seniority": "director", "company_type": "integration"},
                "personality_prior": {"O": 0.47, "C": 0.76, "E": 0.48, "A": 0.64, "N": 0.47},
                "incentives": ["retention stability", "clear operating model"],
                "concerns": ["trust erosion", "role ambiguity"],
                "communication_style": {"tone": "calm", "brevity": "moderate"},
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Clarify what must be preserved and what must change", "style": "neutral", "max_turns": 3, "cues": ["integration_goal", "retention_priority"]},
            {"name": "TENSION", "goal": "Surface trust gaps and control conflicts", "style": "disagreement", "max_turns": 3, "cues": ["trust", "autonomy", "retention_risk"]},
            {"name": "NEGOTIATION", "goal": "Choose an operating model and ownership plan", "style": "consensus", "max_turns": 3, "cues": ["operating_model", "owner", "sequencing"]},
            {"name": "CLOSING", "goal": "Record the integration stance and unresolved people risks", "style": "neutral", "max_turns": 2, "cues": ["summary", "people_risk"]},
        ],
        "world_events": [
            {
                "event_id": "evt_retention_signal",
                "title": "Retention risk signal",
                "description": "Two senior engineers privately signal they may leave if the acquired team loses roadmap autonomy this quarter.",
                "trigger_phase": "TENSION",
            },
            {
                "event_id": "evt_board_pressure",
                "title": "Board pressure note",
                "description": "The board asks for a visible integration milestone before the next earnings call.",
                "trigger_phase": "NEGOTIATION",
            },
        ],
    },
]


def _policy_action_spec() -> dict[str, object]:
    schema = [
        "alignment",
        "trust",
        "uncertainty",
        "execution_confidence",
        "risk",
        "admin_feasibility",
        "spillover_risk",
    ]
    return {
        "world_state_schema": schema,
        "initial_world_state": {
            "alignment": 0.48,
            "trust": 0.50,
            "uncertainty": 0.56,
            "execution_confidence": 0.44,
            "risk": 0.52,
            "admin_feasibility": 0.46,
            "spillover_risk": 0.54,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "pilot",
            "defer_decision",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "uncertainty", "risk"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "transition_rules": {
            "OPENING": {
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.04, "admin_feasibility": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                    "feedback_template": "Evidence request clarifies early implementation questions.",
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.04, "alignment": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                    "feedback_template": "A public clarification improves initial alignment.",
                },
            },
            "TENSION": {
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.08, "risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                    "feedback_template": "Evidence gathering reduces uncertainty during the conflict phase.",
                },
                "narrow_scope": {
                    "global_deltas": {"risk": -0.08, "spillover_risk": -0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                    "feedback_template": "A narrower rollout reduces spillover risk.",
                },
                "pilot": {
                    "global_deltas": {"uncertainty": -0.04, "admin_feasibility": 0.04, "spillover_risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                    "feedback_template": "A pilot contains uncertainty without forcing a full commitment.",
                },
                "defer_decision": {
                    "global_deltas": {"uncertainty": 0.04, "alignment": -0.04},
                    "owner_local_deltas": {"risk": 0.04},
                    "feedback_template": "Deferral protects the actor short term but keeps uncertainty elevated.",
                },
            },
            "NEGOTIATION": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.08, "admin_feasibility": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                    "feedback_template": "Named ownership increases coordination confidence.",
                },
                "pilot": {
                    "global_deltas": {"uncertainty": -0.08, "spillover_risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                    "feedback_template": "A bounded pilot creates a lower-risk compromise.",
                },
                "narrow_scope": {
                    "global_deltas": {"risk": -0.04, "spillover_risk": -0.08, "execution_confidence": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                    "feedback_template": "Scope reduction improves feasibility and lowers risk.",
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.04, "alignment": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                    "feedback_template": "Publishing the negotiation stance improves stakeholder trust.",
                },
            },
            "CLOSING": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                    "feedback_template": "Closing ownership decisions strengthen execution confidence.",
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.08, "alignment": 0.08, "uncertainty": -0.04},
                    "owner_local_deltas": {"trust": 0.04},
                    "feedback_template": "A closing update improves trust and reduces residual uncertainty.",
                },
                "defer_decision": {
                    "global_deltas": {"uncertainty": 0.04, "execution_confidence": -0.04},
                    "owner_local_deltas": {"risk": 0.04},
                    "feedback_template": "An unresolved closing decision preserves uncertainty.",
                },
            },
        },
    }


def _launch_action_spec() -> dict[str, object]:
    schema = [
        "alignment",
        "trust",
        "uncertainty",
        "execution_confidence",
        "risk",
        "launch_readiness",
        "message_alignment",
        "incident_risk",
    ]
    return {
        "world_state_schema": schema,
        "initial_world_state": {
            "alignment": 0.46,
            "trust": 0.51,
            "uncertainty": 0.55,
            "execution_confidence": 0.45,
            "risk": 0.56,
            "launch_readiness": 0.47,
            "message_alignment": 0.50,
            "incident_risk": 0.58,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "pilot",
            "commit_resource",
            "defer_decision",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "uncertainty", "risk", "launch_readiness"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "transition_rules": {
            "OPENING": {
                "publish_update": {
                    "global_deltas": {"alignment": 0.04, "message_alignment": 0.08},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.04, "launch_readiness": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
            },
            "TENSION": {
                "narrow_scope": {
                    "global_deltas": {"incident_risk": -0.12, "risk": -0.08, "launch_readiness": 0.08},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.08, "incident_risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "defer_decision": {
                    "global_deltas": {"risk": -0.04, "launch_readiness": -0.08, "uncertainty": 0.04},
                    "owner_local_deltas": {"risk": -0.04},
                },
            },
            "NEGOTIATION": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.08, "launch_readiness": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "commit_resource": {
                    "global_deltas": {"launch_readiness": 0.08, "execution_confidence": 0.08, "risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "pilot": {
                    "global_deltas": {"incident_risk": -0.08, "uncertainty": -0.04, "launch_readiness": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "publish_update": {
                    "global_deltas": {"message_alignment": 0.08, "trust": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
            "CLOSING": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "publish_update": {
                    "global_deltas": {"message_alignment": 0.08, "trust": 0.08, "uncertainty": -0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "defer_decision": {
                    "global_deltas": {"launch_readiness": -0.08, "uncertainty": 0.04},
                    "owner_local_deltas": {"risk": 0.04},
                },
            },
        },
    }


def _pmi_action_spec() -> dict[str, object]:
    schema = [
        "alignment",
        "trust",
        "uncertainty",
        "execution_confidence",
        "risk",
        "retention_risk",
        "autonomy_confidence",
        "integration_clarity",
    ]
    return {
        "world_state_schema": schema,
        "initial_world_state": {
            "alignment": 0.43,
            "trust": 0.47,
            "uncertainty": 0.58,
            "execution_confidence": 0.42,
            "risk": 0.55,
            "retention_risk": 0.59,
            "autonomy_confidence": 0.44,
            "integration_clarity": 0.40,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "pilot",
            "defer_decision",
            "preserve_autonomy",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "trust", "uncertainty", "retention_risk"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "transition_rules": {
            "OPENING": {
                "publish_update": {
                    "global_deltas": {"trust": 0.04, "alignment": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.04, "integration_clarity": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
            },
            "TENSION": {
                "preserve_autonomy": {
                    "global_deltas": {"trust": 0.08, "autonomy_confidence": 0.12, "retention_risk": -0.08},
                    "owner_local_deltas": {"trust": 0.08},
                    "target_local_deltas": {"trust": 0.04},
                },
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.08, "integration_clarity": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "defer_decision": {
                    "global_deltas": {"retention_risk": 0.08, "uncertainty": 0.04},
                    "owner_local_deltas": {"risk": 0.04},
                },
            },
            "NEGOTIATION": {
                "assign_owner": {
                    "global_deltas": {"integration_clarity": 0.12, "execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "pilot": {
                    "global_deltas": {"uncertainty": -0.04, "risk": -0.04, "integration_clarity": 0.08},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "preserve_autonomy": {
                    "global_deltas": {"autonomy_confidence": 0.08, "trust": 0.04, "retention_risk": -0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
            "CLOSING": {
                "assign_owner": {
                    "global_deltas": {"integration_clarity": 0.08, "execution_confidence": 0.08},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.08, "uncertainty": -0.04, "alignment": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "preserve_autonomy": {
                    "global_deltas": {"autonomy_confidence": 0.08, "retention_risk": -0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
        },
    }


def _augment_with_action_layer_spec(item: dict[str, object]) -> dict[str, object]:
    payload = copy.deepcopy(item)
    simulation_id = str(payload["simulation_id"])
    if simulation_id in {
        "youth_employment_policy",
        "housing_support_policy",
        "commuting_support_policy",
    }:
        payload.update(_policy_action_spec())
    elif simulation_id == "new_product_launch":
        payload.update(_launch_action_spec())
    elif simulation_id == "post_merger_integration":
        payload.update(_pmi_action_spec())
    else:
        raise ValueError(f"Unknown MVP script id for action-layer augmentation: {simulation_id}")
    return payload


def load_mvp_policy_scripts() -> list[SimulationScript]:
    """Return the pre-injected scripts used for MVP benchmarking."""
    return [SimulationScript.from_dict(_augment_with_action_layer_spec(item)) for item in _MVP_POLICY_SCRIPTS]


def load_mvp_policy_script_map() -> dict[str, SimulationScript]:
    return {script.simulation_id: script for script in load_mvp_policy_scripts()}
