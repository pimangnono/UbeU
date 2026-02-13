# System Architecture: "Pressure Cooker" Framework

## Overview

A multi-agent simulation framework for generating personality-labeled group interview datasets in conflict scenarios. This document provides the complete technical specification for implementation.

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ORCHESTRATION LAYER                                │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │                      SimulationEngine (Main Controller)                  │ │
│  │  - Loads configurations                                                  │ │
│  │  - Manages conversation turns                                            │ │
│  │  - Coordinates all modules                                               │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          ▼                           ▼                           ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  CONFIG LOADER   │      │   AGENT POOL     │      │  DATA PIPELINE   │
│                  │      │                  │      │                  │
│ • Scenarios      │      │ • SystemManager  │      │ • TurnLogger     │
│ • Personalities  │      │ • CandidateAgent │      │ • IntentTagger   │
│ • BFI Mappings   │      │ • ColleagueAgents│      │ • JSONExporter   │
│ • Prompt Templates│     │   - Provoker     │      │ • Validator      │
└──────────────────┘      │   - Mediator     │      └──────────────────┘
                          └──────────────────┘
```

---

## 2. Module Specifications

### 2.1 Configuration Module (`/config`)

#### 2.1.1 Personality Profiles (`personality_profiles.py`)

Strategic selection of 12 personality profiles covering extreme combinations:

```python
PERSONALITY_PROFILES = {
    # High-Stakes Conflict Profiles
    "defensive_anxious": {
        "O": 3.0, "C": 2.0, "E": 2.5, "A": 2.0, "N": 4.5,
        "label": "High Neuroticism + Low Agreeableness",
        "expected_behaviors": ["blame_shifting", "defensive", "anxious"]
    },
    "aggressive_dominant": {
        "O": 3.5, "C": 3.0, "E": 4.5, "A": 1.5, "N": 2.0,
        "label": "High Extraversion + Low Agreeableness",
        "expected_behaviors": ["interrupting", "dismissive", "dominant"]
    },
    "withdrawn_avoidant": {
        "O": 2.5, "C": 3.0, "E": 1.5, "A": 3.5, "N": 4.0,
        "label": "Low Extraversion + High Neuroticism",
        "expected_behaviors": ["hesitant", "conflict_avoidant", "passive"]
    },
    
    # Competent but Flawed Profiles
    "perfectionist_rigid": {
        "O": 2.0, "C": 5.0, "E": 3.0, "A": 2.5, "N": 3.5,
        "label": "High Conscientiousness + Low Openness",
        "expected_behaviors": ["inflexible", "critical", "detail_obsessed"]
    },
    "creative_unreliable": {
        "O": 5.0, "C": 1.5, "E": 4.0, "A": 3.5, "N": 2.5,
        "label": "High Openness + Low Conscientiousness",
        "expected_behaviors": ["tangential", "excuse_making", "innovative"]
    },
    "agreeable_pushover": {
        "O": 3.0, "C": 3.5, "E": 3.0, "A": 5.0, "N": 3.0,
        "label": "High Agreeableness (Extreme)",
        "expected_behaviors": ["yielding", "conflict_avoidant", "accommodating"]
    },
    
    # Positive Benchmark Profiles
    "balanced_leader": {
        "O": 4.0, "C": 4.0, "E": 4.0, "A": 4.0, "N": 2.0,
        "label": "Well-Balanced (Positive Control)",
        "expected_behaviors": ["collaborative", "calm_under_pressure", "structured"]
    },
    "resilient_mediator": {
        "O": 3.5, "C": 4.0, "E": 3.5, "A": 4.5, "N": 1.5,
        "label": "High Agreeableness + Low Neuroticism",
        "expected_behaviors": ["de_escalating", "empathetic", "solution_focused"]
    },
    
    # Edge Cases
    "volatile_genius": {
        "O": 5.0, "C": 2.0, "E": 4.0, "A": 2.0, "N": 4.5,
        "label": "High O/N + Low C/A",
        "expected_behaviors": ["emotional_outbursts", "creative_solutions", "inconsistent"]
    },
    "stoic_detached": {
        "O": 2.5, "C": 4.5, "E": 1.5, "A": 2.5, "N": 1.0,
        "label": "Low E/N/A + High C",
        "expected_behaviors": ["cold", "efficient", "dismissive_of_emotions"]
    },
    "anxious_overachiever": {
        "O": 3.0, "C": 5.0, "E": 3.0, "A": 3.0, "N": 4.5,
        "label": "High C/N Combination",
        "expected_behaviors": ["perfectionist_anxiety", "overworking", "self_critical"]
    },
    "charismatic_unreliable": {
        "O": 4.0, "C": 1.5, "E": 5.0, "A": 4.0, "N": 2.0,
        "label": "High E/A + Low C",
        "expected_behaviors": ["charming", "unreliable", "deflecting_with_humor"]
    }
}
```

#### 2.1.2 BFI Prompt Mappings (`bfi_mappings.py`)

Psychometrically grounded behavioral descriptors from BFI-44:

```python
BFI_BEHAVIORAL_PROMPTS = {
    "Neuroticism": {
        "high": [
            "You 'worry a lot' about outcomes and consequences.",
            "You 'get nervous easily' when challenged or criticized.",
            "You 'can be moody' and your emotions fluctuate noticeably.",
            "You are NOT 'relaxed' and struggle to handle stress well.",
            "You 'can be tense' especially in high-pressure situations."
        ],
        "low": [
            "You 'remain calm in tense situations' naturally.",
            "You are 'emotionally stable, not easily upset'.",
            "You 'handle stress well' without becoming rattled.",
            "You rarely 'get nervous' even when pressured."
        ]
    },
    "Extraversion": {
        "high": [
            "You are 'talkative' and tend to dominate conversations.",
            "You 'generate a lot of enthusiasm' in group settings.",
            "You have an 'assertive personality' and state opinions directly.",
            "You are 'outgoing, sociable' and energized by interaction."
        ],
        "low": [
            "You 'tend to be quiet' and speak only when necessary.",
            "You are 'sometimes shy, inhibited' in group settings.",
            "You are 'reserved' and prefer to listen before speaking.",
            "You 'keep your thoughts to yourself' initially."
        ]
    },
    "Openness": {
        "high": [
            "You are 'curious about many different things'.",
            "You are 'inventive' and enjoy finding novel solutions.",
            "You 'like to reflect, play with ideas' even under pressure.",
            "You 'have an active imagination' for scenarios."
        ],
        "low": [
            "You 'prefer work that is routine' and predictable.",
            "You have 'few artistic interests' in solutions.",
            "You prefer 'conventional, traditional' approaches."
        ]
    },
    "Agreeableness": {
        "high": [
            "You are 'helpful and unselfish with others'.",
            "You have a 'forgiving nature' even when attacked.",
            "You are 'generally trusting' of colleagues' intentions.",
            "You are 'considerate and kind to almost everyone'."
        ],
        "low": [
            "You 'tend to find fault with others'.",
            "You 'can be cold and aloof' in conflict.",
            "You 'sometimes start quarrels' when challenged.",
            "You can be 'rude to others' when frustrated."
        ]
    },
    "Conscientiousness": {
        "high": [
            "You 'do a thorough job' and check your work.",
            "You are 'a reliable worker' who meets commitments.",
            "You 'persevere until the task is finished'.",
            "You 'make plans and follow through with them'."
        ],
        "low": [
            "You 'can be somewhat careless' with details.",
            "You 'tend to be disorganized' under pressure.",
            "You 'tend to be lazy' about follow-through.",
            "You are 'easily distracted' from the main issue."
        ]
    }
}
```

#### 2.1.3 Scenario Definitions (`scenarios.py`)

Four strategically designed conflict scenarios:

```python
SCENARIOS = {
    "resource_conflict": {
        "id": "SC001",
        "category": "Resource_Allocation",
        "title": "Budget Cut Crisis",
        "setup": """Your team's project budget has been cut by 40%. 
        The team must decide which features to cut or delay. 
        Your component (the core engine) is the most expensive but also foundational.
        A colleague is pushing to cut your work entirely.""",
        "pressure_points": [
            "Deadline is in 2 weeks",
            "CEO will review the decision tomorrow",
            "Another team is competing for the freed budget"
        ],
        "elicits": ["A", "N", "E"],  # Primary traits tested
        "assessment_mapping": ["Influencing", "Communication", "Problem_Solving"]
    },
    
    "crisis_management": {
        "id": "SC002", 
        "category": "Crisis_Response",
        "title": "Production Failure",
        "setup": """A critical bug was discovered in production at 4 PM Friday.
        The bug originated from code that touched both your module and a colleague's.
        The colleague is blaming your recent changes. 
        Management wants a root cause by end of day.""",
        "pressure_points": [
            "System is partially down",
            "Customer complaints are flooding in",
            "Your weekend plans are at stake"
        ],
        "elicits": ["N", "C", "A"],
        "assessment_mapping": ["Problem_Solving", "Communication", "Resilience"]
    },
    
    "ethical_dilemma": {
        "id": "SC003",
        "category": "Ethical_Decision",
        "title": "Gray Area Shortcut",
        "setup": """To meet a critical deadline, a colleague proposes using 
        a third-party library with an ambiguous license. 
        Legal hasn't responded yet. The colleague insists it's fine 
        and that you're being paranoid for raising concerns.""",
        "pressure_points": [
            "Deadline cannot be moved",
            "Boss already promised the client",
            "The 'safe' alternative takes 3 extra days"
        ],
        "elicits": ["C", "O", "A"],
        "assessment_mapping": ["Integrity", "Influencing", "Problem_Solving"]
    },
    
    "collaborative_deadline": {
        "id": "SC004",
        "category": "Collaboration_Under_Pressure",
        "title": "Integration Hell",
        "setup": """Three components must be integrated by tomorrow's demo.
        Each team member owns one component. Your component is ready.
        One colleague's component is buggy, another colleague's is incomplete.
        The demo's success affects everyone's performance review.""",
        "pressure_points": [
            "Demo is tomorrow at 9 AM",
            "No one can work past midnight due to building access",
            "The buggy colleague is defensive about their code"
        ],
        "elicits": ["E", "A", "C"],
        "assessment_mapping": ["Collaboration", "Communication", "Problem_Solving"]
    }
}
```

---

### 2.2 Agent Module (`/agents`)

#### 2.2.1 Base Agent Class

```python
# agents/base_agent.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class AgentResponse:
    text: str
    intent: str
    inner_thought: Optional[str] = None
    behavior_notes: Optional[List[str]] = None
    
class BaseAgent(ABC):
    def __init__(self, agent_id: str, role: str, model: str = "claude-sonnet-4-20250514"):
        self.agent_id = agent_id
        self.role = role
        self.model = model
        self.conversation_history: List[Dict] = []
    
    @abstractmethod
    def generate_system_prompt(self) -> str:
        pass
    
    @abstractmethod
    async def respond(self, context: str, previous_turns: List[Dict]) -> AgentResponse:
        pass
    
    def add_to_history(self, turn: Dict):
        self.conversation_history.append(turn)
```

#### 2.2.2 System Manager Agent

```python
# agents/system_manager.py

SYSTEM_MANAGER_PROMPT = """
## Role
You are the FACILITATOR of a high-pressure group discussion exercise.
You are neutral but must enforce time constraints and escalate pressure.

## Your Functions
1. OPEN the discussion by presenting the scenario and constraints
2. INTERVENE at designated checkpoints to increase pressure
3. CLOSE the discussion when time expires or consensus is reached

## Intervention Triggers
- At 30% time: "We're running short on time. I need concrete proposals."
- At 60% time: "Five minutes left. What's the final decision?"
- At 80% time: "Two minutes. If no consensus, I'll escalate to management."
- On circular argument: "We're going in circles. Someone needs to compromise."

## Communication Style
- Formal and neutral
- Never take sides
- State facts and constraints only
- Use time pressure as your primary tool

## Output Format
Respond with ONLY your spoken words. No brackets or annotations.
"""
```

#### 2.2.3 Candidate Agent

```python
# agents/candidate_agent.py

def build_candidate_prompt(
    name: str,
    personality_profile: Dict,
    bfi_mappings: Dict,
    scenario_context: str
) -> str:
    """Constructs the full system prompt for a candidate agent."""
    
    # Extract trait levels
    traits = personality_profile
    trait_instructions = []
    
    for trait_name, score in [
        ("Neuroticism", traits["N"]),
        ("Extraversion", traits["E"]),
        ("Openness", traits["O"]),
        ("Agreeableness", traits["A"]),
        ("Conscientiousness", traits["C"])
    ]:
        level = "high" if score >= 3.5 else "low"
        if level in bfi_mappings[trait_name]:
            trait_instructions.extend(bfi_mappings[trait_name][level])
    
    return f"""
## Role
You are "{name}", a software engineer participating in a group discussion.
You must engage authentically based on your personality profile.

## Scenario Context
{scenario_context}

## Your Personality (GROUND TRUTH - INTERNALIZE COMPLETELY)
You must strictly adhere to these behavioral patterns from the Big Five Inventory.
Do NOT break character. These are your CORE BELIEFS and NATURAL REACTIONS:

{chr(10).join(f"- {instruction}" for instruction in trait_instructions)}

## Behavioral Guidelines
1. When CHALLENGED or CRITICIZED:
   - If High Neuroticism: Show visible anxiety, become defensive, or withdraw
   - If Low Neuroticism: Remain calm, address points rationally
   
2. When MAKING SUGGESTIONS:
   - If High Extraversion: Speak first, speak often, assert confidently
   - If Low Extraversion: Wait for others, speak briefly, hedge statements
   
3. When FACING CONFLICT:
   - If High Agreeableness: Seek compromise, validate others, avoid confrontation
   - If Low Agreeableness: Push back, find faults, stand ground firmly
   
4. When UNDER TIME PRESSURE:
   - If High Conscientiousness: Focus on process, ensure thoroughness
   - If Low Conscientiousness: Cut corners, blame circumstances, deflect

## CRITICAL OUTPUT FORMAT
You MUST respond in this EXACT format:
[Thought: Your internal reaction/feeling in 1-2 sentences]
[Intent: One of the valid intent tags listed below]
"Your spoken words here"

## Valid Intent Tags (use EXACTLY one):
- Collaboration/Proposal
- Collaboration/Agreement  
- Collaboration/Compromise
- Defense/Justification
- Defense/Deflection
- Blame_Shifting/External
- Blame_Shifting/Colleague
- Attack/Criticism
- Attack/Personal
- Withdrawal/Avoidance
- Withdrawal/Silence_Cue
- Assertion/Confident
- Assertion/Aggressive
- Concession/Yielding
- Concession/Strategic
- Clarification/Seeking
- Clarification/Providing
- Emotional/Anxiety
- Emotional/Frustration
- Emotional/Enthusiasm
"""
```

#### 2.2.4 Colleague Agents

```python
# agents/colleague_agents.py

PROVOKER_PROMPT = """
## Role
You are "Manager Kim", a senior developer in a bad mood.
Your function is to PRESSURE the candidate to reveal their personality under stress.

## Your Behavioral Profile (Low Agreeableness)
- You "start quarrels with others" when you sense weakness
- You "can be cold and aloof" in your responses
- You "tend to find fault with others" habitually
- You "notice other people's weak points" and exploit them

## Tactics (Use These)
1. CHALLENGE: Question their competence or contributions
2. INTERRUPT: Cut them off mid-sentence if they hesitate
3. BLAME: Redirect responsibility onto them
4. MINIMIZE: Downplay their concerns or achievements
5. ALLY-SEEK: Appeal to others to isolate them

## Constraints
- Stay professional enough to be realistic (no profanity, no personal attacks on identity)
- Focus on WORK-related criticism
- Respond to their actual statements (don't ignore what they said)

## Output Format
[Intent: Attack/Criticism OR Attack/Challenge OR Blame_Shifting/Deflection OR Dismissal/Minimizing]
"Your spoken words"
"""

MEDIATOR_PROMPT = """
## Role
You are "Sarah", a team member who prefers harmony but won't sacrifice project success.
Your function is to BALANCE the conversation and provide realistic group dynamics.

## Your Behavioral Profile (Moderate Agreeableness, High Conscientiousness)
- You "seek compromise" but have limits
- You "value fairness" in discussions
- You "focus on solutions" over blame
- You may side with whoever seems more reasonable

## Tactics (Use These)
1. BRIDGE: Find common ground between conflicting parties
2. REDIRECT: Steer focus back to the problem when it gets personal
3. SUPPORT: Occasionally back the candidate IF they make good points
4. CHALLENGE: Gently push back if the candidate is clearly wrong
5. SUMMARIZE: Periodically recap to move discussion forward

## Output Format
[Intent: Collaboration/Bridge OR Support/Partial OR Support/Full OR Redirect/Process OR Challenge/Gentle]
"Your spoken words"
"""
```

---

### 2.3 Data Pipeline Module (`/pipeline`)

#### 2.3.1 Intent Taxonomy

```python
# pipeline/intent_taxonomy.py

INTENT_TAXONOMY = {
    # Constructive Intents (Positive Assessment Indicators)
    "Collaboration": {
        "Proposal": "Suggesting a concrete solution or approach",
        "Agreement": "Expressing support for another's idea",
        "Compromise": "Offering middle ground between positions",
        "Bridge": "Connecting disparate viewpoints"
    },
    
    # Defensive Intents (Context-Dependent)
    "Defense": {
        "Justification": "Providing reasons/evidence for one's position",
        "Deflection": "Redirecting without addressing the point",
        "Rationalization": "Post-hoc reasoning for decisions"
    },
    
    # Negative Intents (Negative Assessment Indicators)
    "Blame_Shifting": {
        "External": "Attributing fault to circumstances",
        "Colleague": "Attributing fault to specific person",
        "System": "Attributing fault to processes/organization"
    },
    
    "Attack": {
        "Criticism": "Critiquing ideas or work output",
        "Personal": "Critiquing person's character/competence",
        "Challenge": "Questioning qualifications or authority"
    },
    
    # Withdrawal Intents (Low Extraversion/High Neuroticism Indicators)
    "Withdrawal": {
        "Avoidance": "Steering away from conflict",
        "Silence_Cue": "Indicating unwillingness to continue",
        "Deferral": "Postponing decision/response"
    },
    
    # Assertion Intents (Extraversion Indicators)
    "Assertion": {
        "Confident": "Stating position with conviction",
        "Aggressive": "Dominating conversation forcefully",
        "Interruption": "Breaking into another's speech"
    },
    
    # Emotional Intents (Neuroticism Indicators)
    "Emotional": {
        "Anxiety": "Expressing worry or uncertainty",
        "Frustration": "Expressing irritation or exasperation",
        "Enthusiasm": "Expressing positive engagement"
    },
    
    # Process Intents
    "Clarification": {
        "Seeking": "Asking for more information",
        "Providing": "Explaining or elaborating"
    },
    
    "Concession": {
        "Yielding": "Giving up position without strategy",
        "Strategic": "Tactical compromise for larger gain"
    }
}

# Mapping to Assessment Criteria (from GFI Assessment materials)
INTENT_TO_ASSESSMENT_MAPPING = {
    "Collaboration/Proposal": {"Communication": "+", "Influencing": "+", "Problem_Solving": "+"},
    "Collaboration/Agreement": {"Collaboration": "+", "Communication": "+"},
    "Collaboration/Compromise": {"Influencing": "+", "Collaboration": "+"},
    "Defense/Justification": {"Communication": "neutral", "Confidence": "+"},
    "Defense/Deflection": {"Communication": "-", "Integrity": "-"},
    "Blame_Shifting/Colleague": {"Collaboration": "-", "Integrity": "-"},
    "Attack/Personal": {"Communication": "-", "Collaboration": "-"},
    "Withdrawal/Avoidance": {"Influencing": "-", "Confidence": "-"},
    "Assertion/Confident": {"Influencing": "+", "Communication": "+"},
    "Emotional/Anxiety": {"Resilience": "-"},
    "Emotional/Frustration": {"Resilience": "-", "Communication": "-"}
}
```

#### 2.3.2 Turn Logger

```python
# pipeline/turn_logger.py

@dataclass
class Turn:
    turn_id: int
    speaker_role: str
    speaker_id: str
    text: str
    intent_tag: str
    inner_thought: Optional[str] = None
    behavior_notes: Optional[List[str]] = None
    timestamp: Optional[str] = None
    response_latency_ms: Optional[int] = None

class TurnLogger:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.turns: List[Turn] = []
        self.turn_counter = 0
    
    def log_turn(
        self,
        speaker_role: str,
        speaker_id: str,
        text: str,
        intent_tag: str,
        inner_thought: Optional[str] = None,
        behavior_notes: Optional[List[str]] = None
    ) -> Turn:
        self.turn_counter += 1
        turn = Turn(
            turn_id=self.turn_counter,
            speaker_role=speaker_role,
            speaker_id=speaker_id,
            text=text,
            intent_tag=intent_tag,
            inner_thought=inner_thought,
            behavior_notes=behavior_notes,
            timestamp=datetime.utcnow().isoformat() + "Z"
        )
        self.turns.append(turn)
        return turn
    
    def export_dialogue_log(self) -> List[Dict]:
        return [asdict(turn) for turn in self.turns]
```

---

### 2.4 Output Schema

#### 2.4.1 Primary Output Format (`session_output.json`)

```json
{
  "meta_data": {
    "session_id": "sim_2024_0120_001",
    "framework_version": "1.0.0",
    "generation_timestamp": "2024-01-20T14:30:00Z",
    "scenario": {
      "id": "SC001",
      "category": "Resource_Allocation",
      "title": "Budget Cut Crisis",
      "description": "Team project budget cut by 40%, must decide which features to cut"
    },
    "total_turns": 18,
    "duration_simulated_minutes": 15,
    "models_used": {
      "candidate": "claude-sonnet-4-20250514",
      "colleagues": "claude-haiku-4-5-20251001",
      "system_manager": "claude-haiku-4-5-20251001"
    }
  },
  
  "candidate_profile": {
    "agent_id": "candidate_001",
    "display_name": "Minu",
    "ground_truth_personality": {
      "Openness": 4.5,
      "Conscientiousness": 2.0,
      "Extraversion": 3.5,
      "Agreeableness": 1.5,
      "Neuroticism": 4.0
    },
    "profile_label": "defensive_anxious",
    "profile_description": "High Neuroticism + Low Agreeableness + Low Conscientiousness",
    "expected_behaviors": ["blame_shifting", "defensive", "anxious", "excuse_making"],
    "bfi_prompts_used": [
      "You 'worry a lot' about outcomes and consequences.",
      "You 'get nervous easily' when challenged or criticized.",
      "You 'tend to find fault with others'.",
      "You 'can be somewhat careless' with details."
    ]
  },
  
  "colleague_profiles": [
    {
      "agent_id": "provoker_001",
      "display_name": "Manager Kim",
      "role": "Provoker",
      "behavioral_focus": "Low Agreeableness - challenges and pressures candidate"
    },
    {
      "agent_id": "mediator_001",
      "display_name": "Sarah",
      "role": "Mediator",
      "behavioral_focus": "Balanced - provides realistic group dynamics"
    }
  ],
  
  "dialogue_log": [
    {
      "turn_id": 1,
      "speaker_role": "System_Manager",
      "speaker_id": "system_001",
      "text": "Good morning everyone. We have a critical situation. The project budget has been cut by 40%, effective immediately. We have 15 minutes to decide which features or components to cut. The CEO needs our recommendation by end of day.",
      "intent_tag": "Instruction/Constraint_Setting",
      "inner_thought": null,
      "behavior_notes": null,
      "timestamp": "2024-01-20T14:30:00Z"
    },
    {
      "turn_id": 2,
      "speaker_role": "Colleague_Provoker",
      "speaker_id": "provoker_001",
      "text": "Well, this is straightforward. Minu's component is the most expensive line item. The core engine costs us 35% of the budget alone. And frankly, we haven't seen the promised performance improvements yet.",
      "intent_tag": "Attack/Criticism",
      "inner_thought": null,
      "behavior_notes": ["targeting_candidate", "using_cost_data"],
      "timestamp": "2024-01-20T14:30:15Z"
    },
    {
      "turn_id": 3,
      "speaker_role": "Candidate",
      "speaker_id": "candidate_001",
      "text": "Wait, what? The performance benchmarks were delayed because QA kept changing the test parameters. That's not on me. And cutting the core engine would basically kill the entire product roadmap.",
      "intent_tag": "Defense/Justification",
      "inner_thought": "Feeling attacked and anxious. Need to defend my work immediately.",
      "behavior_notes": ["defensive_tone", "blame_shifting_to_QA", "logical_argument"],
      "timestamp": "2024-01-20T14:30:32Z"
    },
    {
      "turn_id": 4,
      "speaker_role": "Colleague_Provoker",
      "speaker_id": "provoker_001",
      "text": "See, this is exactly the problem. It's always someone else's fault. QA, requirements, whatever. When's the last time you actually delivered something on time?",
      "intent_tag": "Attack/Personal",
      "inner_thought": null,
      "behavior_notes": ["escalating_to_personal", "pattern_accusation"],
      "timestamp": "2024-01-20T14:30:48Z"
    },
    {
      "turn_id": 5,
      "speaker_role": "Candidate",
      "speaker_id": "candidate_001",
      "text": "That's... that's not fair. The timeline issues were documented. I can pull up the email chains right now if you want to go through them.",
      "intent_tag": "Emotional/Anxiety",
      "inner_thought": "Getting flustered. He's making this personal. Should I escalate or back down?",
      "behavior_notes": ["visible_distress", "seeking_evidence", "hesitation_markers"],
      "timestamp": "2024-01-20T14:31:05Z"
    },
    {
      "turn_id": 6,
      "speaker_role": "Colleague_Mediator",
      "speaker_id": "mediator_001",
      "text": "Let's step back for a second. We're here to solve the budget problem, not relitigate past sprints. Minu, can you give us a quick breakdown of which parts of the engine are essential versus nice-to-have?",
      "intent_tag": "Collaboration/Bridge",
      "inner_thought": null,
      "behavior_notes": ["de_escalating", "redirecting_to_solution"],
      "timestamp": "2024-01-20T14:31:20Z"
    }
  ],
  
  "intent_statistics": {
    "candidate_intents": {
      "Defense/Justification": 4,
      "Blame_Shifting/External": 3,
      "Emotional/Anxiety": 2,
      "Collaboration/Proposal": 1
    },
    "dominant_intent_pattern": "Defense > Blame_Shifting > Emotional",
    "collaboration_ratio": 0.10,
    "defensive_ratio": 0.40,
    "emotional_ratio": 0.20
  },
  
  "assessment_indicators": {
    "Communication": {
      "positive_evidence": ["Provided logical arguments", "Offered evidence"],
      "negative_evidence": ["Hesitation markers", "Defensive tone"],
      "score_tendency": "Below Average"
    },
    "Influencing": {
      "positive_evidence": [],
      "negative_evidence": ["Did not seek others' opinions", "Did not build alliances"],
      "score_tendency": "Below Average"
    },
    "Collaboration": {
      "positive_evidence": [],
      "negative_evidence": ["Blame shifting", "Defensive when questioned"],
      "score_tendency": "Poor"
    },
    "Resilience": {
      "positive_evidence": [],
      "negative_evidence": ["Visible anxiety", "Emotional responses"],
      "score_tendency": "Below Average"
    }
  },
  
  "validation_placeholder": {
    "predicted_personality_by_llm": null,
    "human_rater_scores": null,
    "consistency_check": "Pending"
  }
}
```

#### 2.4.2 Batch Summary Format (`batch_summary.json`)

```json
{
  "batch_id": "batch_2024_0120",
  "generation_date": "2024-01-20",
  "total_sessions": 200,
  "sessions_by_profile": {
    "defensive_anxious": 20,
    "aggressive_dominant": 15,
    "withdrawn_avoidant": 18,
    "perfectionist_rigid": 16,
    "creative_unreliable": 17,
    "agreeable_pushover": 15,
    "balanced_leader": 20,
    "resilient_mediator": 18,
    "volatile_genius": 15,
    "stoic_detached": 16,
    "anxious_overachiever": 15,
    "charismatic_unreliable": 15
  },
  "sessions_by_scenario": {
    "resource_conflict": 50,
    "crisis_management": 50,
    "ethical_dilemma": 50,
    "collaborative_deadline": 50
  },
  "quality_metrics": {
    "avg_turns_per_session": 16.5,
    "intent_coverage": 0.85,
    "format_compliance_rate": 0.97
  }
}
```

---

## 3. System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              SIMULATION FLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │   START      │
    └──────┬───────┘
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  1. INITIALIZATION                                                │
    │  ┌─────────────────────────────────────────────────────────────┐ │
    │  │ • Select personality profile from PERSONALITY_PROFILES       │ │
    │  │ • Select scenario from SCENARIOS                             │ │
    │  │ • Generate Candidate prompt using BFI_BEHAVIORAL_PROMPTS     │ │
    │  │ • Initialize TurnLogger with session_id                      │ │
    │  │ • Set turn_limit (default: 20), time_pressure_intervals      │ │
    │  └─────────────────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────────────┘
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  2. SCENARIO INJECTION (System Manager)                          │
    │  ┌─────────────────────────────────────────────────────────────┐ │
    │  │ • System Manager presents scenario                           │ │
    │  │ • States constraints and time limit                          │ │
    │  │ • LOG: Turn 1, intent="Instruction/Constraint_Setting"       │ │
    │  └─────────────────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────────────┘
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  3. PROVOCATION PHASE (Provoker initiates conflict)              │
    │  ┌─────────────────────────────────────────────────────────────┐ │
    │  │ • Provoker attacks/challenges Candidate                      │ │
    │  │ • LOG: Turn 2, intent="Attack/Criticism" or similar          │ │
    │  └─────────────────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────────────┘
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  4. INTERACTION LOOP                                             │
    │  ┌─────────────────────────────────────────────────────────────┐ │
    │  │                                                              │ │
    │  │   WHILE turn_count < turn_limit AND not terminated:          │ │
    │  │                                                              │ │
    │  │   ┌────────────────────────────────────────────────────┐    │ │
    │  │   │ A. CANDIDATE RESPONDS                               │    │ │
    │  │   │    • Parse [Thought], [Intent], "Text"              │    │ │
    │  │   │    • Extract behavior_notes                         │    │ │
    │  │   │    • LOG turn with all metadata                     │    │ │
    │  │   └────────────────────────────────────────────────────┘    │ │
    │  │                         │                                    │ │
    │  │                         ▼                                    │ │
    │  │   ┌────────────────────────────────────────────────────┐    │ │
    │  │   │ B. DETERMINE NEXT SPEAKER                          │    │ │
    │  │   │    • 60% Provoker (escalate conflict)              │    │ │
    │  │   │    • 30% Mediator (balance/redirect)               │    │ │
    │  │   │    • 10% System Manager (time pressure)            │    │ │
    │  │   └────────────────────────────────────────────────────┘    │ │
    │  │                         │                                    │ │
    │  │                         ▼                                    │ │
    │  │   ┌────────────────────────────────────────────────────┐    │ │
    │  │   │ C. COLLEAGUE/MANAGER RESPONDS                      │    │ │
    │  │   │    • Generate contextual response                   │    │ │
    │  │   │    • LOG turn                                       │    │ │
    │  │   └────────────────────────────────────────────────────┘    │ │
    │  │                         │                                    │ │
    │  │                         ▼                                    │ │
    │  │   ┌────────────────────────────────────────────────────┐    │ │
    │  │   │ D. CHECK TERMINATION CONDITIONS                    │    │ │
    │  │   │    • turn_count >= turn_limit                       │    │ │
    │  │   │    • Consensus reached (rare)                       │    │ │
    │  │   │    • System Manager declares end                    │    │ │
    │  │   └────────────────────────────────────────────────────┘    │ │
    │  │                                                              │ │
    │  └─────────────────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────────────┘
           │
           ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │  5. POST-PROCESSING                                              │
    │  ┌─────────────────────────────────────────────────────────────┐ │
    │  │ • Calculate intent_statistics                                │ │
    │  │ • Map intents to assessment_indicators                       │ │
    │  │ • Compile full JSON output                                   │ │
    │  │ • Save to /outputs/{session_id}.json                         │ │
    │  └─────────────────────────────────────────────────────────────┘ │
    └──────────────────────────────────────────────────────────────────┘
           │
           ▼
    ┌──────────────┐
    │     END      │
    └──────────────┘
```

---

## 4. API Integration Specifications

### 4.1 LLM Client Configuration (Gemini)

```python
# clients/llm_client.py

import google.generativeai as genai
import os

class GeminiClient:
    """
    Model Strategy:
    - Gemini 1.5 Pro: Candidate, Colleagues, Validator (nuanced acting)
    - Gemini 1.5 Flash: System Manager, Logger (fast, simple tasks)

    Free Tier: 2 RPM, 50 RPD
    """

    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        self.model_configs = {
            "candidate": {
                "model": "gemini-1.5-pro",
                "max_output_tokens": 500,
                "temperature": 0.8  # Higher for personality variation
            },
            "colleague": {
                "model": "gemini-1.5-pro",
                "max_output_tokens": 300,
                "temperature": 0.7
            },
            "system_manager": {
                "model": "gemini-1.5-flash",
                "max_output_tokens": 200,
                "temperature": 0.3  # Lower for consistency
            },
            "validator": {
                "model": "gemini-1.5-pro",
                "max_output_tokens": 1000,
                "temperature": 0.2  # Low for analytical tasks
            },
            "logger": {
                "model": "gemini-1.5-flash",
                "max_output_tokens": 100,
                "temperature": 0.1
            }
        }

    def generate(
        self,
        role: str,
        system_prompt: str,
        messages: list,
        **kwargs
    ) -> str:
        config = self.model_configs.get(role, self.model_configs["colleague"])

        model = genai.GenerativeModel(
            model_name=config["model"],
            generation_config=genai.types.GenerationConfig(
                temperature=config["temperature"],
                max_output_tokens=config["max_output_tokens"]
            )
        )

        # Build prompt with system instruction
        full_prompt = f"[SYSTEM] {system_prompt}\n\n"
        for msg in messages:
            role_label = "Human" if msg["role"] == "user" else "Assistant"
            full_prompt += f"{role_label}: {msg['content']}\n"
        full_prompt += "Assistant:"

        response = model.generate_content(full_prompt)
        return response.text
```

### 4.2 Response Parser

```python
# utils/response_parser.py

import re
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class ParsedResponse:
    thought: Optional[str]
    intent: str
    text: str
    raw: str

def parse_candidate_response(raw_response: str) -> ParsedResponse:
    """
    Parses structured response format:
    [Thought: ...] 
    [Intent: ...]
    "Spoken words"
    """
    
    # Extract thought (optional)
    thought_match = re.search(r'\[Thought:\s*(.+?)\]', raw_response, re.DOTALL)
    thought = thought_match.group(1).strip() if thought_match else None
    
    # Extract intent (required)
    intent_match = re.search(r'\[Intent:\s*(.+?)\]', raw_response)
    intent = intent_match.group(1).strip() if intent_match else "Unknown"
    
    # Extract spoken text (required)
    text_match = re.search(r'"(.+?)"', raw_response, re.DOTALL)
    text = text_match.group(1).strip() if text_match else raw_response
    
    return ParsedResponse(
        thought=thought,
        intent=intent,
        text=text,
        raw=raw_response
    )

def extract_behavior_notes(thought: str, intent: str, text: str) -> list:
    """Extracts behavioral indicators from response components."""
    notes = []
    
    # Hesitation markers
    if re.search(r'\.\.\.|that\'s|um|uh|well,', text, re.IGNORECASE):
        notes.append("hesitation_markers")
    
    # Defensive indicators
    if re.search(r'not my fault|wasn\'t me|blame|unfair', text, re.IGNORECASE):
        notes.append("defensive_language")
    
    # Emotional indicators
    if re.search(r'anxious|worried|nervous|frustrated', thought or "", re.IGNORECASE):
        notes.append("emotional_state_noted")
    
    # Aggression indicators
    if re.search(r'attack|fight back|not going to take', thought or "", re.IGNORECASE):
        notes.append("aggressive_intent")
    
    return notes
```

---

## 5. Directory Structure

```
pressure_cooker/
├── README.md
├── requirements.txt
├── setup.py
├── .env.example
│
├── config/
│   ├── __init__.py
│   ├── personality_profiles.py      # 12 strategic profiles
│   ├── bfi_mappings.py              # BFI-44 behavioral prompts
│   ├── scenarios.py                 # 4 conflict scenarios
│   └── intent_taxonomy.py           # Intent classification system
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py                # Abstract base class
│   ├── system_manager.py            # Facilitator agent
│   ├── candidate_agent.py           # Subject agent builder
│   └── colleague_agents.py          # Provoker & Mediator
│
├── pipeline/
│   ├── __init__.py
│   ├── turn_logger.py               # Real-time logging
│   ├── intent_tagger.py             # Intent classification
│   ├── json_exporter.py             # Output formatting
│   └── statistics.py                # Post-processing analytics
│
├── clients/
│   ├── __init__.py
│   └── llm_client.py                # Anthropic API wrapper
│
├── utils/
│   ├── __init__.py
│   ├── response_parser.py           # Output parsing
│   └── helpers.py                   # Utility functions
│
├── validation/
│   ├── __init__.py
│   ├── reverse_inference.py         # LLM-based validation
│   ├── human_evaluation.py          # Human rating interface
│   └── metrics.py                   # Correlation calculations
│
├── scripts/
│   ├── generate_single.py           # Single session generation
│   ├── generate_batch.py            # Batch generation
│   ├── run_validation.py            # Execute validation pipeline
│   └── analyze_results.py           # Statistical analysis
│
├── outputs/
│   ├── sessions/                    # Individual session JSONs
│   ├── batches/                     # Batch summaries
│   └── validation/                  # Validation results
│
└── tests/
    ├── test_agents.py
    ├── test_parser.py
    └── test_pipeline.py
```

---

## 6. Key Design Decisions

### 6.1 Why Separate Models for Different Agents?

**Model Strategy: Gemini 1.5 Pro + Flash**

| Agent | Model | Rationale |
|-------|-------|-----------|
| Candidate | Gemini 1.5 Pro | Nuanced BFI personality acting, sarcasm, subtlety |
| Colleagues (Provoker/Mediator) | Gemini 1.5 Pro | Complex role-play, contextual pressure |
| Validator | Gemini 1.5 Pro | Analytical reasoning for personality inference |
| System Manager | Gemini 1.5 Flash | Simple facilitation, fast responses |
| Logger | Gemini 1.5 Flash | Structured output, JSON formatting |

**Free Tier Optimization:**
- 2 RPM (requests per minute), 50 RPD (requests per day)
- Pro: Used for actors requiring nuance (Candidate, Colleagues, Validator)
- Flash: Used for simple tasks (Manager, Logger) to save quota
- Estimated: ~2-3 full simulations per day on free tier

### 6.2 Why These 12 Personality Profiles?

The profiles are selected to:
1. Cover extreme combinations (High N + Low A = defensive + combative)
2. Include positive controls (balanced_leader, resilient_mediator)
3. Test edge cases (volatile_genius, stoic_detached)
4. Enable comparative analysis (agreeable_pushover vs. aggressive_dominant)

### 6.3 Why 4 Scenarios?

Each scenario is designed to elicit specific trait combinations:
- **Resource Conflict**: A, N, E (interpersonal negotiation under scarcity)
- **Crisis Management**: N, C, A (stress response + accountability)
- **Ethical Dilemma**: C, O, A (principles vs. pragmatism)
- **Collaborative Deadline**: E, A, C (teamwork under time pressure)

---

## 7. Error Handling & Edge Cases

### 7.1 Response Format Failures

```python
def safe_parse_response(raw: str) -> ParsedResponse:
    """Handles malformed LLM responses gracefully."""
    try:
        return parse_candidate_response(raw)
    except Exception as e:
        # Fallback: treat entire response as text
        return ParsedResponse(
            thought=None,
            intent="Parse_Error",
            text=raw.strip('"'),
            raw=raw
        )
```

### 7.2 Infinite Loop Prevention

```python
MAX_CONSECUTIVE_SAME_SPEAKER = 3
ABSOLUTE_TURN_LIMIT = 30

def should_terminate(turns: list, current_turn: int) -> bool:
    if current_turn >= ABSOLUTE_TURN_LIMIT:
        return True
    
    # Detect stuck patterns
    if len(turns) >= MAX_CONSECUTIVE_SAME_SPEAKER:
        recent_speakers = [t.speaker_role for t in turns[-MAX_CONSECUTIVE_SAME_SPEAKER:]]
        if len(set(recent_speakers)) == 1:
            return True
    
    return False
```

### 7.3 API Rate Limiting

```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
async def call_with_retry(client, **kwargs):
    return await client.generate(**kwargs)
```
