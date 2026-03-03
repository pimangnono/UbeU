"""
Experiment Candidate Agent: Automated candidate for behavioral fidelity testing.

Standalone agent (does NOT extend BaseAgent) that generates candidate responses
based on a personality system prompt. Used by BatchRunner to simulate candidates
with specific OCEAN profiles.
"""

import logging
import re
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from clients.llm_client import LLMClient
    from utils.models import Turn

logger = logging.getLogger(__name__)

# Default prompt for Baseline A (no personality instructions)
DEFAULT_CANDIDATE_PROMPT = (
    "You are a participant named 'Candidate' in a group workplace discussion. "
    "Respond naturally, concisely, and realistically to the ongoing conversation."
)


class ExperimentCandidateAgent:
    """
    Automated candidate agent for the behavioral fidelity experiment.

    Generates responses based on a personality system prompt (or no prompt for
    Baseline A). Does NOT extend BaseAgent to avoid Mode 1 coupling.
    """

    def __init__(
        self,
        client: "LLMClient",
        system_prompt: Optional[str] = None,
        candidate_name: str = "Candidate",
    ):
        """
        Args:
            client: LLM client for generation.
            system_prompt: Personality-based system prompt, or None for Baseline A.
            candidate_name: Name used in the conversation.
        """
        self.client = client
        self.system_prompt = system_prompt or DEFAULT_CANDIDATE_PROMPT
        self.candidate_name = candidate_name

    async def generate_response(
        self,
        turns: list["Turn"],
        scenario_brief: str,
        phase_style: str,
    ) -> str:
        """
        Generate a candidate response given the conversation history.

        Args:
            turns: Full conversation history.
            scenario_brief: The scenario description for context.
            phase_style: Current phase style (neutral/agreement/disagreement/consensus).

        Returns:
            Generated candidate response text.
        """
        # Format last 10 turns as context
        recent_turns = turns[-10:] if len(turns) > 10 else turns
        history_lines = []
        for t in recent_turns:
            history_lines.append(f"[Turn {t.turn_number}] {t.speaker_name}: {t.content}")
        history = "\n".join(history_lines)

        style_hint = ""
        if phase_style == "disagreement":
            style_hint = (
                "\nThe discussion is in a phase where there are differing opinions. "
                "You should take a clear position and express it directly. If you disagree "
                "with what was just said, say so explicitly. Do not hedge or soften your stance."
            )
        elif phase_style == "consensus":
            style_hint = "\nThe group is trying to reach agreement."
        elif phase_style == "agreement":
            style_hint = "\nThe group is in an exploratory, collaborative phase."

        prompt = f"""Here is the recent conversation:

{history}
{style_hint}

Respond as {self.candidate_name} in this discussion. Keep your response natural, concise (1-3 sentences), and in character. Do not include your name as a prefix."""

        try:
            response = await self.client.generate(
                prompt=prompt,
                system_instruction=self.system_prompt,
                temperature=0.7,
                max_tokens=200,
            )
        except Exception as e:
            logger.error(f"Candidate generation failed: {e}")
            # Return a minimal fallback response
            return "I think we should consider all the options before deciding."

        # Clean up the response
        response = response.strip()

        # Remove any "Candidate:" prefix the model might add
        response = re.sub(r"^(Candidate|CANDIDATE)\s*:\s*", "", response, flags=re.IGNORECASE)

        # Remove surrounding quotes if present
        if response.startswith('"') and response.endswith('"'):
            response = response[1:-1]

        # Strip stage directions that leak emotional state
        response = self._strip_stage_directions(response)

        return response.strip()

    # Keywords that indicate a parenthetical is a stage direction, not normal text
    _STAGE_DIRECTION_WORDS = re.compile(
        r'\b(?:hesitat|nervous|softly|quietly|loudly|firmly|slow|quick|sigh|'
        r'pause|lean|shift|fidget|nod|shak|trembl|flinch|shrink|tense|'
        r'smile|frown|laugh|whisper|mutter|stammer|stutter|gulp|swallow|'
        r'gesture|point|wave|shrug|clench|squirm|wince|blush|'
        r'voice|speaking|looking|getting|slightly|visibly)',
        re.IGNORECASE,
    )

    def _strip_stage_directions(self, text: str) -> str:
        """Remove *italicized actions*, [bracket actions], and (parenthetical directions)."""
        text = re.sub(r'\*[^*]+\*', '', text)           # *action*
        text = re.sub(r'\[[^\]]*\]', '', text)          # [action]
        # Remove parentheticals containing stage-direction keywords
        def _remove_stage_parens(m):
            return '' if self._STAGE_DIRECTION_WORDS.search(m.group()) else m.group()
        text = re.sub(r'\([^)]+\)', _remove_stage_parens, text)
        text = re.sub(r'\s{2,}', ' ', text).strip()     # collapse whitespace
        return text
