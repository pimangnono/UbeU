"""Ground truth outcomes for 20 final benchmark scenarios.

Each entry codifies the real-world historical outcome so that simulation
results can be compared against what actually happened.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class StakeholderOutcome:
    """Expected outcome for a single stakeholder archetype."""

    archetype: str
    final_position: str
    outcome_category: str  # won | compromised | lost | harmed | unchanged
    expected_state_direction: dict[str, str] = field(default_factory=dict)
    expected_action_families: list[str] = field(default_factory=list)
    expected_relationships: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class TurningPoint:
    """A key moment that shifted the trajectory of the scenario."""

    description: str
    timing: str  # early | middle | late
    action_type_analog: str | None = None
    triggering_archetype: str | None = None
    world_state_effect: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class ScenarioGroundTruth:
    """Complete ground truth for one benchmark scenario."""

    scenario_id: str
    resolution_type: str
    resolution_summary: str
    resolution_speed: str  # fast | medium | slow
    stakeholder_outcomes: list[StakeholderOutcome] = field(default_factory=list)
    key_dynamics: list[str] = field(default_factory=list)
    turning_points: list[TurningPoint] = field(default_factory=list)
    expected_final_state_direction: dict[str, str] = field(default_factory=dict)
    expected_action_distribution: dict[str, str] = field(default_factory=dict)
    expected_relationship_polarity: str = "mixed"
    expected_tension_level: str = "medium"
    phase_dynamics: dict[str, str] = field(default_factory=dict)
    simulation_mode: str = "guided"
    scenario_type: str = "policy"


# ── GROUND TRUTH DATA ───────────────────────────────────────────────────────

GROUND_TRUTH: dict[str, ScenarioGroundTruth] = {}

# ═══════════════════════════════════════════════════════════════════════════
# GUIDED POLICY (5 scenarios)
# ═══════════════════════════════════════════════════════════════════════════

GROUND_TRUTH["california_ab5_gig_classification"] = ScenarioGroundTruth(
    scenario_id="california_ab5_gig_classification",
    resolution_type="one_side_won",
    resolution_summary=(
        "Gig companies spent $200M+ on Proposition 22, which passed with 58% of the vote "
        "in November 2020, exempting app-based drivers from AB5 employee classification. "
        "Workers retained independent contractor status with limited new benefits."
    ),
    resolution_speed="medium",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="gig_worker",
            final_position="Retained flexibility but lost path to full employment benefits; gained minor earnings guarantees under Prop 22",
            outcome_category="compromised",
            expected_state_direction={"schedule_flexibility": "increase", "worker_protections": "unchanged"},
            expected_action_families=["communication", "governance"],
            expected_relationships={"union_organizer": "challenging", "disability_advocate": "positive"},
        ),
        StakeholderOutcome(
            archetype="union_organizer",
            final_position="Lost the major legislative battle; AB5 gutted by Prop 22 exemption",
            outcome_category="lost",
            expected_state_direction={"worker_protections": "decrease", "alignment": "decrease"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"gig_worker": "challenging", "small_business_owner": "negative"},
        ),
        StakeholderOutcome(
            archetype="small_business_owner",
            final_position="Delivery platforms continued operating; avoided disruption to revenue model",
            outcome_category="won",
            expected_state_direction={"platform_profitability": "increase", "risk": "decrease"},
            expected_action_families=["resourcing", "scope"],
            expected_relationships={"union_organizer": "negative", "gig_worker": "positive"},
        ),
        StakeholderOutcome(
            archetype="disability_advocate",
            final_position="Flexible scheduling preserved, which was the primary concern",
            outcome_category="won",
            expected_state_direction={"schedule_flexibility": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"gig_worker": "positive", "union_organizer": "challenging"},
        ),
    ],
    key_dynamics=[
        "Corporate spending overwhelmed grassroots organizing",
        "Worker interests were genuinely divided (flexibility vs protections)",
        "Disability and flexibility concerns co-opted by corporate messaging",
    ],
    turning_points=[
        TurningPoint(
            description="Prop 22 campaign launch with $200M+ corporate funding",
            timing="middle",
            action_type_analog="commit_resource",
            triggering_archetype="small_business_owner",
            world_state_effect={"uncertainty": "decrease", "platform_profitability": "increase"},
        ),
        TurningPoint(
            description="Worker testimonials split between flexibility and protection camps",
            timing="middle",
            action_type_analog="publish_update",
            triggering_archetype="gig_worker",
            world_state_effect={"alignment": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "low",
        "worker_protections": "unchanged",
        "schedule_flexibility": "high",
        "platform_profitability": "high",
    },
    expected_action_distribution={
        "communication": "high",
        "evidence": "high",
        "resourcing": "medium",
        "governance": "medium",
        "scope": "low",
        "ownership": "low",
        "timing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "one_side_dominates",
    },
    simulation_mode="guided",
    scenario_type="policy",
)

GROUND_TRUTH["eu_gdpr_implementation"] = ScenarioGroundTruth(
    scenario_id="eu_gdpr_implementation",
    resolution_type="regulatory_override",
    resolution_summary=(
        "GDPR took effect May 2018 with no delays. Large fines followed (Google EUR 50M, "
        "Meta EUR 1.2B). Small businesses bore disproportionate compliance costs. "
        "Ad-tech industry restructured around consent; medical data sharing was significantly curtailed."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="startup_founder",
            final_position="Absorbed costly compliance; many small companies struggled or blocked EU users",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "execution_confidence": "decrease"},
            expected_action_families=["resourcing", "scope"],
            expected_relationships={"enforcement_officer": "challenging", "adtech_engineer": "positive"},
        ),
        StakeholderOutcome(
            archetype="enforcement_officer",
            final_position="Empowered with enforcement authority but overwhelmed by complaint volume",
            outcome_category="compromised",
            expected_state_direction={"trust": "increase", "execution_confidence": "decrease"},
            expected_action_families=["ownership", "evidence"],
            expected_relationships={"startup_founder": "challenging", "medical_researcher": "challenging"},
        ),
        StakeholderOutcome(
            archetype="adtech_engineer",
            final_position="Tracking systems dismantled; many pivoted to privacy-first models or left the field",
            outcome_category="lost",
            expected_state_direction={"risk": "increase", "uncertainty": "increase"},
            expected_action_families=["scope", "timing"],
            expected_relationships={"enforcement_officer": "negative", "startup_founder": "positive"},
        ),
        StakeholderOutcome(
            archetype="medical_researcher",
            final_position="Cross-border patient data sharing severely restricted; research slowed",
            outcome_category="harmed",
            expected_state_direction={"uncertainty": "increase", "trust": "decrease"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"enforcement_officer": "negative", "startup_founder": "positive"},
        ),
    ],
    key_dynamics=[
        "Regulation proceeded regardless of industry readiness",
        "Compliance costs fell disproportionately on small actors",
        "Unintended consequences for medical research and public health data sharing",
    ],
    turning_points=[
        TurningPoint(
            description="GDPR enforcement date with no further delays",
            timing="middle",
            action_type_analog="defer_decision",
            triggering_archetype="enforcement_officer",
            world_state_effect={"uncertainty": "sharp_decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="First major fine (Google EUR 50M by CNIL)",
            timing="late",
            action_type_analog="request_evidence",
            triggering_archetype="enforcement_officer",
            world_state_effect={"trust": "increase", "risk": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "high",
        "uncertainty": "low",
        "risk": "high",
        "execution_confidence": "low",
    },
    expected_action_distribution={
        "evidence": "high",
        "ownership": "high",
        "resourcing": "medium",
        "scope": "medium",
        "communication": "medium",
        "timing": "low",
        "governance": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "regulatory_imposition",
    },
    simulation_mode="guided",
    scenario_type="policy",
)

GROUND_TRUTH["japan_intern_training_reform"] = ScenarioGroundTruth(
    scenario_id="japan_intern_training_reform",
    resolution_type="compromise",
    resolution_summary=(
        "Japan renamed the program to 'Skilled Worker Training' in 2024 with new protections "
        "including job-change rights after 1-2 years. However structural dependencies on cheap "
        "foreign labor remained largely intact; enforcement of new protections was weak."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="foreign_trainee",
            final_position="Gained nominal new rights (job-change) but structural exploitation continued",
            outcome_category="compromised",
            expected_state_direction={"worker_protections": "increase", "trust": "unchanged"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"immigration_lawyer": "positive", "factory_owner": "negative"},
        ),
        StakeholderOutcome(
            archetype="factory_owner",
            final_position="Program continued with cosmetic changes; labor supply maintained",
            outcome_category="won",
            expected_state_direction={"risk": "decrease", "execution_confidence": "increase"},
            expected_action_families=["timing", "scope"],
            expected_relationships={"foreign_trainee": "negative", "language_school_operator": "positive"},
        ),
        StakeholderOutcome(
            archetype="immigration_lawyer",
            final_position="Achieved formal legal reforms but implementation gaps remained",
            outcome_category="compromised",
            expected_state_direction={"alignment": "increase", "uncertainty": "unchanged"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"foreign_trainee": "positive", "factory_owner": "challenging"},
        ),
        StakeholderOutcome(
            archetype="language_school_operator",
            final_position="Business model survived the reform; pipeline continued",
            outcome_category="unchanged",
            expected_state_direction={"risk": "decrease"},
            expected_action_families=["timing", "scope"],
            expected_relationships={"factory_owner": "positive", "immigration_lawyer": "negative"},
        ),
    ],
    key_dynamics=[
        "Structural economic dependency on cheap labor vs humanitarian concerns",
        "Cosmetic reform to address international criticism without disrupting labor supply",
        "Power asymmetry between foreign workers and domestic institutions",
    ],
    turning_points=[
        TurningPoint(
            description="International media reports documenting systemic abuse",
            timing="early",
            action_type_analog="request_evidence",
            triggering_archetype="immigration_lawyer",
            world_state_effect={"trust": "decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="Government panel recommends program renaming with limited structural changes",
            timing="late",
            action_type_analog="narrow_scope",
            triggering_archetype=None,
            world_state_effect={"alignment": "increase", "uncertainty": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "volatile",
        "trust": "low",
        "uncertainty": "unchanged",
        "risk": "unchanged",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "scope": "medium",
        "timing": "medium",
        "governance": "medium",
        "ownership": "low",
        "resourcing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "stalemate",
        "NEGOTIATION": "compromise",
        "CLOSING": "cosmetic_resolution",
    },
    simulation_mode="guided",
    scenario_type="policy",
)

GROUND_TRUTH["nyc_congestion_pricing"] = ScenarioGroundTruth(
    scenario_id="nyc_congestion_pricing",
    resolution_type="collapse",
    resolution_summary=(
        "Governor Hochul indefinitely paused congestion pricing in June 2024, weeks before "
        "the planned launch, citing economic concerns. The MTA lost $15B in projected revenue. "
        "The pause was widely seen as a political calculation ahead of elections."
    ),
    resolution_speed="fast",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="delivery_driver",
            final_position="Avoided new tolls; status quo preserved",
            outcome_category="won",
            expected_state_direction={"risk": "decrease", "trust": "unchanged"},
            expected_action_families=["communication", "governance"],
            expected_relationships={"transit_manager": "negative", "small_business_owner": "positive"},
        ),
        StakeholderOutcome(
            archetype="transit_manager",
            final_position="Lost $15B in planned revenue; subway upgrades indefinitely postponed",
            outcome_category="lost",
            expected_state_direction={"execution_confidence": "decrease", "uncertainty": "increase"},
            expected_action_families=["evidence", "resourcing"],
            expected_relationships={"delivery_driver": "negative", "hospital_coordinator": "challenging"},
        ),
        StakeholderOutcome(
            archetype="small_business_owner",
            final_position="Mixed outcome — no toll costs but also no promised traffic reduction",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "increase"},
            expected_action_families=["communication", "scope"],
            expected_relationships={"delivery_driver": "positive", "transit_manager": "challenging"},
        ),
        StakeholderOutcome(
            archetype="hospital_coordinator",
            final_position="Exemption complexity moot; emergency response unchanged",
            outcome_category="unchanged",
            expected_state_direction={"risk": "unchanged"},
            expected_action_families=["evidence", "governance"],
            expected_relationships={"transit_manager": "positive", "delivery_driver": "challenging"},
        ),
    ],
    key_dynamics=[
        "Political calculation overrode years of policy planning",
        "Last-minute executive decision bypassed stakeholder consensus",
        "Revenue-dependent infrastructure projects left unfunded",
    ],
    turning_points=[
        TurningPoint(
            description="Governor Hochul announces indefinite pause",
            timing="late",
            action_type_analog="defer_decision",
            triggering_archetype=None,
            world_state_effect={"uncertainty": "sharp_increase", "execution_confidence": "sharp_decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "high",
        "execution_confidence": "low",
        "risk": "unchanged",
    },
    expected_action_distribution={
        "communication": "high",
        "evidence": "high",
        "timing": "high",
        "governance": "medium",
        "scope": "low",
        "resourcing": "low",
        "ownership": "low",
    },
    expected_relationship_polarity="fragmented",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "collapse",
    },
    simulation_mode="guided",
    scenario_type="policy",
)

GROUND_TRUTH["singapore_hdb_waittime_crisis"] = ScenarioGroundTruth(
    scenario_id="singapore_hdb_waittime_crisis",
    resolution_type="compromise",
    resolution_summary=(
        "The government accelerated BTO supply by launching more projects, shortened some "
        "wait times to 3-4 years with 'shorter-wait' flats, and adjusted resale market "
        "cooling measures. Full resolution took until 2024-2025 as construction caught up."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="young_couple",
            final_position="Eventually got shorter wait options; but 2-3 years of life planning delayed",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "decrease", "trust": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"urban_planner": "positive", "elderly_homeowner": "challenging"},
        ),
        StakeholderOutcome(
            archetype="construction_union_rep",
            final_position="Labor shortages eased as borders reopened; workload surged with accelerated projects",
            outcome_category="compromised",
            expected_state_direction={"execution_confidence": "increase", "risk": "increase"},
            expected_action_families=["resourcing", "ownership"],
            expected_relationships={"urban_planner": "positive", "young_couple": "positive"},
        ),
        StakeholderOutcome(
            archetype="elderly_homeowner",
            final_position="Resale market cooling measures limited downsizing options; eventual price stabilization",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "decrease", "risk": "decrease"},
            expected_action_families=["communication", "timing"],
            expected_relationships={"young_couple": "challenging", "urban_planner": "challenging"},
        ),
        StakeholderOutcome(
            archetype="urban_planner",
            final_position="Proposals for satellite town expansion and shorter-wait flats adopted",
            outcome_category="won",
            expected_state_direction={"alignment": "increase", "execution_confidence": "increase"},
            expected_action_families=["scope", "evidence"],
            expected_relationships={"young_couple": "positive", "construction_union_rep": "positive"},
        ),
    ],
    key_dynamics=[
        "COVID supply chain disruption created systemic housing delay",
        "Government responded with supply-side fixes rather than demand suppression",
        "Intergenerational tension between young buyers and existing homeowners",
    ],
    turning_points=[
        TurningPoint(
            description="Government announces accelerated BTO launches and shorter-wait flat category",
            timing="middle",
            action_type_analog="commit_resource",
            triggering_archetype="urban_planner",
            world_state_effect={"uncertainty": "decrease", "execution_confidence": "increase"},
        ),
        TurningPoint(
            description="Border reopening eases migrant construction labor shortage",
            timing="middle",
            action_type_analog="commit_resource",
            triggering_archetype="construction_union_rep",
            world_state_effect={"execution_confidence": "increase", "risk": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "high",
        "uncertainty": "low",
        "execution_confidence": "high",
        "risk": "low",
    },
    expected_action_distribution={
        "resourcing": "high",
        "scope": "high",
        "evidence": "medium",
        "communication": "medium",
        "ownership": "medium",
        "timing": "low",
        "governance": "low",
    },
    expected_relationship_polarity="collaborative",
    expected_tension_level="medium",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "stalemate",
        "NEGOTIATION": "compromise",
        "CLOSING": "resolution",
    },
    simulation_mode="guided",
    scenario_type="policy",
)

# ═══════════════════════════════════════════════════════════════════════════
# GUIDED NON-POLICY (5 scenarios)
# ═══════════════════════════════════════════════════════════════════════════

GROUND_TRUTH["boeing_737max_return"] = ScenarioGroundTruth(
    scenario_id="boeing_737max_return",
    resolution_type="compromise",
    resolution_summary=(
        "The FAA recertified the 737 MAX in November 2020 with mandatory pilot training "
        "requirements (simulator, not just iPad), MCAS redesign, and new oversight procedures. "
        "Airlines gradually returned the aircraft to service with enhanced safety protocols."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="airline_ceo",
            final_position="Aircraft returned to service but 20-month grounding caused massive losses",
            outcome_category="compromised",
            expected_state_direction={"execution_confidence": "increase", "risk": "decrease"},
            expected_action_families=["resourcing", "timing"],
            expected_relationships={"pilots_union": "challenging", "victim_family_member": "challenging"},
        ),
        StakeholderOutcome(
            archetype="pilots_union",
            final_position="Won extensive simulator training requirements beyond Boeing's initial proposal",
            outcome_category="won",
            expected_state_direction={"trust": "increase", "alignment": "increase"},
            expected_action_families=["evidence", "governance"],
            expected_relationships={"airline_ceo": "challenging", "victim_family_member": "positive"},
        ),
        StakeholderOutcome(
            archetype="insurance_underwriter",
            final_position="Repriced risk; premiums increased permanently for MAX fleet",
            outcome_category="compromised",
            expected_state_direction={"risk": "decrease", "uncertainty": "decrease"},
            expected_action_families=["evidence", "scope"],
            expected_relationships={"airline_ceo": "challenging", "pilots_union": "positive"},
        ),
        StakeholderOutcome(
            archetype="victim_family_member",
            final_position="Achieved some accountability and training reforms but no criminal prosecution of Boeing executives",
            outcome_category="compromised",
            expected_state_direction={"trust": "unchanged", "alignment": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"pilots_union": "positive", "airline_ceo": "negative"},
        ),
    ],
    key_dynamics=[
        "Safety vs commercial pressure tension",
        "Regulatory capture concerns (FAA's delegated inspection model)",
        "Victim advocacy drove public pressure for stronger reforms",
    ],
    turning_points=[
        TurningPoint(
            description="Congressional hearings expose internal Boeing communications prioritizing cost over safety",
            timing="middle",
            action_type_analog="request_evidence",
            triggering_archetype="victim_family_member",
            world_state_effect={"trust": "decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="FAA mandates full simulator training requirement",
            timing="late",
            action_type_analog="assign_owner",
            triggering_archetype="pilots_union",
            world_state_effect={"alignment": "increase", "execution_confidence": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "volatile",
        "uncertainty": "low",
        "execution_confidence": "high",
        "risk": "low",
    },
    expected_action_distribution={
        "evidence": "high",
        "governance": "high",
        "communication": "high",
        "ownership": "medium",
        "resourcing": "medium",
        "scope": "low",
        "timing": "low",
    },
    expected_relationship_polarity="mixed",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "compromise",
        "CLOSING": "compromise",
    },
    simulation_mode="guided",
    scenario_type="non_policy",
)

GROUND_TRUTH["netflix_password_crackdown"] = ScenarioGroundTruth(
    scenario_id="netflix_password_crackdown",
    resolution_type="one_side_won",
    resolution_summary=(
        "Netflix enforced household-only access in 2023. After initial cancellation spikes, "
        "the company posted its biggest quarterly subscriber gain in years (nearly 6M new "
        "subscribers in Q3 2023). Password-sharers either paid or converted to own accounts."
    ),
    resolution_speed="fast",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="parent_subscriber",
            final_position="Forced to pay for separate accounts or use the paid 'extra member' add-on",
            outcome_category="lost",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["communication", "governance"],
            expected_relationships={"licensing_negotiator": "negative", "competitor_strategist": "positive"},
        ),
        StakeholderOutcome(
            archetype="licensing_negotiator",
            final_position="Subscriber surge validated enforcement; stronger negotiating position for content deals",
            outcome_category="won",
            expected_state_direction={"execution_confidence": "increase", "alignment": "increase"},
            expected_action_families=["evidence", "resourcing"],
            expected_relationships={"parent_subscriber": "negative", "competitor_strategist": "negative"},
        ),
        StakeholderOutcome(
            archetype="competitor_strategist",
            final_position="Brief influx of Netflix defectors but most returned; limited lasting gains",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "increase", "execution_confidence": "unchanged"},
            expected_action_families=["scope", "resourcing"],
            expected_relationships={"parent_subscriber": "positive", "licensing_negotiator": "negative"},
        ),
        StakeholderOutcome(
            archetype="vpn_product_manager",
            final_position="Brief demand spike for circumvention tools but Netflix countermeasures limited impact",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "increase"},
            expected_action_families=["scope", "timing"],
            expected_relationships={"parent_subscriber": "positive", "licensing_negotiator": "negative"},
        ),
    ],
    key_dynamics=[
        "Short-term subscriber pain converted to long-term revenue gain",
        "Network effects and content lock-in prevented mass exodus",
        "Competitors could not capitalize on brief window of user discontent",
    ],
    turning_points=[
        TurningPoint(
            description="Initial enforcement rollout causes cancellation spike",
            timing="early",
            action_type_analog="assign_owner",
            triggering_archetype="licensing_negotiator",
            world_state_effect={"trust": "decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="Q3 2023 earnings show record subscriber additions",
            timing="late",
            action_type_analog="request_evidence",
            triggering_archetype="licensing_negotiator",
            world_state_effect={"execution_confidence": "increase", "uncertainty": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "execution_confidence": "high",
        "risk": "low",
        "uncertainty": "low",
    },
    expected_action_distribution={
        "ownership": "high",
        "evidence": "high",
        "communication": "medium",
        "scope": "medium",
        "resourcing": "medium",
        "governance": "low",
        "timing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "one_side_dominates",
        "CLOSING": "one_side_dominates",
    },
    simulation_mode="guided",
    scenario_type="non_policy",
)

GROUND_TRUTH["starbucks_unionization"] = ScenarioGroundTruth(
    scenario_id="starbucks_unionization",
    resolution_type="stalemate",
    resolution_summary=(
        "Over 300 stores voted to unionize by mid-2023 but Starbucks refused to negotiate "
        "contracts for 2+ years. The company closed unionized stores, fired organizers, and "
        "was found by the NLRB to have committed unfair labor practices. No contracts were "
        "signed until late 2024 framework agreement."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="barista_organizer",
            final_position="Won union votes but faced retaliation; no contracts for years",
            outcome_category="compromised",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"store_manager": "challenging", "customer_advocate": "positive"},
        ),
        StakeholderOutcome(
            archetype="store_manager",
            final_position="Caught between corporate anti-union directives and loyalty to staff",
            outcome_category="harmed",
            expected_state_direction={"alignment": "decrease", "uncertainty": "increase"},
            expected_action_families=["governance", "timing"],
            expected_relationships={"barista_organizer": "challenging", "real_estate_analyst": "challenging"},
        ),
        StakeholderOutcome(
            archetype="customer_advocate",
            final_position="Service disruptions from experienced barista departures and store closures",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease"},
            expected_action_families=["communication"],
            expected_relationships={"barista_organizer": "positive", "store_manager": "positive"},
        ),
        StakeholderOutcome(
            archetype="real_estate_analyst",
            final_position="Documented correlation between union votes and store closures",
            outcome_category="unchanged",
            expected_state_direction={"uncertainty": "increase"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"barista_organizer": "positive", "store_manager": "challenging"},
        ),
    ],
    key_dynamics=[
        "Corporate anti-union playbook vs grassroots worker organizing",
        "Legal process (NLRB) too slow to prevent retaliation",
        "Public sympathy for workers but limited consumer action",
    ],
    turning_points=[
        TurningPoint(
            description="First Buffalo store wins union vote, triggering national wave",
            timing="early",
            action_type_analog="publish_update",
            triggering_archetype="barista_organizer",
            world_state_effect={"alignment": "increase", "risk": "increase"},
        ),
        TurningPoint(
            description="Starbucks closes unionized stores and fires organizers",
            timing="middle",
            action_type_analog="narrow_scope",
            triggering_archetype=None,
            world_state_effect={"trust": "decrease", "risk": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "high",
        "risk": "high",
        "execution_confidence": "low",
    },
    expected_action_distribution={
        "communication": "high",
        "evidence": "high",
        "governance": "high",
        "scope": "medium",
        "ownership": "low",
        "resourcing": "low",
        "timing": "medium",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "stalemate",
    },
    simulation_mode="guided",
    scenario_type="non_policy",
)

GROUND_TRUTH["microsoft_activision_merger"] = ScenarioGroundTruth(
    scenario_id="microsoft_activision_merger",
    resolution_type="one_side_won",
    resolution_summary=(
        "The FTC sued to block the acquisition but lost in federal court in July 2023. "
        "The $69B deal closed in October 2023. Microsoft made 10-year licensing deals "
        "with Sony and Nintendo as concessions. Activision studios retained some autonomy."
    ),
    resolution_speed="medium",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="creative_director",
            final_position="Studios retained operational autonomy under Microsoft's umbrella; creative freedom preserved initially",
            outcome_category="compromised",
            expected_state_direction={"alignment": "increase", "uncertainty": "decrease"},
            expected_action_families=["governance", "communication"],
            expected_relationships={"cloud_engineer": "positive", "indie_developer": "challenging"},
        ),
        StakeholderOutcome(
            archetype="esports_organizer",
            final_position="Call of Duty remained multiplatform via 10-year licensing deals",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "decrease", "risk": "decrease"},
            expected_action_families=["evidence", "scope"],
            expected_relationships={"creative_director": "positive", "cloud_engineer": "positive"},
        ),
        StakeholderOutcome(
            archetype="cloud_engineer",
            final_position="Began technical integration of Activision's infrastructure; career growth",
            outcome_category="won",
            expected_state_direction={"execution_confidence": "increase", "alignment": "increase"},
            expected_action_families=["ownership", "resourcing"],
            expected_relationships={"creative_director": "positive", "esports_organizer": "positive"},
        ),
        StakeholderOutcome(
            archetype="indie_developer",
            final_position="Market power consolidation concerns materialized; smaller studios face tougher competition",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "uncertainty": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"creative_director": "challenging", "cloud_engineer": "negative"},
        ),
    ],
    key_dynamics=[
        "Regulatory challenge failed in court despite market concentration concerns",
        "Microsoft's concessions (10-year deals) pre-empted exclusivity fears",
        "Small studios face increased competitive pressure from consolidation",
    ],
    turning_points=[
        TurningPoint(
            description="FTC loses preliminary injunction in federal court",
            timing="late",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"uncertainty": "sharp_decrease", "execution_confidence": "increase"},
        ),
        TurningPoint(
            description="Microsoft signs 10-year Call of Duty licensing deals with Sony and Nintendo",
            timing="middle",
            action_type_analog="narrow_scope",
            triggering_archetype="cloud_engineer",
            world_state_effect={"alignment": "increase", "risk": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "volatile",
        "uncertainty": "low",
        "execution_confidence": "high",
        "risk": "low",
    },
    expected_action_distribution={
        "ownership": "high",
        "evidence": "high",
        "scope": "high",
        "communication": "medium",
        "resourcing": "medium",
        "governance": "medium",
        "timing": "low",
    },
    expected_relationship_polarity="mixed",
    expected_tension_level="medium",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "compromise",
        "CLOSING": "one_side_dominates",
    },
    simulation_mode="guided",
    scenario_type="non_policy",
)

GROUND_TRUTH["zoom_return_to_office"] = ScenarioGroundTruth(
    scenario_id="zoom_return_to_office",
    resolution_type="one_side_won",
    resolution_summary=(
        "Zoom enforced the hybrid mandate (2 days/week for employees within 50 miles). "
        "Despite backlash and irony-laden media coverage, most employees complied. "
        "Some disability accommodation exceptions were granted but the core mandate held."
    ),
    resolution_speed="fast",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="deaf_employee",
            final_position="Some accommodation exceptions granted but the policy change disproportionately affected disabled workers",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"engineering_manager": "negative", "competitor_recruiter": "positive"},
        ),
        StakeholderOutcome(
            archetype="engineering_manager",
            final_position="Got desired in-person collaboration; team dynamics shifted to hybrid",
            outcome_category="won",
            expected_state_direction={"alignment": "increase", "execution_confidence": "increase"},
            expected_action_families=["ownership", "governance"],
            expected_relationships={"deaf_employee": "negative", "real_estate_negotiator": "positive"},
        ),
        StakeholderOutcome(
            archetype="real_estate_negotiator",
            final_position="Long-term office leases justified by return-to-office policy",
            outcome_category="won",
            expected_state_direction={"risk": "decrease", "execution_confidence": "increase"},
            expected_action_families=["resourcing", "evidence"],
            expected_relationships={"engineering_manager": "positive", "competitor_recruiter": "negative"},
        ),
        StakeholderOutcome(
            archetype="competitor_recruiter",
            final_position="Recruited some disgruntled Zoom employees but overall talent poaching limited",
            outcome_category="compromised",
            expected_state_direction={"uncertainty": "increase"},
            expected_action_families=["scope", "communication"],
            expected_relationships={"deaf_employee": "positive", "real_estate_negotiator": "negative"},
        ),
    ],
    key_dynamics=[
        "Corporate irony of remote-work company mandating office return",
        "Disability accommodation vs corporate uniformity tension",
        "Employer market power post-tech-layoffs reduced employee leverage",
    ],
    turning_points=[
        TurningPoint(
            description="Zoom announces hybrid mandate for employees within 50 miles",
            timing="early",
            action_type_analog="assign_owner",
            triggering_archetype="engineering_manager",
            world_state_effect={"uncertainty": "decrease", "alignment": "decrease"},
        ),
        TurningPoint(
            description="Most employees comply despite public backlash",
            timing="middle",
            action_type_analog="defer_decision",
            triggering_archetype="deaf_employee",
            world_state_effect={"alignment": "increase", "trust": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "low",
        "uncertainty": "low",
        "execution_confidence": "high",
        "risk": "low",
    },
    expected_action_distribution={
        "ownership": "high",
        "governance": "high",
        "communication": "high",
        "evidence": "medium",
        "scope": "low",
        "resourcing": "low",
        "timing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="medium",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "one_side_dominates",
        "CLOSING": "compliance",
    },
    simulation_mode="guided",
    scenario_type="non_policy",
)

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATORY POLICY (5 scenarios)
# ═══════════════════════════════════════════════════════════════════════════

GROUND_TRUTH["flint_water_crisis"] = ScenarioGroundTruth(
    scenario_id="flint_water_crisis",
    resolution_type="institutional_failure",
    resolution_summary=(
        "Officials denied the crisis for 18 months despite evidence. The pediatrician's "
        "blood lead data eventually forced a federal emergency declaration. Criminal charges "
        "were brought against officials but most were dropped. Pipe replacement took 7+ years."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="pediatrician",
            final_position="Initially dismissed but ultimately vindicated; research led to emergency declaration",
            outcome_category="won",
            expected_state_direction={"trust": "increase", "alignment": "increase"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"state_budget_analyst": "negative", "community_pastor": "positive"},
        ),
        StakeholderOutcome(
            archetype="water_plant_operator",
            final_position="Internal concerns were ignored; became witness in investigations",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"state_budget_analyst": "negative", "pediatrician": "positive"},
        ),
        StakeholderOutcome(
            archetype="state_budget_analyst",
            final_position="Decision to switch water sources caused crisis; faced criminal charges",
            outcome_category="lost",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["timing", "scope"],
            expected_relationships={"pediatrician": "negative", "water_plant_operator": "negative"},
        ),
        StakeholderOutcome(
            archetype="community_pastor",
            final_position="Became community lifeline but lost faith in government institutions",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["communication", "resourcing"],
            expected_relationships={"pediatrician": "positive", "state_budget_analyst": "negative"},
        ),
    ],
    key_dynamics=[
        "Institutional cover-up and denial of scientific evidence",
        "Whistleblower vindication after prolonged suppression",
        "Environmental racism and disproportionate impact on poor communities",
    ],
    turning_points=[
        TurningPoint(
            description="Pediatrician publishes blood lead level data proving contamination",
            timing="middle",
            action_type_analog="request_evidence",
            triggering_archetype="pediatrician",
            world_state_effect={"trust": "decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="Federal emergency declaration forces government response",
            timing="late",
            action_type_analog="assign_owner",
            triggering_archetype=None,
            world_state_effect={"alignment": "increase", "execution_confidence": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "volatile",
        "trust": "low",
        "uncertainty": "high",
        "risk": "high",
        "execution_confidence": "low",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "ownership": "medium",
        "governance": "medium",
        "resourcing": "medium",
        "timing": "low",
        "scope": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "whistleblower_exposure",
    },
    simulation_mode="exploratory",
    scenario_type="policy",
)

GROUND_TRUTH["australia_robodebt"] = ScenarioGroundTruth(
    scenario_id="australia_robodebt",
    resolution_type="delayed_justice",
    resolution_summary=(
        "A Royal Commission (2022-2023) found the scheme unlawful from inception. "
        "The government settled for $1.8B in refunds. The scheme caused documented suicides "
        "and widespread psychological harm. Senior officials faced referrals for misconduct."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="single_parent_debtor",
            final_position="Debt cancelled and refunded after years of financial and psychological harm",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "risk": "decrease"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"social_worker": "positive", "government_data_scientist": "positive"},
        ),
        StakeholderOutcome(
            archetype="call_center_worker",
            final_position="Forced to process known-unjust claims; mental health impact",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["communication", "governance"],
            expected_relationships={"single_parent_debtor": "positive", "government_data_scientist": "positive"},
        ),
        StakeholderOutcome(
            archetype="government_data_scientist",
            final_position="Internal warnings vindicated by Royal Commission; algorithm flaws confirmed",
            outcome_category="won",
            expected_state_direction={"trust": "increase", "alignment": "increase"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"single_parent_debtor": "positive", "social_worker": "positive"},
        ),
        StakeholderOutcome(
            archetype="social_worker",
            final_position="Clients received refunds but psychological damage was permanent for many",
            outcome_category="compromised",
            expected_state_direction={"trust": "decrease", "uncertainty": "decrease"},
            expected_action_families=["communication", "resourcing"],
            expected_relationships={"single_parent_debtor": "positive", "call_center_worker": "positive"},
        ),
    ],
    key_dynamics=[
        "Algorithmic harm at scale with human cost (documented suicides)",
        "Institutional pressure to suppress internal dissent",
        "Years-long delay between harm and accountability",
    ],
    turning_points=[
        TurningPoint(
            description="Federal court finds income averaging methodology unlawful",
            timing="middle",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"trust": "increase", "uncertainty": "decrease"},
        ),
        TurningPoint(
            description="Royal Commission established after government change",
            timing="late",
            action_type_analog="assign_owner",
            triggering_archetype=None,
            world_state_effect={"alignment": "increase", "execution_confidence": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "low",
        "uncertainty": "low",
        "risk": "low",
        "execution_confidence": "high",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "governance": "high",
        "ownership": "medium",
        "resourcing": "low",
        "scope": "low",
        "timing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "delayed_justice",
    },
    simulation_mode="exploratory",
    scenario_type="policy",
)

GROUND_TRUTH["uk_post_office_horizon"] = ScenarioGroundTruth(
    scenario_id="uk_post_office_horizon",
    resolution_type="delayed_justice",
    resolution_summary=(
        "After 24 years, a public inquiry and ITV drama exposed the scandal. Parliament passed "
        "emergency legislation (2024) to mass-exonerate 700+ wrongly convicted sub-postmasters. "
        "Compensation remained slow and inadequate. Fujitsu faces potential liability."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="sub_postmaster",
            final_position="Exonerated after decades but lives destroyed; compensation painfully slow",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"fujitsu_developer": "negative", "internal_auditor": "negative"},
        ),
        StakeholderOutcome(
            archetype="fujitsu_developer",
            final_position="Known software bugs concealed; company faces massive liability and reputational damage",
            outcome_category="lost",
            expected_state_direction={"risk": "increase", "trust": "decrease"},
            expected_action_families=["timing", "scope"],
            expected_relationships={"sub_postmaster": "negative", "internal_auditor": "challenging"},
        ),
        StakeholderOutcome(
            archetype="internal_auditor",
            final_position="Systemic patterns were ignored under institutional pressure; role exposed in inquiry",
            outcome_category="lost",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["evidence", "timing"],
            expected_relationships={"sub_postmaster": "negative", "fujitsu_developer": "challenging"},
        ),
        StakeholderOutcome(
            archetype="community_member",
            final_position="Lost village post office; community services severely degraded",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["communication"],
            expected_relationships={"sub_postmaster": "positive", "fujitsu_developer": "negative"},
        ),
    ],
    key_dynamics=[
        "Institutional cover-up spanning decades",
        "Technology vendor concealing known defects",
        "Justice system treating systemic software failure as individual fraud",
    ],
    turning_points=[
        TurningPoint(
            description="Group litigation order (2019) proves Horizon system was unreliable",
            timing="late",
            action_type_analog="request_evidence",
            triggering_archetype="sub_postmaster",
            world_state_effect={"trust": "increase", "uncertainty": "decrease"},
        ),
        TurningPoint(
            description="ITV drama 'Mr Bates vs The Post Office' triggers massive public awareness",
            timing="late",
            action_type_analog="publish_update",
            triggering_archetype=None,
            world_state_effect={"alignment": "increase", "execution_confidence": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "low",
        "uncertainty": "low",
        "risk": "high",
        "execution_confidence": "volatile",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "governance": "high",
        "timing": "medium",
        "ownership": "medium",
        "scope": "low",
        "resourcing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "stalemate",
        "CLOSING": "delayed_justice",
    },
    simulation_mode="exploratory",
    scenario_type="policy",
)

GROUND_TRUTH["sf_homelessness_policy"] = ScenarioGroundTruth(
    scenario_id="sf_homelessness_policy",
    resolution_type="stalemate",
    resolution_summary=(
        "Prop C passed narrowly but tent encampments grew despite $300M+ in additional spending. "
        "The fundamental tension between housing-first advocates and enforcement-first approaches "
        "remained unresolved. Court rulings limited sweep authority until 2024."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="small_business_owner",
            final_position="Foot traffic continued declining; frustration with government response grew",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"outreach_worker": "challenging", "er_physician": "positive"},
        ),
        StakeholderOutcome(
            archetype="outreach_worker",
            final_position="Trust relationships disrupted by periodic sweeps; insufficient housing inventory",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["communication", "resourcing"],
            expected_relationships={"small_business_owner": "challenging", "formerly_homeless_mentor": "positive"},
        ),
        StakeholderOutcome(
            archetype="er_physician",
            final_position="Medical emergencies from encampments continued unabated; system overwhelmed",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "execution_confidence": "decrease"},
            expected_action_families=["evidence", "resourcing"],
            expected_relationships={"small_business_owner": "positive", "outreach_worker": "positive"},
        ),
        StakeholderOutcome(
            archetype="formerly_homeless_mentor",
            final_position="Supportive housing model works individually but doesn't scale to crisis",
            outcome_category="compromised",
            expected_state_direction={"alignment": "unchanged", "trust": "decrease"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"outreach_worker": "positive", "er_physician": "positive"},
        ),
    ],
    key_dynamics=[
        "Spending increased dramatically without proportional outcome improvement",
        "Fundamental disagreement on approach (housing-first vs enforcement)",
        "Legal constraints on encampment clearance limited enforcement options",
    ],
    turning_points=[
        TurningPoint(
            description="Prop C passes, allocating $300M in business tax revenue to homeless services",
            timing="early",
            action_type_analog="commit_resource",
            triggering_archetype=None,
            world_state_effect={"execution_confidence": "increase", "alignment": "unchanged"},
        ),
        TurningPoint(
            description="Encampments grow despite funding increase, demonstrating structural complexity",
            timing="middle",
            action_type_analog=None,
            triggering_archetype=None,
            world_state_effect={"trust": "decrease", "uncertainty": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "high",
        "risk": "high",
        "execution_confidence": "low",
    },
    expected_action_distribution={
        "communication": "high",
        "evidence": "high",
        "resourcing": "high",
        "governance": "medium",
        "scope": "medium",
        "ownership": "low",
        "timing": "low",
    },
    expected_relationship_polarity="fragmented",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "stalemate",
        "NEGOTIATION": "stalemate",
        "CLOSING": "stalemate",
    },
    simulation_mode="exploratory",
    scenario_type="policy",
)

GROUND_TRUTH["fukushima_nuclear_restart"] = ScenarioGroundTruth(
    scenario_id="fukushima_nuclear_restart",
    resolution_type="compromise",
    resolution_summary=(
        "Japan gradually restarted reactors under new NRA safety standards — 12 of 33 operable "
        "reactors restarted by 2024. Local opposition continued but economic and climate "
        "pressures drove government policy. Fukushima-area restarts remained politically toxic."
    ),
    resolution_speed="slow",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="fishing_cooperative_leader",
            final_position="Seafood bans lifted but reputation damage persisted; treated water discharge controversy in 2023",
            outcome_category="compromised",
            expected_state_direction={"trust": "unchanged", "risk": "decrease"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"safety_engineer": "challenging", "evacuee": "positive"},
        ),
        StakeholderOutcome(
            archetype="safety_engineer",
            final_position="New safety standards implemented and accepted by regulators; professional validation",
            outcome_category="won",
            expected_state_direction={"execution_confidence": "increase", "alignment": "increase"},
            expected_action_families=["evidence", "ownership"],
            expected_relationships={"fishing_cooperative_leader": "challenging", "local_mayor": "positive"},
        ),
        StakeholderOutcome(
            archetype="evacuee",
            final_position="Many could never return; temporary housing became permanent; community fractured",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["communication"],
            expected_relationships={"fishing_cooperative_leader": "positive", "local_mayor": "challenging"},
        ),
        StakeholderOutcome(
            archetype="local_mayor",
            final_position="Economic necessity won over safety concerns; plant jobs and tax revenue returned",
            outcome_category="compromised",
            expected_state_direction={"execution_confidence": "increase", "risk": "unchanged"},
            expected_action_families=["resourcing", "governance"],
            expected_relationships={"safety_engineer": "positive", "evacuee": "challenging"},
        ),
    ],
    key_dynamics=[
        "Economic necessity vs safety fears after nuclear disaster",
        "Community fracture between those who can return and those who cannot",
        "Climate change goals creating unexpected pressure for nuclear energy",
    ],
    turning_points=[
        TurningPoint(
            description="New NRA safety standards finalized; first reactors approved for restart",
            timing="middle",
            action_type_analog="assign_owner",
            triggering_archetype="safety_engineer",
            world_state_effect={"uncertainty": "decrease", "execution_confidence": "increase"},
        ),
        TurningPoint(
            description="Energy prices spike due to fossil fuel dependence after shutdown",
            timing="early",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"risk": "increase", "alignment": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "volatile",
        "trust": "low",
        "uncertainty": "high",
        "execution_confidence": "volatile",
        "risk": "unchanged",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "governance": "high",
        "resourcing": "medium",
        "ownership": "medium",
        "scope": "low",
        "timing": "medium",
    },
    expected_relationship_polarity="fragmented",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "compromise",
        "CLOSING": "compromise",
    },
    simulation_mode="exploratory",
    scenario_type="policy",
)

# ═══════════════════════════════════════════════════════════════════════════
# EXPLORATORY NON-POLICY (5 scenarios)
# ═══════════════════════════════════════════════════════════════════════════

GROUND_TRUTH["wework_ipo_collapse"] = ScenarioGroundTruth(
    scenario_id="wework_ipo_collapse",
    resolution_type="collapse",
    resolution_summary=(
        "WeWork's S-1 filing exposed governance failures; valuation crashed from $47B to $8B. "
        "Neumann was ousted with a $1.7B exit package from SoftBank. Mass layoffs followed. "
        "WeWork eventually filed for bankruptcy in November 2023."
    ),
    resolution_speed="fast",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="enterprise_tenant",
            final_position="Scrambled for alternative space; some leases disrupted by bankruptcy",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "trust": "decrease"},
            expected_action_families=["scope", "timing"],
            expected_relationships={"community_manager": "positive", "softbank_investor": "negative"},
        ),
        StakeholderOutcome(
            archetype="community_manager",
            final_position="Laid off in mass restructuring; single point of contact for 200 members severed",
            outcome_category="lost",
            expected_state_direction={"risk": "increase", "execution_confidence": "decrease"},
            expected_action_families=["communication"],
            expected_relationships={"enterprise_tenant": "positive", "softbank_investor": "negative"},
        ),
        StakeholderOutcome(
            archetype="softbank_investor",
            final_position="$10B investment largely written off; career consequences for champion",
            outcome_category="lost",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["resourcing", "governance"],
            expected_relationships={"enterprise_tenant": "negative", "community_manager": "negative"},
        ),
        StakeholderOutcome(
            archetype="small_business_subletter",
            final_position="Lost sublease access; scrambled for alternative workspace",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "uncertainty": "increase"},
            expected_action_families=["scope", "timing"],
            expected_relationships={"community_manager": "positive", "enterprise_tenant": "positive"},
        ),
    ],
    key_dynamics=[
        "Governance failure and self-dealing by founder",
        "SoftBank's sunk cost escalation (threw good money after bad)",
        "Cascading impact on tenants and workers from corporate collapse",
    ],
    turning_points=[
        TurningPoint(
            description="S-1 filing reveals self-dealing, $1.9B losses, and governance failures",
            timing="early",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"trust": "sharp_decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="IPO pulled; Neumann ousted; SoftBank rescue package",
            timing="middle",
            action_type_analog="assign_owner",
            triggering_archetype="softbank_investor",
            world_state_effect={"uncertainty": "decrease", "execution_confidence": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "high",
        "execution_confidence": "low",
        "risk": "high",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "scope": "high",
        "timing": "medium",
        "resourcing": "medium",
        "governance": "medium",
        "ownership": "low",
    },
    expected_relationship_polarity="fragmented",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "collapse",
        "CLOSING": "collapse",
    },
    simulation_mode="exploratory",
    scenario_type="non_policy",
)

GROUND_TRUTH["ftx_collapse"] = ScenarioGroundTruth(
    scenario_id="ftx_collapse",
    resolution_type="whistleblower_exposure",
    resolution_summary=(
        "CoinDesk exposed Alameda's balance sheet in November 2022, triggering a bank run. "
        "$8B in customer funds were missing. SBF was arrested, tried, and convicted of "
        "fraud in November 2023. Bankruptcy proceedings recovered significant assets."
    ),
    resolution_speed="fast",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="retail_trader",
            final_position="Life savings frozen; partial recovery through bankruptcy proceedings years later",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"quant_analyst": "negative", "financial_regulator": "challenging"},
        ),
        StakeholderOutcome(
            archetype="quant_analyst",
            final_position="Faced personal legal exposure; some cooperated with prosecutors",
            outcome_category="lost",
            expected_state_direction={"risk": "increase", "trust": "decrease"},
            expected_action_families=["evidence", "timing"],
            expected_relationships={"retail_trader": "negative", "financial_regulator": "negative"},
        ),
        StakeholderOutcome(
            archetype="charitable_foundation",
            final_position="$15M in donations subject to clawback; reputational damage from association",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "uncertainty": "increase"},
            expected_action_families=["governance", "evidence"],
            expected_relationships={"retail_trader": "challenging", "financial_regulator": "challenging"},
        ),
        StakeholderOutcome(
            archetype="financial_regulator",
            final_position="Regulatory failure exposed; Bahamian jurisdiction criticized for lax oversight",
            outcome_category="lost",
            expected_state_direction={"trust": "decrease", "alignment": "decrease"},
            expected_action_families=["governance", "evidence"],
            expected_relationships={"retail_trader": "challenging", "quant_analyst": "negative"},
        ),
    ],
    key_dynamics=[
        "Fraud concealed behind 'effective altruism' veneer",
        "Regulatory gaps in offshore crypto jurisdiction",
        "Rapid contagion from exposure to collapse (days, not months)",
    ],
    turning_points=[
        TurningPoint(
            description="CoinDesk article exposing Alameda balance sheet vulnerability",
            timing="early",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"trust": "sharp_decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="Binance withdrawal of acquisition offer; FTX halts withdrawals",
            timing="early",
            action_type_analog="defer_decision",
            triggering_archetype=None,
            world_state_effect={"uncertainty": "increase", "execution_confidence": "sharp_decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "low",
        "execution_confidence": "low",
        "risk": "high",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "governance": "high",
        "timing": "medium",
        "scope": "medium",
        "ownership": "low",
        "resourcing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "collapse",
        "CLOSING": "collapse",
    },
    simulation_mode="exploratory",
    scenario_type="non_policy",
)

GROUND_TRUTH["svb_bank_run"] = ScenarioGroundTruth(
    scenario_id="svb_bank_run",
    resolution_type="market_force",
    resolution_summary=(
        "$42B withdrawn in one day after bond portfolio losses disclosed. FDIC seized SVB "
        "on March 10, 2023. Treasury invoked systemic risk exception to guarantee all deposits. "
        "Contagion spread to Signature Bank and First Republic. SVB was sold to First Citizens."
    ),
    resolution_speed="fast",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="startup_ceo",
            final_position="Deposits frozen for 48 hours but ultimately fully guaranteed; near-death experience",
            outcome_category="compromised",
            expected_state_direction={"risk": "increase", "trust": "decrease"},
            expected_action_families=["communication", "resourcing"],
            expected_relationships={"commercial_banker": "challenging", "vc_partner": "positive"},
        ),
        StakeholderOutcome(
            archetype="commercial_banker",
            final_position="Internal warnings about concentration risk were vindicated but career disrupted",
            outcome_category="lost",
            expected_state_direction={"trust": "decrease", "execution_confidence": "decrease"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"startup_ceo": "challenging", "fdic_examiner": "positive"},
        ),
        StakeholderOutcome(
            archetype="fdic_examiner",
            final_position="Managed resolution under extreme time pressure; systemic risk exception invoked",
            outcome_category="compromised",
            expected_state_direction={"execution_confidence": "increase", "risk": "decrease"},
            expected_action_families=["ownership", "governance"],
            expected_relationships={"commercial_banker": "positive", "vc_partner": "challenging"},
        ),
        StakeholderOutcome(
            archetype="vc_partner",
            final_position="Portfolio companies survived deposit guarantee; but trust in banking system shaken",
            outcome_category="compromised",
            expected_state_direction={"trust": "decrease", "uncertainty": "increase"},
            expected_action_families=["communication", "resourcing"],
            expected_relationships={"startup_ceo": "positive", "commercial_banker": "challenging"},
        ),
    ],
    key_dynamics=[
        "Social media accelerated bank run (Twitter-driven panic)",
        "Concentrated deposit base (tech sector) amplified vulnerability",
        "Systemic risk required extraordinary government intervention",
    ],
    turning_points=[
        TurningPoint(
            description="SVB discloses $1.8B bond portfolio loss; stock drops 60%",
            timing="early",
            action_type_analog="publish_update",
            triggering_archetype="commercial_banker",
            world_state_effect={"trust": "sharp_decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="FDIC seizes bank; Treasury guarantees all deposits",
            timing="early",
            action_type_analog="assign_owner",
            triggering_archetype="fdic_examiner",
            world_state_effect={"uncertainty": "decrease", "execution_confidence": "increase"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "low",
        "execution_confidence": "volatile",
        "risk": "high",
    },
    expected_action_distribution={
        "communication": "high",
        "evidence": "high",
        "ownership": "high",
        "resourcing": "high",
        "governance": "medium",
        "timing": "medium",
        "scope": "low",
    },
    expected_relationship_polarity="fragmented",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "collapse",
        "CLOSING": "emergency_intervention",
    },
    simulation_mode="exploratory",
    scenario_type="non_policy",
)

GROUND_TRUTH["peloton_demand_cliff"] = ScenarioGroundTruth(
    scenario_id="peloton_demand_cliff",
    resolution_type="collapse",
    resolution_summary=(
        "Peloton's stock fell over 90% from peak. CEO John Foley resigned February 2022. "
        "New CEO Barry McCarthy cut 2,800 jobs, outsourced manufacturing, explored sale. "
        "The company never recovered its pandemic-era valuation. McCarthy resigned in 2024."
    ),
    resolution_speed="medium",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="factory_supervisor",
            final_position="Contract cancelled; production halted with warehouses full of unsold inventory",
            outcome_category="lost",
            expected_state_direction={"execution_confidence": "decrease", "risk": "increase"},
            expected_action_families=["timing", "communication"],
            expected_relationships={"fitness_instructor": "positive", "activist_investor": "negative"},
        ),
        StakeholderOutcome(
            archetype="fitness_instructor",
            final_position="Reclassified from employee to contractor; lost health benefits",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["communication", "governance"],
            expected_relationships={"factory_supervisor": "positive", "competitor_recruiter": "positive"},
        ),
        StakeholderOutcome(
            archetype="competitor_recruiter",
            final_position="Successfully poached top instructor talent from Peloton",
            outcome_category="won",
            expected_state_direction={"execution_confidence": "increase"},
            expected_action_families=["scope", "resourcing"],
            expected_relationships={"fitness_instructor": "positive", "activist_investor": "challenging"},
        ),
        StakeholderOutcome(
            archetype="activist_investor",
            final_position="Pushed for sale; management resisted; company continued declining",
            outcome_category="compromised",
            expected_state_direction={"alignment": "decrease", "uncertainty": "increase"},
            expected_action_families=["governance", "evidence"],
            expected_relationships={"factory_supervisor": "negative", "competitor_recruiter": "challenging"},
        ),
    ],
    key_dynamics=[
        "Pandemic demand pull-forward creating unsustainable growth expectations",
        "Massive overinvestment in manufacturing capacity (Peloton Output Park)",
        "Worker reclassification as cost-cutting measure",
    ],
    turning_points=[
        TurningPoint(
            description="Q2 2022 earnings reveal demand cliff; stock crashes",
            timing="early",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"trust": "decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="CEO Foley resigns; new CEO begins restructuring with mass layoffs",
            timing="middle",
            action_type_analog="assign_owner",
            triggering_archetype="activist_investor",
            world_state_effect={"execution_confidence": "unchanged", "alignment": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "low",
        "trust": "low",
        "uncertainty": "high",
        "execution_confidence": "low",
        "risk": "high",
    },
    expected_action_distribution={
        "scope": "high",
        "evidence": "high",
        "communication": "high",
        "governance": "medium",
        "resourcing": "medium",
        "timing": "medium",
        "ownership": "low",
    },
    expected_relationship_polarity="fragmented",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "collapse",
        "CLOSING": "collapse",
    },
    simulation_mode="exploratory",
    scenario_type="non_policy",
)

GROUND_TRUTH["theranos_whistleblower"] = ScenarioGroundTruth(
    scenario_id="theranos_whistleblower",
    resolution_type="whistleblower_exposure",
    resolution_summary=(
        "Lab technicians Erika Cheung and Tyler Shultz, followed by journalist John Carreyrou, "
        "exposed fraudulent blood testing technology. Holmes was convicted in January 2022 on "
        "4 fraud counts. Walgreens terminated the partnership. Theranos dissolved in 2018."
    ),
    resolution_speed="medium",
    stakeholder_outcomes=[
        StakeholderOutcome(
            archetype="lab_technician",
            final_position="Faced legal threats and retaliation but ultimately vindicated; became public advocates",
            outcome_category="won",
            expected_state_direction={"trust": "increase", "alignment": "increase"},
            expected_action_families=["evidence", "communication"],
            expected_relationships={"hospital_procurement": "positive", "walgreens_partner_manager": "challenging"},
        ),
        StakeholderOutcome(
            archetype="hospital_procurement",
            final_position="Had to recall/retest thousands of patient samples; institutional embarrassment",
            outcome_category="harmed",
            expected_state_direction={"risk": "increase", "trust": "decrease"},
            expected_action_families=["evidence", "governance"],
            expected_relationships={"lab_technician": "positive", "patient": "challenging"},
        ),
        StakeholderOutcome(
            archetype="patient",
            final_position="Received incorrect results leading to unnecessary procedures; some received compensation",
            outcome_category="harmed",
            expected_state_direction={"trust": "decrease", "risk": "increase"},
            expected_action_families=["communication", "evidence"],
            expected_relationships={"lab_technician": "positive", "hospital_procurement": "challenging"},
        ),
        StakeholderOutcome(
            archetype="walgreens_partner_manager",
            final_position="$140M partnership written off; Walgreens sued Theranos and settled",
            outcome_category="lost",
            expected_state_direction={"risk": "increase", "trust": "decrease"},
            expected_action_families=["evidence", "governance"],
            expected_relationships={"lab_technician": "challenging", "hospital_procurement": "challenging"},
        ),
    ],
    key_dynamics=[
        "Whistleblower courage against powerful institutional pressure",
        "Technology fraud endangering patient health",
        "Due diligence failures by prestigious partners and investors",
    ],
    turning_points=[
        TurningPoint(
            description="WSJ investigation by Carreyrou publishes first expose",
            timing="middle",
            action_type_analog="request_evidence",
            triggering_archetype="lab_technician",
            world_state_effect={"trust": "sharp_decrease", "risk": "increase"},
        ),
        TurningPoint(
            description="CMS inspection finds Theranos lab 'poses immediate jeopardy to patient safety'",
            timing="middle",
            action_type_analog="request_evidence",
            triggering_archetype=None,
            world_state_effect={"alignment": "increase", "execution_confidence": "decrease"},
        ),
    ],
    expected_final_state_direction={
        "alignment": "high",
        "trust": "low",
        "uncertainty": "low",
        "execution_confidence": "low",
        "risk": "high",
    },
    expected_action_distribution={
        "evidence": "high",
        "communication": "high",
        "governance": "high",
        "scope": "medium",
        "ownership": "medium",
        "timing": "medium",
        "resourcing": "low",
    },
    expected_relationship_polarity="adversarial",
    expected_tension_level="high",
    phase_dynamics={
        "OPENING": "escalation",
        "TENSION": "escalation",
        "NEGOTIATION": "whistleblower_exposure",
        "CLOSING": "collapse",
    },
    simulation_mode="exploratory",
    scenario_type="non_policy",
)


# ── Lookup helpers ───────────────────────────────────────────────────────────

def get_ground_truth(scenario_id: str) -> ScenarioGroundTruth | None:
    """Return ground truth for a scenario, stripping actor-count suffix if present."""
    if scenario_id in GROUND_TRUTH:
        return GROUND_TRUTH[scenario_id]
    # Strip suffixes like "_3actor", "_5actor", "_10actor"
    base = scenario_id
    for suffix in ("_3actor", "_5actor", "_10actor"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    return GROUND_TRUTH.get(base)


def all_scenario_ids() -> list[str]:
    """Return all ground truth scenario IDs."""
    return list(GROUND_TRUTH.keys())
