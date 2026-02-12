"""
Trait Evaluator: Evidence-Based Personality Inference for Mode 2.

Evaluates group discussion transcripts for Big Five personality traits using:
- Per-trait evidence extraction with calibration notes
- Behavioral statistics for calibration
- Multi-model ensemble (3 judges) for consensus
- Facet-level breakdown for each trait

Every OCEAN score is traceable to specific transcript quotes.
"""

import asyncio
import statistics
from typing import TYPE_CHECKING

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

## Behavioral Statistics (Pre-Computed)
- Candidate average words per turn: {avg_words}
- Candidate turn count: {turn_count}
- Times candidate addressed others by name: {name_mentions}
- Times candidate asked questions: {questions}
- Times candidate expressed disagreement: {disagreements}
- Times candidate acknowledged others: {acknowledgments}

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
- Look for how candidate handles CONFLICT with Alex (the challenger)
- ABSENCE of pushback is evidence of HIGH Agreeableness
- Look for: "I see your point", "That's fair", accommodating others' views, seeking compromise
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
        # Format transcript
        transcript = self._format_transcript(turns, candidate_name)

        # Build prompt
        prompt = TRAIT_EVIDENCE_PROMPT.format(
            trait_name=trait.value.title(),
            candidate_name=candidate_name,
            transcript=transcript,
            avg_words=f"{stats.candidate_avg_words_per_turn:.1f}",
            turn_count=stats.candidate_turns,
            name_mentions=stats.times_addressed_others_by_name,
            questions=stats.times_asked_questions,
            disagreements=stats.times_expressed_disagreement,
            acknowledgments=stats.times_acknowledged_others,
            calibration_notes=CALIBRATION_NOTES[trait],
        )

        # Generate evaluation
        response = await self.client.generate(
            prompt=prompt,
            system_instruction="You are an expert personality psychologist. Be rigorous and cite specific evidence.",
            temperature=0.3,
            max_tokens=1000,
        )

        # Parse response
        result = self._parse_trait_response(response, trait)
        return result

    async def evaluate_ensemble(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
        models: list[str] = None,
    ) -> PersonalityAssessment:
        """
        Run multi-model ensemble evaluation.

        Uses 3 different "judges" (LLM passes with variation) to reduce bias.
        """
        # Run 3 passes with different temperatures
        results = await asyncio.gather(
            self.evaluate(turns, candidate_name, stats),
            self._evaluate_pass_2(turns, candidate_name, stats),
            self._evaluate_pass_3(turns, candidate_name, stats),
        )

        # Aggregate via median for each trait
        trait_scores = {}
        for trait in BigFiveTrait:
            scores = [
                getattr(r, trait.value).score
                for r in results
            ]
            median_score = statistics.median(scores)

            # Get evidence from all passes
            all_evidence = []
            for r in results:
                all_evidence.extend(getattr(r, trait.value).evidence)

            # Calculate confidence from agreement
            score_range = max(scores) - min(scores)
            confidence = 1.0 - score_range

            trait_scores[trait] = TraitScore(
                trait=trait,
                score=median_score,
                confidence=confidence,
                evidence=all_evidence[:5],  # Top 5 pieces of evidence
            )

        # Build final assessment
        return PersonalityAssessment(
            openness=trait_scores[BigFiveTrait.OPENNESS],
            conscientiousness=trait_scores[BigFiveTrait.CONSCIENTIOUSNESS],
            extraversion=trait_scores[BigFiveTrait.EXTRAVERSION],
            agreeableness=trait_scores[BigFiveTrait.AGREEABLENESS],
            neuroticism=trait_scores[BigFiveTrait.NEUROTICISM],
            overall_confidence=sum(ts.confidence for ts in trait_scores.values()) / 5,
        )

    async def _evaluate_pass_2(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
    ) -> PersonalityAssessment:
        """Second evaluation pass with different temperature."""
        # Temporarily increase temperature
        original_temp = 0.3
        trait_results = await asyncio.gather(*[
            self._evaluate_trait_with_temp(turns, candidate_name, stats, trait, 0.5)
            for trait in BigFiveTrait
        ])
        results = {trait: result for trait, result in zip(BigFiveTrait, trait_results)}
        return PersonalityAssessment(
            openness=results[BigFiveTrait.OPENNESS],
            conscientiousness=results[BigFiveTrait.CONSCIENTIOUSNESS],
            extraversion=results[BigFiveTrait.EXTRAVERSION],
            agreeableness=results[BigFiveTrait.AGREEABLENESS],
            neuroticism=results[BigFiveTrait.NEUROTICISM],
        )

    async def _evaluate_pass_3(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
    ) -> PersonalityAssessment:
        """Third evaluation pass with different temperature."""
        trait_results = await asyncio.gather(*[
            self._evaluate_trait_with_temp(turns, candidate_name, stats, trait, 0.6)
            for trait in BigFiveTrait
        ])
        results = {trait: result for trait, result in zip(BigFiveTrait, trait_results)}
        return PersonalityAssessment(
            openness=results[BigFiveTrait.OPENNESS],
            conscientiousness=results[BigFiveTrait.CONSCIENTIOUSNESS],
            extraversion=results[BigFiveTrait.EXTRAVERSION],
            agreeableness=results[BigFiveTrait.AGREEABLENESS],
            neuroticism=results[BigFiveTrait.NEUROTICISM],
        )

    async def _evaluate_trait_with_temp(
        self,
        turns: list[Turn],
        candidate_name: str,
        stats: GroupSessionStats,
        trait: BigFiveTrait,
        temperature: float,
    ) -> TraitScore:
        """Evaluate a trait with specific temperature."""
        transcript = self._format_transcript(turns, candidate_name)
        prompt = TRAIT_EVIDENCE_PROMPT.format(
            trait_name=trait.value.title(),
            candidate_name=candidate_name,
            transcript=transcript,
            avg_words=f"{stats.candidate_avg_words_per_turn:.1f}",
            turn_count=stats.candidate_turns,
            name_mentions=stats.times_addressed_others_by_name,
            questions=stats.times_asked_questions,
            disagreements=stats.times_expressed_disagreement,
            acknowledgments=stats.times_acknowledged_others,
            calibration_notes=CALIBRATION_NOTES[trait],
        )

        response = await self.client.generate(
            prompt=prompt,
            system_instruction="You are an expert personality psychologist.",
            temperature=temperature,
            max_tokens=1000,
        )
        return self._parse_trait_response(response, trait)

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

        except (json.JSONDecodeError, IndexError, KeyError):
            # Fallback: return neutral score
            return TraitScore(
                trait=trait,
                score=0.5,
                confidence=0.3,
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
