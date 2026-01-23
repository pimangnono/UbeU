"""
Base Agent class for Pressure Cooker Framework.
Defines the abstract interface that all agents must implement.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from utils.models import SpeakerRole, Turn, ScenarioConfig

if TYPE_CHECKING:
    from clients.llm_client import GeminiClient, MockGeminiClient, ModelTier


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the simulation.

    All agents share:
    - A name and role
    - Access to the LLM client
    - Knowledge of the scenario context
    - Ability to generate responses based on conversation history
    """

    def __init__(
        self,
        name: str,
        role: SpeakerRole,
        client: "GeminiClient | MockGeminiClient",
        scenario: ScenarioConfig,
    ):
        """
        Initialize base agent.

        Args:
            name: Display name for this agent.
            role: The speaker role (CANDIDATE, PROVOKER, MEDIATOR, SYSTEM).
            client: LLM client for generating responses.
            scenario: The scenario configuration.
        """
        self.name = name
        self.role = role
        self.client = client
        self.scenario = scenario
        self._conversation_history: list[Turn] = []

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """
        The system prompt that defines this agent's behavior.
        Must be implemented by subclasses.
        """
        pass

    @property
    @abstractmethod
    def model_tier(self) -> "ModelTier":
        """
        The model tier to use for this agent.
        Must be implemented by subclasses.
        """
        pass

    def update_history(self, turns: list[Turn]) -> None:
        """Update the agent's view of conversation history."""
        self._conversation_history = turns.copy()

    def format_history_for_prompt(self, max_turns: int = 10) -> str:
        """
        Format recent conversation history for inclusion in prompts.

        Args:
            max_turns: Maximum number of recent turns to include.

        Returns:
            Formatted string of conversation history.
        """
        recent = self._conversation_history[-max_turns:] if self._conversation_history else []

        if not recent:
            return "[No conversation history yet]"

        lines = []
        for turn in recent:
            speaker_label = f"{turn.speaker_name} ({turn.speaker.value})"
            lines.append(f"{speaker_label}: {turn.content}")

        return "\n".join(lines)

    @abstractmethod
    async def generate_response(self, context: str = "") -> str:
        """
        Generate a response based on current conversation state.

        Args:
            context: Additional context for this turn (e.g., tension level).

        Returns:
            The agent's response text.
        """
        pass

    def create_turn(self, content: str, turn_number: int, **kwargs) -> Turn:
        """
        Create a Turn object for this agent's response.

        Args:
            content: The response content.
            turn_number: The sequential turn number.
            **kwargs: Additional Turn fields.

        Returns:
            A Turn object.
        """
        return Turn(
            turn_number=turn_number,
            speaker=self.role,
            speaker_name=self.name,
            content=content,
            **kwargs
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', role={self.role.value})"
