"""
Base Agent: Abstract base class for all AI agents.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from utils.models import Turn, SpeakerRole

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


class BaseAgent(ABC):
    """
    Abstract base class for AI agents in the interview platform.

    All agents share:
    - Name and role
    - LLM client for generation
    - Conversation history tracking
    - System prompt definition
    """

    def __init__(
        self,
        name: str,
        role: SpeakerRole,
        client: "LLMClient",
    ):
        self.name = name
        self.role = role
        self.client = client
        self.conversation_history: list[Turn] = []

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """System prompt defining the agent's behavior."""
        pass

    @abstractmethod
    async def generate_response(self, context: str = "") -> str:
        """Generate a response given the current context."""
        pass

    def update_history(self, turns: list[Turn]):
        """Update the agent's view of conversation history."""
        self.conversation_history = turns.copy()

    def format_history_for_prompt(self, max_turns: int = 10) -> str:
        """Format recent conversation history for inclusion in prompts."""
        recent = self.conversation_history[-max_turns:] if max_turns else self.conversation_history
        lines = []
        for turn in recent:
            lines.append(f"[Turn {turn.turn_number}] {turn.speaker_name}: {turn.content}")
        return "\n".join(lines) if lines else "(No conversation history yet)"
