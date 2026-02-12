# UbeU V3: Dual-Mode AI Interview Platform — Architecture Design Document

**Project**: Pressure Cooker — AI-Simulated Interview Platform  
**Version**: 3.0 (Dual-Mode Architecture)  
**Author**: Architecture Lead  
**Date**: February 2026  
**Status**: Design Specification  
**Academic Context**: NUS Final Year Thesis — Computer Science  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Motivation & Design Rationale](#2-motivation--design-rationale)
3. [Architecture Overview](#3-architecture-overview)
4. [Mode 1: Case Study Interview (1-on-1 Logical Assessment)](#4-mode-1-case-study-interview)
5. [Mode 2: Group Discussion (1-to-Many Personality Assessment)](#5-mode-2-group-discussion)
6. [Validation Framework](#6-validation-framework)
7. [UI Visualization & HR Dashboard](#7-ui-visualization--hr-dashboard)
8. [Implementation Plan](#8-implementation-plan)
9. [Academic Justification & Evidence Base](#9-academic-justification--evidence-base)

---

## 1. Executive Summary

This document specifies the V3 architecture for splitting the current Step 2 interview platform into two distinct assessment modes, each grounded in established psychometric methodology and informed by recent advances in human-AI group conversation research (Hu et al., UIST 2025 — DialogLab).

**The core insight from expert feedback**: Case study interviews assess **logical/analytical thinking** through 1-on-1 structured problem-solving. Personality traits are assessed through **behavioral observation in group settings**, not through case studies. Combining both in a single format conflates two distinct constructs and weakens the validity of each.

**V3 introduces two modes**:

| Aspect | Mode 1: Case Study | Mode 2: Group Discussion |
|--------|-------------------|-------------------------|
| **Format** | 1-on-1 (candidate + AI facilitator) | 1-to-many (candidate + 2-3 AI agents) |
| **Construct Measured** | Analytical thinking, problem-solving, structured reasoning | Big Five personality traits (OCEAN) |
| **Assessment Method** | Rubric-anchored logic evaluation with citation-based evidence | Behavioral signal extraction with facet-level personality inference |
| **Theoretical Basis** | Management consulting case interview methodology | Assessment Center method; Leaderless Group Discussion (LGD) |
| **Ground Truth** | Expert-validated case solutions | BFI-44 self-report (convergent validity) |
| **Key Reference** | McKinsey/BCG case interview format | DialogLab (Hu et al., UIST 2025); Arthur et al., 2003 |

Both modes produce **evidence-based assessment reports** where every score is backed by direct quotes from the conversation transcript, enabling transparent and auditable candidate evaluation by HR managers.

---

## 2. Motivation & Design Rationale

### 2.1 Expert Feedback That Triggered This Redesign

A senior management consultant with extensive case interview experience identified a fundamental construct validity problem:

> "Case studies are always 1-on-1. The interviewer is looking for logical thinking process — how the candidate structures a problem, requests data, synthesizes findings, and arrives at a recommendation. Personality traits are checked separately through behavioral questions, not through case analysis."

This feedback exposes a **construct contamination** problem in V2: the group discussion format around a case study conflated logical assessment (which requires structured 1-on-1 probing) with personality observation (which requires naturalistic multi-party interaction). Neither construct was measured cleanly.

### 2.2 Academic Justification for Separation

The separation is supported by well-established psychometric principles:

**Construct validity** requires that an assessment measures what it claims to measure. When logical reasoning and personality traits are assessed through the same task format, it becomes impossible to attribute variance in scores to either construct independently. This is known as the **method-construct confound** (Lievens & Conway, 2001).

**Assessment Center (AC) research** shows that different exercises (in-basket, group discussion, role-play) tap different constructs, and combining them without clear construct mapping weakens both content validity and criterion-related validity (Arthur et al., 2003; Thornton & Gibbons, 2009).

### 2.3 Why DialogLab Is Relevant

DialogLab (Hu et al., UIST 2025) provides empirical evidence and a design framework directly applicable to Mode 2:

1. **Group dynamics ↔ Conversation flow separation**: DialogLab's core contribution — decoupling social structure (who participates, their roles) from temporal flow (how the conversation unfolds through phases). This maps directly to our need to configure AI agent personas independently from discussion phase management.

2. **Human Control mode superiority**: DialogLab's evaluation with 14 participants showed Human Control mode scored significantly higher in engagement (p < .05) and was perceived as more effective and realistic than Autonomous or Reactive modes. This validates our hybrid approach where the candidate drives the conversation while AI agents respond strategically.

3. **Snippet-based phase management**: DialogLab's concept of "snippets" — discrete conversation phases with distinct interaction styles — aligns with our 8-phase discussion structure (OPENING → STRESS_TEST → CLOSING) and provides a published framework to cite.

4. **Verification analytics**: DialogLab's verification dashboard (turn-taking distribution, sentiment flow, participation balance) establishes precedent for the kind of post-session analytics our HR dashboard needs to display.

5. **Configurable agent personas**: DialogLab allows defining agent name, voice, emotional tone, and backstory through an Inspector Panel, which parallels our BFI-calibrated agent personality system from Step 1.

---

## 3. Architecture Overview

### 3.1 High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BROWSER (Streamlit)                          │
│                                                                     │
│  ┌──────────┐   ┌──────────────┐   ┌──────────────┐   ┌─────────┐ │
│  │  Consent  │──▶│   BFI-44     │──▶│  Mode Select  │──▶│ Survey  │ │
│  │  Page     │   │  Page        │   │  Page         │   │ Page    │ │
│  └──────────┘   └──────────────┘   └───────┬───────┘   └─────────┘ │
│                                     ┌──────┴──────┐                 │
│                               ┌─────▼─────┐ ┌─────▼──────┐         │
│                               │  MODE 1   │ │  MODE 2    │         │
│                               │  Case     │ │  Group     │         │
│                               │  Study    │ │  Discussion│         │
│                               │  1-on-1   │ │  1-to-many │         │
│                               └─────┬─────┘ └─────┬──────┘         │
│                                     └──────┬──────┘                 │
│                               ┌────────────▼────────────┐           │
│                               │    Results Dashboard    │           │
│                               │    (HR Manager View)    │           │
│                               └─────────────────────────┘           │
└─────────────────────────────────────────────────────────────────────┘
                                      │
                         ┌────────────▼────────────┐
                         │    BACKEND (FastAPI)     │
                         │                         │
                         │  ┌───────────────────┐  │
                         │  │ SessionManager    │  │
                         │  │  ├─ CaseEngine    │  │
                         │  │  └─ GroupEngine    │  │
                         │  └───────────────────┘  │
                         │                         │
                         │  ┌───────────────────┐  │
                         │  │ EvidenceAnalyzer  │  │
                         │  │  ├─ LogicEval     │  │
                         │  │  └─ TraitEval     │  │
                         │  └───────────────────┘  │
                         │                         │
                         │  ┌───────────────────┐  │
                         │  │ ValidationEngine  │  │
                         │  │  ├─ MultiJudge    │  │
                         │  │  └─ Ensemble      │  │
                         │  └───────────────────┘  │
                         └────────────┬────────────┘
                                      │
                              OpenRouter API
                         (DeepSeek / Claude Haiku /
                          Gemini Flash)
```

### 3.2 Shared Infrastructure

Both modes share the following components:

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **ParticipantManager** | Registration, consent, BFI-44 ground truth | Existing (no change) |
| **BFI-44 Page** | Self-report personality questionnaire | Existing (no change) |
| **Timer System** | Session duration with LLM latency compensation | Existing (configurable per mode) |
| **TTS System** | Web Speech API for AI agent voices | Existing (extend for multiple voices in Mode 2) |
| **EvidenceExtractor** | Per-turn quote extraction with citation linking | New shared module |
| **OutputManager** | Session data persistence and export | Extended for dual-mode output |
| **Admin Dashboard** | HR manager view of all participant results | Extended for dual-mode display |

### 3.3 Mode Selection Logic

```python
# After BFI-44 completion, participant is assigned to one or both modes
# Study design options:

# Option A: Within-subject (each participant does both modes)
#   - Order counterbalanced: half do Case first, half do Group first
#   - Enables direct comparison of assessment outputs per participant
#   - Stronger statistical design for thesis

# Option B: Between-subject (each participant does one mode)
#   - Randomly assigned to Case or Group
#   - Avoids order effects and fatigue
#   - Simpler but requires larger N

# RECOMMENDED for thesis: Option A (within-subject, counterbalanced)
# Justification: Allows convergent validity analysis between
# Mode 2 personality inference and BFI-44 ground truth while
# also collecting Mode 1 logical assessment data from the same
# participants, enabling correlation analysis between cognitive
# ability and personality traits.
```

---

## 4. Mode 1: Case Study Interview

### 4.1 Design Philosophy

Mode 1 implements a **faithful simulation of a management consulting case interview**. The candidate works 1-on-1 with a single AI facilitator who plays the role of an interviewer holding case data. The facilitator provides data upon request but does **not** guide analysis, suggest frameworks, or evaluate reasoning aloud.

**What Mode 1 assesses** (logical/analytical constructs):

| Construct | Definition | Observable Behaviors |
|-----------|-----------|---------------------|
| **Problem Structuring** | Ability to decompose an ambiguous business problem into analyzable components | Uses frameworks (profitability tree, 4Ps, etc.), identifies key dimensions, articulates hypotheses |
| **Hypothesis-Driven Thinking** | Forms and tests hypotheses using data rather than exploring randomly | States explicit hypotheses before requesting data, updates beliefs based on evidence |
| **Quantitative Reasoning** | Performs calculations, interprets numbers, draws quantitative conclusions | Mental math, back-of-envelope estimation, ratio/percentage interpretation |
| **Data Synthesis** | Connects findings across multiple data categories into coherent insights | Cross-references data points, identifies patterns, explains causal relationships |
| **Recommendation Quality** | Arrives at actionable, evidence-backed recommendations with awareness of risks | Specific action items, supporting data cited, risks/trade-offs acknowledged |
| **Communication Clarity** | Expresses reasoning clearly and structured | Logical flow, signposting ("First... Second..."), concise explanations |

**What Mode 1 does NOT assess**: personality traits, collaboration skills, leadership, stress management. These are explicitly delegated to Mode 2.

### 4.2 Architecture

```
┌─────────────────────────────────────────────────────┐
│                    MODE 1: CASE STUDY                │
│                                                      │
│  ┌──────────────┐                                    │
│  │  CANDIDATE    │◄──────────────────────────┐       │
│  │  (Human)      │                           │       │
│  └──────┬───────┘                           │       │
│         │ text input                         │       │
│         ▼                                    │       │
│  ┌──────────────┐     ┌──────────────────┐  │       │
│  │  CaseEngine   │────▶│  AI FACILITATOR  │──┘       │
│  │               │     │  (Single Agent)  │          │
│  │  - Data gate  │     │                  │          │
│  │  - Phase track│     │  Role: Data      │          │
│  │  - Timer      │     │  clerk only.     │          │
│  └──────┬───────┘     │  No guidance.    │          │
│         │              │  No evaluation.  │          │
│         │              └──────────────────┘          │
│         ▼                                            │
│  ┌──────────────────────────────────────────┐       │
│  │        POST-SESSION EVALUATION            │       │
│  │                                           │       │
│  │  LogicEvaluator (3-pass, evidence-based)  │       │
│  │    ├─ Problem Structuring    [1-5]        │       │
│  │    ├─ Hypothesis Thinking    [1-5]        │       │
│  │    ├─ Quantitative Reasoning [1-5]        │       │
│  │    ├─ Data Synthesis         [1-5]        │       │
│  │    ├─ Recommendation Quality [1-5]        │       │
│  │    └─ Communication Clarity  [1-5]        │       │
│  │                                           │       │
│  │  Each score backed by:                    │       │
│  │    - Direct quotes from transcript        │       │
│  │    - Turn numbers for traceability        │       │
│  │    - Rubric anchor level description      │       │
│  └──────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────┘
```

### 4.3 AI Facilitator Design

The facilitator is deliberately constrained to be a **data clerk**, not a discussion partner. This is critical for construct validity — if the facilitator helps structure the problem, the assessment cannot distinguish the candidate's analytical ability from the AI's guidance.

```python
# Facilitator system prompt (strict version)
FACILITATOR_SYSTEM_PROMPT = """
You are a DATA CLERK in a case interview. You hold business data that
the candidate needs to solve the case.

YOUR ROLE:
- Present the case brief at the start
- Provide data ONLY when the candidate asks specific questions
- Respond with factual data — numbers, tables, categories
- If the candidate asks a vague question, ask them to be more specific

STRICT RULES:
- NEVER suggest frameworks, structures, or analytical approaches
- NEVER say "That's a good point" or evaluate the candidate's reasoning
- NEVER use directive phrases: "Let's consider...", "This suggests...",
  "It's worth noting...", "You might want to look at..."
- NEVER ask follow-up questions that guide analysis
- NEVER summarize implications of the data you provide
- Format: "Here is [data category]: [numbers/facts]." FULL STOP.

If the candidate asks "What do you think?" or seeks your opinion:
→ Reply: "I can provide data to help you analyze. What specific
   information would you like?"

You are testing whether the CANDIDATE can structure problems and
synthesize data independently. Any guidance you provide invalidates
the assessment.
"""
```

### 4.4 Data Gating System

The case study data is organized into categories, progressively revealed only when the candidate asks relevant questions. This tests the candidate's ability to identify what data is needed.

```python
# Example case: MedDevice market entry
CASE_DATA = {
    "market_size": {
        "keywords": ["market", "size", "TAM", "revenue", "industry"],
        "data": "The global medical device market is $550B...",
        "revealed": False
    },
    "competitor_landscape": {
        "keywords": ["competitor", "competition", "players", "share"],
        "data": "Top 3 players hold 65% market share...",
        "revealed": False
    },
    "cost_structure": {
        "keywords": ["cost", "margin", "expense", "COGS", "profit"],
        "data": "Manufacturing cost breakdown: ...",
        "revealed": False
    },
    # ... 8-12 categories per case
}
```

**Tracking metrics** computed during the session:
- `data_categories_requested`: which categories the candidate proactively asked for
- `data_categories_missed`: available data never requested (indicates blind spots)
- `time_to_first_hypothesis`: seconds from case brief to first stated hypothesis
- `hypothesis_count`: number of explicit hypotheses stated
- `data_requests_per_hypothesis`: ratio indicating hypothesis-driven vs. exploratory approach
- `quantitative_statements`: count of numerical calculations or interpretations

### 4.5 Evidence-Based Logic Evaluation

The post-session evaluator uses **3 independent LLM passes** with a detailed rubric, extracting direct quotes as evidence for each score.

#### 4.5.1 Rubric Design (6 Dimensions × 5 Levels)

Each dimension has explicit behavioral anchors at each level. Example for **Problem Structuring**:

```
PROBLEM STRUCTURING RUBRIC:

Score 1 — No Structure
  The candidate dove into data requests or recommendations without
  any attempt to organize the problem. No framework or decomposition
  visible. Responses are reactive and scattered.
  
  Evidence signals: Random data requests with no stated logic,
  no "let me break this down" type statements, no hypothesis.

Score 2 — Minimal Structure  
  The candidate mentioned 1-2 dimensions but did not systematically
  decompose the problem. Partial awareness of structure without
  follow-through.
  
  Evidence signals: Mentions one angle (e.g., "let's look at costs")
  but doesn't map the full problem space.

Score 3 — Adequate Structure
  The candidate identified the key dimensions of the problem and
  organized their analysis around them, though with some gaps or
  inconsistency in execution.
  
  Evidence signals: Names 2-3 key areas, requests data for most,
  but may skip some or lose track of the structure mid-session.

Score 4 — Strong Structure
  The candidate used a clear, appropriate framework to decompose
  the problem. Systematically worked through each dimension and
  connected findings across areas.
  
  Evidence signals: Explicit framework statement early on,
  systematic data requests following the framework, references
  back to the framework during synthesis.

Score 5 — Exceptional Structure
  The candidate demonstrated sophisticated problem decomposition,
  using a well-chosen framework with customized dimensions specific
  to this case. Adapted the structure as new data revealed nuances.
  
  Evidence signals: Custom framework beyond generic templates,
  dynamic restructuring based on data, clear prioritization of
  which dimensions matter most and why.
```

#### 4.5.2 Citation-Based Evidence Extraction

```python
# Evaluator prompt structure
LOGIC_EVALUATOR_PROMPT = """
You are evaluating a case study interview transcript.

TASK: Score the candidate on 6 dimensions using the rubric below.
For EACH dimension, you MUST:

1. Assign a score (1-5) based on the rubric anchors
2. Provide 2-4 DIRECT QUOTES from the candidate's responses
   that justify your score. Each quote must include:
   - The exact quoted text (verbatim, max 2 sentences)
   - The turn number where it appears
   - What the quote demonstrates (e.g., "shows hypothesis formation")
3. Note any ABSENT behaviors — things you expected to see but didn't

OUTPUT FORMAT (JSON):
{
  "dimensions": {
    "problem_structuring": {
      "score": 4,
      "confidence": 0.85,
      "supporting_evidence": [
        {
          "quote": "Let me structure this as a profitability problem — 
                    I want to look at revenue drivers and cost drivers separately.",
          "turn_number": 3,
          "demonstrates": "Explicit framework articulation with customized dimensions"
        },
        {
          "quote": "Before I ask for more data, let me map out what I need: 
                    market size, our cost position, and competitive dynamics.",
          "turn_number": 5,
          "demonstrates": "Systematic data planning before execution"
        }
      ],
      "absent_behaviors": [
        "Did not adapt framework when cost data revealed unexpected pattern"
      ],
      "rubric_justification": "Candidate used a clear profitability framework 
        and systematically requested data for each dimension. Scored 4 rather 
        than 5 because the framework was not adapted when new data suggested 
        the problem was more about pricing power than cost reduction."
    },
    // ... other 5 dimensions
  },
  "overall_assessment": {
    "strengths": ["..."],
    "development_areas": ["..."],
    "summary": "..."
  }
}
"""
```

#### 4.5.3 Multi-Pass Aggregation

```python
async def evaluate_case_session(transcript: list[Turn]) -> LogicAssessment:
    """Run 3 independent evaluation passes and aggregate."""
    
    # 3 parallel passes with temperature=0.4
    results = await asyncio.gather(
        _run_single_eval(transcript, pass_id=1),
        _run_single_eval(transcript, pass_id=2),
        _run_single_eval(transcript, pass_id=3),
    )
    
    aggregated = {}
    for dimension in DIMENSIONS:
        scores = [r[dimension]["score"] for r in results]
        aggregated[dimension] = {
            "final_score": statistics.median(scores),
            "score_range": max(scores) - min(scores),
            "agreement": "high" if max(scores) - min(scores) <= 1 else "low",
            # Union of evidence across all passes, deduplicated by turn_number
            "evidence": _deduplicate_evidence(
                [e for r in results for e in r[dimension]["supporting_evidence"]]
            ),
            "absent_behaviors": _union_absent(
                [r[dimension]["absent_behaviors"] for r in results]
            ),
        }
    
    return LogicAssessment(**aggregated)
```

### 4.6 Session Behavioral Statistics

Computed automatically from the transcript (no LLM needed):

```python
@dataclass
class CaseSessionStats:
    # Timing
    total_duration_seconds: int
    time_to_first_data_request: int       # seconds
    time_to_first_hypothesis: int         # seconds
    time_spent_in_synthesis: int          # seconds (last phase)
    
    # Data engagement
    data_categories_requested: int        # out of total available
    data_categories_available: int
    data_coverage_ratio: float            # requested / available
    data_requests_before_hypothesis: int  # lower = more hypothesis-driven
    
    # Communication
    total_candidate_turns: int
    avg_words_per_turn: float
    questions_asked: int                  # candidate → facilitator
    quantitative_statements: int          # turns with numbers/calculations
    framework_mentions: int              # explicit framework references
    
    # Structure signals
    signposting_count: int               # "First...", "Moving to...", etc.
    hypothesis_statements: int           # "I hypothesize...", "My theory is..."
    synthesis_statements: int            # "Putting this together...", "This means..."
```

---

## 5. Mode 2: Group Discussion

### 5.1 Design Philosophy

Mode 2 implements an **AI-simulated Leaderless Group Discussion (LGD)**, a well-established Assessment Center method for observing interpersonal behavior and personality traits in a naturalistic group setting.

The key insight from DialogLab: **multi-party conversations require explicit modeling of both group dynamics (roles, relationships) and conversation flow dynamics (phases, turn-taking)**. Our architecture adopts this separation.

**What Mode 2 assesses** (personality/behavioral constructs):

| Big Five Trait | Observable in Group Discussion Through... |
|---------------|------------------------------------------|
| **Openness** | Engagement with novel ideas, willingness to explore alternatives, abstract thinking vs. concrete-only |
| **Conscientiousness** | Organization of arguments, time awareness, follow-through on discussion threads |
| **Extraversion** | Response length, initiation frequency, social engagement, elaboration vs. brevity |
| **Agreeableness** | Conflict handling, accommodation vs. pushback, warmth, acknowledgment of others |
| **Neuroticism** | Stress response under disagreement, emotional reactivity, composure under pressure |

**What Mode 2 does NOT assess**: logical reasoning, quantitative ability, framework usage. These are explicitly delegated to Mode 1.

### 5.2 Architecture (DialogLab-Informed)

```
┌────────────────────────────────────────────────────────────────────┐
│                    MODE 2: GROUP DISCUSSION                        │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────┐      │
│  │              GROUP DYNAMICS LAYER                        │      │
│  │              (DialogLab §4.1.1: social setup)            │      │
│  │                                                          │      │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │      │
│  │  │ ALEX     │  │ JORDAN   │  │ RILEY    │              │      │
│  │  │ Assertive│  │ Supportive│ │ Skeptical│              │      │
│  │  │ Hi-E,Lo-A│  │ Hi-A,Hi-E│  │ Lo-E,Lo-O│              │      │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘              │      │
│  │       │              │              │                    │      │
│  │       └──────────────┼──────────────┘                    │      │
│  │                      │                                   │      │
│  │              ┌───────▼───────┐                           │      │
│  │              │   CANDIDATE   │                           │      │
│  │              │   (Human)     │                           │      │
│  │              └───────────────┘                           │      │
│  └─────────────────────────────────────────────────────────┘      │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────┐      │
│  │           CONVERSATION FLOW LAYER                        │      │
│  │           (DialogLab §4.1.2: temporal progression)       │      │
│  │                                                          │      │
│  │  ┌─────────┐   ┌──────────┐   ┌──────────┐             │      │
│  │  │Snippet 1│──▶│Snippet 2 │──▶│Snippet 3 │──▶ ...      │      │
│  │  │OPENING  │   │EXPLORE   │   │DISAGREE  │             │      │
│  │  │neutral  │   │agreement │   │challenge │             │      │
│  │  │2 turns  │   │4 turns   │   │4 turns   │             │      │
│  │  └─────────┘   └──────────┘   └──────────┘             │      │
│  └─────────────────────────────────────────────────────────┘      │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────┐      │
│  │              ORCHESTRATION ENGINE                        │      │
│  │              (GroupEngine)                                │      │
│  │                                                          │      │
│  │  DiscussionOrchestrator                                  │      │
│  │    ├─ Phase Manager (snippet transitions)                │      │
│  │    ├─ Speaker Selector (trait-elicitation strategy)       │      │
│  │    ├─ Tension Monitor (real-time sentiment)              │      │
│  │    └─ Trait Coverage Tracker (which traits observed)     │      │
│  └─────────────────────────────────────────────────────────┘      │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────┐      │
│  │           POST-SESSION PERSONALITY INFERENCE             │      │
│  │                                                          │      │
│  │  Layer 1: Per-Turn Behavioral Signals (fast, in-session) │      │
│  │  Layer 2: 28-Facet BFI Detection (post-session, deep)   │      │
│  │  Layer 3: 3-Judge Ensemble (multi-model consensus)       │      │
│  └─────────────────────────────────────────────────────────┘      │
└────────────────────────────────────────────────────────────────────┘
```

### 5.3 AI Agent Design (Fixed Personality Bots)

Unlike Mode 1 where the AI is personality-neutral, Mode 2 requires AI agents with **fixed, known personality profiles**. The agents' personalities are designed to **elicit specific behavioral responses from the candidate**.

The agent personality system is validated by Step 1 research (agent trait consistency validation, Pearson r = 0.77-0.78 for O, E, A, N across 144 sessions).

#### 5.3.1 Agent Profiles

```python
AGENT_PROFILES = {
    "alex": {
        "name": "Alex",
        "role": "Assertive Challenger",
        "personality": PersonalityVector(O=0.6, C=0.5, E=0.8, A=0.3, N=0.3),
        "purpose": "Elicit candidate's conflict handling (A), stress response (N), assertiveness (E)",
        "behavioral_instructions": """
            - Push back on ideas you disagree with. Don't soften language.
            - Speak confidently and at length (3-5 sentences).
            - Challenge weak reasoning directly: "I don't think that works because..."
            - Occasionally propose competing ideas to force the candidate to
              either defend their position or accommodate.
        """,
        "voice_settings": {"pitch": 0.9, "rate": 1.1},  # Lower pitch, slightly fast
    },
    "jordan": {
        "name": "Jordan",
        "role": "Supportive Collaborator",
        "personality": PersonalityVector(O=0.7, C=0.6, E=0.7, A=0.8, N=0.2),
        "purpose": "Elicit candidate's leadership style (E), idea engagement (O), collaboration (A)",
        "behavioral_instructions": """
            - Acknowledge others' ideas before sharing your own.
            - Build on the candidate's suggestions: "Building on what you said..."
            - Show enthusiasm for creative ideas.
            - Occasionally ask the candidate to elaborate or lead the group.
        """,
        "voice_settings": {"pitch": 1.1, "rate": 1.0},  # Higher pitch, normal rate
    },
    "riley": {
        "name": "Riley",
        "role": "Quiet Skeptic",
        "personality": PersonalityVector(O=0.2, C=0.7, E=0.2, A=0.5, N=0.5),
        "purpose": "Elicit candidate's engagement with quiet members (E), idea defense (O), patience (A)",
        "behavioral_instructions": """
            - Keep responses SHORT — 1-2 sentences maximum.
            - Express doubt about novel ideas: "I'm not sure that would work."
            - Don't volunteer extra information. Speak only when necessary.
            - Focus on practical concerns: "But what about the cost?"
            - Do NOT initiate new topics.
        """,
        "voice_settings": {"pitch": 1.0, "rate": 0.9},  # Normal pitch, slightly slow
    },
}
```

#### 5.3.2 Why These Three Profiles

The three agents create a **personality tension triangle** designed to elicit the full range of Big Five behaviors:

```
                    ALEX (Assertive)
                   E=0.8, A=0.3
                  /               \
                 /                 \
    Conflict zone         Challenge zone
    (tests candidate      (tests candidate
     Agreeableness)        Neuroticism)
               /                     \
              /                       \
   JORDAN (Supportive)  ────────  RILEY (Skeptical)
   A=0.8, E=0.7                  E=0.2, O=0.2
                 Engagement gap
              (tests candidate
               Extraversion,
               Openness)
```

- **Alex vs. Candidate**: Tests how the candidate handles direct disagreement → reveals **Agreeableness** (accommodate vs. push back) and **Neuroticism** (maintain composure vs. show stress)
- **Jordan + Candidate**: Tests whether the candidate elaborates on ideas when supported → reveals **Openness** (explore vs. stay concrete) and **Extraversion** (elaborate vs. stay brief)
- **Riley's silence**: Tests whether the candidate engages quiet members → reveals **Extraversion** (initiate vs. wait) and **Agreeableness** (inclusive vs. ignoring)
- **Alex vs. Jordan disagreement**: The AI agents occasionally disagree with each other, forcing the candidate to mediate, take sides, or redirect → reveals **leadership style** and **conflict resolution approach**

### 5.4 Scenario Design (Behavioral Situations)

Unlike Mode 1's business case with data, Mode 2 uses **behavioral situations** — workplace scenarios that naturally elicit interpersonal behavior without requiring quantitative analysis.

```python
GROUP_SCENARIOS = {
    "resource_conflict": {
        "title": "Project Resource Allocation",
        "brief": """
            Your team has been given a critical 3-week project with a tight deadline.
            You need to decide how to allocate your team's limited resources:
            - Only 2 out of 4 proposed features can be built
            - One team member will need to work overtime
            - The client has conflicting priorities
            
            Discuss with your team and reach a consensus on the plan.
        """,
        "primary_traits_elicited": ["Agreeableness", "Conscientiousness"],
        "secondary_traits_elicited": ["Extraversion", "Neuroticism"],
        "phases": [
            {"name": "INTRODUCTION", "turns": 2, "style": "neutral"},
            {"name": "EXPLORATION", "turns": 4, "style": "agreement",
             "goal": "Each person shares their initial preference"},
            {"name": "CONFLICT", "turns": 5, "style": "disagreement",
             "goal": "Alex pushes for a different plan than the candidate",
             "trigger": "Alex disagrees with the candidate's suggested priority"},
            {"name": "RESOLUTION", "turns": 4, "style": "consensus",
             "goal": "Group must converge on a single plan"},
            {"name": "CLOSING", "turns": 2, "style": "neutral"},
        ],
    },
    "creative_brainstorm": {
        "title": "New Initiative Brainstorm",
        "brief": """
            Your company wants to launch a new employee engagement initiative.
            Leadership has asked your team to brainstorm ideas and present the
            top recommendation by end of day. There's no budget constraint yet,
            but you'll need to justify the investment.
            
            Discuss creative ideas and converge on a recommendation.
        """,
        "primary_traits_elicited": ["Openness", "Extraversion"],
        "secondary_traits_elicited": ["Agreeableness", "Conscientiousness"],
        "phases": [
            {"name": "INTRODUCTION", "turns": 2, "style": "neutral"},
            {"name": "IDEATION", "turns": 5, "style": "agreement",
             "goal": "Generate diverse ideas. Jordan is enthusiastic, Riley skeptical"},
            {"name": "EVALUATION", "turns": 4, "style": "neutral",
             "goal": "Narrow down ideas. Alex pushes for pragmatic choices"},
            {"name": "DEFENSE", "turns": 4, "style": "disagreement",
             "goal": "Candidate must defend their preferred idea against Alex's criticism"},
            {"name": "CLOSING", "turns": 2, "style": "neutral"},
        ],
    },
    "crisis_management": {
        "title": "Unexpected Project Crisis",
        "brief": """
            Your team just learned that a key deliverable has a critical bug
            discovered by the client, who is threatening to escalate. The team
            needs to decide:
            - Who communicates with the client
            - Whether to delay the launch or ship a partial fix
            - How to prevent this from happening again
            
            Time pressure: you have 30 minutes before the client call.
        """,
        "primary_traits_elicited": ["Neuroticism", "Conscientiousness"],
        "secondary_traits_elicited": ["Extraversion", "Agreeableness"],
        "phases": [
            {"name": "CRISIS_REVEAL", "turns": 2, "style": "neutral",
             "goal": "Alex delivers the bad news with urgency"},
            {"name": "INITIAL_REACTION", "turns": 3, "style": "disagreement",
             "goal": "Observe stress response. Alex panics slightly, Jordan stays calm"},
            {"name": "PROBLEM_SOLVING", "turns": 5, "style": "neutral",
             "goal": "Candidate proposes a plan under time pressure"},
            {"name": "STRESS_TEST", "turns": 4, "style": "disagreement",
             "goal": "Alex challenges the plan aggressively. Tests composure."},
            {"name": "CLOSING", "turns": 2, "style": "consensus"},
        ],
    },
    "new_member_integration": {
        "title": "Onboarding a New Team Member",
        "brief": """
            Riley has just joined your team (previously at a different company).
            Your team needs to bring Riley up to speed on the current project
            and decide how to redistribute responsibilities. Riley has strong
            technical skills but different work style preferences.
            
            Help integrate Riley while maintaining team momentum.
        """,
        "primary_traits_elicited": ["Extraversion", "Agreeableness"],
        "secondary_traits_elicited": ["Openness", "Conscientiousness"],
        "phases": [
            {"name": "WELCOME", "turns": 2, "style": "agreement",
             "goal": "Jordan welcomes Riley. Observe if candidate takes initiative"},
            {"name": "CONTEXT_SHARING", "turns": 4, "style": "neutral",
             "goal": "How does candidate explain things? Adapt to Riley's style?"},
            {"name": "ROLE_NEGOTIATION", "turns": 5, "style": "disagreement",
             "goal": "Riley's preferred approach conflicts with current workflow"},
            {"name": "RESOLUTION", "turns": 3, "style": "consensus"},
            {"name": "CLOSING", "turns": 2, "style": "neutral"},
        ],
    },
}
```

### 5.5 Speaker Selection Strategy (Trait-Elicitation Driven)

DialogLab's evaluation showed that **human control mode produced higher engagement and realism**. Our hybrid approach gives the candidate free control over when and what they say (human control) while the AI orchestrator strategically selects which bot responds (autonomous selection optimized for trait elicitation).

```python
class TraitElicitationSelector:
    """
    Selects the next AI speaker based on which personality traits
    have been insufficiently observed so far.
    
    Inspired by DialogLab's discussion of speaker selection in
    multi-party settings (§4.1.2, §5.2.2) and our SmartSystemManager
    from Step 2 (competency-driven routing).
    """
    
    def select_next_speaker(
        self,
        context: DiscussionContext,
        candidate_last_turn: str,
        trait_coverage: dict[str, float],  # trait → observation confidence
    ) -> str:
        
        # Find least-observed trait
        weakest_trait = min(trait_coverage, key=trait_coverage.get)
        
        # Map trait to best-eliciting agent
        TRAIT_TO_AGENT = {
            "agreeableness": "alex",      # Alex's disagreement reveals A
            "neuroticism": "alex",        # Alex's pressure reveals N  
            "openness": "jordan",         # Jordan's enthusiasm reveals O
            "extraversion": "riley",      # Riley's silence reveals E
            "conscientiousness": "jordan", # Jordan's collaboration reveals C
        }
        
        preferred = TRAIT_TO_AGENT[weakest_trait]
        
        # Avoid same speaker twice in a row
        if preferred == context.last_speaker:
            # Fall back to phase-appropriate default
            return self._phase_default(context.current_phase)
        
        return preferred
```

### 5.6 Personality Inference Pipeline (3-Layer)

#### Layer 1: Real-Time Behavioral Signals (During Session)

Fast, rule-based classification per turn. Used for live UI indicators and orchestrator decisions.

```python
# Computed per candidate turn, no LLM call needed
def extract_behavioral_signals(turn: str, context: DiscussionContext) -> dict:
    return {
        "word_count": len(turn.split()),                    # E signal
        "questions_asked": count_questions(turn),           # E signal  
        "addressed_others_by_name": check_names(turn),      # E, A signal
        "used_hedging_language": check_hedging(turn),        # A, N signal
        "expressed_disagreement": check_disagreement(turn),  # A signal (low)
        "acknowledged_others": check_acknowledgment(turn),   # A signal (high)
        "proposed_new_idea": check_novelty(turn),            # O signal
        "referenced_practical_concerns": check_practical(turn),  # O signal (low)
        "showed_stress_language": check_stress(turn),        # N signal
        "organized_response": check_structure(turn),         # C signal
    }
```

#### Layer 2: 28-Facet Detection (Post-Session)

LLM-based analysis of the full transcript, extracting evidence for each BFI facet. This is the existing `FacetDetector` from Step 2, reused without modification.

#### Layer 3: Multi-Model Ensemble (Post-Session)

3 LLMs independently infer OCEAN scores from the transcript. Aggregated via median with inter-judge agreement metrics. This is the existing `EnsembleDetector` from Step 2, reused without modification.

### 5.7 Trait-Specific Evidence Extraction

The critical addition for Mode 2 is **trait-specific citation linking** — every OCEAN score must be traceable to specific candidate behaviors in the transcript.

```python
# Post-session trait evidence prompt
TRAIT_EVIDENCE_PROMPT = """
Analyze this group discussion transcript and extract evidence for
each Big Five personality trait of the CANDIDATE (not the AI agents).

For each trait, provide:
1. A score (0.0 - 1.0) 
2. 3-5 direct quotes from the CANDIDATE that support your score
3. For each quote:
   - The exact text (verbatim)
   - Turn number
   - Which facet it demonstrates (e.g., "assertiveness" for Extraversion)
   - Signal direction: does this indicate HIGH or LOW levels of the trait?
   - Signal strength: weak / moderate / strong

CRITICAL CALIBRATION NOTES:
- Response LENGTH is a primary signal for Extraversion. Count words.
  Average < 15 words/turn = low E. Average > 40 words/turn = high E.
- Simply PARTICIPATING in a group discussion is NOT evidence of Openness.
  Only rate O > 0.6 if the candidate actively explores hypotheticals,
  proposes creative alternatives, or engages with abstract ideas.
- Being ORGANIZED in a discussion is NOT sufficient for high Conscientiousness.
  Most people sound somewhat organized. Only rate C > 0.7 if the candidate
  actively imposes additional structure (timelines, action items, follow-ups).
- ABSENCE of behavior is also evidence. If the candidate never pushes back
  on Alex's disagreements, that is evidence of high Agreeableness.
- If the candidate never initiates topics or engages Riley (the quiet member),
  that is evidence of low Extraversion.

BEHAVIORAL STATISTICS (pre-computed):
- Candidate average words per turn: {avg_words}
- Candidate turn count: {turn_count}  
- Times candidate addressed others by name: {name_mentions}
- Times candidate asked questions: {questions}
- Times candidate expressed disagreement: {disagreements}
- Times candidate acknowledged others: {acknowledgments}
"""
```

---

## 6. Validation Framework

### 6.1 Overview

Each mode requires a distinct validation strategy because they measure different constructs. However, both share the principle of **evidence-based transparency** — every score is backed by citable evidence from the transcript.

```
┌────────────────────────────────────────────────────────────────┐
│                    VALIDATION FRAMEWORK                        │
│                                                                │
│  ┌──────────────────────┐    ┌──────────────────────┐         │
│  │  MODE 1 VALIDATION   │    │  MODE 2 VALIDATION   │         │
│  │                      │    │                      │         │
│  │  ► Inter-rater       │    │  ► Convergent        │         │
│  │    reliability       │    │    validity           │         │
│  │    (3-pass agreement)│    │    (vs BFI-44)        │         │
│  │                      │    │                      │         │
│  │  ► Content validity  │    │  ► Discriminant       │         │
│  │    (rubric coverage) │    │    validity           │         │
│  │                      │    │    (cross-trait)      │         │
│  │  ► Construct         │    │                      │         │
│  │    independence      │    │  ► Test-retest        │         │
│  │    (no personality   │    │    reliability        │         │
│  │     contamination)   │    │    (cross-scenario)   │         │
│  │                      │    │                      │         │
│  │  ► Face validity     │    │  ► Inter-judge        │         │
│  │    (expert review)   │    │    agreement          │         │
│  │                      │    │    (3-model ensemble)  │         │
│  └──────────────────────┘    └──────────────────────┘         │
│                                                                │
│  ┌──────────────────────────────────────────────────┐         │
│  │          SHARED VALIDATION METRICS                │         │
│  │                                                   │         │
│  │  ► Evidence coverage: % of scores with ≥2 quotes │         │
│  │  ► Citation accuracy: quotes verified in transcript│        │
│  │  ► User experience: post-session survey (SUS)    │         │
│  │  ► Ecological validity: realism ratings          │         │
│  └──────────────────────────────────────────────────┘         │
└────────────────────────────────────────────────────────────────┘
```

### 6.2 Mode 1 Validation: Logic Assessment

#### 6.2.1 Inter-Rater Reliability (Primary)

The 3-pass evaluation system serves as a built-in inter-rater reliability check:

```python
# Per-dimension metrics
for dimension in DIMENSIONS:
    scores = [pass1[dimension], pass2[dimension], pass3[dimension]]
    metrics = {
        "median_score": statistics.median(scores),
        "score_range": max(scores) - min(scores),  # Should be ≤ 1
        "std_dev": statistics.stdev(scores),
        "agreement": "high" if max(scores) - min(scores) <= 1 else "low",
    }

# Aggregate across all sessions
# Target: ≥ 80% of dimensions have high agreement (range ≤ 1)
# If agreement is low, the rubric anchors need refinement
```

**Justification**: In consulting case interviews, inter-rater reliability is typically measured between human interviewers and is often moderate (κ = 0.4-0.6). Our 3-pass LLM system with explicit rubric anchors should achieve comparable or higher agreement because the rubric eliminates subjective interpretation variance.

#### 6.2.2 Content Validity

Verified by mapping each rubric dimension to established consulting case interview competencies:

| Our Dimension | Maps to Industry Competency | Source |
|---|---|---|
| Problem Structuring | Issue Identification & Structuring | McKinsey PEI framework |
| Hypothesis-Driven Thinking | Hypothesis-Driven Problem Solving | BCG case methodology |
| Quantitative Reasoning | Quantitative Skills | Bain case evaluation criteria |
| Data Synthesis | Insight Generation | McKinsey "so what" test |
| Recommendation Quality | Business Judgment | Industry-standard case rubric |
| Communication Clarity | Client Communication | MBB interview evaluation forms |

#### 6.2.3 Construct Independence Check

To verify that Mode 1 measures analytical ability independently of personality:

```python
# Correlate Mode 1 logic scores with BFI-44 personality scores
# Expected: LOW correlations (r < 0.3) between logic dimensions
# and personality traits.

# If high correlation found (e.g., "Communication Clarity" correlates
# with Extraversion r > 0.5), this indicates construct contamination
# and the dimension definition needs revision.

for dimension in LOGIC_DIMENSIONS:
    for trait in OCEAN_TRAITS:
        r, p = pearsonr(
            [p.logic_scores[dimension] for p in participants],
            [p.bfi44_scores[trait] for p in participants]
        )
        if abs(r) > 0.3 and p < 0.05:
            print(f"WARNING: {dimension} correlates with {trait} (r={r:.2f})")
```

### 6.3 Mode 2 Validation: Personality Assessment

#### 6.3.1 Convergent Validity (Primary)

The gold standard: do AI-inferred personality scores correlate with the candidate's BFI-44 self-report?

```python
# Per-trait convergent validity
for trait in ["O", "C", "E", "A", "N"]:
    ground_truth = [p.bfi44[trait] for p in participants]
    inferred = [p.ensemble_ocean[trait] for p in participants]
    
    r, p_val = pearsonr(ground_truth, inferred)
    mae = mean_absolute_error(ground_truth, inferred)
    bias = np.mean(np.array(inferred) - np.array(ground_truth))
    
    # Targets based on Step 1 validation results:
    # Pearson r ≥ 0.70 (acceptable), ≥ 0.80 (good)
    # MAE ≤ 0.15 (acceptable), ≤ 0.10 (good)
    # Bias: |bias| ≤ 0.10

# Known limitation from Step 1:
# Conscientiousness tends to be inflated (~+0.15 bias) in group
# discussions because organized behavior is normative in this format.
# This is documented as a structural limitation.
```

**Justification**: Self-report personality measures (BFI-44) have well-established psychometric properties (Cronbach's α = 0.75-0.90, test-retest r = 0.80+). Using BFI-44 as ground truth is standard practice in personality assessment research (John, Donahue, & Kentle, 1991; John & Srivastava, 1999).

#### 6.3.2 Discriminant Validity

Each trait's inferred score should correlate most strongly with its own BFI-44 ground truth, not with other traits:

```python
# Construct a 5x5 correlation matrix: inferred traits × ground truth traits
# Diagonal should be highest in each row and column
# Off-diagonal > 0.5 indicates poor discriminant validity

correlation_matrix = np.zeros((5, 5))
for i, inferred_trait in enumerate(OCEAN):
    for j, ground_trait in enumerate(OCEAN):
        correlation_matrix[i][j] = pearsonr(
            [p.inferred[inferred_trait] for p in participants],
            [p.bfi44[ground_trait] for p in participants]
        )[0]

# Check: diagonal > all off-diagonal in same row
for i in range(5):
    if correlation_matrix[i][i] < max(correlation_matrix[i][:i].tolist() + 
                                       correlation_matrix[i][i+1:].tolist()):
        print(f"WARNING: {OCEAN[i]} discriminant validity issue")
```

#### 6.3.3 Test-Retest Reliability (Cross-Scenario)

If a participant completes multiple group discussion scenarios, their inferred personality scores should be consistent:

```python
# For participants who complete 2+ group discussion scenarios:
for trait in OCEAN:
    scores_scenario1 = [p.inferred[trait] for p in participants if p.scenario == "resource_conflict"]
    scores_scenario2 = [p.inferred[trait] for p in participants if p.scenario == "creative_brainstorm"]
    
    # Same participant across scenarios
    paired_scores = get_paired_scores(scores_scenario1, scores_scenario2)
    icc = intraclass_correlation(paired_scores)
    
    # Target: ICC ≥ 0.60 (moderate), ≥ 0.75 (good)
```

#### 6.3.4 Inter-Judge Agreement (3-Model Ensemble)

```python
# Per-trait agreement across DeepSeek, Claude Haiku, Gemini Flash
for trait in OCEAN:
    judge_scores = {
        "deepseek": [p.judges["deepseek"][trait] for p in participants],
        "claude": [p.judges["claude"][trait] for p in participants],
        "gemini": [p.judges["gemini"][trait] for p in participants],
    }
    
    # Pairwise correlations
    for pair in combinations(judge_scores.keys(), 2):
        r = pearsonr(judge_scores[pair[0]], judge_scores[pair[1]])[0]
        # Target: r ≥ 0.70
    
    # Mean absolute difference
    for pair in combinations(judge_scores.keys(), 2):
        mad = np.mean(np.abs(
            np.array(judge_scores[pair[0]]) - np.array(judge_scores[pair[1]])
        ))
        # Target: MAD ≤ 0.15
```

### 6.4 Cross-Mode Validation

With within-subject design (same participants do both modes), we can test theoretically expected relationships:

```python
# Expected WEAK correlations (construct independence):
# Mode 1 logic scores should NOT strongly predict Mode 2 personality scores
# This confirms the two modes measure different constructs

# Expected MODERATE correlations (theoretical plausibility):
# Conscientiousness (Mode 2) may weakly predict Problem Structuring (Mode 1)
# Openness (Mode 2) may weakly predict Recommendation Quality creativity
# These are theoretically plausible but should be small (r < 0.3)
```

---

## 7. UI Visualization & HR Dashboard

### 7.1 Design Principles

The HR dashboard is designed for **non-technical hiring managers** who need to:
1. Quickly assess candidate quality (summary view)
2. Drill into specific evidence when making decisions (detail view)
3. Compare candidates against each other (comparison view)
4. Trust the assessment through transparency (evidence trail)

Every score displayed must link to **specific transcript quotes** — no "black box" scores.

### 7.2 Candidate Overview Page

```
┌─────────────────────────────────────────────────────────────────┐
│  CANDIDATE: Park Jimin                     ID: P042             │
│  Date: 2026-02-10    Sessions: 2/2 completed                   │
│                                                                 │
│  ┌─────────────────────────┐  ┌─────────────────────────────┐  │
│  │  MODE 1: CASE STUDY     │  │  MODE 2: GROUP DISCUSSION   │  │
│  │  Overall: 3.8 / 5.0     │  │  Personality Profile:       │  │
│  │  ████████████░░░░░ 76%  │  │                             │  │
│  │                         │  │  O ████████░░ 0.72           │  │
│  │  Strongest:             │  │  C ██████░░░░ 0.58           │  │
│  │  • Problem Structuring  │  │  E ████████░░ 0.75           │  │
│  │    (4/5)                │  │  A ██████████ 0.82           │  │
│  │  Development:           │  │  N ███░░░░░░░ 0.28           │  │
│  │  • Quantitative         │  │                             │  │
│  │    Reasoning (3/5)      │  │  Key Trait: High            │  │
│  │                         │  │  Agreeableness              │  │
│  │  [View Full Report →]   │  │  [View Full Report →]       │  │
│  └─────────────────────────┘  └─────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  QUICK VERDICT                                           │   │
│  │                                                          │   │
│  │  Analytical Capability: Above Average                    │   │
│  │  Interpersonal Style: Collaborative, accommodating,      │   │
│  │                       composed under pressure            │   │
│  │                                                          │   │
│  │  ⚠ Note: Quantitative reasoning below benchmark.        │   │
│  │    Consider follow-up assessment for quant-heavy roles.  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 Mode 1 Detail View: Logic Assessment Report

```
┌─────────────────────────────────────────────────────────────────┐
│  CASE STUDY ASSESSMENT — Park Jimin                             │
│  Scenario: MedDevice Market Entry | Duration: 14:32             │
│  Data Coverage: 7/10 categories requested (70%)                 │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  DIMENSION SCORES                                        │   │
│  │                                                          │   │
│  │  Problem Structuring     ████████████████░░░░ 4/5  ✓✓✓  │   │
│  │  Hypothesis Thinking     ████████████████░░░░ 4/5  ✓✓✓  │   │
│  │  Quantitative Reasoning  ████████████░░░░░░░░ 3/5  ✓✓○  │   │
│  │  Data Synthesis           ████████████████░░░░ 4/5  ✓✓✓  │   │
│  │  Recommendation Quality  ████████████░░░░░░░░ 3/5  ✓✓○  │   │
│  │  Communication Clarity   ████████████████████ 5/5  ✓✓✓  │   │
│  │                                                          │   │
│  │  ✓✓✓ = 3/3 passes agree   ✓✓○ = 2/3 passes agree      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ▼ PROBLEM STRUCTURING — Score: 4/5 (Strong)             │   │
│  │                                                          │   │
│  │  Evidence:                                               │   │
│  │                                                          │   │
│  │  📎 Turn 3: "Let me structure this as a profitability    │   │
│  │     problem — I want to look at revenue drivers and      │   │
│  │     cost drivers separately."                            │   │
│  │     → Demonstrates: Framework articulation               │   │
│  │                                                          │   │
│  │  📎 Turn 5: "Before I ask for more data, let me map      │   │
│  │     out what I need: market size, our cost position,     │   │
│  │     and competitive dynamics."                           │   │
│  │     → Demonstrates: Systematic data planning             │   │
│  │                                                          │   │
│  │  📎 Turn 11: "Coming back to my framework, I've covered  │   │
│  │     revenue and costs. Let me now look at competition."  │   │
│  │     → Demonstrates: Framework adherence                  │   │
│  │                                                          │   │
│  │  ⚠ Not observed: Did not adapt framework when cost       │   │
│  │    data revealed an unexpected pattern (Turn 8)          │   │
│  │                                                          │   │
│  │  Rubric: Scored 4 ("Strong Structure") rather than 5     │   │
│  │  because the framework was applied consistently but      │   │
│  │  not adapted when new data suggested a different angle.  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  SESSION STATISTICS                                      │   │
│  │                                                          │   │
│  │  Time to first hypothesis:  2:14  (benchmark: ~3:00)    │   │
│  │  Data categories requested:  7/10  (70%)                │   │
│  │  Hypotheses stated:          3                          │   │
│  │  Quantitative statements:    4                          │   │
│  │  Framework references:       5                          │   │
│  │  Avg words per turn:         42                         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [📄 Full Transcript]  [📊 Export PDF]  [🔗 Share Report]       │
└─────────────────────────────────────────────────────────────────┘
```

### 7.4 Mode 2 Detail View: Personality Assessment Report

```
┌─────────────────────────────────────────────────────────────────┐
│  GROUP DISCUSSION ASSESSMENT — Park Jimin                       │
│  Scenario: Resource Conflict | Duration: 12:45                  │
│  Participants: Candidate + Alex, Jordan, Riley (AI)             │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  PERSONALITY PROFILE                                     │   │
│  │                                                          │   │
│  │         Openness          ████████░░  0.72  (±0.08)     │   │
│  │   Conscientiousness       ██████░░░░  0.58  (±0.12) ⚠  │   │
│  │      Extraversion         ████████░░  0.75  (±0.05)     │   │
│  │     Agreeableness         ██████████  0.82  (±0.04)     │   │
│  │       Neuroticism         ███░░░░░░░  0.28  (±0.06)     │   │
│  │                                                          │   │
│  │  (±) = inter-judge disagreement                         │   │
│  │  ⚠  = low agreement — human review recommended          │   │
│  │                                                          │   │
│  │  Confidence: 🟢 High (4/5 traits with judge agreement)  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │       [Radar Chart: OCEAN Profile]                       │   │
│  │                                                          │   │
│  │              Openness (0.72)                             │   │
│  │                 ╱    ╲                                    │   │
│  │     Neurot.   ╱  ████  ╲   Conscient.                   │   │
│  │     (0.28)  ╱  ████████  ╲  (0.58)                      │   │
│  │             ╲  ████████  ╱                               │   │
│  │     Agree.   ╲  ████  ╱   Extravert.                    │   │
│  │     (0.82)    ╲    ╱     (0.75)                          │   │
│  │                                                          │   │
│  │  ── Inferred Profile   ⋯⋯ BFI-44 Self-Report           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ▼ AGREEABLENESS — Score: 0.82 (High) | Confidence: 🟢  │   │
│  │                                                          │   │
│  │  High Facets Detected:                                   │   │
│  │                                                          │   │
│  │  Trust (0.85):                                           │   │
│  │  📎 Turn 7: "That's a fair point, Alex. I hadn't         │   │
│  │     considered that angle."                              │   │
│  │     → Signal: HIGH trust (accepting critique gracefully) │   │
│  │                                                          │   │
│  │  Altruism (0.80):                                        │   │
│  │  📎 Turn 12: "Riley, what do you think? You've been      │   │
│  │     quiet — I'd love to hear your perspective."          │   │
│  │     → Signal: HIGH altruism (actively including others)  │   │
│  │                                                          │   │
│  │  Compliance (0.78):                                      │   │
│  │  📎 Turn 15: "I see where you're coming from. Let me     │   │
│  │     adjust my proposal to incorporate your concern."     │   │
│  │     → Signal: HIGH compliance (accommodating)            │   │
│  │                                                          │   │
│  │  Low Facets Detected:                                    │   │
│  │  Competitiveness (0.20):                                 │   │
│  │  📎 No instances of competitive behavior observed.       │   │
│  │     Candidate consistently prioritized group harmony.    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  BEHAVIORAL SUMMARY                                      │   │
│  │                                                          │   │
│  │  Strengths:                                              │   │
│  │  • Excellent conflict resolution — consistently          │   │
│  │    de-escalated disagreements with Alex                  │   │
│  │  • Inclusive leadership — actively engaged Riley          │   │
│  │  • Composed under pressure — showed no stress signals    │   │
│  │    during crisis scenario                                │   │
│  │                                                          │   │
│  │  Development Areas:                                      │   │
│  │  • May over-accommodate — never pushed back on Alex's    │   │
│  │    strongest objections (relevant for assertive roles)   │   │
│  │  • Conscientiousness signals mixed — organized in        │   │
│  │    discussion but did not impose deadlines or structure   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  DISCUSSION DYNAMICS (DialogLab-style analytics)         │   │
│  │                                                          │   │
│  │  Speaking Distribution:         Turn-Taking Pattern:     │   │
│  │  ┌─────────────────┐           ┌──────────────────┐     │   │
│  │  │ Candidate  35%  │           │ C→A→C→J→C→R→C    │     │   │
│  │  │ Alex       28%  │           │ Pattern: Candidate│     │   │
│  │  │ Jordan     22%  │           │ drives discussion │     │   │
│  │  │ Riley      15%  │           └──────────────────┘     │   │
│  │  └─────────────────┘                                    │   │
│  │                                                          │   │
│  │  Avg Words/Turn:               Phase Engagement:        │   │
│  │  Candidate: 38                 Opening:    ██░░ Low     │   │
│  │  Alex:      42                 Exploration:████ High    │   │
│  │  Jordan:    35                 Conflict:   ████ High    │   │
│  │  Riley:     12                 Resolution: ███░ Med     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [📄 Full Transcript]  [📊 Export PDF]  [🔗 Share Report]       │
└─────────────────────────────────────────────────────────────────┘
```

### 7.5 Multi-Candidate Comparison View

```
┌─────────────────────────────────────────────────────────────────┐
│  CANDIDATE COMPARISON — Batch: Feb 2026 Cohort                  │
│                                                                 │
│  Filter: [All Scenarios ▼]  Sort: [Overall Logic Score ▼]       │
│                                                                 │
│  ┌───────────┬──────┬──────┬──────┬──────┬──────┬──────────┐   │
│  │ Candidate │ PS   │ HT   │ QR   │ DS   │ RQ   │ Logic Avg│   │
│  ├───────────┼──────┼──────┼──────┼──────┼──────┼──────────┤   │
│  │ P042 Jimin│ 4    │ 4    │ 3    │ 4    │ 3    │ 3.8      │   │
│  │ P038 Sarah│ 5    │ 4    │ 4    │ 3    │ 4    │ 4.0      │   │
│  │ P051 Wei  │ 3    │ 3    │ 5    │ 4    │ 4    │ 3.8      │   │
│  │ ...       │      │      │      │      │      │          │   │
│  └───────────┴──────┴──────┴──────┴──────┴──────┴──────────┘   │
│                                                                 │
│  ┌───────────┬──────┬──────┬──────┬──────┬──────┬──────────┐   │
│  │ Candidate │  O   │  C   │  E   │  A   │  N   │ Top Trait│   │
│  ├───────────┼──────┼──────┼──────┼──────┼──────┼──────────┤   │
│  │ P042 Jimin│ 0.72 │ 0.58 │ 0.75 │ 0.82 │ 0.28 │ Agree.  │   │
│  │ P038 Sarah│ 0.85 │ 0.70 │ 0.60 │ 0.55 │ 0.40 │ Open.   │   │
│  │ P051 Wei  │ 0.45 │ 0.80 │ 0.50 │ 0.65 │ 0.35 │ Consc.  │   │
│  │ ...       │      │      │      │      │      │          │   │
│  └───────────┴──────┴──────┴──────┴──────┴──────┴──────────┘   │
│                                                                 │
│  [Click any candidate row to view full report]                  │
└─────────────────────────────────────────────────────────────────┘
```

### 7.6 Implementation: Streamlit Components

```python
# Key visualization libraries
# - plotly: Radar charts, bar charts, scatter plots
# - streamlit: Layout, tabs, expanders, metrics
# - custom CSS: Scrollable panels, sticky headers, color coding

def render_candidate_report(participant_id: str):
    """Main HR dashboard view for a single candidate."""
    
    data = load_participant_data(participant_id)
    
    # Header with summary metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Logic Score", f"{data.logic_avg:.1f}/5.0")
    col2.metric("Personality Confidence", f"{data.trait_confidence:.0%}")
    col3.metric("Sessions Completed", f"{data.sessions_completed}/2")
    
    # Two-tab layout
    tab1, tab2 = st.tabs(["Case Study Results", "Group Discussion Results"])
    
    with tab1:
        render_logic_assessment(data.case_results)
    
    with tab2:
        render_personality_assessment(data.group_results)


def render_logic_assessment(case_data):
    """Mode 1 results with evidence drill-down."""
    
    # Dimension scores bar chart
    fig = px.bar(
        x=DIMENSION_NAMES, y=case_data.scores,
        color=case_data.scores,
        color_continuous_scale=["red", "yellow", "green"],
        range_y=[0, 5],
    )
    st.plotly_chart(fig)
    
    # Evidence expanders per dimension
    for dim in DIMENSIONS:
        agreement_icon = "✓✓✓" if case_data[dim].agreement == "high" else "✓✓○"
        with st.expander(f"{dim.title()} — {case_data[dim].score}/5 {agreement_icon}"):
            for ev in case_data[dim].evidence:
                st.markdown(f"""
                > 📎 **Turn {ev.turn_number}**: "{ev.quote}"  
                > → *{ev.demonstrates}*
                """)
            if case_data[dim].absent_behaviors:
                st.warning("Not observed: " + "; ".join(case_data[dim].absent_behaviors))


def render_personality_assessment(group_data):
    """Mode 2 results with radar chart and trait evidence."""
    
    # Radar chart: inferred vs BFI-44 ground truth
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[group_data.ocean[t] for t in OCEAN],
        theta=OCEAN_LABELS, fill='toself', name='AI Inferred'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[group_data.bfi44[t] for t in OCEAN],
        theta=OCEAN_LABELS, fill='toself', name='BFI-44 Self-Report',
        line=dict(dash='dot')
    ))
    st.plotly_chart(fig)
    
    # Trait evidence expanders
    for trait in OCEAN:
        confidence = group_data.confidence[trait]
        icon = "🟢" if confidence > 0.7 else "🟡" if confidence > 0.4 else "🔴"
        with st.expander(f"{trait} — {group_data.ocean[trait]:.2f} {icon}"):
            for facet in group_data.facets[trait]:
                st.markdown(f"**{facet.name}** ({facet.score:.2f})")
                for ev in facet.evidence[:3]:
                    st.markdown(f'> Turn {ev.turn_number}: "{ev.quote}"')
```

---

## 8. Implementation Plan

### 8.1 Phase 1: Mode 1 Refactoring (Week 1-2)

| Task | Description | Priority | Effort |
|------|-------------|----------|--------|
| 1.1 | Strip Provoker/Mediator agents from Case Study engine. Keep only Facilitator. | P0 | 2 days |
| 1.2 | Harden Facilitator prompt (data clerk only, no guidance). Port existing `_build_gated_context()` strict rules. | P0 | 1 day |
| 1.3 | Design 6-dimension logic rubric with 5-level anchors. Validate with 2-3 practice cases. | P0 | 2 days |
| 1.4 | Implement `LogicEvaluator` with 3-pass citation-based evaluation. Build on existing `ValidatorAgent` pattern. | P0 | 3 days |
| 1.5 | Compute session behavioral statistics (time-to-hypothesis, data coverage, etc.). | P1 | 1 day |
| 1.6 | Build Mode 1 UI results page with evidence expanders. | P1 | 2 days |
| 1.7 | Run 5 pilot sessions. Verify rubric calibration and evidence quality. | P0 | 1 day |

### 8.2 Phase 2: Mode 2 Development (Week 3-5)

| Task | Description | Priority | Effort |
|------|-------------|----------|--------|
| 2.1 | Design 3 agent profiles (Assertive, Supportive, Skeptical) with fixed BFI vectors. Validate trait expression using Step 1 methodology. | P0 | 2 days |
| 2.2 | Design 4 behavioral scenarios with phase structures (snippets). | P0 | 2 days |
| 2.3 | Implement `GroupEngine` extending current `SmartLiveEngine`. Replace competency-tracking with trait-coverage-tracking. | P0 | 4 days |
| 2.4 | Implement `TraitElicitationSelector` for strategic speaker selection. | P0 | 2 days |
| 2.5 | Implement trait-specific evidence extraction prompt with calibration notes. | P0 | 2 days |
| 2.6 | Integrate existing `FacetDetector` (28-facet) and `EnsembleDetector` (3-model) for post-session analysis. | P1 | 1 day |
| 2.7 | Build Mode 2 UI results page with radar chart and trait evidence. | P1 | 2 days |
| 2.8 | Run 5 pilot sessions. Verify trait elicitation and evidence quality. | P0 | 2 days |

### 8.3 Phase 3: Validation & Dashboard (Week 6-7)

| Task | Description | Priority | Effort |
|------|-------------|----------|--------|
| 3.1 | Implement within-subject study flow (Mode 1 → Mode 2 or vice versa, counterbalanced). | P0 | 2 days |
| 3.2 | Build validation analysis script for Mode 1 (inter-rater reliability, construct independence). | P0 | 2 days |
| 3.3 | Build validation analysis script for Mode 2 (convergent validity, discriminant validity, test-retest). | P0 | 2 days |
| 3.4 | Build HR comparison dashboard with multi-candidate table view. | P1 | 2 days |
| 3.5 | Build PDF export for candidate reports. | P2 | 1 day |
| 3.6 | Run full pilot study (N=10-15) to verify both modes end-to-end. | P0 | 3 days |

### 8.4 Phase 4: Main Study & Analysis (Week 8-10)

| Task | Description | Priority | Effort |
|------|-------------|----------|--------|
| 4.1 | Recruit N=30-50 participants for main study (within-subject, both modes). | P0 | Ongoing |
| 4.2 | Run main study sessions. | P0 | 1-2 weeks |
| 4.3 | Run validation analyses. Generate all metrics. | P0 | 3 days |
| 4.4 | Write thesis results and discussion chapters. | P0 | 1 week |

### 8.5 File Structure

```
pressure_cooker/
├── step2/
│   ├── engines/
│   │   ├── case_engine.py          # Mode 1: 1-on-1 case study engine
│   │   ├── group_engine.py         # Mode 2: 1-to-many group discussion engine
│   │   └── base_engine.py          # Shared base class (timer, TTS, state)
│   ├── agents/
│   │   ├── facilitator_agent.py    # Mode 1: Data clerk facilitator
│   │   ├── group_agents.py         # Mode 2: Alex, Jordan, Riley
│   │   └── trait_selector.py       # Mode 2: Trait-elicitation speaker selection
│   ├── evaluation/
│   │   ├── logic_evaluator.py      # Mode 1: 6-dimension rubric evaluation
│   │   ├── trait_evaluator.py      # Mode 2: Evidence-based OCEAN inference
│   │   ├── validation_mode1.py     # Mode 1: Inter-rater, content, construct checks
│   │   ├── validation_mode2.py     # Mode 2: Convergent, discriminant, test-retest
│   │   └── cross_mode_analysis.py  # Cross-mode construct independence check
│   ├── ui/pages/
│   │   ├── mode_select_page.py     # Mode selection + counterbalancing
│   │   ├── case_interview_page.py  # Mode 1 UI (simplified from current)
│   │   ├── group_discussion_page.py # Mode 2 UI (new)
│   │   ├── results_page.py         # Combined results dashboard
│   │   └── admin_page.py           # HR manager comparison view
│   └── scenarios/
│       ├── case_studies/           # Mode 1: Business cases with gated data
│       └── group_scenarios/        # Mode 2: Behavioral situation scenarios
├── pipeline/
│   ├── facet_detector.py           # Reused from current Step 2
│   ├── ensemble_detector.py        # Reused from current Step 2
│   └── evidence_extractor.py       # NEW: Shared citation extraction
└── config/
    ├── logic_rubric.py             # Mode 1: 6-dimension × 5-level rubric
    ├── group_agent_profiles.py     # Mode 2: Fixed agent personality profiles
    └── group_scenarios.py          # Mode 2: Scenario definitions with phases
```

---

## 9. Academic Justification & Evidence Base

### 9.1 Key References to Cite

| Reference | Relevance to This Work |
|---|---|
| **Hu et al. (UIST 2025)** — DialogLab | Framework for multi-party human-AI conversations; snippet-based phase management; human control mode superiority; verification analytics |
| **Arthur et al. (2003)** — AC dimension meta-analysis | Establishes that Assessment Center group exercises predict job performance and correlate with Big Five traits |
| **Lievens & Conway (2001)** — AC construct validity | Explains method-construct confound; justifies separating logical assessment from personality assessment |
| **Thornton & Gibbons (2009)** — AC theory & practice | Comprehensive guide to Assessment Center methodology including Leaderless Group Discussion |
| **John & Srivastava (1999)** — Big Five trait theory | BFI-44 psychometric properties; theoretical framework for personality assessment |
| **Park et al. (UIST 2023)** — Generative Agents | Precedent for LLM-based agents simulating human behavior in social interactions |
| **Sacks, Schegloff & Jefferson (1974)** — Turn-taking | Theoretical foundation for conversation dynamics in multi-party settings |

### 9.2 Research Questions This Architecture Enables

**RQ1**: Can an AI-facilitated 1-on-1 case study interview produce reliable assessments of logical/analytical thinking, as measured by inter-rater reliability across 3 LLM evaluation passes?

**RQ2**: Can a multi-party group discussion with AI agents produce personality trait estimates that converge with BFI-44 self-report scores (convergent validity)?

**RQ3**: Do the two assessment modes measure distinct constructs, as evidenced by low cross-mode correlations (construct independence)?

**RQ4**: How do candidates perceive the realism and fairness of AI-simulated interviews compared to expectations of human-led interviews?

### 9.3 Expected Contributions

1. **Methodological**: First system to apply DialogLab's multi-party conversation framework specifically to personality assessment, with empirically validated AI agent trait consistency.

2. **Technical**: Evidence-based evaluation architecture where every assessment score is traceable to specific transcript quotes, enabling transparent and auditable candidate evaluation.

3. **Empirical**: Validation data demonstrating the convergent validity of AI-inferred personality traits from group discussions, and the reliability of AI-evaluated logical reasoning from case studies.

4. **Applied**: A practical dual-mode interview platform that HR managers can use to assess candidates on both cognitive and personality dimensions, with full transparency into the evidence behind each score.

---

## Appendix A: DialogLab Concept Mapping

| DialogLab Concept | Our Mode 2 Implementation |
|---|---|
| **Group** (top-level container) | Group Discussion session |
| **Party** (sub-group with roles) | Not used — all agents are peers (leaderless design) |
| **Elements** (participants + content) | 3 AI agents + 1 human candidate + scenario brief |
| **Snippet** (conversation phase) | Phase definitions per scenario (5-6 phases each) |
| **Interaction Pattern** (neutral/agree/disagree) | Phase-specific style configuration |
| **Turn-Taking Mode** (free/moderated/round-robin) | Free mode — no moderation, natural turn-taking |
| **Human Agent** (simulated human mode) | N/A — the human IS the candidate being assessed |
| **Human Control Mode** | Our hybrid: candidate has free input, AI strategically selects responder |
| **Verification Dashboard** | HR Dashboard with turn-taking distribution, sentiment, trait evidence |
| **Inspector Panel** (agent configuration) | Agent profile configuration with BFI vectors and behavioral instructions |
| **Interruptions** | Not implemented in V3 text-based format (future: voice-based) |
| **Backchannels** | Partially implemented via short acknowledgment responses from agents |

---

*End of Document*
