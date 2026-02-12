"""
Logic Evaluator: 3-Pass Citation-Based Evaluation for Mode 1.

Evaluates case study interview transcripts on 6 dimensions using:
- Explicit rubric anchors for each score level
- Direct quote extraction as evidence
- 3 independent LLM evaluation passes
- Aggregation via median with agreement metrics

Each score is backed by specific transcript quotes, enabling transparent
and auditable candidate evaluation.
"""

import asyncio
import statistics
from typing import TYPE_CHECKING

from config.logic_rubric import (
    LOGIC_RUBRIC,
    LogicDimension,
    get_level_description,
    get_evidence_signals,
)
from utils.models import (
    Turn,
    Evidence,
    LogicDimensionScore,
    LogicAssessment,
)

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


# Evaluation prompt template
LOGIC_EVALUATOR_PROMPT = """You are evaluating a case study interview transcript.

## Candidate Information
Candidate Name: {candidate_name}

## Transcript
{transcript}

## Task
Score the candidate on the dimension: **{dimension_name}**

### Dimension Definition
{dimension_definition}

### Observable Behaviors
{observable_behaviors}

### Scoring Rubric
{rubric_levels}

## Instructions
1. Assign a score (1-5) based on the rubric anchors above
2. Provide 2-4 DIRECT QUOTES from the candidate's responses that justify your score
3. Each quote must include:
   - The exact quoted text (verbatim, max 2 sentences)
   - The turn number where it appears
   - What the quote demonstrates
4. Note any ABSENT behaviors - things you expected to see but didn't

## Output Format (JSON)
{{
  "score": <1-5>,
  "confidence": <0.0-1.0>,
  "supporting_evidence": [
    {{
      "quote": "<exact text from candidate>",
      "turn_number": <number>,
      "demonstrates": "<what this shows>"
    }}
  ],
  "absent_behaviors": ["<behavior expected but not seen>"],
  "rubric_justification": "<why this score level was chosen>"
}}

IMPORTANT: Only quote the CANDIDATE's words, not the Facilitator's. Be specific and cite turn numbers."""


class LogicEvaluator:
    """
    Evaluates case study interviews using 3-pass citation-based scoring.

    Each dimension is evaluated independently by 3 LLM passes,
    then aggregated via median to reduce variance.
    """

    def __init__(self, client: "LLMClient"):
        self.client = client

    async def evaluate(
        self,
        turns: list[Turn],
        candidate_name: str,
    ) -> LogicAssessment:
        """
        Run full evaluation on a case study transcript.

        Args:
            turns: The conversation transcript
            candidate_name: Name of the candidate

        Returns:
            LogicAssessment with scores, evidence, and summary
        """
        # Run 3 passes for each dimension in parallel
        dimension_results = await asyncio.gather(*[
            self._evaluate_dimension_3pass(turns, candidate_name, dimension)
            for dimension in LogicDimension
        ])

        # Build assessment from results
        results_dict = {
            dimension: result
            for dimension, result in zip(LogicDimension, dimension_results)
        }

        assessment = LogicAssessment(
            problem_structuring=results_dict[LogicDimension.PROBLEM_STRUCTURING],
            hypothesis_thinking=results_dict[LogicDimension.HYPOTHESIS_THINKING],
            quantitative_reasoning=results_dict[LogicDimension.QUANTITATIVE_REASONING],
            data_synthesis=results_dict[LogicDimension.DATA_SYNTHESIS],
            recommendation_quality=results_dict[LogicDimension.RECOMMENDATION_QUALITY],
            communication_clarity=results_dict[LogicDimension.COMMUNICATION_CLARITY],
        )

        # Generate summary
        assessment.strengths = self._identify_strengths(results_dict)
        assessment.development_areas = self._identify_development_areas(results_dict)

        return assessment

    async def _evaluate_dimension_3pass(
        self,
        turns: list[Turn],
        candidate_name: str,
        dimension: LogicDimension,
    ) -> LogicDimensionScore:
        """Run 3 independent evaluation passes for one dimension."""
        # Run 3 passes in parallel
        results = await asyncio.gather(
            self._single_pass(turns, candidate_name, dimension, pass_id=1),
            self._single_pass(turns, candidate_name, dimension, pass_id=2),
            self._single_pass(turns, candidate_name, dimension, pass_id=3),
        )

        # Aggregate results
        scores = [r["score"] for r in results]
        median_score = int(statistics.median(scores))
        score_range = max(scores) - min(scores)
        agreement = "high" if score_range <= 1 else "low"

        # Combine evidence from all passes (deduplicate by turn number)
        seen_turns = set()
        combined_evidence = []
        for result in results:
            for ev in result.get("supporting_evidence", []):
                turn_num = ev.get("turn_number", 0)
                if turn_num not in seen_turns:
                    seen_turns.add(turn_num)
                    combined_evidence.append(Evidence(
                        quote=ev.get("quote", ""),
                        turn_number=turn_num,
                        demonstrates=ev.get("demonstrates", ""),
                    ))

        # Combine absent behaviors
        all_absent = set()
        for result in results:
            all_absent.update(result.get("absent_behaviors", []))

        # Build justification
        justification = f"Scored {median_score}/5 ({agreement} agreement across 3 passes). "
        justification += results[0].get("rubric_justification", "")

        return LogicDimensionScore(
            dimension=dimension.value,
            score=median_score,
            confidence=1.0 - (score_range / 4.0),  # Higher range = lower confidence
            evidence=combined_evidence,
            absent_behaviors=list(all_absent),
            rubric_justification=justification,
        )

    async def _single_pass(
        self,
        turns: list[Turn],
        candidate_name: str,
        dimension: LogicDimension,
        pass_id: int,
    ) -> dict:
        """Run a single evaluation pass for one dimension."""
        # Format transcript
        transcript = self._format_transcript(turns, candidate_name)

        # Get rubric info
        rubric = LOGIC_RUBRIC[dimension]
        dimension_name = dimension.value.replace("_", " ").title()
        observable_behaviors = "\n".join(f"- {b}" for b in rubric.observable_behaviors)

        # Format rubric levels
        rubric_levels = []
        for score in range(1, 6):
            level = rubric.levels[score]
            signals = "\n    ".join(f"• {s}" for s in level.evidence_signals)
            rubric_levels.append(f"""
**Score {score} - {level.name}**
{level.description}
Evidence signals:
    {signals}
""")
        rubric_levels_str = "\n".join(rubric_levels)

        # Build prompt
        prompt = LOGIC_EVALUATOR_PROMPT.format(
            candidate_name=candidate_name,
            transcript=transcript,
            dimension_name=dimension_name,
            dimension_definition=rubric.definition,
            observable_behaviors=observable_behaviors,
            rubric_levels=rubric_levels_str,
        )

        # Generate evaluation
        response = await self.client.generate(
            prompt=prompt,
            system_instruction="You are an expert case interview evaluator. Be rigorous and cite specific evidence.",
            temperature=0.4,  # Some variance for multi-pass
            max_tokens=800,
        )

        # Parse JSON response
        return self._parse_evaluation_response(response)

    def _format_transcript(self, turns: list[Turn], candidate_name: str) -> str:
        """Format transcript for evaluation prompt."""
        lines = []
        for turn in turns:
            role = "CANDIDATE" if turn.speaker_name == candidate_name else turn.speaker_name.upper()
            lines.append(f"[Turn {turn.turn_number}] {role}: {turn.content}")
        return "\n\n".join(lines)

    def _parse_evaluation_response(self, response: str) -> dict:
        """Parse the LLM's JSON evaluation response."""
        import json

        # Try to extract JSON from response
        try:
            # Look for JSON block
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                json_str = response.split("```")[1].split("```")[0]
            else:
                # Assume entire response is JSON
                json_str = response

            result = json.loads(json_str.strip())
            return result
        except (json.JSONDecodeError, IndexError):
            # Fallback: return minimal structure
            return {
                "score": 3,
                "confidence": 0.5,
                "supporting_evidence": [],
                "absent_behaviors": [],
                "rubric_justification": "Could not parse evaluation response.",
            }

    def _identify_strengths(self, results: dict[LogicDimension, LogicDimensionScore]) -> list[str]:
        """Identify top strengths (scores >= 4)."""
        strengths = []
        for dimension, score_obj in results.items():
            if score_obj.score >= 4:
                dim_name = dimension.value.replace("_", " ").title()
                strengths.append(f"{dim_name} ({score_obj.score}/5)")
        return strengths

    def _identify_development_areas(self, results: dict[LogicDimension, LogicDimensionScore]) -> list[str]:
        """Identify development areas (scores <= 2)."""
        areas = []
        for dimension, score_obj in results.items():
            if score_obj.score <= 2:
                dim_name = dimension.value.replace("_", " ").title()
                areas.append(f"{dim_name} ({score_obj.score}/5)")
        return areas


async def evaluate_case_session(
    client: "LLMClient",
    turns: list[Turn],
    candidate_name: str,
) -> LogicAssessment:
    """Convenience function to evaluate a case study session."""
    evaluator = LogicEvaluator(client)
    return await evaluator.evaluate(turns, candidate_name)
