"""
Ensemble Personality Detector for Multi-Model OCEAN Inference.

Runs FacetDetector with multiple LLM models and aggregates results
to produce more robust personality assessments.

Models used (via OpenRouter):
1. DeepSeek V3 (deepseek/deepseek-chat-v3-0324)
2. Claude Haiku 3.5 (anthropic/claude-3.5-haiku)
3. Gemini Flash 2.0 (google/gemini-2.0-flash-001)
"""

import asyncio
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from utils.models import Turn, PersonalityVector
from pipeline.facet_detector import FacetDetector, FacetAssessment

if TYPE_CHECKING:
    from clients.llm_client import LLMClient


# Default models for ensemble
ENSEMBLE_MODELS = [
    "deepseek/deepseek-chat-v3-0324",
    "anthropic/claude-3.5-haiku",
    "google/gemini-2.0-flash-001",
]


@dataclass
class EvidenceItem:
    """A single piece of evidence for a personality trait."""
    trait: str
    facet: str
    quote: str
    turn_number: int
    signal_strength: float
    reasoning: str


@dataclass
class ModelResult:
    """Result from a single model."""
    model_name: str
    ocean_scores: PersonalityVector
    ocean_confidence: dict[str, float]
    evidence_count: int
    evidence: list[EvidenceItem] = field(default_factory=list)
    success: bool = True
    error: Optional[str] = None


@dataclass
class StrengthWeakness:
    """A strength or weakness with supporting evidence."""
    trait: str
    type: str  # "strength" or "weakness"
    description: str
    evidence: list[dict]  # quotes supporting this


@dataclass
class EnsembleResult:
    """Aggregated result from all models."""
    candidate_name: str
    total_turns_analyzed: int

    # Individual model results
    model_results: list[ModelResult]

    # Aggregated scores (average of successful models)
    average_ocean: PersonalityVector
    average_confidence: dict[str, float]

    # Standard deviation for each trait
    std_dev: dict[str, float]

    # Number of models that succeeded
    models_succeeded: int

    # Combined evidence from all models
    all_evidence: list[dict] = field(default_factory=list)

    # Strengths and weaknesses with evidence
    strengths: list[StrengthWeakness] = field(default_factory=list)
    weaknesses: list[StrengthWeakness] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "candidate_name": self.candidate_name,
            "total_turns_analyzed": self.total_turns_analyzed,
            "models_succeeded": self.models_succeeded,
            "average_ocean": self.average_ocean.model_dump(),
            "average_confidence": self.average_confidence,
            "std_dev": self.std_dev,
            "model_results": [
                {
                    "model": mr.model_name,
                    "ocean_scores": mr.ocean_scores.model_dump() if mr.success else None,
                    "ocean_confidence": mr.ocean_confidence if mr.success else None,
                    "evidence_count": mr.evidence_count if mr.success else 0,
                    "evidence": [
                        {
                            "trait": e.trait,
                            "facet": e.facet,
                            "quote": e.quote,
                            "turn_number": e.turn_number,
                            "signal_strength": e.signal_strength,
                            "reasoning": e.reasoning,
                        }
                        for e in mr.evidence
                    ] if mr.success else [],
                    "success": mr.success,
                    "error": mr.error,
                }
                for mr in self.model_results
            ],
            "all_evidence": self.all_evidence,
            "strengths": [
                {
                    "trait": s.trait,
                    "type": s.type,
                    "description": s.description,
                    "evidence": s.evidence,
                }
                for s in self.strengths
            ],
            "weaknesses": [
                {
                    "trait": w.trait,
                    "type": w.type,
                    "description": w.description,
                    "evidence": w.evidence,
                }
                for w in self.weaknesses
            ],
        }


class EnsembleDetector:
    """
    Runs personality detection using multiple LLM models and aggregates results.

    This provides:
    - Individual OCEAN scores from each model
    - Average OCEAN scores across all models
    - Standard deviation to measure model agreement
    - Confidence scores per trait
    """

    def __init__(
        self,
        base_client: "LLMClient",
        models: Optional[list[str]] = None,
    ):
        """
        Initialize ensemble detector.

        Args:
            base_client: Base LLM client (used for API key and settings).
            models: List of model names to use. Defaults to ENSEMBLE_MODELS.
        """
        self.base_client = base_client
        self.models = models or ENSEMBLE_MODELS

    async def detect_ensemble(
        self,
        turns: list[Turn],
        candidate_name: str,
    ) -> EnsembleResult:
        """
        Run personality detection with all models in parallel.

        Args:
            turns: Conversation turns to analyze.
            candidate_name: Name of candidate.

        Returns:
            EnsembleResult with individual and aggregated scores.
        """
        from clients.llm_client import LLMClient

        # Create tasks for all models
        tasks = []
        for model in self.models:
            tasks.append(self._detect_with_model(turns, candidate_name, model))

        # Run all in parallel
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results
        model_results: list[ModelResult] = []
        successful_results: list[ModelResult] = []

        for i, result in enumerate(results):
            model_name = self.models[i]

            if isinstance(result, Exception):
                model_results.append(ModelResult(
                    model_name=model_name,
                    ocean_scores=PersonalityVector(),
                    ocean_confidence={},
                    evidence_count=0,
                    success=False,
                    error=str(result),
                ))
            else:
                model_results.append(result)
                if result.success:
                    successful_results.append(result)

        # Calculate averages
        avg_ocean, avg_conf, std_dev = self._calculate_averages(successful_results)

        # Aggregate all evidence from all models
        all_evidence = self._aggregate_evidence(successful_results)

        # Compute strengths and weaknesses
        strengths, weaknesses = self._compute_strengths_weaknesses(avg_ocean, all_evidence)

        # Get turn count
        candidate_turns = sum(1 for t in turns if t.speaker.value == "candidate")

        return EnsembleResult(
            candidate_name=candidate_name,
            total_turns_analyzed=candidate_turns,
            model_results=model_results,
            average_ocean=avg_ocean,
            average_confidence=avg_conf,
            std_dev=std_dev,
            models_succeeded=len(successful_results),
            all_evidence=all_evidence,
            strengths=strengths,
            weaknesses=weaknesses,
        )

    async def _detect_with_model(
        self,
        turns: list[Turn],
        candidate_name: str,
        model_name: str,
    ) -> ModelResult:
        """Run detection with a specific model."""
        from clients.llm_client import LLMClient

        try:
            # Create client with specific model
            client = LLMClient(
                api_key=self.base_client.api_key,
                pro_model=model_name,
                flash_model=model_name,
            )

            # Run facet detection
            detector = FacetDetector(client, use_flash_model=True)
            assessment = await detector.detect_facets(turns, candidate_name)

            # Extract evidence from facet scores
            evidence_list = []
            for facet_id, facet_score in assessment.facet_scores.items():
                for ev in facet_score.evidence:
                    evidence_list.append(EvidenceItem(
                        trait=ev.trait,
                        facet=ev.facet_name,
                        quote=ev.quote,
                        turn_number=ev.turn_number,
                        signal_strength=ev.signal_strength,
                        reasoning=ev.reasoning,
                    ))

            return ModelResult(
                model_name=model_name,
                ocean_scores=assessment.ocean_scores,
                ocean_confidence=assessment.ocean_confidence,
                evidence_count=assessment.total_evidence_count,
                evidence=evidence_list,
                success=True,
            )

        except Exception as e:
            return ModelResult(
                model_name=model_name,
                ocean_scores=PersonalityVector(),
                ocean_confidence={},
                evidence_count=0,
                evidence=[],
                success=False,
                error=str(e),
            )

    def _calculate_averages(
        self,
        results: list[ModelResult],
    ) -> tuple[PersonalityVector, dict[str, float], dict[str, float]]:
        """Calculate average OCEAN scores and standard deviation."""
        if not results:
            return (
                PersonalityVector(),
                {t: 0.0 for t in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]},
                {t: 0.0 for t in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]},
            )

        traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]

        # Collect scores per trait
        trait_scores: dict[str, list[float]] = {t: [] for t in traits}
        trait_confs: dict[str, list[float]] = {t: [] for t in traits}

        for result in results:
            for trait in traits:
                trait_scores[trait].append(getattr(result.ocean_scores, trait))
                trait_confs[trait].append(result.ocean_confidence.get(trait, 0.5))

        # Calculate averages
        avg_scores = {}
        avg_confs = {}
        std_devs = {}

        for trait in traits:
            scores = trait_scores[trait]
            confs = trait_confs[trait]

            avg_scores[trait] = round(sum(scores) / len(scores), 3)
            avg_confs[trait] = round(sum(confs) / len(confs), 3)

            # Standard deviation
            if len(scores) > 1:
                mean = sum(scores) / len(scores)
                variance = sum((s - mean) ** 2 for s in scores) / len(scores)
                std_devs[trait] = round(variance ** 0.5, 3)
            else:
                std_devs[trait] = 0.0

        avg_ocean = PersonalityVector(
            openness=avg_scores["openness"],
            conscientiousness=avg_scores["conscientiousness"],
            extraversion=avg_scores["extraversion"],
            agreeableness=avg_scores["agreeableness"],
            neuroticism=avg_scores["neuroticism"],
        )

        return avg_ocean, avg_confs, std_devs

    def _aggregate_evidence(self, results: list[ModelResult]) -> list[dict]:
        """Aggregate and deduplicate evidence from all models."""
        all_evidence = []
        seen_quotes = set()

        for result in results:
            for ev in result.evidence:
                # Deduplicate by quote (same quote from multiple models)
                quote_key = ev.quote.lower().strip()[:50]
                if quote_key not in seen_quotes:
                    seen_quotes.add(quote_key)
                    all_evidence.append({
                        "trait": ev.trait,
                        "facet": ev.facet,
                        "quote": ev.quote,
                        "turn_number": ev.turn_number,
                        "signal_strength": ev.signal_strength,
                        "reasoning": ev.reasoning,
                        "model": result.model_name,
                    })

        # Sort by signal strength
        all_evidence.sort(key=lambda x: x["signal_strength"], reverse=True)
        return all_evidence

    def _compute_strengths_weaknesses(
        self,
        ocean: PersonalityVector,
        evidence: list[dict],
    ) -> tuple[list[StrengthWeakness], list[StrengthWeakness]]:
        """
        Compute candidate strengths and weaknesses based on OCEAN scores.

        Strengths: traits significantly above 0.5 with positive workplace implications
        Weaknesses: traits significantly below 0.5 or high neuroticism
        """
        strengths = []
        weaknesses = []

        # Trait descriptions for workplace context
        trait_descriptions = {
            "openness": {
                "high": "Creative and open to new ideas - brings innovative thinking to problem-solving",
                "low": "Prefers proven approaches - may resist novel solutions or unconventional ideas",
            },
            "conscientiousness": {
                "high": "Organized and detail-oriented - reliable in following through on commitments",
                "low": "Flexible but may lack structure - could benefit from more systematic approaches",
            },
            "extraversion": {
                "high": "Confident communicator - takes initiative in discussions and engages others",
                "low": "Reserved in discussions - may need encouragement to share ideas proactively",
            },
            "agreeableness": {
                "high": "Collaborative and team-oriented - builds rapport and seeks consensus",
                "low": "Direct and challenging - may come across as competitive or confrontational",
            },
            "neuroticism": {
                "high": "Sensitive to pressure - may show stress or anxiety under challenging conditions",
                "low": "Calm under pressure - maintains composure in stressful situations",
            },
        }

        # Thresholds
        HIGH_THRESHOLD = 0.6
        LOW_THRESHOLD = 0.4

        for trait in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]:
            score = getattr(ocean, trait)
            trait_evidence = [e for e in evidence if e["trait"] == trait]

            # Special handling for neuroticism (high = weakness, low = strength)
            if trait == "neuroticism":
                if score >= HIGH_THRESHOLD:
                    weaknesses.append(StrengthWeakness(
                        trait=trait,
                        type="weakness",
                        description=trait_descriptions[trait]["high"],
                        evidence=trait_evidence[:3],
                    ))
                elif score <= LOW_THRESHOLD:
                    strengths.append(StrengthWeakness(
                        trait=trait,
                        type="strength",
                        description=trait_descriptions[trait]["low"],
                        evidence=trait_evidence[:3],
                    ))
            else:
                # For other traits, high = strength, low = weakness
                if score >= HIGH_THRESHOLD:
                    strengths.append(StrengthWeakness(
                        trait=trait,
                        type="strength",
                        description=trait_descriptions[trait]["high"],
                        evidence=trait_evidence[:3],
                    ))
                elif score <= LOW_THRESHOLD:
                    weaknesses.append(StrengthWeakness(
                        trait=trait,
                        type="weakness",
                        description=trait_descriptions[trait]["low"],
                        evidence=trait_evidence[:3],
                    ))

        return strengths, weaknesses


async def detect_personality_ensemble(
    turns: list[Turn],
    candidate_name: str,
    client: "LLMClient",
    models: Optional[list[str]] = None,
) -> EnsembleResult:
    """
    Convenience function to run ensemble personality detection.

    Args:
        turns: Conversation turns.
        candidate_name: Name of candidate.
        client: Base LLM client.
        models: Optional list of models to use.

    Returns:
        EnsembleResult with all model outputs and averages.
    """
    detector = EnsembleDetector(client, models)
    return await detector.detect_ensemble(turns, candidate_name)
