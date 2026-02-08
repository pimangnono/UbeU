"""
Turn Analyzer for Evidence-Based Assessment.

Analyzes individual candidate turns for:
- Intent classification with supporting quotes
- Personality trait signals with evidence
- Reasoning quality assessment with evidence
- Competency signals for later aggregation

Uses LLM to extract structured, quote-backed analysis.
"""

import json
import re
from typing import TYPE_CHECKING, Optional

from utils.models import (
    Turn,
    SpeakerRole,
    IntentCategory,
    BigFiveTrait,
)
from utils.analysis_models import (
    TurnAnalysis,
    IntentAnalysis,
    TraitSignal,
    TraitDirection,
    ReasoningAssessment,
    LogicalConnectionQuality,
    AnalysisSession,
    ScoringEvidence,
    ContributionType,
    CompetencyDimension,
)

if TYPE_CHECKING:
    from clients.llm_client import LLMClient, ModelTier


# =============================================================================
# Analysis Prompts
# =============================================================================

TURN_ANALYSIS_SYSTEM_PROMPT = """You are an expert behavioral analyst evaluating a candidate's response in a consulting case discussion.

Your task is to analyze the candidate's response for:
1. INTENT - What is the candidate trying to communicate/achieve?
2. PERSONALITY SIGNALS - What Big Five personality traits are evidenced?
3. REASONING QUALITY - How well does the candidate reason and use data?
4. COMPETENCY SIGNALS - What workplace competencies are demonstrated?

CRITICAL: All assessments MUST include EXACT QUOTES from the response as evidence.
Do not paraphrase - use the candidate's actual words in quotation marks.

## Intent Categories
- assertive: Taking a clear position, expressing confidence, directing discussion
- cooperative: Building on others' ideas, seeking common ground, acknowledging points
- avoidant: Deflecting, being vague, not taking a stance
- aggressive: Attacking others, dismissing ideas harshly, hostile tone
- anxious: Expressing worry, uncertainty, hedging excessively
- analytical: Focusing on data, logic, structured analysis
- creative: Proposing novel ideas, thinking outside the box
- empathetic: Acknowledging emotions, validating others' concerns
- defensive: Justifying actions, explaining away criticism
- neutral: Matter-of-fact statements without strong signals

## Big Five Traits
For each trait, identify if the response shows HIGH or LOW signals:
- Openness: HIGH = curious, creative, novel ideas; LOW = conventional, practical, routine
- Conscientiousness: HIGH = organized, structured, detail-oriented; LOW = scattered, informal, flexible
- Extraversion: HIGH = verbose, engaging, energetic; LOW = brief, reserved, minimal
- Agreeableness: HIGH = cooperative, warm, harmonious; LOW = challenging, direct, competitive
- Neuroticism: HIGH = anxious, stressed, worried; LOW = calm, composed, stable

## Reasoning Quality
Assess logical connection quality:
- none: No reasoning shown
- weak: Flawed logic or unsupported claims
- moderate: Sound reasoning with some gaps
- strong: Clear, well-supported logical connections

Respond ONLY with valid JSON in the specified format."""

TURN_ANALYSIS_PROMPT_TEMPLATE = """Analyze this candidate response from a consulting case discussion.

## Context
Case: {case_context}
Data Revealed So Far: {revealed_data}
Previous Speaker ({previous_speaker}): "{previous_content}"

## Candidate Response
Speaker: {candidate_name}
Response: "{candidate_response}"

## Analysis Required
Provide a detailed, evidence-based analysis. EVERY assessment must include an exact quote.

Respond with JSON in this exact format:
{{
    "intent_analysis": {{
        "primary_intent": "<intent_category>",
        "primary_confidence": <0.0-1.0>,
        "primary_evidence": "<exact quote from response>",
        "primary_reasoning": "<why this quote shows this intent>",
        "secondary_intent": "<intent_category or null>",
        "secondary_confidence": <0.0-1.0 or null>,
        "secondary_evidence": "<quote or null>"
    }},
    "trait_signals": [
        {{
            "trait": "<openness|conscientiousness|extraversion|agreeableness|neuroticism>",
            "direction": "<high|low>",
            "signal_strength": <0.0-1.0>,
            "evidence_quote": "<exact quote>",
            "reasoning": "<why this quote shows this trait direction>"
        }}
    ],
    "reasoning_assessment": {{
        "makes_assumption": <true|false>,
        "assumption_text": "<the assumption or null>",
        "assumption_valid": <true|false|null>,
        "assumption_evidence": "<quote showing assumption or null>",
        "uses_data": <true|false>,
        "data_categories_referenced": ["<category1>", "<category2>"],
        "data_categories_used_effectively": ["<category1>"],
        "logical_connection_quality": "<none|weak|moderate|strong>",
        "logic_evidence_quote": "<quote showing reasoning quality>",
        "logic_explanation": "<why this rating>",
        "uses_framework": <true|false>,
        "framework_name": "<framework name or null>"
    }},
    "competency_signals": {{
        "collaboration": ["<quote showing collaboration or empty>"],
        "leadership": ["<quote showing leadership or empty>"],
        "problem_solving": ["<quote showing problem-solving or empty>"],
        "communication": ["<quote showing clear communication or empty>"],
        "stress_management": ["<quote showing composure or empty>"]
    }},
    "emotional_tone": "<e.g., confident, frustrated, curious, defensive, calm>",
    "data_requested": ["<data category requested in this turn>"]
}}"""


# =============================================================================
# Turn Analyzer Class
# =============================================================================

class TurnAnalyzer:
    """
    Analyzes individual turns for evidence-based assessment.

    Uses LLM to extract structured analysis with quote-backed evidence
    for intent, personality traits, and reasoning quality.
    """

    def __init__(
        self,
        client: "LLMClient",
        case_context: str = "",
        candidate_name: str = "Candidate",
    ):
        """
        Initialize the turn analyzer.

        Args:
            client: LLM client for analysis.
            case_context: Brief description of the case study.
            candidate_name: Name of the candidate being analyzed.
        """
        self.client = client
        self.case_context = case_context
        self.candidate_name = candidate_name
        self._analysis_session: Optional[AnalysisSession] = None

    def start_session(self, session_id: str) -> AnalysisSession:
        """Start a new analysis session."""
        self._analysis_session = AnalysisSession(
            session_id=session_id,
            candidate_name=self.candidate_name,
        )
        return self._analysis_session

    def get_session(self) -> Optional[AnalysisSession]:
        """Get the current analysis session."""
        return self._analysis_session

    async def analyze_turn(
        self,
        turn: Turn,
        previous_turn: Optional[Turn] = None,
        revealed_data: Optional[list[str]] = None,
        conversation_history: Optional[list[Turn]] = None,
    ) -> TurnAnalysis:
        """
        Analyze a single candidate turn.

        Args:
            turn: The turn to analyze.
            previous_turn: The turn this is responding to.
            revealed_data: Data categories revealed so far.
            conversation_history: Full conversation for context.

        Returns:
            TurnAnalysis with evidence-based assessments.
        """
        from clients.llm_client import ModelTier

        # Build prompt
        prompt = TURN_ANALYSIS_PROMPT_TEMPLATE.format(
            case_context=self.case_context or "Business case study discussion",
            revealed_data=", ".join(revealed_data) if revealed_data else "None",
            previous_speaker=previous_turn.speaker_name if previous_turn else "Facilitator",
            previous_content=previous_turn.content[:200] if previous_turn else "Opening question",
            candidate_name=turn.speaker_name,
            candidate_response=turn.content,
        )

        # Call LLM for analysis
        response = await self.client.generate(
            prompt=prompt,
            tier=ModelTier.FLASH,  # Use faster model for analysis
            system_instruction=TURN_ANALYSIS_SYSTEM_PROMPT,
            temperature=0.2,  # Low temperature for consistent analysis
            max_tokens=2048,
        )

        # Parse response
        analysis = self._parse_analysis_response(response, turn)

        # Add to session if active
        if self._analysis_session:
            self._analysis_session.add_turn_analysis(analysis)

        return analysis

    def _parse_analysis_response(self, response: str, turn: Turn) -> TurnAnalysis:
        """Parse LLM response into TurnAnalysis."""
        try:
            # Clean response
            text = response.strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[1] if "\n" in text else text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()
            if text.startswith("json"):
                text = text[4:].strip()

            data = json.loads(text)
            return self._build_turn_analysis(data, turn)

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            # Return minimal analysis on parse failure
            return self._build_fallback_analysis(turn, str(e))

    def _build_turn_analysis(self, data: dict, turn: Turn) -> TurnAnalysis:
        """Build TurnAnalysis from parsed JSON data."""
        # Parse intent analysis
        intent_data = data.get("intent_analysis", {})
        intent_analysis = IntentAnalysis(
            primary_intent=self._parse_intent(intent_data.get("primary_intent", "neutral")),
            primary_confidence=float(intent_data.get("primary_confidence", 0.5)),
            primary_evidence=intent_data.get("primary_evidence", turn.content[:100]),
            primary_reasoning=intent_data.get("primary_reasoning", ""),
            secondary_intent=self._parse_intent(intent_data.get("secondary_intent")) if intent_data.get("secondary_intent") else None,
            secondary_confidence=float(intent_data.get("secondary_confidence")) if intent_data.get("secondary_confidence") else None,
            secondary_evidence=intent_data.get("secondary_evidence"),
        )

        # Parse trait signals
        trait_signals = []
        for signal_data in data.get("trait_signals", []):
            try:
                trait_signals.append(TraitSignal(
                    trait=self._parse_trait(signal_data.get("trait", "")),
                    direction=TraitDirection(signal_data.get("direction", "neutral")),
                    signal_strength=float(signal_data.get("signal_strength", 0.5)),
                    evidence_quote=signal_data.get("evidence_quote", ""),
                    reasoning=signal_data.get("reasoning", ""),
                ))
            except (ValueError, KeyError):
                continue

        # Parse reasoning assessment
        reasoning_data = data.get("reasoning_assessment", {})
        reasoning_assessment = None
        if reasoning_data:
            reasoning_assessment = ReasoningAssessment(
                makes_assumption=reasoning_data.get("makes_assumption", False),
                assumption_text=reasoning_data.get("assumption_text"),
                assumption_valid=reasoning_data.get("assumption_valid"),
                assumption_evidence=reasoning_data.get("assumption_evidence"),
                uses_data=reasoning_data.get("uses_data", False),
                data_categories_referenced=reasoning_data.get("data_categories_referenced", []),
                data_categories_used_effectively=reasoning_data.get("data_categories_used_effectively", []),
                logical_connection_quality=self._parse_logic_quality(
                    reasoning_data.get("logical_connection_quality", "none")
                ),
                logic_evidence_quote=reasoning_data.get("logic_evidence_quote"),
                logic_explanation=reasoning_data.get("logic_explanation"),
                uses_framework=reasoning_data.get("uses_framework", False),
                framework_name=reasoning_data.get("framework_name"),
            )

        # Parse competency signals
        competency_signals = {}
        for dim in CompetencyDimension:
            quotes = data.get("competency_signals", {}).get(dim.value, [])
            if quotes and isinstance(quotes, list):
                competency_signals[dim.value] = [q for q in quotes if q]

        # Count words and sentences
        word_count = len(turn.content.split())
        sentence_count = len(re.findall(r'[.!?]+', turn.content)) or 1

        return TurnAnalysis(
            turn_number=turn.turn_number,
            speaker=turn.speaker,
            speaker_name=turn.speaker_name,
            content=turn.content,
            word_count=word_count,
            sentence_count=sentence_count,
            intent_analysis=intent_analysis,
            trait_signals=trait_signals,
            reasoning_assessment=reasoning_assessment,
            data_requested=data.get("data_requested", []),
            tension_level=turn.tension_level or 0.3,
            emotional_tone=data.get("emotional_tone"),
            competency_signals=competency_signals,
        )

    def _build_fallback_analysis(self, turn: Turn, error: str) -> TurnAnalysis:
        """Build minimal TurnAnalysis when parsing fails."""
        from pipeline.statistics import classify_intent_rule_based

        # Use rule-based intent as fallback
        intent = classify_intent_rule_based(turn.content)

        word_count = len(turn.content.split())
        sentence_count = len(re.findall(r'[.!?]+', turn.content)) or 1

        return TurnAnalysis(
            turn_number=turn.turn_number,
            speaker=turn.speaker,
            speaker_name=turn.speaker_name,
            content=turn.content,
            word_count=word_count,
            sentence_count=sentence_count,
            intent_analysis=IntentAnalysis(
                primary_intent=intent,
                primary_confidence=0.3,
                primary_evidence=turn.content[:100],
                primary_reasoning=f"Fallback analysis due to: {error[:50]}",
            ),
            trait_signals=[],
            reasoning_assessment=None,
            tension_level=turn.tension_level or 0.3,
        )

    def _parse_intent(self, intent_str: str) -> IntentCategory:
        """Parse intent string to IntentCategory."""
        if not intent_str:
            return IntentCategory.NEUTRAL
        intent_str = intent_str.lower().strip()
        for cat in IntentCategory:
            if cat.value == intent_str:
                return cat
        return IntentCategory.NEUTRAL

    def _parse_trait(self, trait_str: str) -> BigFiveTrait:
        """Parse trait string to BigFiveTrait."""
        trait_str = trait_str.lower().strip()
        for trait in BigFiveTrait:
            if trait.value == trait_str:
                return trait
        raise ValueError(f"Unknown trait: {trait_str}")

    def _parse_logic_quality(self, quality_str: str) -> LogicalConnectionQuality:
        """Parse logic quality string."""
        quality_str = quality_str.lower().strip()
        for quality in LogicalConnectionQuality:
            if quality.value == quality_str:
                return quality
        return LogicalConnectionQuality.NONE

    async def analyze_conversation(
        self,
        turns: list[Turn],
        revealed_data_by_turn: Optional[dict[int, list[str]]] = None,
    ) -> list[TurnAnalysis]:
        """
        Analyze all candidate turns in a conversation.

        Args:
            turns: All turns in the conversation.
            revealed_data_by_turn: Mapping of turn number to revealed data at that point.

        Returns:
            List of TurnAnalysis for candidate turns only.
        """
        analyses = []
        previous_turn = None

        for i, turn in enumerate(turns):
            if turn.speaker != SpeakerRole.CANDIDATE:
                previous_turn = turn
                continue

            # Get revealed data up to this turn
            revealed = []
            if revealed_data_by_turn:
                for t_num in range(turn.turn_number + 1):
                    if t_num in revealed_data_by_turn:
                        revealed.extend(revealed_data_by_turn[t_num])
                revealed = list(set(revealed))

            analysis = await self.analyze_turn(
                turn=turn,
                previous_turn=previous_turn,
                revealed_data=revealed,
                conversation_history=turns[:i],
            )
            analyses.append(analysis)
            previous_turn = turn

        return analyses


# =============================================================================
# Aggregation Functions
# =============================================================================

def aggregate_trait_signals(
    analyses: list[TurnAnalysis],
) -> dict[str, list[TraitSignal]]:
    """
    Aggregate trait signals across all analyzed turns.

    Returns dict mapping trait name to list of signals.
    """
    aggregated = {trait.value: [] for trait in BigFiveTrait}
    for analysis in analyses:
        for signal in analysis.trait_signals:
            aggregated[signal.trait.value].append(signal)
    return aggregated


def infer_trait_score(signals: list[TraitSignal]) -> tuple[float, float]:
    """
    Infer trait score (0-1) from signals.

    Returns (score, confidence).
    """
    if not signals:
        return 0.5, 0.0  # Default to middle, zero confidence

    high_weight = 0.0
    low_weight = 0.0

    for signal in signals:
        if signal.direction == TraitDirection.HIGH:
            high_weight += signal.signal_strength
        elif signal.direction == TraitDirection.LOW:
            low_weight += signal.signal_strength

    total_weight = high_weight + low_weight
    if total_weight == 0:
        return 0.5, 0.0

    # Score: 0 = all low, 1 = all high
    score = high_weight / total_weight

    # Confidence based on quantity and strength
    avg_strength = total_weight / len(signals)
    quantity_factor = min(1.0, len(signals) / 5)
    confidence = avg_strength * quantity_factor

    return score, confidence


def extract_competency_evidence(
    analyses: list[TurnAnalysis],
    dimension: CompetencyDimension,
) -> list[ScoringEvidence]:
    """
    Extract all evidence for a competency dimension from analyses.
    """
    evidence = []
    for analysis in analyses:
        quotes = analysis.competency_signals.get(dimension.value, [])
        for quote in quotes:
            if quote:
                evidence.append(ScoringEvidence(
                    turn_number=analysis.turn_number,
                    quote=quote,
                    contribution=ContributionType.POSITIVE,
                    weight=0.1,  # Base weight, can be adjusted
                    explanation=f"Demonstrated {dimension.value.replace('_', ' ')}",
                ))
    return evidence
