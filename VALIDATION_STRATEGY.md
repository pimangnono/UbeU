# UbeU Validation Strategy: 3-Step Pipeline

## Overview

This document outlines the validation pipeline for UbeU's multi-agent group interview platform. The core question: **can we trust this system to assess personality traits?** This breaks into three sequential validation steps, each building confidence before the next.

---

## Step 1: Agent Trait Consistency (Synthetic)

> **"Do the AI personas behave according to their assigned personality?"**

### Current Status
- Framework: complete (10 profiles, 4 scenarios, multi-agent orchestration)
- Generated sessions: 2
- Reverse inference validation: 150+ results
- LLM provider: DeepSeek V3.2 via OpenRouter

### What Still Needs to Be Done

#### 1.1 Expand Sample Generation
- **Target**: 120 sessions (10 profiles x 4 scenarios x 3 repetitions)
- **Why 3 reps per combination**: measures *within-profile consistency* -- does the same profile behave similarly across repeated runs of the same scenario?
- **Execution**: use `generate_batch.py` with full profile-scenario matrix

#### 1.2 Run Reverse Inference at Scale
- For all 120 sessions, run blind reverse inference (ground truth hidden)
- Use **2-3 different LLM judges** (e.g., DeepSeek, GPT-4o, Claude) to reduce single-model bias
- Store all results in `outputs/validation/`

#### 1.3 Statistical Analysis
Compute the following metrics across all sessions:

| Metric | Target | Minimum Acceptable |
|--------|--------|--------------------|
| Per-trait Pearson correlation (assigned vs inferred) | r >= 0.60 | r >= 0.40 |
| Mean Absolute Error per trait | MAE <= 0.15 | MAE <= 0.25 |
| Within-profile consistency (3 reps, same scenario) | SD <= 0.10 | SD <= 0.15 |
| Cross-scenario stability (same profile, 4 scenarios) | ICC >= 0.70 | ICC >= 0.60 |

#### 1.4 Identify Weak Spots
- Which profiles are poorly expressed? (e.g., does "Quiet Analyst" get confused with "Stoic Pragmatist"?)
- Which traits are hardest to express/detect? (Neuroticism and Openness are typically harder)
- Which scenarios elicit the most discriminating behavior?
- Use findings to refine system prompts and scenario designs

#### 1.5 Deliverable
- A report showing: "AI agents express assigned traits with r = X correlation and MAE = Y, with the following caveats: [...]"
- This gives confidence (or identifies problems) before putting real humans into the system

---

## Step 2: Evaluator Accuracy (Human-in-the-Loop)

> **"Can the LLM accurately assess a real person's personality traits from conversation?"**

This is the critical step. It requires real humans with **known personality ground truth** interacting with the platform.

### 2.1 Study Design

#### Participants
- **Target**: 30 participants (minimum 20 for statistical power)
- **Recruitment**: university students, colleagues, online (Prolific/MTurk for scale)
- **Compensation**: appropriate for 30-40 min total time commitment

#### Protocol Per Participant
```
1. Pre-session: Complete BFI-44 questionnaire (5-10 min)
   → Produces ground truth Big Five scores

2. Interview session: Interact with AI agents (15-20 min)
   → Participant plays themselves (NOT role-playing)
   → AI agents (Provoker, Mediator, Facilitator) run the group interview
   → Conversation is recorded as structured JSON

3. Post-session: Brief experience survey (2-3 min)
   → "Did you feel you could be yourself?"
   → "Did the AI agents feel realistic?"
   → Helps filter out low-engagement sessions
```

#### Evaluation
- LLM evaluator reads the conversation transcript (participant's turns only)
- Infers Big Five scores for the participant
- Compare LLM inference against BFI-44 ground truth

### 2.2 UI Transformation: Annotation Tool → Live Interview Platform

The current Streamlit UI is built for **annotation** (reviewing past conversations). For Step 2, it needs to become an **interactive interview platform**. Key changes:

#### Phase A: Pre-Session Module (New)
- Landing page with consent form and study info
- Embedded BFI-44 questionnaire (44 items, Likert scale 1-5)
  - Self-hosted, not a redirect -- keeps participant in-flow
  - Auto-scores and stores results server-side (hidden from participant)
- Participant ID generation (anonymous)
- Scenario assignment (random or counterbalanced)

#### Phase B: Live Interview Interface (Major Rework)
Current annotation UI shows past conversations. New UI must support **real-time interaction**:

```
┌─────────────────────────────────────────────────┐
│  GROUP INTERVIEW - [Scenario Title]             │
│  Time remaining: 14:32                          │
├──────────────────────────────────┬──────────────┤
│                                  │ Participants │
│   Conversation Panel             │              │
│   (scrolling chat view)          │ 👤 You       │
│                                  │ 🟢 Jordan    │
│   Jordan: "I think we should..." │ 🟢 Sam       │
│   Sam: "That's a fair point..."  │ 🟡 Facilitator│
│   [Typing indicator when AI      │              │
│    agents are "thinking"]        │              │
│                                  │──────────────│
│                                  │ Topic        │
│                                  │ [Brief desc] │
├──────────────────────────────────┴──────────────┤
│  ┌────────────────────────────────────┐ [Send]  │
│  │ Type your response...              │         │
│  └────────────────────────────────────┘         │
└─────────────────────────────────────────────────┘
```

Key features:
- **Chat-style interface** (familiar UX, lowers barrier)
- **Typing indicators** for AI agents (adds realism, gives think time)
- **Timer** for the 15-20 min session
- **No personality labels visible** -- participant sees "Jordan", "Sam", not "Provoker", "Mediator"
- **Natural turn-taking**: system prompts participant when it's their turn, but allows free-form input
- **Graceful session end**: Facilitator wraps up naturally when timer runs out

#### Phase C: Post-Session Module (New)
- Short experience survey (5-7 questions)
- Thank you page with debrief (after study concludes)
- Data export: conversation JSON + BFI-44 scores + survey responses

#### Technical Considerations
- **Backend**: Keep the existing agent pipeline (`simulation_engine.py`), but replace the candidate agent's LLM calls with a WebSocket/HTTP endpoint that waits for real human input
- **Latency**: AI agent responses should take 3-8 seconds (realistic "thinking" time, even if LLM responds faster -- instant responses feel uncanny)
- **Session persistence**: if connection drops, participant can reconnect
- **Data separation**: BFI-44 ground truth stored separately from conversation data (evaluator never sees it)

### 2.3 Evaluation Pipeline

```
For each participant:
  conversation_json = recorded session
  ground_truth = BFI-44 scores (normalized to 0.0-1.0)

  # Multiple LLM judges
  for judge in [DeepSeek, GPT-4o, Claude]:
      inferred_scores = judge.evaluate(conversation_json)

  # Metrics
  per_trait_correlation(inferred, ground_truth)
  mae_per_trait(inferred, ground_truth)

# Aggregate across all participants
overall_correlation_per_trait
overall_mae
judge_agreement (inter-rater reliability across LLM judges)
```

### 2.4 Success Criteria

| Metric | Target | Minimum |
|--------|--------|--------------------|
| Per-trait correlation (inferred vs BFI-44 ground truth) | r >= 0.50 | r >= 0.30 |
| Mean Absolute Error per trait | MAE <= 0.20 | MAE <= 0.30 |
| LLM judge inter-agreement (3 judges) | ICC >= 0.70 | ICC >= 0.60 |
| Participant engagement (post-survey) | >= 4.0/5.0 | >= 3.5/5.0 |

Note: targets here are deliberately lower than Step 1. Assessing real humans from 15-20 min of text is genuinely hard -- even human psychologists have limited accuracy from brief interactions.

### 2.5 Deliverable
- A report showing: "LLM evaluator can infer participant Big Five traits with r = X correlation against validated BFI-44 scores, based on N = 30 participants"
- Identification of which traits are reliably detectable and which are not
- UX findings from post-session surveys

---

## Step 3: End-to-End Platform Validation

> **"Does UbeU produce meaningful, reliable personality assessments in practice?"**

This step validates the **complete pipeline** -- from AI agent interaction design to final personality report -- as a cohesive product.

### 3.1 Prerequisites
- Step 1 confirms agents are trait-consistent (or identifies which need fixing)
- Step 2 confirms the LLM evaluator has measurable accuracy (or identifies limits)
- Fixes from Steps 1-2 are implemented

### 3.2 Study Design

#### Test-Retest Reliability
- **N >= 30 participants**, each completes **2 sessions** (different scenarios), 1-2 weeks apart
- If the platform is reliable, trait assessments should be stable across sessions
- Target: test-retest ICC >= 0.60

#### Convergent Validity
- Compare UbeU trait assessments against:
  - BFI-44 self-report (already collected in Step 2)
  - Peer ratings (ask 1-2 people who know the participant to rate their Big Five)
  - If possible: other validated assessment tools
- Multi-trait-multi-method (MTMM) matrix analysis

#### Discriminant Validity
- Do different personality profiles actually get different assessment results?
- Cluster analysis: do participants with similar BFI-44 profiles get similar UbeU assessments?

#### Scenario Sensitivity Analysis
- Does the choice of scenario affect trait assessment?
- Some scenarios may better elicit certain traits (e.g., deadline pressure for Neuroticism)
- Goal: understand which scenarios are most diagnostic

### 3.3 Soft Skills Evaluation Extension
Once personality assessment is validated, extend to soft skills:

```
Personality Traits (Big Five)     →  Validated in Steps 1-3
                                      ↓
Soft Skills Assessment             →  Built on top of trait foundation
  - Leadership                        Derived from E, C, O patterns
  - Teamwork                          Derived from A, E patterns
  - Stress Management                 Derived from N, C patterns
  - Communication                     Derived from E, A, O patterns
  - Problem Solving                   Derived from O, C patterns
```

- Soft skill rubrics grounded in observed behaviors during the interview
- Mapping from Big Five patterns to soft skill indicators (research-backed)
- Separate validation study for soft skill accuracy

### 3.4 Success Criteria

| Metric | Target | Minimum |
|--------|--------|--------------------|
| Test-retest reliability | ICC >= 0.65 | ICC >= 0.50 |
| Convergent validity (vs BFI-44) | r >= 0.50 | r >= 0.35 |
| Convergent validity (vs peer ratings) | r >= 0.40 | r >= 0.25 |
| Scenario independence (same person, diff scenario) | ICC >= 0.60 | ICC >= 0.45 |

### 3.5 Deliverable
- Full validation report suitable for academic publication or investor presentation
- Clear statement of what UbeU can and cannot reliably assess
- Recommended scenario configurations for different assessment goals

---

## Timeline & Dependencies

```
Step 1: Agent Trait Consistency
  ├── 1.1 Generate 120 sessions (batch generation)
  ├── 1.2 Multi-judge reverse inference
  ├── 1.3 Statistical analysis
  └── 1.4 Prompt refinement based on findings
         │
         ▼
Step 2: Evaluator Accuracy
  ├── 2.1 Build BFI-44 questionnaire into UI
  ├── 2.2 Transform UI into live interview platform
  ├── 2.3 Pilot test (3-5 participants, fix bugs)
  ├── 2.4 Main study (30 participants)
  └── 2.5 Analysis and reporting
         │
         ▼
Step 3: End-to-End Validation
  ├── 3.1 Apply fixes from Steps 1-2
  ├── 3.2 Test-retest study (30 participants x 2 sessions)
  ├── 3.3 Convergent/discriminant validity analysis
  └── 3.4 Soft skills extension (if personality validated)
```

---

## Your 48 Samples: Where They Fit

The 48 samples you've generated (or plan to generate) map to **Step 1**. Specifically:
- 48 sessions ≈ 10 profiles x 4 scenarios x ~1.2 reps (incomplete coverage)
- **Recommendation**: expand to 120 sessions (3 reps per combination) for within-profile consistency stats
- These 48 are still valuable as a first pass -- run the analysis on them first, then expand

They do **not** serve Step 2 (which requires real humans with BFI-44 ground truth). That's a fundamentally different dataset.

---

## Risk & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM personality expression is inconsistent | Step 1 fails | Prompt engineering iterations, try different base models |
| LLM evaluator can't infer traits from 15-20 min text | Step 2 fails | Extend session length, add structured prompts/questions, use behavioral coding instead of direct inference |
| Participants don't engage authentically with AI agents | Step 2 data quality | Post-session engagement filters, improve UI realism, add typing delays |
| Low recruitment numbers | Underpowered studies | Start with accessible pools (university), use online recruitment platforms |
| BFI-44 self-report itself has noise | Ground truth is imperfect | Use multiple ground truth sources in Step 3 (peer ratings, test-retest) |
