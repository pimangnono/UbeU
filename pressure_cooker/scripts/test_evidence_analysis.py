#!/usr/bin/env python3
"""
Test script for the new evidence-based analysis pipeline.

This script tests:
1. TurnAnalysis model creation
2. TurnAnalyzer with mock LLM
3. AssessmentBuilder aggregation
4. Full pipeline integration

Run from project root:
    python pressure_cooker/scripts/test_evidence_analysis.py
"""

import asyncio
import json
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.models import Turn, SpeakerRole, IntentCategory
from utils.analysis_models import (
    TurnAnalysis,
    IntentAnalysis,
    TraitSignal,
    TraitDirection,
    ReasoningAssessment,
    LogicalConnectionQuality,
    CompetencyDimension,
    BigFiveTrait,
)
from pipeline.turn_analyzer import TurnAnalyzer, aggregate_trait_signals, infer_trait_score
from pipeline.assessment_builder import AssessmentBuilder, build_evidence_based_assessment


def create_sample_turns() -> list[Turn]:
    """Create sample conversation turns for testing."""
    return [
        Turn(
            turn_number=0,
            speaker=SpeakerRole.SYSTEM,
            speaker_name="Facilitator",
            content="TechFlow is a B2B SaaS company with $12M ARR facing declining margins. What would you like to explore first?",
            tension_level=0.2,
        ),
        Turn(
            turn_number=1,
            speaker=SpeakerRole.CANDIDATE,
            speaker_name="Jin",
            content="Let me structure this analysis using a profitability framework. First, I'd like to understand the cost breakdown - can we get COGS and OPEX as a percentage of ARR?",
            tension_level=0.2,
        ),
        Turn(
            turn_number=2,
            speaker=SpeakerRole.SYSTEM,
            speaker_name="Facilitator",
            content="Here's the cost breakdown: Engineering 37%, Sales & Marketing 32%, Customer Success 18%, G&A 13%.",
            tension_level=0.3,
        ),
        Turn(
            turn_number=3,
            speaker=SpeakerRole.PROVOKER,
            speaker_name="Jordan",
            content="Those percentages don't tell us anything useful without knowing which segments are actually profitable. Stop wasting time on surface-level analysis.",
            tension_level=0.6,
        ),
        Turn(
            turn_number=4,
            speaker=SpeakerRole.CANDIDATE,
            speaker_name="Jin",
            content="I understand Jordan's concern about segment profitability. Let me refine my approach - could we see customer segments by revenue contribution and their respective LTV:CAC ratios? That would help us identify which segments are truly profitable.",
            tension_level=0.5,
        ),
        Turn(
            turn_number=5,
            speaker=SpeakerRole.MEDIATOR,
            speaker_name="Sam",
            content="Good pivot, Jin. Jordan makes a fair point about segment-level analysis. Should we also look at support costs by segment?",
            tension_level=0.4,
        ),
        Turn(
            turn_number=6,
            speaker=SpeakerRole.CANDIDATE,
            speaker_name="Jin",
            content="Yes, that's exactly right. I hypothesize that we may have a customer mix problem - some segments could be consuming disproportionate resources. Once we have the segment data, I'd propose we analyze: 1) Revenue contribution by segment, 2) Cost-to-serve by segment, and 3) Identify which segments have positive unit economics.",
            tension_level=0.4,
        ),
    ]


def create_sample_turn_analyses() -> list[TurnAnalysis]:
    """Create sample TurnAnalysis objects for testing the assessment builder."""
    analyses = []

    # Turn 1 - Structured analytical approach
    analyses.append(TurnAnalysis(
        turn_number=1,
        speaker=SpeakerRole.CANDIDATE,
        speaker_name="Jin",
        content="Let me structure this analysis using a profitability framework. First, I'd like to understand the cost breakdown - can we get COGS and OPEX as a percentage of ARR?",
        word_count=27,
        sentence_count=2,
        intent_analysis=IntentAnalysis(
            primary_intent=IntentCategory.ANALYTICAL,
            primary_confidence=0.85,
            primary_evidence="Let me structure this analysis using a profitability framework",
            primary_reasoning="Candidate explicitly mentions using a structured framework approach",
            secondary_intent=IntentCategory.ASSERTIVE,
            secondary_confidence=0.6,
            secondary_evidence="First, I'd like to understand the cost breakdown",
        ),
        trait_signals=[
            TraitSignal(
                trait=BigFiveTrait.CONSCIENTIOUSNESS,
                direction=TraitDirection.HIGH,
                signal_strength=0.8,
                evidence_quote="Let me structure this analysis using a profitability framework",
                reasoning="Organized, structured approach to problem-solving",
            ),
            TraitSignal(
                trait=BigFiveTrait.OPENNESS,
                direction=TraitDirection.HIGH,
                signal_strength=0.6,
                evidence_quote="profitability framework",
                reasoning="Uses conceptual framework, showing intellectual engagement",
            ),
        ],
        reasoning_assessment=ReasoningAssessment(
            makes_assumption=False,
            uses_data=False,
            data_categories_referenced=["costs"],
            logical_connection_quality=LogicalConnectionQuality.MODERATE,
            logic_evidence_quote="First, I'd like to understand the cost breakdown",
            logic_explanation="Logical sequencing of analysis, starting with cost structure",
            uses_framework=True,
            framework_name="profitability framework",
        ),
        data_requested=["costs"],
        tension_level=0.2,
        emotional_tone="confident",
        competency_signals={
            "leadership": ["Let me structure this analysis"],
            "problem_solving": ["using a profitability framework"],
            "communication": ["First, I'd like to understand the cost breakdown"],
        },
    ))

    # Turn 4 - Handling challenge gracefully
    analyses.append(TurnAnalysis(
        turn_number=4,
        speaker=SpeakerRole.CANDIDATE,
        speaker_name="Jin",
        content="I understand Jordan's concern about segment profitability. Let me refine my approach - could we see customer segments by revenue contribution and their respective LTV:CAC ratios?",
        word_count=30,
        sentence_count=2,
        intent_analysis=IntentAnalysis(
            primary_intent=IntentCategory.COOPERATIVE,
            primary_confidence=0.75,
            primary_evidence="I understand Jordan's concern about segment profitability",
            primary_reasoning="Acknowledges colleague's feedback constructively",
            secondary_intent=IntentCategory.ANALYTICAL,
            secondary_confidence=0.7,
            secondary_evidence="LTV:CAC ratios",
        ),
        trait_signals=[
            TraitSignal(
                trait=BigFiveTrait.AGREEABLENESS,
                direction=TraitDirection.HIGH,
                signal_strength=0.7,
                evidence_quote="I understand Jordan's concern",
                reasoning="Shows willingness to acknowledge others' points",
            ),
            TraitSignal(
                trait=BigFiveTrait.NEUROTICISM,
                direction=TraitDirection.LOW,
                signal_strength=0.65,
                evidence_quote="Let me refine my approach",
                reasoning="Calm, non-defensive response to criticism",
            ),
        ],
        reasoning_assessment=ReasoningAssessment(
            makes_assumption=False,
            uses_data=False,
            data_categories_referenced=["customer_segments", "unit_economics"],
            logical_connection_quality=LogicalConnectionQuality.STRONG,
            logic_evidence_quote="LTV:CAC ratios",
            logic_explanation="Proposes specific metric to address the gap identified by Jordan",
            uses_framework=False,
        ),
        data_requested=["customer_segments", "unit_economics"],
        tension_level=0.5,
        emotional_tone="composed",
        competency_signals={
            "collaboration": ["I understand Jordan's concern"],
            "stress_management": ["Let me refine my approach"],
            "problem_solving": ["LTV:CAC ratios"],
        },
    ))

    # Turn 6 - Synthesizing and proposing structure
    analyses.append(TurnAnalysis(
        turn_number=6,
        speaker=SpeakerRole.CANDIDATE,
        speaker_name="Jin",
        content="Yes, that's exactly right. I hypothesize that we may have a customer mix problem - some segments could be consuming disproportionate resources. Once we have the segment data, I'd propose we analyze: 1) Revenue contribution by segment, 2) Cost-to-serve by segment, and 3) Identify which segments have positive unit economics.",
        word_count=52,
        sentence_count=3,
        intent_analysis=IntentAnalysis(
            primary_intent=IntentCategory.ASSERTIVE,
            primary_confidence=0.8,
            primary_evidence="I hypothesize that we may have a customer mix problem",
            primary_reasoning="Takes a clear analytical stance with hypothesis",
        ),
        trait_signals=[
            TraitSignal(
                trait=BigFiveTrait.CONSCIENTIOUSNESS,
                direction=TraitDirection.HIGH,
                signal_strength=0.85,
                evidence_quote="1) Revenue contribution by segment, 2) Cost-to-serve by segment, and 3) Identify",
                reasoning="Highly organized numbered list structure",
            ),
            TraitSignal(
                trait=BigFiveTrait.EXTRAVERSION,
                direction=TraitDirection.HIGH,
                signal_strength=0.6,
                evidence_quote="[52-word detailed response]",
                reasoning="Lengthy, elaborative response style",
            ),
        ],
        reasoning_assessment=ReasoningAssessment(
            makes_assumption=True,
            assumption_text="Some segments could be consuming disproportionate resources",
            assumption_valid=None,  # Not yet validated
            assumption_evidence="I hypothesize that we may have a customer mix problem",
            uses_data=False,
            data_categories_referenced=["customer_segments", "costs"],
            logical_connection_quality=LogicalConnectionQuality.STRONG,
            logic_evidence_quote="Once we have the segment data, I'd propose we analyze: 1) Revenue contribution",
            logic_explanation="Clear logical sequencing with prioritized analysis plan",
            uses_framework=True,
            framework_name="segment profitability analysis",
        ),
        data_requested=["customer_segments"],
        tension_level=0.4,
        emotional_tone="confident",
        competency_signals={
            "leadership": ["I'd propose we analyze: 1) Revenue contribution"],
            "problem_solving": ["I hypothesize that we may have a customer mix problem"],
            "communication": ["1) Revenue contribution by segment, 2) Cost-to-serve by segment, and 3) Identify"],
        },
    ))

    return analyses


async def test_turn_analyzer_with_mock():
    """Test TurnAnalyzer with mock client."""
    print("\n" + "=" * 60)
    print("TEST: TurnAnalyzer with Mock Client")
    print("=" * 60)

    from clients.llm_client import MockLLMClient

    client = MockLLMClient()
    turns = create_sample_turns()

    analyzer = TurnAnalyzer(
        client=client,
        case_context="TechFlow B2B SaaS profitability case",
        candidate_name="Jin",
    )

    # Start session
    session = analyzer.start_session("test-session-001")
    print(f"✓ Created analysis session: {session.session_id}")

    # The mock client won't return proper JSON, so we'll test with sample data instead
    print("✓ TurnAnalyzer initialized successfully")
    print(f"  - Case context: {analyzer.case_context}")
    print(f"  - Candidate: {analyzer.candidate_name}")


def test_assessment_builder():
    """Test AssessmentBuilder with sample turn analyses."""
    print("\n" + "=" * 60)
    print("TEST: AssessmentBuilder")
    print("=" * 60)

    analyses = create_sample_turn_analyses()
    print(f"✓ Created {len(analyses)} sample turn analyses")

    builder = AssessmentBuilder(
        session_id="test-session-001",
        candidate_name="Jin",
    )

    assessment = builder.build_assessment(analyses)
    print(f"✓ Built evidence-based assessment")

    # Print competency scores with evidence
    print("\n--- Competency Scores ---")
    for score in assessment.competency_scores:
        print(f"\n{score.dimension.value.upper()}: {score.score:.3f}")
        print(f"  Summary: {score.summary}")
        print(f"  Evidence pieces: {len(score.evidence)}")
        for evidence in score.get_top_evidence(2):
            print(f"    [{evidence.contribution.value}] \"{evidence.quote[:50]}...\"")

    # Print personality inference
    print("\n--- Personality Inference ---")
    pi = assessment.personality_inference
    print(f"  Confidence: {pi.confidence:.2f}")
    print(f"  Openness: {pi.inferred_vector.openness:.2f}")
    print(f"  Conscientiousness: {pi.inferred_vector.conscientiousness:.2f}")
    print(f"  Extraversion: {pi.inferred_vector.extraversion:.2f}")
    print(f"  Agreeableness: {pi.inferred_vector.agreeableness:.2f}")
    print(f"  Neuroticism: {pi.inferred_vector.neuroticism:.2f}")

    # Print trait evidence
    for trait in BigFiveTrait:
        evidence = pi.get_evidence_for_trait(trait)
        if evidence:
            print(f"\n  {trait.value.upper()} evidence ({len(evidence)} signals):")
            for e in evidence[:2]:
                print(f"    [{e.trait_signal.value}] \"{e.quote[:40]}...\"")

    # Print logical assessment
    print("\n--- Logical Assessment ---")
    la = assessment.logical_assessment
    print(f"  Analytical Depth: {la.analytical_depth}/5")
    print(f"  Recommendation Quality: {la.recommendation_quality}/5")
    print(f"  Assumptions made: {len(la.assumptions)}")
    print(f"  Logical gaps: {len(la.logical_gaps)}")

    # Print summary
    print("\n--- Summary ---")
    print(f"  {assessment.overall_summary}")
    print("\n  Key Strengths:")
    for s in assessment.key_strengths:
        print(f"    • {s}")
    print("\n  Areas for Development:")
    for d in assessment.areas_for_development:
        print(f"    • {d}")

    # Test backwards compatibility
    print("\n--- Backwards Compatibility ---")
    legacy = assessment.to_legacy_assessment_mapping()
    print(f"  Legacy format: {json.dumps(legacy, indent=2)}")

    return assessment


def test_trait_inference():
    """Test trait signal aggregation and inference."""
    print("\n" + "=" * 60)
    print("TEST: Trait Signal Aggregation")
    print("=" * 60)

    analyses = create_sample_turn_analyses()

    # Aggregate signals
    aggregated = aggregate_trait_signals(analyses)

    print("\nAggregated trait signals:")
    for trait_name, signals in aggregated.items():
        if signals:
            score, confidence = infer_trait_score(signals)
            print(f"\n  {trait_name.upper()}: {len(signals)} signals")
            print(f"    Inferred score: {score:.2f} (confidence: {confidence:.2f})")
            for s in signals:
                print(f"      [{s.direction.value}] strength={s.signal_strength:.2f}: \"{s.evidence_quote[:30]}...\"")


def test_model_serialization():
    """Test that models serialize to JSON correctly."""
    print("\n" + "=" * 60)
    print("TEST: Model Serialization")
    print("=" * 60)

    analyses = create_sample_turn_analyses()
    assessment = build_evidence_based_assessment(
        session_id="test-session-001",
        candidate_name="Jin",
        turn_analyses=analyses,
    )

    # Serialize to JSON
    json_str = assessment.model_dump_json(indent=2)
    print(f"✓ Assessment serialized to JSON ({len(json_str)} chars)")

    # Parse back
    from utils.analysis_models import EvidenceBasedAssessment
    parsed = EvidenceBasedAssessment.model_validate_json(json_str)
    print(f"✓ Assessment parsed back from JSON")
    print(f"  - Session: {parsed.session_id}")
    print(f"  - Candidate: {parsed.candidate_name}")
    print(f"  - Turns analyzed: {parsed.total_turns_analyzed}")
    print(f"  - Competencies: {len(parsed.competency_scores)}")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("Evidence-Based Analysis Pipeline Tests")
    print("=" * 60)

    # Test 1: TurnAnalyzer initialization
    await test_turn_analyzer_with_mock()

    # Test 2: Assessment builder
    test_assessment_builder()

    # Test 3: Trait inference
    test_trait_inference()

    # Test 4: Serialization
    test_model_serialization()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
