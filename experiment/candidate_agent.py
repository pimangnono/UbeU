"""
Experiment Candidate Agent: Automated candidate for behavioral fidelity testing.

Standalone agent (does NOT extend BaseAgent) that generates candidate responses
based on a personality system prompt. Used by BatchRunner to simulate candidates
with specific OCEAN profiles.
"""

import asyncio
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
        self._base_system_prompt = system_prompt or DEFAULT_CANDIDATE_PROMPT
        self._current_nudge: Optional[str] = None
        self.candidate_name = candidate_name

    @property
    def system_prompt(self) -> str:
        """Active system prompt = base + current nudge (if any)."""
        if self._current_nudge:
            return self._base_system_prompt + "\n\n" + self._current_nudge
        return self._base_system_prompt

    def update_nudge(self, nudge_text: Optional[str]):
        """Update the corrective nudge appended to system prompt."""
        self._current_nudge = nudge_text

    async def generate_response(
        self,
        turns: list["Turn"],
        scenario_brief: str,
        phase_style: str,
        constraint_suffix: Optional[str] = None,
        style_directive: Optional[str] = None,
        policy_plan: Optional[dict] = None,
        phase_name: Optional[str] = None,
        phase_cues: Optional[list[str]] = None,
        target_traits: Optional[list[str]] = None,
        enable_trait_execution: bool = False,
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

        policy_text = ""
        if policy_plan:
            policy_text = (
                "\nHidden policy plan (do not mention explicitly): "
                f"stance={policy_plan.get('stance')}; "
                f"goal_mode={policy_plan.get('goal_mode')}; "
                f"planning_depth={policy_plan.get('planning_depth')}; "
                f"novelty_move={policy_plan.get('novelty_move')}; "
                f"social_tactic={policy_plan.get('social_tactic')}; "
                f"risk_posture={policy_plan.get('risk_posture')}; "
                f"memory_focus={policy_plan.get('memory_focus')}."
            )

        phase_hint = f"\nCurrent phase: {phase_name}." if phase_name else ""
        cues_hint = ""
        if phase_cues:
            cues_hint = f"\nPhase cues: {', '.join(phase_cues)}."
        traits_hint = ""
        if target_traits:
            traits_hint = f"\nTarget traits for this phase: {', '.join(target_traits)}."

        style_hint_extra = f"\nStyle slot: {style_directive}." if style_directive else ""
        execution_hint = ""
        if enable_trait_execution:
            execution_hint = (
                "\nExecution invariants (only when context makes them relevant): "
                "if ambiguity/options appear, include at least one alternative or reframe and name a tradeoff; "
                "if planning/ownership is needed, include at least one concrete owner/deadline/next-step/follow-up element."
            )

        prompt = f"""Here is the recent conversation:

{history}
{style_hint}
{phase_hint}{cues_hint}{traits_hint}{style_hint_extra}{policy_text}{execution_hint}

Respond as {self.candidate_name} in this discussion. Keep your response natural, concise (1-3 sentences), and in character. Do not include your name as a prefix."""

        # Append constraint suffix if requested (legacy hook; no regeneration in v1.1)
        if constraint_suffix:
            prompt += constraint_suffix

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

    async def generate_candidate_pool(
        self,
        turns: list["Turn"],
        scenario_brief: str,
        phase_style: str,
        n: int = 4,
        constraint_suffix: Optional[str] = None,
        enable_trait_execution: bool = False,
    ) -> list[str]:
        """
        Generate a pool of N candidate responses for Best-of-N selection.

        Uses the same prompt and settings for each sample.
        """
        tasks = [
            self.generate_response(
                turns=turns,
                scenario_brief=scenario_brief,
                phase_style=phase_style,
                constraint_suffix=constraint_suffix,
                enable_trait_execution=enable_trait_execution,
            )
            for _ in range(n)
        ]
        return list(await asyncio.gather(*tasks))

    async def generate_policy_plan(
        self,
        turns: list["Turn"],
        scenario_brief: str,
        phase_name: Optional[str] = None,
        phase_cues: Optional[list[str]] = None,
        target_traits: Optional[list[str]] = None,
    ) -> dict:
        """
        Generate a latent policy plan (hierarchical persona scaffold).
        Used in BCFC v4.
        """
        recent_turns = turns[-8:] if len(turns) > 8 else turns
        history_lines = [f"{t.speaker_name}: {t.content}" for t in recent_turns]
        history = "\n".join(history_lines)

        phase_hint = f"Phase: {phase_name}" if phase_name else "Phase: unknown"
        cues_hint = f"Cues: {', '.join(phase_cues)}" if phase_cues else "Cues: none"
        traits_hint = f"Target traits: {', '.join(target_traits)}" if target_traits else "Target traits: none"

        prompt = f"""Given the discussion, output a compact JSON with fields:
stance (support/oppose/synthesize/probe),
goal_mode (influence/coordinate/protect/discover),
planning_depth (none/milestone/owner_deadline/contingency),
novelty_move (none/analogy/reframe/new_option/third_option),
social_tactic (empathize/challenge/persuade/mediate/align),
risk_posture (bold/balanced/cautious),
memory_focus (commitment/relation/identity/none).

Scenario: {scenario_brief}
{phase_hint}
{cues_hint}
{traits_hint}
Transcript:
{history}

Return JSON only."""

        try:
            resp = await self.client.generate(
                prompt=prompt,
                system_instruction="Return JSON only. Be concise.",
                temperature=0.3,
                max_tokens=200,
            )
        except Exception:
            return {
                "stance": "synthesize",
                "goal_mode": "coordinate",
                "planning_depth": "milestone",
                "novelty_move": "none",
                "social_tactic": "align",
                "risk_posture": "balanced",
                "memory_focus": "commitment",
            }

        # Best-effort JSON parse
        text = resp.strip()
        if "{" in text and "}" in text:
            text = text[text.find("{"):text.rfind("}") + 1]
        try:
            import json
            data = json.loads(text)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {
                "stance": "synthesize",
                "goal_mode": "coordinate",
                "planning_depth": "milestone",
                "novelty_move": "none",
                "social_tactic": "align",
                "risk_posture": "balanced",
                "memory_focus": "commitment",
            }

    async def generate_candidate_pool_styles(
        self,
        turns: list["Turn"],
        scenario_brief: str,
        phase_style: str,
        style_slots: list[str],
        phase_name: Optional[str] = None,
        phase_cues: Optional[list[str]] = None,
        target_traits: Optional[list[str]] = None,
        constraint_suffix: Optional[str] = None,
        policy_plan: Optional[dict] = None,
        enable_trait_execution: bool = False,
    ) -> list[dict]:
        """
        Generate candidates for best-of-styles selection (BCFC v3).
        Returns list of dicts: {slot, text, scaffold}.
        """
        if policy_plan is None:
            policy_plan = await self.generate_policy_plan(
                turns=turns,
                scenario_brief=scenario_brief,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
            )
        tasks = [
            self.generate_response(
                turns=turns,
                scenario_brief=scenario_brief,
                phase_style=phase_style,
                constraint_suffix=constraint_suffix,
                style_directive=slot,
                policy_plan=policy_plan,
                phase_name=phase_name,
                phase_cues=phase_cues,
                target_traits=target_traits,
                enable_trait_execution=enable_trait_execution,
            )
            for slot in style_slots
        ]
        texts = await asyncio.gather(*tasks)
        outputs: list[dict] = []
        for slot, text in zip(style_slots, texts):
            outputs.append({
                "slot": slot,
                "text": text,
                "policy_plan": policy_plan,
            })
        return outputs

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
