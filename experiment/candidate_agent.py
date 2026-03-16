"""
Experiment Candidate Agent: Automated candidate for behavioral fidelity testing.

Standalone agent (does NOT extend BaseAgent) that generates candidate responses
based on a personality system prompt. Used by BatchRunner to simulate candidates
with specific OCEAN profiles.
"""

import asyncio
import json
import logging
import os
import random
import re
from dataclasses import dataclass
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
DEFAULT_FALLBACK_RESPONSE = "I think we should consider all the options before deciding."

ALL_ACTION_TYPES = (
    "assign_owner", "commit_resource", "publish_update", "narrow_scope",
    "defer_decision", "set_deadline", "escalate", "allocate_budget",
    "audit_compliance", "preserve_autonomy", "request_evidence", "pilot", "none",
)

CANDIDATE_RESPONSE_SCHEMA_INSTRUCTION = """
Respond in JSON with this exact structure:
{
  "dialogue": "<your in-character response>",
  "intended_action": "<one of: assign_owner|commit_resource|publish_update|narrow_scope|defer_decision|set_deadline|escalate|allocate_budget|audit_compliance|preserve_autonomy|request_evidence|pilot|none>",
  "stance_shift": "<one of: maintain|soften|harden|pivot>"
}
"""


@dataclass
class GenerationPayload:
    text: str
    generation_meta: dict


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
        self._response_retry_attempts = max(
            1, int(os.getenv("SIM_CANDIDATE_RETRY_ATTEMPTS", "6"))
        )
        self._response_retry_base_delay = max(
            0.0, float(os.getenv("SIM_CANDIDATE_RETRY_BASE_DELAY", "1.0"))
        )
        self._response_retry_max_delay = max(
            self._response_retry_base_delay,
            float(os.getenv("SIM_CANDIDATE_RETRY_MAX_DELAY", "8.0")),
        )
        self._response_retry_jitter = max(
            0.0, float(os.getenv("SIM_CANDIDATE_RETRY_JITTER", "0.25"))
        )
        self._response_request_timeout_seconds = max(
            0.0, float(os.getenv("SIM_CANDIDATE_REQUEST_TIMEOUT_SECONDS", "60.0"))
        )
        self._pool_max_concurrency = max(
            1, int(os.getenv("SIM_CANDIDATE_POOL_MAX_CONCURRENCY", "2"))
        )

    @property
    def system_prompt(self) -> str:
        """Active system prompt = base + current nudge (if any)."""
        if self._current_nudge:
            return self._base_system_prompt + "\n\n" + self._current_nudge
        return self._base_system_prompt

    def update_nudge(self, nudge_text: Optional[str]):
        """Update the corrective nudge appended to system prompt."""
        self._current_nudge = nudge_text

    @staticmethod
    def _is_transient_generation_error(error: Exception) -> bool:
        if isinstance(error, asyncio.TimeoutError):
            return True
        text = str(error).lower()
        transient_hints = (
            "connection error",
            "rate limit",
            "timeout",
            "temporarily unavailable",
            "service unavailable",
            "too many requests",
            "429",
            "502",
            "503",
            "504",
        )
        return any(hint in text for hint in transient_hints)

    async def _generate_with_retry(
        self,
        *,
        prompt: str,
        system_instruction: str,
        temperature: float,
        max_tokens: int,
        operation_name: str,
        use_json_mode: bool = False,
    ) -> str:
        last_error: Exception | None = None
        for attempt in range(self._response_retry_attempts):
            try:
                gen_method = (
                    self.client.generate_structured
                    if use_json_mode
                    else self.client.generate
                )
                generation_coro = gen_method(
                    prompt=prompt,
                    system_instruction=system_instruction,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                if self._response_request_timeout_seconds > 0:
                    return await asyncio.wait_for(
                        generation_coro,
                        timeout=self._response_request_timeout_seconds,
                    )
                return await generation_coro
            except Exception as error:
                last_error = error
                is_transient = self._is_transient_generation_error(error)
                is_last_attempt = attempt >= self._response_retry_attempts - 1
                if not is_transient or is_last_attempt:
                    raise
                delay = min(
                    self._response_retry_base_delay * (2 ** attempt),
                    self._response_retry_max_delay,
                )
                if self._response_retry_jitter > 0 and delay > 0:
                    delay += delay * random.uniform(
                        -self._response_retry_jitter,
                        self._response_retry_jitter,
                    )
                    delay = max(0.0, delay)
                logger.warning(
                    "%s generation attempt %d/%d failed with transient error: %s. Retrying in %.1fs.",
                    operation_name,
                    attempt + 1,
                    self._response_retry_attempts,
                    error,
                    delay,
                )
                if delay > 0:
                    await asyncio.sleep(delay)
        if last_error is not None:
            raise last_error
        raise RuntimeError(f"{operation_name} generation failed without error details.")

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
        payload = await self.generate_response_payload(
            turns=turns,
            scenario_brief=scenario_brief,
            phase_style=phase_style,
            constraint_suffix=constraint_suffix,
            style_directive=style_directive,
            policy_plan=policy_plan,
            phase_name=phase_name,
            phase_cues=phase_cues,
            target_traits=target_traits,
            enable_trait_execution=enable_trait_execution,
        )
        return payload.text

    async def generate_response_payload(
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
        commitment_context: Optional[str] = None,
        use_json_mode: bool = False,
        slot_action_vocabulary: Optional[list[str]] = None,
    ) -> GenerationPayload:
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
        commitment_hint = commitment_context or ""

        # Build structured JSON instruction when JSON mode is enabled
        json_schema_instruction = ""
        if use_json_mode:
            if slot_action_vocabulary:
                action_list = "|".join(slot_action_vocabulary + ["none"])
                json_schema_instruction = (
                    f"\n\nRespond in JSON with this exact structure:\n"
                    f'{{"dialogue": "<your in-character response>", '
                    f'"intended_action": "<one of: {action_list}>", '
                    f'"stance_shift": "<one of: maintain|soften|harden|pivot>"}}'
                )
            else:
                json_schema_instruction = CANDIDATE_RESPONSE_SCHEMA_INSTRUCTION

        prompt = f"""Here is the recent conversation:

{history}
{style_hint}
{phase_hint}{cues_hint}{traits_hint}{style_hint_extra}{policy_text}{execution_hint}{commitment_hint}

Respond as {self.candidate_name} in this discussion. Keep your response natural, concise (1-3 sentences), and in character. Do not include your name as a prefix.{json_schema_instruction}"""

        # Append constraint suffix if requested (legacy hook; no regeneration in v1.1)
        if constraint_suffix:
            prompt += constraint_suffix

        # When using JSON mode, system instruction must mention JSON (OpenAI requirement)
        system_instruction = self.system_prompt
        if use_json_mode:
            system_instruction += "\n\nAlways respond in valid JSON."

        try:
            response = await self._generate_with_retry(
                prompt=prompt,
                system_instruction=system_instruction,
                temperature=0.7,
                max_tokens=250 if use_json_mode else 200,
                operation_name="candidate_response",
                use_json_mode=use_json_mode,
            )
        except Exception as e:
            logger.error(f"Candidate generation failed: {e}")
            return GenerationPayload(
                text=DEFAULT_FALLBACK_RESPONSE,
                generation_meta={
                    "used_fallback": True,
                    "fallback_type": self._fallback_type_for_error(e),
                    "fallback_reason": str(e),
                    "operation_name": "candidate_response",
                },
            )

        # Parse structured JSON response when JSON mode is enabled
        intended_action = None
        stance_shift = None
        if use_json_mode:
            try:
                text = response.strip()
                if "{" in text and "}" in text:
                    text = text[text.find("{"):text.rfind("}") + 1]
                parsed = json.loads(text)
                if isinstance(parsed, dict):
                    response = parsed.get("dialogue", response)
                    raw_action = parsed.get("intended_action", "none")
                    if raw_action in ALL_ACTION_TYPES:
                        intended_action = raw_action
                    stance_shift = parsed.get("stance_shift")
            except (json.JSONDecodeError, ValueError):
                # Fallback: treat entire response as dialogue text
                logger.debug("JSON parse failed for candidate response, using raw text")

        # Clean up the response
        response = response.strip()

        # Remove any "Candidate:" prefix the model might add
        response = re.sub(r"^(Candidate|CANDIDATE)\s*:\s*", "", response, flags=re.IGNORECASE)

        # Remove surrounding quotes if present
        if response.startswith('"') and response.endswith('"'):
            response = response[1:-1]

        # Strip stage directions that leak emotional state
        response = self._strip_stage_directions(response)

        return GenerationPayload(
            text=response.strip(),
            generation_meta={
                "used_fallback": False,
                "fallback_type": None,
                "fallback_reason": None,
                "operation_name": "candidate_response",
                "intended_action": intended_action,
                "stance_shift": stance_shift,
            },
        )

    @staticmethod
    def _fallback_type_for_error(error: Exception) -> str:
        if isinstance(error, asyncio.TimeoutError):
            return "timeout_fallback"
        lowered = str(error).lower()
        if "timeout" in lowered:
            return "timeout_fallback"
        if any(token in lowered for token in ("rate limit", "temporarily unavailable", "service unavailable", "too many requests", "429", "502", "503", "504", "connection error")):
            return "retry_exhausted_fallback"
        return "non_transient_fallback"

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
        async def _run_slot() -> str:
            return await self.generate_response(
                turns=turns,
                scenario_brief=scenario_brief,
                phase_style=phase_style,
                constraint_suffix=constraint_suffix,
                enable_trait_execution=enable_trait_execution,
            )

        return await self._gather_with_concurrency(
            [_run_slot for _ in range(n)],
            max_concurrency=min(self._pool_max_concurrency, n),
        )

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

        fallback_plan = {
            "stance": "synthesize",
            "goal_mode": "coordinate",
            "planning_depth": "milestone",
            "novelty_move": "none",
            "social_tactic": "align",
            "risk_posture": "balanced",
            "memory_focus": "commitment",
        }
        try:
            resp = await self._generate_with_retry(
                prompt=prompt,
                system_instruction="You are a policy plan generator. Respond in JSON only. Be concise.",
                temperature=0.3,
                max_tokens=200,
                operation_name="policy_plan",
                use_json_mode=True,
            )
        except Exception:
            return dict(fallback_plan)

        # Parse JSON response (json_object mode guarantees valid JSON)
        text = resp.strip()
        if "{" in text and "}" in text:
            text = text[text.find("{"):text.rfind("}") + 1]
        try:
            data = json.loads(text)
            return data if isinstance(data, dict) else dict(fallback_plan)
        except Exception:
            return dict(fallback_plan)

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
        max_concurrency_override: Optional[int] = None,
        commitment_context: Optional[str] = None,
        use_json_mode: bool = False,
        slot_action_vocabularies: Optional[dict[str, list[str]]] = None,
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
        async def _run_slot(slot: str) -> GenerationPayload:
            slot_vocab = (slot_action_vocabularies or {}).get(slot)
            return await self.generate_response_payload(
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
                commitment_context=commitment_context,
                use_json_mode=use_json_mode,
                slot_action_vocabulary=slot_vocab,
            )

        tasks = [lambda slot=slot: _run_slot(slot) for slot in style_slots]
        payloads = await self._gather_with_concurrency(
            tasks,
            max_concurrency=min(
                max_concurrency_override or self._pool_max_concurrency,
                len(style_slots),
            ),
        )
        outputs: list[dict] = []
        for slot, payload in zip(style_slots, payloads):
            meta = dict(payload.generation_meta)
            candidate_dict = {
                "slot": slot,
                "text": payload.text,
                "policy_plan": policy_plan,
                "generation_meta": meta,
            }
            # Promote structured fields to top-level for controller access
            if meta.get("intended_action"):
                candidate_dict["intended_action"] = meta["intended_action"]
            if meta.get("stance_shift"):
                candidate_dict["stance_shift"] = meta["stance_shift"]
            outputs.append(candidate_dict)
        surviving = [
            item for item in outputs
            if not item.get("generation_meta", {}).get("used_fallback", False)
        ]
        if surviving:
            return surviving
        if not outputs:
            return []
        first = dict(outputs[0])
        first["generation_meta"] = {
            **dict(first.get("generation_meta", {})),
            "used_fallback": True,
            "fallback_type": "empty_pool_fallback",
            "fallback_reason": "all_candidate_slots_fell_back",
            "operation_name": "candidate_pool",
        }
        return [first]

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

    async def _gather_with_concurrency(
        self,
        jobs: list,
        *,
        max_concurrency: int,
    ) -> list:
        if not jobs:
            return []

        semaphore = asyncio.Semaphore(max(1, max_concurrency))
        results: list = [None] * len(jobs)

        async def _run(index: int, job):
            async with semaphore:
                results[index] = await job()

        await asyncio.gather(*(_run(index, job) for index, job in enumerate(jobs)))
        return results
