# Research Design: Behavioral Fidelity of LLM Personas Under Social Pressure

**Date:** 2026-03-03
**Author:** Jihae Park
**Project:** UbeU — Final Year Project (NTU)
**Status:** Pre-experiment refinement (ready for implementation)

---

## Executive Summary

This document formalizes the research design for evaluating whether LLM agents assigned specific Big Five personality traits actually *express* those traits as observable behavior in multi-agent group conversations under social pressure. The study is fully computational (no human participants required for the core experiment) and produces a reusable behavioral fidelity benchmark for LLM persona simulation.

**Long-term vision:** This research lays the empirical foundation for trustworthy LLM-based digital twin infrastructure — enabling simulation tools for negotiation training, policy impact forecasting, and business scenario modeling, where behavioral fidelity of synthetic personas is a prerequisite for any downstream application.

**Thesis statement (1 sentence):**
> "LLM-based digital twins and synthetic personas are increasingly proposed for user simulation and interactive applications, but it remains unclear whether assigned personality traits are behaviorally expressed and maintained under social pressure. This study evaluates trait-behavior alignment in multi-agent, high-pressure group conversations."

---

## 1. Problem Definition (문제 정의 명확성)

### 1.1 Background & Motivation

LLM-based synthetic personas are rapidly being deployed as substitutes for human participants:
- **User simulation** for product testing (Persona Generators, Paglieri et al. 2026)
- **Digital twins** for behavioral prediction (BehaviorChain, Li et al. 2025; TwinVoice, 2025)
- **Policy simulation** for population-level response forecasting (Social Digital Twins, 2026)
- **Consumer modeling** for marketing and business impact analysis (MSI 2025)

However, a critical gap exists:

> **Most existing evaluations measure persona fidelity through questionnaire responses (stated preferences) or single-turn outputs, not through sustained behavioral expression in interactive, dynamic settings.**

This is problematic because:
1. **RLHF sycophancy bias** causes LLMs to converge toward agreeable, polite, cooperative behavior regardless of assigned traits (Santurkar et al. 2023)
2. **Personality traits are most visible under pressure** — in calm settings, most agents behave similarly; conflict, time pressure, and social friction expose trait differences
3. **Prompt following ≠ behavioral fidelity** — an agent might describe itself as "disagreeable" while consistently producing agreeable responses

### 1.2 The Core Problem

**In casual conversation, all LLM personas look the same.**

Due to RLHF tuning, LLMs default to a cooperative, helpful, conflict-avoidant communication style. This means:
- A persona assigned low Agreeableness still says "That's a great point"
- A persona assigned high Neuroticism still responds calmly to criticism
- A persona assigned low Extraversion still produces lengthy, detailed responses

**Pressure is not a gimmick — it is the diagnostic tool.** Just as stress tests reveal cardiac vulnerabilities invisible in resting ECGs, social pressure reveals personality expression invisible in casual dialogue.

### 1.3 Research Questions

| ID | Research Question | What It Tests |
|----|------------------|---------------|
| **RQ1** | Are assigned Big Five traits **detectable** from group conversation transcripts by an independent LLM judge? | Can a blind evaluator reconstruct the assigned personality profile from behavioral evidence alone? |
| **RQ2** | Is trait expression **consistent** across different conflict scenarios and repeated runs? | Does the same personality profile produce similar behavioral patterns regardless of situational context? |
| **RQ3** | Does trait expression **decay** over the course of a conversation, reverting to default LLM behavior? | Do LLM personas maintain their assigned traits throughout the interaction, or does "persona leakage" occur? |

### 1.4 Why These Questions Matter

**If RQ1 fails** (traits are not detectable): LLM personas are cosmetic labels with no behavioral substance. Any downstream application built on personality-conditioned agents is unreliable.

**If RQ2 fails** (traits are not consistent): LLM personas are context-dependent — they "perform" personality only when the scenario makes it easy. This undermines generalizability.

**If RQ3 confirms decay**: LLM persona fidelity has a shelf life. This has direct implications for long-horizon simulations (negotiations, multi-day policy scenarios) where persona consistency is assumed.

### 1.5 What This Study Does NOT Claim

- ❌ "LLMs can replicate real human personality" — We do not validate against human ground truth in this study
- ❌ "LLM assessment can replace psychometric testing" — We test *expression*, not *assessment accuracy*
- ❌ "Pressure makes evaluation better" — We test whether pressure makes trait *differences more observable*
- ✅ "Assigned traits are (or are not) computationally detectable and behaviorally expressed within this simulation setting"

---

## 2. Methodology (방법론의 논리성)

### 2.1 Overall Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    EXPERIMENT PIPELINE                       │
│                                                             │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │ Profile  │───▶│ Multi-Agent  │───▶│ Blind Evaluation │   │
│  │ Assignment│    │ Conversation │    │ (Cross-Model)    │   │
│  │ (IV)     │    │ (Simulation) │    │ (DV Extraction)  │   │
│  └──────────┘    └──────────────┘    └──────────────────┘   │
│       │                │                      │             │
│       ▼                ▼                      ▼             │
│  12 OCEAN         Transcripts +          Inferred OCEAN     │
│  profiles         Behavioral Stats       scores + evidence  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              ANALYSIS & COMPARISON                    │   │
│  │  Assigned OCEAN  ←── compare ──▶  Inferred OCEAN     │   │
│  │                  + Behavioral Feature Analysis        │   │
│  │                  + Baseline Comparison                │   │
│  │                  + Temporal Decay Analysis            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Why This Methodology Is Logically Sound

The methodology follows a **known-input → observed-output → comparison** paradigm:

1. **Known input (IV):** We assign specific, quantified OCEAN trait values to each persona
2. **Behavioral observation:** The persona interacts in a multi-agent group conversation under controlled conditions
3. **Blind evaluation:** An independent LLM judge (different model from the conversation agent) reads only the transcript and infers OCEAN traits
4. **Comparison:** Assigned traits vs. inferred traits = measure of behavioral fidelity

This is logically equivalent to a **construct validity test** in psychometrics: if we build a persona with trait X, does an independent observer detect trait X from behavioral evidence?

### 2.3 Addressing Circularity (The Critical Methodological Risk)

**The risk:** LLM generates personas → LLM simulates conversations → LLM evaluates = self-referential loop.

**How we mitigate this (3 layers):**

| Layer | Mechanism | Implementation |
|-------|-----------|----------------|
| **Cross-model evaluation** | Generation model ≠ Evaluation model | Conversation: DeepSeek V3. Evaluation ensemble: Claude 3.5 Haiku + Gemini 2.5 Flash + Grok 4.1 Fast (median aggregation). DeepSeek explicitly excluded from evaluation to eliminate circularity. |
| **Rule-based behavioral features** | Non-LLM quantitative metrics extracted from transcripts | Already implemented in `GroupSessionStats`: word count per turn, question ratio, disagreement count, idea proposals, acknowledgments, phase engagement |
| **Evidence-traced scoring** | Every LLM-judge score must cite specific transcript quotes | Each trait score includes `quote`, `turn_number`, `signal_direction`, `signal_strength` |

**Why this is sufficient for an FYP:**
- Perfect elimination of circularity would require human annotation, which is beyond scope
- Cross-model evaluation + rule-based features is the standard approach in current computational behavioral research (BehaviorChain 2025, TwinVoice 2025)
- The evidence-tracing requirement makes evaluation auditable — any score can be manually verified against the transcript

### 2.4 Role of Pressure in Methodology

Pressure is not an optional enhancement — it is a **methodological necessity** for trait discrimination.

**Without pressure:**
```
Agent A (low A, high N): "That's a good suggestion, let me think about it."
Agent B (high A, low N): "That's a good suggestion, let me think about it."
→ Indistinguishable
```

**With pressure (conflict scenario, Alex challenges directly):**
```
Agent A (low A, high N): "I... I'm not sure, maybe we should reconsider..."
Agent B (high A, low N): "I see your concern, but here's why this still works..."
→ Distinguishable
```

The 4 scenarios are designed to apply different types of pressure that differentially activate specific traits (see Section 3.3).

---

## 3. Experimental Design (실험 설계 디자인과 타당성)

### 3.1 Variables

#### Independent Variables (IVs)

| Variable | Levels | Operationalization |
|----------|--------|-------------------|
| **Personality Profile** | 12 profiles (see 3.2) | Each profile = 5 OCEAN values on 0.0–1.0 scale, embedded in persona system prompt |
| **Scenario Type** | 4 scenarios (see 3.3) | Each scenario has 5 phases with scripted pressure points |

#### Dependent Variables (DVs)

| Variable | Source | Scale |
|----------|--------|-------|
| **LLM-inferred OCEAN scores** | Ensemble evaluation (3 models, median) | 0.0–1.0 per trait |
| **Evaluation confidence** | 1.0 - score_range across ensemble models | 0.0–1.0 |
| **Behavioral statistics** | Rule-based extraction from transcript | Count/ratio |

**Behavioral statistics (already implemented in system):**

| Feature | Metric | Primary Trait Signal |
|---------|--------|---------------------|
| `candidate_avg_words_per_turn` | Mean words per speaking turn | **Extraversion** (high E → more words) |
| `times_asked_questions` | Total questions asked | **Openness** (curiosity, engagement) |
| `times_expressed_disagreement` | Count of disagreement instances | **Agreeableness** (low A → more disagreement) |
| `times_acknowledged_others` | Count of acknowledgment phrases | **Agreeableness** (high A → more acknowledgment) |
| `times_proposed_new_ideas` | Count of novel proposals | **Openness** (high O → more ideas) |
| `phase_engagement` | Per-phase engagement level | **Neuroticism** (engagement drop under stress) |
| `times_addressed_others_by_name` | Name mentions | **Extraversion** (social awareness) |

#### Control Variables

| Variable | Fixed Value | Rationale |
|----------|------------|-----------|
| **Conversation model** | DeepSeek V3 (`deepseek/deepseek-chat-v3-0324`) | Consistency across sessions |
| **Conversation temperature** | 0.7 | Already calibrated for natural dialogue |
| **Evaluation temperature** | 0.3 | Already calibrated for focused scoring |
| **Agent roles** | Alex (Challenger), Jordan (Collaborator), Riley (Quiet Skeptic) — fixed prompts | Controlled interactional stimulus |
| **Turn structure** | ~17 turns per scenario (5 phases) | Standardized via phase turn limits |
| **Max tokens per agent** | Alex: 150, Jordan: 100, Riley: 60 | Controls response length by role |
| **Evaluation ensemble** | DeepSeek V3 + Gemini 2.5 Flash + Grok 4.1 Fast | Cross-model evaluation |

### 3.2 Personality Profiles (12 Profiles)

**Selection Principle:** Profiles are selected to cover 4 categories of Big Five trait space:
1. **Extreme contrast profiles** (4): Maximally distinct on 2+ traits
2. **Socially challenging profiles** (3): Combinations that create interpersonal friction
3. **Balanced/moderate profiles** (3): Mid-range traits that test discrimination sensitivity
4. **Domain-relevant profiles** (2): Profiles typical in workplace assessment contexts

| # | Profile Name | O | C | E | A | N | Category | Design Rationale |
|---|-------------|---|---|---|---|---|----------|-----------------|
| 1 | **Assertive Leader** | 0.6 | 0.8 | 0.9 | 0.4 | 0.2 | Extreme | High E + Low A: dominant, direct, confident |
| 2 | **Quiet Analyst** | 0.5 | 0.9 | 0.2 | 0.6 | 0.3 | Extreme | Low E + High C: thorough but reserved |
| 3 | **Creative Rebel** | 0.9 | 0.3 | 0.7 | 0.3 | 0.4 | Extreme | High O + Low C + Low A: innovative but chaotic |
| 4 | **Anxious Perfectionist** | 0.4 | 0.9 | 0.3 | 0.7 | 0.9 | Extreme | High C + High N: meticulous but stressed |
| 5 | **Defensive Contrarian** | 0.3 | 0.5 | 0.6 | 0.2 | 0.8 | Socially Challenging | Low A + High N: combative under pressure |
| 6 | **Passive Avoider** | 0.4 | 0.4 | 0.2 | 0.8 | 0.7 | Socially Challenging | Low E + High A + High N: withdraws from conflict |
| 7 | **Volatile Visionary** | 0.9 | 0.4 | 0.8 | 0.3 | 0.7 | Socially Challenging | High O + High E + Low A + High N: passionate but unstable |
| 8 | **Steady Mediator** | 0.6 | 0.7 | 0.6 | 0.9 | 0.2 | Balanced | High A + Low N: calm, accommodating, stable |
| 9 | **Neutral Observer** | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | Balanced | All traits at midpoint — tests discrimination at center |
| 10 | **Warm Supporter** | 0.6 | 0.6 | 0.7 | 0.8 | 0.3 | Balanced | Moderately high on most — tests detection of subtle differences |
| 11 | **Diligent Team Player** | 0.5 | 0.8 | 0.6 | 0.7 | 0.3 | Domain-Relevant | Common "good employee" profile — tests if LLM can differentiate from baseline |
| 12 | **Independent Strategist** | 0.7 | 0.7 | 0.5 | 0.4 | 0.4 | Domain-Relevant | Common "strategic thinker" profile — low A is the differentiator |

**Why 12 profiles (not 32 or 5):**
- 2^5 = 32 full factorial is computationally excessive for an FYP
- 5 profiles would not cover enough of the trait space
- 12 profiles × 4 scenarios × 3 repetitions = 144 sessions is substantial but feasible
- The 4-category selection principle ensures coverage of extremes, challenges, moderates, and domain-relevant combinations

### 3.2.1 Behavior Prompt Design: Scientific Justification

#### Why this matters

The behavior prompt is the **sole mechanism** through which assigned OCEAN values are translated into LLM behavior. If the prompt is poorly designed, the entire experiment fails — not because the LLM lacks capability, but because the instruction was inadequate. This section justifies our prompt design approach with empirical evidence.

#### Evaluated Approaches from Literature

| # | Approach | Source | Method | Validation |
|---|----------|--------|--------|------------|
| 1 | **Simple trait labels** | PersonaLLM (Jiang et al., NAACL 2024) | "You are a character who is [extroverted, agreeable...]" | 80% human perception accuracy; large effect sizes on BFI self-report (d = 0.65–1.80 across traits) |
| 2 | **Behavioral description** | PERSONAGE (Mairesse & Walker, 2007, JAIR) | Empirically derived linguistic markers per trait mapped to generation parameters | Validated against 2,000+ human personality ratings; significant correlations between generated language features and perceived personality |
| 3 | **Logic of Appropriateness** | Concordia / Persona Generators (Leibo et al., 2024; Paglieri et al., 2026) | "What kind of person am I? What does a person like me do in this situation?" | Validated for *diversity* of generated personas; NOT validated for behavioral fidelity |

#### Our Approach: Hybrid (Approach 1 + 2)

We combine **simple trait labels** (Approach 1) for interpretability with **empirically grounded behavioral descriptors** (Approach 2) for precision. This avoids the complexity of Logic of Appropriateness (which requires a separate reasoning step per turn) while grounding behavioral instructions in validated psycholinguistic research.

**Why NOT use the Persona Generators paper's method:**
- The Persona Generators paper (Paglieri et al., 2026) uses AlphaEvolve to optimize persona *diversity*, not behavioral *fidelity*
- Their evaluation metric is persona diversity (how different are generated personas from each other), not trait-behavior alignment (does a high-E persona actually behave extraverted?)
- Their method (Logic of Appropriateness) is designed for Concordia simulations where each agent reasons about "what would a person like me do?" — this adds latency and complexity without evidence that it improves fidelity
- **Conclusion: The Persona Generators paper's method is validated for diversity generation but NOT for behavioral fidelity.** It is not directly applicable to our use case.

#### Empirical Basis for Trait→Behavior Mapping

Each behavioral instruction in our prompt is grounded in one or more of the following evidence sources:

| Evidence Source | Description | Traits Covered |
|----------------|-------------|----------------|
| **Mairesse & Walker (2007)** | PERSONAGE system: empirically validated mappings between Big Five traits and 67 linguistic parameters (verbosity, hedging, lexical choice, etc.) based on 2,000+ personality ratings | All 5 traits |
| **Pennebaker & King (1999)** | LIWC-based analysis of 2,400 essays showing significant correlations between word categories and personality traits | All 5 traits |
| **Mehl et al. (2006)** | Electronically Activated Recorder (EAR) study: naturalistic observation of 96 participants' daily speech patterns correlated with Big Five | E, A, N |
| **Scherer (1979); Mairesse et al. (2007)** | Meta-analysis of personality perception in speech: content features (topic, verbosity) and style features (hedging, formality) as trait indicators | All 5 traits |
| **PMC 9523152 (group discussion study)** | LIWC and behavioral coding in group discussion contexts specifically — closest to our scenario | All 5 traits |

#### OCEAN → Behavioral Instruction Mapping

For each trait level (High ≥ 0.7 / Moderate 0.4–0.6 / Low ≤ 0.3), we specify behavioral instructions grounded in the empirical literature above.

**Extraversion (E)**

| Level | Behavioral Instruction | Empirical Basis |
|-------|----------------------|-----------------|
| **High (≥ 0.7)** | Speak at length (4-6 sentences per turn). Take initiative to start new topics. Use social/positive-emotion words. Address others by name frequently. Express enthusiasm openly. | Mairesse & Walker (2007): verbosity is the strongest E marker (r=0.40). Mehl et al. (2006): extraverts speak more in group settings. PMC 9523152: word count r=0.15, positive emotions r=0.20-0.21 |
| **Moderate (0.4–0.6)** | Respond at natural length (2-3 sentences). Contribute when you have something relevant. Neither dominate nor withdraw. | Interpolation between extremes |
| **Low (≤ 0.3)** | Keep responses brief (1-2 sentences maximum). Wait to be addressed before speaking. Minimal elaboration. Avoid initiating new topics. | Mairesse & Walker (2007): low verbosity, fewer social references. Mehl et al. (2006): introverts speak less in groups |

**Agreeableness (A)**

| Level | Behavioral Instruction | Empirical Basis |
|-------|----------------------|-----------------|
| **High (≥ 0.7)** | Acknowledge others' ideas before responding ("Good point", "I see what you mean"). Seek compromise in disagreements. Use positive emotion words. Avoid negations and confrontational language. When challenged, accommodate rather than defend. | Mairesse & Walker (2007): agreeable speakers use more positive emotion words, fewer negations, more acknowledgments. PMC 9523152: positive emotions, fewer negations correlated with A |
| **Moderate (0.4–0.6)** | Balance agreement and disagreement. Express your view but remain respectful. Willing to compromise but not at the expense of your core position. | Interpolation |
| **Low (≤ 0.3)** | Challenge ideas directly ("I disagree because..."). Defend your position firmly when challenged. Use direct language without softeners. Prioritize being correct over being liked. Don't accommodate just to avoid conflict. | Mairesse & Walker (2007): low A speakers use more negations, confrontational language, fewer acknowledgments |

**Openness (O)**

| Level | Behavioral Instruction | Empirical Basis |
|-------|----------------------|-----------------|
| **High (≥ 0.7)** | Propose novel ideas and hypotheticals ("What if we tried..."). Use diverse vocabulary and complex sentence structures. Explore abstract concepts. Build creative connections between ideas. Express intellectual curiosity. | Pennebaker & King (1999): O correlates with articles, prepositions (r=0.15), lexical diversity. Mairesse & Walker (2007): high O → more complex syntax, diverse word choice |
| **Moderate (0.4–0.6)** | Mix practical and creative suggestions. Open to new ideas but also consider feasibility. | Interpolation |
| **Low (≤ 0.3)** | Focus on practical, concrete solutions. Prefer proven approaches ("Let's stick with what works"). Resist abstract hypotheticals. Simple, direct language. Express skepticism toward untested ideas. | Pennebaker & King (1999): low O → simpler vocabulary, fewer abstract words. Mairesse & Walker (2007): low O → conventional word choice |

**Conscientiousness (C)**

| Level | Behavioral Instruction | Empirical Basis |
|-------|----------------------|-----------------|
| **High (≥ 0.7)** | Structure responses with clear organization (numbered points, priorities). Reference deadlines, timelines, action items. Use certainty and discrepancy words ("We need to", "We should"). Follow up on earlier commitments. Be detail-oriented and thorough. | PMC 9523152: C correlates with certainty/discrepancy words, suggestions, detail orientation. Pennebaker & King (1999): C correlates with achievement words |
| **Moderate (0.4–0.6)** | Reasonably organized but not rigid. Address practical concerns without over-structuring. | Interpolation |
| **Low (≤ 0.3)** | Respond ad hoc without clear structure. Jump between topics. Forget or ignore earlier points. Avoid committing to specific actions or timelines. Casual, informal tone. | PMC 9523152: low C → scattered responses, low certainty language |

**Neuroticism (N)**

| Level | Behavioral Instruction | Empirical Basis |
|-------|----------------------|-----------------|
| **High (≥ 0.7)** | Under pressure, use hedging language ("I'm not sure", "maybe", "I think"). Express anxiety or defensiveness when challenged. Use negative emotion words. Become more verbose or more withdrawn under stress (inconsistent response). Apologize preemptively. | PMC 9523152: N correlates with negative emotions, anxiety words, first-person plural pronouns. Mairesse & Walker (2007): high N → more hedges, self-references, anxiety markers. Mehl et al. (2006): high N shows more negative affect in speech |
| **Moderate (0.4–0.6)** | Show mild concern under pressure but recover. Occasional hedging without pervasive anxiety. | Interpolation |
| **Low (≤ 0.3)** | Remain calm and composed under pressure. Use confident, steady language. Don't apologize unnecessarily. Address challenges matter-of-factly. Maintain consistent tone regardless of stress level. | Mairesse & Walker (2007): low N → confident language, fewer hedges, emotional stability |

#### Candidate Agent System Prompt Template

The behavior prompt follows a structured template that combines trait labels (PersonaLLM approach) with behavioral descriptors (PERSONAGE approach):

```
You are a participant in a group discussion. You have the following personality profile:

## Your Personality (Big Five / OCEAN)
- Openness: {O_level} ({O_value})
- Conscientiousness: {C_level} ({C_value})
- Extraversion: {E_level} ({E_value})
- Agreeableness: {A_level} ({A_value})
- Neuroticism: {N_level} ({N_value})

## How Your Personality Affects Your Behavior
{E_behavioral_instruction}
{A_behavioral_instruction}
{O_behavioral_instruction}
{C_behavioral_instruction}
{N_behavioral_instruction}

## Important Rules
- Stay in character throughout the entire discussion
- Your personality should be expressed through HOW you communicate, not by explicitly stating your traits
- React naturally to what others say — your personality influences your reactions
- Do NOT mention personality traits, OCEAN scores, or psychology terms
- Respond ONLY with your dialogue — no actions, no stage directions, no name prefix
```

**Template variables:**
- `{X_level}`: "High", "Moderate", or "Low" based on thresholds (≥0.7, 0.4-0.6, ≤0.3)
- `{X_value}`: Raw OCEAN value (e.g., 0.8) — included for precision
- `{X_behavioral_instruction}`: Selected from the mapping table above based on trait level
- For traits in the 0.31-0.39 or 0.61-0.69 range, use the "leaning" modifier: e.g., "Moderate-High (0.65)" with a blend of moderate and high instructions

**Generation parameters:**
- Model: DeepSeek V3 (`deepseek/deepseek-chat-v3-0324`)
- Temperature: **0.7** (allows behavioral variation within personality constraints)
- Max tokens: **200** (ensures substantive but bounded responses)

**Example: Assertive Leader (O=0.6, C=0.8, E=0.9, A=0.4, N=0.2)**

```
You are a participant in a group discussion. You have the following personality profile:

## Your Personality (Big Five / OCEAN)
- Openness: Moderate (0.6)
- Conscientiousness: High (0.8)
- Extraversion: High (0.9)
- Agreeableness: Moderate-Low (0.4)
- Neuroticism: Low (0.2)

## How Your Personality Affects Your Behavior
EXTRAVERSION (High): Speak at length (4-6 sentences per turn). Take initiative to start new topics. Use social/positive-emotion words. Address others by name frequently. Express enthusiasm openly.

AGREEABLENESS (Moderate-Low): Balance agreement and disagreement but lean toward directness. Express your view firmly. Willing to defend your position when challenged. Don't accommodate just to avoid conflict.

OPENNESS (Moderate): Mix practical and creative suggestions. Open to new ideas but also consider feasibility.

CONSCIENTIOUSNESS (High): Structure responses with clear organization (numbered points, priorities). Reference deadlines, timelines, action items. Use certainty words ("We need to", "We should"). Follow up on earlier commitments. Be detail-oriented and thorough.

NEUROTICISM (Low): Remain calm and composed under pressure. Use confident, steady language. Don't apologize unnecessarily. Address challenges matter-of-factly. Maintain consistent tone regardless of stress level.

## Important Rules
- Stay in character throughout the entire discussion
- Your personality should be expressed through HOW you communicate, not by explicitly stating your traits
- React naturally to what others say — your personality influences your reactions
- Do NOT mention personality traits, OCEAN scores, or psychology terms
- Respond ONLY with your dialogue — no actions, no stage directions, no name prefix
```

#### Prompt Validation Strategy

To verify that behavior prompts produce the intended behavioral patterns **before** running the full experiment:

1. **Pilot test (Week 1):** Run 2 extreme-contrast profiles (Assertive Leader + Passive Avoider) × 2 scenarios × 1 rep = 4 sessions
2. **Quick check:** Compare word count (E proxy), disagreement count (A proxy), hedging language (N proxy) between profiles
3. **Expected differences:** Assertive Leader should show ≥2x word count and ≥3x disagreement count vs. Passive Avoider
4. **If differences are weak:** Increase behavioral instruction specificity (add more concrete examples) before proceeding

### 3.3 Scenario–Trait Mapping

Each scenario is designed to apply specific types of social pressure that differentially activate certain Big Five traits:

| Scenario | Primary Traits Elicited | Pressure Mechanism | Expected Behavioral Signals |
|----------|------------------------|--------------------|-----------------------------|
| **Resource Conflict** | Agreeableness, Conscientiousness | Scarce resources force trade-offs; Alex pushes for his preferred allocation | High A: compromises, seeks win-win. Low A: holds ground, argues. High C: proposes structured criteria. Low C: ad hoc decisions |
| **Creative Brainstorm** | Openness, Extraversion | Open-ended ideation → Alex criticizes candidate's ideas | High O: generates novel ideas, explores hypotheticals. Low O: stays practical. High E: dominates ideation, speaks at length. Low E: brief contributions |
| **Crisis Management** | Neuroticism, Conscientiousness | Urgent bug, 30-min deadline, Alex delivers bad news aggressively | High N: hedging, apologetic tone, defensive. Low N: calm problem-solving. High C: creates action plan, prioritizes. Low C: scattered response |
| **New Member Integration** | Extraversion, Agreeableness | Riley (quiet newcomer) needs inclusion; conflict over work style | High E: proactively engages Riley, takes initiative. Low E: waits for others. High A: accommodates Riley's preferences. Low A: pushes own workflow |

**Design rationale:** Every Big Five trait is a primary elicitation target in at least one scenario and a secondary target in at least one other. No trait is tested in only one context.

| Trait | Primary in | Secondary in |
|-------|-----------|-------------|
| **Openness** | Creative Brainstorm | New Member Integration |
| **Conscientiousness** | Resource Conflict, Crisis Management | Creative Brainstorm |
| **Extraversion** | Creative Brainstorm, New Member Integration | Resource Conflict |
| **Agreeableness** | Resource Conflict, New Member Integration | Creative Brainstorm |
| **Neuroticism** | Crisis Management | Resource Conflict |

### 3.4 Session Structure

Each session follows a standardized 5-phase structure (~17 turns total):

```
Phase 1: INTRODUCTION (2 turns)    → Neutral warm-up
Phase 2: EXPLORATION (4-5 turns)   → Agreement/ideation — baseline behavior
Phase 3: CONFLICT (4-5 turns)      → Disagreement — peak pressure
Phase 4: RESOLUTION (3-4 turns)    → Consensus-seeking — recovery behavior
Phase 5: CLOSING (2 turns)         → Wrap-up
```

**For RQ3 (decay analysis), sessions are divided into 3 temporal windows:**

| Window | Phases | Label | Expected Pattern |
|--------|--------|-------|-----------------|
| **Window 1** | Phase 1-2 (turns 1-7) | Early | Strongest trait expression (fresh persona prompt) |
| **Window 2** | Phase 3 (turns 8-12) | Peak Pressure | Trait amplification or breakdown under stress |
| **Window 3** | Phase 4-5 (turns 13-17) | Late | Potential decay toward default LLM behavior |

### 3.5 Baseline Conditions

| Condition | Description | Sessions | Purpose |
|-----------|-------------|----------|---------|
| **Main Experiment** | 12 profiles × 4 scenarios × 3 reps | **144** | Core data |
| **Baseline A: No-Persona** | No personality description in prompt; only scenario context | 4 scenarios × 3 reps = **12** | Tests whether trait assignment changes behavior at all vs. default LLM |
| **Baseline B: Random-Persona** | OCEAN values randomly shuffled from the 12 profiles (assigned label ≠ actual values) | 4 scenarios × 2 reps = **8** | Tests whether the *specific* trait values matter, or any personality description produces the same effect |
| **Total** | | **164 sessions** | |

**What each baseline answers:**

- **Main vs. Baseline A:** "Does assigning any personality trait produce behaviorally distinct responses compared to no trait assignment?"
  - If no difference → trait assignment is cosmetic; LLM ignores persona instructions
  - Expected metric: Main experiment inferred scores should show higher variance than Baseline A

- **Main vs. Baseline B:** "Does the *specific* trait configuration matter, or does any personality description produce generic 'personality-like' behavior?"
  - If no difference → LLM follows the instruction to "have a personality" but doesn't differentiate between specific traits
  - Expected metric: Main experiment assigned-inferred correlation should be significantly higher than Baseline B

### 3.6 Evaluation Protocol

#### Stage 1: LLM Ensemble Evaluation (Primary DV)

```
Input:  Raw transcript only (no profile information — blind evaluation)
Models: Claude 3.5 Haiku + Gemini 2.5 Flash + Grok 4.1 Fast
        (DeepSeek V3 excluded — used for generation, not evaluation)
Output: Per-trait score (0.0–1.0) with evidence citations
Aggregation: Median score per trait
Confidence: 1.0 − (max_score − min_score) across 3 models
Temperature: 0.3
```

The evaluation prompt requires:
- Specific transcript quotes as evidence for each score
- Signal direction (high/low) and strength (strong/moderate/weak)
- Calibration anchors (e.g., "Only rate Extraversion > 0.7 if avg words/turn > 40")

#### Stage 2: Rule-Based Feature Extraction (Secondary DV)

Extracted automatically from transcript (no LLM involved):

| Feature | Computation | Expected Trait Correlation |
|---------|-------------|--------------------------|
| Words per turn (mean) | Total words / total turns | + Extraversion |
| Question ratio | Questions asked / total turns | + Openness |
| Disagreement ratio | Disagreements / total turns | − Agreeableness |
| Acknowledgment ratio | Acknowledgments / total turns | + Agreeableness |
| New idea count | Novel proposals | + Openness |
| Name mention count | Times addressed others by name | + Extraversion |
| Phase engagement pattern | Engagement level per phase | − Neuroticism (drops under stress) |

#### Stage 3: Temporal Analysis (RQ3 only)

For each session, the evaluation is run **3 times** — once per temporal window (early / peak / late):
- Same evaluation prompt, but restricted to transcript segments from each window
- Compare inferred trait scores: Window 1 vs Window 2 vs Window 3
- Decay = significant drop in assigned-inferred correlation from Window 1 to Window 3

### 3.7 Metrics & Success Criteria

#### Threshold Justification Framework

Each threshold is grounded in one or more of the following evidence sources:

| Source Type | Description | Examples Used |
|-------------|-------------|---------------|
| **Psychometric benchmarks** | Established reliability/validity standards from personality psychology | BFI-44 test-retest reliability, Big Five meta-analyses |
| **Effect size conventions** | Cohen's (1988) widely-adopted benchmarks for behavioral science | *r* = .10 small, .30 medium, .50 large |
| **Comparable LLM studies** | Performance benchmarks from recent LLM persona/digital twin research | Park et al. (2024), BehaviorChain (2025), TwinVoice (2025) |
| **Statistical standards** | Established interpretation guidelines from reliability research | Koo & Li (2016), Cicchetti (1994) |

---

#### RQ1 Metrics: Trait Detectability

**Metric 1: Pearson *r* (assigned vs. inferred) ≥ 0.60**

| Justification Layer | Evidence | Value |
|---------------------|----------|-------|
| **Cohen's convention** | Cohen (1988) defines *r* ≥ 0.50 as a "large" effect in behavioral science. Our threshold exceeds this to account for the controlled nature of our study (assigned traits are known, not estimated). | *r* ≥ 0.50 = large effect |
| **BFI-44 test-retest** | Human test-retest reliability for BFI-44 ranges from *r* = .65 (Openness) to *r* = .79 (Extraversion) over 6-8 weeks (Gosling et al., 2003). A meta-analysis of 682 test-retest correlations across 74 samples found a median dependability of ρ = .816 (Gnambs, 2014). We set our threshold *below* human test-retest reliability to acknowledge that LLM behavioral fidelity is a weaker construct than human personality stability. | *r* = .65–.82 (human baseline) |
| **Comparable LLM study** | Park et al. (2024) reported persona-based agent normalized correlation of 0.75 for Big Five prediction, while demographic-only agents achieved 0.55. Our threshold of 0.60 sits between the demographic-only baseline (low bar) and the interview-grounded agents (high bar), appropriate for an interactive behavioral study without interview grounding. | *r* = .55–.75 (LLM range) |
| **Study design adjustment** | Unlike Park et al., we measure behavioral *expression* (observed in conversation), not questionnaire *response* (self-report). Behavioral observation typically yields lower correlations than self-report due to measurement noise. Setting the threshold at .60 rather than .75 accounts for this methodological difference. | Adjusted downward |

**Threshold decision:** *r* ≥ 0.60 represents a large effect (Cohen), is below human test-retest reliability (realistic), and sits between known LLM baselines (discriminating). If achieved, it provides evidence that assigned traits produce behaviorally detectable patterns above chance and above demographic-only conditioning.

**Minimum acceptable:** *r* ≥ 0.40 (Cohen's "medium" effect). Below this, trait detectability is marginal.

---

**Metric 2: MAE ≤ 0.15 (on 0.0–1.0 scale)**

| Justification Layer | Evidence | Value |
|---------------------|----------|-------|
| **Likert scale equivalence** | BFI-44 uses a 5-point Likert scale (1–5). An MAE of 0.15 on a 0–1 scale translates to 0.60 on a 1–5 scale, which is less than the width of one response category. This means the inferred score is, on average, within the same response band as the assigned score. | 0.15 × 4 = 0.60 Likert points |
| **BFI-44 measurement precision** | BFI-44 subscale standard errors of measurement (SEM) typically range from 0.50 to 0.70 on the 1–5 scale (John & Srivastava, 1999), equivalent to 0.125–0.175 on 0–1 scale. Our MAE threshold aligns with the upper bound of the instrument's own measurement error. | SEM ≈ 0.125–0.175 (on 0–1) |
| **Comparable LLM study** | Park et al. (2024) reported that interview-based agents achieved significantly lower MAE than demographic-based agents for Big Five traits (F(2, 3153) = 25.96, p < .001). While exact MAE values were not standardized to 0–1, the finding establishes MAE as a validated metric for LLM persona accuracy and confirms that meaningful differences exist in this range. | MAE as validated metric |
| **Practical interpretation** | On our 0–1 scale: MAE of 0.15 means if a profile is assigned Agreeableness = 0.3, the inferred score falls between 0.15–0.45 on average. This range still preserves the qualitative distinction (low A vs. high A) needed for behavioral interpretation. | Preserves qualitative meaning |

**Threshold decision:** MAE ≤ 0.15 ensures inferred scores are within one Likert-equivalent band of assigned values and within the BFI-44's own measurement error range. This is a reasonable precision standard for computational behavioral inference.

**Minimum acceptable:** MAE ≤ 0.20. Above 0.20 (= 0.80 Likert points), inferred scores may cross qualitative boundaries (e.g., "low" misclassified as "moderate").

---

**Metric 3: Main vs. Baseline A — *p* < 0.05**

| Justification | Standard |
|---------------|----------|
| Conventional significance level in behavioral science (Fisher, 1925; Neyman & Pearson, 1933). Applied with independent samples t-test comparing trait score variance between main experiment and no-persona baseline. We also report Cohen's *d* effect size to supplement *p*-value interpretation. | Industry standard |

---

**Metric 4: Main vs. Baseline B — Fisher *z*-test, *p* < 0.05**

| Justification | Standard |
|---------------|----------|
| Fisher's *z*-transformation test compares whether two independent correlations differ significantly. We compare *r*(main: assigned vs inferred) against *r*(random: misassigned vs inferred). If main *r* is not significantly higher than random *r*, trait specificity is not demonstrated — any personality description produces similar behavioral effects regardless of actual trait values. | Standard correlation comparison method |

---

#### RQ2 Metrics: Trait Consistency

**Metric 5: ICC ≥ 0.70 (cross-scenario consistency)**

| Justification Layer | Evidence | Value |
|---------------------|----------|-------|
| **Koo & Li (2016) guidelines** | ICC interpretation: < 0.50 = poor, 0.50–0.75 = moderate, 0.75–0.90 = good, > 0.90 = excellent. Our threshold of 0.70 targets the upper end of "moderate" reliability. | 0.70 = upper-moderate |
| **Cicchetti (1994) guidelines** | Alternative interpretation: 0.60–0.74 = good, ≥ 0.75 = excellent. Under Cicchetti's framework, our threshold of 0.70 falls in the "good" range. | 0.70 = good |
| **Why not ≥ 0.75 (Koo & Li "good")?** | Human Big Five test-retest ICC typically ranges from 0.70–0.85 over 6–8 week intervals. Since we are measuring cross-*scenario* consistency (same trait, different situational context) rather than cross-*time* consistency (same situation, different time), we expect lower ICC because different scenarios activate different behavioral registers. Setting the threshold at 0.70 rather than 0.75 accounts for legitimate scenario-driven variation. | Scenario variation > time variation |
| **BFI-44 internal consistency** | BFI-44 Cronbach's alpha ranges from .73 (Neuroticism) to .81 (Extraversion) across international samples. Our ICC threshold of .70 is below the instrument's own internal consistency, acknowledging that behavioral expression consistency across scenarios is a harder standard than item response consistency within a questionnaire. | α = .73–.81 (BFI-44) |
| **ICC form specification** | We use ICC(3,k) — two-way mixed effects, absolute agreement, average measures — because: (a) the 3 evaluation models are a fixed set (not randomly sampled), (b) we report the average of the ensemble, and (c) absolute agreement matters (not just rank order). This follows Koo & Li (2016) recommendation for reliability studies with fixed raters. | ICC(3,k) specified |

**Threshold decision:** ICC ≥ 0.70 is "upper-moderate" (Koo & Li) or "good" (Cicchetti), aligns with the lower bound of human BFI test-retest reliability, and accounts for legitimate scenario-driven variation.

**Minimum acceptable:** ICC ≥ 0.50 (Koo & Li "moderate"). Below 0.50, cross-scenario consistency is poor — traits are highly context-dependent.

---

**Metric 6: Within-profile SD ≤ 0.10 (cross-repetition consistency)**

| Justification Layer | Evidence | Value |
|---------------------|----------|-------|
| **Measurement precision** | On a 0–1 scale, SD = 0.10 means that 95% of repeated measurements fall within ±0.20 of the mean (assuming normality). This represents a ±1 Likert point on a 5-point scale — the smallest meaningful unit of personality measurement. | ±0.20 = ±1 Likert point |
| **BFI-44 within-person variability** | Studies on short-term BFI test-retest report within-person SDs of 0.40–0.70 on the 1–5 scale (= 0.10–0.175 on 0–1 scale) for intervals of days to weeks (Soto & John, 2017). Our threshold of 0.10 is at the lower end of human within-person variability, which is appropriate because LLM outputs should be *more* consistent than humans (no mood effects, no memory decay). | SD = 0.10–0.175 (human range) |
| **Practical interpretation** | If an Assertive Leader profile is assigned E = 0.9 and is evaluated three times in the same scenario, we expect the inferred E scores to be within 0.80–1.00 (SD ≤ 0.10). Larger spread would suggest the persona is not reliably expressing the assigned level of Extraversion. | Meaningful precision band |

**Threshold decision:** SD ≤ 0.10 is at the lower bound of human within-person variability, appropriate for LLM personas which should show higher consistency than humans.

---

#### RQ3 Metrics: Temporal Decay

**Metric 7: Window 1 vs. Window 3 — Paired comparison (exploratory)**

| Justification | Rationale |
|---------------|-----------|
| **No fixed threshold — exploratory analysis** | RQ3 is the most novel question in this study. No prior work has measured turn-level personality decay in LLM personas during multi-agent interaction. Setting a fixed threshold without empirical precedent would be arbitrary. Instead, we report: (a) paired t-test *p*-value, (b) Cohen's *d* effect size, and (c) direction of change for each trait. |
| **Cohen's *d* interpretation** | *d* = 0.20 small, 0.50 medium, 0.80 large (Cohen, 1988). We report *d* to enable future studies to compare against our results. |
| **Why paired t-test?** | Each session provides two measurements (Window 1 score, Window 3 score) of the same persona in the same scenario — a natural within-subjects design. |

---

**Metric 8: Decay rate — Correlation drop *r*(W1) − *r*(W3)**

| Justification | Rationale |
|---------------|-----------|
| **BehaviorChain precedent** | Li et al. (2025) demonstrated that LLM behavioral simulation accuracy degrades as behavior chains lengthen, with error accumulation across sequential predictions. This establishes that temporal decay is a real phenomenon in LLM persona simulation, motivating our measurement. However, BehaviorChain measures sequential behavior prediction, not personality expression, so their specific decay rates are not directly comparable. |
| **Interpretive guideline** | We propose: Δ*r* < 0.10 = negligible decay (persona is stable); Δ*r* = 0.10–0.20 = moderate decay (noticeable weakening); Δ*r* > 0.20 = substantial decay (persona fidelity degrades meaningfully). These bands are derived from the principle that a 0.20 drop in correlation corresponds to approximately halving the explained variance (e.g., *r* = .70 → .50 means R² drops from .49 to .25). |
| **TwinVoice context** | TwinVoice (2025) found that LLMs achieve moderate persona simulation accuracy (~47–76% depending on model and task) but fall short on memory recall and syntactic style — capabilities that are likely to degrade over longer interactions. This supports the hypothesis that decay is plausible and worth measuring. |

**Threshold decision:** No fixed pass/fail — report magnitude and effect size. The interpretive guideline (negligible / moderate / substantial) provides a framework without arbitrary cutoffs for a novel measurement.

---

#### Summary: Metrics at a Glance

| RQ | Metric | Threshold | Justification Source | Type |
|----|--------|-----------|---------------------|------|
| RQ1 | Pearson *r* | ≥ 0.60 (min: 0.40) | Cohen (1988) + BFI-44 test-retest + Park et al. (2024) | Psychometric + LLM benchmark |
| RQ1 | MAE | ≤ 0.15 (min: 0.20) | BFI-44 SEM + Likert equivalence + Park et al. (2024) | Psychometric + LLM benchmark |
| RQ1 | vs. Baseline A | *p* < 0.05 + Cohen's *d* | Fisher (1925) | Statistical standard |
| RQ1 | vs. Baseline B | Fisher *z*, *p* < 0.05 | Standard correlation comparison | Statistical standard |
| RQ2 | ICC | ≥ 0.70 (min: 0.50) | Koo & Li (2016) + Cicchetti (1994) + BFI-44 α | Reliability guidelines |
| RQ2 | Within-profile SD | ≤ 0.10 | BFI within-person variability + LLM consistency expectation | Psychometric + logical |
| RQ3 | Paired comparison | Report *d* | Cohen (1988) | Effect size convention |
| RQ3 | Correlation drop | Report Δ*r* | BehaviorChain decay precedent + variance interpretation | LLM benchmark + statistical |

**Interpretation framework:**

| Outcome | Interpretation | Implication |
|---------|---------------|-------------|
| RQ1 pass + RQ2 pass + RQ3 no decay | LLM personas are behaviorally faithful and robust | Strong evidence for trustworthy persona simulation |
| RQ1 pass + RQ2 fail | Traits are detectable but context-dependent | Personas are reliable only within specific scenarios |
| RQ1 pass + RQ3 shows decay | Traits are initially expressed but degrade over time | Personas have limited fidelity horizon — problematic for long simulations |
| RQ1 fail | Assigned traits are not behaviorally expressed | Fundamental limitation of current LLM persona simulation |

### 3.8 Validity Assessment

#### Internal Validity

| Threat | Mitigation |
|--------|-----------|
| **Circularity** (LLM evaluates LLM) | Cross-model evaluation (generation ≠ evaluation families) + rule-based features + evidence-traced scoring. DeepSeek V3 generates; Claude Haiku + Gemini + Grok evaluate. |
| **Experimenter bias** (profiles designed to succeed) | 4-category profile selection with balanced/moderate profiles included; Neutral Observer (all 0.5) tests discrimination at center |
| **Order effects** | Scenarios run in randomized order across repetitions |
| **Prompt leakage** | Evaluation is blind — judge receives only transcript, no profile information |

#### Construct Validity

| Question | Evidence |
|----------|---------|
| Does our "behavioral fidelity" measure what it claims? | We define fidelity through 3 independent dimensions (detectability, consistency, stability) rather than a single score |
| Do the scenarios actually elicit the target traits? | Each scenario has documented primary/secondary trait targets with specific pressure mechanisms |
| Are the behavioral features valid trait indicators? | Feature-trait mappings (e.g., words/turn → Extraversion) are grounded in established psycholinguistic literature |

#### External Validity (Limitations)

| Limitation | Scope Restriction |
|-----------|------------------|
| Single conversation model (DeepSeek V3) | Results are model-specific; different LLMs may show different fidelity patterns |
| English-language only | Big Five trait expression may differ across languages/cultures |
| Simulated pressure (not real stakes) | Real-world pressure may produce different behavioral responses |
| ~17 turns per session | Results may not generalize to longer interactions |

---

## 4. Limitations & Risk Awareness (한계 인식)

### 4.1 Acknowledged Limitations (with mitigation status)

| # | Limitation | Severity | Mitigation | Status |
|---|-----------|----------|-----------|--------|
| L1 | **LLM-LLM circularity** | High | Cross-model ensemble + rule-based features | ✅ Addressed |
| L2 | **No human ground truth** | High | Frame conclusions as "computational detectability", not "human-equivalent fidelity" | ✅ Addressed via scope framing |
| L3 | **Model version dependency** | Medium | Pin exact model versions; note that results are version-specific | ✅ Easy to implement |
| L4 | **RLHF sycophancy bias** | Medium | Pressure scenarios designed to break through default compliance; measure whether it succeeds | ✅ Built into design |
| L5 | **12 profiles ≠ full Big Five space** | Medium | 4-category selection principle documented; acknowledge as limitation | ✅ Addressed via design rationale |
| L6 | **Agent interaction confounds** | Medium | Alex/Jordan/Riley prompts are fixed; treated as "controlled interactional stimulus" rather than confounding variable | ✅ Addressed via framing |
| L7 | **Facet-level granularity** | Low | Out of scope; trait-level is sufficient for FYP | 📌 Future work |
| L8 | **Cultural/language bias** | Low | English-only Big Five; acknowledged as limitation | 📌 Future work |
| L9 | **Long-horizon generalization** | Low | 17 turns ≠ multi-day simulation; acknowledged | 📌 Future work |

### 4.2 What This Study Does Not Prove

This section is crucial for defense during presentation:

1. **Does NOT prove** that LLM personas can replace human participants in research
2. **Does NOT prove** that personality assessment via LLM is clinically valid
3. **Does NOT prove** that results generalize to other LLMs, languages, or longer interactions
4. **DOES demonstrate** whether assigned personality traits produce measurably distinct behavioral patterns in controlled interactive settings
5. **DOES provide** a reusable evaluation framework (profiles, scenarios, metrics) for future personality fidelity research

### 4.3 Honest Risk Assessment

| Risk | Probability | Impact | Contingency |
|------|-------------|--------|-------------|
| RQ1 fails entirely (no trait detectability) | Low (20%) | High | Negative result is still publishable — "LLM personas lack behavioral fidelity" is an important finding |
| Partial RQ1 (some traits detectable, others not) | High (50%) | Medium | Analyze which traits succeed/fail — this is actually the most interesting and nuanced outcome |
| RQ2 shows scenario dependency | Medium (40%) | Low | Report as finding: "trait expression is context-dependent" — has implications for simulation design |
| RQ3 shows significant decay | Medium (40%) | Low | Report as finding: "persona fidelity has temporal limits" — directly useful for practitioners |
| Computational cost exceeds budget | Low (15%) | Medium | Reduce reps from 3→2 or baselines from 20→10 sessions |

---

## 5. Significance (연구의 의의)

### 5.1 Academic Significance

**Gap in existing literature:**

| Existing Work | What They Evaluate | What They Miss |
|--------------|-------------------|---------------|
| BehaviorChain (ACL 2025) | Sequential behavior prediction | No multi-agent interaction, no personality traits |
| TwinVoice (2025) | Communication style fidelity | No Big Five, no pressure/conflict |
| Persona Generators (DeepMind 2026) | Diversity of synthetic populations | No behavioral validation of generated personas |
| Park et al. (2024) | 1000-person simulation fidelity | Questionnaire-based, no interactive behavior |
| Santurkar et al. (2023) | LLM opinion alignment by demographics | No personality traits, no interaction |

**This study fills the intersection:**
- ✅ Interactive (multi-agent, not single-agent)
- ✅ Personality-grounded (Big Five, not demographics)
- ✅ Pressure-tested (conflict scenarios, not casual conversation)
- ✅ Temporally analyzed (decay over conversation)
- ✅ Multi-metric (LLM judge + rule-based features)

### 5.2 Methodological Significance

This study establishes a **persona fidelity validation protocol** that can be reused:

1. **Profile design framework** — 4-category selection principle for covering trait space
2. **Scenario–trait mapping** — linking pressure scenarios to specific trait elicitation
3. **3-dimensional fidelity definition** — detectability, consistency, stability
4. **Cross-model evaluation standard** — generation model ≠ evaluation model
5. **Behavioral feature battery** — rule-based metrics as LLM-independent validation

Anyone building LLM-based digital twins can use this protocol to validate their personas before deployment.

### 5.3 Practical Significance (Long-term Vision)

**Immediate (FYP):**
- Benchmark dataset: 164 annotated group conversation transcripts with ground-truth personality profiles
- Reusable evaluation framework for LLM persona validation

**Near-term (1-2 years):**
- Persona QA toolkit — validate synthetic agents before deployment
- Training simulation calibration — ensure simulated negotiators/customers/patients behave as specified

**Long-term vision (3-5 years):**
The ultimate goal is building **trustworthy LLM-based simulation infrastructure** for:

| Application | Use Case | Why Fidelity Matters |
|------------|----------|---------------------|
| **Negotiation training** | Simulate counterparts with specific personality profiles | Trainees need to practice against genuinely assertive/passive/anxious opponents, not uniformly polite ones |
| **Policy impact simulation** | Model population behavioral responses to new policies | If all simulated citizens are agreeable, policy stress-tests miss resistance patterns |
| **Business scenario modeling** | Simulate customer segments, team dynamics, market reactions | Consumer digital twins must reflect real preference diversity, not RLHF-averaged behavior |
| **Assessment & hiring** | Pre-validate interview tools against known personality profiles | Assessment systems must discriminate between personalities before being deployed on real candidates |

**This FYP is Step 0:** Before building any of these applications, you need to answer: *"Can we trust that LLM personas behave according to their assigned traits?"* If the answer is no, the entire downstream infrastructure is built on sand.

---

## 6. Experiment Protocol (실험 프로토콜 요약)

```
┌─────────────────────────────────────────────────────────────┐
│                   EXPERIMENT PROTOCOL                        │
├─────────────────────────────────────────────────────────────┤
│ RQ1: Are assigned Big Five traits detectable from            │
│      group conversation transcripts?                         │
│ RQ2: Is trait expression consistent across scenarios         │
│      and repetitions?                                        │
│ RQ3: Does trait expression decay over conversation length?   │
├─────────────────────────────────────────────────────────────┤
│ IV:  12 personality profiles (OCEAN values: Table 3.2)       │
│      4 conflict scenarios (trait mapping: Table 3.3)         │
│ DV:  LLM-inferred OCEAN (ensemble, blind) + behavioral      │
│      statistics (rule-based)                                 │
│ Control: Temperature (0.7/0.3), turn count (~17),            │
│          agent prompts (fixed), model versions (pinned)      │
├─────────────────────────────────────────────────────────────┤
│ Main Experiment:  12 profiles × 4 scenarios × 3 reps = 144  │
│ Baseline A:       No-persona × 4 scenarios × 3 reps = 12    │
│ Baseline B:       Random-persona × 4 scenarios × 2 reps = 8 │
│ Total:            164 sessions                               │
├─────────────────────────────────────────────────────────────┤
│ Metrics:                                                     │
│   RQ1 → Pearson r ≥ 0.60, MAE ≤ 0.15, t-test vs baselines  │
│   RQ2 → ICC ≥ 0.70, within-profile SD ≤ 0.10               │
│   RQ3 → Paired comparison (Window 1 vs 3), Cohen's d        │
├─────────────────────────────────────────────────────────────┤
│ Models:                                                      │
│   Conversation: DeepSeek V3 (temp 0.7)                       │
│   Evaluation:   Claude 3.5 Haiku + Gemini 2.5 Flash +       │
│                 Grok 4.1 Fast (temp 0.3, median aggregation) │
│   (DeepSeek removed from eval to eliminate circularity)      │
├─────────────────────────────────────────────────────────────┤
│ Limitations (top 3):                                         │
│   1. LLM-LLM circularity (mitigated: cross-model + rules)   │
│   2. No human validation (scope: computational only)         │
│   3. Model version dependency (pin versions, report)         │
└─────────────────────────────────────────────────────────────┘
```

---

## 6A. Implementation Specification (코딩 바로 시작 가능한 수준)

This section provides coding-ready specifications for all components that need to be built. Each subsection includes the exact file location, data structures, function signatures, and step-by-step logic.

### 6A.1 Candidate Agent Automation (`experiment/candidate_agent.py`)

The candidate in the experiment is NOT a human — it is an LLM agent with an assigned personality profile. This agent replaces `submit_candidate_turn()` in the human-interactive flow.

```python
"""
Automated Candidate Agent for Behavioral Fidelity Experiment.
Replaces human candidate with LLM agent using personality-injected prompts.
"""
import asyncio
from dataclasses import dataclass
from utils.models import PersonalityVector

@dataclass
class ExperimentProfile:
    """A personality profile for the experiment."""
    id: str                          # e.g., "assertive_leader"
    name: str                        # e.g., "Assertive Leader"
    display_name: str                # e.g., "Candidate"  (fixed for all)
    vector: PersonalityVector        # OCEAN values
    category: str                    # "extreme" | "socially_challenging" | "balanced" | "domain_relevant"

    def get_level(self, value: float) -> str:
        """Convert 0-1 value to High/Moderate/Low label."""
        if value >= 0.7:
            return "High"
        elif value <= 0.3:
            return "Low"
        elif value >= 0.6:
            return "Moderate-High"
        elif value <= 0.4:
            return "Moderate-Low"
        else:
            return "Moderate"

    def build_system_prompt(self, scenario_brief: str) -> str:
        """Build the full candidate system prompt from OCEAN values."""
        # See Section 3.2.1 for the template and behavioral instruction mapping
        # Implementation: select behavioral instruction per trait based on level
        ...

EXPERIMENT_PROFILES: dict[str, ExperimentProfile] = {
    "assertive_leader": ExperimentProfile(
        id="assertive_leader", name="Assertive Leader",
        display_name="Candidate",
        vector=PersonalityVector(O=0.6, C=0.8, E=0.9, A=0.4, N=0.2),
        category="extreme",
    ),
    # ... (all 12 profiles from Table 3.2)
}
```

**Candidate turn generation flow:**

```
1. GroupEngine calls generate_ai_response() → AI agents respond
2. Instead of waiting for human input, BatchRunner calls:
   candidate_response = await candidate_agent.generate_response(
       turns=engine.turns,
       scenario_brief=scenario.brief,
       phase_style=current_phase_config.style,
   )
3. engine.submit_candidate_turn(candidate_response)
4. Loop until all phases complete
```

**Key parameter:** Candidate agent uses **temperature 0.7** for conversation generation (same as AI agents). This is the IV temperature — distinct from evaluation temperature (0.3).

### 6A.2 Batch Runner (`experiment/batch_runner.py`)

**Purpose:** Execute all 164 sessions sequentially with automatic saving.

```python
"""
Batch Runner: Execute 164 experiment sessions sequentially.
Saves results incrementally to prevent data loss.
"""
import asyncio
import json
import random
import time
from pathlib import Path
from datetime import datetime

@dataclass
class ExperimentConfig:
    profiles: list[str]           # 12 profile IDs
    scenarios: list[str]          # 4 scenario IDs
    repetitions: int = 3          # 3 reps per profile×scenario
    baseline_a_reps: int = 3      # no-persona baseline
    baseline_b_reps: int = 2      # random-persona baseline
    output_dir: Path = Path("experiment/results")
    save_every: int = 1           # Save after every session

class BatchRunner:
    def __init__(self, config: ExperimentConfig, client: LLMClient):
        self.config = config
        self.client = client
        self.results: list[dict] = []
        self.failed: list[dict] = []

    async def run_all(self):
        """Execute all 164 sessions."""
        sessions = self._build_session_list()
        random.shuffle(sessions)  # Randomize order to prevent systematic effects

        for i, session in enumerate(sessions):
            print(f"\n{'='*60}")
            print(f"Session {i+1}/{len(sessions)}: {session['profile_id']} × {session['scenario_id']} (rep {session['rep']})")
            print(f"Condition: {session['condition']}")
            print(f"{'='*60}")

            try:
                result = await self._run_single_session(session)
                self.results.append(result)
                self._save_incremental(result, i)
            except Exception as e:
                print(f"FAILED: {e}")
                self.failed.append({**session, "error": str(e)})
                self._save_failures()

            # Rate limit: wait between sessions
            if i < len(sessions) - 1:
                await asyncio.sleep(2.0)

        self._save_final_summary()

    def _build_session_list(self) -> list[dict]:
        """Build list of all 164 sessions."""
        sessions = []

        # Main experiment: 12 × 4 × 3 = 144
        for profile_id in self.config.profiles:
            for scenario_id in self.config.scenarios:
                for rep in range(self.config.repetitions):
                    sessions.append({
                        "condition": "main",
                        "profile_id": profile_id,
                        "scenario_id": scenario_id,
                        "rep": rep + 1,
                    })

        # Baseline A (no-persona): 4 × 3 = 12
        for scenario_id in self.config.scenarios:
            for rep in range(self.config.baseline_a_reps):
                sessions.append({
                    "condition": "baseline_a",
                    "profile_id": "no_persona",
                    "scenario_id": scenario_id,
                    "rep": rep + 1,
                })

        # Baseline B (random-persona): 4 × 2 = 8
        for scenario_id in self.config.scenarios:
            for rep in range(self.config.baseline_b_reps):
                sessions.append({
                    "condition": "baseline_b",
                    "profile_id": "random_persona",
                    "scenario_id": scenario_id,
                    "rep": rep + 1,
                })

        return sessions  # Total: 164

    async def _run_single_session(self, session: dict) -> dict:
        """Run one session and return results."""
        # 1. Create engine with scenario
        scenario = create_scenario(session["scenario_id"])
        engine = GroupEngine(
            client=self.client,
            participant_id=f"exp_{session['condition']}_{session['profile_id']}_{session['scenario_id']}_r{session['rep']}",
            participant_name="Candidate",
            scenario=scenario,
        )

        # 2. Create candidate agent based on condition
        if session["condition"] == "baseline_a":
            candidate_prompt = None  # No personality injection
        elif session["condition"] == "baseline_b":
            # Random: shuffle OCEAN values from a random profile
            random_profile = random.choice(list(EXPERIMENT_PROFILES.values()))
            shuffled = random.sample(
                [random_profile.vector.O, random_profile.vector.C,
                 random_profile.vector.E, random_profile.vector.A,
                 random_profile.vector.N], 5
            )
            candidate_prompt = build_system_prompt(
                PersonalityVector(O=shuffled[0], C=shuffled[1], E=shuffled[2], A=shuffled[3], N=shuffled[4]),
                scenario.brief,
            )
        else:
            profile = EXPERIMENT_PROFILES[session["profile_id"]]
            candidate_prompt = profile.build_system_prompt(scenario.brief)

        # 3. Run session loop
        opening_turns = await engine.generate_opening()
        max_turns = sum(phase.turns for phase in scenario.phases)

        for turn_idx in range(max_turns):
            # Generate candidate response
            candidate_response = await self._generate_candidate_turn(
                engine.turns, candidate_prompt, scenario.brief
            )
            await engine.submit_candidate_turn(candidate_response)

            # Generate AI response(s)
            ai_turns = await engine.generate_ai_response()

            if engine.state == SessionState.ENDED:
                break

        # 4. Compute stats and build output
        stats = engine.compute_session_stats()
        output = engine.to_session_output()

        # 5. Run evaluation (ensemble, blind — no profile info)
        assessment = await evaluate_group_session(
            client=self.eval_client,  # DIFFERENT client with eval-only models
            turns=engine.turns,
            candidate_name="Candidate",
            stats=stats,
            use_ensemble=True,
        )

        return {
            "session_id": output.session_id,
            "condition": session["condition"],
            "profile_id": session["profile_id"],
            "scenario_id": session["scenario_id"],
            "rep": session["rep"],
            "assigned_vector": session.get("assigned_vector", None),
            "inferred_vector": {
                "O": assessment.openness.score,
                "C": assessment.conscientiousness.score,
                "E": assessment.extraversion.score,
                "A": assessment.agreeableness.score,
                "N": assessment.neuroticism.score,
            },
            "confidence": {
                "O": assessment.openness.confidence,
                "C": assessment.conscientiousness.confidence,
                "E": assessment.extraversion.confidence,
                "A": assessment.agreeableness.confidence,
                "N": assessment.neuroticism.confidence,
            },
            "stats": {
                "total_turns": stats.total_turns,
                "candidate_turns": stats.candidate_turns,
                "avg_words_per_turn": stats.candidate_avg_words_per_turn,
                "questions": stats.times_asked_questions,
                "disagreements": stats.times_expressed_disagreement,
                "acknowledgments": stats.times_acknowledged_others,
                "new_ideas": stats.times_proposed_new_ideas,
            },
            "turns": [{"turn": t.turn_number, "speaker": t.speaker_name, "content": t.content}
                      for t in engine.turns],
            "timestamp": datetime.now().isoformat(),
        }
```

**API Call Estimate:**

| Component | Calls per Session | Sessions | Total |
|-----------|-------------------|----------|-------|
| AI agent responses (~17 turns, ~1.5 AI turns per candidate turn) | ~12 | 164 | ~1,968 |
| Candidate agent responses | ~8 | 164 | ~1,312 |
| Evaluation (5 traits × 3 models) | 15 | 164 | ~2,460 |
| Temporal window evaluation (5 traits × 3 models × 3 windows) | 45 | 144 | ~6,480 |
| **Total** | | | **~12,220** |

**Cost Estimate (OpenRouter pricing, March 2026):**

| Model | Usage | Approx. Cost |
|-------|-------|-------------|
| DeepSeek V3 (conversation) | ~3,280 calls × ~600 tokens avg | ~$2–4 |
| DeepSeek V3 (eval, to be replaced) | ~2,160 calls × ~1,000 tokens | ~$2–3 |
| Gemini 2.5 Flash (eval) | ~2,160 calls × ~1,000 tokens | ~$3–5 |
| Grok 4.1 Fast (eval) | ~2,160 calls × ~1,000 tokens | ~$3–5 |
| **Total estimated** | | **~$10–17** |

**Execution Time Estimate:**
- Rate limit: 60 RPM → ~204 minutes for 12,220 calls
- LLM latency: ~2-5 seconds per call → additional overhead
- **Total: ~6-10 hours** (run overnight)

### 6A.3 Temporal Window Split (`experiment/temporal_analysis.py`)

**Purpose:** Split each session transcript into 3 temporal windows for RQ3 decay analysis. The split is based on phase boundaries (which map to turn ranges), NOT arbitrary turn counts.

```python
"""
Temporal Window Analysis: Split transcripts by phase for decay measurement.
"""
from utils.models import Turn

# Phase → Window mapping (defined by session structure)
PHASE_TO_WINDOW = {
    # Standard 5-phase scenarios
    "INTRODUCTION": "early",    # Window 1: Phases 1-2
    "EXPLORATION": "early",
    "IDEATION": "early",        # Creative Brainstorm variant
    "WELCOME": "early",         # New Member variant
    "CONTEXT_SHARING": "early",
    "CONFLICT": "peak",         # Window 2: Phase 3 (pressure)
    "EVALUATION": "peak",
    "DEFENSE": "peak",
    "INITIAL_REACTION": "peak",
    "PROBLEM_SOLVING": "peak",
    "CRISIS_REVEAL": "peak",
    "STRESS_TEST": "peak",
    "ROLE_NEGOTIATION": "peak",
    "RESOLUTION": "late",       # Window 3: Phases 4-5 (recovery)
    "CLOSING": "late",
}

def split_into_windows(
    turns: list[Turn],
    scenario_phases: list,  # list of GroupScenarioPhase
) -> dict[str, list[Turn]]:
    """
    Split transcript into 3 temporal windows based on phase boundaries.

    Returns:
        {"early": [...], "peak": [...], "late": [...]}
    """
    windows = {"early": [], "peak": [], "late": []}

    # Build turn → phase mapping from phase configs
    turn_to_phase = {}
    cumulative_turn = 0
    for phase in scenario_phases:
        for t in range(phase.turns):
            # Each phase.turns covers CANDIDATE turns;
            # but we also have AI turns interspersed.
            # We track by sequential turn number.
            turn_to_phase[cumulative_turn] = phase.name
            cumulative_turn += 1

    # Map each turn to its window
    phase_boundaries = _compute_phase_boundaries(scenario_phases, len(turns))

    current_phase_idx = 0
    for turn in turns:
        # Determine which phase this turn belongs to
        while (current_phase_idx < len(phase_boundaries) - 1 and
               turn.turn_number >= phase_boundaries[current_phase_idx + 1]):
            current_phase_idx += 1

        phase_name = scenario_phases[min(current_phase_idx, len(scenario_phases)-1)].name
        window = PHASE_TO_WINDOW.get(phase_name, "early")
        windows[window].append(turn)

    return windows


def _compute_phase_boundaries(phases: list, total_turns: int) -> list[int]:
    """
    Compute turn number boundaries for each phase.

    Since phases define candidate turn counts but actual turn numbers
    include AI turns, we estimate proportionally.
    """
    total_phase_turns = sum(p.turns for p in phases)
    boundaries = [0]
    cumulative = 0
    for phase in phases:
        cumulative += phase.turns
        boundary = int((cumulative / total_phase_turns) * total_turns)
        boundaries.append(boundary)
    return boundaries


async def evaluate_per_window(
    eval_client,
    turns: list[Turn],
    scenario_phases: list,
    candidate_name: str,
    stats,
) -> dict[str, dict]:
    """
    Run trait evaluation on each temporal window separately.

    Returns:
        {
            "early":  {"O": 0.7, "C": 0.8, ...},
            "peak":   {"O": 0.6, "C": 0.7, ...},
            "late":   {"O": 0.5, "C": 0.6, ...},
        }
    """
    windows = split_into_windows(turns, scenario_phases)
    results = {}

    for window_name, window_turns in windows.items():
        if len(window_turns) < 3:
            # Too few turns for meaningful evaluation
            results[window_name] = None
            continue

        # Compute window-specific stats
        window_stats = compute_window_stats(window_turns, candidate_name)

        # Run ensemble evaluation on window subset
        assessment = await evaluate_group_session(
            client=eval_client,
            turns=window_turns,
            candidate_name=candidate_name,
            stats=window_stats,
            use_ensemble=True,
        )

        results[window_name] = {
            "O": assessment.openness.score,
            "C": assessment.conscientiousness.score,
            "E": assessment.extraversion.score,
            "A": assessment.agreeableness.score,
            "N": assessment.neuroticism.score,
        }

    return results
```

**Key implementation notes:**
- Window boundaries are **phase-based**, not arbitrary turn splits
- Each window gets **independent** behavioral stats (word count, questions, etc. for that window only)
- The evaluation prompt receives **only the window's turns** — no full-session context leaks
- Minimum 3 turns per window to produce a meaningful evaluation

### 6A.4 Statistical Analysis Pipeline (`experiment/analysis.py`)

**Purpose:** Compute all metrics for RQ1, RQ2, RQ3 from experiment results.

```python
"""
Statistical Analysis Pipeline for Behavioral Fidelity Experiment.
Dependencies: pandas, scipy, numpy, pingouin (for ICC)
"""
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import pearsonr, ttest_ind, ttest_rel
import pingouin as pg  # pip install pingouin — for ICC computation

# ============================================================
# STEP 1: Load results into DataFrame
# ============================================================

def load_results(results_dir: str) -> pd.DataFrame:
    """
    Load all session results into a single DataFrame.

    Expected columns after processing:
    - session_id, condition, profile_id, scenario_id, rep
    - assigned_O, assigned_C, assigned_E, assigned_A, assigned_N
    - inferred_O, inferred_C, inferred_E, inferred_A, inferred_N
    - conf_O, conf_C, conf_E, conf_A, conf_N
    - avg_words, questions, disagreements, acknowledgments, new_ideas
    """
    import json
    from pathlib import Path

    records = []
    for f in Path(results_dir).glob("session_*.json"):
        with open(f) as fp:
            data = json.load(fp)

        profile = EXPERIMENT_PROFILES.get(data["profile_id"])
        assigned = profile.vector.to_dict() if profile else {t: None for t in "OCEAN"}

        records.append({
            "session_id": data["session_id"],
            "condition": data["condition"],
            "profile_id": data["profile_id"],
            "scenario_id": data["scenario_id"],
            "rep": data["rep"],
            # Assigned (IV)
            "assigned_O": assigned.get("O"), "assigned_C": assigned.get("C"),
            "assigned_E": assigned.get("E"), "assigned_A": assigned.get("A"),
            "assigned_N": assigned.get("N"),
            # Inferred (DV)
            "inferred_O": data["inferred_vector"]["O"],
            "inferred_C": data["inferred_vector"]["C"],
            "inferred_E": data["inferred_vector"]["E"],
            "inferred_A": data["inferred_vector"]["A"],
            "inferred_N": data["inferred_vector"]["N"],
            # Confidence
            "conf_O": data["confidence"]["O"], "conf_C": data["confidence"]["C"],
            "conf_E": data["confidence"]["E"], "conf_A": data["confidence"]["A"],
            "conf_N": data["confidence"]["N"],
            # Behavioral stats
            "avg_words": data["stats"]["avg_words_per_turn"],
            "questions": data["stats"]["questions"],
            "disagreements": data["stats"]["disagreements"],
            "acknowledgments": data["stats"]["acknowledgments"],
            "new_ideas": data["stats"]["new_ideas"],
        })

    return pd.DataFrame(records)


# ============================================================
# STEP 2: RQ1 — Trait Detectability
# ============================================================

def rq1_analysis(df: pd.DataFrame) -> dict:
    """Compute RQ1 metrics: Pearson r, MAE, baseline comparisons."""
    main = df[df["condition"] == "main"]
    results = {}

    traits = ["O", "C", "E", "A", "N"]
    trait_names = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

    # --- Metric 1 & 2: Pearson r and MAE per trait ---
    for trait, name in zip(traits, trait_names):
        assigned = main[f"assigned_{trait}"]
        inferred = main[f"inferred_{trait}"]

        r, p = pearsonr(assigned, inferred)
        mae = np.mean(np.abs(assigned - inferred))

        results[name] = {
            "pearson_r": round(r, 4),
            "r_p_value": round(p, 6),
            "mae": round(mae, 4),
            "n": len(assigned),
            "r_pass": r >= 0.60,
            "mae_pass": mae <= 0.15,
        }

    # --- Metric 3: Main vs Baseline A (t-test on trait score variance) ---
    baseline_a = df[df["condition"] == "baseline_a"]
    for trait, name in zip(traits, trait_names):
        main_scores = main[f"inferred_{trait}"]
        base_scores = baseline_a[f"inferred_{trait}"]

        # Compare variance (F-test) and mean difference (t-test)
        t_stat, p_val = ttest_ind(main_scores, base_scores)
        cohens_d = (main_scores.mean() - base_scores.mean()) / np.sqrt(
            (main_scores.var() + base_scores.var()) / 2
        )
        # Also compare variance: Levene's test
        levene_stat, levene_p = stats.levene(main_scores, base_scores)

        results[name]["vs_baseline_a"] = {
            "t_stat": round(t_stat, 4),
            "p_value": round(p_val, 6),
            "cohens_d": round(cohens_d, 4),
            "main_var": round(main_scores.var(), 4),
            "baseline_var": round(base_scores.var(), 4),
            "levene_p": round(levene_p, 6),
        }

    # --- Metric 4: Main vs Baseline B (Fisher z-test on correlations) ---
    baseline_b = df[df["condition"] == "baseline_b"]
    # For baseline B: correlate the ASSIGNED label (which is mismatched) with inferred
    for trait, name in zip(traits, trait_names):
        main_r = results[name]["pearson_r"]
        n_main = results[name]["n"]

        if len(baseline_b) >= 5:
            base_assigned = baseline_b[f"assigned_{trait}"]
            base_inferred = baseline_b[f"inferred_{trait}"]
            base_r, _ = pearsonr(base_assigned, base_inferred) if len(base_assigned) > 2 else (0, 1)
            n_base = len(base_assigned)

            # Fisher z-transformation
            z_main = np.arctanh(main_r)
            z_base = np.arctanh(base_r) if abs(base_r) < 0.999 else np.arctanh(0.999 * np.sign(base_r))
            se = np.sqrt(1/(n_main-3) + 1/(n_base-3))
            z_diff = (z_main - z_base) / se
            p_fisher = 2 * (1 - stats.norm.cdf(abs(z_diff)))

            results[name]["vs_baseline_b"] = {
                "main_r": round(main_r, 4),
                "baseline_r": round(base_r, 4),
                "fisher_z": round(z_diff, 4),
                "p_value": round(p_fisher, 6),
            }

    # --- Overall correlation (all traits pooled) ---
    all_assigned = pd.concat([main[f"assigned_{t}"] for t in traits])
    all_inferred = pd.concat([main[f"inferred_{t}"] for t in traits])
    overall_r, overall_p = pearsonr(all_assigned, all_inferred)
    overall_mae = np.mean(np.abs(all_assigned - all_inferred))

    results["overall"] = {
        "pearson_r": round(overall_r, 4),
        "p_value": round(overall_p, 6),
        "mae": round(overall_mae, 4),
    }

    return results


# ============================================================
# STEP 3: RQ2 — Trait Consistency
# ============================================================

def rq2_analysis(df: pd.DataFrame) -> dict:
    """Compute RQ2 metrics: ICC across scenarios, within-profile SD."""
    main = df[df["condition"] == "main"]
    results = {}
    traits = ["O", "C", "E", "A", "N"]
    trait_names = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

    for trait, name in zip(traits, trait_names):
        # --- Metric 5: ICC across scenarios ---
        # Reshape: rows = profile × rep, columns = scenarios
        icc_data = main.pivot_table(
            index=["profile_id", "rep"],
            columns="scenario_id",
            values=f"inferred_{trait}",
        ).reset_index()

        # pingouin ICC requires long format: targets (subjects), raters, ratings
        icc_long = main[["profile_id", "rep", "scenario_id", f"inferred_{trait}"]].copy()
        icc_long["subject"] = icc_long["profile_id"] + "_" + icc_long["rep"].astype(str)
        icc_long = icc_long.rename(columns={
            "scenario_id": "rater",
            f"inferred_{trait}": "rating",
        })

        try:
            icc_result = pg.intraclass_corr(
                data=icc_long, targets="subject", raters="rater", ratings="rating"
            )
            # Use ICC3k (two-way mixed, average measures, absolute agreement)
            icc3k = icc_result[icc_result["Type"] == "ICC3k"]["ICC"].values[0]
        except Exception:
            icc3k = None

        # --- Metric 6: Within-profile SD (across repetitions within same scenario) ---
        within_sds = []
        for profile_id in main["profile_id"].unique():
            for scenario_id in main["scenario_id"].unique():
                subset = main[
                    (main["profile_id"] == profile_id) &
                    (main["scenario_id"] == scenario_id)
                ][f"inferred_{trait}"]
                if len(subset) >= 2:
                    within_sds.append(subset.std())

        mean_within_sd = np.mean(within_sds) if within_sds else None

        results[name] = {
            "icc3k": round(icc3k, 4) if icc3k is not None else None,
            "icc_pass": icc3k >= 0.70 if icc3k is not None else False,
            "mean_within_sd": round(mean_within_sd, 4) if mean_within_sd is not None else None,
            "sd_pass": mean_within_sd <= 0.10 if mean_within_sd is not None else False,
        }

    return results


# ============================================================
# STEP 4: RQ3 — Temporal Decay
# ============================================================

def rq3_analysis(window_results: list[dict]) -> dict:
    """
    Compute RQ3 metrics from temporal window evaluation results.

    Input: list of dicts with keys:
        - profile_id, scenario_id, rep
        - early: {O, C, E, A, N}
        - peak: {O, C, E, A, N}
        - late: {O, C, E, A, N}
        - assigned: {O, C, E, A, N}
    """
    df = pd.DataFrame(window_results)
    results = {}
    traits = ["O", "C", "E", "A", "N"]
    trait_names = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

    for trait, name in zip(traits, trait_names):
        early_scores = df[f"early_{trait}"]
        late_scores = df[f"late_{trait}"]
        assigned_scores = df[f"assigned_{trait}"]

        # Paired t-test: Window 1 vs Window 3
        t_stat, p_val = ttest_rel(early_scores, late_scores)

        # Cohen's d (paired)
        diff = early_scores - late_scores
        cohens_d = diff.mean() / diff.std() if diff.std() > 0 else 0

        # Correlation drop: r(assigned, early) - r(assigned, late)
        r_early, _ = pearsonr(assigned_scores, early_scores)
        r_late, _ = pearsonr(assigned_scores, late_scores)
        delta_r = r_early - r_late

        # Decay classification
        if abs(delta_r) < 0.10:
            decay_level = "negligible"
        elif abs(delta_r) < 0.20:
            decay_level = "moderate"
        else:
            decay_level = "substantial"

        results[name] = {
            "early_mean": round(early_scores.mean(), 4),
            "late_mean": round(late_scores.mean(), 4),
            "t_stat": round(t_stat, 4),
            "p_value": round(p_val, 6),
            "cohens_d": round(cohens_d, 4),
            "r_early": round(r_early, 4),
            "r_late": round(r_late, 4),
            "delta_r": round(delta_r, 4),
            "decay_level": decay_level,
        }

    return results


# ============================================================
# STEP 5: Rule-Based Feature Correlation
# ============================================================

def rule_based_validation(df: pd.DataFrame) -> dict:
    """
    Correlate rule-based behavioral features with inferred trait scores.
    This provides LLM-independent validation.
    """
    main = df[df["condition"] == "main"]
    correlations = {}

    feature_trait_pairs = [
        ("avg_words", "inferred_E", "Extraversion", "+"),
        ("questions", "inferred_O", "Openness", "+"),
        ("disagreements", "inferred_A", "Agreeableness", "−"),
        ("acknowledgments", "inferred_A", "Agreeableness", "+"),
        ("new_ideas", "inferred_O", "Openness", "+"),
    ]

    for feature, trait_col, trait_name, expected_dir in feature_trait_pairs:
        r, p = pearsonr(main[feature], main[trait_col])
        direction_match = (r > 0 and expected_dir == "+") or (r < 0 and expected_dir == "−")

        correlations[f"{feature}_vs_{trait_name}"] = {
            "r": round(r, 4),
            "p": round(p, 6),
            "expected_direction": expected_dir,
            "direction_match": direction_match,
        }

    return correlations


# ============================================================
# STEP 6: Generate Summary Report
# ============================================================

def generate_report(rq1, rq2, rq3, rule_based) -> str:
    """Generate a formatted summary report."""
    lines = ["# Behavioral Fidelity Experiment — Results Summary\n"]
    lines.append(f"Generated: {datetime.now().isoformat()}\n")

    lines.append("## RQ1: Trait Detectability\n")
    for trait, data in rq1.items():
        if trait == "overall":
            continue
        r_status = "✅" if data.get("r_pass") else "❌"
        mae_status = "✅" if data.get("mae_pass") else "❌"
        lines.append(f"- **{trait}**: r={data['pearson_r']} {r_status}  MAE={data['mae']} {mae_status}")

    lines.append(f"\n**Overall**: r={rq1['overall']['pearson_r']}, MAE={rq1['overall']['mae']}\n")

    lines.append("## RQ2: Trait Consistency\n")
    for trait, data in rq2.items():
        icc_status = "✅" if data.get("icc_pass") else "❌"
        sd_status = "✅" if data.get("sd_pass") else "❌"
        lines.append(f"- **{trait}**: ICC={data['icc3k']} {icc_status}  SD={data['mean_within_sd']} {sd_status}")

    lines.append("\n## RQ3: Temporal Decay\n")
    for trait, data in rq3.items():
        lines.append(f"- **{trait}**: Δr={data['delta_r']} ({data['decay_level']}), d={data['cohens_d']}, p={data['p_value']}")

    lines.append("\n## Rule-Based Validation\n")
    for pair, data in rule_based.items():
        match_status = "✅" if data["direction_match"] else "⚠️"
        lines.append(f"- {pair}: r={data['r']}, p={data['p']} {match_status}")

    return "\n".join(lines)
```

**Required Python packages:**
```
pip install pandas numpy scipy pingouin
```

### 6A.5 Cross-Model Circularity Resolution

**Problem identified:** DeepSeek V3 is currently used for BOTH conversation generation AND as one of the 3 ensemble evaluation models. This creates circularity — the same model family that generates behavior also judges it.

**Resolution: Remove DeepSeek V3 from the evaluation ensemble.**

| Role | Current | Resolved |
|------|---------|----------|
| **Conversation generation** | DeepSeek V3 | DeepSeek V3 (unchanged) |
| **Evaluation Model 1** | ~~DeepSeek V3~~ | **Claude 3.5 Haiku** (`anthropic/claude-3.5-haiku`) |
| **Evaluation Model 2** | Gemini 2.5 Flash | Gemini 2.5 Flash (unchanged) |
| **Evaluation Model 3** | Grok 4.1 Fast | Grok 4.1 Fast (unchanged) |

**Why Claude 3.5 Haiku as replacement:**
- Different model family (Anthropic vs. DeepSeek) — eliminates circularity
- Fast inference speed suitable for batch evaluation
- Competitive instruction-following and JSON output parsing
- Cost-effective for 2,000+ evaluation calls

**Implementation change in `clients/llm_client.py`:**
```python
# BEFORE (circular)
self.ensemble_models = [
    "deepseek/deepseek-chat-v3-0324",  # SAME as generation model
    "google/gemini-2.5-flash",
    "x-ai/grok-4.1-fast",
]

# AFTER (resolved)
self.ensemble_models = [
    "anthropic/claude-3.5-haiku",      # Different family from generation
    "google/gemini-2.5-flash",
    "x-ai/grok-4.1-fast",
]
```

**For the batch runner, use two separate clients:**
```python
# Conversation generation client
gen_client = LLMClient(pro_model="deepseek/deepseek-chat-v3-0324")

# Evaluation client (no DeepSeek)
eval_client = LLMClient()
eval_client.ensemble_models = [
    "anthropic/claude-3.5-haiku",
    "google/gemini-2.5-flash",
    "x-ai/grok-4.1-fast",
]
```

### 6A.6 Baseline Prompt Specifications

**Baseline A (No-Persona):**
```
You are a participant in a group discussion about a workplace scenario.

## Current Scenario
{scenario_brief}

## Instructions
- Respond naturally to what others say
- Contribute your thoughts on the topic
- Respond ONLY with your dialogue — no actions, no stage directions, no name prefix
```
No personality information whatsoever. Tests default LLM behavior.

**Baseline B (Random-Persona):**
Uses the same prompt template as Section 3.2.1, but with **shuffled OCEAN values**. For example, if the label says "Assertive Leader" but the OCEAN values are randomly permuted from another profile, this tests whether the *specific values* matter or whether *any* personality description produces generic behavior.

Implementation:
```python
def create_random_persona_prompt(scenario_brief: str) -> str:
    """Create a baseline B prompt with shuffled OCEAN values."""
    # Pick a random profile's values
    source_profile = random.choice(list(EXPERIMENT_PROFILES.values()))
    values = [source_profile.vector.O, source_profile.vector.C,
              source_profile.vector.E, source_profile.vector.A,
              source_profile.vector.N]
    random.shuffle(values)
    shuffled_vector = PersonalityVector(O=values[0], C=values[1], E=values[2],
                                        A=values[3], N=values[4])
    return build_system_prompt(shuffled_vector, scenario_brief)
```

---

## 7. Timeline (Suggested)

| Week | Activity | Deliverable |
|------|----------|-------------|
| 1 | Finalize 12 persona prompts; expand from current 3 test personas | `test_personas.py` updated with 12 profiles |
| 2 | Run pilot: 2 profiles × 2 scenarios × 1 rep = 4 sessions | Verify pipeline works end-to-end; calibrate evaluation |
| 3-4 | Run main experiment: 144 sessions | Raw transcripts + evaluation results |
| 5 | Run baselines: 20 sessions | Baseline transcripts + evaluation results |
| 5 | Run temporal analysis: re-evaluate main sessions by window | Window-level trait scores |
| 6 | Statistical analysis: RQ1, RQ2, RQ3 | Results tables, correlation matrices, ICC values |
| 7 | Write report + prepare presentation | Draft paper + slides |
| 8 | Revise and finalize | Final submission |

---

## Appendix A: References

### Core LLM Persona / Digital Twin Studies
- Paglieri, D. et al. (2026). Persona Generators: Generating Diverse Synthetic Personas at Scale. arXiv:2602.03545.
- Li, R. et al. (2025). [How Far are LLMs from Being Our Digital Twins? A Benchmark for Persona-Based Behavior Chain Simulation](https://aclanthology.org/2025.findings-acl.813/). ACL Findings 2025.
- TwinVoice (2025). [A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation](https://arxiv.org/abs/2510.25536). arXiv:2510.25536.
- Social Digital Twins (2026). [LLM-Powered Social Digital Twins: A Framework for Simulating Population Behavioral Response to Policy Interventions](https://arxiv.org/html/2601.06111v1). arXiv:2601.06111.
- Park, J.S. et al. (2024). [Generative Agent Simulations of 1,000 People](https://arxiv.org/abs/2411.10109). arXiv:2411.10109.
- Santurkar, S. et al. (2023). Whose Opinions Do Language Models Reflect? ICML 2023.

### Psychometric Instruments & Personality Psychology
- John, O.P. & Srivastava, S. (1999). The Big Five Trait Taxonomy: History, Measurement, and Theoretical Perspectives. In *Handbook of Personality: Theory and Research* (2nd ed., pp. 102–138). Guilford Press.
- Gosling, S.D., Rentfrow, P.J., & Swann, W.B. (2003). A very brief measure of the Big-Five personality domains. *Journal of Research in Personality*, 37(6), 504–528.
- Soto, C.J. & John, O.P. (2017). The next Big Five Inventory (BFI-2): Developing and assessing a hierarchical model with 15 facets. *Journal of Personality and Social Psychology*, 113(1), 117–143.
- Gnambs, T. (2014). [A meta-analysis of dependability coefficients (test-retest reliabilities) for measures of the Big Five](https://www.researchgate.net/publication/262938625). *Journal of Research in Personality*, 52, 20–28.

### Personality–Language / Behavior Prompt Justification
- Mairesse, F. & Walker, M.A. (2007). [PERSONAGE: Personality Generation for Dialogue](https://aclanthology.org/P07-1063/). *Proceedings of ACL 2007*. — Empirically validated mappings between Big Five traits and 67 linguistic generation parameters.
- Mairesse, F., Walker, M.A., Mehl, M.R., & Moore, R.K. (2007). Using Linguistic Cues for the Automatic Recognition of Personality in Conversation and Text. *Journal of Artificial Intelligence Research*, 30, 457–500.
- Jiang, H. et al. (2024). [PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits](https://aclanthology.org/2024.findings-naacl.229/). *Findings of NAACL 2024*. — Simple trait label prompts achieve 80% human perception accuracy with large effect sizes.
- Pennebaker, J.W. & King, L.A. (1999). Linguistic Styles: Language Use as an Individual Difference. *Journal of Personality and Social Psychology*, 77(6), 1296–1312.
- Mehl, M.R., Gosling, S.D., & Pennebaker, J.W. (2006). Personality in its Natural Habitat: Manifestations and Implicit Folk Theories of Personality in Daily Life. *Journal of Personality and Social Psychology*, 90(5), 862–877.
- Scherer, K.R. (1979). Personality Markers in Speech. In K.R. Scherer & H. Giles (Eds.), *Social Markers in Speech*. Cambridge University Press.
- Leibo, J.Z. et al. (2024). [Concordia: A Library for Building Multi-Agent Simulations](https://arxiv.org/abs/2312.03664). — Logic of Appropriateness framework for agent behavior.

### Statistical Methods & Effect Size Conventions
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates.
- Koo, T.K. & Li, M.Y. (2016). [A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC4913118/). *Journal of Chiropractic Medicine*, 15(2), 155–163.
- Cicchetti, D.V. (1994). Guidelines, criteria, and rules of thumb for evaluating normed and standardized assessment instruments in psychology. *Psychological Assessment*, 6(4), 284–290.
- Fisher, R.A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd.

## Appendix B: Current System Status

| Component | Status | Location | Notes |
|-----------|--------|----------|-------|
| Group discussion engine | ✅ Implemented | `engines/group_engine.py` | Ready to use |
| AI agents (Alex, Jordan, Riley) | ✅ Implemented | `agents/group_agents.py` | Fixed prompts, no changes needed |
| Moderator (adaptive dispatch) | ✅ Implemented | `agents/moderator.py` | Ready to use |
| Trait evaluator (ensemble) | ✅ Implemented | `evaluation/trait_evaluator.py` | Need to swap DeepSeek → Claude Haiku in ensemble |
| Behavioral statistics | ✅ Implemented | `utils/models.py` (GroupSessionStats) | Need per-window stats function |
| 4 scenarios | ✅ Implemented | `config/group_scenarios.py` | Ready to use |
| 3 test personas | ✅ Implemented | `pressure_cooker/config/test_personas.py` | Reference only — experiment uses new profiles |
| **Behavior prompt mapping** | ✅ **Designed** | Section 3.2.1 of this document | Empirically justified; ready to implement |
| **12 experiment profiles** | ✅ **Designed** | Section 3.2 + 3.2.1 | OCEAN values + behavioral instructions specified; code in `experiment/candidate_agent.py` |
| **Candidate agent automation** | ✅ **Specified** | Section 6A.1 | Replace human input with LLM agent; spec ready |
| **Batch runner** | ✅ **Specified** | Section 6A.2 | 164 sessions, ~12K API calls, ~$10-17, ~6-10 hrs |
| **Temporal window split** | ✅ **Specified** | Section 6A.3 | Phase-based split, 3 windows per session |
| **Statistical analysis** | ✅ **Specified** | Section 6A.4 | pandas + scipy + pingouin; all metrics coded |
| **Cross-model circularity** | ✅ **Resolved** | Section 6A.5 | DeepSeek removed from eval; replaced with Claude Haiku |
| **Baseline prompts** | ✅ **Specified** | Section 6A.6 | No-persona + random-persona templates |

### Implementation Priority Order

| Step | Task | Dependency | Estimated Time |
|------|------|------------|---------------|
| 1 | Create `experiment/candidate_agent.py` with 12 profiles + prompt builder | None | 2-3 hours |
| 2 | Create `experiment/batch_runner.py` | Step 1 | 3-4 hours |
| 3 | Update `clients/llm_client.py` ensemble models (swap DeepSeek → Claude Haiku) | None | 10 minutes |
| 4 | Pilot test: 4 sessions (2 profiles × 2 scenarios) | Steps 1-3 | 1-2 hours |
| 5 | Run full experiment: 164 sessions | Step 4 validation | 6-10 hours (overnight) |
| 6 | Create `experiment/temporal_analysis.py` | Step 5 data | 2-3 hours |
| 7 | Run temporal analysis on 144 main sessions | Steps 5-6 | 4-6 hours |
| 8 | Create `experiment/analysis.py` and run all metrics | Steps 5, 7 | 3-4 hours |
| 9 | Generate report | Step 8 | 1 hour |
