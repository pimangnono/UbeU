"""
Case data structures for consulting scenarios with information gating.

CaseDataItem: A single data category with keywords for gating.
CaseStudy: A complete case study with gated data categories.
"""

import re
from dataclasses import dataclass, field

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.models import ScenarioConfig


@dataclass
class CaseDataItem:
    """A single hidden data category within a case study."""
    category: str          # e.g., "customer_segments", "revenue", "costs"
    label: str             # display label
    detail: str            # the actual hidden data
    keywords: list[str] = field(default_factory=list)  # trigger words that reveal this category


@dataclass
class CaseStudy:
    """
    A consulting case study with gated information.

    The problem_statement is shown upfront. Data items are hidden
    until the candidate asks about them (matched via keywords).
    """
    id: str
    company_name: str
    industry: str
    problem_statement: str
    data_items: list[CaseDataItem] = field(default_factory=list)

    def get_revealed_data(self, revealed_categories: set[str]) -> str:
        """Get formatted text of all revealed data categories."""
        parts = []
        for item in self.data_items:
            if item.category in revealed_categories:
                parts.append(f"**{item.label}:**\n{item.detail}")
        return "\n\n".join(parts) if parts else ""

    def get_all_category_labels(self) -> dict[str, str]:
        """Get mapping of category ID -> label for all data items."""
        return {item.category: item.label for item in self.data_items}

    def match_categories(self, text: str) -> set[str]:
        """
        Match text against data item keywords to determine which
        categories the candidate is asking about.

        Returns set of category IDs that should be revealed.
        """
        text_lower = text.lower()
        matched = set()
        for item in self.data_items:
            for keyword in item.keywords:
                # Match word prefix (allows plurals: "competitor" matches "competitors")
                if re.search(r'\b' + re.escape(keyword.lower()), text_lower):
                    matched.add(item.category)
                    break
        return matched

    def to_scenario_config(self) -> ScenarioConfig:
        """
        Convert this case study into a ScenarioConfig compatible
        with the existing LiveEngine/agent architecture.
        """
        context = (
            f"You are in a consulting case discussion. The company is {self.company_name}, "
            f"operating in the {self.industry} industry.\n\n"
            f"Problem: {self.problem_statement}\n\n"
            f"The team must analyze the problem and develop a recommendation."
        )

        provoker_goal = (
            "You are a skeptical analyst. Challenge assumptions, demand data-backed reasoning, "
            "question if proposed solutions are realistic given the constraints. Push the candidate "
            "to think deeper about root causes. If the candidate makes claims without evidence, "
            "call it out. Be direct but professional."
        )

        mediator_goal = (
            "You are a supportive analyst. Acknowledge good questions, build on ideas, suggest "
            "frameworks when appropriate. If the candidate hasn't asked about key data, model "
            "analytical behavior by asking about it yourself. Help structure the discussion "
            "but don't give away the answer."
        )

        escalation_triggers = [
            "Candidate makes unfounded assumptions without asking for data",
            "Analysis ignores key cost drivers or revenue dynamics",
            "Proposed solution lacks specificity or implementation detail",
            "Candidate dismisses competitor analysis as irrelevant",
            "Recommendation doesn't address the core problem statement",
        ]

        resolution_paths = [
            "Structured framework covering all relevant dimensions",
            "Data-driven recommendation backed by case data",
            "Clear implementation roadmap with priorities",
            "Consideration of risks and competitive dynamics",
        ]

        return ScenarioConfig(
            id=self.id,
            name=f"{self.company_name} Case Study",
            description=f"{self.company_name} ({self.industry}): {self.problem_statement[:80]}...",
            context=context,
            conflict_point=f"The team needs to solve: {self.problem_statement}",
            provoker_goal=provoker_goal,
            mediator_goal=mediator_goal,
            escalation_triggers=escalation_triggers,
            resolution_paths=resolution_paths,
            turn_limit=30,
            min_turns=15,
        )
