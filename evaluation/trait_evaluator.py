"""
Trait Evaluator: Evidence-Based Personality Inference for Mode 2.

V5.1 upgrades:
- Dual-order evaluation: Order A (transcript→features) and Order B (features→transcript)
  to control for LLM-as-judge presentation-order bias.
- Per-model median across both orders, then median across models.
- Judge diagnostics: order_effect, model_range, uncertain flag per trait.
- True multi-model ensemble: 5 models in parallel via generate_ensemble()
- Parse error logging with confidence=0.0 fallback (S6)

Every OCEAN score is traceable to specific transcript quotes.
"""

import asyncio
import logging
import statistics
from typing import TYPE_CHECKING, Optional

logger = logging.getLogger(__name__)

from experiment.behavioral_features import extract_features, BehavioralFeatures
from utils.models import (
    Turn,
    Evidence,
    BigFiveTrait,
    TraitScore,
    TraitFacetScore,
    PersonalityAssessment,
    GroupSessionStats,
)

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


# =============================================================================
# Prompt template sections (split for dual-order evaluation)
# =============================================================================

PROMPT_HEADER = """Analyze this group discussion transcript and extract evidence for the Big Five personality trait: **{trait_name}**

## Candidate Information
Candidate Name: {candidate_name}
"""

PROMPT_TRANSCRIPT = """## Transcript
{transcript}
"""

PROMPT_FEATURES = """## Behavioral Statistics (Pre-Computed, 30 Features)
### Volume & Verbosity
- Average words per turn: {avg_words}
- Max words in a turn: {max_words}
- Min words in a turn: {min_words}
- Word count variance (stdev): {word_variance}
- Candidate turn count: {turn_count}

### Social Engagement
- Name mentions (Alex/Jordan/Riley): {name_mentions}
- Questions asked (ratio): {question_ratio}
- Exclamation ratio: {exclamation_ratio}
- Turn initiation ratio: {initiation_ratio}
- Avg response latency rank: {latency_rank}

### Language Style
- Hedge count ("maybe", "I think", etc.): {hedges}
- Certainty count ("definitely", "clearly", etc.): {certainty}
- First-person pronoun ratio (I/me/my): {first_person}
- Inclusive pronoun ratio (we/our/us): {inclusive}
- Unique word ratio (vocabulary diversity): {unique_words}
- Long sentence ratio (>20 words): {long_sentences}

### Behavioral Signals
- Disagreement count: {disagreements}
- Acknowledgment count: {acknowledgments}
- New idea count: {ideas}
- Planning phrase count: {planning}
- Conditional ratio (if/should/would): {conditionals}
- Emotional word count (negative): {emotional}
- Positive emotion count: {positive_emotion}

### Conscientiousness Signals
- Structure marker count (numbered lists, ordering): {structure_markers}
- Reference-back count (citing earlier points): {reference_backs}
- Action item count (assignments, deadlines): {action_items}

### Openness Signals
- Hypothetical count (speculative scenarios): {hypotheticals}

### Neuroticism Signals
- Apology count: {apologies}
- Self-doubt count: {self_doubts}
- Reassurance-seeking count: {reassurance_seeking}

### Agreeableness Signals
- Negation count (no, not, won't, etc.): {negations}
"""

PROMPT_TAIL = """## Calibration Notes for {trait_name}
{calibration_notes}

## Instructions
1. Provide a score (0.0 - 1.0) for this trait
2. Extract 3-5 direct quotes from the CANDIDATE that support your score
3. For each quote, specify:
   - The exact text (verbatim)
   - Turn number
   - Which facet it demonstrates
   - Signal direction: "high" or "low" trait level
   - Signal strength: "weak", "moderate", or "strong"
4. Consider ABSENCE of behavior as evidence too

## Output Format (JSON)
{{
  "trait": "{trait_name}",
  "score": <0.0-1.0>,
  "confidence": <0.0-1.0>,
  "facets": [
    {{
      "facet_name": "<facet>",
      "score": <0.0-1.0>,
      "evidence": [
        {{
          "quote": "<exact text>",
          "turn_number": <number>,
          "signal_direction": "high" or "low",
          "signal_strength": "weak/moderate/strong"
        }}
      ]
    }}
  ],
  "overall_evidence": [
    {{
      "quote": "<exact text>",
      "turn_number": <number>,
      "demonstrates": "<what this shows>",
      "signal_direction": "high" or "low",
      "signal_strength": "weak/moderate/strong"
    }}
  ],
  "reasoning": "<explanation for the score>"
}}

IMPORTANT: Only quote the CANDIDATE's words, not the AI agents (Alex, Jordan, Riley)."""


def build_trait_prompt(kwargs: dict, order: str = "A") -> str:
    """
    Build the full trait evaluation prompt with configurable section order.

    Args:
        kwargs: Format kwargs from _build_prompt_kwargs().
        order: "A" = transcript then features, "B" = features then transcript.

    Returns:
        Fully formatted prompt string.
    """
    header = PROMPT_HEADER.format(**kwargs)
    transcript = PROMPT_TRANSCRIPT.format(**kwargs)
    features = PROMPT_FEATURES.format(**kwargs)
    tail = PROMPT_TAIL.format(**kwargs)

    if order == "A":
        return header + transcript + features + tail
    else:
        return header + features + transcript + tail


# Calibration notes for each trait
CALIBRATION_NOTES = {
    BigFiveTrait.OPENNESS: """
- Simply PARTICIPATING in a group discussion is NOT evidence of Openness
- Only rate O > 0.6 if the candidate actively explores hypotheticals, proposes creative alternatives, or engages with abstract ideas
- Look for: "what if...", "another way to think about this...", "imagine if..."
- Low O signals: Sticking only to practical/concrete points, dismissing novel ideas, preferring "proven" approaches
- High O facets: Imagination, Artistic interests, Emotionality, Adventurousness, Intellect, Liberalism
""",
    BigFiveTrait.CONSCIENTIOUSNESS: """
- Being ORGANIZED in a discussion is NOT sufficient for high Conscientiousness
- Most people sound somewhat organized. Only rate C > 0.7 if the candidate actively imposes additional structure
- Look for: Creating timelines, action items, follow-ups, checklists, explicit prioritization
- High C facets: Self-efficacy, Orderliness, Dutifulness, Achievement-striving, Self-discipline, Cautiousness
- Low C signals: Scattered responses, forgetting earlier points, no follow-through on commitments
""",
    BigFiveTrait.EXTRAVERSION: """
- Response LENGTH is a PRIMARY signal for Extraversion. Count words.
- Average < 15 words/turn = low E. Average > 40 words/turn = high E.
- Look for: Initiative in starting topics, elaboration beyond what's asked, engaging quiet members, asking questions
- High E facets: Friendliness, Gregariousness, Assertiveness, Activity level, Excitement-seeking, Cheerfulness
- Low E signals: Brief responses, waiting to be addressed, minimal elaboration
""",
    BigFiveTrait.AGREEABLENESS: """
AGREEABLENESS CALIBRATION (CRITICAL):
- A group discussion naturally encourages cooperation — DO NOT treat baseline
  politeness as evidence of high Agreeableness.
- Focus on DISAGREEMENT BEHAVIOR: How does the candidate handle conflict?
  Do they push back when challenged, or immediately accommodate?
- Key signals: disagreement_count ({disagreements}), acknowledgment_count ({acknowledgments})
- If disagreements < 2 AND acknowledgments > 3: likely high A
- If disagreements > 3 AND few accommodations: likely low A
- IMPORTANT: The ratio of disagreements to acknowledgments matters more
  than absolute counts. A candidate with 0 disagreements in a conflict
  phase is VERY high A, not just "normal."
- Low A signals: "I disagree", defending position firmly, not acknowledging others' points
- High A facets: Trust, Morality, Altruism, Cooperation, Modesty, Sympathy
""",
    BigFiveTrait.NEUROTICISM: """
- Look for stress response under pressure, especially during conflict phases
- Composure indicators: Calm language, staying focused, not defensive
- Anxiety indicators: "I'm not sure", hedging, apologetic tone, defensive responses
- High N facets: Anxiety, Anger, Depression, Self-consciousness, Immoderation, Vulnerability
- LOW Neuroticism is often positive: "no problem", "we can handle this", steady under pressure
""",
}


class TraitEvaluator:
    """
    Evaluates group discussions for Big Five personality traits.

    Uses evidence-based inference with calibration and multi-model ensemble.
    """

    def __init__(self, client: "LLMClient"):
        self.client = client

    def _build_prompt_kwargs(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
        trait: BigFiveTrait,
    ) -> dict:
        """Build format kwargs for the evaluation prompt with all 30 features."""
        transcript = self._format_transcript(turns, candidate_name)
        features = extract_features(turns, candidate_name)

        return {
            "trait_name": trait.value.title(),
            "candidate_name": candidate_name,
            "transcript": transcript,
            # Volume & Verbosity
            "avg_words": f"{features.avg_words_per_turn:.1f}",
            "max_words": features.max_words_in_turn,
            "min_words": features.min_words_in_turn,
            "word_variance": f"{features.word_count_variance:.1f}",
            "turn_count": stats.candidate_turns,
            # Social Engagement
            "name_mentions": features.name_mention_count,
            "question_ratio": f"{features.question_ratio:.2f}",
            "exclamation_ratio": f"{features.exclamation_ratio:.2f}",
            "initiation_ratio": f"{features.turn_initiation_ratio:.2f}",
            "latency_rank": f"{features.avg_response_latency_rank:.1f}",
            # Language Style
            "hedges": features.hedge_count,
            "certainty": features.certainty_count,
            "first_person": f"{features.first_person_ratio:.3f}",
            "inclusive": f"{features.inclusive_pronoun_ratio:.3f}",
            "unique_words": f"{features.unique_word_ratio:.3f}",
            "long_sentences": f"{features.long_sentence_ratio:.2f}",
            # Behavioral Signals
            "disagreements": features.disagreement_count,
            "acknowledgments": features.acknowledgment_count,
            "ideas": features.idea_count,
            "planning": features.planning_count,
            "conditionals": f"{features.conditional_ratio:.2f}",
            "emotional": features.emotional_word_count,
            "positive_emotion": features.positive_emotion_count,
            # New: Conscientiousness Signals
            "structure_markers": features.structure_marker_count,
            "reference_backs": features.reference_back_count,
            "action_items": features.action_item_count,
            # New: Openness Signals
            "hypotheticals": features.hypothetical_count,
            # New: Neuroticism Signals
            "apologies": features.apology_count,
            "self_doubts": features.self_doubt_count,
            "reassurance_seeking": features.reassurance_seeking_count,
            # New: Agreeableness Signals
            "negations": features.negation_count,
            # Calibration
            "calibration_notes": CALIBRATION_NOTES[trait].format(
                disagreements=features.disagreement_count,
                acknowledgments=features.acknowledgment_count,
            ) if trait == BigFiveTrait.AGREEABLENESS else CALIBRATION_NOTES[trait],
        }

    async def evaluate(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
    ) -> PersonalityAssessment:
        """
        Run full personality evaluation on a group discussion transcript.

        Args:
            turns: The conversation transcript
            candidate_name: Name of the candidate
            stats: Pre-computed behavioral statistics

        Returns:
            PersonalityAssessment with trait scores, evidence, and summary
        """
        # Evaluate all 5 traits in parallel
        trait_results = await asyncio.gather(*[
            self._evaluate_trait(turns, candidate_name, stats, trait)
            for trait in BigFiveTrait
        ])

        # Build results dict
        results = {trait: result for trait, result in zip(BigFiveTrait, trait_results)}

        # Calculate overall confidence
        confidences = [r.confidence for r in results.values()]
        overall_confidence = sum(confidences) / len(confidences)

        assessment = PersonalityAssessment(
            openness=results[BigFiveTrait.OPENNESS],
            conscientiousness=results[BigFiveTrait.CONSCIENTIOUSNESS],
            extraversion=results[BigFiveTrait.EXTRAVERSION],
            agreeableness=results[BigFiveTrait.AGREEABLENESS],
            neuroticism=results[BigFiveTrait.NEUROTICISM],
            overall_confidence=overall_confidence,
        )

        # Generate behavioral summary
        assessment.behavioral_summary = self._generate_summary(results)
        assessment.strengths = self._identify_trait_strengths(results)
        assessment.development_areas = self._identify_trait_areas(results)

        return assessment

    async def _evaluate_trait(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
        trait: BigFiveTrait,
    ) -> TraitScore:
        """Evaluate a single Big Five trait (single model, order A only)."""
        kwargs = self._build_prompt_kwargs(turns, candidate_name, stats, trait)
        prompt = build_trait_prompt(kwargs, order="A")

        response = await self.client.generate(
            prompt=prompt,
            system_instruction="You are an expert personality psychologist. Be rigorous and cite specific evidence.",
            temperature=0.3,
            max_tokens=3000,
        )

        result = self._parse_trait_response(response, trait)
        return result

    async def evaluate_ensemble(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
        models: Optional[list[str]] = None,
    ) -> PersonalityAssessment:
        """
        Run dual-order multi-model ensemble evaluation (V5.1).

        For each trait, sends two prompts (order A: transcript→features,
        order B: features→transcript) to all ensemble models in parallel.
        Per model: median(score_A, score_B). Final: median across models.

        Stores per_model_scores, per_model_order_scores, and judge_diagnostics
        in the assessment for downstream analysis.
        """
        # Evaluate all 5 traits with dual-order ensemble
        trait_results = await asyncio.gather(*[
            self._evaluate_trait_ensemble(turns, candidate_name, stats, trait, models=models)
            for trait in BigFiveTrait
        ])

        # Unpack: each result is (TraitScore, per_model_scores, per_model_order_scores, diagnostics)
        trait_scores = {}
        all_per_model: dict[str, dict[str, float]] = {}
        all_per_model_order: dict[str, dict[str, dict[str, float]]] = {}
        all_diagnostics: dict[str, dict] = {}
        uncertain_traits: list[str] = []
        uncertain_reasons: dict[str, list[str]] = {}

        trait_key_map = {
            BigFiveTrait.OPENNESS: "O",
            BigFiveTrait.CONSCIENTIOUSNESS: "C",
            BigFiveTrait.EXTRAVERSION: "E",
            BigFiveTrait.AGREEABLENESS: "A",
            BigFiveTrait.NEUROTICISM: "N",
        }

        for trait, (score, per_model, per_model_order, diag) in zip(BigFiveTrait, trait_results):
            trait_scores[trait] = score
            trait_abbrev = trait_key_map[trait]

            # Aggregate per-model scores (median across orders)
            for model_name, model_score in per_model.items():
                all_per_model.setdefault(model_name, {})[trait_abbrev] = model_score

            # Aggregate per-model order scores {model: {trait: {A: x, B: y}}}
            for model_name, order_scores in per_model_order.items():
                all_per_model_order.setdefault(model_name, {})[trait_abbrev] = order_scores

            # Per-trait diagnostics
            all_diagnostics[trait_abbrev] = diag

            # Track uncertain traits
            if diag.get("uncertain", False):
                uncertain_traits.append(trait_abbrev)
                reasons = []
                if diag["order_effect"] > 0.12:
                    reasons.append(f"order_effect>{diag['order_effect']:.2f}")
                if diag["model_range"] > 0.30:
                    reasons.append(f"model_range>{diag['model_range']:.2f}")
                if diag["parse_errors"] >= 2:
                    reasons.append(f"parse_errors={diag['parse_errors']}")
                uncertain_reasons[trait_abbrev] = reasons

        judge_diagnostics = {
            "per_trait": all_diagnostics,
            "uncertain_traits": uncertain_traits,
            "uncertain_reasons": uncertain_reasons,
        }

        assessment = PersonalityAssessment(
            openness=trait_scores[BigFiveTrait.OPENNESS],
            conscientiousness=trait_scores[BigFiveTrait.CONSCIENTIOUSNESS],
            extraversion=trait_scores[BigFiveTrait.EXTRAVERSION],
            agreeableness=trait_scores[BigFiveTrait.AGREEABLENESS],
            neuroticism=trait_scores[BigFiveTrait.NEUROTICISM],
            overall_confidence=sum(ts.confidence for ts in trait_scores.values()) / 5,
            per_model_scores=all_per_model,
            per_model_order_scores=all_per_model_order,
            judge_diagnostics=judge_diagnostics,
        )

        # Generate summary and strengths/areas
        assessment.behavioral_summary = self._generate_summary(trait_scores)
        assessment.strengths = self._identify_trait_strengths(trait_scores)
        assessment.development_areas = self._identify_trait_areas(trait_scores)

        return assessment

    async def _evaluate_trait_ensemble(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
        trait: BigFiveTrait,
        models: Optional[list[str]] = None,
    ) -> tuple[TraitScore, dict[str, float], dict[str, dict[str, float]], dict]:
        """
        Evaluate a single trait using dual-order multi-model ensemble (V5.1).

        For each trait, sends two prompts (order A and B) to all ensemble models.
        Per model: median(score_A, score_B). Final: median across models.

        Returns:
            (TraitScore, per_model_scores, per_model_order_scores, diagnostics)
            - per_model_scores: {model_name: median_score}
            - per_model_order_scores: {model_name: {"A": score_a, "B": score_b}}
            - diagnostics: {order_effect, model_range, parse_errors, uncertain}
        """
        kwargs = self._build_prompt_kwargs(turns, candidate_name, stats, trait)
        prompt_a = build_trait_prompt(kwargs, order="A")
        prompt_b = build_trait_prompt(kwargs, order="B")

        system_instruction = "You are an expert personality psychologist. Be rigorous and cite specific evidence."

        try:
            # Send both orders to all models in parallel
            resp_a, resp_b = await asyncio.gather(
                self.client.generate_ensemble(
                    prompt=prompt_a,
                    system_instruction=system_instruction,
                    temperature=0.3,
                    max_tokens=3000,
                    models=models,
                ),
                self.client.generate_ensemble(
                    prompt=prompt_b,
                    system_instruction=system_instruction,
                    temperature=0.3,
                    max_tokens=3000,
                    models=models,
                ),
            )
        except RuntimeError:
            logger.error(f"Ensemble failed for {trait.value}, falling back to single model")
            result = await self._evaluate_trait(turns, candidate_name, stats, trait)
            return (
                result,
                {"fallback": result.score},
                {"fallback": {"A": result.score, "B": result.score}},
                {"order_effect": 0.0, "model_range": 0.0, "parse_errors": 0, "uncertain": False},
            )

        # Parse responses and align by model name
        scores_by_model: dict[str, dict[str, float]] = {}
        parse_errors = 0
        all_evidence = []
        all_facets = []

        for model_name, response in resp_a:
            result = self._parse_trait_response(response, trait)
            if result.confidence <= 0.0 and result.score == 0.5:
                parse_errors += 1
                logger.warning(f"Parse error for {trait.value} order A from {model_name}")
            scores_by_model.setdefault(model_name, {})["A"] = result.score
            all_evidence.extend(result.evidence)
            all_facets.extend(result.facets)

        for model_name, response in resp_b:
            result = self._parse_trait_response(response, trait)
            if result.confidence <= 0.0 and result.score == 0.5:
                parse_errors += 1
                logger.warning(f"Parse error for {trait.value} order B from {model_name}")
            scores_by_model.setdefault(model_name, {})["B"] = result.score
            all_evidence.extend(result.evidence)
            all_facets.extend(result.facets)

        # Per-model: median across both orders
        model_scores = []
        order_deltas = []
        per_model_scores: dict[str, float] = {}
        per_model_order_scores: dict[str, dict[str, float]] = {}

        for model_name, d in scores_by_model.items():
            per_model_order_scores[model_name] = d
            if "A" in d and "B" in d:
                s = statistics.median([d["A"], d["B"]])
                model_scores.append(s)
                order_deltas.append(abs(d["A"] - d["B"]))
                per_model_scores[model_name] = s
            elif "A" in d:
                model_scores.append(d["A"])
                per_model_scores[model_name] = d["A"]
            elif "B" in d:
                model_scores.append(d["B"])
                per_model_scores[model_name] = d["B"]

        if not model_scores:
            empty_diag = {
                "order_effect": 0.0,
                "model_range": 1.0,
                "parse_errors": parse_errors,
                "uncertain": True,
                "confidence": 0.0,
            }
            return TraitScore(trait=trait, score=0.5, confidence=0.0), {}, {}, empty_diag

        # Final trait score: median across models
        trait_score_value = statistics.median(model_scores)

        # Diagnostics
        order_effect = statistics.median(order_deltas) if order_deltas else 0.0
        model_range = max(model_scores) - min(model_scores) if len(model_scores) > 1 else 0.0
        uncertain = order_effect > 0.12 or model_range > 0.30 or parse_errors >= 2

        # Confidence: 1.0 - model_range, penalized by parse errors
        confidence = max(0.0, 1.0 - model_range)
        if parse_errors > 0:
            total_responses = len(resp_a) + len(resp_b)
            confidence *= (1.0 - parse_errors / max(total_responses, 1))

        diagnostics = {
            "order_effect": round(order_effect, 4),
            "model_range": round(model_range, 4),
            "parse_errors": parse_errors,
            "uncertain": uncertain,
            "confidence": round(confidence, 4),
        }

        trait_score = TraitScore(
            trait=trait,
            score=trait_score_value,
            confidence=confidence,
            evidence=all_evidence[:5],
            facets=all_facets[:6],
        )
        return trait_score, per_model_scores, per_model_order_scores, diagnostics

    def _format_transcript(self, turns: list[Turn], candidate_name: str) -> str:
        """Format transcript for evaluation prompt."""
        lines = []
        for turn in turns:
            if turn.speaker_name == candidate_name:
                speaker = "CANDIDATE"
            else:
                speaker = turn.speaker_name.upper()
            lines.append(f"[Turn {turn.turn_number}] {speaker}: {turn.content}")
        return "\n\n".join(lines)

    def _parse_trait_response(self, response: str, trait: BigFiveTrait) -> TraitScore:
        """Parse the LLM's JSON trait evaluation response."""
        import json

        try:
            # Extract JSON
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                json_str = response.split("```")[1].split("```")[0]
            else:
                json_str = response

            result = json.loads(json_str.strip())

            # Build evidence list
            evidence = []
            for ev in result.get("overall_evidence", []):
                evidence.append(Evidence(
                    quote=ev.get("quote", ""),
                    turn_number=ev.get("turn_number", 0),
                    demonstrates=ev.get("demonstrates", ""),
                    signal_direction=ev.get("signal_direction", "neutral"),
                    signal_strength=ev.get("signal_strength", "moderate"),
                ))

            # Build facet list
            facets = []
            for facet in result.get("facets", []):
                facet_evidence = [
                    Evidence(
                        quote=e.get("quote", ""),
                        turn_number=e.get("turn_number", 0),
                        demonstrates=e.get("demonstrates", facet.get("facet_name", "")),
                        signal_direction=e.get("signal_direction", "neutral"),
                        signal_strength=e.get("signal_strength", "moderate"),
                    )
                    for e in facet.get("evidence", [])
                ]
                facets.append(TraitFacetScore(
                    facet_name=facet.get("facet_name", ""),
                    score=facet.get("score", 0.5),
                    evidence=facet_evidence,
                ))

            return TraitScore(
                trait=trait,
                score=result.get("score", 0.5),
                confidence=result.get("confidence", 0.5),
                facets=facets,
                evidence=evidence,
            )

        except (json.JSONDecodeError, IndexError, KeyError, AttributeError, TypeError) as e:
            # S6: Log parse errors, return neutral score with zero confidence
            logger.warning(f"Parse error for {trait.value}: {e}. Response: {response[:200]}")
            return TraitScore(
                trait=trait,
                score=0.5,
                confidence=0.0,
            )

    def _generate_summary(self, results: dict[BigFiveTrait, TraitScore]) -> str:
        """Generate a behavioral summary from trait scores."""
        summaries = []

        # Extraversion summary
        e_score = results[BigFiveTrait.EXTRAVERSION].score
        if e_score > 0.7:
            summaries.append("Highly engaged communicator, took initiative frequently")
        elif e_score < 0.3:
            summaries.append("Reserved participant, preferred listening over speaking")

        # Agreeableness summary
        a_score = results[BigFiveTrait.AGREEABLENESS].score
        if a_score > 0.7:
            summaries.append("Collaborative and accommodating in conflict situations")
        elif a_score < 0.3:
            summaries.append("Assertive in defending positions, comfortable with disagreement")

        # Neuroticism summary
        n_score = results[BigFiveTrait.NEUROTICISM].score
        if n_score > 0.6:
            summaries.append("Showed some stress signals under pressure")
        elif n_score < 0.4:
            summaries.append("Maintained composure throughout, steady under pressure")

        return "; ".join(summaries) if summaries else "Balanced personality profile"

    def _identify_trait_strengths(self, results: dict[BigFiveTrait, TraitScore]) -> list[str]:
        """Identify notable positive traits."""
        strengths = []
        if results[BigFiveTrait.AGREEABLENESS].score > 0.7:
            strengths.append("Strong collaboration skills")
        if results[BigFiveTrait.NEUROTICISM].score < 0.4:
            strengths.append("Excellent composure under pressure")
        if results[BigFiveTrait.OPENNESS].score > 0.7:
            strengths.append("Creative and open to new ideas")
        if results[BigFiveTrait.CONSCIENTIOUSNESS].score > 0.7:
            strengths.append("Highly organized and detail-oriented")
        return strengths

    def _identify_trait_areas(self, results: dict[BigFiveTrait, TraitScore]) -> list[str]:
        """Identify potential development areas."""
        areas = []
        if results[BigFiveTrait.EXTRAVERSION].score < 0.4:
            areas.append("Could increase engagement and initiative")
        if results[BigFiveTrait.AGREEABLENESS].score > 0.85:
            areas.append("May over-accommodate (consider being more assertive)")
        if results[BigFiveTrait.NEUROTICISM].score > 0.7:
            areas.append("Stress management under pressure")
        return areas


async def evaluate_group_session(
    client: "LLMClient",
    turns: list[Turn],
    candidate_name: str,
    stats: GroupSessionStats,
    use_ensemble: bool = True,
    escalate: bool = False,
) -> PersonalityAssessment:
    """Convenience function to evaluate a group discussion session."""
    evaluator = TraitEvaluator(client)
    if use_ensemble:
        assessment = await evaluator.evaluate_ensemble(turns, candidate_name, stats)

        if not escalate:
            return assessment

        from experiment.bcfc_config import DEFAULT_CONFIG

        # Determine whether escalation is needed
        diag = assessment.judge_diagnostics or {}
        per_trait = diag.get("per_trait", {})
        uncertain_traits = diag.get("uncertain_traits", [])
        usage_before = client.get_usage() if hasattr(client, "get_usage") else None

        need_escalation = False
        if DEFAULT_CONFIG.escalation_uncertain_only and uncertain_traits:
            need_escalation = True

        # Confidence/model range triggers
        for trait_abbrev, tdiag in per_trait.items():
            if tdiag.get("model_range", 0) > DEFAULT_CONFIG.escalation_model_range_threshold:
                need_escalation = True
            if tdiag.get("confidence", 1.0) < DEFAULT_CONFIG.escalation_confidence_threshold:
                need_escalation = True

        if need_escalation and getattr(client, "ensemble_models_extra", None):
            models = client.ensemble_models + client.ensemble_models_extra
            escalated = await evaluator.evaluate_ensemble(
                turns, candidate_name, stats, models=models
            )
            extra_prompt = extra_completion = extra_total = None
            if usage_before and hasattr(client, "get_usage"):
                usage_after = client.get_usage()
                extra_prompt = usage_after.get("prompt_tokens", 0) - usage_before.get("prompt_tokens", 0)
                extra_completion = usage_after.get("completion_tokens", 0) - usage_before.get("completion_tokens", 0)
                extra_total = usage_after.get("total_tokens", 0) - usage_before.get("total_tokens", 0)
            diag["escalation"] = {
                "triggered": True,
                "models": models,
                "overall_confidence": escalated.overall_confidence,
                "inferred_vector": escalated.to_vector().to_dict(),
                "per_model_scores": escalated.per_model_scores,
                "per_model_order_scores": escalated.per_model_order_scores,
                "extra_prompt_tokens": extra_prompt,
                "extra_completion_tokens": extra_completion,
                "extra_total_tokens": extra_total,
            }
            assessment.judge_diagnostics = diag
        else:
            diag["escalation"] = {
                "triggered": False,
                "models": getattr(client, "ensemble_models_extra", []),
                "extra_prompt_tokens": 0,
                "extra_completion_tokens": 0,
                "extra_total_tokens": 0,
            }
            assessment.judge_diagnostics = diag

        return assessment

    return await evaluator.evaluate(turns, candidate_name, stats)
