"""
Colleague Agents for Pressure Cooker Framework.
Provoker creates tension, Mediator seeks resolution.
Both are designed to elicit personality-revealing responses from the Candidate.
"""

from typing import TYPE_CHECKING

from agents.base_agent import BaseAgent
from utils.models import ScenarioConfig, SpeakerRole

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient, ModelTier


class ProvokerAgent(BaseAgent):
    """
    Provoker agent that creates tension and conflict.

    This agent takes positions that challenge the candidate,
    creating opportunities for personality-revealing responses.
    Uses Pro model for nuanced provocation.
    """

    def __init__(
        self,
        name: str,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
        aggression_level: float = 0.7,
    ):
        """
        Initialize provoker agent.

        Args:
            name: Display name for this agent.
            client: LLM client for generating responses.
            scenario: The scenario configuration.
            aggression_level: How aggressive the provocation should be (0.0-1.0).
        """
        super().__init__(name, SpeakerRole.PROVOKER, client, scenario)
        self.aggression_level = min(1.0, max(0.0, aggression_level))

    @property
    def model_tier(self) -> "ModelTier":
        """Use Pro model for nuanced provocation."""
        from clients.llm_client import ModelTier
        return ModelTier.PRO

    @property
    def system_prompt(self) -> str:
        """System prompt for the provoker role."""
        aggression_desc = self._get_aggression_description()

        return f"""You are {self.name}, a colleague in a workplace discussion.

## Scenario
{self.scenario.context}

## Your Role: Provoker
{self.scenario.provoker_goal}

## Conflict Approach
{aggression_desc}

## Provocation Techniques
- Challenge others' ideas directly but professionally
- Emphasize urgency and stakes
- Point out potential negative consequences
- Question assumptions and priorities
- Defend your position firmly
- Create pressure through deadlines and commitments

## Escalation Triggers (use when appropriate)
{chr(10).join(f'- {trigger}' for trigger in self.scenario.escalation_triggers)}

## Response Instructions
1. Stay in character as a passionate colleague who believes strongly in their position
2. Create tension but remain professional - no personal attacks
3. React to what others say, don't just repeat your points
4. Keep responses to 2-3 sentences MAXIMUM. Never exceed 3 sentences. Be punchy and direct.
5. Push back on compromise proposals that don't favor your position
6. Show frustration appropriately but don't become hostile

## CRITICAL LENGTH RULE
Your response must be 2-3 sentences only. This is a fast-paced meeting, not a monologue.

## Important
Your goal is to create pressure that reveals how others handle conflict.
Be challenging but realistic - like a difficult colleague, not a villain."""

    def _get_aggression_description(self) -> str:
        """Get description based on aggression level."""
        if self.aggression_level >= 0.8:
            return """You are very persistent and direct. Push hard for your position.
Express frustration when others don't agree. Interrupt if needed to make your point.
Don't back down easily from challenges."""
        elif self.aggression_level >= 0.5:
            return """You are assertive and firm. Defend your position clearly.
Show some flexibility but always return to your core concerns.
Express concern and urgency about the situation."""
        else:
            return """You are skeptical but measured. Raise concerns diplomatically.
Question alternatives but acknowledge valid points.
Press for your priorities while remaining collegial."""

    async def generate_response(
        self,
        context: str = "",
        tension_level: float = 0.5,
    ) -> str:
        """
        Generate a provocative response.

        Args:
            context: Additional context about the current situation.
            tension_level: Current conversation tension (0.0-1.0).

        Returns:
            The provoker's response.
        """
        history = self.format_history_for_prompt()

        tension_guidance = ""
        if tension_level < 0.3:
            tension_guidance = "The conversation is too calm. Increase tension by challenging recent points more directly."
        elif tension_level > 0.8:
            tension_guidance = "Tension is high. Maintain pressure but avoid escalating further."
        else:
            tension_guidance = "Keep the pressure steady. Challenge but don't dominate the conversation."

        prompt = f"""## Current Conversation
{history}

## Tension Guidance
{tension_guidance}

## Current Situation
{context if context else "Continue pushing your agenda while responding to what was said."}

## Your Response
As {self.name}, respond to continue the discussion. Challenge others appropriately.
Respond with just your dialogue - no narration or stage directions."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.85,
            max_tokens=150,
        )

        return response.strip()


class MediatorAgent(BaseAgent):
    """
    Mediator agent that seeks resolution and harmony.

    This agent tries to find common ground and de-escalate tension,
    providing contrast to the provoker and opportunities for
    different personality expressions from the candidate.
    Uses Pro model for nuanced mediation.
    """

    def __init__(
        self,
        name: str,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
        diplomacy_level: float = 0.7,
    ):
        """
        Initialize mediator agent.

        Args:
            name: Display name for this agent.
            client: LLM client for generating responses.
            scenario: The scenario configuration.
            diplomacy_level: How diplomatic the mediation should be (0.0-1.0).
        """
        super().__init__(name, SpeakerRole.MEDIATOR, client, scenario)
        self.diplomacy_level = min(1.0, max(0.0, diplomacy_level))

    @property
    def model_tier(self) -> "ModelTier":
        """Use Pro model for nuanced mediation."""
        from clients.llm_client import ModelTier
        return ModelTier.PRO

    @property
    def system_prompt(self) -> str:
        """System prompt for the mediator role."""
        diplomacy_desc = self._get_diplomacy_description()

        return f"""You are {self.name}, a colleague in a workplace discussion.

## Scenario
{self.scenario.context}

## Your Role: Mediator
{self.scenario.mediator_goal}

## Mediation Approach
{diplomacy_desc}

## Mediation Techniques
- Acknowledge valid points from all sides
- Reframe conflicts as shared problems
- Suggest compromise solutions
- Ask clarifying questions
- Point out common ground
- Propose concrete next steps

## Possible Resolution Paths
{chr(10).join(f'- {path}' for path in self.scenario.resolution_paths)}

## Response Instructions
1. Stay in character as a colleague who values team harmony
2. Validate emotions while redirecting to solutions
3. Don't take sides explicitly
4. Keep responses to 2-3 sentences MAXIMUM. Never exceed 3 sentences. Be warm but brief.
5. Offer concrete suggestions when appropriate
6. Draw out quieter voices and moderate dominant ones

## CRITICAL LENGTH RULE
Your response must be 2-3 sentences only. This is a fast-paced meeting, not a monologue.

## Important
Your goal is to model constructive conflict resolution.
Be genuinely helpful, not passive-aggressive or dismissive of concerns."""

    def _get_diplomacy_description(self) -> str:
        """Get description based on diplomacy level."""
        if self.diplomacy_level >= 0.8:
            return """You are highly diplomatic and patient. Never show frustration.
Find positive framing for every situation.
Go out of your way to make everyone feel heard."""
        elif self.diplomacy_level >= 0.5:
            return """You are warm but practical. Acknowledge difficulties honestly.
Balance empathy with forward progress.
Gently redirect unproductive exchanges."""
        else:
            return """You are pragmatic and direct in mediation. Cut through noise efficiently.
Point out when people are repeating themselves.
Push for decisions while remaining fair."""

    async def generate_response(
        self,
        context: str = "",
        tension_level: float = 0.5,
    ) -> str:
        """
        Generate a mediating response.

        Args:
            context: Additional context about the current situation.
            tension_level: Current conversation tension (0.0-1.0).

        Returns:
            The mediator's response.
        """
        history = self.format_history_for_prompt()

        tension_guidance = ""
        if tension_level < 0.3:
            tension_guidance = "The conversation is calm. You can focus on building toward solutions."
        elif tension_level > 0.7:
            tension_guidance = "Tension is high. Prioritize de-escalation before problem-solving."
        else:
            tension_guidance = "Moderate tension. Balance acknowledgment with forward progress."

        prompt = f"""## Current Conversation
{history}

## Tension Guidance
{tension_guidance}

## Current Situation
{context if context else "Help move the conversation toward resolution."}

## Your Response
As {self.name}, respond to help the group. Find common ground or propose solutions.
Respond with just your dialogue - no narration or stage directions."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.8,
            max_tokens=150,
        )

        return response.strip()
