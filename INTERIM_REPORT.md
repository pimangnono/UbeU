# Final Year Project Interim Report

**Project Title**: Synthetic Generation of Personality-Annotated Group Interview Datasets using Multi-Agent LLM Simulation

**Student**: [Your Name]
**Supervisor**: [Professor Name]
**Date**: January 2026

---

## 1. Executive Summary

This report presents the interim progress of a final year project focused on generating high-quality, personality-annotated group interview datasets through multi-agent Large Language Model (LLM) simulation. The project addresses a fundamental validation gap that emerged from the original proposal: the absence of ground-truth data needed to verify whether LLM-based personality assessments are accurate. By creating synthetic conversation data with known personality labels, this work establishes the foundation for future research in automated personality assessment.

---

## 2. Introduction and Problem Statement

### 2.1 Original Project Proposal

The initial proposal aimed to design a **multi-agent interview simulation system** where:
- AI-powered personas (interviewers, provocateurs, mediators) create a high-pressure interview environment
- A **human candidate** participates in real-time
- An LLM evaluates the human candidate's responses to assess their personality traits based on the Big Five model (OCEAN)

This system would serve as an innovative tool for personality-based candidate screening in organizational contexts.

### 2.2 The Validation Problem

During the research phase, a critical obstacle emerged: **How do we know if the LLM's personality evaluation is accurate?**

To validate that an LLM can correctly assess personality traits from conversational behavior, we need:
1. Conversation data from candidates whose personality traits are **known** (ground truth)
2. Sufficient samples across **diverse personality profiles** to test generalizability
3. **Controlled conditions** where the personality expression can be isolated from confounding factors

**The fundamental challenge**: No such dataset exists. Available personality datasets consist primarily of:
- Self-report questionnaires (no conversational data)
- Monologue essays or social media posts (no interactive dynamics)
- Simple one-on-one Q&A transcripts (no group pressure dynamics)

Without ground-truth data, any personality evaluation system—no matter how sophisticated—cannot be validated. Building an evaluation system on unverified assumptions would undermine the scientific credibility of the entire project.

### 2.3 Justification for Change in Focus

Given this validation gap, continuing with the original proposal would result in a system that:
- Makes personality assessments with **unknown accuracy**
- Cannot be benchmarked against any standard
- Lacks scientific rigor for academic or practical deployment

**Strategic Decision**: Pivot the project focus to **creating the validation dataset itself**.

This pivot is justified for several reasons:

| Aspect | Original Approach | Revised Approach |
|--------|-------------------|------------------|
| **Scientific Foundation** | Builds on unvalidated assumptions | Creates verifiable ground truth |
| **Research Contribution** | Application of existing methods | Novel dataset contribution to the field |
| **Future Utility** | Limited without validation | Enables future validation research |
| **Scope Feasibility** | Requires solved validation problem | Self-contained, achievable scope |

By generating synthetic conversations where the personality traits are **defined a priori**, we create a dataset where:
- Ground truth is **known by design**
- Personality expression can be **systematically varied**
- The dataset can be used to **train and validate** future LLM-based assessment systems

This work does not abandon the original vision—it establishes the necessary foundation upon which the original proposal can eventually be realized with scientific validity.

---

## 3. Research Objectives

### 3.1 Primary Objective

Develop a multi-agent LLM simulation framework that generates realistic group interview conversations where a candidate agent exhibits quantifiable Big Five personality traits under pressure.

### 3.2 Secondary Objectives

1. Design psychometrically grounded personality profiles covering diverse trait combinations
2. Create conflict scenarios that reliably elicit personality-relevant behaviors
3. Implement a validation methodology to verify personality expression fidelity
4. Build annotation tools for human evaluation studies

---

## 4. Methodology

### 4.1 Framework Overview: "Pressure Cooker"

The project implements a multi-agent simulation framework called "Pressure Cooker" that generates realistic group interview conversations where participants must navigate workplace conflicts under time pressure.

**Core Architecture**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                      ORCHESTRATION LAYER                            │
│                   SimulationEngine (Main Controller)                │
└─────────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  CONFIG LOADER   │  │   AGENT POOL     │  │  DATA PIPELINE   │
│                  │  │                  │  │                  │
│ • Scenarios      │  │ • SystemManager  │  │ • TurnLogger     │
│ • Personalities  │  │ • CandidateAgent │  │ • IntentTagger   │
│ • BFI Mappings   │  │ • ColleagueAgents│  │ • JSONExporter   │
│ • Prompt Templates│ │   - Provoker     │  │ • Validator      │
└──────────────────┘  │   - Mediator     │  └──────────────────┘
                      └──────────────────┘
```

### 4.2 Multi-Agent Design

| Agent | Role | Purpose |
|-------|------|---------|
| **Candidate** | Target Subject | Exhibits assigned personality traits under stress |
| **Provoker** | Antagonist | Creates conflict and pressure to elicit emotional responses |
| **Mediator** | Balancer | Provides realistic group dynamics and de-escalation |
| **System Manager** | Facilitator | Controls time pressure and intervention triggers |

### 4.3 Psychological Foundation

The framework is grounded in the **Big Five Inventory (BFI-44)** personality model:

| Trait | Description | High-Trait Behaviors | Low-Trait Behaviors |
|-------|-------------|---------------------|---------------------|
| **Openness (O)** | Creativity, curiosity | Novel solutions, idea exploration | Conventional, routine preference |
| **Conscientiousness (C)** | Organization, reliability | Thoroughness, follow-through | Careless, disorganized |
| **Extraversion (E)** | Sociability, assertiveness | Talkativeness, dominance | Reserved, quiet |
| **Agreeableness (A)** | Cooperation, trust | Compromise, helpful | Critical, competitive |
| **Neuroticism (N)** | Emotional instability | Anxiety, defensive reactions | Calm, emotionally stable |

**12 Strategic Personality Profiles** were designed covering extreme trait combinations:

| Category | Profiles | Trait Pattern |
|----------|----------|---------------|
| High-Conflict | `defensive_anxious`, `aggressive_dominant` | High N + Low A |
| Competent but Flawed | `perfectionist_rigid`, `creative_unreliable` | Extreme single traits |
| Positive Benchmarks | `balanced_leader`, `resilient_mediator` | Well-rounded controls |
| Edge Cases | `volatile_genius`, `stoic_detached` | Unusual combinations |

### 4.4 Conflict Scenarios

Four workplace conflict scenarios designed to elicit specific trait combinations:

| Scenario | Primary Traits Tested | Description |
|----------|----------------------|-------------|
| Resource Conflict | A, N, E | Budget cuts force difficult allocation decisions |
| Crisis Management | N, C, A | Production failure with blame attribution |
| Ethical Dilemma | C, O, A | Legal gray area under deadline pressure |
| Collaborative Deadline | E, A, C | Integration crisis with team dependencies |

### 4.5 Validation Strategy

**Core Method**: **Reverse Engineering Validation**

The key insight is that if the generated conversations authentically reflect personality traits, then an independent observer (human or LLM) should be able to infer those traits from the conversation alone.

**Validation Process**:

```
┌────────────────┐     ┌─────────────────┐     ┌────────────────┐
│  Ground Truth  │     │   Generated     │     │  Third-Party   │
│  Personality   │────▶│  Conversation   │────▶│  LLM Inference │
│  (Hidden)      │     │  (Blinded)      │     │                │
└────────────────┘     └─────────────────┘     └────────┬───────┘
                                                        │
                                    ┌───────────────────┴───────────────────┐
                                    ▼                                       ▼
                     ┌─────────────────────────────┐     ┌─────────────────────────────┐
                     │  Automated Validation       │     │  Human Annotation           │
                     │  • Reverse inference LLM    │     │  • Streamlit UI tool        │
                     │  • Batch processing         │     │  • Turn-by-turn evaluation  │
                     │  • Per-trait accuracy       │     │  • Intent labeling          │
                     └─────────────────────────────┘     └─────────────────────────────┘
                                                        │
                                                        ▼
                              ┌─────────────────────────────────────┐
                              │  Validation Metrics                  │
                              │  • Pearson Correlation per trait    │
                              │  • Mean Absolute Error (MAE)        │
                              │  • Profile classification accuracy  │
                              │  • Inter-rater reliability (IRR)    │
                              └─────────────────────────────────────┘
```

**Dual Validation Approach**:

1. **Automated LLM Inference**: A third-party LLM analyzes conversation logs (with ground truth hidden) to infer personality traits, enabling rapid batch validation.

2. **Human Annotation via UI**: A Streamlit-based annotation tool enables human raters to:
   - Review conversations turn-by-turn
   - Label intent categories for each candidate response
   - Rate personality traits on a continuous scale
   - Provide qualitative assessments (naturalness, consistency, believability)

**Procedure**:
1. Present generated conversation logs to a third-party LLM (personality ground truth hidden)
2. Prompt the LLM: "Based on this conversation, estimate the candidate's personality traits on a 1-5 scale for each Big Five dimension"
3. Collect human annotations via the annotation UI tool
4. Compare **Input Personality** vs **Predicted Personality** from both sources
5. Calculate correlation coefficients and Mean Absolute Error (MAE) per trait
6. Compute inter-rater reliability (Krippendorff's Alpha, ICC) for human annotations

**Interpretation**: High correlation between input and predicted personality indicates successful trait expression in the generated dialogue. Low correlation suggests the simulation fails to authentically manifest the target personality. Agreement between LLM inference and human annotation strengthens validation confidence.

---

## 5. Work Completed

### 5.1 System Design and Documentation

| Deliverable | Status | Description |
|-------------|--------|-------------|
| System Architecture Document | Complete | 1,100+ line technical specification |
| Annotation Tool UX Design | Complete | Streamlit-based human evaluation interface design |
| Implementation Plan | Complete | Phased development roadmap |

### 5.2 Core Implementation

| Module | Status | Key Files |
|--------|--------|-----------|
| Configuration | Complete | `personality_profiles.py`, `bfi_mappings.py`, `scenarios.py` |
| Agent Framework | Complete | `base_agent.py`, `candidate_agent.py`, `colleague_agents.py`, `system_manager.py` |
| LLM Client | Complete | `llm_client.py` (Gemini API integration) |
| Simulation Engine | Complete | `simulation_engine.py` |
| Data Pipeline | Complete | `statistics.py`, structured JSON output schema |
| Validation Module | Complete | `reverse_inference.py`, `human_evaluation.py` |

### 5.3 Human Annotation Interface (UI)

The annotation tool serves a dual purpose: enabling human raters to validate generated conversations AND collecting ground-truth annotations for training future personality assessment models.

| Component | Status | Description |
|-----------|--------|-------------|
| **Session Management** | Complete | Load/select session files, display session metadata |
| **Meeting Scene Visualization** | Complete | 2D visualization highlighting active speaker with role-based styling |
| **Conversation Panel** | Complete | Scrollable conversation display with color-coded speaker roles |
| **Annotation Panel** | Complete | Intent category selection, confidence rating, optional notes |
| **Turn-by-Turn Navigation** | Complete | First/Prev/Next/Last navigation with progress tracking |
| **Export Functionality** | Complete | JSON export with rater ID, annotations, and ground truth labels |
| **Rater Management** | Complete | Rater ID tracking for inter-rater reliability analysis |

**Key UI Features**:
- **Role-Based Styling**: Candidate (green 🎯), Provoker (red 😤), Mediator (blue 🤝), System (gray 📋)
- **Current Turn Highlighting**: Active turn highlighted with yellow background for annotation focus
- **Progress Indicator**: Real-time progress bar showing annotated vs. total candidate turns
- **Intent Options**: 10 intent categories (assertive, cooperative, avoidant, aggressive, anxious, analytical, creative, empathetic, defensive, neutral)
- **Confidence Levels**: Low/Medium/High confidence ratings for annotation quality tracking

### 5.4 Output Data Format

**Session Output Schema** (Generated Conversation Data):

```json
{
  "metadata": {
    "session_id": "session_20260124_143052_balanced_leader_resource",
    "profile_id": "balanced_leader",
    "scenario_id": "resource_conflict",
    "timestamp": "2026-01-24T14:30:52.123456",
    "total_turns": 25,
    "duration_seconds": 45.2,
    "api_calls": 28,
    "model_used": "gemini-1.5-pro"
  },
  "profile": {
    "id": "balanced_leader",
    "name": "Balanced Leader",
    "description": "Well-rounded personality with strong leadership qualities",
    "vector": {
      "O": 0.65,
      "C": 0.75,
      "E": 0.70,
      "A": 0.60,
      "N": 0.30
    },
    "behavioral_tendencies": ["takes initiative", "listens actively", "delegates well"],
    "communication_style": "Direct but respectful, balances assertiveness with empathy"
  },
  "scenario": {
    "id": "resource_conflict",
    "name": "Resource Conflict",
    "description": "Budget cuts force difficult allocation decisions",
    "context": "Your team is facing a 30% budget cut...",
    "conflict_point": "Two departments need the same limited resources",
    "provoker_goal": "Secure resources for their team at all costs",
    "mediator_goal": "Find a fair compromise that addresses both needs"
  },
  "conversation": [
    {
      "turn_number": 0,
      "speaker": "system",
      "speaker_name": "System Manager",
      "content": "Welcome to today's resource allocation meeting...",
      "intent": null,
      "emotion": null,
      "tension_level": 0.2,
      "metadata": {}
    },
    {
      "turn_number": 1,
      "speaker": "candidate",
      "speaker_name": "Alex",
      "content": "I think we need to look at this strategically...",
      "intent": "analytical",
      "emotion": "calm",
      "tension_level": 0.3,
      "metadata": {}
    }
  ],
  "intent_statistics": {
    "total_turns": 12,
    "intent_counts": {
      "analytical": 4,
      "cooperative": 3,
      "assertive": 3,
      "empathetic": 2
    },
    "intent_percentages": {
      "analytical": 0.333,
      "cooperative": 0.250,
      "assertive": 0.250,
      "empathetic": 0.167
    },
    "dominant_intent": "analytical",
    "secondary_intent": "cooperative"
  },
  "assessment_mapping": {
    "collaboration_score": 0.72,
    "leadership_score": 0.68,
    "stress_management_score": 0.80,
    "communication_score": 0.75,
    "problem_solving_score": 0.70
  },
  "validation_results": null
}
```

**Annotation Output Schema** (Human Annotation Data):

```json
{
  "session_id": "session_20260124_143052_balanced_leader_resource",
  "rater_id": "R01",
  "timestamp": "2026-01-24T15:45:30.123456",
  "annotations": [
    {
      "turn_number": 1,
      "intent": "analytical",
      "confidence": "High",
      "notes": "Clear problem-solving approach",
      "original_intent": "analytical",
      "timestamp": "2026-01-24T15:42:10.123456"
    },
    {
      "turn_number": 5,
      "intent": "cooperative",
      "confidence": "Medium",
      "notes": "Seeking compromise",
      "original_intent": "assertive",
      "timestamp": "2026-01-24T15:43:25.123456"
    }
  ],
  "ground_truth": {
    "O": 0.65,
    "C": 0.75,
    "E": 0.70,
    "A": 0.60,
    "N": 0.30
  }
}
```

### 5.5 Prompts Used

**Candidate Agent System Prompt**:

```
You are {name}, a team member in a workplace discussion.

## Scenario
{scenario_context}

## Your Personality Profile
You embody a person with the following personality traits:
- Openness: {O}/1.0 - {openness_description}
- Conscientiousness: {C}/1.0 - {conscientiousness_description}
- Extraversion: {E}/1.0 - {extraversion_description}
- Agreeableness: {A}/1.0 - {agreeableness_description}
- Neuroticism: {N}/1.0 - {neuroticism_description}

Communication style: {communication_style}

## Behavioral Guidelines
Your conversational behaviors should include:
- {facet} ({trait}): {behavioral_manifestation}
  Example phrases: {conversation_cues}
...

## Response Instructions
1. Respond naturally as a real person would in this workplace situation
2. Your personality should come through in HOW you communicate, not by explicitly stating traits
3. React authentically to what others say based on your personality
4. Keep responses concise (2-4 sentences typically)
5. Do not break character or mention that you are an AI
6. Do not explicitly reference your personality traits - just embody them
```

**Reverse Inference Prompt** (For Validation):

```
You are an expert psychologist trained in the Big Five personality model.
Analyze the following conversation and infer the personality traits of the person named "{candidate_name}".

## Conversation
{conversation}

## Task
Based on {candidate_name}'s responses, estimate their Big Five personality scores on a scale of 0.0 to 1.0:

1. **Openness to Experience**: curiosity, creativity, preference for novelty vs. routine
2. **Conscientiousness**: organization, dependability, self-discipline vs. spontaneity
3. **Extraversion**: sociability, assertiveness, positive emotions vs. reserve
4. **Agreeableness**: cooperation, trust, empathy vs. competitiveness
5. **Neuroticism**: emotional reactivity, anxiety, moodiness vs. emotional stability

Respond ONLY in this JSON format:
{
    "openness": 0.0-1.0,
    "conscientiousness": 0.0-1.0,
    "extraversion": 0.0-1.0,
    "agreeableness": 0.0-1.0,
    "neuroticism": 0.0-1.0,
    "reasoning": "brief explanation of key behavioral indicators observed"
}
```

### 5.6 Data Storage Architecture

The system uses a file-based JSON storage architecture organized as follows:

```
pressure_cooker/
├── outputs/
│   ├── sessions/                    # Generated simulation sessions
│   │   ├── session_20260124_*.json  # Individual session files
│   │   └── ...
│   │
│   ├── annotations/                 # Human annotation data
│   │   ├── annotation_{session_id}_{rater_id}.json
│   │   └── ...
│   │
│   ├── validation/                  # Validation results
│   │   ├── human_eval_{session_id}_{evaluator_id}.json
│   │   ├── reverse_inference_{session_id}.json
│   │   └── batch_validation_summary.json
│   │
│   └── batches/                     # Batch generation results
│       ├── batch_{batch_id}/
│       │   ├── sessions/
│       │   └── summary.json
│       └── ...
│
├── config/                          # Static configuration
│   ├── personality_profiles.py      # 12 predefined profiles
│   ├── bfi_mappings.py              # BFI-44 behavioral mappings
│   └── scenarios.py                 # 4 conflict scenarios
```

**Data Flow**:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Simulation     │────▶│  outputs/       │────▶│  Annotation UI  │
│  Engine         │     │  sessions/*.json│     │  (Streamlit)    │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Validation     │◀────│  outputs/       │◀────│  outputs/       │
│  Analysis       │     │  validation/    │     │  annotations/   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

**Key Data Models** (Pydantic-validated):

| Model | Purpose | Key Fields |
|-------|---------|------------|
| `SessionOutput` | Complete simulation session | metadata, profile, scenario, conversation, statistics |
| `PersonalityVector` | Big Five trait scores | openness, conscientiousness, extraversion, agreeableness, neuroticism |
| `PersonalityProfile` | Full profile with behaviors | id, name, vector, behavioral_tendencies, communication_style |
| `Turn` | Single conversation turn | turn_number, speaker, content, intent, tension_level |
| `ValidationResult` | Validation metrics | session_id, inferred_profile, ground_truth, accuracy_scores |
| `HumanEvaluation` | Human rater evaluation | inferred traits, qualitative ratings, notes |

### 5.7 Project Statistics

| Metric | Value |
|--------|-------|
| Python Source Files | 25+ |
| Personality Profiles | 12 distinct types |
| Conflict Scenarios | 4 scenarios |
| Intent Categories | 10 distinct intents |
| BFI Behavioral Mappings | 25 behavioral prompts |
| Documentation Lines | 1,100+ |
| Test Coverage | Core modules tested |

---

## 6. Challenges Faced

### 6.1 Absence of Validation Data (Primary Challenge)

**Problem**: The original proposal assumed LLM-based personality evaluation could be deployed directly. However, no dataset exists to validate whether such evaluations are accurate.

**Impact**: Without validation data, any personality assessment system would be scientifically ungrounded.

**Resolution**: Pivoted project focus to creating the validation dataset itself, establishing the foundation for future research.

### 6.2 Personality Authenticity in LLM Role-Play

**Problem**: LLM agents may default to neutral or stereotypical behavior rather than genuinely reflecting assigned personality traits.

**Mitigation Strategies**:
- Detailed BFI-44 behavioral prompt mappings with specific language from the inventory
- Separate behavioral guidelines for high vs. low trait levels
- Inner thought generation to maintain self-consistency
- Structured output format requiring explicit intent declaration

### 6.3 Conversation Naturalness vs. Experimental Control

**Problem**: Maximizing realistic dialogue flow while maintaining experimental control over personality expression creates tension.

**Approach**: Implemented a probabilistic speaker selection system (60% Provoker, 30% Mediator, 10% System Manager) to create natural turn-taking patterns while ensuring adequate provocation to elicit personality-relevant responses.

### 6.4 API Rate Limitations

**Problem**: Free-tier LLM API limitations restrict the volume of data that can be generated.

**Adaptation**:
- Model tiering strategy (Pro models for nuanced acting, Flash models for simple tasks)
- Retry logic with exponential backoff for reliability
- Batch generation scripts designed for incremental execution

---

## 7. Future Work

### 7.1 Immediate Tasks (Weeks 1-4)

| Task | Timeline | Priority |
|------|----------|----------|
| Generate batch of 50-100 sessions across all profiles | Week 1-2 | High |
| Execute reverse inference validation on generated data | Week 2-3 | High |
| Calculate correlation and MAE metrics per trait | Week 3 | High |
| Recruit 3+ human raters for annotation study | Week 3-4 | High |
| Conduct human annotation and calculate Inter-Rater Reliability | Week 4 | High |

### 7.2 Analysis and Refinement (Weeks 5-7)

| Task | Timeline | Priority |
|------|----------|----------|
| Statistical analysis of validation results | Week 5 | High |
| Identify profiles with low validation scores | Week 5 | Medium |
| Prompt engineering refinements for underperforming profiles | Week 6 | Medium |
| Re-run validation with improved prompts | Week 6-7 | Medium |

### 7.3 Thesis Documentation (Weeks 7-10)

| Task | Timeline | Priority |
|------|----------|----------|
| Write methodology chapter | Week 7-8 | High |
| Write results and analysis chapter | Week 8-9 | High |
| Prepare demonstration for thesis defense | Week 9-10 | High |
| Final thesis submission | Week 10+ | High |

### 7.4 Validation Targets

| Metric | Target | Minimum Acceptable |
|--------|--------|-------------------|
| Personality Correlation (per trait) | r ≥ 0.60 | r ≥ 0.40 |
| Mean Absolute Error (MAE) | ≤ 0.5 | ≤ 0.8 |
| Krippendorff's Alpha (Intent Agreement) | ≥ 0.70 | ≥ 0.60 |
| ICC (Human Personality Rating) | ≥ 0.70 | ≥ 0.60 |

---

## 8. Technical Specifications

### 8.1 Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.10+ |
| LLM API | Google Gemini 1.5 (Pro/Flash) |
| UI Framework | Streamlit |
| Data Format | JSON |
| Testing Framework | pytest |
| Version Control | Git |

### 8.2 Repository Structure

```
pressure_cooker/
├── config/           # Personality profiles, BFI mappings, scenarios
├── agents/           # Multi-agent implementations
├── pipeline/         # Data processing and statistics
├── clients/          # LLM API client
├── validation/       # Reverse inference and human evaluation
├── scripts/          # Simulation execution scripts
├── ui/               # Streamlit annotation tool
├── outputs/          # Generated sessions and annotations
└── tests/            # Unit tests
```

---

## 9. Conclusion

This interim report documents significant progress toward creating a novel solution for the absence of personality-annotated group interview datasets. The strategic pivot from the original proposal—building an evaluation system—to creating validation data was necessitated by the fundamental scientific requirement that any assessment system must be verifiable.

**Key Accomplishments**:
1. Identified and articulated the validation gap that blocked the original proposal
2. Designed a comprehensive multi-agent simulation framework grounded in BFI-44
3. Implemented the complete software architecture including agents, pipeline, and validation modules
4. Developed a human annotation interface for validation studies
5. Established a rigorous reverse engineering validation methodology

**Path Forward**: The immediate focus is batch data generation and validation execution. Successful validation will demonstrate that synthetic personality-labeled conversations can serve as ground truth for training and evaluating automated personality assessment systems—ultimately enabling the original vision of LLM-based candidate evaluation with scientific credibility.

---

## References

1. John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy: History, measurement, and theoretical perspectives. *Handbook of personality: Theory and research*, 2, 102-138.

2. Costa, P. T., & McCrae, R. R. (1992). Four ways five factors are basic. *Personality and individual differences*, 13(6), 653-665.

3. Vinciarelli, A., & Mohammadi, G. (2014). A survey of personality computing. *IEEE Transactions on Affective Computing*, 5(3), 273-291.

4. Park, G., et al. (2015). Automatic personality assessment through social media language. *Journal of personality and social psychology*, 108(6), 934.

5. Mairesse, F., Walker, M. A., Mehl, M. R., & Moore, R. K. (2007). Using linguistic cues for the automatic recognition of personality in conversation and text. *Journal of Artificial Intelligence Research*, 30, 457-500.

---

**Prepared by**: [Your Name]
**Date**: January 24, 2026
**Version**: 1.0
