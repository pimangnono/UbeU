"""
Facet-Level Personality Detection Module.

Provides fine-grained OCEAN trait assessment by detecting all 28 BFI facets
with evidence extraction from conversation transcripts.

This module complements the real-time 10-intent classification by providing
detailed, evidence-backed personality inference during post-session analysis.

Architecture:
    - Layer 1 (Real-time): 10 IntentCategories for live feedback
    - Layer 2 (Post-processing): 28 Facets for detailed assessment (this module)

Usage:
    detector = FacetDetector(client)
    assessment = await detector.detect_facets(turns, candidate_name)
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, TYPE_CHECKING

from utils.models import Turn, SpeakerRole, PersonalityVector

if TYPE_CHECKING:
    from clients.llm_client import LLMClient, ModelTier


class FacetDirection(str, Enum):
    """Whether a facet indicates HIGH or LOW trait score."""
    HIGH = "high"
    LOW = "low"


@dataclass
class FacetDefinition:
    """Definition of a single BFI facet."""
    facet_id: str
    facet_name: str
    trait: str  # openness, conscientiousness, extraversion, agreeableness, neuroticism
    direction: FacetDirection  # Whether this facet indicates HIGH or LOW trait
    description: str
    detection_cues: list[str]


@dataclass
class FacetEvidence:
    """Evidence of a facet observed in conversation."""
    facet_id: str
    facet_name: str
    trait: str
    direction: str  # "high" or "low"
    quote: str
    turn_number: int
    signal_strength: float  # 0.0 - 1.0
    reasoning: str


@dataclass
class FacetScore:
    """Aggregated score for a single facet."""
    facet_id: str
    facet_name: str
    trait: str
    direction: str
    score: float  # 0.0 - 1.0 (how strongly this facet was observed)
    evidence_count: int
    evidence: list[FacetEvidence] = field(default_factory=list)


@dataclass
class FacetAssessment:
    """Complete facet-level personality assessment."""
    candidate_name: str
    total_turns_analyzed: int
    facet_scores: dict[str, FacetScore]  # Keyed by facet_id
    ocean_scores: PersonalityVector
    ocean_confidence: dict[str, float]  # Confidence per trait
    total_evidence_count: int
    assessment_method: str = "facet_aggregation"

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "candidate_name": self.candidate_name,
            "total_turns_analyzed": self.total_turns_analyzed,
            "assessment_method": self.assessment_method,
            "total_evidence_count": self.total_evidence_count,
            "ocean_scores": self.ocean_scores.model_dump(),
            "ocean_confidence": self.ocean_confidence,
            "facet_scores": {
                fid: {
                    "facet_name": fs.facet_name,
                    "trait": fs.trait,
                    "direction": fs.direction,
                    "score": fs.score,
                    "evidence_count": fs.evidence_count,
                    "evidence": [
                        {
                            "quote": e.quote,
                            "turn_number": e.turn_number,
                            "signal_strength": e.signal_strength,
                            "reasoning": e.reasoning,
                        }
                        for e in fs.evidence
                    ],
                }
                for fid, fs in self.facet_scores.items()
            },
        }


# =============================================================================
# FACET DEFINITIONS (28 facets from BFI-44 behavioral mappings)
# =============================================================================

FACET_DEFINITIONS: list[FacetDefinition] = [
    # OPENNESS (6 facets)
    FacetDefinition(
        facet_id="O_ideas",
        facet_name="Ideas",
        trait="openness",
        direction=FacetDirection.HIGH,
        description="Intellectually curious, enjoys abstract discussions, explores hypotheticals",
        detection_cues=["what if", "theoretical", "concept", "interesting idea", "explore", "hypothetically"],
    ),
    FacetDefinition(
        facet_id="O_fantasy",
        facet_name="Fantasy",
        trait="openness",
        direction=FacetDirection.HIGH,
        description="Imaginative, uses metaphors and analogies, paints vivid scenarios",
        detection_cues=["imagine", "picture this", "it's like", "metaphor", "analogy", "envision"],
    ),
    FacetDefinition(
        facet_id="O_aesthetics",
        facet_name="Aesthetics",
        trait="openness",
        direction=FacetDirection.HIGH,
        description="Appreciates elegance in solutions, values simplicity and beauty",
        detection_cues=["elegant", "beautiful", "simplicity", "clean solution", "aesthetic", "graceful"],
    ),
    FacetDefinition(
        facet_id="O_conventionality",
        facet_name="Conventionality",
        trait="openness",
        direction=FacetDirection.LOW,
        description="Strongly prefers established methods, resists novel or untested ideas",
        detection_cues=["always done it this way", "proven method", "stick to what works", "traditional", "established"],
    ),
    FacetDefinition(
        facet_id="O_practicality",
        facet_name="Practicality",
        trait="openness",
        direction=FacetDirection.LOW,
        description="Focuses exclusively on concrete matters, dismisses abstract thinking",
        detection_cues=["practical application", "concrete", "realistic", "actually implement", "not theoretical"],
    ),
    FacetDefinition(
        facet_id="O_narrow_focus",
        facet_name="Narrow Focus",
        trait="openness",
        direction=FacetDirection.LOW,
        description="Shows no curiosity about alternatives, avoids exploratory questions",
        detection_cues=["don't see why", "no need to change", "not relevant", "let's move on", "waste of time"],
    ),

    # CONSCIENTIOUSNESS (6 facets)
    FacetDefinition(
        facet_id="C_order",
        facet_name="Order",
        trait="conscientiousness",
        direction=FacetDirection.HIGH,
        description="Organized, systematic approach, creates structure and plans",
        detection_cues=["structured plan", "first second third", "checklist", "timeline", "organize", "systematic"],
    ),
    FacetDefinition(
        facet_id="C_dutifulness",
        facet_name="Dutifulness",
        trait="conscientiousness",
        direction=FacetDirection.HIGH,
        description="Follows through on commitments, takes responsibilities seriously",
        detection_cues=["committed", "promised", "responsibility", "follow through", "deadline", "deliver"],
    ),
    FacetDefinition(
        facet_id="C_achievement",
        facet_name="Achievement-Striving",
        trait="conscientiousness",
        direction=FacetDirection.HIGH,
        description="Goal-oriented, ambitious, wants to exceed expectations",
        detection_cues=["target", "goal", "measure success", "exceed expectations", "achieve", "ambitious"],
    ),
    FacetDefinition(
        facet_id="C_flexibility",
        facet_name="Flexibility",
        trait="conscientiousness",
        direction=FacetDirection.LOW,
        description="Adaptable, spontaneous, resists rigid structure",
        detection_cues=["see where this goes", "figure it out", "flexible", "adaptable", "play it by ear"],
    ),
    FacetDefinition(
        facet_id="C_casualness",
        facet_name="Casualness",
        trait="conscientiousness",
        direction=FacetDirection.LOW,
        description="Relaxed about deadlines and details, doesn't worry about precision",
        detection_cues=["close enough", "don't worry about details", "roughly", "approximate", "good enough"],
    ),
    FacetDefinition(
        facet_id="C_disorganization",
        facet_name="Disorganization",
        trait="conscientiousness",
        direction=FacetDirection.LOW,
        description="Jumps between topics, loses track, doesn't follow structure",
        detection_cues=["off topic", "wait what were we", "sorry where were we", "reminds me of", "tangent"],
    ),

    # EXTRAVERSION (6 facets)
    FacetDefinition(
        facet_id="E_assertiveness",
        facet_name="Assertiveness",
        trait="extraversion",
        direction=FacetDirection.HIGH,
        description="Takes charge, speaks up, directs the conversation",
        detection_cues=["here's what we should do", "let me take the lead", "I think we need to", "my view is"],
    ),
    FacetDefinition(
        facet_id="E_gregariousness",
        facet_name="Gregariousness",
        trait="extraversion",
        direction=FacetDirection.HIGH,
        description="Enjoys group interaction, engages others, builds rapport",
        detection_cues=["love working with", "great point", "let's all", "team", "together", "everyone"],
    ),
    FacetDefinition(
        facet_id="E_positive_emotions",
        facet_name="Positive Emotions",
        trait="extraversion",
        direction=FacetDirection.HIGH,
        description="Enthusiastic, optimistic, expresses excitement",
        detection_cues=["exciting", "great", "looking forward", "fantastic", "amazing", "love this"],
    ),
    FacetDefinition(
        facet_id="E_reserve",
        facet_name="Reserve",
        trait="extraversion",
        direction=FacetDirection.LOW,
        description="Quiet, speaks only when necessary, gives minimal responses",
        detection_cues=["I see", "okay", "noted", "let me think", "hmm"],
    ),
    FacetDefinition(
        facet_id="E_independence",
        facet_name="Independence",
        trait="extraversion",
        direction=FacetDirection.LOW,
        description="Prefers working alone, doesn't seek group engagement",
        detection_cues=["handle this independently", "work alone", "on my own", "take this offline", "solo"],
    ),
    FacetDefinition(
        facet_id="E_brevity",
        facet_name="Brevity",
        trait="extraversion",
        direction=FacetDirection.LOW,
        description="Keeps responses short, doesn't elaborate or fill silences",
        detection_cues=["agreed", "yes", "no", "that works", "fine"],
    ),

    # AGREEABLENESS (5 facets)
    FacetDefinition(
        facet_id="A_trust",
        facet_name="Trust",
        trait="agreeableness",
        direction=FacetDirection.HIGH,
        description="Assumes good intentions, gives benefit of the doubt",
        detection_cues=["trust", "benefit of the doubt", "meant well", "good intentions", "believe"],
    ),
    FacetDefinition(
        facet_id="A_altruism",
        facet_name="Altruism",
        trait="agreeableness",
        direction=FacetDirection.HIGH,
        description="Helpful, puts others first, offers assistance",
        detection_cues=["how can I help", "let me help", "happy to", "support you", "what do you need"],
    ),
    FacetDefinition(
        facet_id="A_compliance",
        facet_name="Compliance",
        trait="agreeableness",
        direction=FacetDirection.HIGH,
        description="Avoids conflict, yields to others, seeks consensus",
        detection_cues=["go along with", "whatever works", "don't want to cause problems", "consensus", "agree"],
    ),
    FacetDefinition(
        facet_id="A_skepticism",
        facet_name="Skepticism",
        trait="agreeableness",
        direction=FacetDirection.LOW,
        description="Questions motives and claims, demands proof",
        detection_cues=["real agenda", "prove it", "skeptical", "don't believe", "show me evidence"],
    ),
    FacetDefinition(
        facet_id="A_competitiveness",
        facet_name="Competitiveness",
        trait="agreeableness",
        direction=FacetDirection.LOW,
        description="Focuses on winning and self-interest, doesn't back down",
        detection_cues=["what's in it for me", "not backing down", "my approach is better", "I win", "compete"],
    ),

    # NEUROTICISM (5 facets)
    FacetDefinition(
        facet_id="N_anxiety",
        facet_name="Anxiety",
        trait="neuroticism",
        direction=FacetDirection.HIGH,
        description="Worries about potential problems, expresses uncertainty",
        detection_cues=["worried", "what if something goes wrong", "concerned", "risky", "anxious", "nervous"],
    ),
    FacetDefinition(
        facet_id="N_anger",
        facet_name="Anger",
        trait="neuroticism",
        direction=FacetDirection.HIGH,
        description="Quick to frustration, expresses irritation",
        detection_cues=["frustrating", "annoying", "can't believe", "ridiculous", "irritated", "angry"],
    ),
    FacetDefinition(
        facet_id="N_self_consciousness",
        facet_name="Self-Consciousness",
        trait="neuroticism",
        direction=FacetDirection.HIGH,
        description="Sensitive to criticism, defensive, worries about perception",
        detection_cues=["am I being blamed", "hope I didn't mess up", "did I do something wrong", "defensive"],
    ),
    FacetDefinition(
        facet_id="N_calm",
        facet_name="Calm",
        trait="neuroticism",
        direction=FacetDirection.LOW,
        description="Stays composed under pressure, not easily upset",
        detection_cues=["stay calm", "not worried", "we'll figure it out", "no problem", "under control"],
    ),
    FacetDefinition(
        facet_id="N_resilience",
        facet_name="Resilience",
        trait="neuroticism",
        direction=FacetDirection.LOW,
        description="Bounces back from setbacks, sees challenges as opportunities",
        detection_cues=["learning opportunity", "setback", "won't stop us", "handled worse", "bounce back"],
    ),
]

# Create lookup dictionaries
FACETS_BY_ID: dict[str, FacetDefinition] = {f.facet_id: f for f in FACET_DEFINITIONS}
FACETS_BY_TRAIT: dict[str, list[FacetDefinition]] = {}
for f in FACET_DEFINITIONS:
    if f.trait not in FACETS_BY_TRAIT:
        FACETS_BY_TRAIT[f.trait] = []
    FACETS_BY_TRAIT[f.trait].append(f)


# =============================================================================
# FACET DETECTION PROMPT
# =============================================================================

FACET_DETECTION_PROMPT = """You are an expert psychologist analyzing a conversation to detect Big Five personality facets.

## Candidate to Analyze
Name: {candidate_name}

## Conversation Transcript
{conversation}

## Facet Definitions
Analyze the candidate's responses for evidence of these 28 personality facets:

### OPENNESS
- Ideas (HIGH): Intellectually curious, enjoys abstract discussions, explores hypotheticals
- Fantasy (HIGH): Imaginative, uses metaphors and analogies
- Aesthetics (HIGH): Appreciates elegance in solutions
- Conventionality (LOW): Prefers established methods, resists new ideas
- Practicality (LOW): Focuses on concrete matters, dismisses abstract thinking
- Narrow Focus (LOW): No curiosity about alternatives

### CONSCIENTIOUSNESS
- Order (HIGH): Organized, systematic, creates structure and plans
- Dutifulness (HIGH): Follows through on commitments
- Achievement-Striving (HIGH): Goal-oriented, ambitious
- Flexibility (LOW): Spontaneous, resists rigid structure
- Casualness (LOW): Relaxed about deadlines and details
- Disorganization (LOW): Jumps between topics, loses track

### EXTRAVERSION
- Assertiveness (HIGH): Takes charge, speaks up, directs conversation
- Gregariousness (HIGH): Enjoys group interaction, engages others
- Positive Emotions (HIGH): Enthusiastic, optimistic
- Reserve (LOW): Quiet, speaks only when necessary
- Independence (LOW): Prefers working alone
- Brevity (LOW): Keeps responses short, doesn't elaborate

### AGREEABLENESS
- Trust (HIGH): Assumes good intentions
- Altruism (HIGH): Helpful, puts others first
- Compliance (HIGH): Avoids conflict, yields to others
- Skepticism (LOW): Questions motives, demands proof
- Competitiveness (LOW): Focuses on winning, self-interest

### NEUROTICISM
- Anxiety (HIGH): Worries about problems, expresses uncertainty
- Anger (HIGH): Quick to frustration
- Self-Consciousness (HIGH): Sensitive to criticism, defensive
- Calm (LOW): Composed under pressure
- Resilience (LOW): Bounces back from setbacks

## Task
For each facet where you find evidence in the candidate's responses:
1. Extract a direct quote (exact words from the candidate)
2. Identify the turn number
3. Rate signal strength (0.0-1.0): How strongly does this quote indicate the facet?
4. Provide brief reasoning

## Response Format
Return ONLY valid JSON in this exact format:
{{
    "evidence": [
        {{
            "facet_id": "O_ideas",
            "quote": "exact quote from candidate",
            "turn_number": 1,
            "signal_strength": 0.8,
            "reasoning": "Shows intellectual curiosity by exploring hypothetical scenarios"
        }}
    ]
}}

Rules:
- Only include facets with clear evidence (don't force-fit)
- Quotes must be exact text from the candidate (not paraphrased)
- Signal strength: 0.3-0.5 = mild signal, 0.6-0.8 = moderate, 0.9-1.0 = strong
- Focus only on {candidate_name}'s responses, not other speakers
- Include multiple pieces of evidence for the same facet if present"""


class FacetDetector:
    """
    Detects all 28 BFI facets from conversation transcripts.

    Uses LLM to extract evidence quotes and map them to facets,
    then aggregates facet scores into OCEAN trait scores.
    """

    def __init__(
        self,
        client: "LLMClient",
        use_flash_model: bool = True,
    ):
        """
        Initialize the facet detector.

        Args:
            client: LLM client for API calls.
            use_flash_model: If True, use FLASH tier (cheaper). Default True.
        """
        self.client = client
        self.use_flash_model = use_flash_model

    def _format_conversation(self, turns: list[Turn], candidate_name: str) -> str:
        """Format conversation turns for the prompt."""
        lines = []
        for turn in turns:
            prefix = ">>>" if turn.speaker == SpeakerRole.CANDIDATE else "   "
            lines.append(f"{prefix} [Turn {turn.turn_number}] {turn.speaker_name}: {turn.content}")
        return "\n".join(lines)

    async def detect_facets(
        self,
        turns: list[Turn],
        candidate_name: str,
    ) -> FacetAssessment:
        """
        Detect all 28 facets from conversation and aggregate to OCEAN scores.

        Args:
            turns: List of conversation turns.
            candidate_name: Name of the candidate to analyze.

        Returns:
            FacetAssessment with facet scores and OCEAN scores.
        """
        from clients.llm_client import ModelTier

        # Format conversation
        conversation = self._format_conversation(turns, candidate_name)

        # Build prompt
        prompt = FACET_DETECTION_PROMPT.format(
            candidate_name=candidate_name,
            conversation=conversation,
        )

        # Call LLM
        tier = ModelTier.FLASH if self.use_flash_model else ModelTier.PRO
        response = await self.client.generate(
            prompt=prompt,
            tier=tier,
            temperature=0.3,  # Lower temperature for more consistent extraction
            max_tokens=4096,  # Need space for 28 facets
        )

        # Parse response
        evidence_list = self._parse_response(response)

        # Build facet scores
        facet_scores = self._aggregate_evidence(evidence_list)

        # Calculate OCEAN scores from facets
        ocean_scores, ocean_confidence = self._calculate_ocean_scores(facet_scores)

        # Count candidate turns
        candidate_turns = sum(1 for t in turns if t.speaker == SpeakerRole.CANDIDATE)

        return FacetAssessment(
            candidate_name=candidate_name,
            total_turns_analyzed=candidate_turns,
            facet_scores=facet_scores,
            ocean_scores=ocean_scores,
            ocean_confidence=ocean_confidence,
            total_evidence_count=len(evidence_list),
        )

    def _parse_response(self, response: str) -> list[FacetEvidence]:
        """Parse LLM response into FacetEvidence objects."""
        evidence_list = []

        try:
            # Extract JSON from response
            json_str = response.strip()
            if "```json" in json_str:
                json_str = json_str.split("```json")[1].split("```")[0]
            elif "```" in json_str:
                json_str = json_str.split("```")[1].split("```")[0]

            data = json.loads(json_str)

            for item in data.get("evidence", []):
                facet_id = item.get("facet_id", "")
                if facet_id not in FACETS_BY_ID:
                    continue  # Skip invalid facet IDs

                facet_def = FACETS_BY_ID[facet_id]

                evidence = FacetEvidence(
                    facet_id=facet_id,
                    facet_name=facet_def.facet_name,
                    trait=facet_def.trait,
                    direction=facet_def.direction.value,
                    quote=item.get("quote", ""),
                    turn_number=item.get("turn_number", 0),
                    signal_strength=min(1.0, max(0.0, float(item.get("signal_strength", 0.5)))),
                    reasoning=item.get("reasoning", ""),
                )
                evidence_list.append(evidence)

        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Warning: Failed to parse facet detection response: {e}")

        return evidence_list

    def _aggregate_evidence(self, evidence_list: list[FacetEvidence]) -> dict[str, FacetScore]:
        """Aggregate evidence into facet scores."""
        facet_scores: dict[str, FacetScore] = {}

        # Initialize all facets with zero scores
        for facet_def in FACET_DEFINITIONS:
            facet_scores[facet_def.facet_id] = FacetScore(
                facet_id=facet_def.facet_id,
                facet_name=facet_def.facet_name,
                trait=facet_def.trait,
                direction=facet_def.direction.value,
                score=0.0,
                evidence_count=0,
                evidence=[],
            )

        # Add evidence to facets
        for evidence in evidence_list:
            if evidence.facet_id in facet_scores:
                fs = facet_scores[evidence.facet_id]
                fs.evidence.append(evidence)
                fs.evidence_count += 1

        # Calculate scores based on evidence
        for facet_id, fs in facet_scores.items():
            if fs.evidence_count > 0:
                # Score = weighted average of signal strengths, boosted by evidence count
                total_strength = sum(e.signal_strength for e in fs.evidence)
                avg_strength = total_strength / fs.evidence_count

                # Boost score slightly for multiple pieces of evidence (diminishing returns)
                count_boost = min(0.2, (fs.evidence_count - 1) * 0.05)
                fs.score = round(min(1.0, avg_strength + count_boost), 3)

        return facet_scores

    def _calculate_ocean_scores(
        self,
        facet_scores: dict[str, FacetScore],
    ) -> tuple[PersonalityVector, dict[str, float]]:
        """
        Calculate OCEAN trait scores from facet scores.

        For each trait:
        - HIGH facets contribute positively to trait score
        - LOW facets contribute negatively (inverted)
        - Final score normalized to 0.0-1.0

        Returns:
            Tuple of (PersonalityVector, confidence_dict)
        """
        trait_scores: dict[str, float] = {}
        trait_confidence: dict[str, float] = {}

        for trait in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]:
            trait_facets = FACETS_BY_TRAIT.get(trait, [])

            high_signals: list[float] = []
            low_signals: list[float] = []
            total_evidence = 0

            for facet_def in trait_facets:
                fs = facet_scores.get(facet_def.facet_id)
                if fs and fs.score > 0:
                    total_evidence += fs.evidence_count
                    if facet_def.direction == FacetDirection.HIGH:
                        high_signals.append(fs.score)
                    else:  # LOW direction
                        low_signals.append(fs.score)

            # Calculate trait score
            # HIGH signals push toward 1.0, LOW signals push toward 0.0
            if high_signals or low_signals:
                high_contribution = sum(high_signals) / len(trait_facets) if high_signals else 0
                low_contribution = sum(low_signals) / len(trait_facets) if low_signals else 0

                # Combine: start at 0.5 (neutral), push up with HIGH, push down with LOW
                trait_score = 0.5 + (high_contribution * 0.5) - (low_contribution * 0.5)
                trait_score = max(0.0, min(1.0, trait_score))
            else:
                # No evidence: default to neutral
                trait_score = 0.5

            trait_scores[trait] = round(trait_score, 3)

            # Confidence based on evidence count and coverage
            facets_with_evidence = sum(1 for f in trait_facets if facet_scores.get(f.facet_id, FacetScore("", "", "", "", 0, 0)).score > 0)
            coverage = facets_with_evidence / len(trait_facets) if trait_facets else 0
            evidence_factor = min(1.0, total_evidence / 5)  # Cap at 5 pieces of evidence
            trait_confidence[trait] = round(coverage * 0.5 + evidence_factor * 0.5, 3)

        ocean_vector = PersonalityVector(
            openness=trait_scores["openness"],
            conscientiousness=trait_scores["conscientiousness"],
            extraversion=trait_scores["extraversion"],
            agreeableness=trait_scores["agreeableness"],
            neuroticism=trait_scores["neuroticism"],
        )

        return ocean_vector, trait_confidence


async def detect_facets_from_session(
    turns: list[Turn],
    candidate_name: str,
    client: "LLMClient",
) -> FacetAssessment:
    """
    Convenience function to detect facets from a session.

    Args:
        turns: Conversation turns.
        candidate_name: Name of candidate.
        client: LLM client.

    Returns:
        FacetAssessment with full analysis.
    """
    detector = FacetDetector(client)
    return await detector.detect_facets(turns, candidate_name)
