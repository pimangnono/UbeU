"""
Candidate Agent for Pressure Cooker Framework.
The main subject of personality simulation - generates responses
that should reflect the injected personality profile.
"""

from typing import TYPE_CHECKING

from agents.base_agent import BaseAgent
from config.bfi_mappings import get_relevant_behaviors, generate_behavioral_prompt_injection
from utils.models import PersonalityProfile, ScenarioConfig, SpeakerRole

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient, ModelTier


class CandidateAgent(BaseAgent):
    """
    Candidate agent with personality injection.

    This agent represents the person being assessed. Their responses
    should naturally reflect the injected Big Five personality traits.
    Uses the Pro model for nuanced personality acting.
    """

    def __init__(
        self,
        name: str,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
        profile: PersonalityProfile,
    ):
        """
        Initialize candidate agent with personality profile.

        Args:
            name: Display name for this agent.
            client: LLM client for generating responses.
            scenario: The scenario configuration.
            profile: The personality profile to embody.
        """
        super().__init__(name, SpeakerRole.CANDIDATE, client, scenario)
        self.profile = profile
        self._behavioral_prompts = self._generate_behavioral_prompts()

    def _generate_behavioral_prompts(self) -> str:
        """Generate behavioral prompts based on personality vector."""
        behaviors = get_relevant_behaviors(
            openness=self.profile.vector.openness,
            conscientiousness=self.profile.vector.conscientiousness,
            extraversion=self.profile.vector.extraversion,
            agreeableness=self.profile.vector.agreeableness,
            neuroticism=self.profile.vector.neuroticism,
        )
        return generate_behavioral_prompt_injection(behaviors)

    @property
    def model_tier(self) -> "ModelTier":
        """Use Pro model for nuanced personality acting."""
        from clients.llm_client import ModelTier
        return ModelTier.PRO

    @property
    def system_prompt(self) -> str:
        """
        System prompt with personality injection.
        Combines scenario context, personality profile, and behavioral prompts.
        """
        return f"""You are {self.name}, a team member in a workplace discussion.

## Scenario
{self.scenario.context}

## Your Personality Profile
{self.profile.get_system_prompt_injection()}

## Behavioral Guidelines
{self._behavioral_prompts}

## Response Instructions
1. Respond naturally as a real person would in this workplace situation
2. Your personality should come through in HOW you communicate, not by explicitly stating traits
3. React authentically to what others say based on your personality
4. Keep responses concise (2-4 sentences typically)
5. Do not break character or mention that you are an AI
6. Do not explicitly reference your personality traits - just embody them

## Important
- Your responses will be analyzed to infer your personality
- Respond as naturally as possible while staying consistent with your traits
- Show your personality through word choice, emotional reactions, and interaction style"""

    async def generate_response(self, context: str = "") -> str:
        """
        Generate a personality-consistent response.

        Args:
            context: Additional context about the current situation.

        Returns:
            The candidate's response.
        """
        history = self.format_history_for_prompt()

        prompt = f"""## Current Conversation
{history}

## Current Situation
{context if context else "Continue the discussion naturally."}

## Your Response
As {self.name}, respond to the conversation. Remember to stay in character with your personality profile.
Respond with just your dialogue - no narration or stage directions."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.9,  # Higher temperature for more natural variation
            max_tokens=256,
        )

        return response.strip()

    def get_profile_summary(self) -> dict:
        """Get a summary of the profile for logging."""
        return {
            "profile_id": self.profile.id,
            "profile_name": self.profile.name,
            "traits": self.profile.vector.to_dict(),
        }
