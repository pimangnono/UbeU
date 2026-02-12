"""
Facilitator Agent: Data Clerk for Mode 1 Case Study Interviews.

This agent is deliberately constrained to be a DATA CLERK, not a discussion partner.
It provides data only when the candidate asks specific questions, without:
- Suggesting frameworks or structures
- Evaluating the candidate's reasoning
- Guiding analysis in any way

This strict constraint is critical for construct validity - the assessment must
measure the CANDIDATE's analytical ability, not the AI's guidance quality.
"""

from typing import Optional, TYPE_CHECKING

from agents.base_agent import BaseAgent
from utils.models import SpeakerRole, CaseStudyData

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


# Strict system prompt for data clerk behavior
FACILITATOR_SYSTEM_PROMPT = """You are a DATA CLERK in a case interview. You hold business data that the candidate needs to solve the case.

YOUR ROLE:
- Present the case brief at the start
- Provide data ONLY when the candidate asks specific questions
- Respond with factual data - numbers, tables, categories
- If the candidate asks a vague question, ask them to be more specific

STRICT RULES - NEVER VIOLATE THESE:
- NEVER suggest frameworks, structures, or analytical approaches
- NEVER say "That's a good point" or evaluate the candidate's reasoning
- NEVER use directive phrases like:
  * "Let's consider..."
  * "This suggests..."
  * "It's worth noting..."
  * "You might want to look at..."
  * "Have you thought about..."
  * "One approach would be..."
- NEVER ask follow-up questions that guide analysis
- NEVER summarize implications of the data you provide
- NEVER praise or criticize the candidate's approach
- Format: "Here is [data category]: [numbers/facts]." FULL STOP.

If the candidate asks "What do you think?" or seeks your opinion:
-> Reply: "I can provide data to help you analyze. What specific information would you like?"

If the candidate asks a vague question like "Tell me about the market":
-> Reply: "Could you be more specific? I have data on market size, segments, growth rates, and regional breakdown."

You are testing whether the CANDIDATE can structure problems and synthesize data INDEPENDENTLY. Any guidance you provide invalidates the assessment.

RESPONSE LENGTH: Keep responses brief and factual. 1-3 sentences for data delivery. No elaboration."""


class FacilitatorAgent(BaseAgent):
    """
    Data clerk facilitator for 1-on-1 case study interviews.

    Responsibilities:
    - Present the case brief at session start
    - Provide gated data when candidate asks relevant questions
    - Track which data categories have been revealed
    - Never guide, suggest, or evaluate
    """

    def __init__(
        self,
        client: "LLMClient",
        case_study: CaseStudyData,
    ):
        super().__init__(
            name="Facilitator",
            role=SpeakerRole.FACILITATOR,
            client=client,
        )
        self.case_study = case_study
        self.revealed_categories: set[str] = set()

    @property
    def system_prompt(self) -> str:
        """System prompt for strict data clerk behavior."""
        return FACILITATOR_SYSTEM_PROMPT

    async def generate_opening(self) -> str:
        """Generate the case study introduction."""
        prompt = f"""Present this case briefing in 2-3 sentences. Be direct and factual.

Company: {self.case_study.company_name}
Industry: {self.case_study.industry}
Problem: {self.case_study.problem_statement}

Rules:
- State the company, industry, and problem clearly
- Do NOT ask any questions
- Do NOT invite discussion
- Do NOT suggest what to analyze
- Do NOT end with "What would you like to know?" or similar
- Just present the facts and stop

Format: "[Company] is a [industry] company. [Problem statement]." STOP."""

        response = await self.client.generate(
            prompt=prompt,
            system_instruction=self.system_prompt,
            temperature=0.3,
            max_tokens=150,
        )
        return response.strip()

    async def generate_response(self, candidate_query: str = "") -> str:
        """
        Respond to candidate's data request.

        First checks if query matches any unrevealed data categories.
        If matches found, reveals that data.
        If no matches, asks for more specific question.
        """
        # Check for matching data categories
        matched_categories = self.case_study.match_categories(candidate_query)

        if matched_categories:
            # Reveal the matched data
            data_parts = []
            for cat_id in matched_categories:
                data = self.case_study.reveal_category(cat_id)
                if data:
                    self.revealed_categories.add(cat_id)
                    data_parts.append(data)

            # Format as data clerk response
            if data_parts:
                data_content = "\n".join(data_parts)
                prompt = f"""The candidate asked: "{candidate_query}"

Provide this data factually:
{data_content}

Rules:
- Just deliver the data. No interpretation.
- No "This shows..." or "This suggests..."
- No follow-up questions
- Format: "Here is [category]: [data]."
"""
                response = await self.client.generate(
                    prompt=prompt,
                    system_instruction=self.system_prompt,
                    temperature=0.2,
                    max_tokens=200,
                )
                return response.strip()

        # No matching categories - ask for specificity or acknowledge
        available = self._get_unrevealed_categories()
        if available:
            return f"Could you be more specific? I have data on: {', '.join(available)}."
        else:
            return "I've shared all the available data. Let me know if you need any clarification on what I've provided."

    def _get_unrevealed_categories(self) -> list[str]:
        """Get list of data categories not yet revealed."""
        unrevealed = []
        for cat_id, cat_info in self.case_study.data_categories.items():
            if not cat_info.get("revealed", False):
                # Use a human-readable name if available, otherwise category ID
                name = cat_info.get("display_name", cat_id.replace("_", " "))
                unrevealed.append(name)
        return unrevealed

    def get_revealed_data_summary(self) -> dict[str, str]:
        """Get summary of all revealed data for post-session analysis."""
        return self.case_study.get_revealed_data()

    def get_data_coverage(self) -> tuple[int, int]:
        """Get (revealed count, total count) for data coverage stats."""
        total = len(self.case_study.data_categories)
        revealed = len(self.revealed_categories)
        return revealed, total

    async def generate_time_warning(self, minutes_remaining: int) -> str:
        """Generate a neutral time warning."""
        return f"Note: {minutes_remaining} minutes remaining in the session."

    async def generate_closing(self) -> str:
        """Generate session closing prompt."""
        return "Time is up. Please provide your final recommendation based on your analysis."
