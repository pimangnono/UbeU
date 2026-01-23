"""
Unit tests for Pressure Cooker core components.
Run with: pytest tests/test_core.py -v
"""

import asyncio
import sys
from pathlib import Path

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


class TestPersonalityModels:
    """Tests for personality data models."""

    def test_personality_vector_creation(self):
        """Test creating a PersonalityVector."""
        from utils.models import PersonalityVector

        vector = PersonalityVector(
            openness=0.8,
            conscientiousness=0.6,
            extraversion=0.4,
            agreeableness=0.7,
            neuroticism=0.3
        )

        assert vector.openness == 0.8
        assert vector.conscientiousness == 0.6
        assert vector.extraversion == 0.4
        assert vector.agreeableness == 0.7
        assert vector.neuroticism == 0.3

    def test_personality_vector_bounds(self):
        """Test that PersonalityVector validates bounds."""
        from utils.models import PersonalityVector
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            PersonalityVector(
                openness=1.5,  # Invalid: > 1.0
                conscientiousness=0.5,
                extraversion=0.5,
                agreeableness=0.5,
                neuroticism=0.5
            )

        with pytest.raises(ValidationError):
            PersonalityVector(
                openness=-0.1,  # Invalid: < 0.0
                conscientiousness=0.5,
                extraversion=0.5,
                agreeableness=0.5,
                neuroticism=0.5
            )

    def test_personality_vector_to_dict(self):
        """Test converting PersonalityVector to dict."""
        from utils.models import PersonalityVector

        vector = PersonalityVector(
            openness=0.8,
            conscientiousness=0.6,
            extraversion=0.4,
            agreeableness=0.7,
            neuroticism=0.3
        )

        d = vector.to_dict()
        assert d["O"] == 0.8
        assert d["C"] == 0.6
        assert d["E"] == 0.4
        assert d["A"] == 0.7
        assert d["N"] == 0.3

    def test_personality_vector_description(self):
        """Test generating natural language description."""
        from utils.models import PersonalityVector

        # High openness and low neuroticism
        vector = PersonalityVector(
            openness=0.9,
            conscientiousness=0.5,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.1
        )

        desc = vector.to_description()
        assert "open to new experiences" in desc.lower()
        assert "calm" in desc.lower() or "stable" in desc.lower()


class TestPersonalityProfiles:
    """Tests for personality profile configurations."""

    def test_get_all_profiles(self):
        """Test that all profiles are accessible."""
        from config.personality_profiles import get_all_profile_ids, get_profile

        profile_ids = get_all_profile_ids()
        assert len(profile_ids) == 12

        for profile_id in profile_ids:
            profile = get_profile(profile_id)
            assert profile.id == profile_id
            assert profile.name
            assert profile.vector

    def test_profile_system_prompt(self):
        """Test that profiles generate valid system prompts."""
        from config.personality_profiles import get_profile

        profile = get_profile("balanced_leader")
        prompt = profile.get_system_prompt_injection()

        assert "Openness" in prompt
        assert "Conscientiousness" in prompt
        assert "personality traits" in prompt.lower()

    def test_invalid_profile_raises(self):
        """Test that invalid profile ID raises error."""
        from config.personality_profiles import get_profile

        with pytest.raises(ValueError):
            get_profile("nonexistent_profile")


class TestScenarios:
    """Tests for scenario configurations."""

    def test_get_all_scenarios(self):
        """Test that all scenarios are accessible."""
        from config.scenarios import get_all_scenario_ids, get_scenario

        scenario_ids = get_all_scenario_ids()
        assert len(scenario_ids) == 4

        for scenario_id in scenario_ids:
            scenario = get_scenario(scenario_id)
            assert scenario.id == scenario_id
            assert scenario.context
            assert scenario.conflict_point

    def test_scenario_turn_limits(self):
        """Test that scenarios have valid turn limits."""
        from config.scenarios import get_all_scenario_ids, get_scenario

        for scenario_id in get_all_scenario_ids():
            scenario = get_scenario(scenario_id)
            assert scenario.turn_limit >= scenario.min_turns
            assert scenario.turn_limit >= 10
            assert scenario.min_turns >= 5


class TestBFIMappings:
    """Tests for BFI behavioral mappings."""

    def test_get_behaviors_for_trait(self):
        """Test retrieving behaviors for specific trait/level."""
        from config.bfi_mappings import get_behaviors_for_trait

        high_openness = get_behaviors_for_trait("openness", "high")
        assert len(high_openness) > 0
        assert all(b.trait == "openness" for b in high_openness)
        assert all(b.level == "high" for b in high_openness)

    def test_get_relevant_behaviors(self):
        """Test getting behaviors based on personality vector."""
        from config.bfi_mappings import get_relevant_behaviors

        # High openness, low conscientiousness
        behaviors = get_relevant_behaviors(
            openness=0.9,
            conscientiousness=0.2,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.5
        )

        traits = [b.trait for b in behaviors]
        assert "openness" in traits
        assert "conscientiousness" in traits

    def test_generate_behavioral_prompt(self):
        """Test generating prompt injection from behaviors."""
        from config.bfi_mappings import (
            get_relevant_behaviors,
            generate_behavioral_prompt_injection
        )

        behaviors = get_relevant_behaviors(
            openness=0.9,
            conscientiousness=0.2,
            extraversion=0.5,
            agreeableness=0.5,
            neuroticism=0.5
        )

        prompt = generate_behavioral_prompt_injection(behaviors)
        assert "behaviors" in prompt.lower()


class TestMockClient:
    """Tests for the mock LLM client."""

    def test_mock_client_creation(self):
        """Test creating a mock client."""
        from clients.llm_client import create_client

        client = create_client(use_mock=True)
        assert client is not None
        assert client.total_requests == 0

    def test_mock_client_generate(self):
        """Test mock client generates responses."""
        import asyncio
        from clients.llm_client import create_client, ModelTier

        async def run_test():
            client = create_client(use_mock=True)
            response = await client.generate(
                "Test prompt",
                tier=ModelTier.PRO
            )

            assert isinstance(response, str)
            assert len(response) > 0
            assert client.total_requests == 1

        asyncio.run(run_test())

    def test_mock_client_role_responses(self):
        """Test mock client returns role-appropriate responses."""
        import asyncio
        from clients.llm_client import create_client, ModelTier

        async def run_test():
            client = create_client(use_mock=True)

            provoker_response = await client.generate(
                "As the provoker, respond...",
                tier=ModelTier.PRO
            )
            assert "disagree" in provoker_response.lower()

            mediator_response = await client.generate(
                "As the mediator, respond...",
                tier=ModelTier.PRO
            )
            assert "understand" in mediator_response.lower() or "perspectives" in mediator_response.lower()

        asyncio.run(run_test())


class TestRateLimiter:
    """Tests for the rate limiter."""

    def test_rate_limiter_creation(self):
        """Test creating a rate limiter."""
        from clients.llm_client import RateLimiter

        limiter = RateLimiter(rpm_limit=2, rpd_limit=50)
        assert limiter.rpm_limit == 2
        assert limiter.rpd_limit == 50
        assert limiter.daily_count == 0

    def test_rate_limiter_remaining(self):
        """Test tracking remaining requests."""
        from clients.llm_client import RateLimiter

        limiter = RateLimiter(rpm_limit=2, rpd_limit=50)

        assert limiter.get_remaining_daily() == 50

        limiter.record_request()
        assert limiter.get_remaining_daily() == 49

        limiter.record_request()
        assert limiter.get_remaining_daily() == 48


class TestIntentClassification:
    """Tests for intent classification."""

    def test_rule_based_classification(self):
        """Test rule-based intent classification."""
        from pipeline.statistics import classify_intent_rule_based
        from utils.models import IntentCategory

        # Assertive
        intent = classify_intent_rule_based("I think we should prioritize this.")
        assert intent == IntentCategory.ASSERTIVE

        # Cooperative
        intent = classify_intent_rule_based("Let's work together on this.")
        assert intent == IntentCategory.COOPERATIVE

        # Anxious
        intent = classify_intent_rule_based("I'm worried about what if this fails?")
        assert intent == IntentCategory.ANXIOUS

    def test_intent_statistics_calculation(self):
        """Test calculating intent statistics."""
        from pipeline.statistics import calculate_intent_statistics
        from utils.models import Turn, SpeakerRole, IntentCategory

        turns = [
            Turn(
                turn_number=0,
                speaker=SpeakerRole.CANDIDATE,
                speaker_name="Alex",
                content="I think we should do this.",
                intent=IntentCategory.ASSERTIVE
            ),
            Turn(
                turn_number=1,
                speaker=SpeakerRole.CANDIDATE,
                speaker_name="Alex",
                content="Let's work together.",
                intent=IntentCategory.COOPERATIVE
            ),
            Turn(
                turn_number=2,
                speaker=SpeakerRole.CANDIDATE,
                speaker_name="Alex",
                content="I believe this is right.",
                intent=IntentCategory.ASSERTIVE
            ),
        ]

        stats = calculate_intent_statistics(turns, candidate_only=True)

        assert stats.total_turns == 3
        assert stats.intent_counts[IntentCategory.ASSERTIVE.value] == 2
        assert stats.intent_counts[IntentCategory.COOPERATIVE.value] == 1
        assert stats.dominant_intent == IntentCategory.ASSERTIVE.value


class TestAssessmentMapping:
    """Tests for assessment score mapping."""

    def test_map_to_assessment(self):
        """Test mapping intent stats to assessment scores."""
        from pipeline.statistics import map_to_assessment
        from utils.models import IntentStatistics, IntentCategory

        stats = IntentStatistics(
            total_turns=10,
            intent_counts={
                IntentCategory.ASSERTIVE.value: 3,
                IntentCategory.COOPERATIVE.value: 4,
                IntentCategory.ANALYTICAL.value: 2,
                IntentCategory.EMPATHETIC.value: 1,
            },
            intent_percentages={
                IntentCategory.ASSERTIVE.value: 30.0,
                IntentCategory.COOPERATIVE.value: 40.0,
                IntentCategory.ANALYTICAL.value: 20.0,
                IntentCategory.EMPATHETIC.value: 10.0,
            },
            dominant_intent=IntentCategory.COOPERATIVE.value,
            secondary_intent=IntentCategory.ASSERTIVE.value,
        )

        assessment = map_to_assessment(stats, tension_avg=0.5)

        assert 0.0 <= assessment.collaboration_score <= 1.0
        assert 0.0 <= assessment.leadership_score <= 1.0
        assert 0.0 <= assessment.stress_management_score <= 1.0
        assert 0.0 <= assessment.communication_score <= 1.0
        assert 0.0 <= assessment.problem_solving_score <= 1.0


class TestTurnCreation:
    """Tests for Turn model."""

    def test_turn_creation(self):
        """Test creating a Turn."""
        from utils.models import Turn, SpeakerRole

        turn = Turn(
            turn_number=0,
            speaker=SpeakerRole.CANDIDATE,
            speaker_name="Alex",
            content="Hello, let's discuss this.",
            tension_level=0.3
        )

        assert turn.turn_number == 0
        assert turn.speaker == SpeakerRole.CANDIDATE
        assert turn.speaker_name == "Alex"
        assert turn.tension_level == 0.3


class TestSessionOutput:
    """Tests for SessionOutput model."""

    def test_session_output_serialization(self):
        """Test SessionOutput serialization."""
        from datetime import datetime
        from utils.models import (
            SessionOutput,
            SessionMetadata,
            PersonalityProfile,
            PersonalityVector,
            ScenarioConfig,
            Turn,
            SpeakerRole,
        )

        metadata = SessionMetadata(
            session_id="test123",
            profile_id="balanced_leader",
            scenario_id="resource_conflict",
            timestamp=datetime.now(),
            total_turns=5,
        )

        profile = PersonalityProfile(
            id="test",
            name="Test Profile",
            description="Test",
            vector=PersonalityVector(
                openness=0.5,
                conscientiousness=0.5,
                extraversion=0.5,
                agreeableness=0.5,
                neuroticism=0.5
            )
        )

        scenario = ScenarioConfig(
            id="test",
            name="Test Scenario",
            description="Test",
            context="Test context",
            conflict_point="Test conflict",
            provoker_goal="Test goal",
            mediator_goal="Test goal",
        )

        turns = [
            Turn(
                turn_number=0,
                speaker=SpeakerRole.CANDIDATE,
                speaker_name="Alex",
                content="Hello"
            )
        ]

        session = SessionOutput(
            metadata=metadata,
            profile=profile,
            scenario=scenario,
            conversation=turns,
        )

        json_str = session.to_json()
        assert "test123" in json_str
        assert "balanced_leader" in json_str

    def test_get_candidate_turns(self):
        """Test filtering candidate turns."""
        from utils.models import SessionOutput, SessionMetadata, Turn, SpeakerRole
        from config.personality_profiles import get_profile
        from config.scenarios import get_scenario
        from datetime import datetime

        session = SessionOutput(
            metadata=SessionMetadata(
                session_id="test",
                profile_id="balanced_leader",
                scenario_id="resource_conflict",
            ),
            profile=get_profile("balanced_leader"),
            scenario=get_scenario("resource_conflict"),
            conversation=[
                Turn(turn_number=0, speaker=SpeakerRole.CANDIDATE, speaker_name="Alex", content="Hi"),
                Turn(turn_number=1, speaker=SpeakerRole.PROVOKER, speaker_name="Jordan", content="Hello"),
                Turn(turn_number=2, speaker=SpeakerRole.CANDIDATE, speaker_name="Alex", content="Bye"),
            ]
        )

        candidate_turns = session.get_candidate_turns()
        assert len(candidate_turns) == 2
        assert all(t.speaker == SpeakerRole.CANDIDATE for t in candidate_turns)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
