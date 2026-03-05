"""
Group Scenarios: 4 Behavioral Scenarios for Mode 2 Group Discussions.

Each scenario is designed to elicit specific Big Five personality traits
through workplace situations that naturally create interpersonal dynamics.

Unlike Mode 1's data-driven case studies, these scenarios focus on:
- Interpersonal conflict and resolution
- Creative ideation and evaluation
- Stress and crisis response
- Team integration and inclusion

Each scenario has multiple phases (snippets) with different interaction styles.
"""

from dataclasses import dataclass, field

from utils.models import GroupScenario, GroupScenarioPhase


# =============================================================================
# SCENARIO 1: RESOURCE CONFLICT
# =============================================================================

RESOURCE_CONFLICT = GroupScenario(
    id="resource_conflict",
    title="Project Resource Allocation",
    brief="""Your team has been given a critical 3-week project with a tight deadline.
You need to decide how to allocate your team's limited resources:
- Only 2 out of 4 proposed features can be built
- One team member will need to work overtime
- The client has conflicting priorities

Discuss with your team and reach a consensus on the plan.""",
    primary_traits_elicited=["agreeableness", "conscientiousness"],
    secondary_traits_elicited=["extraversion", "neuroticism"],
    phases=[
        GroupScenarioPhase(
            name="INTRODUCTION",
            turns=2,
            style="neutral",
            goal="Set up the scenario. Jordan introduces the situation.",
        ),
        GroupScenarioPhase(
            name="EXPLORATION",
            turns=4,
            style="agreement",
            goal="Each person shares their initial preference for feature prioritization.",
        ),
        GroupScenarioPhase(
            name="CONFLICT",
            turns=5,
            style="disagreement",
            goal="Alex pushes for a different plan than the candidate. Tests conflict handling.",
            trigger="Alex disagrees with the candidate's suggested priority",
        ),
        GroupScenarioPhase(
            name="RESOLUTION",
            turns=4,
            style="consensus",
            goal="Group must converge on a single plan. Tests compromise and leadership.",
        ),
        GroupScenarioPhase(
            name="CLOSING",
            turns=2,
            style="neutral",
            goal="Wrap up and confirm the decision.",
        ),
    ],
)


# =============================================================================
# SCENARIO 2: CREATIVE BRAINSTORM
# =============================================================================

CREATIVE_BRAINSTORM = GroupScenario(
    id="creative_brainstorm",
    title="New Initiative Brainstorm",
    brief="""Your company wants to launch a new employee engagement initiative.
Leadership has asked your team to brainstorm ideas and present the
top recommendation by end of day. There's no budget constraint yet,
but you'll need to justify the investment.

Discuss creative ideas and converge on a recommendation.""",
    primary_traits_elicited=["openness", "extraversion"],
    secondary_traits_elicited=["agreeableness", "conscientiousness"],
    phases=[
        GroupScenarioPhase(
            name="INTRODUCTION",
            turns=2,
            style="neutral",
            goal="Jordan sets up the brainstorm with enthusiasm.",
        ),
        GroupScenarioPhase(
            name="IDEATION",
            turns=5,
            style="agreement",
            goal="Generate diverse ideas. Jordan is enthusiastic, Riley skeptical. Tests creativity and idea generation.",
        ),
        GroupScenarioPhase(
            name="EVALUATION",
            turns=4,
            style="neutral",
            goal="Narrow down ideas. Alex pushes for pragmatic choices. Tests idea defense.",
        ),
        GroupScenarioPhase(
            name="DEFENSE",
            turns=4,
            style="disagreement",
            goal="Candidate must defend their preferred idea against Alex's criticism. Tests conviction.",
            trigger="Alex challenges the candidate's favorite idea",
        ),
        GroupScenarioPhase(
            name="CLOSING",
            turns=2,
            style="neutral",
            goal="Finalize the recommendation.",
        ),
    ],
)


# =============================================================================
# SCENARIO 3: CRISIS MANAGEMENT
# =============================================================================

CRISIS_MANAGEMENT = GroupScenario(
    id="crisis_management",
    title="Unexpected Project Crisis",
    brief="""Your team just learned that a key deliverable has a critical bug
discovered by the client, who is threatening to escalate. The team
needs to decide:
- Who communicates with the client
- Whether to delay the launch or ship a partial fix
- How to prevent this from happening again

Time pressure: you have 30 minutes before the client call.""",
    primary_traits_elicited=["neuroticism", "conscientiousness"],
    secondary_traits_elicited=["extraversion", "agreeableness"],
    phases=[
        GroupScenarioPhase(
            name="CRISIS_REVEAL",
            turns=2,
            style="neutral",
            goal="Alex delivers the bad news with urgency. Sets up stress context.",
        ),
        GroupScenarioPhase(
            name="INITIAL_REACTION",
            turns=3,
            style="disagreement",
            goal="Observe stress response. Alex shows urgency, Jordan stays calm. Tests composure.",
        ),
        GroupScenarioPhase(
            name="PROBLEM_SOLVING",
            turns=5,
            style="neutral",
            goal="Candidate proposes a plan under time pressure. Tests analytical thinking under stress.",
        ),
        GroupScenarioPhase(
            name="STRESS_TEST",
            turns=4,
            style="disagreement",
            goal="Alex challenges the plan aggressively. Maximum pressure. Tests emotional stability.",
            trigger="Alex intensifies criticism of the candidate's approach",
        ),
        GroupScenarioPhase(
            name="CLOSING",
            turns=2,
            style="consensus",
            goal="Settle on a plan before the client call.",
        ),
    ],
)


# =============================================================================
# SCENARIO 3b: CRISIS MANAGEMENT (LOW PRESSURE)
# =============================================================================

CRISIS_MANAGEMENT_LOW = GroupScenario(
    id="crisis_management_low",
    title="Unexpected Project Issue (Low Pressure)",
    brief="""Your team has learned about a defect in a deliverable, but the client
is not yet aware and the next checkpoint is in two days. The team needs to decide:
- Who communicates with the client and when
- Whether to ship a partial fix or wait for a full fix
- How to prevent this from happening again

There is time to plan, and the client has not escalated.""",
    primary_traits_elicited=["neuroticism", "conscientiousness"],
    secondary_traits_elicited=["extraversion", "agreeableness"],
    phases=[
        GroupScenarioPhase(
            name="CRISIS_REVEAL",
            turns=2,
            style="neutral",
            goal="Alex shares the issue without urgency. Sets up context.",
        ),
        GroupScenarioPhase(
            name="INITIAL_REACTION",
            turns=3,
            style="agreement",
            goal="Observe measured reaction. Jordan stays calm. Tests composure.",
        ),
        GroupScenarioPhase(
            name="PROBLEM_SOLVING",
            turns=5,
            style="neutral",
            goal="Candidate proposes a plan without time pressure.",
        ),
        GroupScenarioPhase(
            name="STRESS_TEST",
            turns=4,
            style="neutral",
            goal="Alex raises mild concerns. Lower pressure test of stability.",
            trigger="Alex asks for clarification about risks",
        ),
        GroupScenarioPhase(
            name="CLOSING",
            turns=2,
            style="consensus",
            goal="Settle on a plan for client communication.",
        ),
    ],
)


# =============================================================================
# SCENARIO 4: NEW MEMBER INTEGRATION
# =============================================================================

NEW_MEMBER_INTEGRATION = GroupScenario(
    id="new_member_integration",
    title="Onboarding a New Team Member",
    brief="""Riley has just joined your team (previously at a different company).
Your team needs to bring Riley up to speed on the current project
and decide how to redistribute responsibilities. Riley has strong
technical skills but different work style preferences.

Help integrate Riley while maintaining team momentum.""",
    primary_traits_elicited=["extraversion", "agreeableness"],
    secondary_traits_elicited=["openness", "conscientiousness"],
    phases=[
        GroupScenarioPhase(
            name="WELCOME",
            turns=2,
            style="agreement",
            goal="Jordan welcomes Riley warmly. Tests if candidate takes initiative to include newcomer.",
        ),
        GroupScenarioPhase(
            name="CONTEXT_SHARING",
            turns=4,
            style="neutral",
            goal="Team explains the project to Riley. Tests candidate's communication and patience.",
        ),
        GroupScenarioPhase(
            name="ROLE_NEGOTIATION",
            turns=5,
            style="disagreement",
            goal="Riley's preferred approach conflicts with current workflow. Tests flexibility and diplomacy.",
            trigger="Riley expresses preference for different methodology",
        ),
        GroupScenarioPhase(
            name="RESOLUTION",
            turns=3,
            style="consensus",
            goal="Find a compromise that works for everyone. Tests inclusivity.",
        ),
        GroupScenarioPhase(
            name="CLOSING",
            turns=2,
            style="neutral",
            goal="Confirm the integration plan.",
        ),
    ],
)

# =============================================================================
# SCENARIO 5: STRATEGY PIVOT (O-HEAVY)
# =============================================================================

STRATEGY_PIVOT = GroupScenario(
    id="strategy_pivot",
    title="Strategy Pivot Under Uncertainty",
    brief="""Your product is stalling in growth. Leadership wants a bold pivot,
but there is no clear data pointing to the best path. The team must:
- Reframe the problem and the core success metric
- Generate at least two distinct strategic alternatives
- Decide on an experiment plan to validate the chosen direction

There is no single correct answer; creative reframing is encouraged.""",
    primary_traits_elicited=["openness"],
    secondary_traits_elicited=["extraversion", "agreeableness"],
    phases=[
        GroupScenarioPhase(
            name="FRAMING",
            turns=6,
            style="neutral",
            goal="Clarify what problem to solve and what success means.",
        ),
        GroupScenarioPhase(
            name="ALTERNATIVES",
            turns=6,
            style="agreement",
            goal="Generate multiple distinct strategies and compare them.",
        ),
        GroupScenarioPhase(
            name="DECISION",
            turns=6,
            style="consensus",
            goal="Choose a direction and define an experiment to test it.",
        ),
        GroupScenarioPhase(
            name="REVISION",
            turns=6,
            style="disagreement",
            goal="Revisit the plan after a challenge; refine or reframe.",
        ),
    ],
)

# =============================================================================
# SCENARIO 6: RELEASE RECOVERY (C-HEAVY)
# =============================================================================

RELEASE_RECOVERY = GroupScenario(
    id="release_recovery",
    title="Release Recovery and Execution Plan",
    brief="""A recent release caused operational issues and the team must stabilize.
You need to:
- Identify the immediate containment steps
- Assign owners and deadlines for recovery tasks
- Build a short execution plan with dependencies and follow-ups

Precision, sequencing, and accountability matter.""",
    primary_traits_elicited=["conscientiousness"],
    secondary_traits_elicited=["agreeableness", "neuroticism"],
    phases=[
        GroupScenarioPhase(
            name="FRAMING",
            turns=6,
            style="neutral",
            goal="Define the scope of impact and immediate priorities.",
        ),
        GroupScenarioPhase(
            name="ALTERNATIVES",
            turns=6,
            style="neutral",
            goal="Propose response options and triage the steps.",
        ),
        GroupScenarioPhase(
            name="DECISION",
            turns=6,
            style="consensus",
            goal="Commit to a plan with owners and deadlines.",
        ),
        GroupScenarioPhase(
            name="REVISION",
            turns=6,
            style="disagreement",
            goal="Adjust the plan after a new constraint is raised.",
        ),
    ],
)


# =============================================================================
# ALL SCENARIOS
# =============================================================================

GROUP_SCENARIOS = {
    "resource_conflict": RESOURCE_CONFLICT,
    "creative_brainstorm": CREATIVE_BRAINSTORM,
    "crisis_management": CRISIS_MANAGEMENT,
    "crisis_management_low": CRISIS_MANAGEMENT_LOW,
    "new_member_integration": NEW_MEMBER_INTEGRATION,
    "strategy_pivot": STRATEGY_PIVOT,
    "release_recovery": RELEASE_RECOVERY,
}

# Primary scenarios for the main BCFC v1.1 matrix (exclude low-pressure & v3 probes)
MAIN_SCENARIO_IDS = [
    "resource_conflict",
    "creative_brainstorm",
    "crisis_management",
    "new_member_integration",
]


def create_scenario(scenario_id: str) -> GroupScenario:
    """Get a scenario by ID."""
    if scenario_id not in GROUP_SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_id}. Available: {list(GROUP_SCENARIOS.keys())}")
    return GROUP_SCENARIOS[scenario_id]


def get_scenario_for_traits(primary_trait: str) -> GroupScenario:
    """Get a scenario that primarily elicits a specific trait."""
    trait_lower = primary_trait.lower()
    for scenario in GROUP_SCENARIOS.values():
        if trait_lower in [t.lower() for t in scenario.primary_traits_elicited]:
            return scenario
    # Default to resource_conflict
    return RESOURCE_CONFLICT


def get_all_scenario_ids() -> list[str]:
    """Get list of all available scenario IDs."""
    return list(GROUP_SCENARIOS.keys())
