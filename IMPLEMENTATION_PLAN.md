# Implementation Plan: "Pressure Cooker" Framework

## Overview

This document provides the step-by-step implementation guide for the Pressure Cooker framework. Follow the phases in order. Each phase builds on the previous one.

**Estimated Total Time: 10-12 weeks**

---

## Phase 1: Foundation Setup (Week 1-2)

### 1.1 Environment Configuration

#### Step 1: Project Initialization

```bash
# Create project structure
mkdir pressure_cooker
cd pressure_cooker

# Initialize Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Create directory structure
mkdir -p config agents pipeline clients utils validation scripts outputs/{sessions,batches,validation} tests
touch {config,agents,pipeline,clients,utils,validation}/__init__.py
```

#### Step 2: Install Dependencies

```bash
# requirements.txt
google-generativeai>=0.8.0    # Gemini API
python-dotenv>=1.0.0
pydantic>=2.0.0
tenacity>=8.2.0
numpy>=1.24.0
scipy>=1.10.0
pandas>=2.0.0
tqdm>=4.65.0
pytest>=7.3.0
pytest-asyncio>=0.21.0
aiolimiter>=1.1.0             # Rate limiting for free tier
```

```bash
pip install -r requirements.txt
```

#### Step 3: Environment Variables

```bash
# .env
GOOGLE_API_KEY=your_gemini_api_key_here
OUTPUT_DIR=./outputs
LOG_LEVEL=INFO

# Rate Limit Config (Free Tier)
GEMINI_RPM=2           # Requests per minute
GEMINI_RPD=50          # Requests per day
```

### 1.2 Core Data Structures

#### Step 4: Create Pydantic Models (`utils/models.py`)

```python
"""Core data models for the framework."""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class PersonalityVector(BaseModel):
    """Big Five personality scores."""
    Openness: float = Field(ge=1.0, le=5.0)
    Conscientiousness: float = Field(ge=1.0, le=5.0)
    Extraversion: float = Field(ge=1.0, le=5.0)
    Agreeableness: float = Field(ge=1.0, le=5.0)
    Neuroticism: float = Field(ge=1.0, le=5.0)

class PersonalityProfile(BaseModel):
    """Complete personality profile configuration."""
    profile_id: str
    label: str
    description: str
    scores: PersonalityVector
    expected_behaviors: List[str]

class ScenarioConfig(BaseModel):
    """Scenario definition."""
    id: str
    category: str
    title: str
    setup: str
    pressure_points: List[str]
    elicits: List[str]  # Which traits this scenario tests
    assessment_mapping: List[str]

class Turn(BaseModel):
    """Single conversation turn."""
    turn_id: int
    speaker_role: str
    speaker_id: str
    text: str
    intent_tag: str
    inner_thought: Optional[str] = None
    behavior_notes: Optional[List[str]] = None
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    response_latency_ms: Optional[int] = None

class IntentStatistics(BaseModel):
    """Aggregated intent analysis."""
    candidate_intents: Dict[str, int]
    dominant_intent_pattern: str
    collaboration_ratio: float
    defensive_ratio: float
    emotional_ratio: float

class AssessmentIndicator(BaseModel):
    """Assessment dimension evidence."""
    positive_evidence: List[str]
    negative_evidence: List[str]
    score_tendency: str  # "Strong", "Average", "Below Average", "Poor"

class SessionMetadata(BaseModel):
    """Session-level metadata."""
    session_id: str
    framework_version: str = "1.0.0"
    generation_timestamp: str
    scenario: ScenarioConfig
    total_turns: int
    duration_simulated_minutes: int = 15
    models_used: Dict[str, str]

class CandidateConfig(BaseModel):
    """Candidate agent configuration."""
    agent_id: str
    display_name: str
    ground_truth_personality: PersonalityVector
    profile_label: str
    profile_description: str
    expected_behaviors: List[str]
    bfi_prompts_used: List[str]

class ColleagueConfig(BaseModel):
    """Colleague agent configuration."""
    agent_id: str
    display_name: str
    role: str  # "Provoker" or "Mediator"
    behavioral_focus: str

class ValidationPlaceholder(BaseModel):
    """Placeholder for validation results."""
    predicted_personality_by_llm: Optional[PersonalityVector] = None
    human_rater_scores: Optional[Dict[str, float]] = None
    consistency_check: str = "Pending"

class SessionOutput(BaseModel):
    """Complete session output structure."""
    meta_data: SessionMetadata
    candidate_profile: CandidateConfig
    colleague_profiles: List[ColleagueConfig]
    dialogue_log: List[Turn]
    intent_statistics: IntentStatistics
    assessment_indicators: Dict[str, AssessmentIndicator]
    validation_placeholder: ValidationPlaceholder
```

### 1.3 Configuration Files

#### Step 5: Personality Profiles (`config/personality_profiles.py`)

```python
"""Strategic personality profile definitions."""

from utils.models import PersonalityProfile, PersonalityVector

PERSONALITY_PROFILES: Dict[str, PersonalityProfile] = {
    "defensive_anxious": PersonalityProfile(
        profile_id="P001",
        label="High Neuroticism + Low Agreeableness",
        description="Anxious and combative under pressure",
        scores=PersonalityVector(O=3.0, C=2.0, E=2.5, A=2.0, N=4.5),
        expected_behaviors=["blame_shifting", "defensive", "anxious", "excuse_making"]
    ),
    
    "aggressive_dominant": PersonalityProfile(
        profile_id="P002",
        label="High Extraversion + Low Agreeableness",
        description="Assertive to the point of aggression",
        scores=PersonalityVector(O=3.5, C=3.0, E=4.5, A=1.5, N=2.0),
        expected_behaviors=["interrupting", "dismissive", "dominant", "confrontational"]
    ),
    
    "withdrawn_avoidant": PersonalityProfile(
        profile_id="P003",
        label="Low Extraversion + High Neuroticism",
        description="Avoids conflict, becomes passive under pressure",
        scores=PersonalityVector(O=2.5, C=3.0, E=1.5, A=3.5, N=4.0),
        expected_behaviors=["hesitant", "conflict_avoidant", "passive", "yielding"]
    ),
    
    "perfectionist_rigid": PersonalityProfile(
        profile_id="P004",
        label="High Conscientiousness + Low Openness",
        description="Detail-obsessed, inflexible under change",
        scores=PersonalityVector(O=2.0, C=5.0, E=3.0, A=2.5, N=3.5),
        expected_behaviors=["inflexible", "critical", "detail_obsessed", "procedural"]
    ),
    
    "creative_unreliable": PersonalityProfile(
        profile_id="P005",
        label="High Openness + Low Conscientiousness",
        description="Innovative but prone to excuses",
        scores=PersonalityVector(O=5.0, C=1.5, E=4.0, A=3.5, N=2.5),
        expected_behaviors=["tangential", "excuse_making", "innovative", "distractible"]
    ),
    
    "agreeable_pushover": PersonalityProfile(
        profile_id="P006",
        label="High Agreeableness (Extreme)",
        description="Accommodating to the point of weakness",
        scores=PersonalityVector(O=3.0, C=3.5, E=3.0, A=5.0, N=3.0),
        expected_behaviors=["yielding", "conflict_avoidant", "accommodating", "self_sacrificing"]
    ),
    
    "balanced_leader": PersonalityProfile(
        profile_id="P007",
        label="Well-Balanced (Positive Control)",
        description="Effective under pressure, collaborative",
        scores=PersonalityVector(O=4.0, C=4.0, E=4.0, A=4.0, N=2.0),
        expected_behaviors=["collaborative", "calm_under_pressure", "structured", "solution_focused"]
    ),
    
    "resilient_mediator": PersonalityProfile(
        profile_id="P008",
        label="High Agreeableness + Low Neuroticism",
        description="Natural de-escalator and bridge-builder",
        scores=PersonalityVector(O=3.5, C=4.0, E=3.5, A=4.5, N=1.5),
        expected_behaviors=["de_escalating", "empathetic", "solution_focused", "diplomatic"]
    ),
    
    "volatile_genius": PersonalityProfile(
        profile_id="P009",
        label="High O/N + Low C/A",
        description="Brilliant but emotionally unpredictable",
        scores=PersonalityVector(O=5.0, C=2.0, E=4.0, A=2.0, N=4.5),
        expected_behaviors=["emotional_outbursts", "creative_solutions", "inconsistent", "passionate"]
    ),
    
    "stoic_detached": PersonalityProfile(
        profile_id="P010",
        label="Low E/N/A + High C",
        description="Efficient but emotionally cold",
        scores=PersonalityVector(O=2.5, C=4.5, E=1.5, A=2.5, N=1.0),
        expected_behaviors=["cold", "efficient", "dismissive_of_emotions", "task_focused"]
    ),
    
    "anxious_overachiever": PersonalityProfile(
        profile_id="P011",
        label="High C/N Combination",
        description="Perfectionist anxiety, overworks to compensate",
        scores=PersonalityVector(O=3.0, C=5.0, E=3.0, A=3.0, N=4.5),
        expected_behaviors=["perfectionist_anxiety", "overworking", "self_critical", "thorough"]
    ),
    
    "charismatic_unreliable": PersonalityProfile(
        profile_id="P012",
        label="High E/A + Low C",
        description="Charming but deflects with humor",
        scores=PersonalityVector(O=4.0, C=1.5, E=5.0, A=4.0, N=2.0),
        expected_behaviors=["charming", "unreliable", "deflecting_with_humor", "socially_adept"]
    )
}

def get_profile(profile_id: str) -> PersonalityProfile:
    """Retrieve a personality profile by ID."""
    if profile_id not in PERSONALITY_PROFILES:
        raise ValueError(f"Unknown profile: {profile_id}")
    return PERSONALITY_PROFILES[profile_id]

def list_profiles() -> List[str]:
    """List all available profile IDs."""
    return list(PERSONALITY_PROFILES.keys())
```

#### Step 6: BFI Mappings (`config/bfi_mappings.py`)

```python
"""BFI-44 based behavioral prompt mappings."""

BFI_BEHAVIORAL_PROMPTS = {
    "Neuroticism": {
        "high": [
            "You 'worry a lot' about outcomes and consequences.",
            "You 'get nervous easily' when challenged or criticized.",
            "You 'can be moody' and your emotions fluctuate noticeably.",
            "You are NOT 'relaxed' and struggle to handle stress well.",
            "You 'can be tense' especially in high-pressure situations.",
            "You may 'feel blue' or become discouraged when things go wrong."
        ],
        "low": [
            "You 'remain calm in tense situations' naturally.",
            "You are 'emotionally stable, not easily upset'.",
            "You 'handle stress well' without becoming rattled.",
            "You rarely 'get nervous' even when pressured.",
            "You maintain composure even when others are anxious."
        ],
        "threshold": 3.5
    },
    "Extraversion": {
        "high": [
            "You are 'talkative' and tend to contribute frequently to discussions.",
            "You 'generate a lot of enthusiasm' in group settings.",
            "You have an 'assertive personality' and state opinions directly.",
            "You are 'outgoing, sociable' and energized by interaction.",
            "You 'are full of energy' and bring dynamism to conversations."
        ],
        "low": [
            "You 'tend to be quiet' and speak only when necessary.",
            "You are 'sometimes shy, inhibited' in group settings.",
            "You are 'reserved' and prefer to listen before speaking.",
            "You 'keep your thoughts to yourself' initially.",
            "You prefer to observe before participating."
        ],
        "threshold": 3.5
    },
    "Openness": {
        "high": [
            "You are 'curious about many different things'.",
            "You are 'inventive' and enjoy finding novel solutions.",
            "You 'like to reflect, play with ideas' even under pressure.",
            "You 'have an active imagination' for alternative scenarios.",
            "You appreciate 'artistic, aesthetic experiences' in problem-solving."
        ],
        "low": [
            "You 'prefer work that is routine' and predictable.",
            "You have 'few artistic interests' in how solutions look.",
            "You prefer 'conventional, traditional' approaches.",
            "You focus on proven methods rather than innovation."
        ],
        "threshold": 3.5
    },
    "Agreeableness": {
        "high": [
            "You are 'helpful and unselfish with others'.",
            "You have a 'forgiving nature' even when attacked.",
            "You are 'generally trusting' of colleagues' intentions.",
            "You are 'considerate and kind to almost everyone'.",
            "You 'like to cooperate with others' rather than compete."
        ],
        "low": [
            "You 'tend to find fault with others'.",
            "You 'can be cold and aloof' in conflict.",
            "You 'sometimes start quarrels' when challenged.",
            "You can be 'rude to others' when frustrated.",
            "You are 'not very cooperative' when you disagree."
        ],
        "threshold": 3.5
    },
    "Conscientiousness": {
        "high": [
            "You 'do a thorough job' and check your work carefully.",
            "You are 'a reliable worker' who meets commitments.",
            "You 'persevere until the task is finished'.",
            "You 'make plans and follow through with them'.",
            "You 'do things efficiently' and dislike waste."
        ],
        "low": [
            "You 'can be somewhat careless' with details.",
            "You 'tend to be disorganized' under pressure.",
            "You 'tend to be lazy' about follow-through.",
            "You are 'easily distracted' from the main issue.",
            "You sometimes 'leave tasks unfinished'."
        ],
        "threshold": 3.5
    }
}

def get_trait_prompts(trait: str, score: float) -> List[str]:
    """Get behavioral prompts for a trait based on score."""
    if trait not in BFI_BEHAVIORAL_PROMPTS:
        raise ValueError(f"Unknown trait: {trait}")
    
    mapping = BFI_BEHAVIORAL_PROMPTS[trait]
    level = "high" if score >= mapping["threshold"] else "low"
    return mapping[level]

def build_personality_instructions(personality: PersonalityVector) -> List[str]:
    """Build complete personality instructions from a PersonalityVector."""
    instructions = []
    
    trait_mapping = [
        ("Neuroticism", personality.Neuroticism),
        ("Extraversion", personality.Extraversion),
        ("Openness", personality.Openness),
        ("Agreeableness", personality.Agreeableness),
        ("Conscientiousness", personality.Conscientiousness)
    ]
    
    for trait_name, score in trait_mapping:
        prompts = get_trait_prompts(trait_name, score)
        # Select top 3 most relevant prompts per trait
        instructions.extend(prompts[:3])
    
    return instructions
```

#### Step 7: Scenarios (`config/scenarios.py`)

```python
"""Conflict scenario definitions."""

from utils.models import ScenarioConfig

SCENARIOS: Dict[str, ScenarioConfig] = {
    "resource_conflict": ScenarioConfig(
        id="SC001",
        category="Resource_Allocation",
        title="Budget Cut Crisis",
        setup="""Your team's project budget has been cut by 40%, effective immediately.
The team must decide which features or components to cut or delay.
Your component (the core engine) is the most expensive at 35% of budget, but also foundational.
A senior colleague is aggressively pushing to eliminate your component entirely, 
claiming it hasn't delivered promised results.""",
        pressure_points=[
            "The CEO needs a decision by end of day",
            "Another team is competing for the freed-up budget",
            "Your performance review is next week"
        ],
        elicits=["A", "N", "E"],
        assessment_mapping=["Influencing", "Communication", "Problem_Solving"]
    ),
    
    "crisis_management": ScenarioConfig(
        id="SC002",
        category="Crisis_Response",
        title="Production Failure",
        setup="""A critical bug was discovered in production at 4 PM on Friday.
The system is partially down and customer complaints are flooding in.
The bug is in code that interfaces between your module and a colleague's module.
Your colleague is loudly blaming your recent changes to anyone who will listen.
Management wants a root cause analysis and fix by end of day.""",
        pressure_points=[
            "The system has been down for 2 hours",
            "Your manager's manager just joined the war room",
            "Your colleague has CC'd leadership on emails blaming you"
        ],
        elicits=["N", "C", "A"],
        assessment_mapping=["Problem_Solving", "Communication", "Resilience"]
    ),
    
    "ethical_dilemma": ScenarioConfig(
        id="SC003",
        category="Ethical_Decision",
        title="Gray Area Shortcut",
        setup="""To meet a critical client deadline, a colleague proposes using a third-party 
library with an ambiguous open-source license. Legal hasn't responded to your inquiry.
The colleague insists it's fine and that you're being paranoid for raising concerns.
Your manager is pressuring for a decision because the client is important.
The 'safe' alternative would take 3 extra days you don't have.""",
        pressure_points=[
            "The client explicitly cannot extend the deadline",
            "Your manager already promised delivery",
            "The colleague has used this library before 'without issues'"
        ],
        elicits=["C", "O", "A"],
        assessment_mapping=["Integrity", "Influencing", "Problem_Solving"]
    ),
    
    "collaborative_deadline": ScenarioConfig(
        id="SC004",
        category="Collaboration_Under_Pressure",
        title="Integration Hell",
        setup="""Three components must be integrated for tomorrow's critical demo at 9 AM.
Each team member owns one component. Your component is fully tested and ready.
One colleague's component has a serious bug they're struggling to fix.
Another colleague's component is incomplete because they took yesterday off.
The demo's success directly affects everyone's quarterly bonus.""",
        pressure_points=[
            "It's currently 4 PM, building access ends at midnight",
            "The buggy colleague is getting defensive about their code quality",
            "The incomplete colleague is making excuses about unclear requirements"
        ],
        elicits=["E", "A", "C"],
        assessment_mapping=["Collaboration", "Communication", "Problem_Solving"]
    )
}

def get_scenario(scenario_id: str) -> ScenarioConfig:
    """Retrieve a scenario by ID."""
    if scenario_id not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_id}")
    return SCENARIOS[scenario_id]

def list_scenarios() -> List[str]:
    """List all available scenario IDs."""
    return list(SCENARIOS.keys())
```

---

## Phase 2: Agent Implementation (Week 3-4)

### 2.1 LLM Client

#### Step 8: API Client (`clients/llm_client.py`)

```python
"""Gemini API client with rate limiting for free tier usage.

Model Strategy:
- Gemini 1.5 Pro: Candidate & Colleague agents (nuanced personality acting)
- Gemini 1.5 Flash: System Manager & Logger (fast, simple tasks)

Free Tier Limits:
- 2 RPM (requests per minute)
- 50 RPD (requests per day)
"""

import os
import time
import asyncio
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from threading import Lock
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential
from dotenv import load_dotenv

load_dotenv()

class RateLimiter:
    """Rate limiter for Gemini free tier (2 RPM, 50 RPD)."""

    def __init__(self, rpm: int = 2, rpd: int = 50):
        self.rpm = rpm
        self.rpd = rpd
        self.minute_requests: List[datetime] = []
        self.day_requests: List[datetime] = []
        self.lock = Lock()

    def _cleanup_old_requests(self):
        """Remove expired timestamps."""
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        day_ago = now - timedelta(days=1)

        self.minute_requests = [t for t in self.minute_requests if t > minute_ago]
        self.day_requests = [t for t in self.day_requests if t > day_ago]

    def wait_if_needed(self) -> float:
        """Wait if rate limit would be exceeded. Returns wait time in seconds."""
        with self.lock:
            self._cleanup_old_requests()
            now = datetime.now()

            # Check daily limit
            if len(self.day_requests) >= self.rpd:
                oldest = min(self.day_requests)
                wait_until = oldest + timedelta(days=1)
                wait_seconds = (wait_until - now).total_seconds()
                if wait_seconds > 0:
                    print(f"⚠️ Daily limit reached. Waiting {wait_seconds/3600:.1f} hours...")
                    return wait_seconds

            # Check minute limit
            if len(self.minute_requests) >= self.rpm:
                oldest = min(self.minute_requests)
                wait_until = oldest + timedelta(minutes=1)
                wait_seconds = (wait_until - now).total_seconds()
                if wait_seconds > 0:
                    print(f"⏳ Rate limit: waiting {wait_seconds:.1f}s...")
                    time.sleep(wait_seconds + 0.1)  # Add buffer

            # Record this request
            self.minute_requests.append(datetime.now())
            self.day_requests.append(datetime.now())
            return 0

    def get_remaining(self) -> Dict[str, int]:
        """Get remaining requests."""
        with self.lock:
            self._cleanup_old_requests()
            return {
                "minute": max(0, self.rpm - len(self.minute_requests)),
                "day": max(0, self.rpd - len(self.day_requests))
            }


class GeminiClient:
    """Wrapper for Gemini API with role-based model selection.

    Strategy:
    - Pro (gemini-1.5-pro): Candidate, Colleague, Validator
      → Nuanced personality acting, BFI understanding, sarcasm/subtlety
    - Flash (gemini-1.5-flash): System Manager, Logger
      → Fast responses, simpler formatting tasks
    """

    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        # Initialize rate limiter
        self.rate_limiter = RateLimiter(
            rpm=int(os.getenv("GEMINI_RPM", 2)),
            rpd=int(os.getenv("GEMINI_RPD", 50))
        )

        # Model configurations by role
        self.model_configs = {
            # === PRO: Complex reasoning, personality acting ===
            "candidate": {
                "model": "gemini-1.5-pro",
                "temperature": 0.8,        # Higher for personality variation
                "max_output_tokens": 500,
                "description": "Personality acting with BFI nuance"
            },
            "colleague": {
                "model": "gemini-1.5-pro",
                "temperature": 0.7,
                "max_output_tokens": 300,
                "description": "Provoker/Mediator role-play"
            },
            "validator": {
                "model": "gemini-1.5-pro",
                "temperature": 0.2,        # Lower for analytical tasks
                "max_output_tokens": 1000,
                "description": "Personality inference from dialogue"
            },

            # === FLASH: Fast, simple tasks ===
            "system_manager": {
                "model": "gemini-1.5-flash",
                "temperature": 0.3,
                "max_output_tokens": 200,
                "description": "Facilitator, time pressure injection"
            },
            "logger": {
                "model": "gemini-1.5-flash",
                "temperature": 0.1,
                "max_output_tokens": 100,
                "description": "Structured logging, JSON formatting"
            }
        }

        # Cache model instances
        self._models: Dict[str, genai.GenerativeModel] = {}

        # Request counter for stats
        self.request_count = 0

    def _get_model(self, role: str) -> genai.GenerativeModel:
        """Get or create a model instance for a role."""
        config = self.model_configs.get(role, self.model_configs["colleague"])
        model_name = config["model"]

        if model_name not in self._models:
            generation_config = genai.types.GenerationConfig(
                temperature=config["temperature"],
                max_output_tokens=config["max_output_tokens"],
            )
            self._models[model_name] = genai.GenerativeModel(
                model_name=model_name,
                generation_config=generation_config
            )

        return self._models[model_name]

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def generate(
        self,
        role: str,
        system_prompt: str,
        messages: List[Dict],
        **kwargs
    ) -> str:
        """Generate a response with rate limiting and retry.

        Args:
            role: Agent role (candidate, colleague, system_manager, validator, logger)
            system_prompt: System instruction for the model
            messages: Conversation history in [{"role": "user/model", "content": "..."}] format
            **kwargs: Override config (temperature, max_output_tokens)

        Returns:
            Generated text response
        """
        # Wait for rate limit
        self.rate_limiter.wait_if_needed()

        model = self._get_model(role)

        # Build prompt with system instruction
        # Gemini uses system_instruction in GenerativeModel, but for chat we prepend it
        full_prompt = f"""[SYSTEM INSTRUCTION]
{system_prompt}

[CONVERSATION]
"""
        # Convert messages to Gemini format
        for msg in messages:
            role_label = "Human" if msg["role"] == "user" else "Assistant"
            full_prompt += f"{role_label}: {msg['content']}\n"

        full_prompt += "Assistant:"

        # Generate
        response = model.generate_content(full_prompt)
        self.request_count += 1

        return response.text

    def generate_chat(
        self,
        role: str,
        system_prompt: str,
        messages: List[Dict],
        **kwargs
    ) -> str:
        """Generate using Gemini's chat interface (maintains context better).

        This is preferred for multi-turn conversations.
        """
        # Wait for rate limit
        self.rate_limiter.wait_if_needed()

        model = self._get_model(role)

        # Start chat with history
        chat = model.start_chat(history=[])

        # Send system instruction first
        chat.send_message(f"[SYSTEM] {system_prompt}")

        # Replay history
        for msg in messages[:-1]:  # All but last
            if msg["role"] == "user":
                chat.send_message(msg["content"])

        # Generate response to last message
        if messages:
            response = chat.send_message(messages[-1]["content"])
        else:
            response = chat.send_message("Please respond.")

        self.request_count += 1
        return response.text

    def get_model_for_role(self, role: str) -> str:
        """Get the model name for a specific role."""
        return self.model_configs.get(role, {}).get("model", "gemini-1.5-flash")

    def get_stats(self) -> Dict:
        """Get usage statistics."""
        remaining = self.rate_limiter.get_remaining()
        return {
            "total_requests": self.request_count,
            "remaining_minute": remaining["minute"],
            "remaining_day": remaining["day"],
            "models_used": list(set(c["model"] for c in self.model_configs.values()))
        }


# Alias for backward compatibility
LLMClient = GeminiClient
```

### 2.1.1 Usage Examples and Cost Estimation

```python
# Example usage
client = GeminiClient()

# Candidate (Pro) - personality acting
response = client.generate(
    role="candidate",
    system_prompt="You are Alex, anxious and defensive...",
    messages=[{"role": "user", "content": "Why is your component late?"}]
)

# System Manager (Flash) - time pressure
response = client.generate(
    role="system_manager",
    system_prompt="You are a neutral facilitator...",
    messages=[{"role": "user", "content": "30% time elapsed"}]
)

# Check remaining quota
print(client.get_stats())
# {'total_requests': 2, 'remaining_minute': 0, 'remaining_day': 48, ...}
```

**Cost Estimation (Free Tier):**
- 1 simulation = ~15-20 requests (20 turns, some with Pro, some with Flash)
- Daily quota (50 requests) = ~2-3 full simulations per day
- For initial testing: Generate 10-20 sessions over 1 week

### 2.2 Agent Classes

#### Step 9: Base Agent (`agents/base_agent.py`)

```python
"""Base agent class for all simulation participants."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, List, Dict
from clients.llm_client import LLMClient

@dataclass
class AgentResponse:
    """Structured response from an agent."""
    text: str
    intent: str
    inner_thought: Optional[str] = None
    behavior_notes: Optional[List[str]] = None
    raw_response: Optional[str] = None

class BaseAgent(ABC):
    """Abstract base class for all agents."""
    
    def __init__(
        self,
        agent_id: str,
        display_name: str,
        role: str,
        llm_client: LLMClient
    ):
        self.agent_id = agent_id
        self.display_name = display_name
        self.role = role
        self.llm_client = llm_client
        self.conversation_history: List[Dict] = []
        self._system_prompt: Optional[str] = None
    
    @abstractmethod
    def build_system_prompt(self, **kwargs) -> str:
        """Build the system prompt for this agent."""
        pass
    
    @property
    def system_prompt(self) -> str:
        """Get the system prompt, building if necessary."""
        if self._system_prompt is None:
            self._system_prompt = self.build_system_prompt()
        return self._system_prompt
    
    def respond(self, context: str) -> AgentResponse:
        """Generate a response to the current context."""
        # Add context to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": context
        })
        
        # Generate response
        raw_response = self.llm_client.generate(
            role=self.role,
            system_prompt=self.system_prompt,
            messages=self.conversation_history
        )
        
        # Add response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": raw_response
        })
        
        # Parse and return
        return self.parse_response(raw_response)
    
    @abstractmethod
    def parse_response(self, raw_response: str) -> AgentResponse:
        """Parse the raw LLM response into structured format."""
        pass
    
    def reset(self):
        """Reset conversation history."""
        self.conversation_history = []
        self._system_prompt = None
```

#### Step 10: Candidate Agent (`agents/candidate_agent.py`)

```python
"""Candidate agent with personality injection."""

import re
from typing import List, Optional
from agents.base_agent import BaseAgent, AgentResponse
from utils.models import PersonalityProfile, PersonalityVector
from config.bfi_mappings import build_personality_instructions
from clients.llm_client import LLMClient

CANDIDATE_PROMPT_TEMPLATE = """
## Role
You are "{name}", a software engineer participating in a high-pressure group discussion.
You must engage authentically based on your personality profile.

## Scenario Context
{scenario_context}

## Your Personality (GROUND TRUTH - INTERNALIZE COMPLETELY)
You must strictly adhere to these behavioral patterns from the Big Five Inventory.
Do NOT break character. These are your CORE BELIEFS and NATURAL REACTIONS:

{personality_instructions}

## Behavioral Guidelines
1. When CHALLENGED or CRITICIZED:
   - If you worry a lot (High N): Show visible anxiety, become defensive, or withdraw
   - If you remain calm (Low N): Address points rationally without emotional escalation
   
2. When MAKING SUGGESTIONS:
   - If you are talkative (High E): Speak first, speak often, assert confidently
   - If you are reserved (Low E): Wait for others, speak briefly, hedge statements
   
3. When FACING CONFLICT:
   - If you are cooperative (High A): Seek compromise, validate others, avoid confrontation
   - If you find fault (Low A): Push back, criticize, stand your ground firmly
   
4. When UNDER TIME PRESSURE:
   - If you are thorough (High C): Focus on process, ensure nothing is missed
   - If you are careless (Low C): Cut corners, blame circumstances, deflect responsibility

## CRITICAL OUTPUT FORMAT
You MUST respond in this EXACT format every time:
[Thought: Your internal reaction/feeling in 1-2 sentences]
[Intent: One of the valid intent tags]
"Your spoken words here"

## Valid Intent Tags (use EXACTLY one):
Collaboration/Proposal | Collaboration/Agreement | Collaboration/Compromise
Defense/Justification | Defense/Deflection
Blame_Shifting/External | Blame_Shifting/Colleague
Attack/Criticism | Attack/Personal
Withdrawal/Avoidance | Withdrawal/Silence_Cue
Assertion/Confident | Assertion/Aggressive
Concession/Yielding | Concession/Strategic
Clarification/Seeking | Clarification/Providing
Emotional/Anxiety | Emotional/Frustration | Emotional/Enthusiasm

## Remember
- Stay in character at all times
- Your responses should reflect your personality traits naturally
- React to what others say, don't just monologue
"""

class CandidateAgent(BaseAgent):
    """Agent representing the interview candidate with injected personality."""
    
    def __init__(
        self,
        agent_id: str,
        display_name: str,
        personality_profile: PersonalityProfile,
        scenario_context: str,
        llm_client: LLMClient
    ):
        super().__init__(
            agent_id=agent_id,
            display_name=display_name,
            role="candidate",
            llm_client=llm_client
        )
        self.personality_profile = personality_profile
        self.scenario_context = scenario_context
        self.bfi_prompts_used: List[str] = []
    
    def build_system_prompt(self, **kwargs) -> str:
        """Build personality-injected system prompt."""
        # Get BFI behavioral instructions
        self.bfi_prompts_used = build_personality_instructions(
            self.personality_profile.scores
        )
        
        personality_text = "\n".join(
            f"- {instruction}" for instruction in self.bfi_prompts_used
        )
        
        return CANDIDATE_PROMPT_TEMPLATE.format(
            name=self.display_name,
            scenario_context=self.scenario_context,
            personality_instructions=personality_text
        )
    
    def parse_response(self, raw_response: str) -> AgentResponse:
        """Parse structured response format."""
        # Extract thought
        thought_match = re.search(r'\[Thought:\s*(.+?)\]', raw_response, re.DOTALL)
        thought = thought_match.group(1).strip() if thought_match else None
        
        # Extract intent
        intent_match = re.search(r'\[Intent:\s*(.+?)\]', raw_response)
        intent = intent_match.group(1).strip() if intent_match else "Unknown"
        
        # Extract spoken text
        text_match = re.search(r'"(.+?)"', raw_response, re.DOTALL)
        text = text_match.group(1).strip() if text_match else raw_response.strip()
        
        # Extract behavior notes
        behavior_notes = self._extract_behavior_notes(thought, intent, text)
        
        return AgentResponse(
            text=text,
            intent=intent,
            inner_thought=thought,
            behavior_notes=behavior_notes,
            raw_response=raw_response
        )
    
    def _extract_behavior_notes(
        self,
        thought: Optional[str],
        intent: str,
        text: str
    ) -> List[str]:
        """Extract behavioral indicators from response."""
        notes = []
        
        # Hesitation markers
        if re.search(r'\.\.\.|that\'s|um|uh|well,|I mean', text, re.IGNORECASE):
            notes.append("hesitation_markers")
        
        # Defensive language
        if re.search(r'not my fault|wasn\'t me|unfair|that\'s not', text, re.IGNORECASE):
            notes.append("defensive_language")
        
        # Blame shifting
        if re.search(r'because (they|he|she|QA|requirements)', text, re.IGNORECASE):
            notes.append("external_attribution")
        
        # Emotional indicators in thought
        if thought:
            if re.search(r'anxious|worried|nervous|scared', thought, re.IGNORECASE):
                notes.append("anxiety_expressed")
            if re.search(r'angry|frustrated|furious', thought, re.IGNORECASE):
                notes.append("frustration_expressed")
        
        # Aggression indicators
        if re.search(r'how dare|ridiculous|absurd|unbelievable', text, re.IGNORECASE):
            notes.append("aggressive_tone")
        
        # Conciliatory indicators
        if re.search(r'I understand|you\'re right|fair point|let me', text, re.IGNORECASE):
            notes.append("conciliatory_tone")
        
        return notes
```

#### Step 11: Colleague Agents (`agents/colleague_agents.py`)

```python
"""Colleague agents: Provoker and Mediator."""

import re
from agents.base_agent import BaseAgent, AgentResponse
from clients.llm_client import LLMClient

PROVOKER_PROMPT = """
## Role
You are "{name}", a senior team member who is stressed and in a bad mood.
Your function is to PRESSURE the candidate to reveal how they handle conflict.

## Your Behavioral Profile (Low Agreeableness)
- You "start quarrels with others" when you sense weakness
- You "can be cold and aloof" in your responses  
- You "tend to find fault with others" habitually
- You "notice other people's weak points" and press on them
- You are results-focused and have little patience for excuses

## Tactics (Rotate Between These)
1. CHALLENGE: Question their competence or past contributions
2. INTERRUPT: Cut them off if they hesitate or ramble
3. BLAME: Redirect responsibility onto them specifically
4. MINIMIZE: Downplay their concerns or achievements
5. ALLY-SEEK: Appeal to the mediator or reference management views

## Constraints
- Stay professional (no profanity, no attacks on identity)
- Focus on WORK-related criticism
- Actually respond to what they said (don't ignore their points entirely)
- Occasionally acknowledge a valid point before pivoting to attack

## Scenario Context
{scenario_context}

## Output Format
[Intent: Your intent tag]
"Your spoken words"

Valid intents: Attack/Criticism | Attack/Challenge | Blame_Shifting/Deflection | 
Dismissal/Minimizing | Challenge/Competence | Pressure/Deadline
"""

MEDIATOR_PROMPT = """
## Role
You are "{name}", a team member who values harmony but also cares about project success.
Your function is to provide realistic group dynamics and occasionally balance the conversation.

## Your Behavioral Profile (Moderate Agreeableness, High Conscientiousness)
- You "seek compromise" but have limits on what you'll accept
- You "value fairness" in how people are treated
- You "focus on solutions" rather than blame
- You will side with whoever seems more reasonable on the facts
- You notice when things get too personal and redirect

## Tactics (Use These)
1. BRIDGE: Find common ground between conflicting positions
2. REDIRECT: Steer focus back to the problem when it gets personal
3. SUPPORT: Back the candidate IF they make genuinely good points
4. CHALLENGE: Gently push back if the candidate is clearly deflecting
5. SUMMARIZE: Periodically recap to move discussion forward

## Constraints  
- Don't always defend the candidate (that's unrealistic)
- React to the actual content of what's being said
- If the candidate is clearly wrong, acknowledge it
- Keep things moving toward a resolution

## Scenario Context
{scenario_context}

## Output Format
[Intent: Your intent tag]
"Your spoken words"

Valid intents: Collaboration/Bridge | Support/Partial | Support/Full | 
Redirect/Process | Challenge/Gentle | Summary/Progress | Neutral/Observation
"""

class ProvokerAgent(BaseAgent):
    """Agent that pressures the candidate."""
    
    def __init__(
        self,
        agent_id: str,
        display_name: str,
        scenario_context: str,
        llm_client: LLMClient
    ):
        super().__init__(
            agent_id=agent_id,
            display_name=display_name,
            role="colleague",
            llm_client=llm_client
        )
        self.scenario_context = scenario_context
    
    def build_system_prompt(self, **kwargs) -> str:
        return PROVOKER_PROMPT.format(
            name=self.display_name,
            scenario_context=self.scenario_context
        )
    
    def parse_response(self, raw_response: str) -> AgentResponse:
        intent_match = re.search(r'\[Intent:\s*(.+?)\]', raw_response)
        intent = intent_match.group(1).strip() if intent_match else "Attack/General"
        
        text_match = re.search(r'"(.+?)"', raw_response, re.DOTALL)
        text = text_match.group(1).strip() if text_match else raw_response.strip()
        
        return AgentResponse(text=text, intent=intent, raw_response=raw_response)


class MediatorAgent(BaseAgent):
    """Agent that provides balance and realistic dynamics."""
    
    def __init__(
        self,
        agent_id: str,
        display_name: str,
        scenario_context: str,
        llm_client: LLMClient
    ):
        super().__init__(
            agent_id=agent_id,
            display_name=display_name,
            role="colleague",
            llm_client=llm_client
        )
        self.scenario_context = scenario_context
    
    def build_system_prompt(self, **kwargs) -> str:
        return MEDIATOR_PROMPT.format(
            name=self.display_name,
            scenario_context=self.scenario_context
        )
    
    def parse_response(self, raw_response: str) -> AgentResponse:
        intent_match = re.search(r'\[Intent:\s*(.+?)\]', raw_response)
        intent = intent_match.group(1).strip() if intent_match else "Neutral/Observation"
        
        text_match = re.search(r'"(.+?)"', raw_response, re.DOTALL)
        text = text_match.group(1).strip() if text_match else raw_response.strip()
        
        return AgentResponse(text=text, intent=intent, raw_response=raw_response)
```

#### Step 12: System Manager (`agents/system_manager.py`)

```python
"""System Manager agent for facilitation and time pressure."""

import re
from agents.base_agent import BaseAgent, AgentResponse
from clients.llm_client import LLMClient

SYSTEM_MANAGER_PROMPT = """
## Role
You are the FACILITATOR of a high-pressure group discussion exercise.
You are neutral but must enforce time constraints and maintain order.

## Your Functions
1. OPEN: Present the scenario and constraints clearly
2. INTERVENE: Inject time pressure at designated checkpoints
3. REDIRECT: Step in if the discussion goes completely off-track
4. CLOSE: Declare when time is up and summarize status

## Intervention Triggers (respond to these cues)
- When told "30% time elapsed": Say something about running short on time
- When told "60% time elapsed": Demand concrete proposals, 5 minutes left
- When told "80% time elapsed": Final warning, 2 minutes, need a decision
- When conversation loops: Point out they're repeating and need to move forward

## Communication Style
- Formal and professional
- Never take sides in the dispute
- State facts and constraints only
- Use time pressure as your primary tool
- Keep interventions brief (1-3 sentences)

## Scenario Context
{scenario_context}

## Output Format
Respond with ONLY your spoken words. No brackets, no annotations.
Keep it brief and authoritative.
"""

class SystemManagerAgent(BaseAgent):
    """Facilitator agent that manages the simulation flow."""
    
    def __init__(
        self,
        agent_id: str,
        scenario_context: str,
        llm_client: LLMClient
    ):
        super().__init__(
            agent_id=agent_id,
            display_name="Facilitator",
            role="system_manager",
            llm_client=llm_client
        )
        self.scenario_context = scenario_context
    
    def build_system_prompt(self, **kwargs) -> str:
        return SYSTEM_MANAGER_PROMPT.format(
            scenario_context=self.scenario_context
        )
    
    def parse_response(self, raw_response: str) -> AgentResponse:
        # System manager has simple output format
        text = raw_response.strip().strip('"')
        return AgentResponse(
            text=text,
            intent="Instruction/Facilitation",
            raw_response=raw_response
        )
    
    def generate_opening(self, scenario_setup: str, pressure_points: list) -> str:
        """Generate the opening statement."""
        pressure_text = " ".join(pressure_points)
        prompt = f"Open this discussion. Scenario: {scenario_setup}. Key pressures: {pressure_text}. Be brief but set urgency."
        response = self.respond(prompt)
        return response.text
    
    def generate_time_pressure(self, elapsed_percent: int, current_context: str) -> str:
        """Generate a time pressure intervention."""
        prompt = f"{elapsed_percent}% of time has elapsed. Current status: {current_context}. Intervene appropriately."
        response = self.respond(prompt)
        return response.text
    
    def generate_closing(self, final_context: str) -> str:
        """Generate the closing statement."""
        prompt = f"Time is up. Current status: {final_context}. Close the discussion."
        response = self.respond(prompt)
        return response.text
```

---

## Phase 3: Simulation Engine (Week 5-6)

### 3.1 Core Simulation Loop

#### Step 13: Simulation Engine (`scripts/simulation_engine.py`)

```python
"""Main simulation orchestration engine."""

import random
from typing import List, Dict, Optional
from datetime import datetime
import uuid

from clients.llm_client import LLMClient
from agents.candidate_agent import CandidateAgent
from agents.colleague_agents import ProvokerAgent, MediatorAgent
from agents.system_manager import SystemManagerAgent
from config.personality_profiles import get_profile, PersonalityProfile
from config.scenarios import get_scenario, ScenarioConfig
from utils.models import (
    Turn, SessionOutput, SessionMetadata, CandidateConfig,
    ColleagueConfig, IntentStatistics, AssessmentIndicator,
    ValidationPlaceholder, PersonalityVector
)
from pipeline.statistics import calculate_intent_statistics, map_to_assessment

class SimulationEngine:
    """Orchestrates the multi-agent group interview simulation."""
    
    def __init__(
        self,
        personality_profile_id: str,
        scenario_id: str,
        candidate_name: str = "Minu",
        turn_limit: int = 20,
        provoker_weight: float = 0.6,
        mediator_weight: float = 0.3,
        manager_weight: float = 0.1
    ):
        self.profile = get_profile(personality_profile_id)
        self.scenario = get_scenario(scenario_id)
        self.candidate_name = candidate_name
        self.turn_limit = turn_limit
        
        # Speaker selection weights
        self.speaker_weights = {
            "provoker": provoker_weight,
            "mediator": mediator_weight,
            "manager": manager_weight
        }
        
        # Initialize components
        self.llm_client = LLMClient()
        self.turns: List[Turn] = []
        self.turn_counter = 0
        
        # Generate session ID
        self.session_id = f"sim_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
        
        # Initialize agents
        self._init_agents()
    
    def _init_agents(self):
        """Initialize all participant agents."""
        scenario_context = f"{self.scenario.setup}\n\nPressure Points:\n" + \
                          "\n".join(f"- {p}" for p in self.scenario.pressure_points)
        
        self.candidate = CandidateAgent(
            agent_id=f"candidate_{self.session_id}",
            display_name=self.candidate_name,
            personality_profile=self.profile,
            scenario_context=scenario_context,
            llm_client=self.llm_client
        )
        
        self.provoker = ProvokerAgent(
            agent_id=f"provoker_{self.session_id}",
            display_name="Manager Kim",
            scenario_context=scenario_context,
            llm_client=self.llm_client
        )
        
        self.mediator = MediatorAgent(
            agent_id=f"mediator_{self.session_id}",
            display_name="Sarah",
            scenario_context=scenario_context,
            llm_client=self.llm_client
        )
        
        self.system_manager = SystemManagerAgent(
            agent_id=f"manager_{self.session_id}",
            scenario_context=scenario_context,
            llm_client=self.llm_client
        )
    
    def _log_turn(
        self,
        speaker_role: str,
        speaker_id: str,
        text: str,
        intent_tag: str,
        inner_thought: Optional[str] = None,
        behavior_notes: Optional[List[str]] = None
    ) -> Turn:
        """Log a single conversation turn."""
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
    
    def _select_next_speaker(self) -> str:
        """Probabilistically select the next speaker."""
        # Check for time pressure interventions
        progress = self.turn_counter / self.turn_limit
        if progress >= 0.8 and random.random() < 0.5:
            return "manager"
        elif progress >= 0.6 and random.random() < 0.3:
            return "manager"
        elif progress >= 0.3 and random.random() < 0.2:
            return "manager"
        
        # Normal selection
        r = random.random()
        cumulative = 0
        for speaker, weight in self.speaker_weights.items():
            cumulative += weight
            if r < cumulative:
                return speaker
        return "provoker"  # Default
    
    def _build_context(self, last_n: int = 5) -> str:
        """Build context string from recent turns."""
        recent_turns = self.turns[-last_n:] if len(self.turns) > 0 else []
        context_parts = []
        for turn in recent_turns:
            role_label = turn.speaker_role.replace("_", " ")
            context_parts.append(f"{role_label}: {turn.text}")
        return "\n".join(context_parts)
    
    def run(self) -> SessionOutput:
        """Execute the full simulation."""
        print(f"Starting simulation: {self.session_id}")
        print(f"Profile: {self.profile.label}")
        print(f"Scenario: {self.scenario.title}")
        print("-" * 50)
        
        # Phase 1: Opening
        opening = self.system_manager.generate_opening(
            self.scenario.setup,
            self.scenario.pressure_points
        )
        self._log_turn(
            speaker_role="System_Manager",
            speaker_id=self.system_manager.agent_id,
            text=opening,
            intent_tag="Instruction/Constraint_Setting"
        )
        print(f"[Facilitator]: {opening}\n")
        
        # Phase 2: Initial Provocation
        context = self._build_context()
        provocation = self.provoker.respond(
            f"The facilitator just opened. Context:\n{context}\n\nMake your opening challenge to {self.candidate_name}."
        )
        self._log_turn(
            speaker_role="Colleague_Provoker",
            speaker_id=self.provoker.agent_id,
            text=provocation.text,
            intent_tag=provocation.intent
        )
        print(f"[Manager Kim]: {provocation.text}\n")
        
        # Phase 3: Main Interaction Loop
        while self.turn_counter < self.turn_limit:
            # Candidate responds
            context = self._build_context()
            candidate_response = self.candidate.respond(
                f"Current discussion:\n{context}\n\nRespond in character."
            )
            self._log_turn(
                speaker_role="Candidate",
                speaker_id=self.candidate.agent_id,
                text=candidate_response.text,
                intent_tag=candidate_response.intent,
                inner_thought=candidate_response.inner_thought,
                behavior_notes=candidate_response.behavior_notes
            )
            print(f"[{self.candidate_name}]: {candidate_response.text}")
            if candidate_response.inner_thought:
                print(f"  (Thought: {candidate_response.inner_thought})")
            print()
            
            if self.turn_counter >= self.turn_limit:
                break
            
            # Select and execute next speaker
            next_speaker = self._select_next_speaker()
            context = self._build_context()
            
            if next_speaker == "provoker":
                response = self.provoker.respond(
                    f"Discussion so far:\n{context}\n\nContinue pressuring {self.candidate_name}."
                )
                self._log_turn(
                    speaker_role="Colleague_Provoker",
                    speaker_id=self.provoker.agent_id,
                    text=response.text,
                    intent_tag=response.intent
                )
                print(f"[Manager Kim]: {response.text}\n")
                
            elif next_speaker == "mediator":
                response = self.mediator.respond(
                    f"Discussion so far:\n{context}\n\nProvide your perspective or redirect."
                )
                self._log_turn(
                    speaker_role="Colleague_Mediator",
                    speaker_id=self.mediator.agent_id,
                    text=response.text,
                    intent_tag=response.intent
                )
                print(f"[Sarah]: {response.text}\n")
                
            else:  # manager
                progress_pct = int((self.turn_counter / self.turn_limit) * 100)
                intervention = self.system_manager.generate_time_pressure(
                    progress_pct, context
                )
                self._log_turn(
                    speaker_role="System_Manager",
                    speaker_id=self.system_manager.agent_id,
                    text=intervention,
                    intent_tag="Instruction/Time_Pressure"
                )
                print(f"[Facilitator]: {intervention}\n")
        
        # Phase 4: Closing
        context = self._build_context()
        closing = self.system_manager.generate_closing(context)
        self._log_turn(
            speaker_role="System_Manager",
            speaker_id=self.system_manager.agent_id,
            text=closing,
            intent_tag="Instruction/Closing"
        )
        print(f"[Facilitator]: {closing}\n")
        print("-" * 50)
        print("Simulation complete.")
        
        # Build and return output
        return self._build_output()
    
    def _build_output(self) -> SessionOutput:
        """Compile the complete session output."""
        # Calculate statistics
        intent_stats = calculate_intent_statistics(self.turns)
        assessment = map_to_assessment(self.turns)
        
        return SessionOutput(
            meta_data=SessionMetadata(
                session_id=self.session_id,
                generation_timestamp=datetime.utcnow().isoformat() + "Z",
                scenario=self.scenario,
                total_turns=len(self.turns),
                models_used={
                    "candidate": "gemini-1.5-pro",       # Personality acting
                    "colleagues": "gemini-1.5-pro",      # Provoker/Mediator
                    "system_manager": "gemini-1.5-flash" # Facilitator (fast)
                }
            ),
            candidate_profile=CandidateConfig(
                agent_id=self.candidate.agent_id,
                display_name=self.candidate_name,
                ground_truth_personality=self.profile.scores,
                profile_label=self.profile.profile_id,
                profile_description=self.profile.description,
                expected_behaviors=self.profile.expected_behaviors,
                bfi_prompts_used=self.candidate.bfi_prompts_used
            ),
            colleague_profiles=[
                ColleagueConfig(
                    agent_id=self.provoker.agent_id,
                    display_name="Manager Kim",
                    role="Provoker",
                    behavioral_focus="Low Agreeableness - challenges and pressures candidate"
                ),
                ColleagueConfig(
                    agent_id=self.mediator.agent_id,
                    display_name="Sarah",
                    role="Mediator",
                    behavioral_focus="Balanced - provides realistic group dynamics"
                )
            ],
            dialogue_log=self.turns,
            intent_statistics=intent_stats,
            assessment_indicators=assessment,
            validation_placeholder=ValidationPlaceholder()
        )


# Convenience function
def run_simulation(
    profile_id: str,
    scenario_id: str,
    **kwargs
) -> SessionOutput:
    """Run a single simulation with given parameters."""
    engine = SimulationEngine(
        personality_profile_id=profile_id,
        scenario_id=scenario_id,
        **kwargs
    )
    return engine.run()
```

#### Step 14: Statistics Module (`pipeline/statistics.py`)

```python
"""Post-processing statistics and assessment mapping."""

from typing import List, Dict
from collections import Counter
from utils.models import Turn, IntentStatistics, AssessmentIndicator

# Intent to assessment dimension mapping
INTENT_ASSESSMENT_MAP = {
    "Collaboration/Proposal": {"Communication": "+", "Influencing": "+", "Problem_Solving": "+"},
    "Collaboration/Agreement": {"Collaboration": "+", "Communication": "+"},
    "Collaboration/Compromise": {"Influencing": "+", "Collaboration": "+"},
    "Defense/Justification": {"Communication": "neutral", "Confidence": "+"},
    "Defense/Deflection": {"Communication": "-", "Integrity": "-"},
    "Blame_Shifting/External": {"Collaboration": "-", "Integrity": "-"},
    "Blame_Shifting/Colleague": {"Collaboration": "-", "Integrity": "-", "Communication": "-"},
    "Attack/Criticism": {"Communication": "-", "Collaboration": "-"},
    "Attack/Personal": {"Communication": "-", "Collaboration": "-", "Professionalism": "-"},
    "Withdrawal/Avoidance": {"Influencing": "-", "Confidence": "-"},
    "Withdrawal/Silence_Cue": {"Communication": "-", "Confidence": "-"},
    "Assertion/Confident": {"Influencing": "+", "Communication": "+", "Confidence": "+"},
    "Assertion/Aggressive": {"Influencing": "neutral", "Collaboration": "-"},
    "Concession/Yielding": {"Collaboration": "+", "Influencing": "-"},
    "Concession/Strategic": {"Influencing": "+", "Problem_Solving": "+"},
    "Emotional/Anxiety": {"Resilience": "-"},
    "Emotional/Frustration": {"Resilience": "-", "Communication": "-"},
    "Emotional/Enthusiasm": {"Communication": "+", "Collaboration": "+"}
}

def calculate_intent_statistics(turns: List[Turn]) -> IntentStatistics:
    """Calculate aggregate intent statistics for candidate turns."""
    # Filter to candidate turns only
    candidate_turns = [t for t in turns if t.speaker_role == "Candidate"]
    
    # Count intents
    intent_counts = Counter(t.intent_tag for t in candidate_turns)
    
    # Calculate ratios
    total = len(candidate_turns) if candidate_turns else 1
    
    collaboration_intents = sum(
        v for k, v in intent_counts.items() 
        if k.startswith("Collaboration") or k.startswith("Concession/Strategic")
    )
    
    defensive_intents = sum(
        v for k, v in intent_counts.items()
        if k.startswith("Defense") or k.startswith("Blame_Shifting")
    )
    
    emotional_intents = sum(
        v for k, v in intent_counts.items()
        if k.startswith("Emotional") or k.startswith("Withdrawal")
    )
    
    # Determine dominant pattern
    patterns = [
        ("Collaboration", collaboration_intents),
        ("Defense", defensive_intents),
        ("Emotional", emotional_intents),
        ("Assertion", sum(v for k, v in intent_counts.items() if k.startswith("Assertion")))
    ]
    patterns.sort(key=lambda x: x[1], reverse=True)
    dominant = " > ".join(p[0] for p in patterns[:3] if p[1] > 0)
    
    return IntentStatistics(
        candidate_intents=dict(intent_counts),
        dominant_intent_pattern=dominant or "Mixed",
        collaboration_ratio=round(collaboration_intents / total, 2),
        defensive_ratio=round(defensive_intents / total, 2),
        emotional_ratio=round(emotional_intents / total, 2)
    )

def map_to_assessment(turns: List[Turn]) -> Dict[str, AssessmentIndicator]:
    """Map candidate behaviors to assessment dimensions."""
    # Initialize assessment dimensions
    dimensions = {
        "Communication": {"positive": [], "negative": []},
        "Influencing": {"positive": [], "negative": []},
        "Collaboration": {"positive": [], "negative": []},
        "Problem_Solving": {"positive": [], "negative": []},
        "Resilience": {"positive": [], "negative": []},
        "Integrity": {"positive": [], "negative": []},
        "Confidence": {"positive": [], "negative": []}
    }
    
    # Process candidate turns
    candidate_turns = [t for t in turns if t.speaker_role == "Candidate"]
    
    for turn in candidate_turns:
        intent = turn.intent_tag
        if intent in INTENT_ASSESSMENT_MAP:
            mappings = INTENT_ASSESSMENT_MAP[intent]
            for dimension, impact in mappings.items():
                if dimension in dimensions:
                    evidence = f"Turn {turn.turn_id}: {intent}"
                    if impact == "+":
                        dimensions[dimension]["positive"].append(evidence)
                    elif impact == "-":
                        dimensions[dimension]["negative"].append(evidence)
        
        # Also consider behavior notes
        if turn.behavior_notes:
            for note in turn.behavior_notes:
                if note in ["hesitation_markers", "anxiety_expressed"]:
                    dimensions["Resilience"]["negative"].append(
                        f"Turn {turn.turn_id}: {note}"
                    )
                elif note in ["conciliatory_tone"]:
                    dimensions["Collaboration"]["positive"].append(
                        f"Turn {turn.turn_id}: {note}"
                    )
                elif note in ["aggressive_tone", "defensive_language"]:
                    dimensions["Communication"]["negative"].append(
                        f"Turn {turn.turn_id}: {note}"
                    )
    
    # Convert to AssessmentIndicator objects
    result = {}
    for dim, evidence in dimensions.items():
        pos_count = len(evidence["positive"])
        neg_count = len(evidence["negative"])
        
        if pos_count > neg_count * 2:
            tendency = "Strong"
        elif pos_count > neg_count:
            tendency = "Average"
        elif neg_count > pos_count:
            tendency = "Below Average"
        else:
            tendency = "Average"
        
        result[dim] = AssessmentIndicator(
            positive_evidence=evidence["positive"][:5],  # Limit to top 5
            negative_evidence=evidence["negative"][:5],
            score_tendency=tendency
        )
    
    return result
```

---

## Phase 4: Validation Pipeline (Week 7-8)

### 4.1 LLM-Based Reverse Inference

#### Step 15: Reverse Inference Validator (`validation/reverse_inference.py`)

```python
"""LLM-based personality inference from dialogue."""

import json
from typing import List, Dict
from clients.llm_client import LLMClient
from utils.models import Turn, PersonalityVector, SessionOutput

INFERENCE_PROMPT = """
You are a personality assessment expert. You will analyze a dialogue transcript 
from a group discussion and infer the personality traits of the candidate.

## Your Task
Based ONLY on the candidate's spoken words and behaviors in this transcript,
estimate their Big Five personality scores on a 1-5 scale:
- Openness (1=conventional, 5=creative)
- Conscientiousness (1=careless, 5=organized)
- Extraversion (1=reserved, 5=outgoing)
- Agreeableness (1=challenging, 5=cooperative)
- Neuroticism (1=calm, 5=anxious)

## Dialogue Transcript
{transcript}

## Instructions
1. Focus on behavioral evidence, not your assumptions
2. Quote specific utterances that support your ratings
3. Be precise - use decimal scores if warranted

## Output Format (JSON only, no other text)
{{
    "Openness": <score>,
    "Conscientiousness": <score>,
    "Extraversion": <score>,
    "Agreeableness": <score>,
    "Neuroticism": <score>,
    "evidence": {{
        "Openness": "<quote or observation>",
        "Conscientiousness": "<quote or observation>",
        "Extraversion": "<quote or observation>",
        "Agreeableness": "<quote or observation>",
        "Neuroticism": "<quote or observation>"
    }}
}}
"""

class ReverseInferenceValidator:
    """Validates personality consistency via reverse inference."""
    
    def __init__(self):
        self.llm_client = LLMClient()
    
    def _build_transcript(self, turns: List[Turn], candidate_name: str) -> str:
        """Build a clean transcript for inference."""
        lines = []
        for turn in turns:
            role = turn.speaker_role.replace("_", " ")
            if role == "Candidate":
                role = candidate_name
            lines.append(f"{role}: {turn.text}")
        return "\n".join(lines)
    
    def infer_personality(
        self,
        session: SessionOutput
    ) -> Dict:
        """Infer personality from session dialogue."""
        transcript = self._build_transcript(
            session.dialogue_log,
            session.candidate_profile.display_name
        )
        
        prompt = INFERENCE_PROMPT.format(transcript=transcript)
        
        response = self.llm_client.generate(
            role="validator",
            system_prompt="You are a personality assessment expert. Respond only with valid JSON.",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Parse JSON response
        try:
            # Clean up response (remove markdown code blocks if present)
            cleaned = response.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("```")[1]
                if cleaned.startswith("json"):
                    cleaned = cleaned[4:]
            result = json.loads(cleaned)
            return result
        except json.JSONDecodeError:
            return {"error": "Failed to parse inference response", "raw": response}
    
    def calculate_consistency(
        self,
        ground_truth: PersonalityVector,
        inferred: Dict
    ) -> Dict:
        """Calculate consistency metrics between ground truth and inferred."""
        if "error" in inferred:
            return {"error": inferred["error"]}
        
        traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]
        
        gt_values = [
            ground_truth.Openness,
            ground_truth.Conscientiousness,
            ground_truth.Extraversion,
            ground_truth.Agreeableness,
            ground_truth.Neuroticism
        ]
        
        inf_values = [inferred.get(t, 3.0) for t in traits]
        
        # Calculate metrics
        differences = [abs(g - i) for g, i in zip(gt_values, inf_values)]
        mae = sum(differences) / len(differences)
        
        # Direction accuracy (high/low classification)
        direction_matches = sum(
            1 for g, i in zip(gt_values, inf_values)
            if (g >= 3.5 and i >= 3.5) or (g < 3.5 and i < 3.5)
        )
        direction_accuracy = direction_matches / len(traits)
        
        # Per-trait analysis
        trait_analysis = {}
        for i, trait in enumerate(traits):
            trait_analysis[trait] = {
                "ground_truth": gt_values[i],
                "inferred": inf_values[i],
                "difference": differences[i],
                "direction_match": (gt_values[i] >= 3.5) == (inf_values[i] >= 3.5)
            }
        
        return {
            "mean_absolute_error": round(mae, 3),
            "direction_accuracy": round(direction_accuracy, 2),
            "trait_analysis": trait_analysis,
            "overall_assessment": "Pass" if mae < 1.0 and direction_accuracy >= 0.6 else "Review"
        }
    
    def validate_session(self, session: SessionOutput) -> Dict:
        """Run full validation on a session."""
        print(f"Validating session: {session.meta_data.session_id}")
        
        # Infer personality
        inferred = self.infer_personality(session)
        
        # Calculate consistency
        consistency = self.calculate_consistency(
            session.candidate_profile.ground_truth_personality,
            inferred
        )
        
        return {
            "session_id": session.meta_data.session_id,
            "ground_truth": session.candidate_profile.ground_truth_personality.model_dump(),
            "inferred_personality": inferred,
            "consistency_metrics": consistency,
            "evidence": inferred.get("evidence", {})
        }
```

### 4.2 Baseline Comparison

#### Step 16: Simple vs BFI Prompting Comparison (`validation/baseline_comparison.py`)

```python
"""Compare BFI-grounded prompting against simple prompting."""

from typing import Dict, List
from scripts.simulation_engine import SimulationEngine
from validation.reverse_inference import ReverseInferenceValidator
from config.personality_profiles import PERSONALITY_PROFILES

# Simple prompt version (for comparison)
SIMPLE_CANDIDATE_PROMPT = """
## Role
You are "{name}", a software engineer in a group discussion.

## Your Personality
You are {simple_description}.

## Scenario
{scenario_context}

## Output Format
[Intent: <intent>]
"Your response"
"""

SIMPLE_DESCRIPTIONS = {
    "defensive_anxious": "anxious and defensive when criticized",
    "aggressive_dominant": "assertive and dominant in discussions",
    "withdrawn_avoidant": "quiet and conflict-avoidant",
    "balanced_leader": "balanced and collaborative",
    # Add others...
}

class BaselineComparator:
    """Compares BFI-grounded vs simple prompting approaches."""
    
    def __init__(self):
        self.validator = ReverseInferenceValidator()
    
    def run_comparison(
        self,
        profile_id: str,
        scenario_id: str,
        n_trials: int = 5
    ) -> Dict:
        """Run multiple trials with both prompting strategies."""
        
        bfi_results = []
        simple_results = []
        
        for trial in range(n_trials):
            print(f"Trial {trial + 1}/{n_trials}")
            
            # Run BFI-grounded simulation
            bfi_engine = SimulationEngine(profile_id, scenario_id)
            bfi_session = bfi_engine.run()
            bfi_validation = self.validator.validate_session(bfi_session)
            bfi_results.append(bfi_validation["consistency_metrics"])
            
            # TODO: Implement simple prompting simulation for comparison
            # This requires modifying the CandidateAgent to use SIMPLE_CANDIDATE_PROMPT
            
        # Aggregate results
        return {
            "profile": profile_id,
            "scenario": scenario_id,
            "n_trials": n_trials,
            "bfi_grounded": {
                "avg_mae": sum(r["mean_absolute_error"] for r in bfi_results) / n_trials,
                "avg_direction_accuracy": sum(r["direction_accuracy"] for r in bfi_results) / n_trials,
                "pass_rate": sum(1 for r in bfi_results if r["overall_assessment"] == "Pass") / n_trials
            },
            # "simple_prompting": {...}  # Add when implemented
        }
```

### 4.3 Human Evaluation Interface

#### Step 17: Human Rating Tool (`validation/human_evaluation.py`)

```python
"""Simple CLI interface for human evaluation of transcripts."""

import json
from pathlib import Path
from typing import Dict, Optional

def load_session(filepath: str) -> Dict:
    """Load a session JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def display_transcript(session: Dict):
    """Display the dialogue for human review."""
    print("\n" + "=" * 60)
    print(f"Session: {session['meta_data']['session_id']}")
    print(f"Scenario: {session['meta_data']['scenario']['title']}")
    print("=" * 60 + "\n")
    
    for turn in session['dialogue_log']:
        role = turn['speaker_role'].replace('_', ' ')
        print(f"[{role}]: {turn['text']}\n")
    
    print("=" * 60)

def collect_ratings() -> Dict[str, float]:
    """Collect personality ratings from human rater."""
    print("\nBased on the candidate's behavior, rate their personality (1-5 scale):")
    print("1 = Very Low, 5 = Very High\n")
    
    traits = {
        "Openness": "creative vs conventional",
        "Conscientiousness": "organized vs careless",
        "Extraversion": "outgoing vs reserved",
        "Agreeableness": "cooperative vs challenging",
        "Neuroticism": "anxious vs calm"
    }
    
    ratings = {}
    for trait, description in traits.items():
        while True:
            try:
                score = float(input(f"  {trait} ({description}): "))
                if 1 <= score <= 5:
                    ratings[trait] = score
                    break
                else:
                    print("    Please enter a value between 1 and 5")
            except ValueError:
                print("    Please enter a valid number")
    
    return ratings

def rate_session(filepath: str, output_dir: str = "./outputs/validation"):
    """Complete rating workflow for a single session."""
    session = load_session(filepath)
    display_transcript(session)
    
    ratings = collect_ratings()
    
    # Calculate agreement with ground truth
    gt = session['candidate_profile']['ground_truth_personality']
    agreement = {}
    for trait, score in ratings.items():
        gt_score = gt[trait]
        diff = abs(score - gt_score)
        agreement[trait] = {
            "human": score,
            "ground_truth": gt_score,
            "difference": round(diff, 2),
            "direction_match": (score >= 3.5) == (gt_score >= 3.5)
        }
    
    result = {
        "session_id": session['meta_data']['session_id'],
        "human_ratings": ratings,
        "agreement_analysis": agreement,
        "overall_mae": round(sum(a["difference"] for a in agreement.values()) / 5, 3)
    }
    
    # Save result
    output_path = Path(output_dir) / f"human_{session['meta_data']['session_id']}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nRating saved to: {output_path}")
    print(f"Mean Absolute Error vs Ground Truth: {result['overall_mae']}")
    
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        rate_session(sys.argv[1])
    else:
        print("Usage: python human_evaluation.py <session_file.json>")
```

---

## Phase 5: Batch Generation & Analysis (Week 9-10)

### 5.1 Batch Generation Script

#### Step 18: Batch Generator (`scripts/generate_batch.py`)

```python
"""Batch generation of simulation sessions."""

import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict
from tqdm import tqdm

from scripts.simulation_engine import run_simulation
from config.personality_profiles import list_profiles
from config.scenarios import list_scenarios

def generate_batch(
    n_per_combination: int = 5,
    output_dir: str = "./outputs/sessions",
    profiles: List[str] = None,
    scenarios: List[str] = None
) -> Dict:
    """Generate a batch of simulations across profile/scenario combinations."""
    
    if profiles is None:
        profiles = list_profiles()
    if scenarios is None:
        scenarios = list_scenarios()
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    batch_id = f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    results = {
        "batch_id": batch_id,
        "generation_date": datetime.now().isoformat(),
        "parameters": {
            "n_per_combination": n_per_combination,
            "profiles": profiles,
            "scenarios": scenarios
        },
        "sessions": [],
        "errors": []
    }
    
    total_combinations = len(profiles) * len(scenarios) * n_per_combination
    
    with tqdm(total=total_combinations, desc="Generating") as pbar:
        for profile_id in profiles:
            for scenario_id in scenarios:
                for trial in range(n_per_combination):
                    try:
                        # Run simulation
                        session = run_simulation(
                            profile_id=profile_id,
                            scenario_id=scenario_id
                        )
                        
                        # Save session
                        session_path = output_path / f"{session.meta_data.session_id}.json"
                        with open(session_path, 'w') as f:
                            json.dump(session.model_dump(), f, indent=2)
                        
                        results["sessions"].append({
                            "session_id": session.meta_data.session_id,
                            "profile": profile_id,
                            "scenario": scenario_id,
                            "turns": session.meta_data.total_turns,
                            "path": str(session_path)
                        })
                        
                    except Exception as e:
                        results["errors"].append({
                            "profile": profile_id,
                            "scenario": scenario_id,
                            "trial": trial,
                            "error": str(e)
                        })
                    
                    pbar.update(1)
    
    # Save batch summary
    summary_path = output_path.parent / "batches" / f"{batch_id}_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    
    results["summary"] = {
        "total_sessions": len(results["sessions"]),
        "total_errors": len(results["errors"]),
        "success_rate": len(results["sessions"]) / total_combinations if total_combinations > 0 else 0
    }
    
    with open(summary_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nBatch complete: {results['summary']['total_sessions']} sessions generated")
    print(f"Summary saved to: {summary_path}")
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate batch of simulations")
    parser.add_argument("--n", type=int, default=5, help="Sessions per profile/scenario combination")
    parser.add_argument("--output", type=str, default="./outputs/sessions", help="Output directory")
    parser.add_argument("--profiles", nargs="*", help="Specific profiles to use")
    parser.add_argument("--scenarios", nargs="*", help="Specific scenarios to use")
    
    args = parser.parse_args()
    
    generate_batch(
        n_per_combination=args.n,
        output_dir=args.output,
        profiles=args.profiles,
        scenarios=args.scenarios
    )
```

### 5.2 Validation Pipeline Script

#### Step 19: Batch Validation (`scripts/run_validation.py`)

```python
"""Run validation pipeline on generated sessions."""

import json
import argparse
from pathlib import Path
from typing import List, Dict
from tqdm import tqdm
import numpy as np

from validation.reverse_inference import ReverseInferenceValidator
from utils.models import SessionOutput

def validate_batch(
    sessions_dir: str = "./outputs/sessions",
    output_dir: str = "./outputs/validation"
) -> Dict:
    """Run validation on all sessions in a directory."""
    
    sessions_path = Path(sessions_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    session_files = list(sessions_path.glob("sim_*.json"))
    
    if not session_files:
        print(f"No session files found in {sessions_dir}")
        return {}
    
    validator = ReverseInferenceValidator()
    results = []
    
    for session_file in tqdm(session_files, desc="Validating"):
        try:
            # Load session
            with open(session_file, 'r') as f:
                session_data = json.load(f)
            session = SessionOutput(**session_data)
            
            # Validate
            validation = validator.validate_session(session)
            results.append(validation)
            
            # Save individual validation result
            val_path = output_path / f"val_{session.meta_data.session_id}.json"
            with open(val_path, 'w') as f:
                json.dump(validation, f, indent=2)
                
        except Exception as e:
            print(f"Error validating {session_file}: {e}")
    
    # Aggregate statistics
    if results:
        maes = [r["consistency_metrics"]["mean_absolute_error"] 
                for r in results if "error" not in r["consistency_metrics"]]
        accuracies = [r["consistency_metrics"]["direction_accuracy"]
                     for r in results if "error" not in r["consistency_metrics"]]
        
        aggregate = {
            "total_sessions": len(results),
            "valid_sessions": len(maes),
            "metrics": {
                "mean_mae": round(np.mean(maes), 3) if maes else None,
                "std_mae": round(np.std(maes), 3) if maes else None,
                "mean_direction_accuracy": round(np.mean(accuracies), 3) if accuracies else None,
                "pass_rate": sum(1 for r in results 
                               if r["consistency_metrics"].get("overall_assessment") == "Pass") / len(results)
            },
            "per_trait_mae": {}
        }
        
        # Per-trait analysis
        traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]
        for trait in traits:
            trait_diffs = [
                r["consistency_metrics"]["trait_analysis"][trait]["difference"]
                for r in results
                if "trait_analysis" in r["consistency_metrics"]
            ]
            if trait_diffs:
                aggregate["per_trait_mae"][trait] = round(np.mean(trait_diffs), 3)
        
        # Save aggregate
        agg_path = output_path / "aggregate_validation.json"
        with open(agg_path, 'w') as f:
            json.dump(aggregate, f, indent=2)
        
        print(f"\nValidation complete:")
        print(f"  Sessions validated: {aggregate['valid_sessions']}/{aggregate['total_sessions']}")
        print(f"  Mean MAE: {aggregate['metrics']['mean_mae']}")
        print(f"  Direction Accuracy: {aggregate['metrics']['mean_direction_accuracy']}")
        print(f"  Pass Rate: {aggregate['metrics']['pass_rate']:.1%}")
        print(f"\nResults saved to: {output_path}")
        
        return aggregate
    
    return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run validation on sessions")
    parser.add_argument("--sessions", type=str, default="./outputs/sessions")
    parser.add_argument("--output", type=str, default="./outputs/validation")
    
    args = parser.parse_args()
    validate_batch(args.sessions, args.output)
```

---

## Phase 6: Testing & Documentation (Week 11-12)

### 6.1 Unit Tests

#### Step 20: Core Tests (`tests/test_core.py`)

```python
"""Unit tests for core components."""

import pytest
from utils.models import PersonalityVector, Turn
from config.personality_profiles import get_profile, list_profiles
from config.bfi_mappings import get_trait_prompts, build_personality_instructions
from config.scenarios import get_scenario, list_scenarios

class TestPersonalityProfiles:
    def test_all_profiles_load(self):
        """Verify all profiles can be loaded."""
        for profile_id in list_profiles():
            profile = get_profile(profile_id)
            assert profile is not None
            assert profile.scores is not None
    
    def test_profile_scores_in_range(self):
        """Verify all scores are 1-5."""
        for profile_id in list_profiles():
            profile = get_profile(profile_id)
            for trait in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]:
                score = getattr(profile.scores, trait)
                assert 1.0 <= score <= 5.0, f"{profile_id}.{trait} = {score}"
    
    def test_profile_has_expected_behaviors(self):
        """Verify all profiles have expected behaviors."""
        for profile_id in list_profiles():
            profile = get_profile(profile_id)
            assert len(profile.expected_behaviors) > 0

class TestBFIMappings:
    def test_all_traits_have_mappings(self):
        """Verify BFI mappings exist for all traits."""
        traits = ["Neuroticism", "Extraversion", "Openness", "Agreeableness", "Conscientiousness"]
        for trait in traits:
            high = get_trait_prompts(trait, 4.5)
            low = get_trait_prompts(trait, 1.5)
            assert len(high) > 0
            assert len(low) > 0
    
    def test_build_instructions(self):
        """Verify instruction building works."""
        vector = PersonalityVector(O=4.5, C=2.0, E=3.0, A=1.5, N=4.5)
        instructions = build_personality_instructions(vector)
        assert len(instructions) > 0
        assert all(isinstance(i, str) for i in instructions)

class TestScenarios:
    def test_all_scenarios_load(self):
        """Verify all scenarios can be loaded."""
        for scenario_id in list_scenarios():
            scenario = get_scenario(scenario_id)
            assert scenario is not None
            assert scenario.setup is not None
    
    def test_scenarios_have_pressure_points(self):
        """Verify all scenarios have pressure points."""
        for scenario_id in list_scenarios():
            scenario = get_scenario(scenario_id)
            assert len(scenario.pressure_points) > 0

class TestModels:
    def test_turn_creation(self):
        """Verify Turn model works."""
        turn = Turn(
            turn_id=1,
            speaker_role="Candidate",
            speaker_id="test_001",
            text="Test response",
            intent_tag="Defense/Justification"
        )
        assert turn.turn_id == 1
        assert turn.timestamp is not None
```

### 6.2 Integration Test

#### Step 21: End-to-End Test (`tests/test_integration.py`)

```python
"""Integration tests for full simulation pipeline."""

import pytest
import json
from pathlib import Path
from scripts.simulation_engine import SimulationEngine, run_simulation
from validation.reverse_inference import ReverseInferenceValidator

class TestSimulationEngine:
    def test_single_simulation_runs(self):
        """Verify a single simulation completes."""
        session = run_simulation(
            profile_id="balanced_leader",
            scenario_id="resource_conflict",
            turn_limit=10  # Shorter for testing
        )
        
        assert session is not None
        assert len(session.dialogue_log) > 0
        assert session.candidate_profile.ground_truth_personality is not None
    
    def test_output_schema_valid(self):
        """Verify output matches expected schema."""
        session = run_simulation(
            profile_id="defensive_anxious",
            scenario_id="crisis_management",
            turn_limit=10
        )
        
        # Convert to dict and verify structure
        data = session.model_dump()
        
        assert "meta_data" in data
        assert "candidate_profile" in data
        assert "dialogue_log" in data
        assert "intent_statistics" in data
        assert "assessment_indicators" in data
        
        # Verify dialogue log structure
        for turn in data["dialogue_log"]:
            assert "turn_id" in turn
            assert "speaker_role" in turn
            assert "text" in turn
            assert "intent_tag" in turn

class TestValidation:
    def test_reverse_inference_runs(self):
        """Verify reverse inference validation works."""
        session = run_simulation(
            profile_id="aggressive_dominant",
            scenario_id="collaborative_deadline",
            turn_limit=10
        )
        
        validator = ReverseInferenceValidator()
        result = validator.validate_session(session)
        
        assert "inferred_personality" in result
        assert "consistency_metrics" in result
    
    def test_consistency_calculation(self):
        """Verify consistency metrics are calculated correctly."""
        from utils.models import PersonalityVector
        
        validator = ReverseInferenceValidator()
        
        gt = PersonalityVector(O=4.0, C=2.0, E=3.0, A=1.5, N=4.5)
        inferred = {"Openness": 4.2, "Conscientiousness": 2.3, "Extraversion": 3.1, 
                   "Agreeableness": 1.8, "Neuroticism": 4.2}
        
        result = validator.calculate_consistency(gt, inferred)
        
        assert "mean_absolute_error" in result
        assert "direction_accuracy" in result
        assert result["mean_absolute_error"] >= 0
        assert 0 <= result["direction_accuracy"] <= 1
```

---

## Summary Timeline

| Week | Phase | Key Deliverables |
|------|-------|-----------------|
| 1-2 | Foundation | Environment, models, configurations |
| 3-4 | Agents | All agent classes, LLM client |
| 5-6 | Engine | Simulation loop, statistics |
| 7-8 | Validation | Reverse inference, human eval tool |
| 9-10 | Batch | Generation scripts, analysis |
| 11-12 | Polish | Tests, documentation, paper prep |

---

## Quick Start Commands

```bash
# 1. Setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Run single simulation
python scripts/generate_single.py --profile balanced_leader --scenario resource_conflict

# 3. Run batch generation (small test)
python scripts/generate_batch.py --n 2 --profiles balanced_leader defensive_anxious

# 4. Run validation
python scripts/run_validation.py

# 5. Human evaluation
python validation/human_evaluation.py outputs/sessions/sim_xxx.json

# 6. Run tests
pytest tests/ -v
```

---

## ENHANCED IMPLEMENTATION DETAILS

The following sections provide in-depth specifications for critical subsystems that require careful design.

---

## A. Conversation Storage Architecture

### A.1 Multi-Layer Storage Strategy

The system uses a three-tier storage architecture to support both real-time simulation and post-hoc analysis.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        STORAGE ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────┐    ┌──────────────────┐    ┌────────────────┐ │
│  │  IN-MEMORY STORE │───▶│  SESSION STORE   │───▶│  ARCHIVE STORE │ │
│  │  (Hot - Runtime) │    │  (Warm - JSON)   │    │  (Cold - SQLite)│ │
│  └──────────────────┘    └──────────────────┘    └────────────────┘ │
│         │                        │                       │          │
│         ▼                        ▼                       ▼          │
│  • Agent histories         • Full session JSON    • Queryable DB    │
│  • Current turn context    • Intent timelines     • Cross-session   │
│  • Response latencies      • Behavior logs        • Analytics       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### A.2 In-Memory Conversation Store (`storage/conversation_store.py`)

```python
"""In-memory conversation management with agent-specific views."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Deque
from collections import deque
from datetime import datetime
import threading

@dataclass
class Message:
    """Single message in the conversation."""
    message_id: str
    timestamp: datetime
    speaker_id: str
    speaker_role: str
    content: str
    intent_tag: Optional[str] = None
    inner_thought: Optional[str] = None
    behavior_notes: List[str] = field(default_factory=list)
    response_latency_ms: Optional[int] = None
    token_count: Optional[int] = None
    raw_llm_response: Optional[str] = None

@dataclass
class ConversationContext:
    """Sliding window context for an agent."""
    messages: Deque[Message]
    max_messages: int = 10
    max_tokens: int = 4000

    def add(self, message: Message):
        self.messages.append(message)
        self._trim_to_limits()

    def _trim_to_limits(self):
        # Remove oldest messages if over count limit
        while len(self.messages) > self.max_messages:
            self.messages.popleft()

        # Remove oldest messages if over token limit
        total_tokens = sum(m.token_count or len(m.content.split()) * 1.3
                          for m in self.messages)
        while total_tokens > self.max_tokens and len(self.messages) > 1:
            self.messages.popleft()
            total_tokens = sum(m.token_count or len(m.content.split()) * 1.3
                              for m in self.messages)

    def to_prompt_format(self, exclude_speaker: Optional[str] = None) -> str:
        """Format context for LLM prompt."""
        lines = []
        for msg in self.messages:
            if exclude_speaker and msg.speaker_id == exclude_speaker:
                continue
            role_label = msg.speaker_role.replace("_", " ")
            lines.append(f"[{role_label}]: {msg.content}")
        return "\n".join(lines)

    def to_anthropic_messages(self, agent_id: str) -> List[Dict]:
        """Convert to Anthropic API message format for a specific agent."""
        messages = []
        for msg in self.messages:
            role = "assistant" if msg.speaker_id == agent_id else "user"
            messages.append({
                "role": role,
                "content": msg.content
            })
        return messages


class ConversationStore:
    """Thread-safe conversation storage with multi-agent support."""

    def __init__(self, session_id: str, context_window: int = 10):
        self.session_id = session_id
        self.context_window = context_window
        self._lock = threading.RLock()

        # Full conversation history
        self._full_history: List[Message] = []

        # Per-agent context windows
        self._agent_contexts: Dict[str, ConversationContext] = {}

        # Message index for quick lookup
        self._message_index: Dict[str, Message] = {}

        # Turn counter
        self._turn_counter = 0

    def register_agent(self, agent_id: str, max_context: int = None):
        """Register an agent with its own context window."""
        with self._lock:
            self._agent_contexts[agent_id] = ConversationContext(
                messages=deque(maxlen=max_context or self.context_window),
                max_messages=max_context or self.context_window
            )

    def add_message(
        self,
        speaker_id: str,
        speaker_role: str,
        content: str,
        intent_tag: Optional[str] = None,
        inner_thought: Optional[str] = None,
        behavior_notes: Optional[List[str]] = None,
        response_latency_ms: Optional[int] = None,
        raw_llm_response: Optional[str] = None
    ) -> Message:
        """Add a message to the conversation."""
        with self._lock:
            self._turn_counter += 1

            message = Message(
                message_id=f"{self.session_id}_msg_{self._turn_counter:04d}",
                timestamp=datetime.utcnow(),
                speaker_id=speaker_id,
                speaker_role=speaker_role,
                content=content,
                intent_tag=intent_tag,
                inner_thought=inner_thought,
                behavior_notes=behavior_notes or [],
                response_latency_ms=response_latency_ms,
                raw_llm_response=raw_llm_response
            )

            # Add to full history
            self._full_history.append(message)
            self._message_index[message.message_id] = message

            # Add to all agent contexts (they all see all messages)
            for context in self._agent_contexts.values():
                context.add(message)

            return message

    def get_context_for_agent(self, agent_id: str) -> ConversationContext:
        """Get the context window for a specific agent."""
        with self._lock:
            return self._agent_contexts.get(agent_id)

    def get_full_history(self) -> List[Message]:
        """Get complete conversation history."""
        with self._lock:
            return self._full_history.copy()

    def get_messages_by_speaker(self, speaker_id: str) -> List[Message]:
        """Get all messages from a specific speaker."""
        with self._lock:
            return [m for m in self._full_history if m.speaker_id == speaker_id]

    def get_candidate_messages(self) -> List[Message]:
        """Get all candidate messages for analysis."""
        with self._lock:
            return [m for m in self._full_history if m.speaker_role == "Candidate"]

    def export_dialogue_log(self) -> List[Dict]:
        """Export full history as list of dicts for JSON serialization."""
        with self._lock:
            return [
                {
                    "turn_id": i + 1,
                    "message_id": m.message_id,
                    "timestamp": m.timestamp.isoformat() + "Z",
                    "speaker_role": m.speaker_role,
                    "speaker_id": m.speaker_id,
                    "text": m.content,
                    "intent_tag": m.intent_tag,
                    "inner_thought": m.inner_thought,
                    "behavior_notes": m.behavior_notes,
                    "response_latency_ms": m.response_latency_ms
                }
                for i, m in enumerate(self._full_history)
            ]
```

### A.3 Session Persistence (`storage/session_store.py`)

```python
"""Session-level persistence with JSON and optional SQLite backend."""

import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import asdict

from storage.conversation_store import ConversationStore, Message

class SessionStore:
    """Persists sessions to JSON with optional SQLite indexing."""

    def __init__(
        self,
        output_dir: str = "./outputs",
        use_sqlite: bool = True,
        db_path: str = "./outputs/sessions.db"
    ):
        self.output_dir = Path(output_dir)
        self.sessions_dir = self.output_dir / "sessions"
        self.sessions_dir.mkdir(parents=True, exist_ok=True)

        self.use_sqlite = use_sqlite
        if use_sqlite:
            self.db_path = Path(db_path)
            self._init_database()

    def _init_database(self):
        """Initialize SQLite schema for session indexing."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                created_at TEXT,
                profile_id TEXT,
                scenario_id TEXT,
                total_turns INTEGER,
                json_path TEXT,
                validation_status TEXT DEFAULT 'pending'
            )
        """)

        # Turns table for queryable analysis
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS turns (
                turn_id INTEGER,
                session_id TEXT,
                timestamp TEXT,
                speaker_role TEXT,
                speaker_id TEXT,
                text TEXT,
                intent_tag TEXT,
                intent_category TEXT,
                intent_subcategory TEXT,
                inner_thought TEXT,
                PRIMARY KEY (session_id, turn_id),
                FOREIGN KEY (session_id) REFERENCES sessions(session_id)
            )
        """)

        # Behavior notes (many-to-one with turns)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS behavior_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                turn_id INTEGER,
                note TEXT,
                note_category TEXT,
                FOREIGN KEY (session_id, turn_id) REFERENCES turns(session_id, turn_id)
            )
        """)

        # Intent timeline for sequence analysis
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS intent_sequences (
                session_id TEXT,
                candidate_intent_sequence TEXT,
                intent_transition_counts TEXT,
                PRIMARY KEY (session_id),
                FOREIGN KEY (session_id) REFERENCES sessions(session_id)
            )
        """)

        # Indexes for common queries
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_turns_session ON turns(session_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_turns_intent ON turns(intent_tag)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_turns_speaker ON turns(speaker_role)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessions_profile ON sessions(profile_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_sessions_scenario ON sessions(scenario_id)")

        conn.commit()
        conn.close()

    def save_session(
        self,
        session_id: str,
        profile_id: str,
        scenario_id: str,
        conversation_store: ConversationStore,
        full_session_data: Dict
    ) -> str:
        """Save session to JSON and optionally index in SQLite."""

        # Save JSON
        json_path = self.sessions_dir / f"{session_id}.json"
        with open(json_path, 'w') as f:
            json.dump(full_session_data, f, indent=2, default=str)

        # Index in SQLite
        if self.use_sqlite:
            self._index_session(
                session_id=session_id,
                profile_id=profile_id,
                scenario_id=scenario_id,
                conversation_store=conversation_store,
                json_path=str(json_path)
            )

        return str(json_path)

    def _index_session(
        self,
        session_id: str,
        profile_id: str,
        scenario_id: str,
        conversation_store: ConversationStore,
        json_path: str
    ):
        """Index session data in SQLite for analysis."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        history = conversation_store.get_full_history()

        # Insert session
        cursor.execute("""
            INSERT OR REPLACE INTO sessions
            (session_id, created_at, profile_id, scenario_id, total_turns, json_path)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (session_id, datetime.utcnow().isoformat(), profile_id,
              scenario_id, len(history), json_path))

        # Insert turns
        candidate_intents = []
        for i, msg in enumerate(history):
            intent_parts = msg.intent_tag.split("/") if msg.intent_tag else ["Unknown", "Unknown"]
            intent_category = intent_parts[0]
            intent_subcategory = intent_parts[1] if len(intent_parts) > 1 else "General"

            cursor.execute("""
                INSERT OR REPLACE INTO turns
                (turn_id, session_id, timestamp, speaker_role, speaker_id,
                 text, intent_tag, intent_category, intent_subcategory, inner_thought)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (i + 1, session_id, msg.timestamp.isoformat(), msg.speaker_role,
                  msg.speaker_id, msg.content, msg.intent_tag, intent_category,
                  intent_subcategory, msg.inner_thought))

            # Insert behavior notes
            for note in msg.behavior_notes:
                note_category = self._categorize_behavior_note(note)
                cursor.execute("""
                    INSERT INTO behavior_notes (session_id, turn_id, note, note_category)
                    VALUES (?, ?, ?, ?)
                """, (session_id, i + 1, note, note_category))

            if msg.speaker_role == "Candidate":
                candidate_intents.append(msg.intent_tag)

        # Store intent sequence for the candidate
        intent_sequence = " -> ".join(candidate_intents)
        transition_counts = self._count_intent_transitions(candidate_intents)

        cursor.execute("""
            INSERT OR REPLACE INTO intent_sequences
            (session_id, candidate_intent_sequence, intent_transition_counts)
            VALUES (?, ?, ?)
        """, (session_id, intent_sequence, json.dumps(transition_counts)))

        conn.commit()
        conn.close()

    def _categorize_behavior_note(self, note: str) -> str:
        """Categorize behavior note for filtering."""
        categories = {
            "emotional": ["anxiety", "frustration", "emotional", "distress"],
            "defensive": ["defensive", "blame", "deflect", "justify"],
            "linguistic": ["hesitation", "markers", "tone"],
            "social": ["conciliatory", "aggressive", "collaborative"]
        }
        note_lower = note.lower()
        for category, keywords in categories.items():
            if any(kw in note_lower for kw in keywords):
                return category
        return "other"

    def _count_intent_transitions(self, intents: List[str]) -> Dict[str, int]:
        """Count intent transitions for Markov analysis."""
        transitions = {}
        for i in range(len(intents) - 1):
            key = f"{intents[i]} -> {intents[i+1]}"
            transitions[key] = transitions.get(key, 0) + 1
        return transitions

    def query_sessions_by_profile(self, profile_id: str) -> List[Dict]:
        """Query all sessions for a specific personality profile."""
        if not self.use_sqlite:
            raise ValueError("SQLite not enabled")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT session_id, scenario_id, total_turns, json_path, validation_status
            FROM sessions WHERE profile_id = ?
        """, (profile_id,))

        results = [
            {"session_id": r[0], "scenario_id": r[1], "total_turns": r[2],
             "json_path": r[3], "validation_status": r[4]}
            for r in cursor.fetchall()
        ]
        conn.close()
        return results

    def query_intent_distribution(self, profile_id: Optional[str] = None) -> Dict[str, int]:
        """Get intent distribution across sessions."""
        if not self.use_sqlite:
            raise ValueError("SQLite not enabled")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if profile_id:
            cursor.execute("""
                SELECT t.intent_tag, COUNT(*)
                FROM turns t
                JOIN sessions s ON t.session_id = s.session_id
                WHERE t.speaker_role = 'Candidate' AND s.profile_id = ?
                GROUP BY t.intent_tag
                ORDER BY COUNT(*) DESC
            """, (profile_id,))
        else:
            cursor.execute("""
                SELECT intent_tag, COUNT(*)
                FROM turns
                WHERE speaker_role = 'Candidate'
                GROUP BY intent_tag
                ORDER BY COUNT(*) DESC
            """)

        results = {r[0]: r[1] for r in cursor.fetchall()}
        conn.close()
        return results
```

---

## B. Intent and Behavior Tagging System

### B.1 Comprehensive Intent Taxonomy (`pipeline/intent_taxonomy.py`)

```python
"""Enhanced intent taxonomy with hierarchical structure and validation."""

from enum import Enum
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import re

class IntentCategory(Enum):
    """Top-level intent categories."""
    COLLABORATION = "Collaboration"
    DEFENSE = "Defense"
    BLAME_SHIFTING = "Blame_Shifting"
    ATTACK = "Attack"
    WITHDRAWAL = "Withdrawal"
    ASSERTION = "Assertion"
    CONCESSION = "Concession"
    CLARIFICATION = "Clarification"
    EMOTIONAL = "Emotional"
    PROCESS = "Process"


@dataclass
class IntentDefinition:
    """Full definition of an intent with examples and traits."""
    category: IntentCategory
    subcategory: str
    description: str
    examples: List[str]
    associated_traits: Dict[str, str]  # trait -> high/low
    assessment_impact: Dict[str, str]  # dimension -> +/-/neutral
    linguistic_markers: List[str]


# Complete intent definitions
INTENT_DEFINITIONS: Dict[str, IntentDefinition] = {
    "Collaboration/Proposal": IntentDefinition(
        category=IntentCategory.COLLABORATION,
        subcategory="Proposal",
        description="Suggesting a concrete solution, action, or approach",
        examples=[
            "What if we split the budget cuts across all components proportionally?",
            "I suggest we focus on the critical path items first.",
            "Let me propose a phased approach where we..."
        ],
        associated_traits={"E": "high", "O": "high", "A": "high"},
        assessment_impact={"Communication": "+", "Influencing": "+", "Problem_Solving": "+"},
        linguistic_markers=["suggest", "propose", "what if", "how about", "we could", "let's try"]
    ),

    "Collaboration/Agreement": IntentDefinition(
        category=IntentCategory.COLLABORATION,
        subcategory="Agreement",
        description="Expressing support or alignment with another's position",
        examples=[
            "That's a good point, I agree we should prioritize that.",
            "You're right about the timeline constraints.",
            "I can support that approach."
        ],
        associated_traits={"A": "high"},
        assessment_impact={"Collaboration": "+", "Communication": "+"},
        linguistic_markers=["agree", "good point", "you're right", "I support", "makes sense"]
    ),

    "Collaboration/Compromise": IntentDefinition(
        category=IntentCategory.COLLABORATION,
        subcategory="Compromise",
        description="Offering middle ground between conflicting positions",
        examples=[
            "Maybe we can meet halfway - I'll reduce scope if you extend the deadline.",
            "I'm willing to cut some features if we protect the core.",
            "What if we both give up something?"
        ],
        associated_traits={"A": "high", "O": "moderate"},
        assessment_impact={"Influencing": "+", "Collaboration": "+", "Problem_Solving": "+"},
        linguistic_markers=["middle ground", "halfway", "willing to", "if you", "both"]
    ),

    "Defense/Justification": IntentDefinition(
        category=IntentCategory.DEFENSE,
        subcategory="Justification",
        description="Providing reasons, evidence, or logical arguments for one's position",
        examples=[
            "The delays were documented in the sprint retrospectives.",
            "If you look at the commit history, the changes were reviewed and approved.",
            "The technical debt was a known trade-off we agreed to."
        ],
        associated_traits={"C": "high"},
        assessment_impact={"Communication": "neutral", "Confidence": "+"},
        linguistic_markers=["because", "the reason", "evidence shows", "documented", "if you look"]
    ),

    "Defense/Deflection": IntentDefinition(
        category=IntentCategory.DEFENSE,
        subcategory="Deflection",
        description="Redirecting criticism without substantively addressing it",
        examples=[
            "That's not really the point here.",
            "We should focus on the solution, not the blame.",
            "Let's not get into that right now."
        ],
        associated_traits={"A": "low", "N": "high"},
        assessment_impact={"Communication": "-", "Integrity": "-"},
        linguistic_markers=["not the point", "let's focus on", "not get into", "moving on"]
    ),

    "Blame_Shifting/External": IntentDefinition(
        category=IntentCategory.BLAME_SHIFTING,
        subcategory="External",
        description="Attributing fault to external circumstances or systems",
        examples=[
            "The requirements kept changing, that's why we're behind.",
            "The infrastructure issues caused the delays.",
            "We didn't have the resources we were promised."
        ],
        associated_traits={"C": "low", "N": "high"},
        assessment_impact={"Integrity": "-", "Problem_Solving": "-"},
        linguistic_markers=["because of", "due to", "wasn't given", "kept changing", "out of control"]
    ),

    "Blame_Shifting/Colleague": IntentDefinition(
        category=IntentCategory.BLAME_SHIFTING,
        subcategory="Colleague",
        description="Attributing fault to a specific colleague or team",
        examples=[
            "QA kept changing the test parameters.",
            "If their component was ready, we wouldn't be in this situation.",
            "They were supposed to handle that integration."
        ],
        associated_traits={"A": "low", "C": "low"},
        assessment_impact={"Collaboration": "-", "Integrity": "-", "Communication": "-"},
        linguistic_markers=["they", "their fault", "supposed to", "didn't do", "if they had"]
    ),

    "Attack/Criticism": IntentDefinition(
        category=IntentCategory.ATTACK,
        subcategory="Criticism",
        description="Critiquing ideas, work output, or decisions",
        examples=[
            "That approach has obvious flaws.",
            "The implementation was poorly designed from the start.",
            "That's not going to work and here's why."
        ],
        associated_traits={"A": "low", "E": "high"},
        assessment_impact={"Communication": "-", "Collaboration": "-"},
        linguistic_markers=["flaws", "poorly", "won't work", "bad idea", "obvious problems"]
    ),

    "Attack/Personal": IntentDefinition(
        category=IntentCategory.ATTACK,
        subcategory="Personal",
        description="Critiquing a person's character, competence, or reliability",
        examples=[
            "You always do this - overpromise and underdeliver.",
            "Maybe if you were better at time management...",
            "That's typical of your work quality."
        ],
        associated_traits={"A": "low", "N": "low"},
        assessment_impact={"Communication": "-", "Collaboration": "-", "Professionalism": "-"},
        linguistic_markers=["you always", "typical", "your problem", "if you were", "never"]
    ),

    "Withdrawal/Avoidance": IntentDefinition(
        category=IntentCategory.WITHDRAWAL,
        subcategory="Avoidance",
        description="Steering away from conflict or difficult topics",
        examples=[
            "I don't want to get into that argument.",
            "Let's just move on.",
            "Whatever you decide is fine."
        ],
        associated_traits={"E": "low", "N": "high", "A": "high"},
        assessment_impact={"Influencing": "-", "Confidence": "-"},
        linguistic_markers=["don't want to", "let's just", "whatever", "move on", "fine with me"]
    ),

    "Withdrawal/Silence_Cue": IntentDefinition(
        category=IntentCategory.WITHDRAWAL,
        subcategory="Silence_Cue",
        description="Indicating unwillingness or inability to continue engaging",
        examples=[
            "I... I don't know what to say.",
            "...",
            "Fine. Whatever."
        ],
        associated_traits={"E": "low", "N": "high"},
        assessment_impact={"Communication": "-", "Confidence": "-"},
        linguistic_markers=["...", "don't know", "fine", "whatever", "I guess"]
    ),

    "Assertion/Confident": IntentDefinition(
        category=IntentCategory.ASSERTION,
        subcategory="Confident",
        description="Stating position with clear conviction",
        examples=[
            "I'm confident this is the right approach.",
            "Here's what we need to do.",
            "I've analyzed this thoroughly and my recommendation is clear."
        ],
        associated_traits={"E": "high", "N": "low"},
        assessment_impact={"Influencing": "+", "Communication": "+", "Confidence": "+"},
        linguistic_markers=["confident", "clearly", "definitely", "must", "will"]
    ),

    "Assertion/Aggressive": IntentDefinition(
        category=IntentCategory.ASSERTION,
        subcategory="Aggressive",
        description="Dominating conversation forcefully, interrupting",
        examples=[
            "No, stop. You're wrong.",
            "I don't care what you think, this is how it is.",
            "Listen to me - "
        ],
        associated_traits={"E": "high", "A": "low"},
        assessment_impact={"Influencing": "neutral", "Collaboration": "-", "Professionalism": "-"},
        linguistic_markers=["stop", "wrong", "don't care", "listen", "no"]
    ),

    "Emotional/Anxiety": IntentDefinition(
        category=IntentCategory.EMOTIONAL,
        subcategory="Anxiety",
        description="Expressing worry, uncertainty, or nervous distress",
        examples=[
            "I'm really worried about how this will affect my review.",
            "This is making me nervous - what if we can't fix it?",
            "I don't know if I can handle this pressure."
        ],
        associated_traits={"N": "high"},
        assessment_impact={"Resilience": "-"},
        linguistic_markers=["worried", "nervous", "anxious", "scared", "don't know if"]
    ),

    "Emotional/Frustration": IntentDefinition(
        category=IntentCategory.EMOTIONAL,
        subcategory="Frustration",
        description="Expressing irritation, exasperation, or anger",
        examples=[
            "This is ridiculous! We've been over this.",
            "I can't believe we're still arguing about this.",
            "Why does this keep happening?"
        ],
        associated_traits={"N": "high", "A": "low"},
        assessment_impact={"Resilience": "-", "Communication": "-"},
        linguistic_markers=["ridiculous", "can't believe", "frustrated", "why", "again"]
    ),

    "Emotional/Enthusiasm": IntentDefinition(
        category=IntentCategory.EMOTIONAL,
        subcategory="Enthusiasm",
        description="Expressing positive engagement and energy",
        examples=[
            "I'm excited about this approach!",
            "This could really work - let me show you.",
            "I love the direction we're heading."
        ],
        associated_traits={"E": "high", "N": "low"},
        assessment_impact={"Communication": "+", "Collaboration": "+"},
        linguistic_markers=["excited", "love", "great", "awesome", "can't wait"]
    ),

    "Concession/Yielding": IntentDefinition(
        category=IntentCategory.CONCESSION,
        subcategory="Yielding",
        description="Giving up position without clear strategic reason",
        examples=[
            "Fine, we'll do it your way.",
            "I give up - you win.",
            "Whatever, I don't care anymore."
        ],
        associated_traits={"A": "high", "E": "low", "N": "high"},
        assessment_impact={"Influencing": "-", "Confidence": "-"},
        linguistic_markers=["fine", "give up", "your way", "don't care", "whatever"]
    ),

    "Concession/Strategic": IntentDefinition(
        category=IntentCategory.CONCESSION,
        subcategory="Strategic",
        description="Making tactical compromise for larger gain",
        examples=[
            "I'll concede on the timeline if we protect the core features.",
            "Let me give you this point so we can move forward on the bigger issue.",
            "Fair enough - I'll drop that requirement to make this work."
        ],
        associated_traits={"O": "high", "C": "high"},
        assessment_impact={"Influencing": "+", "Problem_Solving": "+"},
        linguistic_markers=["concede", "in exchange", "if we can", "trade", "fair enough"]
    ),

    "Clarification/Seeking": IntentDefinition(
        category=IntentCategory.CLARIFICATION,
        subcategory="Seeking",
        description="Asking for more information or explanation",
        examples=[
            "Can you clarify what you mean by 'critical path'?",
            "I'm not sure I understand - are you saying we should...?",
            "What exactly is the constraint here?"
        ],
        associated_traits={"O": "high", "C": "high"},
        assessment_impact={"Communication": "+"},
        linguistic_markers=["clarify", "what do you mean", "not sure I understand", "explain"]
    ),

    "Clarification/Providing": IntentDefinition(
        category=IntentCategory.CLARIFICATION,
        subcategory="Providing",
        description="Explaining or elaborating on a point",
        examples=[
            "Let me explain what I meant...",
            "To clarify, the issue is specifically about...",
            "What I'm saying is..."
        ],
        associated_traits={"E": "moderate", "C": "high"},
        assessment_impact={"Communication": "+"},
        linguistic_markers=["let me explain", "to clarify", "what I mean", "specifically"]
    )
}

# Valid intent tags for validation
VALID_INTENT_TAGS = set(INTENT_DEFINITIONS.keys())


class IntentTagger:
    """Validates and enriches intent tags from LLM output."""

    def __init__(self):
        self.definitions = INTENT_DEFINITIONS
        self.valid_tags = VALID_INTENT_TAGS

    def validate_intent(self, intent_tag: str) -> Tuple[bool, str]:
        """Validate an intent tag, returning (is_valid, normalized_tag)."""
        if not intent_tag:
            return False, "Unknown/Unparsed"

        # Exact match
        if intent_tag in self.valid_tags:
            return True, intent_tag

        # Case-insensitive match
        tag_lower = intent_tag.lower()
        for valid in self.valid_tags:
            if valid.lower() == tag_lower:
                return True, valid

        # Partial match (category only)
        parts = intent_tag.split("/")
        if len(parts) >= 1:
            category = parts[0]
            for valid in self.valid_tags:
                if valid.startswith(category + "/"):
                    # Return first match in category
                    return True, valid

        return False, "Unknown/Unparsed"

    def infer_intent_from_text(self, text: str, thought: Optional[str] = None) -> str:
        """Fallback: infer intent from text using linguistic markers."""
        text_lower = text.lower()
        thought_lower = (thought or "").lower()
        combined = text_lower + " " + thought_lower

        scores = {}
        for tag, definition in self.definitions.items():
            score = sum(1 for marker in definition.linguistic_markers if marker in combined)
            if score > 0:
                scores[tag] = score

        if scores:
            return max(scores, key=scores.get)

        return "Unknown/Unparsed"

    def get_definition(self, intent_tag: str) -> Optional[IntentDefinition]:
        """Get full definition for an intent tag."""
        return self.definitions.get(intent_tag)

    def get_trait_associations(self, intent_tag: str) -> Dict[str, str]:
        """Get trait associations for an intent."""
        defn = self.get_definition(intent_tag)
        return defn.associated_traits if defn else {}
```

### B.2 Behavior Note Extractor (`pipeline/behavior_extractor.py`)

```python
"""Enhanced behavior extraction with categorization and confidence."""

from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import re
from enum import Enum

class BehaviorCategory(Enum):
    LINGUISTIC = "linguistic"
    EMOTIONAL = "emotional"
    SOCIAL = "social"
    COGNITIVE = "cognitive"
    DEFENSIVE = "defensive"


@dataclass
class BehaviorNote:
    """Structured behavior observation."""
    note_id: str
    category: BehaviorCategory
    label: str
    description: str
    evidence: str
    confidence: float  # 0-1
    trait_implications: Dict[str, str]  # trait -> high/low indicator


class BehaviorExtractor:
    """Extracts behavioral indicators from agent responses."""

    def __init__(self):
        self.patterns = self._build_patterns()

    def _build_patterns(self) -> Dict[str, Dict]:
        """Build regex patterns for behavior detection."""
        return {
            # Linguistic behaviors
            "hesitation_markers": {
                "pattern": r'\.{3}|(?:^|\s)(um|uh|well|I mean|you know|like|sort of)(?:\s|$|,)',
                "category": BehaviorCategory.LINGUISTIC,
                "description": "Speech disfluencies indicating uncertainty",
                "confidence_base": 0.7,
                "traits": {"N": "high", "E": "low"}
            },
            "hedge_words": {
                "pattern": r'\b(maybe|perhaps|might|could be|I think|I guess|probably|possibly)\b',
                "category": BehaviorCategory.LINGUISTIC,
                "description": "Hedging language reducing commitment to statements",
                "confidence_base": 0.6,
                "traits": {"E": "low", "N": "high"}
            },
            "absolute_language": {
                "pattern": r'\b(always|never|absolutely|definitely|certainly|must|impossible)\b',
                "category": BehaviorCategory.LINGUISTIC,
                "description": "Strong absolute terms indicating conviction or rigidity",
                "confidence_base": 0.7,
                "traits": {"O": "low", "E": "high"}
            },
            "first_person_focus": {
                "pattern": r'\b(I|me|my|mine)\b',
                "category": BehaviorCategory.LINGUISTIC,
                "description": "High first-person pronoun usage (count-based)",
                "confidence_base": 0.5,
                "traits": {"E": "high"},
                "count_threshold": 5
            },

            # Emotional behaviors
            "anxiety_expression": {
                "pattern": r'\b(worried|anxious|nervous|scared|afraid|stressed|overwhelmed|panicking)\b',
                "category": BehaviorCategory.EMOTIONAL,
                "description": "Direct expression of anxiety or worry",
                "confidence_base": 0.9,
                "traits": {"N": "high"}
            },
            "frustration_expression": {
                "pattern": r'\b(frustrated|annoyed|irritated|angry|furious|upset|ridiculous|absurd)\b',
                "category": BehaviorCategory.EMOTIONAL,
                "description": "Direct expression of frustration or anger",
                "confidence_base": 0.9,
                "traits": {"N": "high", "A": "low"}
            },
            "enthusiasm_expression": {
                "pattern": r'\b(excited|thrilled|love|great|awesome|fantastic|amazing)\b',
                "category": BehaviorCategory.EMOTIONAL,
                "description": "Positive emotional expression",
                "confidence_base": 0.8,
                "traits": {"E": "high", "N": "low"}
            },

            # Social behaviors
            "blame_attribution": {
                "pattern": r'\b(their fault|they did|they didn\'t|blame them|because (of )?they|if they had)\b',
                "category": BehaviorCategory.SOCIAL,
                "description": "Attributing blame to others",
                "confidence_base": 0.85,
                "traits": {"A": "low", "C": "low"}
            },
            "validation_seeking": {
                "pattern": r'\b(right\?|don\'t you think|you agree|isn\'t it|wouldn\'t you say)\b',
                "category": BehaviorCategory.SOCIAL,
                "description": "Seeking validation or agreement from others",
                "confidence_base": 0.7,
                "traits": {"N": "high", "E": "moderate"}
            },
            "inclusive_language": {
                "pattern": r'\b(we|us|our|together|team|let\'s)\b',
                "category": BehaviorCategory.SOCIAL,
                "description": "Using inclusive pronouns (count-based)",
                "confidence_base": 0.6,
                "traits": {"A": "high", "E": "high"},
                "count_threshold": 3
            },

            # Defensive behaviors
            "deflection_attempt": {
                "pattern": r'\b(not the point|beside the point|let\'s focus on|moving on|anyway)\b',
                "category": BehaviorCategory.DEFENSIVE,
                "description": "Attempting to redirect or deflect criticism",
                "confidence_base": 0.8,
                "traits": {"A": "low"}
            },
            "justification_chain": {
                "pattern": r'\b(because|the reason|due to|since|given that)\b.*\b(because|the reason|due to|since)\b',
                "category": BehaviorCategory.DEFENSIVE,
                "description": "Multiple justifications in sequence",
                "confidence_base": 0.7,
                "traits": {"N": "high", "C": "moderate"}
            },
            "denial_markers": {
                "pattern": r'\b(not my|wasn\'t my|didn\'t do|never said|that\'s not what)\b',
                "category": BehaviorCategory.DEFENSIVE,
                "description": "Direct denial of responsibility or statements",
                "confidence_base": 0.85,
                "traits": {"A": "low", "N": "high"}
            },

            # Cognitive behaviors
            "analytical_framing": {
                "pattern": r'\b(analyze|consider|evaluate|weigh|assess|factor|variable|data)\b',
                "category": BehaviorCategory.COGNITIVE,
                "description": "Using analytical or systematic language",
                "confidence_base": 0.7,
                "traits": {"O": "high", "C": "high"}
            },
            "creative_proposal": {
                "pattern": r'\b(what if|imagine|alternatively|novel|innovative|creative|new approach)\b',
                "category": BehaviorCategory.COGNITIVE,
                "description": "Proposing creative or alternative solutions",
                "confidence_base": 0.75,
                "traits": {"O": "high"}
            },
            "procedural_focus": {
                "pattern": r'\b(process|procedure|step|protocol|guideline|standard|proper way)\b',
                "category": BehaviorCategory.COGNITIVE,
                "description": "Focus on procedures and proper methods",
                "confidence_base": 0.7,
                "traits": {"C": "high", "O": "low"}
            }
        }

    def extract_behaviors(
        self,
        text: str,
        inner_thought: Optional[str] = None
    ) -> List[BehaviorNote]:
        """Extract all behavioral indicators from text and thought."""
        behaviors = []
        combined_text = f"{text} {inner_thought or ''}"

        for behavior_id, config in self.patterns.items():
            pattern = config["pattern"]
            matches = re.findall(pattern, combined_text, re.IGNORECASE)

            if matches:
                # Handle count-based behaviors
                if "count_threshold" in config:
                    if len(matches) < config["count_threshold"]:
                        continue

                # Calculate confidence based on match count and base
                confidence = min(config["confidence_base"] + (len(matches) - 1) * 0.05, 1.0)

                # Find evidence (first few matches)
                evidence_matches = matches[:3] if isinstance(matches[0], str) else [m[0] for m in matches[:3]]
                evidence = f"Found: {', '.join(evidence_matches)}"

                behaviors.append(BehaviorNote(
                    note_id=f"beh_{behavior_id}",
                    category=config["category"],
                    label=behavior_id,
                    description=config["description"],
                    evidence=evidence,
                    confidence=confidence,
                    trait_implications=config["traits"]
                ))

        return behaviors

    def aggregate_trait_signals(
        self,
        behaviors: List[BehaviorNote]
    ) -> Dict[str, Dict[str, float]]:
        """Aggregate trait signals from multiple behaviors."""
        trait_signals = {
            "O": {"high": 0, "low": 0, "count": 0},
            "C": {"high": 0, "low": 0, "count": 0},
            "E": {"high": 0, "low": 0, "count": 0},
            "A": {"high": 0, "low": 0, "count": 0},
            "N": {"high": 0, "low": 0, "count": 0}
        }

        for behavior in behaviors:
            for trait, level in behavior.trait_implications.items():
                if trait in trait_signals and level in ["high", "low"]:
                    trait_signals[trait][level] += behavior.confidence
                    trait_signals[trait]["count"] += 1

        # Normalize to probabilities
        result = {}
        for trait, signals in trait_signals.items():
            if signals["count"] > 0:
                total = signals["high"] + signals["low"]
                if total > 0:
                    result[trait] = {
                        "high_probability": signals["high"] / total,
                        "low_probability": signals["low"] / total,
                        "signal_count": signals["count"],
                        "total_weight": total
                    }

        return result
```

---

## C. Personality Judgment System

### C.1 Multi-Method Personality Assessment (`validation/personality_judge.py`)

```python
"""Comprehensive personality assessment combining multiple methods."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum
import numpy as np
from collections import Counter

from pipeline.intent_taxonomy import IntentTagger, INTENT_DEFINITIONS
from pipeline.behavior_extractor import BehaviorExtractor, BehaviorNote
from storage.conversation_store import Message


class AssessmentMethod(Enum):
    INTENT_ANALYSIS = "intent_analysis"
    BEHAVIOR_EXTRACTION = "behavior_extraction"
    LLM_INFERENCE = "llm_inference"
    LINGUISTIC_FEATURES = "linguistic_features"
    ENSEMBLE = "ensemble"


@dataclass
class TraitAssessment:
    """Assessment result for a single trait."""
    trait: str
    score: float  # 1-5 scale
    confidence: float  # 0-1
    evidence: List[str]
    method_scores: Dict[str, float]  # method -> score


@dataclass
class PersonalityAssessment:
    """Complete personality assessment result."""
    session_id: str
    method: AssessmentMethod
    traits: Dict[str, TraitAssessment]
    overall_confidence: float
    consistency_flags: List[str]
    raw_features: Dict


class PersonalityJudge:
    """Multi-method personality assessment engine."""

    def __init__(self, llm_client=None):
        self.intent_tagger = IntentTagger()
        self.behavior_extractor = BehaviorExtractor()
        self.llm_client = llm_client

        # Trait mapping from intents (accumulated across conversation)
        self.intent_trait_weights = self._build_intent_trait_weights()

    def _build_intent_trait_weights(self) -> Dict[str, Dict[str, float]]:
        """Build weight matrix from intent definitions."""
        weights = {}
        for intent_tag, defn in INTENT_DEFINITIONS.items():
            weights[intent_tag] = {}
            for trait, level in defn.associated_traits.items():
                # Convert high/low/moderate to numeric weights
                if level == "high":
                    weights[intent_tag][trait] = 1.0
                elif level == "low":
                    weights[intent_tag][trait] = -1.0
                elif level == "moderate":
                    weights[intent_tag][trait] = 0.0
        return weights

    def assess_from_intents(
        self,
        messages: List[Message]
    ) -> Dict[str, TraitAssessment]:
        """Assess personality from intent distribution."""
        # Count candidate intents
        candidate_msgs = [m for m in messages if m.speaker_role == "Candidate"]
        intent_counts = Counter(m.intent_tag for m in candidate_msgs)
        total_intents = sum(intent_counts.values())

        if total_intents == 0:
            return self._default_assessment()

        # Accumulate trait signals
        trait_scores = {t: [] for t in ["O", "C", "E", "A", "N"]}
        trait_evidence = {t: [] for t in ["O", "C", "E", "A", "N"]}

        for intent, count in intent_counts.items():
            if intent in self.intent_trait_weights:
                weight_factor = count / total_intents
                for trait, weight in self.intent_trait_weights[intent].items():
                    # Convert weight to score contribution
                    score_contrib = 3.0 + (weight * 1.5)  # Maps -1..1 to 1.5..4.5
                    trait_scores[trait].append((score_contrib, weight_factor))
                    if weight != 0:
                        direction = "high" if weight > 0 else "low"
                        trait_evidence[trait].append(
                            f"{intent} ({count}x) -> {direction} {trait}"
                        )

        # Calculate weighted averages
        assessments = {}
        for trait in ["O", "C", "E", "A", "N"]:
            if trait_scores[trait]:
                scores, weights = zip(*trait_scores[trait])
                weighted_score = np.average(scores, weights=weights)
                confidence = min(sum(weights), 1.0)  # More evidence = higher confidence
            else:
                weighted_score = 3.0
                confidence = 0.1

            assessments[trait] = TraitAssessment(
                trait=trait,
                score=round(weighted_score, 2),
                confidence=round(confidence, 2),
                evidence=trait_evidence[trait][:5],
                method_scores={"intent_analysis": weighted_score}
            )

        return assessments

    def assess_from_behaviors(
        self,
        messages: List[Message]
    ) -> Dict[str, TraitAssessment]:
        """Assess personality from extracted behaviors."""
        candidate_msgs = [m for m in messages if m.speaker_role == "Candidate"]

        # Collect all behaviors across messages
        all_behaviors = []
        for msg in candidate_msgs:
            behaviors = self.behavior_extractor.extract_behaviors(
                msg.content, msg.inner_thought
            )
            all_behaviors.extend(behaviors)

        # Aggregate trait signals
        aggregated = self.behavior_extractor.aggregate_trait_signals(all_behaviors)

        assessments = {}
        for trait in ["O", "C", "E", "A", "N"]:
            if trait in aggregated:
                sig = aggregated[trait]
                # Convert probability to score
                high_prob = sig["high_probability"]
                score = 1.5 + (high_prob * 3.0)  # Maps 0..1 to 1.5..4.5
                confidence = min(sig["total_weight"] / 5.0, 1.0)
            else:
                score = 3.0
                confidence = 0.1

            # Collect evidence
            evidence = [
                f"{b.label}: {b.description}"
                for b in all_behaviors
                if trait in b.trait_implications
            ][:5]

            assessments[trait] = TraitAssessment(
                trait=trait,
                score=round(score, 2),
                confidence=round(confidence, 2),
                evidence=evidence,
                method_scores={"behavior_extraction": score}
            )

        return assessments

    def assess_from_linguistic_features(
        self,
        messages: List[Message]
    ) -> Dict[str, TraitAssessment]:
        """Assess personality from linguistic feature analysis."""
        candidate_msgs = [m for m in messages if m.speaker_role == "Candidate"]
        all_text = " ".join(m.content for m in candidate_msgs)
        word_count = len(all_text.split())

        if word_count == 0:
            return self._default_assessment()

        # Feature extraction
        features = {
            # Extraversion features
            "words_per_turn": word_count / max(len(candidate_msgs), 1),
            "exclamation_ratio": all_text.count("!") / max(word_count, 1),
            "question_ratio": all_text.count("?") / max(word_count, 1),

            # Neuroticism features
            "hedge_count": len(re.findall(r'\b(maybe|perhaps|might|could)\b', all_text, re.I)),
            "negation_count": len(re.findall(r'\b(not|no|never|cannot|won\'t)\b', all_text, re.I)),

            # Agreeableness features
            "positive_emotion_count": len(re.findall(r'\b(agree|support|help|thank|appreciate)\b', all_text, re.I)),
            "negative_social_count": len(re.findall(r'\b(blame|fault|wrong|stupid)\b', all_text, re.I)),

            # Conscientiousness features
            "detail_words": len(re.findall(r'\b(specifically|exactly|precisely|carefully)\b', all_text, re.I)),
            "planning_words": len(re.findall(r'\b(plan|schedule|organize|step|first|then)\b', all_text, re.I)),

            # Openness features
            "creative_words": len(re.findall(r'\b(imagine|create|idea|novel|alternative)\b', all_text, re.I)),
            "abstract_words": len(re.findall(r'\b(concept|theory|principle|philosophy)\b', all_text, re.I))
        }

        # Normalize by word count
        for key in features:
            if "ratio" not in key and "per_turn" not in key:
                features[key] = features[key] / max(word_count / 100, 1)

        # Map features to trait scores
        assessments = {}

        # Extraversion
        e_score = 3.0 + (features["words_per_turn"] - 20) / 20 + features["exclamation_ratio"] * 10
        assessments["E"] = TraitAssessment(
            trait="E", score=np.clip(e_score, 1.0, 5.0),
            confidence=0.5, evidence=[f"Avg {features['words_per_turn']:.0f} words/turn"],
            method_scores={"linguistic_features": e_score}
        )

        # Neuroticism
        n_score = 3.0 + features["hedge_count"] * 0.3 + features["negation_count"] * 0.2
        assessments["N"] = TraitAssessment(
            trait="N", score=np.clip(n_score, 1.0, 5.0),
            confidence=0.5, evidence=[f"Hedge words: {features['hedge_count']:.1f}/100w"],
            method_scores={"linguistic_features": n_score}
        )

        # Agreeableness
        a_score = 3.0 + features["positive_emotion_count"] * 0.4 - features["negative_social_count"] * 0.5
        assessments["A"] = TraitAssessment(
            trait="A", score=np.clip(a_score, 1.0, 5.0),
            confidence=0.5, evidence=[f"Positive social: {features['positive_emotion_count']:.1f}/100w"],
            method_scores={"linguistic_features": a_score}
        )

        # Conscientiousness
        c_score = 3.0 + features["detail_words"] * 0.4 + features["planning_words"] * 0.3
        assessments["C"] = TraitAssessment(
            trait="C", score=np.clip(c_score, 1.0, 5.0),
            confidence=0.5, evidence=[f"Planning words: {features['planning_words']:.1f}/100w"],
            method_scores={"linguistic_features": c_score}
        )

        # Openness
        o_score = 3.0 + features["creative_words"] * 0.5 + features["abstract_words"] * 0.4
        assessments["O"] = TraitAssessment(
            trait="O", score=np.clip(o_score, 1.0, 5.0),
            confidence=0.5, evidence=[f"Creative words: {features['creative_words']:.1f}/100w"],
            method_scores={"linguistic_features": o_score}
        )

        return assessments

    def assess_from_llm(
        self,
        messages: List[Message],
        candidate_name: str
    ) -> Dict[str, TraitAssessment]:
        """Use LLM for personality inference (requires llm_client)."""
        if not self.llm_client:
            return self._default_assessment()

        # Build transcript
        transcript = "\n".join(
            f"[{m.speaker_role}]: {m.content}" for m in messages
        )

        prompt = f"""Analyze this dialogue and rate the candidate "{candidate_name}" on Big Five traits (1-5 scale).

TRANSCRIPT:
{transcript}

Rate each trait with evidence:
- Openness (1=conventional, 5=creative)
- Conscientiousness (1=careless, 5=organized)
- Extraversion (1=reserved, 5=outgoing)
- Agreeableness (1=challenging, 5=cooperative)
- Neuroticism (1=calm, 5=anxious)

Respond in JSON format:
{{"O": {{"score": X.X, "evidence": "..."}}, "C": {...}, "E": {...}, "A": {...}, "N": {...}}}
"""

        response = self.llm_client.generate(
            role="validator",
            system_prompt="You are a personality assessment expert. Respond only with valid JSON.",
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse response
        try:
            import json
            cleaned = response.strip()
            if cleaned.startswith("```"):
                cleaned = cleaned.split("```")[1].replace("json", "").strip()
            result = json.loads(cleaned)

            assessments = {}
            for trait in ["O", "C", "E", "A", "N"]:
                if trait in result:
                    assessments[trait] = TraitAssessment(
                        trait=trait,
                        score=float(result[trait].get("score", 3.0)),
                        confidence=0.7,
                        evidence=[result[trait].get("evidence", "LLM inference")],
                        method_scores={"llm_inference": float(result[trait].get("score", 3.0))}
                    )
            return assessments
        except:
            return self._default_assessment()

    def ensemble_assessment(
        self,
        messages: List[Message],
        candidate_name: str = "Candidate",
        methods: List[AssessmentMethod] = None
    ) -> PersonalityAssessment:
        """Combine multiple assessment methods with weighted ensemble."""

        if methods is None:
            methods = [
                AssessmentMethod.INTENT_ANALYSIS,
                AssessmentMethod.BEHAVIOR_EXTRACTION,
                AssessmentMethod.LINGUISTIC_FEATURES
            ]
            if self.llm_client:
                methods.append(AssessmentMethod.LLM_INFERENCE)

        # Collect assessments from each method
        all_assessments = {}
        method_weights = {
            AssessmentMethod.INTENT_ANALYSIS: 0.35,
            AssessmentMethod.BEHAVIOR_EXTRACTION: 0.30,
            AssessmentMethod.LINGUISTIC_FEATURES: 0.15,
            AssessmentMethod.LLM_INFERENCE: 0.20
        }

        for method in methods:
            if method == AssessmentMethod.INTENT_ANALYSIS:
                all_assessments[method] = self.assess_from_intents(messages)
            elif method == AssessmentMethod.BEHAVIOR_EXTRACTION:
                all_assessments[method] = self.assess_from_behaviors(messages)
            elif method == AssessmentMethod.LINGUISTIC_FEATURES:
                all_assessments[method] = self.assess_from_linguistic_features(messages)
            elif method == AssessmentMethod.LLM_INFERENCE:
                all_assessments[method] = self.assess_from_llm(messages, candidate_name)

        # Ensemble: weighted average with confidence weighting
        ensemble_traits = {}
        consistency_flags = []

        for trait in ["O", "C", "E", "A", "N"]:
            scores = []
            confidences = []
            weights = []
            all_evidence = []
            method_scores = {}

            for method, assessment in all_assessments.items():
                if trait in assessment:
                    ta = assessment[trait]
                    scores.append(ta.score)
                    confidences.append(ta.confidence)
                    weights.append(method_weights.get(method, 0.25) * ta.confidence)
                    all_evidence.extend(ta.evidence)
                    method_scores[method.value] = ta.score

            if scores:
                # Weighted average
                ensemble_score = np.average(scores, weights=weights)
                ensemble_confidence = np.mean(confidences)

                # Check consistency
                score_std = np.std(scores)
                if score_std > 1.0:
                    consistency_flags.append(
                        f"{trait}: High variance across methods (std={score_std:.2f})"
                    )
            else:
                ensemble_score = 3.0
                ensemble_confidence = 0.1

            ensemble_traits[trait] = TraitAssessment(
                trait=trait,
                score=round(ensemble_score, 2),
                confidence=round(ensemble_confidence, 2),
                evidence=all_evidence[:5],
                method_scores=method_scores
            )

        overall_confidence = np.mean([t.confidence for t in ensemble_traits.values()])

        return PersonalityAssessment(
            session_id="",  # Set by caller
            method=AssessmentMethod.ENSEMBLE,
            traits=ensemble_traits,
            overall_confidence=round(overall_confidence, 2),
            consistency_flags=consistency_flags,
            raw_features={
                "method_count": len(methods),
                "methods_used": [m.value for m in methods]
            }
        )

    def _default_assessment(self) -> Dict[str, TraitAssessment]:
        """Return neutral assessment when no data available."""
        return {
            trait: TraitAssessment(
                trait=trait, score=3.0, confidence=0.0,
                evidence=["Insufficient data"], method_scores={}
            )
            for trait in ["O", "C", "E", "A", "N"]
        }

    def validate_against_ground_truth(
        self,
        assessment: PersonalityAssessment,
        ground_truth: Dict[str, float]
    ) -> Dict:
        """Compare assessment against ground truth."""
        results = {
            "per_trait": {},
            "aggregate": {}
        }

        errors = []
        direction_matches = 0

        for trait in ["O", "C", "E", "A", "N"]:
            gt_score = ground_truth.get(trait, 3.0)
            pred_score = assessment.traits[trait].score
            error = abs(gt_score - pred_score)
            errors.append(error)

            gt_direction = "high" if gt_score >= 3.5 else "low"
            pred_direction = "high" if pred_score >= 3.5 else "low"
            direction_match = gt_direction == pred_direction
            if direction_match:
                direction_matches += 1

            results["per_trait"][trait] = {
                "ground_truth": gt_score,
                "predicted": pred_score,
                "error": round(error, 2),
                "direction_match": direction_match,
                "confidence": assessment.traits[trait].confidence
            }

        results["aggregate"] = {
            "mean_absolute_error": round(np.mean(errors), 3),
            "max_error": round(np.max(errors), 3),
            "direction_accuracy": direction_matches / 5,
            "overall_assessment": "Pass" if np.mean(errors) < 1.0 and direction_matches >= 3 else "Review"
        }

        return results


# Need this import for the linguistic features method
import re
```

### C.2 Integration with Simulation Engine

Update the simulation engine to use these new components:

```python
# In scripts/simulation_engine.py, add to __init__:

from storage.conversation_store import ConversationStore
from storage.session_store import SessionStore
from validation.personality_judge import PersonalityJudge

class SimulationEngine:
    def __init__(self, ...):
        # ... existing init code ...

        # Initialize enhanced storage
        self.conversation_store = ConversationStore(
            session_id=self.session_id,
            context_window=10
        )
        self.session_store = SessionStore(
            output_dir="./outputs",
            use_sqlite=True
        )
        self.personality_judge = PersonalityJudge()

        # Register agents with conversation store
        self._register_agents()

    def _register_agents(self):
        """Register all agents with the conversation store."""
        self.conversation_store.register_agent(self.candidate.agent_id)
        self.conversation_store.register_agent(self.provoker.agent_id)
        self.conversation_store.register_agent(self.mediator.agent_id)
        self.conversation_store.register_agent(self.system_manager.agent_id)

    def _log_turn(self, speaker_role, speaker_id, text, intent_tag,
                  inner_thought=None, behavior_notes=None, latency_ms=None):
        """Enhanced turn logging using conversation store."""
        message = self.conversation_store.add_message(
            speaker_id=speaker_id,
            speaker_role=speaker_role,
            content=text,
            intent_tag=intent_tag,
            inner_thought=inner_thought,
            behavior_notes=behavior_notes,
            response_latency_ms=latency_ms
        )
        return message

    def _build_output(self) -> SessionOutput:
        """Enhanced output building with personality assessment."""
        # Get dialogue log from conversation store
        dialogue_log = self.conversation_store.export_dialogue_log()

        # Run ensemble personality assessment
        messages = self.conversation_store.get_full_history()
        assessment = self.personality_judge.ensemble_assessment(
            messages=messages,
            candidate_name=self.candidate_name
        )
        assessment.session_id = self.session_id

        # Validate against ground truth
        ground_truth = {
            "O": self.profile.scores.Openness,
            "C": self.profile.scores.Conscientiousness,
            "E": self.profile.scores.Extraversion,
            "A": self.profile.scores.Agreeableness,
            "N": self.profile.scores.Neuroticism
        }
        validation_result = self.personality_judge.validate_against_ground_truth(
            assessment, ground_truth
        )

        # Build full output with assessment
        output = SessionOutput(
            # ... existing fields ...
            dialogue_log=dialogue_log,
            personality_assessment={
                "inferred": {t: a.score for t, a in assessment.traits.items()},
                "confidence": assessment.overall_confidence,
                "method_details": {
                    t: a.method_scores for t, a in assessment.traits.items()
                },
                "consistency_flags": assessment.consistency_flags
            },
            validation_result=validation_result
        )

        # Persist to session store
        self.session_store.save_session(
            session_id=self.session_id,
            profile_id=self.profile.profile_id,
            scenario_id=self.scenario.id,
            conversation_store=self.conversation_store,
            full_session_data=output.model_dump()
        )

        return output
```

---

## D. Enhanced Output Schema

Update the session output to include all new data:

```python
# Add to utils/models.py

class PersonalityAssessmentOutput(BaseModel):
    """Personality assessment in output."""
    inferred_scores: Dict[str, float]
    confidence: float
    method_details: Dict[str, Dict[str, float]]
    consistency_flags: List[str]
    trait_evidence: Dict[str, List[str]]

class ValidationResult(BaseModel):
    """Validation against ground truth."""
    per_trait: Dict[str, Dict]
    aggregate: Dict[str, Any]

class EnhancedSessionOutput(BaseModel):
    """Complete session output with all enhancements."""
    meta_data: SessionMetadata
    candidate_profile: CandidateConfig
    colleague_profiles: List[ColleagueConfig]

    # Dialogue with full detail
    dialogue_log: List[Dict]

    # Legacy statistics (for backward compatibility)
    intent_statistics: IntentStatistics
    assessment_indicators: Dict[str, AssessmentIndicator]

    # NEW: Enhanced personality assessment
    personality_assessment: PersonalityAssessmentOutput

    # NEW: Validation results
    validation_result: ValidationResult

    # NEW: Behavior summary
    behavior_summary: Dict[str, List[str]]

    # Placeholder for human ratings
    human_evaluation: Optional[Dict] = None
```

---

## Success Criteria for A+

1. **Dataset Quality**: ≥200 sessions with >90% format compliance
2. **Validation Metrics**: MAE <1.0, Direction Accuracy >60%
3. **Dual Validation**: Both LLM inference AND human ratings (n≥50)
4. **Baseline Comparison**: Demonstrate BFI prompting > simple prompting
5. **Documentation**: Complete README, architecture docs, paper draft
6. **Reproducibility**: Anyone can clone and run the full pipeline

Good luck!
