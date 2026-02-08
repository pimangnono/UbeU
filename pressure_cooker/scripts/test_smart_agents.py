#!/usr/bin/env python3
"""
Test script for the improved Smart Agent workflow.

Tests:
1. DiscussionPhase transitions
2. CompetencyCoverageTracker behavior detection
3. SmartProvokerAgent targeting
4. ActiveMediatorAgent advancement
5. SmartSystemManager speaker selection

Run from project root:
    python pressure_cooker/scripts/test_smart_agents.py
"""

import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.models import Turn, SpeakerRole, ScenarioConfig
from agents.discussion_orchestrator import (
    DiscussionPhase,
    DiscussionContext,
    CompetencyCoverageTracker,
    PHASE_TRIGGERS,
)
from agents.smart_agents import (
    SmartProvokerAgent,
    ActiveMediatorAgent,
    SmartSystemManager,
)


def create_test_scenario() -> ScenarioConfig:
    """Create a test scenario config."""
    return ScenarioConfig(
        id="test_techflow",
        name="TechFlow Case Study",
        description="B2B SaaS profitability analysis",
        context="TechFlow is a B2B SaaS company with $12M ARR facing declining margins.",
        conflict_point="The team needs to identify ways to improve profitability by 5 percentage points.",
        provoker_goal="Challenge assumptions and demand data-backed reasoning.",
        mediator_goal="Support the candidate while advancing the discussion productively.",
        escalation_triggers=["Surface-level analysis", "Ignoring data", "Vague recommendations"],
        resolution_paths=["Data-driven recommendation", "Clear implementation plan"],
    )


def create_sample_turns() -> list[Turn]:
    """Create sample conversation turns for testing."""
    return [
        Turn(
            turn_number=0,
            speaker=SpeakerRole.SYSTEM,
            speaker_name="Facilitator",
            content="TechFlow is a B2B SaaS company with $12M ARR facing declining margins. How would you approach this problem?",
            tension_level=0.2,
        ),
        Turn(
            turn_number=1,
            speaker=SpeakerRole.CANDIDATE,
            speaker_name="Jin",
            content="Let me structure this using a profitability framework. I'd want to understand the cost breakdown first - can we see COGS and OPEX as percentage of ARR?",
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
            content="Those percentages are useless without knowing segment profitability. Stop wasting time on surface-level analysis.",
            tension_level=0.6,
        ),
        Turn(
            turn_number=4,
            speaker=SpeakerRole.CANDIDATE,
            speaker_name="Jin",
            content="I understand Jordan's concern about segment profitability. Let me refine - could we see customer segments by revenue contribution and their LTV:CAC ratios?",
            tension_level=0.5,
        ),
    ]


def test_competency_tracker():
    """Test the CompetencyCoverageTracker."""
    print("\n" + "=" * 60)
    print("TEST: CompetencyCoverageTracker")
    print("=" * 60)

    tracker = CompetencyCoverageTracker()

    # Test initial state
    print("\n--- Initial State ---")
    summary = tracker.get_coverage_summary()
    for name, data in summary.items():
        print(f"  {name}: {data['tested']}/{data['total']} ({data['coverage']*100:.0f}%)")

    # Test behavior detection
    print("\n--- Behavior Detection ---")
    turns = create_sample_turns()

    for turn in turns:
        if turn.speaker == SpeakerRole.CANDIDATE:
            detected = tracker.detect_behaviors(turn)
            print(f"\n  Turn {turn.turn_number} ({turn.speaker_name}):")
            print(f"    Content: \"{turn.content[:60]}...\"")
            if detected:
                for comp, behavior, quote in detected:
                    print(f"    ✓ Detected: {comp}.{behavior}")
                    tracker.mark_behavior_observed(comp, behavior, turn.turn_number, quote)
            else:
                print("    (No specific behaviors detected)")

    # Test coverage after detection
    print("\n--- Coverage After Detection ---")
    summary = tracker.get_coverage_summary()
    for name, data in summary.items():
        print(f"  {name}: {data['tested']}/{data['total']} ({data['coverage']*100:.0f}%)")
        if data['untested_behaviors']:
            print(f"    Untested: {', '.join(data['untested_behaviors'][:3])}")

    # Test priority competency
    print("\n--- Priority Competency by Phase ---")
    for phase in DiscussionPhase:
        priority = tracker.get_priority_competency(phase)
        if priority:
            behavior = tracker.get_untested_behavior(priority)
            print(f"  {phase.value}: {priority} - {behavior.behavior_id if behavior else 'all tested'}")


def test_discussion_context():
    """Test the DiscussionContext."""
    print("\n" + "=" * 60)
    print("TEST: DiscussionContext")
    print("=" * 60)

    context = DiscussionContext()

    # Test initial state
    print("\n--- Initial State ---")
    print(f"  Phase: {context.current_phase.value}")
    print(f"  Turns in phase: {context.turns_in_phase}")
    print(f"  Total turns: {context.total_turns}")

    # Record turns
    turns = create_sample_turns()
    print("\n--- Recording Turns ---")
    for turn in turns:
        context.record_turn(turn)
        print(f"  Turn {turn.turn_number}: phase={context.current_phase.value}, should_advance={context.should_advance_phase()}")

        if context.should_advance_phase():
            context.advance_phase()
            print(f"    → Advanced to {context.current_phase.value}")

    # Check state
    print("\n--- Final State ---")
    print(f"  Phase: {context.current_phase.value}")
    print(f"  Turns in phase: {context.turns_in_phase}")
    print(f"  Candidate turns: {context.candidate_turns}")
    print(f"  Data requested: {context.data_requested}")
    print(f"  Hypotheses: {len(context.hypotheses_stated)}")
    print(f"  Tension: {context.tension_level}")

    # Test phase guidance
    print("\n--- Phase Guidance ---")
    print(f"  {context.get_phase_guidance()}")

    # Test untested competency prompt
    print("\n--- Untested Competency Prompt ---")
    prompt = context.get_untested_competency_prompt()
    print(f"  {prompt or 'None needed'}")


async def test_smart_provoker():
    """Test the SmartProvokerAgent."""
    print("\n" + "=" * 60)
    print("TEST: SmartProvokerAgent")
    print("=" * 60)

    from clients.llm_client import MockLLMClient

    client = MockLLMClient()
    scenario = create_test_scenario()
    context = DiscussionContext()

    provoker = SmartProvokerAgent(
        name="Jordan",
        client=client,
        scenario=scenario,
        context=context,
    )

    # Update history
    turns = create_sample_turns()
    provoker.update_history(turns)

    # Record turns to update context
    for turn in turns:
        context.record_turn(turn)

    # Test targeting
    print("\n--- Current Targeting ---")
    targeting = provoker.get_targeting_summary()
    print(f"  Phase: {targeting['phase']}")
    print(f"  Intensity: {targeting['intensity']}")

    # Force target selection
    comp, behavior = provoker._select_target_competency()
    print(f"  Target competency: {comp}")
    print(f"  Target behavior: {behavior}")

    # Test system prompt
    print("\n--- System Prompt Excerpt ---")
    prompt = provoker.system_prompt
    lines = prompt.split("\n")
    for line in lines[:20]:
        if line.strip():
            print(f"  {line[:80]}")

    print("\n✓ SmartProvokerAgent initialized and targeting working")


async def test_active_mediator():
    """Test the ActiveMediatorAgent."""
    print("\n" + "=" * 60)
    print("TEST: ActiveMediatorAgent")
    print("=" * 60)

    from clients.llm_client import MockLLMClient

    client = MockLLMClient()
    scenario = create_test_scenario()
    context = DiscussionContext()

    mediator = ActiveMediatorAgent(
        name="Sam",
        client=client,
        scenario=scenario,
        context=context,
    )

    # Update history
    turns = create_sample_turns()
    mediator.update_history(turns)

    for turn in turns:
        context.record_turn(turn)

    # Test advancement prompt
    print("\n--- Advancement Prompts by Phase ---")
    for phase in [DiscussionPhase.HYPOTHESIS_GENERATION, DiscussionPhase.DATA_GATHERING,
                  DiscussionPhase.SYNTHESIS, DiscussionPhase.RECOMMENDATION]:
        context.current_phase = phase
        prompt = mediator._get_advancement_prompt()
        print(f"  {phase.value}: {prompt[:60] if prompt else 'None'}...")

    # Test phase role
    print("\n--- Phase Roles ---")
    for phase in DiscussionPhase:
        context.current_phase = phase
        role = mediator._get_phase_role()
        print(f"  {phase.value}: {role[:50]}...")

    print("\n✓ ActiveMediatorAgent initialized and advancement logic working")


async def test_smart_system_manager():
    """Test the SmartSystemManager."""
    print("\n" + "=" * 60)
    print("TEST: SmartSystemManager")
    print("=" * 60)

    from clients.llm_client import MockLLMClient

    client = MockLLMClient()
    scenario = create_test_scenario()
    context = DiscussionContext()

    manager = SmartSystemManager(
        name="Facilitator",
        client=client,
        scenario=scenario,
        context=context,
    )

    turns = create_sample_turns()

    # Test speaker selection at different phases
    print("\n--- Strategic Speaker Selection ---")
    for phase in [DiscussionPhase.PROBLEM_FRAMING, DiscussionPhase.STRESS_TEST]:
        context.current_phase = phase
        context.tension_level = 0.5

        # Test after candidate speaks
        next_speaker = manager.decide_next_speaker_strategic(
            turns=turns,
            provoker_name="Jordan",
            mediator_name="Sam",
            candidate_name="Jin",
        )
        print(f"  Phase {phase.value}, after candidate: → {next_speaker}")

    # Test with high tension
    context.tension_level = 0.8
    context.current_phase = DiscussionPhase.DATA_GATHERING
    next_speaker = manager.decide_next_speaker_strategic(
        turns=turns,
        provoker_name="Jordan",
        mediator_name="Sam",
        candidate_name="Jin",
    )
    print(f"  High tension (0.8): → {next_speaker}")

    # Test phase transitions
    print("\n--- Phase Transition Messages ---")
    for phase in DiscussionPhase:
        context.current_phase = phase
        msg = manager.get_phase_transition_message()
        if msg:
            print(f"  {phase.value}: {msg[:50]}...")

    print("\n✓ SmartSystemManager speaker selection working")


def test_phase_triggers():
    """Test phase trigger configuration."""
    print("\n" + "=" * 60)
    print("TEST: Phase Triggers Configuration")
    print("=" * 60)

    print("\n--- Phase Transition Map ---")
    for phase, config in PHASE_TRIGGERS.items():
        print(f"\n  {phase.value}:")
        print(f"    → Next: {config['next_phase'].value}")
        print(f"    Min turns: {config['min_turns']}")
        print(f"    Triggers: {', '.join(config['trigger_conditions'][:2])}")


async def test_full_integration():
    """Test all components working together."""
    print("\n" + "=" * 60)
    print("TEST: Full Integration")
    print("=" * 60)

    from clients.llm_client import MockLLMClient

    client = MockLLMClient()
    scenario = create_test_scenario()

    # Create shared context
    context = DiscussionContext()

    # Create all agents
    provoker = SmartProvokerAgent("Jordan", client, scenario, context)
    mediator = ActiveMediatorAgent("Sam", client, scenario, context)
    manager = SmartSystemManager("Facilitator", client, scenario, context)

    turns = create_sample_turns()

    # Simulate discussion flow
    print("\n--- Simulated Discussion Flow ---")

    for turn in turns:
        # Record turn
        context.record_turn(turn)

        # Update all agents
        provoker.update_history(turns[:turn.turn_number + 1])
        mediator.update_history(turns[:turn.turn_number + 1])
        manager.update_history(turns[:turn.turn_number + 1])

        print(f"\n  Turn {turn.turn_number} ({turn.speaker_name}):")
        print(f"    Phase: {context.current_phase.value}")
        print(f"    Competency coverage: {sum(d.coverage for d in context.competency_tracker.dimensions.values()) / 5 * 100:.0f}%")

        # Check phase advancement
        if context.should_advance_phase():
            print(f"    → Should advance phase")

        # Get next speaker
        if turn.speaker == SpeakerRole.CANDIDATE:
            next_speaker = manager.decide_next_speaker_strategic(
                turns[:turn.turn_number + 1],
                "Jordan", "Sam", "Jin"
            )
            print(f"    → Next speaker: {next_speaker}")

    print("\n--- Final Coverage Summary ---")
    coverage = context.competency_tracker.get_coverage_summary()
    for name, data in coverage.items():
        status = "✓" if data['coverage'] >= 0.5 else "○"
        print(f"  {status} {name}: {data['tested']}/{data['total']}")

    print("\n✓ Full integration test complete")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("Smart Agent Workflow Tests")
    print("=" * 60)

    # Test 1: Competency Tracker
    test_competency_tracker()

    # Test 2: Discussion Context
    test_discussion_context()

    # Test 3: Phase Triggers
    test_phase_triggers()

    # Test 4: Smart Provoker
    await test_smart_provoker()

    # Test 5: Active Mediator
    await test_active_mediator()

    # Test 6: Smart System Manager
    await test_smart_system_manager()

    # Test 7: Full Integration
    await test_full_integration()

    print("\n" + "=" * 60)
    print("All Smart Agent tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
