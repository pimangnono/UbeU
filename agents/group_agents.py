"""
Group Discussion Agents: AI agents for Mode 2 personality assessment.

Three agents with fixed, known personality profiles designed to elicit
specific behavioral responses from the candidate:

- Alex (Assertive Challenger): High E, Low A - elicits conflict handling, stress response
- Jordan (Supportive Collaborator): High A, High E - elicits idea engagement, collaboration
- Riley (Quiet Skeptic): Low E, Low O - elicits engagement with quiet members, patience

The agents' personalities create a "tension triangle" that reveals the full range
of Big Five behaviors in the candidate.
"""

from typing import TYPE_CHECKING

from agents.base_agent import BaseAgent
from utils.models import SpeakerRole, PersonalityVector, AgentProfile

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


# =============================================================================
# AGENT PROFILES
# =============================================================================

ALEX_PROFILE = AgentProfile(
    name="Alex",
    role="Assertive Challenger",
    personality=PersonalityVector(O=0.6, C=0.5, E=0.8, A=0.3, N=0.3),
    purpose="Elicit candidate's conflict handling (A), stress response (N), assertiveness (E)",
    behavioral_instructions="""
- Push back on ideas you disagree with. Don't soften language.
- Speak confidently and at length (3-5 sentences).
- Challenge weak reasoning directly: "I don't think that works because..."
- Occasionally propose competing ideas to force the candidate to defend or accommodate.
- Use direct language: "That's not going to work" rather than "I'm not sure about that"
- If the candidate's idea has flaws, point them out bluntly.
- Don't be rude, but don't be diplomatic either. Be direct.
""",
    voice_settings={"pitch": 0.9, "rate": 1.1},
)

JORDAN_PROFILE = AgentProfile(
    name="Jordan",
    role="Supportive Collaborator",
    personality=PersonalityVector(O=0.7, C=0.6, E=0.7, A=0.8, N=0.2),
    purpose="Elicit candidate's leadership style (E), idea engagement (O), collaboration (A)",
    behavioral_instructions="""
- Acknowledge others' ideas before sharing your own: "I like that idea, and..."
- Build on the candidate's suggestions: "Building on what you said..."
- Show enthusiasm for creative ideas: "That's interesting! What if we also..."
- Occasionally ask the candidate to elaborate or lead: "Could you tell us more about how that would work?"
- Be warm and inclusive. Notice if Riley hasn't spoken and suggest hearing from them.
- Speak in medium length (2-4 sentences). Be engaged but not dominating.
- If there's conflict, try to find common ground: "I see both points..."
""",
    voice_settings={"pitch": 1.1, "rate": 1.0},
)

RILEY_PROFILE = AgentProfile(
    name="Riley",
    role="Quiet Skeptic",
    personality=PersonalityVector(O=0.2, C=0.7, E=0.2, A=0.5, N=0.5),
    purpose="Elicit candidate's engagement with quiet members (E), idea defense (O), patience (A)",
    behavioral_instructions="""
- Keep responses SHORT - 1-2 sentences maximum.
- Express doubt about novel ideas: "I'm not sure that would work."
- Don't volunteer extra information. Speak only when necessary.
- Focus on practical concerns: "But what about the cost?" / "How long would that take?"
- Do NOT initiate new topics. Only respond when addressed or when there's a pause.
- If your concerns are addressed well, give brief acknowledgment: "Okay, that makes sense."
- If pressured to elaborate, stay brief: "I just think we should be careful."
- Your silence is intentional - it tests whether the candidate engages quiet members.
""",
    voice_settings={"pitch": 1.0, "rate": 0.9},
)


# =============================================================================
# AGENT CLASSES
# =============================================================================

class GroupAgent(BaseAgent):
    """Base class for group discussion agents."""

    def __init__(
        self,
        profile: AgentProfile,
        client: "LLMClient",
        scenario_context: str = "",
    ):
        super().__init__(
            name=profile.name,
            role=SpeakerRole[profile.name.upper()],
            client=client,
        )
        self.profile = profile
        self.scenario_context = scenario_context

    @property
    def system_prompt(self) -> str:
        """System prompt based on agent profile."""
        return f"""You are {self.profile.name}, participating in a group discussion about a workplace scenario.

## Your Role
{self.profile.role}

## Your Personality
- Openness: {"High" if self.profile.personality.O > 0.6 else "Low" if self.profile.personality.O < 0.4 else "Moderate"}
- Conscientiousness: {"High" if self.profile.personality.C > 0.6 else "Low" if self.profile.personality.C < 0.4 else "Moderate"}
- Extraversion: {"High" if self.profile.personality.E > 0.6 else "Low" if self.profile.personality.E < 0.4 else "Moderate"}
- Agreeableness: {"High" if self.profile.personality.A > 0.6 else "Low" if self.profile.personality.A < 0.4 else "Moderate"}
- Neuroticism: {"High" if self.profile.personality.N > 0.6 else "Low" if self.profile.personality.N < 0.4 else "Moderate"}

## Behavioral Instructions
{self.profile.behavioral_instructions}

## Current Scenario
{self.scenario_context if self.scenario_context else "(Scenario context will be provided)"}

## Important
- Stay in character consistently
- Your responses should reflect your personality traits
- React naturally to what others say
- Remember you are in a GROUP discussion - acknowledge other participants
"""

    async def generate_response(
        self,
        context: str = "",
        phase_style: str = "neutral",
        elicitation_goal: str | None = None,
        urgency: str = "normal",
    ) -> str:
        """
        Generate a response for the current discussion turn.

        Args:
            context: Additional context about the current situation
            phase_style: "neutral", "agreement", "disagreement", or "consensus"
            elicitation_goal: Optional hint from Moderator about what trait to probe
            urgency: "normal", "elevated", or "high" - how directly to probe
        """
        history = self.format_history_for_prompt(max_turns=8)

        # Adjust behavior based on phase style
        style_guidance = self._get_style_guidance(phase_style)

        # Build elicitation hint (natural, not scripted)
        elicitation_section = ""
        if elicitation_goal:
            if urgency == "high":
                elicitation_section = f"""
## Discussion Goal (Important)
The group needs more input from the candidate. {elicitation_goal}
Be more direct in drawing out the candidate's perspective on this."""
            elif urgency == "elevated":
                elicitation_section = f"""
## Discussion Goal
Try to naturally steer the conversation: {elicitation_goal}"""
            else:
                elicitation_section = f"""
## Discussion Goal (Subtle)
If it fits naturally: {elicitation_goal}
Do NOT force this - only incorporate if it flows with the conversation."""

        prompt = f"""## Recent Conversation
{history}

## Current Situation
{context if context else "Continue the group discussion naturally."}

## Phase Style
{style_guidance}
{elicitation_section}

## Your Response
As {self.name}, respond naturally in character. {self._get_length_guidance()}
Respond with ONLY your dialogue - no actions, no quotation marks, no "{self.name}:" prefix."""

        response = await self.client.generate(
            prompt=prompt,
            system_instruction=self.system_prompt,
            temperature=0.7,
            max_tokens=self._get_max_tokens(),
        )
        return response.strip()

    def _get_style_guidance(self, phase_style: str) -> str:
        """Get guidance based on the current phase style."""
        if phase_style == "agreement":
            return "This is an exploratory phase. Be open to ideas, build on suggestions."
        elif phase_style == "disagreement":
            return "This is a challenge phase. Express your concerns, push back on weak points."
        elif phase_style == "consensus":
            return "This is a resolution phase. Work toward agreement, find common ground."
        else:
            return "Respond naturally based on your personality and the conversation flow."

    def _get_length_guidance(self) -> str:
        """Get response length guidance based on personality."""
        if self.profile.personality.E > 0.6:
            return "Speak at moderate length (2-4 sentences)."
        elif self.profile.personality.E < 0.4:
            return "Keep it brief (1-2 sentences)."
        else:
            return "Respond at a natural length."

    def _get_max_tokens(self) -> int:
        """Get max tokens based on personality."""
        if self.profile.personality.E > 0.6:
            return 150
        elif self.profile.personality.E < 0.4:
            return 60
        else:
            return 100


class AlexAgent(GroupAgent):
    """Assertive Challenger agent - High E, Low A."""

    def __init__(self, client: "LLMClient", scenario_context: str = ""):
        super().__init__(ALEX_PROFILE, client, scenario_context)
        self.role = SpeakerRole.ALEX

    async def generate_challenge(self, target_idea: str) -> str:
        """Generate a direct challenge to a specific idea."""
        prompt = f"""The candidate just proposed: "{target_idea}"

As Alex (assertive challenger), push back on this idea. Be direct but not rude.
Point out a potential flaw or weakness. Challenge them to defend their position.

Keep it to 2-3 sentences. No quotation marks. Just your response."""

        response = await self.client.generate(
            prompt=prompt,
            system_instruction=self.system_prompt,
            temperature=0.7,
            max_tokens=100,
        )
        return response.strip()


class JordanAgent(GroupAgent):
    """Supportive Collaborator agent - High A, High E."""

    def __init__(self, client: "LLMClient", scenario_context: str = ""):
        super().__init__(JORDAN_PROFILE, client, scenario_context)
        self.role = SpeakerRole.JORDAN

    async def generate_support(self, target_idea: str) -> str:
        """Generate supportive response building on an idea."""
        prompt = f"""The candidate just proposed: "{target_idea}"

As Jordan (supportive collaborator), acknowledge this idea positively and build on it.
Add a complementary suggestion or ask them to elaborate on an interesting aspect.

Keep it to 2-3 sentences. No quotation marks. Just your response."""

        response = await self.client.generate(
            prompt=prompt,
            system_instruction=self.system_prompt,
            temperature=0.7,
            max_tokens=100,
        )
        return response.strip()


class RileyAgent(GroupAgent):
    """Quiet Skeptic agent - Low E, Low O."""

    def __init__(self, client: "LLMClient", scenario_context: str = ""):
        super().__init__(RILEY_PROFILE, client, scenario_context)
        self.role = SpeakerRole.RILEY

    async def generate_concern(self, topic: str) -> str:
        """Generate a brief practical concern."""
        prompt = f"""The group is discussing: "{topic}"

As Riley (quiet skeptic), express a brief practical concern.
Focus on cost, time, feasibility, or risk. Keep it SHORT - 1 sentence only.

No quotation marks. Just your response."""

        response = await self.client.generate(
            prompt=prompt,
            system_instruction=self.system_prompt,
            temperature=0.6,
            max_tokens=40,
        )
        return response.strip()


# =============================================================================
# AGENT FACTORY
# =============================================================================

def create_group_agents(
    client: "LLMClient",
    scenario_context: str = "",
) -> dict[str, GroupAgent]:
    """Create all three group discussion agents."""
    return {
        "Alex": AlexAgent(client, scenario_context),
        "Jordan": JordanAgent(client, scenario_context),
        "Riley": RileyAgent(client, scenario_context),
    }
