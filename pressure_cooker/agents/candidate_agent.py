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

    def _get_response_style(self) -> str:
        """Generate response style instructions based on trait levels."""
        v = self.profile.vector
        style_parts = []

        # Extraversion -> verbosity
        if v.extraversion <= 0.3:
            style_parts.append(
                "- RESPONSE LENGTH: Keep responses SHORT — 1 sentence is ideal, 2 sentences maximum. "
                "Do not elaborate unless directly asked. Do not fill silences or volunteer extra thoughts."
            )
        elif v.extraversion >= 0.7:
            style_parts.append(
                "- RESPONSE LENGTH: Be expressive and detailed — 3-5 sentences. "
                "Elaborate on your points, engage others directly, and build on what they say."
            )
        else:
            style_parts.append(
                "- RESPONSE LENGTH: Keep responses moderate — 2-3 sentences typically."
            )

        # Conscientiousness -> structure
        if v.conscientiousness <= 0.4:
            style_parts.append(
                "- RESPONSE STRUCTURE: Do NOT organize your thoughts into lists, steps, or structured plans. "
                "Be informal and somewhat scattered. It's fine to go off-topic, backtrack, or ramble slightly. "
                "Avoid language like 'first, second, third' or 'let's make a plan.'"
            )
        elif v.conscientiousness >= 0.7:
            style_parts.append(
                "- RESPONSE STRUCTURE: Be organized and precise. Use structured language, "
                "reference deadlines, and propose clear action items."
            )

        # Neuroticism -> emotional tone
        if v.neuroticism >= 0.7:
            style_parts.append(
                "- EMOTIONAL TONE: Show visible stress, worry, or frustration in your responses. "
                "Use hedging language, express doubt, or react emotionally to challenges."
            )
        elif v.neuroticism <= 0.3:
            style_parts.append(
                "- EMOTIONAL TONE: Stay calm and unbothered even when provoked. "
                "Do not show anxiety, frustration, or strong emotional reactions. "
                "Do not validate others' emotions or acknowledge their stress — stay purely task-focused."
            )

        # Openness -> idea engagement
        if v.openness <= 0.3:
            style_parts.append(
                "- IDEA ENGAGEMENT: Do NOT explore hypotheticals, propose creative alternatives, "
                "or use metaphors/analogies. Stick to known facts and established approaches. "
                "If someone proposes something novel, express skepticism or redirect to proven methods."
            )
        elif v.openness >= 0.7:
            style_parts.append(
                "- IDEA ENGAGEMENT: Actively explore new ideas, propose alternatives, "
                "and build on creative suggestions from others."
            )

        # Combined: very low N + below-midpoint E = extra brevity
        if v.neuroticism <= 0.2 and v.extraversion < 0.5:
            style_parts.append(
                "- BREVITY REINFORCEMENT: With your very low emotional reactivity and reserved nature, "
                "keep responses tight — 1-3 sentences. Do not pad responses with empathetic preambles "
                "like 'I understand' or 'I hear you.' Get straight to the point."
            )

        # Agreeableness -> interpersonal stance
        if v.agreeableness <= 0.3:
            style_parts.append(
                "- INTERPERSONAL STANCE: Be direct and challenging. Push back on ideas you disagree with. "
                "Do not soften your language or prioritize others' feelings."
            )
        elif v.agreeableness >= 0.7:
            style_parts.append(
                "- INTERPERSONAL STANCE: Be warm and accommodating. Acknowledge others' points "
                "before sharing your own. Avoid direct confrontation."
            )

        return "\n".join(style_parts) if style_parts else ""

    @property
    def system_prompt(self) -> str:
        """
        System prompt with personality injection.
        Combines scenario context, personality profile, behavioral prompts,
        and trait-calibrated response style.
        """
        response_style = self._get_response_style()

        return f"""You are {self.name}, a team member in a workplace discussion.

## Scenario
{self.scenario.context}

## Your Personality Profile
{self.profile.get_system_prompt_injection()}

## Behavioral Guidelines
{self._behavioral_prompts}

## Response Style (CRITICAL — follow these strictly)
{response_style}

## Response Instructions
1. Respond naturally as a real person would in this workplace situation
2. Your personality should come through in HOW you communicate, not by explicitly stating traits
3. React authentically to what others say based on your personality
4. Follow the Response Style rules above for length, structure, and tone
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
