"""
AI Test Candidate Agent for automated interview testing.

Simulates human candidates with different personas:
- Varying levels of business knowledge (expert vs novice)
- Different typing comfort levels (short vs detailed responses)
- Optional typo simulation

Used for testing the interview platform without human participants.
"""

import random
import re
from typing import TYPE_CHECKING, Optional

from agents.base_agent import BaseAgent
from config.test_personas import TestPersona
from step2.case_data import CaseStudy
from utils.models import ScenarioConfig, SpeakerRole

if TYPE_CHECKING:
    from clients.llm_client import LLMClient, ModelTier


# Common typo patterns (character swaps, missing letters, double letters)
TYPO_PATTERNS = [
    (r'the', ['teh', 'hte', 'th']),
    (r'and', ['adn', 'nad', 'an']),
    (r'that', ['taht', 'htat', 'tha']),
    (r'have', ['ahve', 'hav', 'hvae']),
    (r'what', ['waht', 'wha', 'hwat']),
    (r'this', ['tihs', 'thsi', 'ths']),
    (r'with', ['wiht', 'wtih', 'wth']),
    (r'from', ['form', 'fom', 'frmo']),
    (r'they', ['tehy', 'thye', 'thy']),
    (r'should', ['shoudl', 'shuold', 'shoud']),
    (r'could', ['coudl', 'cuold', 'coud']),
    (r'would', ['woudl', 'wuold', 'woud']),
    (r'think', ['thnik', 'thnk', 'htink']),
    (r'about', ['abuot', 'abotu', 'abot']),
    (r'their', ['thier', 'ther', 'tehir']),
    (r'there', ['tehre', 'ther', 'theer']),
    (r'because', ['becuase', 'becasue', 'becaus']),
    (r'customer', ['cusotmer', 'custoemr', 'custmer']),
    (r'revenue', ['revneue', 'reveune', 'revenu']),
    (r'margin', ['margni', 'maring', 'margn']),
    (r'segment', ['segmnet', 'segmetn', 'segent']),
    (r'business', ['busniess', 'buisness', 'busines']),
    (r'analysis', ['anaylsis', 'analyis', 'anlysis']),
    (r'question', ['quesiton', 'questoin', 'questin']),
    (r'problem', ['problme', 'probelm', 'problm']),
]


class AITestCandidate(BaseAgent):
    """
    AI agent that simulates a human candidate for testing.

    This agent uses TestPersona configuration to determine:
    - Business knowledge level and framework awareness
    - Response length and typing comfort
    - Whether to include realistic typos
    """

    def __init__(
        self,
        client: "LLMClient",
        scenario: ScenarioConfig,
        persona: TestPersona,
        case_study: Optional[CaseStudy] = None,
    ):
        """
        Initialize AI test candidate.

        Args:
            client: LLM client for generating responses.
            scenario: The scenario configuration.
            persona: Test persona configuration.
            case_study: Optional case study for context.
        """
        super().__init__(
            name=persona.display_name,
            role=SpeakerRole.CANDIDATE,
            client=client,
            scenario=scenario,
        )
        self.persona = persona
        self.case_study = case_study
        self._revealed_categories: set[str] = set()

    @property
    def model_tier(self) -> "ModelTier":
        """Use Pro model for nuanced persona acting."""
        from clients.llm_client import ModelTier
        return ModelTier.PRO

    def update_revealed_categories(self, categories: set[str]) -> None:
        """Update the set of revealed case study data categories."""
        self._revealed_categories = categories

    @property
    def system_prompt(self) -> str:
        """
        System prompt with persona injection.

        Combines:
        - Role context (candidate in a case study discussion)
        - Persona-specific knowledge and behavior
        - Response style based on typing comfort
        - Case study context if available
        """
        personality_injection = self.persona.personality.get_system_prompt_injection()
        persona_injection = self.persona.get_system_prompt_injection()

        # Build case study context
        case_context = ""
        if self.case_study:
            case_context = f"""
## Case Study Context
Company: {self.case_study.company_name} ({self.case_study.industry})
Problem: {self.case_study.problem_statement}

You are analyzing this case with colleagues. Lead the analysis by asking for
relevant data, proposing hypotheses, and building toward a recommendation.
"""
            # Add revealed data context
            if self._revealed_categories:
                revealed_data = self.case_study.get_revealed_data(self._revealed_categories)
                if revealed_data:
                    case_context += f"\n## Data You've Learned\n{revealed_data}\n"

        # Response length constraints based on persona
        length_instruction = self._get_length_instruction()

        return f"""You are {self.name}, a participant in a consulting case study discussion.

## Your Role
You are the candidate being assessed. Lead the case analysis, ask for data,
and work toward a recommendation. Jordan and Sam are your colleagues who will
react to your ideas. The Facilitator provides data when you ask for it.

{case_context}

## Your Background
{persona_injection}

## Your Personality
{personality_injection}

{length_instruction}

## Response Guidelines
1. Stay in character with your persona at all times
2. Lead the discussion - propose what to analyze next
3. Ask specific questions to get data from the Facilitator
4. React to your colleagues' points
5. Build toward a logical recommendation
6. Do NOT break character or mention you are an AI
7. Do NOT explicitly reference your persona or traits

## Important
- Your responses will be analyzed to infer your capability and approach
- Respond naturally while staying consistent with your persona
- Show your knowledge (or lack thereof) through how you tackle the problem"""

    def _get_length_instruction(self) -> str:
        """Get response length instruction based on typing comfort."""
        if self.persona.typing_comfort == "uncomfortable":
            return """## RESPONSE LENGTH (CRITICAL)
You are uncomfortable with typing. Follow these rules STRICTLY:
- Maximum 1-2 sentences per response
- Never write more than 40 words
- Skip pleasantries and filler phrases
- Use abbreviations when natural (e.g., "&" for "and", "w/" for "with")
- Get straight to your point
- One idea per message"""

        if self.persona.response_length == "detailed":
            return """## RESPONSE LENGTH
You are comfortable with typing and can express ideas fully:
- Use 3-5 sentences typically
- Structure complex points with clear organization
- Explain your reasoning
- Reference frameworks or approaches you're using
- It's okay to be thorough"""

        return """## RESPONSE LENGTH
Moderate response length:
- Use 2-3 sentences typically
- Clear but not overly elaborate
- Balance brevity with clarity"""

    def _add_typos(self, text: str) -> str:
        """Add realistic typos to text if persona includes typos."""
        if not self.persona.include_typos:
            return text

        if self.persona.typo_probability <= 0:
            return text

        # Only add typos probabilistically
        if random.random() > self.persona.typo_probability:
            return text

        # Apply 1-2 typos
        num_typos = random.randint(1, 2)
        words = text.split()

        for _ in range(num_typos):
            for pattern, replacements in random.sample(TYPO_PATTERNS, len(TYPO_PATTERNS)):
                # Find matches in the text
                for i, word in enumerate(words):
                    if re.match(pattern, word.lower()):
                        # Preserve capitalization for first letter
                        replacement = random.choice(replacements)
                        if word[0].isupper():
                            replacement = replacement[0].upper() + replacement[1:]
                        words[i] = replacement
                        break
                else:
                    continue
                break

        return " ".join(words)

    async def generate_response(self, context: str = "") -> str:
        """
        Generate a response as the test candidate.

        Args:
            context: Additional context about the current situation.

        Returns:
            The candidate's response, possibly with typos.
        """
        history = self.format_history_for_prompt()

        # Build prompt
        prompt_parts = []

        if history:
            prompt_parts.append(f"## Conversation So Far\n{history}")

        if context:
            prompt_parts.append(f"## Current Situation\n{context}")

        # Add specific guidance based on persona
        if self.persona.business_knowledge_level == "novice":
            prompt_parts.append(
                "## Your Approach\n"
                "Remember: You don't know any business frameworks. "
                "Use common sense and intuition. Ask simple questions. "
                "If you hear terms you don't know, ask what they mean."
            )
        elif self.persona.typing_comfort == "uncomfortable":
            prompt_parts.append(
                "## Your Response Style\n"
                "Keep it SHORT. 1-2 sentences max. Get to the point."
            )
        else:
            prompt_parts.append(
                "## Your Approach\n"
                "Lead the analysis. Propose a structure or hypothesis. "
                "Ask for specific data. Reference frameworks if appropriate."
            )

        prompt_parts.append(
            f"## Your Response\n"
            f"As {self.name}, respond to the conversation. "
            f"Respond with just your dialogue - no narration."
        )

        prompt = "\n\n".join(prompt_parts)

        # Adjust max tokens based on persona
        max_tokens = 100 if self.persona.typing_comfort == "uncomfortable" else 256

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.9,
            max_tokens=max_tokens,
        )

        response = response.strip()

        # Add typos if configured
        response = self._add_typos(response)

        return response

    def get_persona_summary(self) -> dict:
        """Get a summary of the persona for logging."""
        return {
            "persona_id": self.persona.id,
            "persona_name": self.persona.name,
            "display_name": self.persona.display_name,
            "business_knowledge": self.persona.business_knowledge_level,
            "knows_frameworks": self.persona.knows_frameworks,
            "typing_comfort": self.persona.typing_comfort,
            "include_typos": self.persona.include_typos,
        }
