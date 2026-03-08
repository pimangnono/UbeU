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


_EXPLORATORY_PRESSURE_SCRIPTS = [
    {
        "simulation_id": "brand_crisis_response",
        "title": "Brand Crisis Response Pressure Test",
        "objective": "Explore reputational, legal, and community tradeoffs after a public product backlash.",
        "brief": (
            "A consumer brand faces an online backlash after a widely shared customer incident. The team must "
            "decide how to acknowledge the issue, what to investigate, and how much of the response should be "
            "public versus internal. The point is not to force one correct ending, but to observe how different "
            "stakeholder priorities shape the response path."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Avery",
                "role": "Brand communications lead",
                "identity_core": {"function": "communications", "seniority": "director"},
                "personality_prior": {"O": 0.58, "C": 0.54, "E": 0.63, "A": 0.57, "N": 0.46},
                "incentives": ["protect trust", "stabilize public narrative"],
                "concerns": ["brand damage", "slow response"],
            },
            {
                "actor_id": "actor_2",
                "display_name": "Daniel",
                "role": "Legal and risk lead",
                "identity_core": {"function": "legal", "seniority": "director"},
                "personality_prior": {"O": 0.33, "C": 0.82, "E": 0.34, "A": 0.39, "N": 0.37},
                "incentives": ["limit legal exposure", "maintain process discipline"],
                "concerns": ["premature admission", "regulatory scrutiny"],
            },
            {
                "actor_id": "actor_3",
                "display_name": "Leah",
                "role": "Community operations lead",
                "identity_core": {"function": "community", "seniority": "manager"},
                "personality_prior": {"O": 0.49, "C": 0.63, "E": 0.52, "A": 0.64, "N": 0.53},
                "incentives": ["reduce frontline escalation", "support affected users"],
                "concerns": ["agent burnout", "unanswered customer harm"],
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Frame what happened and what is uncertain", "style": "neutral", "max_turns": 3, "cues": ["incident_frame", "known_unknowns"]},
            {"name": "TENSION", "goal": "Surface reputational, legal, and community pressure", "style": "disagreement", "max_turns": 3, "cues": ["reputation", "liability", "frontline_pressure"]},
            {"name": "NEGOTIATION", "goal": "Test response paths without forcing a single fixed ending", "style": "consensus", "max_turns": 3, "cues": ["response_path", "ownership", "risk_tradeoff"]},
            {"name": "CLOSING", "goal": "Record the response stance and unresolved risks", "style": "neutral", "max_turns": 2, "cues": ["summary", "residual_risk"]},
        ],
        "world_events": [
            {
                "event_id": "evt_viral_clip",
                "title": "Viral clip spreads",
                "description": "A short video of the customer incident spreads rapidly across multiple social platforms.",
                "trigger_phase": "TENSION",
            },
            {
                "event_id": "evt_regulator_inquiry",
                "title": "Regulator inquiry",
                "description": "A consumer protection regulator asks whether the company plans a formal corrective action.",
                "trigger_phase": "NEGOTIATION",
            },
        ],
    },
    {
        "simulation_id": "resource_reallocation_crunch",
        "title": "Resource Reallocation Crunch",
        "objective": "Explore how teams react when budget cuts force competing priorities into the open.",
        "brief": (
            "A company faces an unexpected budget cut and must rebalance roadmap commitments, support load, and "
            "operational resilience. There is no fixed preferred ending; the goal is to observe how different "
            "stakeholders trade off delivery, customer stability, and financial control under pressure."
        ),
        "stakeholders": [
            {
                "actor_id": "actor_1",
                "display_name": "Iris",
                "role": "Finance controller",
                "identity_core": {"function": "finance", "seniority": "director"},
                "personality_prior": {"O": 0.31, "C": 0.84, "E": 0.36, "A": 0.41, "N": 0.34},
                "incentives": ["budget discipline", "predictable burn"],
                "concerns": ["overcommitment", "late cost surprises"],
            },
            {
                "actor_id": "actor_2",
                "display_name": "Noah",
                "role": "Product program lead",
                "identity_core": {"function": "product", "seniority": "director"},
                "personality_prior": {"O": 0.57, "C": 0.62, "E": 0.47, "A": 0.48, "N": 0.42},
                "incentives": ["protect roadmap integrity", "keep critical delivery on track"],
                "concerns": ["team thrash", "scope collapse"],
            },
            {
                "actor_id": "actor_3",
                "display_name": "Sara",
                "role": "Customer success lead",
                "identity_core": {"function": "customer_success", "seniority": "head"},
                "personality_prior": {"O": 0.46, "C": 0.58, "E": 0.56, "A": 0.67, "N": 0.51},
                "incentives": ["customer continuity", "service stability"],
                "concerns": ["renewal risk", "support backlog"],
            },
        ],
        "phases": [
            {"name": "OPENING", "goal": "Clarify what changed and what is most exposed", "style": "neutral", "max_turns": 3, "cues": ["budget_shock", "exposure"]},
            {"name": "TENSION", "goal": "Expose tradeoffs between savings, delivery, and customer impact", "style": "disagreement", "max_turns": 3, "cues": ["savings", "delivery_risk", "customer_risk"]},
            {"name": "NEGOTIATION", "goal": "Test competing reallocation paths", "style": "consensus", "max_turns": 3, "cues": ["reprioritization", "ownership", "risk_tradeoff"]},
            {"name": "CLOSING", "goal": "Capture chosen direction and unresolved pressure", "style": "neutral", "max_turns": 2, "cues": ["summary", "residual_exposure"]},
        ],
        "world_events": [
            {
                "event_id": "evt_budget_cut_notice",
                "title": "Budget cut notice",
                "description": "Finance confirms a 15% spend reduction target for the next quarter.",
                "trigger_phase": "TENSION",
            },
            {
                "event_id": "evt_customer_escalation",
                "title": "Customer escalation",
                "description": "A strategic customer escalates concerns about delayed commitments and support responsiveness.",
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


def _brand_crisis_action_spec() -> dict[str, object]:
    schema = [
        "alignment",
        "trust",
        "uncertainty",
        "execution_confidence",
        "risk",
        "reputation_stability",
        "legal_exposure",
    ]
    return {
        "world_state_schema": schema,
        "initial_world_state": {
            "alignment": 0.42,
            "trust": 0.46,
            "uncertainty": 0.61,
            "execution_confidence": 0.40,
            "risk": 0.62,
            "reputation_stability": 0.34,
            "legal_exposure": 0.57,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "defer_decision",
            "commit_resource",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "trust", "uncertainty", "risk", "reputation_stability"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "transition_rules": {
            "OPENING": {
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.04, "legal_exposure": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.04, "reputation_stability": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
            "TENSION": {
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.08, "legal_exposure": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "publish_update": {
                    "global_deltas": {"reputation_stability": 0.08, "trust": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "narrow_scope": {
                    "global_deltas": {"risk": -0.08, "legal_exposure": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
            },
            "NEGOTIATION": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.08, "reputation_stability": 0.08, "uncertainty": -0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "commit_resource": {
                    "global_deltas": {"execution_confidence": 0.08, "risk": -0.04, "reputation_stability": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "defer_decision": {
                    "global_deltas": {"uncertainty": 0.08, "reputation_stability": -0.04},
                    "owner_local_deltas": {"risk": 0.04},
                },
            },
            "CLOSING": {
                "publish_update": {
                    "global_deltas": {"trust": 0.08, "uncertainty": -0.04, "reputation_stability": 0.08},
                    "owner_local_deltas": {"trust": 0.04},
                },
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
            },
        },
    }


def _resource_reallocation_action_spec() -> dict[str, object]:
    schema = [
        "alignment",
        "trust",
        "uncertainty",
        "execution_confidence",
        "risk",
        "budget_health",
        "delivery_capacity",
        "customer_risk",
    ]
    return {
        "world_state_schema": schema,
        "initial_world_state": {
            "alignment": 0.45,
            "trust": 0.49,
            "uncertainty": 0.57,
            "execution_confidence": 0.43,
            "risk": 0.58,
            "budget_health": 0.38,
            "delivery_capacity": 0.47,
            "customer_risk": 0.55,
        },
        "allowed_action_types": [
            "assign_owner",
            "request_evidence",
            "publish_update",
            "narrow_scope",
            "commit_resource",
            "defer_decision",
        ],
        "state_visibility_rules": {
            "global_keys": ["alignment", "uncertainty", "risk", "budget_health", "customer_risk"],
            "local_keys": ["trust", "execution_confidence", "alignment"],
            "max_recent_actions": 2,
        },
        "transition_rules": {
            "OPENING": {
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.04, "budget_health": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "publish_update": {
                    "global_deltas": {"alignment": 0.04, "trust": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
            "TENSION": {
                "narrow_scope": {
                    "global_deltas": {"risk": -0.08, "delivery_capacity": 0.08, "customer_risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "defer_decision": {
                    "global_deltas": {"uncertainty": 0.04, "delivery_capacity": -0.04, "budget_health": 0.04},
                    "owner_local_deltas": {"risk": 0.04},
                },
                "request_evidence": {
                    "global_deltas": {"uncertainty": -0.08, "customer_risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
            },
            "NEGOTIATION": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "commit_resource": {
                    "global_deltas": {"delivery_capacity": 0.08, "budget_health": -0.08, "customer_risk": -0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "narrow_scope": {
                    "global_deltas": {"budget_health": 0.08, "risk": -0.04, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.04},
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.04, "alignment": 0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
            "CLOSING": {
                "assign_owner": {
                    "global_deltas": {"execution_confidence": 0.08, "alignment": 0.04},
                    "owner_local_deltas": {"execution_confidence": 0.08},
                },
                "publish_update": {
                    "global_deltas": {"trust": 0.08, "uncertainty": -0.04},
                    "owner_local_deltas": {"trust": 0.04},
                },
            },
        },
    }


def _scenario_family(simulation_id: str) -> str:
    if simulation_id in {
        "youth_employment_policy",
        "housing_support_policy",
        "commuting_support_policy",
    }:
        return "policy_spillover"
    if simulation_id == "new_product_launch":
        return "launch_pressure"
    if simulation_id == "post_merger_integration":
        return "integration_trust"
    if simulation_id == "brand_crisis_response":
        return "brand_crisis"
    if simulation_id == "resource_reallocation_crunch":
        return "resource_scarcity"
    return "generic"


def _simulation_mode(simulation_id: str) -> str:
    if simulation_id in {"brand_crisis_response", "resource_reallocation_crunch"}:
        return "exploratory"
    return "guided"


def _outcome_spec(simulation_id: str) -> dict[str, object]:
    if _simulation_mode(simulation_id) == "exploratory":
        return {
            "fixed_ending": False,
            "target_end_state": {},
            "evaluation_focus": ["trajectory_diversity", "persona_stability", "stakeholder_conflict_map"],
        }
    if simulation_id == "new_product_launch":
        return {
            "fixed_ending": True,
            "target_end_state": {
                "execution_confidence": "increase",
                "launch_readiness": "increase",
                "incident_risk": "decrease",
            },
            "evaluation_focus": ["action_coherence", "persona_stability", "owner_clarity"],
        }
    if simulation_id == "post_merger_integration":
        return {
            "fixed_ending": True,
            "target_end_state": {
                "integration_clarity": "increase",
                "retention_risk": "decrease",
                "trust": "increase",
            },
            "evaluation_focus": ["trust_preservation", "persona_stability", "coordination_clarity"],
        }
    return {
        "fixed_ending": True,
        "target_end_state": {
            "alignment": "increase",
            "uncertainty": "decrease",
            "execution_confidence": "increase",
        },
        "evaluation_focus": ["persona_stability", "action_coherence", "spillover_control"],
    }


def _phase_action_policies(simulation_id: str) -> dict[str, dict[str, object]]:
    policies = {
        "OPENING": {
            "action_mode": "shadow",
            "diversity_required": False,
            "duplicate_penalty": 0.04,
            "uniqueness_bonus": 0.04,
            "convergence_backoff_threshold": 0.97,
            "allow_no_action": True,
            "family_cap": 1,
            "max_actions_per_phase": 1,
            "sparsity_threshold": 0.66,
            "style_slot_limit": 3,
            "pool_max_concurrency": 2,
            "planner_cache": True,
        },
        "TENSION": {
            "action_mode": "shadow",
            "diversity_required": True,
            "duplicate_penalty": 0.14,
            "uniqueness_bonus": 0.10,
            "convergence_backoff_threshold": 0.93,
            "allow_no_action": True,
            "family_cap": 1,
            "max_actions_per_phase": 2,
            "sparsity_threshold": 0.70,
            "style_slot_limit": 3,
            "pool_max_concurrency": 2,
            "planner_cache": False,
        },
        "NEGOTIATION": {
            "action_mode": "execute",
            "diversity_required": True,
            "duplicate_penalty": 0.24,
            "uniqueness_bonus": 0.18,
            "convergence_backoff_threshold": 0.90,
            "allow_no_action": True,
            "family_cap": 1,
            "max_actions_per_phase": 3,
            "sparsity_threshold": 0.76,
            "style_slot_limit": 4,
            "pool_max_concurrency": 2,
            "planner_cache": False,
        },
        "CLOSING": {
            "action_mode": "execute",
            "diversity_required": False,
            "duplicate_penalty": 0.08,
            "uniqueness_bonus": 0.06,
            "convergence_backoff_threshold": 0.95,
            "allow_no_action": True,
            "family_cap": 1,
            "max_actions_per_phase": 2,
            "sparsity_threshold": 0.64,
            "style_slot_limit": 2,
            "pool_max_concurrency": 1,
            "planner_cache": True,
        },
    }
    if simulation_id == "new_product_launch":
        policies["NEGOTIATION"].update({
            "max_actions_per_phase": 2,
            "sparsity_threshold": 0.82,
            "duplicate_penalty": 0.30,
            "style_slot_limit": 2,
            "pool_max_concurrency": 1,
        })
        policies["TENSION"].update({
            "max_actions_per_phase": 1,
            "sparsity_threshold": 0.76,
            "style_slot_limit": 2,
            "pool_max_concurrency": 1,
        })
    elif simulation_id == "post_merger_integration":
        policies["NEGOTIATION"].update({
            "max_actions_per_phase": 2,
            "sparsity_threshold": 0.80,
            "duplicate_penalty": 0.28,
            "style_slot_limit": 2,
            "pool_max_concurrency": 1,
        })
        policies["CLOSING"].update({
            "max_actions_per_phase": 1,
            "sparsity_threshold": 0.72,
            "style_slot_limit": 2,
            "pool_max_concurrency": 1,
        })
    elif simulation_id in {"brand_crisis_response", "resource_reallocation_crunch"}:
        policies["OPENING"].update({
            "action_mode": "shadow",
            "diversity_required": True,
            "duplicate_penalty": 0.10,
            "uniqueness_bonus": 0.12,
            "family_cap": 2,
            "sparsity_threshold": 0.52,
            "style_slot_limit": 4,
        })
        policies["TENSION"].update({
            "action_mode": "shadow",
            "diversity_required": True,
            "duplicate_penalty": 0.10,
            "uniqueness_bonus": 0.12,
            "family_cap": 2,
            "sparsity_threshold": 0.52,
            "style_slot_limit": 4,
        })
        policies["NEGOTIATION"].update({
            "action_mode": "execute",
            "duplicate_penalty": 0.24,
            "uniqueness_bonus": 0.30,
            "family_cap": 1,
            "max_same_family_per_phase": 1,
            "max_actions_per_phase": 2,
            "sparsity_threshold": 0.55,
            "style_slot_limit": 4,
        })
        policies["CLOSING"].update({
            "action_mode": "shadow",
            "diversity_required": True,
            "duplicate_penalty": 0.10,
            "uniqueness_bonus": 0.12,
            "family_cap": 2,
            "max_actions_per_phase": 1,
            "sparsity_threshold": 0.52,
            "style_slot_limit": 4,
        })
    return policies


def _default_pref(
    *,
    primary_families: list[str],
    secondary_families: list[str],
    state_priority_keys: list[str],
    avoid_families: list[str] | None = None,
    preferred_action_types: list[str] | None = None,
    preferred_target_keys: list[str] | None = None,
) -> dict[str, object]:
    return {
        "primary_families": primary_families,
        "secondary_families": secondary_families,
        "avoid_families": avoid_families or [],
        "state_priority_keys": state_priority_keys,
        "preferred_action_types": preferred_action_types or [],
        "preferred_target_keys": preferred_target_keys or [],
    }


def _actor_action_preferences(simulation_id: str) -> dict[str, dict[str, dict[str, object]]]:
    if simulation_id == "youth_employment_policy":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["evidence", "governance"],
                    secondary_families=["communication", "scope"],
                    state_priority_keys=["uncertainty", "trust", "spillover_risk"],
                ),
                "NEGOTIATION": _default_pref(
                    primary_families=["scope", "communication"],
                    secondary_families=["evidence"],
                    state_priority_keys=["risk", "trust", "alignment"],
                    avoid_families=["ownership"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["evidence", "scope"],
                    secondary_families=["communication"],
                    state_priority_keys=["spillover_risk", "uncertainty", "risk"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["ownership", "communication"],
                    secondary_families=["evidence"],
                    state_priority_keys=["execution_confidence", "admin_feasibility", "alignment"],
                ),
            },
        }
    if simulation_id == "housing_support_policy":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["communication", "evidence"],
                    secondary_families=["scope"],
                    state_priority_keys=["trust", "uncertainty", "alignment"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["governance", "evidence"],
                    secondary_families=["timing"],
                    state_priority_keys=["risk", "spillover_risk", "trust"],
                    avoid_families=["ownership"],
                ),
                "NEGOTIATION": _default_pref(
                    primary_families=["evidence", "governance"],
                    secondary_families=["timing"],
                    state_priority_keys=["risk", "spillover_risk", "trust"],
                    avoid_families=["ownership", "resourcing"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["ownership", "communication"],
                    secondary_families=["evidence"],
                    state_priority_keys=["execution_confidence", "admin_feasibility", "alignment"],
                ),
            },
        }
    if simulation_id == "commuting_support_policy":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["evidence", "communication"],
                    secondary_families=["scope"],
                    state_priority_keys=["trust", "uncertainty", "risk"],
                    avoid_families=["ownership"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["evidence", "scope"],
                    secondary_families=["communication"],
                    state_priority_keys=["risk", "uncertainty", "alignment"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["ownership", "communication"],
                    secondary_families=["evidence"],
                    state_priority_keys=["execution_confidence", "alignment", "trust"],
                ),
            },
        }
    if simulation_id == "new_product_launch":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["ownership", "resourcing"],
                    secondary_families=["scope", "communication"],
                    state_priority_keys=["launch_readiness", "execution_confidence", "alignment"],
                ),
                "NEGOTIATION": _default_pref(
                    primary_families=["ownership", "resourcing"],
                    secondary_families=["scope"],
                    state_priority_keys=["execution_confidence", "launch_readiness", "alignment"],
                    avoid_families=["evidence"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["communication", "scope"],
                    secondary_families=["resourcing"],
                    state_priority_keys=["message_alignment", "trust", "launch_readiness"],
                ),
                "NEGOTIATION": _default_pref(
                    primary_families=["communication", "scope"],
                    secondary_families=["timing"],
                    state_priority_keys=["message_alignment", "trust", "alignment"],
                    avoid_families=["evidence"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["evidence", "scope"],
                    secondary_families=["timing"],
                    state_priority_keys=["risk", "incident_risk", "uncertainty"],
                ),
                "NEGOTIATION": _default_pref(
                    primary_families=["evidence", "scope"],
                    secondary_families=["timing"],
                    state_priority_keys=["risk", "incident_risk", "uncertainty"],
                    avoid_families=["communication", "ownership"],
                ),
            },
        }
    if simulation_id == "post_merger_integration":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["ownership", "communication"],
                    secondary_families=["resourcing"],
                    state_priority_keys=["integration_clarity", "execution_confidence", "alignment"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["governance", "communication"],
                    secondary_families=["timing"],
                    state_priority_keys=["autonomy_confidence", "trust", "retention_risk"],
                    avoid_families=["ownership"],
                ),
                "NEGOTIATION": _default_pref(
                    primary_families=["governance", "communication"],
                    secondary_families=["timing"],
                    state_priority_keys=["autonomy_confidence", "trust", "retention_risk"],
                    avoid_families=["ownership", "resourcing"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["communication", "ownership"],
                    secondary_families=["evidence"],
                    state_priority_keys=["trust", "retention_risk", "integration_clarity"],
                ),
            },
        }
    if simulation_id == "brand_crisis_response":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["communication", "ownership"],
                    secondary_families=["resourcing"],
                    state_priority_keys=["reputation_stability", "trust", "alignment"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["evidence", "governance"],
                    secondary_families=["scope"],
                    state_priority_keys=["legal_exposure", "risk", "uncertainty"],
                    avoid_families=["communication"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["communication", "scope"],
                    secondary_families=["resourcing"],
                    state_priority_keys=["trust", "risk", "execution_confidence"],
                ),
            },
        }
    if simulation_id == "resource_reallocation_crunch":
        return {
            "actor_1": {
                "default": _default_pref(
                    primary_families=["governance", "scope"],
                    secondary_families=["evidence"],
                    state_priority_keys=["budget_health", "risk", "uncertainty"],
                ),
            },
            "actor_2": {
                "default": _default_pref(
                    primary_families=["ownership", "resourcing"],
                    secondary_families=["scope"],
                    state_priority_keys=["delivery_capacity", "execution_confidence", "alignment"],
                ),
            },
            "actor_3": {
                "default": _default_pref(
                    primary_families=["communication", "evidence"],
                    secondary_families=["resourcing"],
                    state_priority_keys=["customer_risk", "trust", "alignment"],
                ),
            },
        }
    return {}


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
    elif simulation_id == "brand_crisis_response":
        payload.update(_brand_crisis_action_spec())
    elif simulation_id == "resource_reallocation_crunch":
        payload.update(_resource_reallocation_action_spec())
    else:
        raise ValueError(f"Unknown MVP script id for action-layer augmentation: {simulation_id}")
    payload["scenario_family"] = _scenario_family(simulation_id)
    payload["simulation_mode"] = _simulation_mode(simulation_id)
    payload["outcome_spec"] = _outcome_spec(simulation_id)
    payload["metadata"] = {
        **dict(payload.get("metadata", {})),
        "phase_action_policies": _phase_action_policies(simulation_id),
        "actor_action_preferences": _actor_action_preferences(simulation_id),
    }
    return payload


def load_mvp_policy_scripts() -> list[SimulationScript]:
    """Return the pre-injected scripts used for MVP benchmarking."""
    items = _MVP_POLICY_SCRIPTS + _EXPLORATORY_PRESSURE_SCRIPTS
    return [SimulationScript.from_dict(_augment_with_action_layer_spec(item)) for item in items]


def load_mvp_policy_script_map() -> dict[str, SimulationScript]:
    return {script.simulation_id: script for script in load_mvp_policy_scripts()}
