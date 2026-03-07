"""Pre-injected policy simulation scripts for MVP benchmarking."""

from __future__ import annotations

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
]


def load_mvp_policy_scripts() -> list[SimulationScript]:
    """Return the pre-injected scripts used for MVP benchmarking."""
    return [SimulationScript.from_dict(item) for item in _MVP_POLICY_SCRIPTS]


def load_mvp_policy_script_map() -> dict[str, SimulationScript]:
    return {script.simulation_id: script for script in load_mvp_policy_scripts()}
