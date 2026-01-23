"""
4 Workplace Conflict Scenarios for Pressure Cooker Simulations.
Each scenario is designed to elicit personality-consistent responses
through realistic workplace tensions.
"""

from utils.models import ScenarioConfig


# Scenario 1: Resource Conflict
RESOURCE_CONFLICT = ScenarioConfig(
    id="resource_conflict",
    name="Resource Allocation Conflict",
    description="Team members compete for limited budget and personnel resources for their projects.",
    context="""You are in a project planning meeting with your colleagues. The company has
announced budget cuts, and your team must decide how to allocate the remaining resources
among three competing projects. Each person has a stake in different projects, and there
isn't enough budget to fully fund all of them. The deadline for the decision is end of today.""",
    conflict_point="""The Provoker strongly believes their project should get priority funding
because it has the nearest deadline and existing client commitments. They see any delay as
potentially damaging to the company's reputation.""",
    provoker_goal="""Push for your project to receive the majority of resources. Challenge
any alternative proposals and emphasize the urgency of your deadlines. Create pressure by
highlighting negative consequences of not prioritizing your work.""",
    mediator_goal="""Find a balanced solution that considers all projects. Encourage
discussion of trade-offs and look for creative resource-sharing arrangements. Keep the
conversation productive even when tensions rise.""",
    escalation_triggers=[
        "Someone dismisses another's project as less important",
        "Accusations of self-interest or unfairness",
        "Threats to escalate to management",
        "Bringing up past failures or mistakes"
    ],
    resolution_paths=[
        "Phased allocation approach",
        "Shared resources with rotating priority",
        "Scope reduction across all projects",
        "Seeking additional resources from other departments"
    ],
    turn_limit=30,
    min_turns=15
)


# Scenario 2: Credit Attribution Dispute
CREDIT_DISPUTE = ScenarioConfig(
    id="credit_dispute",
    name="Project Credit Attribution",
    description="Disagreement about who deserves credit for a successful project outcome.",
    context="""A major project has just been completed successfully, and management wants to
recognize the key contributors in the upcoming company meeting. However, there's disagreement
about who contributed most significantly. The team is meeting to discuss how credit should
be attributed before management makes any announcements.""",
    conflict_point="""The Provoker believes they did the majority of critical work and feels
others are trying to claim undeserved credit. They have specific examples of their
contributions and feel strongly about being recognized appropriately.""",
    provoker_goal="""Ensure your contributions are properly recognized. Point out specific
work you did that others may be overlooking. Push back if you feel others are
over-claiming their involvement.""",
    mediator_goal="""Help the team fairly acknowledge everyone's contributions. Look for
ways to recognize different types of contributions (leadership, execution, support).
Prevent the discussion from becoming personal attacks.""",
    escalation_triggers=[
        "Minimizing someone's contributions",
        "Questioning the quality of someone's work",
        "Suggesting someone took credit for others' work",
        "Bringing up compensation or promotion implications"
    ],
    resolution_paths=[
        "Collaborative recognition statement",
        "Role-specific acknowledgments",
        "Letting management decide based on documented contributions",
        "Focus on team success rather than individual credit"
    ],
    turn_limit=30,
    min_turns=15
)


# Scenario 3: Process Change Resistance
PROCESS_CHANGE = ScenarioConfig(
    id="process_change",
    name="New Process Implementation",
    description="Resistance to a new workflow or tool being introduced to the team.",
    context="""Management has decided to implement a new project management system that will
significantly change how the team works. Some team members see this as an opportunity for
improvement, while others view it as unnecessary disruption. The team is meeting to discuss
the implementation approach and timeline.""",
    conflict_point="""The Provoker strongly opposes the new system, seeing it as management
imposing unnecessary change without understanding the team's actual needs. They worry about
productivity loss during transition and question whether the benefits justify the disruption.""",
    provoker_goal="""Express concerns about the new system and resist rushed implementation.
Challenge assumptions about its benefits. Push for maintaining current processes or at
minimum, a much slower transition timeline.""",
    mediator_goal="""Bridge the gap between change advocates and skeptics. Acknowledge valid
concerns while highlighting potential benefits. Look for compromise on implementation
timeline and training support.""",
    escalation_triggers=[
        "Dismissing concerns as resistance to change",
        "Implying someone is not adaptable",
        "Bringing up past failed changes",
        "Questioning competence with new tools"
    ],
    resolution_paths=[
        "Phased rollout with pilot group",
        "Extended parallel running period",
        "Additional training and support resources",
        "Feedback mechanism for ongoing improvements"
    ],
    turn_limit=30,
    min_turns=15
)


# Scenario 4: Deadline Pressure
DEADLINE_PRESSURE = ScenarioConfig(
    id="deadline_pressure",
    name="Impossible Deadline",
    description="Team faces an unrealistic deadline and must decide how to respond.",
    context="""The team has just been informed that a major deliverable deadline has been
moved up by two weeks due to client demands. The original timeline was already tight, and
this change seems impossible to meet without significant sacrifices. The team must decide
how to respond to this pressure.""",
    conflict_point="""The Provoker believes the team should push back on the deadline and
communicate that it's unrealistic. They see accepting impossible timelines as setting a
bad precedent and potentially leading to burnout or quality issues.""",
    provoker_goal="""Advocate for pushing back on the deadline or clearly communicating
what trade-offs will be necessary. Challenge any suggestions to just 'work harder' and
highlight the risks of rushed delivery.""",
    mediator_goal="""Help the team find a realistic path forward. Explore options for
scope reduction, additional resources, or managed expectations. Keep focus on solutions
rather than blame.""",
    escalation_triggers=[
        "Suggesting someone isn't committed enough",
        "Blaming poor planning on specific individuals",
        "Dismissing concerns about quality or burnout",
        "Implying someone can't handle pressure"
    ],
    resolution_paths=[
        "Scope negotiation with stakeholders",
        "Phased delivery approach",
        "Temporary resource augmentation",
        "Clear communication of risks and trade-offs"
    ],
    turn_limit=30,
    min_turns=15
)


# All scenarios dictionary
SCENARIOS: dict[str, ScenarioConfig] = {
    "resource_conflict": RESOURCE_CONFLICT,
    "credit_dispute": CREDIT_DISPUTE,
    "process_change": PROCESS_CHANGE,
    "deadline_pressure": DEADLINE_PRESSURE,
}


def get_scenario(scenario_id: str) -> ScenarioConfig:
    """Get a scenario by ID."""
    if scenario_id not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_id}. Available: {list(SCENARIOS.keys())}")
    return SCENARIOS[scenario_id]


def get_all_scenario_ids() -> list[str]:
    """Get all available scenario IDs."""
    return list(SCENARIOS.keys())
