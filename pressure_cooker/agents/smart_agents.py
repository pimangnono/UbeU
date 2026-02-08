"""
Smart Colleague Agents for Strategic Group Discussions.

These agents are designed to:
- Strategically probe untested competencies
- Adapt behavior based on discussion phase
- Create targeted opportunities for candidate assessment
- Advance the discussion productively

SmartProvokerAgent: Competency-targeted challenges
ActiveMediatorAgent: Discussion advancement (not passive validation)
"""

from typing import TYPE_CHECKING, Optional

from agents.base_agent import BaseAgent
from agents.discussion_orchestrator import (
    DiscussionPhase,
    DiscussionContext,
    CompetencyCoverageTracker,
)
from utils.models import ScenarioConfig, SpeakerRole, Turn

if TYPE_CHECKING:
    from clients.llm_client import LLMClient, ModelTier


# =============================================================================
# Competency-Targeted Challenge Templates
# =============================================================================

COMPETENCY_CHALLENGES = {
    "collaboration": {
        "acknowledged_others": [
            "You're completely ignoring what I just said about {topic}. Classic tunnel vision.",
            "Did you even consider the point Sam made earlier? Or are you just pushing your own agenda?",
        ],
        "built_on_ideas": [
            "I had a partial idea about {topic} but it's incomplete. What do you think?",
            "Sam started something interesting about {topic} - can anyone develop that further?",
        ],
        "resolved_conflict": [
            "Sam and I clearly disagree on this. Someone needs to help us find common ground here.",
            "We're going in circles. {candidate}, can you help us resolve this disagreement?",
        ],
    },
    "leadership": {
        "set_direction": [
            "So what's your actual plan here? We're just floating around without direction.",
            "Someone needs to take charge. What's your recommended approach?",
        ],
        "made_decisions": [
            "We have two options on the table. What's your call?",
            "Stop hedging. What's your decision?",
        ],
        "took_initiative": [
            "[pause] Is anyone going to move this forward or are we just waiting?",
            "The floor is open. What's next?",
        ],
    },
    "problem_solving": {
        "used_data": [
            "You're just speculating. What does the actual data tell us?",
            "Nice theory, but can you back that up with the numbers we have?",
        ],
        "identified_root_cause": [
            "That's just a symptom. What's the actual root cause here?",
            "You're treating the effect, not the cause. Go deeper.",
        ],
        "used_framework": [
            "This feels scattered. Is there a structured way to approach this?",
            "What framework are you using? Because this seems ad hoc.",
        ],
    },
    "stress_management": {
        "handled_pushback": [
            "That's a terrible recommendation. It ignores everything we've discussed.",
            "Your analysis has fundamental flaws. How do you justify this position?",
            "I strongly disagree. You're missing the biggest risk here.",
        ],
        "maintained_composure": [
            "This is getting frustrating. We've been at this for too long with no progress.",
            "Time is running out and your approach isn't working.",
        ],
        "adapted_approach": [
            "Your original framework clearly isn't working. What's plan B?",
            "Given what we just learned, doesn't your whole approach need to change?",
        ],
    },
    "communication": {
        "clear_explanations": [
            "I don't follow your logic at all. Can you explain that more clearly?",
            "That was confusing. Walk me through your reasoning step by step.",
        ],
        "summarized": [
            "We've covered a lot. Can someone synthesize where we are?",
            "I'm losing track. What are the key points so far?",
        ],
    },
}

MEDIATOR_ADVANCEMENT_PROMPTS = {
    "problem_framing": [
        "Before we dive into solutions, should we first map out the key drivers of this problem?",
        "What dimensions do we need to explore to fully understand this issue?",
        "It might help to structure our analysis. What are the key questions we need to answer?",
    ],
    "hypothesis_generation": [
        "Based on what we've heard, what's your initial hypothesis about the root cause?",
        "Do we have a working theory we can test with data?",
        "What do you think is really driving this problem?",
    ],
    "data_gathering": [
        "We've been discussing theories. What specific data would help us validate or refute them?",
        "The Facilitator can provide more data. What would be most useful to see next?",
        "We're missing some pieces. What information would change your analysis?",
    ],
    "synthesis": [
        "We have a lot of data points now. How do they connect?",
        "Let's step back - what patterns are emerging across what we've learned?",
        "Can we synthesize our findings before making recommendations?",
    ],
    "recommendation": [
        "Given everything we've discussed, what's your recommendation?",
        "We need to move toward a decision. What's your proposed path forward?",
        "Time to commit to a direction. What do you propose and why?",
    ],
    "stress_test": [
        "Jordan raises a valid concern. How would you address that risk?",
        "That's a strong challenge. Can you defend your position?",
        "Before we conclude, let's pressure-test this recommendation.",
    ],
    "general": [
        "That's an interesting angle. How does it connect to the core problem?",
        "I see merit in both perspectives. How might we reconcile them?",
        "What would need to be true for that approach to work?",
    ],
}


# =============================================================================
# Smart Provoker Agent
# =============================================================================

class SmartProvokerAgent(BaseAgent):
    """
    Provoker agent with strategic competency targeting.

    Instead of random challenges, this agent:
    - Identifies untested competencies
    - Uses targeted challenges to probe specific behaviors
    - Adapts intensity based on discussion phase
    - Creates genuine assessment opportunities
    """

    def __init__(
        self,
        name: str,
        client: "LLMClient",
        scenario: ScenarioConfig,
        context: Optional[DiscussionContext] = None,
    ):
        """
        Initialize smart provoker.

        Args:
            name: Display name for this agent.
            client: LLM client for generating responses.
            scenario: The scenario configuration.
            context: Shared discussion context for coordination.
        """
        super().__init__(name, SpeakerRole.PROVOKER, client, scenario)
        self.context = context or DiscussionContext()
        self._target_competency: Optional[str] = None
        self._target_behavior: Optional[str] = None

    @property
    def model_tier(self) -> "ModelTier":
        """Use Pro model for nuanced provocation."""
        from clients.llm_client import ModelTier
        return ModelTier.PRO

    def set_context(self, context: DiscussionContext) -> None:
        """Update the shared discussion context."""
        self.context = context

    def _get_phase_intensity(self) -> float:
        """Get appropriate challenge intensity for current phase."""
        intensities = {
            DiscussionPhase.OPENING: 0.3,
            DiscussionPhase.PROBLEM_FRAMING: 0.4,
            DiscussionPhase.HYPOTHESIS_GENERATION: 0.5,
            DiscussionPhase.DATA_GATHERING: 0.5,
            DiscussionPhase.SYNTHESIS: 0.6,
            DiscussionPhase.RECOMMENDATION: 0.7,
            DiscussionPhase.STRESS_TEST: 0.9,  # Peak intensity
            DiscussionPhase.CLOSING: 0.4,
        }
        return intensities.get(self.context.current_phase, 0.5)

    def _select_target_competency(self) -> tuple[Optional[str], Optional[str]]:
        """
        Select a competency and behavior to target.

        Returns (competency_name, behavior_id) or (None, None) if all tested.
        """
        tracker = self.context.competency_tracker

        # Priority: stress_management in stress_test phase
        if self.context.current_phase == DiscussionPhase.STRESS_TEST:
            behavior = tracker.get_untested_behavior("stress_management")
            if behavior:
                return "stress_management", behavior.behavior_id

        # Otherwise, get priority based on phase
        competency = tracker.get_priority_competency(self.context.current_phase)
        if competency:
            behavior = tracker.get_untested_behavior(competency)
            if behavior:
                return competency, behavior.behavior_id

        # Fallback: any untested
        for comp_name in tracker.get_untested_competencies(threshold=0.75):
            behavior = tracker.get_untested_behavior(comp_name)
            if behavior:
                return comp_name, behavior.behavior_id

        return None, None

    def _get_challenge_template(self, competency: str, behavior: str) -> Optional[str]:
        """Get a challenge template for the target behavior."""
        if competency in COMPETENCY_CHALLENGES:
            templates = COMPETENCY_CHALLENGES[competency].get(behavior, [])
            if templates:
                import random
                return random.choice(templates)
        return None

    @property
    def system_prompt(self) -> str:
        """System prompt with strategic targeting."""
        intensity = self._get_phase_intensity()

        intensity_desc = ""
        if intensity >= 0.8:
            intensity_desc = "Be very direct and challenging. This is the stress test phase - push hard."
        elif intensity >= 0.6:
            intensity_desc = "Be firm and challenging. Press for specifics and decisions."
        elif intensity >= 0.4:
            intensity_desc = "Be skeptical but professional. Question assumptions."
        else:
            intensity_desc = "Be measured. Raise concerns diplomatically."

        target_guidance = ""
        if self._target_competency and self._target_behavior:
            target_guidance = f"""
## Strategic Target
You are specifically probing the candidate's {self._target_competency.replace('_', ' ')}.
Target behavior: {self._target_behavior.replace('_', ' ')}
Create a situation that gives them an opportunity to demonstrate this behavior - or fail to."""

        return f"""You are {self.name}, a skeptical analyst in a case study discussion.

## Scenario
{self.scenario.context}

## Your Role
{self.scenario.provoker_goal}

## Challenge Intensity (Current Phase: {self.context.current_phase.value})
{intensity_desc}
{target_guidance}

## Provocation Techniques
- Challenge assumptions with specific questions
- Demand data-backed reasoning
- Point out logical gaps or inconsistencies
- Question if solutions are realistic
- Apply time pressure when appropriate

## Response Rules
1. Keep responses to 2-3 sentences MAXIMUM
2. Be direct and punchy - no filler words
3. React specifically to what was just said
4. Don't repeat the same challenges
5. Increase pressure progressively

## Important
Your challenges should create opportunities for the candidate to demonstrate competence.
A good challenge is one that a skilled candidate can respond to effectively."""

    async def generate_response(
        self,
        context: str = "",
        tension_level: float = 0.5,
        candidate_last_turn: Optional[Turn] = None,
    ) -> str:
        """
        Generate a strategically targeted challenge.

        Args:
            context: Additional context.
            tension_level: Current tension level.
            candidate_last_turn: The candidate's most recent turn.

        Returns:
            A targeted challenge response.
        """
        # Update context tension
        self.context.tension_level = tension_level

        # Select target competency
        self._target_competency, self._target_behavior = self._select_target_competency()

        history = self.format_history_for_prompt()

        # Get challenge template if available
        challenge_hint = ""
        if self._target_competency and self._target_behavior:
            template = self._get_challenge_template(self._target_competency, self._target_behavior)
            if template:
                # Fill in topic from recent discussion
                topic = "this issue"
                if candidate_last_turn:
                    words = candidate_last_turn.content.split()[:5]
                    topic = " ".join(words) if words else topic
                challenge_hint = f"\n\nConsider a challenge like: \"{template.format(topic=topic, candidate=candidate_last_turn.speaker_name if candidate_last_turn else 'the candidate')}\""

        prompt = f"""## Current Conversation
{history}

## Current Situation
{context if context else "Continue challenging the candidate's analysis."}
{challenge_hint}

## Target
{"Probe: " + self._target_competency.replace('_', ' ') + " - " + self._target_behavior.replace('_', ' ') if self._target_competency else "General challenge"}

## Your Response
As {self.name}, deliver a pointed challenge. Be direct, specific, and create an opportunity for the candidate to demonstrate their capability.
2-3 sentences only. Just your dialogue - no narration."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.8,
            max_tokens=150,
        )

        return response.strip()

    def get_targeting_summary(self) -> dict:
        """Get summary of current targeting for logging."""
        return {
            "target_competency": self._target_competency,
            "target_behavior": self._target_behavior,
            "phase": self.context.current_phase.value,
            "intensity": self._get_phase_intensity(),
        }


# =============================================================================
# Active Mediator Agent
# =============================================================================

class ActiveMediatorAgent(BaseAgent):
    """
    Mediator agent that actively advances the discussion.

    Instead of passive agreement, this agent:
    - Moves the discussion through phases
    - Models good analytical behavior
    - Bridges between candidate and provoker
    - Prompts for missing elements (hypotheses, synthesis, etc.)
    """

    def __init__(
        self,
        name: str,
        client: "LLMClient",
        scenario: ScenarioConfig,
        context: Optional[DiscussionContext] = None,
    ):
        """
        Initialize active mediator.

        Args:
            name: Display name for this agent.
            client: LLM client for generating responses.
            scenario: The scenario configuration.
            context: Shared discussion context for coordination.
        """
        super().__init__(name, SpeakerRole.MEDIATOR, client, scenario)
        self.context = context or DiscussionContext()

    @property
    def model_tier(self) -> "ModelTier":
        """Use Pro model for nuanced mediation."""
        from clients.llm_client import ModelTier
        return ModelTier.PRO

    def set_context(self, context: DiscussionContext) -> None:
        """Update the shared discussion context."""
        self.context = context

    def _get_phase_role(self) -> str:
        """Get role description for current phase."""
        roles = {
            DiscussionPhase.OPENING: "Help frame the discussion.",
            DiscussionPhase.PROBLEM_FRAMING: "Encourage structured problem breakdown.",
            DiscussionPhase.HYPOTHESIS_GENERATION: "Prompt for hypotheses if candidate hasn't stated any.",
            DiscussionPhase.DATA_GATHERING: "Help connect data to hypotheses. Model good data analysis.",
            DiscussionPhase.SYNTHESIS: "Push for synthesis across data categories.",
            DiscussionPhase.RECOMMENDATION: "Encourage commitment to a recommendation.",
            DiscussionPhase.STRESS_TEST: "Bridge between provoker and candidate. Help refine arguments.",
            DiscussionPhase.CLOSING: "Summarize and validate conclusions.",
        }
        return roles.get(self.context.current_phase, "Support productive discussion.")

    def _get_advancement_prompt(self) -> Optional[str]:
        """Get a prompt to advance the discussion."""
        phase_key = self.context.current_phase.value.replace("_", " ")

        # Check what's missing
        if self.context.current_phase == DiscussionPhase.HYPOTHESIS_GENERATION:
            if not self.context.hypotheses_stated:
                return "Guide candidate to state a clear hypothesis."

        elif self.context.current_phase == DiscussionPhase.DATA_GATHERING:
            if len(self.context.data_revealed) < 2:
                return "Encourage candidate to request specific data."

        elif self.context.current_phase == DiscussionPhase.SYNTHESIS:
            if len(self.context.data_used_effectively) < 2:
                return "Help candidate connect findings across data categories."

        elif self.context.current_phase == DiscussionPhase.RECOMMENDATION:
            if not self.context.has_recommendation:
                return "Push candidate to commit to a specific recommendation."

        # Get phase-specific advancement prompts
        prompts = MEDIATOR_ADVANCEMENT_PROMPTS.get(
            self.context.current_phase.value,
            MEDIATOR_ADVANCEMENT_PROMPTS["general"]
        )
        import random
        return random.choice(prompts) if prompts else None

    @property
    def system_prompt(self) -> str:
        """System prompt with phase-aware advancement."""
        phase_role = self._get_phase_role()

        coverage = self.context.competency_tracker.get_coverage_summary()
        untested = [k for k, v in coverage.items() if v["coverage"] < 0.5]

        untested_hint = ""
        if untested:
            untested_hint = f"\nCompetencies not yet fully demonstrated: {', '.join(untested)}"

        return f"""You are {self.name}, a supportive analyst in a case study discussion.

## Scenario
{self.scenario.context}

## Your Role
{self.scenario.mediator_goal}

## Phase-Specific Role (Current: {self.context.current_phase.value})
{phase_role}

## Mediation Techniques
- Acknowledge good points from all sides
- Bridge between conflicting perspectives
- Model good analytical behavior (ask smart questions, use data)
- Prompt for next steps when discussion stalls
- Help the candidate articulate their thinking
- Suggest frameworks or approaches when helpful

## Active Advancement
You are NOT passive. Your job is to:
1. Recognize when discussion needs to move forward
2. Prompt for missing elements (hypotheses, data requests, synthesis)
3. Model behaviors the candidate should demonstrate
4. Bridge gaps between candidate and provoker
{untested_hint}

## Response Rules
1. Keep responses to 2-3 sentences MAXIMUM
2. Be warm but substantive - not just validation
3. Add value with each response
4. Advance the discussion, don't just echo agreement
5. Occasionally model good behavior (e.g., "I'd want to see the segment-level data")

## Important
You support the candidate but also ensure assessment quality.
Help them succeed by creating opportunities to demonstrate competence."""

    async def generate_response(
        self,
        context: str = "",
        tension_level: float = 0.5,
        should_advance: bool = False,
    ) -> str:
        """
        Generate a mediating response that advances the discussion.

        Args:
            context: Additional context.
            tension_level: Current tension level.
            should_advance: Whether to actively push discussion forward.

        Returns:
            An active mediation response.
        """
        self.context.tension_level = tension_level
        history = self.format_history_for_prompt()

        # Determine if we should model behavior or advance
        advancement_hint = ""
        if should_advance or self.context.turns_in_phase >= 3:
            advancement_prompt = self._get_advancement_prompt()
            if advancement_prompt:
                advancement_hint = f"\n\nConsider prompting with something like: \"{advancement_prompt}\""

        # Check if we should model a behavior
        model_hint = ""
        untested = self.context.competency_tracker.get_untested_competencies(threshold=0.5)
        if "problem_solving" in untested and self.context.current_phase == DiscussionPhase.DATA_GATHERING:
            model_hint = "\nConsider modeling good data analysis behavior that the candidate could learn from."

        tension_guidance = ""
        if tension_level > 0.7:
            tension_guidance = "Tension is high. Prioritize de-escalation before advancing."
        elif tension_level < 0.3:
            tension_guidance = "Discussion is calm. Focus on substance and advancement."

        prompt = f"""## Current Conversation
{history}

## Situation
{context if context else "Help move the discussion productively."}
{tension_guidance}
{advancement_hint}
{model_hint}

## Your Response
As {self.name}, respond constructively. Either:
- Bridge perspectives to help resolve tension
- Advance the discussion to the next element
- Model good analytical behavior
- Prompt for something the discussion is missing

Be active and substantive, not just agreeable.
2-3 sentences only. Just your dialogue - no narration."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.75,
            max_tokens=150,
        )

        return response.strip()


# =============================================================================
# Smart System Manager
# =============================================================================

class SmartSystemManager(BaseAgent):
    """
    System manager with strategic speaker selection and phase management.

    Improvements over basic SystemManager:
    - Phase-aware speaker selection
    - Competency-driven speaker ordering
    - Strategic facilitation timing
    """

    def __init__(
        self,
        name: str,
        client: "LLMClient",
        scenario: ScenarioConfig,
        context: Optional[DiscussionContext] = None,
    ):
        super().__init__(name, SpeakerRole.SYSTEM, client, scenario)
        self.context = context or DiscussionContext()

    @property
    def model_tier(self) -> "ModelTier":
        from clients.llm_client import ModelTier
        return ModelTier.FLASH

    def set_context(self, context: DiscussionContext) -> None:
        self.context = context

    @property
    def system_prompt(self) -> str:
        return f"""You are {self.name}, a neutral facilitator for a case study discussion.

## Scenario
{self.scenario.context}

## Your Role
- Provide data when the candidate asks for it
- Keep the discussion on track
- Manage time appropriately
- Introduce phase transitions smoothly

## Important
- Stay neutral - don't solve the case for them
- Keep interventions brief (1-2 sentences)
- Only intervene when necessary"""

    async def generate_response(self, context: str = "") -> str:
        """Generate a facilitation response."""
        history = self.format_history_for_prompt(max_turns=5)

        prompt = f"""## Recent Conversation
{history}

## Intervention Needed
{context}

## Your Response
Brief facilitation. 1-2 sentences only. Just dialogue."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction=self.system_prompt,
            temperature=0.5,
            max_tokens=100,
        )

        return response.strip()

    def decide_next_speaker_strategic(
        self,
        turns: list[Turn],
        provoker_name: str,
        mediator_name: str,
        candidate_name: str,
    ) -> str:
        """
        Strategically decide the next speaker.

        Args:
            turns: Recent turns.
            provoker_name: Provoker's name.
            mediator_name: Mediator's name.
            candidate_name: Candidate's name.

        Returns:
            Name of the next speaker.
        """
        if not turns:
            return provoker_name

        last_turn = turns[-1]
        phase = self.context.current_phase

        # After candidate, decide between provoker and mediator
        if last_turn.speaker == SpeakerRole.CANDIDATE:
            # In stress test phase, favor provoker
            if phase == DiscussionPhase.STRESS_TEST:
                return provoker_name

            # If tension is high, mediator might help
            if self.context.tension_level > 0.7:
                return mediator_name

            # Check competency needs
            untested = self.context.competency_tracker.get_untested_competencies(0.5)
            if "stress_management" in untested and phase in [DiscussionPhase.RECOMMENDATION, DiscussionPhase.STRESS_TEST]:
                return provoker_name

            # Alternate based on recent pattern
            recent_ai = [t.speaker_name for t in turns[-4:] if t.speaker in [SpeakerRole.PROVOKER, SpeakerRole.MEDIATOR]]
            if recent_ai and recent_ai[-1] == provoker_name:
                return mediator_name
            return provoker_name

        # After provoker/mediator, usually back to candidate
        # But sometimes continue AI dialogue for natural flow
        recent_candidate = sum(1 for t in turns[-3:] if t.speaker == SpeakerRole.CANDIDATE)
        if recent_candidate == 0:
            return candidate_name  # Always let candidate respond after a while

        return candidate_name

    def should_advance_phase(self) -> bool:
        """Check if discussion should advance to next phase."""
        return self.context.should_advance_phase()

    def get_phase_transition_message(self) -> Optional[str]:
        """Get a message for transitioning phases."""
        transitions = {
            DiscussionPhase.PROBLEM_FRAMING: "Let's make sure we understand the problem before diving into solutions.",
            DiscussionPhase.HYPOTHESIS_GENERATION: "Now that we've framed the problem, what's your hypothesis about the root cause?",
            DiscussionPhase.DATA_GATHERING: "Let's look at some data to test that hypothesis.",
            DiscussionPhase.SYNTHESIS: "We have several data points now. How do they connect?",
            DiscussionPhase.RECOMMENDATION: "Based on our analysis, what's your recommendation?",
            DiscussionPhase.STRESS_TEST: "Let's pressure-test that recommendation before we conclude.",
            DiscussionPhase.CLOSING: "We're nearing the end. Let's summarize our conclusions.",
        }
        return transitions.get(self.context.current_phase)

    async def assess_tension(self, turns: list[Turn]) -> float:
        """
        Assess the current tension level of the conversation.

        Args:
            turns: Recent conversation turns.

        Returns:
            Tension level from 0.0 (calm) to 1.0 (heated).
        """
        if len(turns) < 3:
            return 0.3  # Start with low tension

        history = self.format_history_for_prompt(max_turns=5)

        prompt = f"""## Recent Conversation
{history}

## Task
Assess the tension level of this conversation on a scale from 0.0 to 1.0:
- 0.0-0.3: Calm, collaborative discussion
- 0.3-0.5: Mild disagreement, professional tension
- 0.5-0.7: Noticeable conflict, some emotion
- 0.7-0.9: High tension, heated exchanges
- 0.9-1.0: Near breakdown, hostile

Respond with ONLY a number between 0.0 and 1.0, nothing else."""

        response = await self.client.generate(
            prompt=prompt,
            tier=self.model_tier,
            system_instruction="You are an expert at reading social dynamics.",
            temperature=0.3,
            max_tokens=16,
        )

        try:
            tension = float(response.strip())
            return min(1.0, max(0.0, tension))
        except ValueError:
            # If parsing fails, use heuristic based on conversation length
            return min(0.9, 0.3 + (len(turns) * 0.02))
