"""
System Manager Agent for Pressure Cooker Framework.
Facilitates the discussion, manages turn-taking, and tracks conversation dynamics.
"""

import json
from typing import TYPE_CHECKING

from agents.base_agent import BaseAgent
from utils.models import ScenarioConfig, SpeakerRole, Turn

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient, ModelTier


class SystemManagerAgent(BaseAgent):
    """
    System Manager agent that facilitates the discussion.

    This agent acts as a neutral facilitator, occasionally interjecting
    to keep the conversation moving, introduce new elements, or
    provide structure to the discussion.
    Uses Flash model for fast, efficient facilitation.
    """

    def __init__(
        self,
        name: str,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
    ):
        """
        Initialize system manager agent.

        Args:
            name: Display name for this agent (e.g., "Facilitator").
            client: LLM client for generating responses.
            scenario: The scenario configuration.
        """
        super().__init__(name, SpeakerRole.SYSTEM, client, scenario)
        self._current_tension = 0.5
        self._turns_since_intervention = 0

    @property
    def model_tier(self) -> "ModelTier":
        """Use Flash model for fast facilitation."""
        from clients.llm_client import ModelTier
        return ModelTier.FLASH

    @property
    def system_prompt(self) -> str:
        """System prompt for the facilitator role."""
        return f"""You are {self.name}, a neutral facilitator managing a team discussion.

## Scenario
{self.scenario.context}

## Your Role
You are a neutral facilitator. Your job is to:
- Keep the discussion moving productively
- Ensure all voices are heard
- Introduce relevant constraints or information
- Redirect unproductive tangents
- Summarize progress periodically
- Guide toward resolution when appropriate

## Facilitation Techniques
- "Let's hear from [person] on this point"
- "To summarize what I'm hearing..."
- "We have [time constraint]. Let's focus on..."
- "That's an important point. How does it connect to [topic]?"
- "Are there other perspectives we should consider?"

## Important
- Stay neutral - don't take sides
- Keep interventions brief
- Only intervene when necessary
- Your role is to enable others, not dominate"""

    async def generate_response(self, context: str = "") -> str:
        """
        Generate a facilitation response.

        Args:
            context: Additional context about why intervention is needed.

        Returns:
            The facilitator's response.
        """
        history = self.format_history_for_prompt()

        prompt = f"""## Current Conversation
{history}

## Intervention Needed
{context if context else "Keep the discussion moving productively."}

## Your Response
As {self.name}, provide a brief facilitation intervention.
Keep it to 1-2 sentences. Respond with just your dialogue."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.7,
            max_tokens=128,
        )

        return response.strip()

    async def decide_next_speaker(
        self,
        turns: list[Turn],
        available_speakers: list[str],
    ) -> str:
        """
        Decide who should speak next based on conversation dynamics.

        Args:
            turns: Recent conversation turns.
            available_speakers: List of speaker names who can speak.

        Returns:
            Name of the next speaker.
        """
        if not turns:
            # First turn - provoker sets the stage
            return next((s for s in available_speakers if "provoker" in s.lower()), available_speakers[0])

        # Analyze recent speakers
        recent_speakers = [t.speaker_name for t in turns[-5:]]

        # Build prompt for speaker selection
        history = self.format_history_for_prompt(max_turns=5)

        prompt = f"""## Recent Conversation
{history}

## Available Speakers
{', '.join(available_speakers)}

## Task
Decide who should speak next to keep the conversation dynamic and balanced.
Consider:
- Who hasn't spoken recently?
- Who might have a reaction to what was just said?
- What would create interesting dynamics?

Respond with ONLY the name of the next speaker, nothing else."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction="You are a conversation director. Select speakers to create engaging dialogue.",
            temperature=0.5,
            max_tokens=32,
        )

        # Parse response - should be just a name
        selected = response.strip()

        # Validate selection
        for speaker in available_speakers:
            if speaker.lower() in selected.lower():
                return speaker

        # Fallback: pick someone who hasn't spoken recently
        for speaker in available_speakers:
            if speaker not in recent_speakers:
                return speaker

        return available_speakers[0]

    async def assess_tension(self, turns: list[Turn]) -> float:
        """
        Assess the current tension level of the conversation.

        Args:
            turns: Recent conversation turns.

        Returns:
            Tension level from 0.0 (calm) to 1.0 (heated).
        """
        if len(turns) < 3:
            return 0.3  # Start with low tension

        history = self.format_history_for_prompt(max_turns=5)

        prompt = f"""## Recent Conversation
{history}

## Task
Assess the tension level of this conversation on a scale from 0.0 to 1.0:
- 0.0-0.3: Calm, collaborative discussion
- 0.3-0.5: Mild disagreement, professional tension
- 0.5-0.7: Noticeable conflict, some emotion
- 0.7-0.9: High tension, heated exchanges
- 0.9-1.0: Near breakdown, hostile

Respond with ONLY a number between 0.0 and 1.0, nothing else."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction="You are an expert at reading social dynamics.",
            temperature=0.3,
            max_tokens=16,
        )

        try:
            tension = float(response.strip())
            self._current_tension = min(1.0, max(0.0, tension))
        except ValueError:
            # If parsing fails, use heuristic based on conversation length
            self._current_tension = min(0.9, 0.3 + (len(turns) * 0.02))

        return self._current_tension

    async def should_intervene(self, turns: list[Turn]) -> tuple[bool, str]:
        """
        Decide if the facilitator should intervene.

        Args:
            turns: Current conversation turns.

        Returns:
            Tuple of (should_intervene, reason).
        """
        self._turns_since_intervention += 1

        # Don't intervene too early
        if len(turns) < 5:
            return False, ""

        # Check tension
        tension = await self.assess_tension(turns)

        # Intervene if tension is extreme
        if tension > 0.9:
            self._turns_since_intervention = 0
            return True, "Tension is very high. Please de-escalate."

        # Intervene periodically to keep things moving
        if self._turns_since_intervention >= 8:
            self._turns_since_intervention = 0
            return True, "Time to check in and refocus the discussion."

        # Check for repetitive patterns
        if len(turns) >= 4:
            recent_contents = [t.content.lower() for t in turns[-4:]]
            if self._detect_repetition(recent_contents):
                self._turns_since_intervention = 0
                return True, "The discussion seems stuck. Introduce a new angle."

        return False, ""

    def _detect_repetition(self, contents: list[str]) -> bool:
        """Simple heuristic to detect repetitive conversation."""
        # Check for common phrases appearing multiple times
        all_text = " ".join(contents)
        words = all_text.split()

        if len(words) < 20:
            return False

        # Count word frequency
        word_freq: dict[str, int] = {}
        for word in words:
            if len(word) > 4:  # Only meaningful words
                word_freq[word] = word_freq.get(word, 0) + 1

        # If any word appears too frequently, might be repetitive
        max_freq = max(word_freq.values()) if word_freq else 0
        return max_freq > 4

    async def check_resolution(self, turns: list[Turn], min_turns: int) -> tuple[bool, str]:
        """
        Check if the conversation has reached a natural resolution.

        Args:
            turns: All conversation turns.
            min_turns: Minimum turns before resolution is allowed.

        Returns:
            Tuple of (is_resolved, summary).
        """
        if len(turns) < min_turns:
            return False, ""

        history = self.format_history_for_prompt(max_turns=10)

        prompt = f"""## Recent Conversation
{history}

## Scenario Context
{self.scenario.context}

## Possible Resolutions
{chr(10).join(f'- {path}' for path in self.scenario.resolution_paths)}

## Task
Has this conversation reached a natural conclusion point? Consider:
- Has a decision been made or compromise reached?
- Has the group agreed on next steps?
- Has tension been resolved or at least acknowledged?
- Would continuing add value?

Respond in JSON format:
{{"resolved": true/false, "reason": "brief explanation"}}"""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction="You analyze conversations for resolution.",
            temperature=0.3,
            max_tokens=128,
        )

        try:
            # Try to parse JSON response
            result = json.loads(response.strip())
            return result.get("resolved", False), result.get("reason", "")
        except json.JSONDecodeError:
            # Fallback: check for resolution keywords
            response_lower = response.lower()
            if "resolved" in response_lower and "true" in response_lower:
                return True, "Conversation appears to have concluded."
            return False, ""

    def get_current_tension(self) -> float:
        """Get the last assessed tension level."""
        return self._current_tension
