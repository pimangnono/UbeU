"""
Agent Registry: Discovers and indexes A2A agent cards.

Adding a new agent requires:
1. Create agents/agent_cards/<name>.json
2. Add agent class in group_agents.py
3. Registry auto-discovers on startup
"""

import json
import logging
from pathlib import Path
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

AGENT_CARDS_DIR = Path(__file__).parent / "agent_cards"


@dataclass
class AgentCard:
    """Parsed agent card from JSON."""
    name: str
    display_name: str
    description: str
    role: str
    personality: dict[str, float]
    skills: list[dict]
    best_for_probing: list[str]
    style: str


class AgentRegistry:
    """
    Discovers agent cards from JSON files.

    Usage:
        registry = AgentRegistry()
        card = registry.get("alex")
        all_names = registry.list_agents()
    """

    def __init__(self, cards_dir: Path = AGENT_CARDS_DIR):
        self._cards: dict[str, AgentCard] = {}
        self._load_cards(cards_dir)

    def _load_cards(self, cards_dir: Path) -> None:
        """Load all agent card JSON files from the directory."""
        if not cards_dir.exists():
            logger.warning(f"Agent cards directory not found: {cards_dir}")
            return

        for json_file in sorted(cards_dir.glob("*.json")):
            try:
                with open(json_file) as f:
                    data = json.load(f)

                card = AgentCard(
                    name=data["name"],
                    display_name=data.get("display_name", data["name"].title()),
                    description=data.get("description", ""),
                    role=data.get("role", ""),
                    personality=data.get("personality", {}),
                    skills=data.get("skills", []),
                    best_for_probing=data.get("best_for_probing", []),
                    style=data.get("style", ""),
                )
                self._cards[card.name] = card
                logger.debug(f"Loaded agent card: {card.display_name}")

            except (json.JSONDecodeError, KeyError) as e:
                logger.warning(f"Failed to load agent card {json_file}: {e}")

    def get(self, name: str) -> AgentCard:
        """Get an agent card by name."""
        name_lower = name.lower()
        if name_lower not in self._cards:
            raise ValueError(f"Agent '{name}' not found. Available: {list(self._cards.keys())}")
        return self._cards[name_lower]

    def list_agents(self) -> list[str]:
        """List all registered agent display names."""
        return [card.display_name for card in self._cards.values()]

    def get_agent_for_trait(self, trait: str) -> str:
        """Find the best agent for probing a given trait."""
        trait_lower = trait.lower()
        for card in self._cards.values():
            if trait_lower in card.best_for_probing:
                return card.display_name
        # Default to Jordan
        return "Jordan"

    def __len__(self) -> int:
        return len(self._cards)
