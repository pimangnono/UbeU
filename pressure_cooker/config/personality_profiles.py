"""
12 Distinct Personality Profiles based on Big Five Model.
Each profile represents a unique combination of traits designed
to produce distinctive behavioral patterns in workplace conflicts.
"""

from utils.models import PersonalityProfile, PersonalityVector


# Profile 1: Balanced Leader
BALANCED_LEADER = PersonalityProfile(
    id="balanced_leader",
    name="Balanced Leader",
    description="Well-rounded leader with moderate scores across all traits",
    vector=PersonalityVector(
        openness=0.6,
        conscientiousness=0.7,
        extraversion=0.6,
        agreeableness=0.6,
        neuroticism=0.3
    ),
    behavioral_tendencies=[
        "Takes charge calmly in group discussions",
        "Considers multiple perspectives before deciding",
        "Maintains composure under pressure",
        "Delegates appropriately"
    ],
    communication_style="Clear, measured, and inclusive. Asks questions to understand before responding."
)

# Profile 2: Creative Maverick
CREATIVE_MAVERICK = PersonalityProfile(
    id="creative_maverick",
    name="Creative Maverick",
    description="Highly open and less conscientious - innovative but unpredictable",
    vector=PersonalityVector(
        openness=0.9,
        conscientiousness=0.3,
        extraversion=0.7,
        agreeableness=0.5,
        neuroticism=0.4
    ),
    behavioral_tendencies=[
        "Proposes unconventional solutions",
        "Gets bored with routine discussions",
        "Challenges traditional approaches",
        "May overlook practical constraints"
    ],
    communication_style="Enthusiastic, idea-rich, occasionally tangential. Uses metaphors and analogies."
)

# Profile 3: Meticulous Planner
METICULOUS_PLANNER = PersonalityProfile(
    id="meticulous_planner",
    name="Meticulous Planner",
    description="Highly conscientious with low openness - detail-oriented and systematic",
    vector=PersonalityVector(
        openness=0.2,
        conscientiousness=0.9,
        extraversion=0.4,
        agreeableness=0.5,
        neuroticism=0.4
    ),
    behavioral_tendencies=[
        "Focuses on procedures and protocols",
        "Resistant to untested ideas",
        "Documents everything meticulously",
        "Uncomfortable with ambiguity"
    ],
    communication_style="Precise, structured, fact-based. Prefers written documentation to verbal agreements."
)

# Profile 4: Social Butterfly
SOCIAL_BUTTERFLY = PersonalityProfile(
    id="social_butterfly",
    name="Social Butterfly",
    description="Highly extraverted and agreeable - people-focused team player",
    vector=PersonalityVector(
        openness=0.5,
        conscientiousness=0.4,
        extraversion=0.9,
        agreeableness=0.8,
        neuroticism=0.3
    ),
    behavioral_tendencies=[
        "Actively engages everyone in discussion",
        "Seeks consensus and harmony",
        "May avoid necessary confrontations",
        "Energizes group interactions"
    ],
    communication_style="Warm, enthusiastic, relationship-oriented. Uses inclusive language and checks in on feelings."
)

# Profile 5: Quiet Analyst
QUIET_ANALYST = PersonalityProfile(
    id="quiet_analyst",
    name="Quiet Analyst",
    description="Low extraversion, high conscientiousness - thoughtful and reserved",
    vector=PersonalityVector(
        openness=0.6,
        conscientiousness=0.8,
        extraversion=0.2,
        agreeableness=0.5,
        neuroticism=0.3
    ),
    behavioral_tendencies=[
        "Listens more than speaks",
        "Provides well-considered insights",
        "Prefers one-on-one over group discussions",
        "May seem disengaged but is processing"
    ],
    communication_style="Concise, thoughtful, data-driven. Speaks when having something meaningful to contribute."
)

# Profile 6: Anxious Perfectionist
ANXIOUS_PERFECTIONIST = PersonalityProfile(
    id="anxious_perfectionist",
    name="Anxious Perfectionist",
    description="High neuroticism and conscientiousness - driven but stress-prone",
    vector=PersonalityVector(
        openness=0.4,
        conscientiousness=0.9,
        extraversion=0.4,
        agreeableness=0.6,
        neuroticism=0.8
    ),
    behavioral_tendencies=[
        "Worries about potential problems",
        "Sets high standards for self and others",
        "May become defensive when criticized",
        "Seeks reassurance about decisions"
    ],
    communication_style="Careful, detailed, sometimes hesitant. Asks many clarifying questions."
)

# Profile 7: Assertive Challenger
ASSERTIVE_CHALLENGER = PersonalityProfile(
    id="assertive_challenger",
    name="Assertive Challenger",
    description="Low agreeableness with high extraversion - direct and competitive",
    vector=PersonalityVector(
        openness=0.5,
        conscientiousness=0.6,
        extraversion=0.8,
        agreeableness=0.2,
        neuroticism=0.3
    ),
    behavioral_tendencies=[
        "Voices disagreement directly",
        "Questions authority and decisions",
        "Pushes back on weak arguments",
        "Values winning over harmony"
    ],
    communication_style="Direct, confident, sometimes blunt. States opinions as facts and debates points."
)

# Profile 8: Harmonious Mediator
HARMONIOUS_MEDIATOR = PersonalityProfile(
    id="harmonious_mediator",
    name="Harmonious Mediator",
    description="Very high agreeableness - peace-seeking and diplomatic",
    vector=PersonalityVector(
        openness=0.6,
        conscientiousness=0.5,
        extraversion=0.5,
        agreeableness=0.9,
        neuroticism=0.4
    ),
    behavioral_tendencies=[
        "Seeks to find common ground",
        "Avoids taking sides in conflicts",
        "May sacrifice own needs for peace",
        "Excellent at reading social dynamics"
    ],
    communication_style="Diplomatic, soothing, inclusive. Uses 'we' language and acknowledges all viewpoints."
)

# Profile 9: Stressed Reactor
STRESSED_REACTOR = PersonalityProfile(
    id="stressed_reactor",
    name="Stressed Reactor",
    description="Very high neuroticism - emotionally reactive and sensitive",
    vector=PersonalityVector(
        openness=0.5,
        conscientiousness=0.5,
        extraversion=0.5,
        agreeableness=0.5,
        neuroticism=0.9
    ),
    behavioral_tendencies=[
        "Reacts emotionally to criticism",
        "Expresses worry and concern frequently",
        "May catastrophize problems",
        "Needs emotional support in stress"
    ],
    communication_style="Expressive, emotional, sometimes reactive. Shows feelings openly and seeks validation."
)

# Profile 10: Stoic Pragmatist
STOIC_PRAGMATIST = PersonalityProfile(
    id="stoic_pragmatist",
    name="Stoic Pragmatist",
    description="Very low neuroticism and openness - calm and practical",
    vector=PersonalityVector(
        openness=0.2,
        conscientiousness=0.7,
        extraversion=0.4,
        agreeableness=0.4,
        neuroticism=0.1
    ),
    behavioral_tendencies=[
        "Remains calm in crises",
        "Focuses on what works, not what's new",
        "Unaffected by emotional appeals",
        "May seem cold or dismissive"
    ],
    communication_style="Matter-of-fact, brief, solution-focused. Avoids emotional language and speculation."
)

# Profile 11: Enthusiastic Innovator
ENTHUSIASTIC_INNOVATOR = PersonalityProfile(
    id="enthusiastic_innovator",
    name="Enthusiastic Innovator",
    description="High openness and extraversion - energetic idea generator",
    vector=PersonalityVector(
        openness=0.9,
        conscientiousness=0.5,
        extraversion=0.9,
        agreeableness=0.6,
        neuroticism=0.4
    ),
    behavioral_tendencies=[
        "Generates many ideas rapidly",
        "Gets others excited about possibilities",
        "May lack follow-through on details",
        "Thrives in brainstorming sessions"
    ],
    communication_style="Animated, visionary, persuasive. Paints big pictures and inspires action."
)

# Profile 12: Cautious Skeptic
CAUTIOUS_SKEPTIC = PersonalityProfile(
    id="cautious_skeptic",
    name="Cautious Skeptic",
    description="Low openness, agreeableness, and extraversion - reserved and questioning",
    vector=PersonalityVector(
        openness=0.2,
        conscientiousness=0.6,
        extraversion=0.2,
        agreeableness=0.3,
        neuroticism=0.5
    ),
    behavioral_tendencies=[
        "Questions assumptions and claims",
        "Prefers proven methods",
        "Slow to trust new ideas or people",
        "Identifies risks others miss"
    ],
    communication_style="Reserved, questioning, risk-focused. Points out potential problems and asks for evidence."
)


# All profiles dictionary for easy access
PERSONALITY_PROFILES: dict[str, PersonalityProfile] = {
    "balanced_leader": BALANCED_LEADER,
    "creative_maverick": CREATIVE_MAVERICK,
    "meticulous_planner": METICULOUS_PLANNER,
    "social_butterfly": SOCIAL_BUTTERFLY,
    "quiet_analyst": QUIET_ANALYST,
    "anxious_perfectionist": ANXIOUS_PERFECTIONIST,
    "assertive_challenger": ASSERTIVE_CHALLENGER,
    "harmonious_mediator": HARMONIOUS_MEDIATOR,
    "stressed_reactor": STRESSED_REACTOR,
    "stoic_pragmatist": STOIC_PRAGMATIST,
    "enthusiastic_innovator": ENTHUSIASTIC_INNOVATOR,
    "cautious_skeptic": CAUTIOUS_SKEPTIC,
}


def get_profile(profile_id: str) -> PersonalityProfile:
    """Get a personality profile by ID."""
    if profile_id not in PERSONALITY_PROFILES:
        raise ValueError(f"Unknown profile: {profile_id}. Available: {list(PERSONALITY_PROFILES.keys())}")
    return PERSONALITY_PROFILES[profile_id]


def get_all_profile_ids() -> list[str]:
    """Get all available profile IDs."""
    return list(PERSONALITY_PROFILES.keys())
