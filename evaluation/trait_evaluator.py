"""
Trait Evaluator: Evidence-Based Personality Inference for Mode 2.

V4 upgrades:
- True multi-model ensemble: DeepSeek V3 + Gemini 2.5 Flash + Grok 4.1 Fast
- Same prompt sent to all 3 models in parallel via generate_ensemble()
- Aggregation: median score per trait, confidence = 1.0 - range
- Per-model scores stored for analysis
- Parse error logging with confidence=0.0 fallback (S6)

Every OCEAN score is traceable to specific transcript quotes.
"""

import asyncio
import logging
import statistics
from typing import TYPE_CHECKING

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


# Trait evidence extraction prompt
TRAIT_EVIDENCE_PROMPT = """Analyze this group discussion transcript and extract evidence for the Big Five personality trait: **{trait_name}**

## Candidate Information
Candidate Name: {candidate_name}

## Transcript
{transcript}

## Behavioral Statistics (Pre-Computed, 22 Features)
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

## Calibration Notes for {trait_name}
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
        """Build format kwargs for the evaluation prompt with all 22 features."""
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
        """Evaluate a single Big Five trait."""
        # Build prompt with all 22 features
        kwargs = self._build_prompt_kwargs(turns, candidate_name, stats, trait)
        prompt = TRAIT_EVIDENCE_PROMPT.format(**kwargs)

        # Generate evaluation
        response = await self.client.generate(
            prompt=prompt,
            system_instruction="You are an expert personality psychologist. Be rigorous and cite specific evidence.",
            temperature=0.3,
            max_tokens=3000,
        )

        # Parse response
        result = self._parse_trait_response(response, trait)
        return result

    async def evaluate_ensemble(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
    ) -> PersonalityAssessment:
        """
        Run true multi-model ensemble evaluation.

        Sends the same prompt to 3 different models (DeepSeek, Gemini, Grok)
        in parallel for each trait. Aggregates via median score.
        Confidence = 1.0 - score_range across models.

        Per-model scores are stored in the assessment for analysis.
        """
        # Evaluate all 5 traits with ensemble
        trait_results = await asyncio.gather(*[
            self._evaluate_trait_ensemble(turns, candidate_name, stats, trait)
            for trait in BigFiveTrait
        ])

        # Unpack: each result is (TraitScore, per_model_dict)
        trait_scores = {}
        all_per_model: dict[str, dict[str, float]] = {}
        trait_key_map = {
            BigFiveTrait.OPENNESS: "O",
            BigFiveTrait.CONSCIENTIOUSNESS: "C",
            BigFiveTrait.EXTRAVERSION: "E",
            BigFiveTrait.AGREEABLENESS: "A",
            BigFiveTrait.NEUROTICISM: "N",
        }

        for trait, (score, per_model) in zip(BigFiveTrait, trait_results):
            trait_scores[trait] = score
            trait_abbrev = trait_key_map[trait]
            for model_name, model_score in per_model.items():
                if model_name not in all_per_model:
                    all_per_model[model_name] = {}
                all_per_model[model_name][trait_abbrev] = model_score

        assessment = PersonalityAssessment(
            openness=trait_scores[BigFiveTrait.OPENNESS],
            conscientiousness=trait_scores[BigFiveTrait.CONSCIENTIOUSNESS],
            extraversion=trait_scores[BigFiveTrait.EXTRAVERSION],
            agreeableness=trait_scores[BigFiveTrait.AGREEABLENESS],
            neuroticism=trait_scores[BigFiveTrait.NEUROTICISM],
            overall_confidence=sum(ts.confidence for ts in trait_scores.values()) / 5,
            per_model_scores=all_per_model,
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
    ) -> tuple[TraitScore, dict[str, float]]:
        """
        Evaluate a single trait using multi-model ensemble.

        Sends the same prompt to all ensemble models in parallel.
        Returns (TraitScore, per_model_scores_dict) where per_model_scores_dict
        maps model_name -> score for this trait.
        """
        kwargs = self._build_prompt_kwargs(turns, candidate_name, stats, trait)
        prompt = TRAIT_EVIDENCE_PROMPT.format(**kwargs)

        system_instruction = "You are an expert personality psychologist. Be rigorous and cite specific evidence."

        try:
            # Send to all models in parallel
            model_responses = await self.client.generate_ensemble(
                prompt=prompt,
                system_instruction=system_instruction,
                temperature=0.3,
                max_tokens=3000,
            )
        except RuntimeError:
            # All models failed — fallback to single model
            logger.error(f"Ensemble failed for {trait.value}, falling back to single model")
            result = await self._evaluate_trait(turns, candidate_name, stats, trait)
            return result, {"fallback": result.score}

        # Parse each model's response
        parsed_results = []
        per_model_scores: dict[str, float] = {}
        parse_errors = 0
        for model_name, response in model_responses:
            result = self._parse_trait_response(response, trait)
            if result.confidence <= 0.0 and result.score == 0.5:
                # Parse failure — flag but include
                parse_errors += 1
                logger.warning(f"Parse error for {trait.value} from model {model_name}")
            parsed_results.append((model_name, result))
            per_model_scores[model_name] = result.score

        if not parsed_results:
            return TraitScore(trait=trait, score=0.5, confidence=0.0), per_model_scores

        # Aggregate: median score
        scores = [r.score for _, r in parsed_results]
        median_score = statistics.median(scores)

        # Confidence: 1.0 - range (higher agreement = higher confidence)
        score_range = max(scores) - min(scores)
        confidence = max(0.0, 1.0 - score_range)

        # If parse errors occurred, reduce confidence
        if parse_errors > 0:
            confidence *= (1.0 - parse_errors / len(parsed_results))

        # Collect evidence from all models
        all_evidence = []
        all_facets = []
        for _, result in parsed_results:
            all_evidence.extend(result.evidence)
            all_facets.extend(result.facets)

        trait_score = TraitScore(
            trait=trait,
            score=median_score,
            confidence=confidence,
            evidence=all_evidence[:5],
            facets=all_facets[:6],
        )
        return trait_score, per_model_scores

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

        except (json.JSONDecodeError, IndexError, KeyError) as e:
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
) -> PersonalityAssessment:
    """Convenience function to evaluate a group discussion session."""
    evaluator = TraitEvaluator(client)
    if use_ensemble:
        return await evaluator.evaluate_ensemble(turns, candidate_name, stats)
    return await evaluator.evaluate(turns, candidate_name, stats)
