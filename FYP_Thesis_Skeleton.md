# Persona Fidelity in LLM-Based Multi-Stakeholder Policy Deliberation: A Simulation Engine Approach

---

## Abstract

Large Language Models (LLMs) have enabled a new paradigm of multi-agent simulation in which synthetic stakeholders engage in naturalistic policy deliberation. However, three fundamental problems undermine the validity of such simulations: persona drift, whereby agents gradually deviate from their assigned personality profiles over extended dialogue; sycophancy convergence, driven by Reinforcement Learning from Human Feedback (RLHF) training that biases agents toward agreement; and an RLHF-imposed behavioral ceiling that structurally suppresses certain personality traits. This study presents a simulation engine comprising six integrated components — a Persona State Controller, a 4-Slot Candidate Pool, Sycophancy Detection, a Commitment Lifecycle tracker, an Action Layer with 12 structured action types, and Strategic Disposition calibration — designed to maintain individual behavioral fidelity in multi-stakeholder policy deliberation. A large-scale benchmark of 4,080 simulation runs across 20 real-world policy and corporate scenarios demonstrates that the engine reduces persona drift by 5.7% (Cohen's d = −0.94, large effect), envelope violations by 9.9%, and sycophantic acknowledgment by 69%, while increasing idea generation by 267% and disagreement by 37% relative to a naive baseline. The engine achieves universal advantage across all 20 scenarios. However, the study also reveals that RLHF imposes a fundamental ceiling on traits such as Neuroticism and low Agreeableness, where LLMs refuse to generate anxiety or self-doubt expressions regardless of engine intervention. A follow-up 240-run iterative refinement validates that benchmark-driven hyperparameter calibration yields further improvements, establishing a reproducible refinement cycle. These findings establish persona fidelity as a prerequisite for meaningful multi-stakeholder deliberation simulation and delineate the boundaries of what current LLM-based approaches can achieve.

**Keywords**: LLM simulation, persona fidelity, multi-agent deliberation, OCEAN personality model, sycophancy, RLHF

---

## Chapter 1: Introduction

### 1.1 Background

Policy decisions affecting millions of citizens are routinely made with limited understanding of how diverse stakeholders will respond. Environmental impact assessments in the United States require a median of 2.2 years to complete (Council on Environmental Quality, 2024), while professional stakeholder war-gaming exercises conducted by firms such as McKinsey command fees exceeding $500,000 per engagement. These constraints — temporal, financial, and logistical — severely limit the ability of policymakers to anticipate opposition, identify coalition opportunities, and stress-test policy proposals before implementation.

The advent of Large Language Models (LLMs) has opened a fundamentally new approach to this problem. Rather than assembling physical participants or relying on rule-based simulations, LLMs can serve as synthetic stakeholder agents capable of naturalistic dialogue, nuanced argumentation, and context-sensitive negotiation. Recent demonstrations have shown that LLM-based agents can replicate individual human responses with up to 85% accuracy on attitudinal surveys (Park et al., 2024) [REF: Generative Agent Simulations of 1,000 People.pdf] and that AI-generated consensus statements are preferred over human-mediated ones by 56% of participants (Bakker, Tessler et al., 2024). The commercial viability of this approach is evidenced by substantial venture funding: Simile, a Stanford spin-off, raised $100 million in Series A funding for LLM-based persona simulation, while Aaru achieved a valuation approaching $1 billion for synthetic population prediction. Gartner has classified "Decision Intelligence" as a transformational technology in its 2025 AI Hype Cycle.

Despite this momentum, no production-grade tool exists for simulating how a specific group of 5–10 stakeholders would deliberate around a policy table — what arguments they would advance, where they would resist, and how compromise might emerge. This gap is not due to insufficient market demand but rather to unresolved technical challenges that render current LLM-based simulations unreliable for substantive policy analysis.

### 1.2 Problem Statement

This study identifies three interconnected problems that prevent LLM-based multi-agent simulation from producing meaningful policy deliberation.

**Problem 1: Persona Drift.** When an LLM is assigned a specific personality profile — for example, a fiscally conservative regulator with high Conscientiousness and low Openness — it tends to deviate from that profile as dialogue progresses. Over multiple turns of interaction, the agent's behavioral characteristics converge toward a generic, agreeable mean, eroding the distinctive perspectives that make stakeholder simulation informative. Without mechanisms to monitor and correct this drift, the diversity of viewpoints that motivates multi-stakeholder simulation is lost within the first few turns of dialogue.

**Problem 2: Sycophancy Convergence.** LLMs trained through RLHF are optimized to produce responses that human evaluators rate favorably, which creates an inherent bias toward agreement and validation (Wei et al., 2024) [REF: SIMPLE SYNTHETIC DATA REDUCES SYCOPHANCY IN LLM.pdf]. In a multi-agent deliberation context, this manifests as rapid consensus formation: agents default to acknowledging each other's points, expressing agreement, and converging on shared positions regardless of their assigned stakeholder roles. Jain et al. (2026) demonstrate that interaction context further amplifies sycophantic tendencies in LLMs [REF: Interaction Context Often Increases Sycophancy in LLMs.pdf]. An unconstrained simulation of a labor policy debate, for instance, may reach unanimous agreement within three turns — an outcome that is neither realistic nor informative.

**Problem 3: RLHF Behavioral Ceiling.** RLHF safety training structurally suppresses certain personality characteristics. Specifically, traits associated with emotional volatility (high Neuroticism) and confrontational behavior (low Agreeableness) are difficult or impossible for LLMs to express, as the safety alignment process penalizes outputs containing anxiety, self-doubt, or aggressive disagreement. This creates a fundamental ceiling on the range of stakeholder personas that can be faithfully simulated, regardless of the sophistication of the surrounding engine architecture.

These three problems are not merely technical inconveniences; they represent structural barriers that, if left unaddressed, confine LLM-based multi-agent simulation to the status of a toy demonstration rather than a reliable analytical tool.

### 1.3 Application Context

This simulation engine is positioned as a multi-stakeholder policy deliberation simulator — a tool that enables policymakers to preview how diverse stakeholders might react to, argue against, and negotiate around proposed policies before committing to implementation.

The value proposition of this application is qualitatively distinct from quantitative policy modeling. Tools such as EUROMOD (European Commission Joint Research Centre) project fiscal impacts through microsimulation of tax-benefit systems, while platforms such as Polis (employed in Taiwan's vTaiwan initiative) aggregate real citizen opinions through asynchronous polling. The present engine occupies a different niche: it simulates the conversational dynamics of a small group of identified stakeholders — their argumentative strategies, emotional responses, and coalition behaviors — in a controlled deliberation setting.

This positioning aligns naturally with the engine's demonstrated capabilities. The 20 benchmark scenarios are drawn from real-world policy and corporate contexts (EU GDPR enforcement, NYC Congestion Pricing, Boeing 737 MAX crisis response, among others), and the OCEAN personality model maps naturally to stakeholder communication styles: a high-Extraversion union leader advocates differently from a low-Extraversion compliance officer, even when both oppose the same policy.

### 1.4 Contributions

This study makes the following contributions:

1. **Simulation engine architecture.** A six-component engine integrating a Persona State Controller (30 behavioral features, OCEAN trait estimation), a 4-Slot Candidate Pool (integrator, planner, challenger, skeptic), Sycophancy Detection, a Commitment Lifecycle tracker, an Action Layer (12 structured action types with world-state deltas), and Strategic Disposition calibration for multi-stakeholder policy deliberation.

2. **Large-scale empirical validation.** A benchmark of 4,080 simulation runs across 20 real-world policy and corporate scenarios, three actor scales (3, 5, 10 agents), and two experimental conditions (engine-controlled vs. naive baseline), yielding statistically significant improvements in persona drift (−5.7%, Cohen's d = −0.94), envelope violations (−9.9%), and sycophancy reduction (−69%).

3. **Discovery of the RLHF behavioral ceiling.** Quantitative evidence that RLHF safety training imposes a fundamental limit on persona simulation fidelity, particularly for Neuroticism (self-doubt expression = 0.000 across both conditions) and low Agreeableness, establishing a boundary that cannot be overcome through engine-level intervention alone.

4. **Iterative refinement methodology.** A follow-up 240-run iterative refinement demonstrating that benchmark-driven hyperparameter calibration (relationship delta clamping, fuzzy action validation) yields further improvements, establishing a reproducible refinement cycle for simulation engine development.

### 1.5 Report Structure

The remainder of this report is organized as follows. Chapter 2 reviews related work in LLM-based persona simulation, multi-agent systems, the OCEAN personality model in NLP, behavioral fidelity evaluation, and existing policy simulation tools. Chapter 3 presents the system design of the simulation engine, detailing each of the six components with pseudocode for all deterministic logic. Chapter 4 describes the experimental setup, including scenarios, conditions, metrics, and statistical methods. Chapter 5 reports the results of the 4,080-run benchmark. Chapter 6 discusses the implications of these findings, the fidelity-authenticity tension, the RLHF ceiling, iterative refinement results, limitations, and future work. Chapter 7 concludes.

---

## Chapter 2: Related Work

### 2.1 LLM-Based Role-Playing and Persona Simulation

The use of LLMs as role-playing agents has progressed rapidly from single-turn character impersonation to sustained multi-turn persona maintenance. Park et al. (2023) introduced Generative Agents, demonstrating that 25 LLM-powered agents inhabiting a virtual town could exhibit emergent social behaviors such as party planning and relationship formation [REF: Generative Agent Simulations of 1,000 People.pdf]. This foundational work established the feasibility of LLM-based social simulation but focused on behavioral plausibility rather than quantitative fidelity to assigned personality profiles.

Subsequent work has addressed the challenge of personality consistency more directly. Abdulhai et al. (2025) proposed using multi-turn reinforcement learning to maintain consistent persona behavior across extended conversations, demonstrating that RL-based fine-tuning can reduce persona drift relative to prompting-based approaches [REF: Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning.pdf]. Liu et al. (2022) explored persona extending techniques that enrich a character's personality description with inferred attributes to improve consistency in dialogue systems [REF: Improving Personality Consistency in Conversation by Persona Extending.pdf].

The digital twin paradigm has emerged as a parallel line of research. Du et al. (2025) proposed TwinVoice, a multi-dimensional benchmark for evaluating how well LLM personas replicate human behavior across personality, values, and decision-making dimensions [REF: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona.pdf]. Li et al. (2025) examined how far LLMs are from serving as digital twins by benchmarking persona-based behavior chain simulation [REF: How Far are LLMs from Being Our Digital Twins?.pdf]. Paglieri et al. (2026) from Google DeepMind introduced Persona Generators, a framework for creating diverse synthetic personas at scale [REF: google-deepmind-Persona Generators.pdf].

However, these works predominantly address single-agent persona fidelity — the question of whether one LLM agent can consistently impersonate one person. The qualitatively different challenge of maintaining persona fidelity when multiple agents interact, exert social pressure on each other, and must sustain distinctive viewpoints against sycophantic convergence forces remains largely unexplored.

### 2.2 Multi-Agent Systems for Deliberation

Multi-agent LLM systems have been deployed for a range of collaborative and adversarial tasks. Frameworks such as AutoGen (Microsoft), CrewAI, and LangGraph provide infrastructure for orchestrating multi-agent workflows, but these are general-purpose tools without specific mechanisms for maintaining behavioral fidelity in deliberative settings.

In the policy domain, AgentSociety (Tsinghua University, 2025) demonstrated a simulation of 10,000 LLM-powered agents interacting over 5 million exchanges to model policy effects at population scale. While impressive in scale, this work does not evaluate individual agent behavioral fidelity — whether each agent's personality and argumentative style remain consistent with their assigned profile across interactions.

The Habermas Machine (Bakker, Tessler et al., 2024; published in *Science*) represents a significant advance in AI-mediated deliberation, demonstrating that an AI system can generate consensus statements preferred by human participants over those produced by human mediators. However, this system facilitates deliberation among real human participants rather than simulating synthetic stakeholders, placing it in a fundamentally different problem space.

Shapira et al. (2026) introduced "Agents of Chaos," examining the dynamics and emergent behaviors in multi-agent LLM interactions [REF: Agents of Chaos.pdf]. Hu et al. (2025) presented DialogLab, a system for authoring, simulating, and testing dynamic human-AI group conversations, providing tools for designing multi-party dialogue scenarios [REF: google dialoglab.pdf].

Laban et al. (2025) demonstrated that LLMs systematically degrade in performance during multi-turn conversations, a finding directly relevant to the persona drift problem addressed in this study [REF: LLMS GET LOST IN MULTI-TURN CONVERSATION.pdf].

In the policy simulation evaluation space, PolicySimEval (February 2025) represents the first benchmark specifically designed for evaluating agent-based policy simulations, comprising 20 comprehensive scenarios with 65 targeted sub-tasks and 200 auto-generated tasks. The best-performing systems achieve only 24.5% accuracy, demonstrating the substantial difficulty of the policy simulation task and the massive room for improvement in current approaches.

The MAPS framework (Multi-agent AI-augmented Participatory System, 2025) uses DeepSeek V3 for multi-round stakeholder deliberation, representing the closest existing work to the present study. However, MAPS does not include systematic behavioral fidelity evaluation — it focuses on participatory process outcomes rather than individual agent persona consistency.

The *Journal of Deliberative Democracy* published "The Case for Using Generative AI to Run Deliberation Simulations" (2024–2025), arguing that practitioners should use GAI to run hypothetical deliberations for two key use cases: training facilitators and time-sensitive policy consultation. This provides theoretical grounding for the application context of the present study.

The gap in the literature is clear: while multi-agent deliberation systems exist at both population scale (AgentSociety) and human-mediated scale (Habermas Machine), and a benchmark has been established (PolicySimEval), no existing work addresses the specific problem of maintaining individual behavioral fidelity in a small-group multi-stakeholder deliberation among synthetic agents.

### 2.3 OCEAN Personality Model in NLP

The Big Five (OCEAN) personality model — comprising Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism — has been the dominant framework in personality psychology since Costa and McCrae's (1992) formalization, with the Big Five Inventory (BFI) serving as the standard measurement instrument (John & Srivastava, 1999) [REF: BigFiveInventory.pdf].

The application of OCEAN to LLM behavior has generated substantial research interest. Lee et al. (2025) developed TRAIT, a personality test set designed specifically for LLMs with psychometric rigor, finding that LLMs do exhibit distinct and partially consistent personality profiles [REF: Do LLMs Have Distinct and Consistent Personality?.pdf]. Hilliard et al. (2024) investigated methods for eliciting personality traits in LLMs, examining how prompting strategies affect the manifestation of Big Five characteristics [REF: Eliciting Personality Traits in Large Language Models.pdf].

Wang et al. (2025) proposed a Personality Structured Interview framework for LLM simulation in personality research, providing a systematic methodology for assessing LLM personality expression [REF: Personality Structured Interview for Large Language Model Simulation in Personality Research.pdf]. Wuttke et al. (2025) demonstrated that LLMs can serve as adaptive interviewers, transforming survey methodology through conversational AI [REF: AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers.pdf].

Recent work has begun connecting Big Five traits to LLM agent behavior in interactive settings. "Exploring Big Five Personality and AI Capability Effects in LLM-Simulated Negotiation Dialogues" (2025), using the Sotopia testbed, found that Agreeableness and Extraversion significantly affect believability, goal achievement, and knowledge acquisition in negotiations — a finding consistent with the present study's per-trait results. "The Impact of Big Five Personality Traits on AI Agent Decision-Making in Public Spaces" (March 2025) demonstrated that LLMs can simulate Big Five traits that influence collective decision-making, while "Dynamic Personality in LLM Agents" (ACL Findings 2025) proposed a framework for personality trait evolution in multi-agent simulations.

Despite these advances, the application of OCEAN to multi-stakeholder policy deliberation — where personality traits map to communication styles rather than self-reported attitudes — remains unexplored. The present study's contribution is to operationalize OCEAN as a behavioral fidelity framework for deliberation simulation, using 30 linguistic features to continuously estimate trait expression and detect drift from assigned profiles.

### 2.4 Behavioral Fidelity Evaluation

The evaluation of behavioral fidelity in LLM-based simulation has emerged as a critical but underdeveloped research area. Gupta and Sheikh (2026) demonstrated that LLM-powered social digital twins can simulate population behavioral responses to policy interventions with 20.7% improvement over gradient boosting baselines, but their evaluation operates at the population level rather than the individual persona level [REF: LLM-Powered Social Digital Twins.pdf].

The challenge of evaluation methodology itself has received attention. Stureborg et al. (2024) demonstrated that LLMs are inconsistent and biased when used as evaluators [REF: Large Language Models are Inconsistent and Biased Evaluators.pdf], while Verga et al. (2024) proposed replacing single-model judges with jury panels of diverse models to improve evaluation reliability [REF: Replacing Judges with Juries.pdf]. These findings informed the present study's decision to use deterministic, rule-based behavioral feature extraction rather than LLM-based evaluation for measuring persona fidelity.

Li et al. (2025) proposed behavioral chain simulation as a benchmark for digital twins, providing a framework for evaluating sequential decision-making fidelity. Li et al. (consumer behavior context) examined how LLM-powered digital twins predict consumer behaviors [REF: Predicting Behaviors with Large Language Model (LLM)-Powered Digital Twins of Consumers.pdf].

PolicySimEval (February 2025) represents the first benchmark specifically designed for evaluating agent-based policy simulations, comprising 20 comprehensive scenarios with 65 targeted sub-tasks. The best-performing systems achieve only 24.5% accuracy on this benchmark, highlighting the substantial difficulty of the policy simulation evaluation task and the nascent state of the field.

The gap in existing evaluation approaches is their focus on aggregate prediction accuracy — whether a simulated population votes correctly or a simulated consumer makes the expected purchase. No existing work measures turn-by-turn behavioral fidelity at the individual agent level during multi-party interaction. This study addresses this gap through a 30-feature behavioral extraction pipeline that estimates OCEAN trait expression at each dialogue turn and quantifies drift from assigned personality priors.

### 2.5 Existing Policy Simulation Tools

The landscape of policy simulation tools can be categorized into four tiers by their proximity to the multi-stakeholder deliberation problem addressed in this study.

**Quantitative policy models** such as EUROMOD (EU Joint Research Centre) and the tools maintained by the U.S. Congressional Budget Office provide microsimulation of tax-benefit systems and macroeconomic projections. These tools are indispensable for fiscal analysis but do not model stakeholder behavior or communication dynamics.

**Agent-based modeling (ABM) platforms** such as AnyLogic ($12,000–$19,000/year license) and NetLogo (open-source) enable simulation of large agent populations with rule-based behaviors. Traditional ABM agents follow programmed rules and lack the linguistic richness and emergent reasoning capabilities of LLM-based agents. AgentTorch (MIT) bridges this gap partially by integrating LLMs into an ABM framework for large-scale social simulation.

**Commercial AI simulation platforms** represent the nearest competitive landscape. Simile (Stanford spin-off, $100M Series A) offers LLM-based persona replication for applications including earnings call rehearsal and litigation preparation. Aaru (~$1B valuation) specializes in synthetic population prediction, achieving notable accuracy in election forecasting. Artificial Societies (YC W25, €4.5M) provides 300–5,000 AI personas for marketing and communication testing at $40/month. However, none of these platforms specifically targets small-group policy deliberation with behavioral fidelity guarantees. The nearest government-sector product is Fujitsu's Policy Twin (launched December 2024), which creates digital twins of societal movements for local government policy simulation in Japan; in field trials, it identified policies that doubled both cost savings and health improvements. However, it remains Japan-only and in early deployment stages.

**Citizen participation and democratic innovation platforms** represent an important adjacent category. Polis, an open-source platform using machine learning to surface areas of agreement, has been deployed in Taiwan's vTaiwan initiative (where 80% of issues led to government action), Finland, Spain, New Zealand, and Germany. Audrey Tang, Taiwan's former Digital Minister, has pioneered the integration of AI tools into deliberative processes, with vTaiwan now experimenting with generative AI for transcript recording, opinion clustering, and analysis. Stanford HAI's Deliberation.io became the first AI-powered deliberation platform deployed by a U.S. city when Washington, D.C. used it for an AI Public Listening Session in September 2025. DemocracyNext and MIT's Center for Constructive Communication launched a two-year lab in 2025 to integrate AI into all three phases of citizens' assemblies. The UK's AI Consult tool automated analysis of public consultation responses, achieving a median review time of 23 seconds per response and saving over £250,000 across seven live consultations. These platforms facilitate real human deliberation rather than synthetic simulation — they address a fundamentally different problem: aggregating existing human opinions rather than generating synthetic stakeholder responses. The present study's engine could complement these platforms by pre-testing policy proposals through synthetic deliberation before launching public consultations.

The market gap is thus precisely defined: no existing tool simulates how 5–10 specific stakeholders would negotiate around a policy table, maintaining their distinctive argumentative styles while responding authentically to each other's positions. This study's simulation engine occupies this gap as a stakeholder agent engine — a core component that could eventually integrate with quantitative models, RAG-based knowledge enrichment, and scenario branching to form a complete strategic simulation platform.

---

## Chapter 3: System Design

This chapter presents the architecture of the simulation engine, organized around the principle that each component addresses a specific, identified problem. All deterministic logic — scoring functions, feature extraction, state management — is presented in pseudocode following the principle that non-LLM-wrapper logic must be fully transparent and reproducible.

### 3.1 Architecture Overview

The simulation engine processes a structured JSON simulation script through a phase-based dialogue loop. Each simulation script defines the scenario context, stakeholder roster (with OCEAN personality priors, incentives, and concerns), phase structure (OPENING, TENSION, NEGOTIATION, CLOSING), and world events.

**Figure 1: System Architecture Pipeline** *(to be created)*

```
Simulation Script (JSON)
    ↓
Phase Loop (4 phases: OPENING → TENSION → NEGOTIATION → CLOSING)
    ↓
  Actor Turn Loop
    ├── 1. Policy Plan Generation (LLM)
    ├── 2. 4-Slot Candidate Generation (4 × LLM calls)
    ├── 3. Behavioral Feature Extraction (30 features, deterministic)
    ├── 4. OCEAN Trait Estimation (deterministic)
    ├── 5. Candidate Scoring (persona + sycophancy + social, deterministic)
    ├── 6. Best Candidate Selection (deterministic)
    ├── 7. Action Extraction (hybrid: keyword + LLM fallback)
    ├── 8. World State Update (deterministic deltas)
    ├── 9. Commitment Tracking (state ledger)
    └── 10. Relationship Update (sentiment detection)
```

The engine operates in two modes: **guided** (outcome-anchored, where phase outcomes are specified in the script) and **exploratory** (open-ended, where outcomes emerge from agent interaction). Both modes share the same persona fidelity infrastructure.

**Technology stack:** Python, LangGraph (state machine orchestration), DeepSeek V3 (text generation), sentence-transformers (semantic embeddings for convergence measurement).

### 3.2 Persona State Controller

**Problem:** LLMs exhibit persona drift in extended multi-turn conversations, gradually deviating from assigned personality profiles.

**Design Decision:** Rather than relying on LLM self-correction (which is unreliable) or post-hoc filtering (which wastes generation), the controller monitors behavioral fidelity at every turn and selects the most persona-consistent candidate from a pool of alternatives.

**Implementation:** At each turn, the controller extracts 30 behavioral features from the candidate's text, estimates the candidate's current OCEAN trait expression, compares it against the assigned personality prior, and applies a penalty proportional to the deviation.

```pseudocode
FUNCTION score_candidate(candidate_text, actor_prior, phase, conversation_history):
    features ← extract_30_features(candidate_text)
    inferred_ocean ← estimate_ocean(features, conversation_history)

    // Persona consistency: inverse of drift from assigned prior
    drift ← mean(|inferred_ocean[t] - actor_prior[t]| for t in {O,C,E,A,N})
    persona_score ← 1.0 - drift

    // Sycophancy risk: penalize agreement-biased candidates
    syc_risk ← detect_sycophancy(features, actor_prior, phase)

    // Social trait alignment: E, A, N tolerance bands
    social_score ← compute_social_alignment(inferred_ocean, actor_prior)

    // Envelope penalty: quadratic penalty for traits outside ±threshold
    envelope_penalty ← sum(overshoot² for traits exceeding bounds)

    // Phase-weighted combination
    weights ← PHASE_WEIGHT_MODIFIERS[phase]
    total ← weights.persona × persona_score
           + weights.sycophancy × (1 - syc_risk)
           + weights.social × social_score
           - weights.envelope × envelope_penalty
           - redundancy_penalty(candidate_text, conversation_history)
           - genericity_penalty(candidate_text)

    RETURN total
```

**Phase Weight Modifiers:**

| Phase | Persona Weight | Sycophancy Weight | Social Weight | Envelope Weight |
|-------|---------------|-------------------|---------------|-----------------|
| OPENING | 1.2× | 0.8× | 1.0× | 1.0× |
| TENSION | 1.0× | 1.8× | 1.4× | 1.0× |
| NEGOTIATION | 1.0× | 1.0× | 1.0× | 1.3× |
| CLOSING | 1.3× | 1.0× | 1.0× | 1.4× |

The rationale for phase-specific weighting: during TENSION, sycophancy risk is highest (agents tend to smooth over conflict); during CLOSING, envelope violations are most likely (agents converge toward a generic "summarize and agree" pattern).

### 3.3 Behavioral Feature Extraction and OCEAN Estimation

**30 Behavioral Features:**

The controller extracts 30 linguistic features from each candidate text, organized by their primary OCEAN trait association. Table 7 presents a representative subset (one per trait plus sycophancy indicators); the complete 30-feature specification is provided in Appendix B.

**Table 7: Representative Behavioral Features (subset of 30)**

| Feature | Primary Trait | Extraction Method | Why This Feature |
|---------|---------------|-------------------|------------------|
| idea_count | **Openness** | Novel proposals introduced | High-O individuals generate more creative alternatives |
| planning_count | **Conscientiousness** | "plan", "schedule", "timeline" | High-C individuals impose structure on deliberation |
| avg_words_per_turn | **Extraversion** | Word count / turn count | High-E individuals speak more and at greater length |
| disagreement_count | **Low Agreeableness** | "disagree", "however", "but" | Low-A individuals challenge others more frequently |
| hedge_count | **Neuroticism** | "maybe", "perhaps", "might" | High-N individuals express more uncertainty |
| acknowledgment_count | **Sycophancy indicator** | "great point", "agree", "makes sense" | Detects RLHF-driven agreement bias |

**OCEAN Estimation with Dynamic Calibration:**

A critical design decision is the use of dynamic calibration against the conversation baseline when multiple speakers are present. This addresses the observation that absolute feature counts are uninformative without context — a planning_count of 3 may indicate high Conscientiousness in a casual discussion but low Conscientiousness in a project management meeting.

```pseudocode
FUNCTION estimate_ocean(features, conversation_history):
    IF multiple_speakers_present(conversation_history):
        baseline ← compute_conversation_baseline(conversation_history)

        O ← clip(0.50 + 0.55 × (raw_O(features) - baseline.O), 0, 1)
        C ← clip(0.50 + 0.55 × (raw_C(features) - baseline.C), 0, 1)
        E ← clip(0.50 + 0.65 × (raw_E(features) - baseline.E), 0, 1)
        A ← clip(0.50 + 0.50 × (raw_A(features) - baseline.A), 0, 1)
        N ← clip(0.50 + 0.50 × (raw_N(features) - baseline.N), 0, 1)
    ELSE:
        // Static formula for single-speaker context
        O ← clip(0.25 + 0.10×min(idea,4) + 0.10×min(hypo,3) + 0.90×min(uwr,0.20), 0, 1)
        C ← clip(0.12 + 0.06×plan + 0.05×struct + 0.06×ref + 0.08×action, 0, 1)
        E ← clip(0.20 + min(words,80)/120 + 0.08×names + 0.12×questions, 0, 1)
        A ← clip(0.45 + 0.10×ack - 0.10×disagree - 0.02×negation, 0, 1)
        N ← clip(0.18 + 0.08×hedge + 0.10×doubt + 0.08×reassurance + 0.06×apology, 0, 1)

    RETURN {O, C, E, A, N}
```

**Rolling Trait Estimation:** The state ledger maintains a rolling estimate of each actor's trait expression using exponential smoothing (α = 0.6 for current turn, 0.4 for history), preventing single-turn anomalies from triggering excessive correction.

### 3.4 4-Slot Candidate Pool

**Problem:** A single LLM generation for each turn produces limited diversity and may yield suboptimal responses that happen to be sycophantic or persona-inconsistent.

**Design Decision:** Generate four candidate responses per turn, each with a distinct rhetorical style, and select the best according to the persona fidelity scoring function.

**Implementation:**

```pseudocode
STYLE_SLOTS = {
    "integrator": {
        tone: "seeks common ground and collaborative solutions",
        action_vocabulary: [assign_owner, commit_resource, publish_update]
    },
    "planner": {
        tone: "proposes structured plans and timelines",
        action_vocabulary: [set_deadline, narrow_scope, pilot]
    },
    "challenger": {
        tone: "questions assumptions and raises counterarguments",
        action_vocabulary: [preserve_autonomy, request_evidence, escalate]
    },
    "skeptic": {
        tone: "expresses doubt and demands justification",
        action_vocabulary: [audit_compliance, defer_decision, request_evidence]
    }
}

FUNCTION generate_and_select(actor, context, phase, prior):
    candidates ← []
    FOR EACH slot IN STYLE_SLOTS:
        prompt ← build_prompt(actor, context, phase, slot.tone)
        candidate ← LLM.generate(prompt)
        score ← score_candidate(candidate, prior, phase, context)
        candidates.append({text: candidate, score: score, slot: slot})

    RETURN candidates.sort_by(score).best()
```

**Cost-Diversity Tradeoff:** Each turn requires 4 LLM generation calls, resulting in approximately 88 API calls per simulation run (11 average turns × 4 slots × 2 actors per turn). A complete simulation takes approximately 3 minutes. This cost is justified by the diversity it provides: without multiple candidates, the controller has no alternatives from which to select persona-consistent responses.

### 3.5 Sycophancy Detection

**Problem:** RLHF-trained LLMs exhibit a systematic bias toward agreement, causing multi-agent simulations to converge rapidly on consensus.

**Design Decision:** A multi-layered detection system that penalizes sycophantic candidates during scoring, with sensitivity calibrated to the scenario's structural polarity and each actor's strategic disposition.

```pseudocode
FUNCTION detect_sycophancy(features, actor_prior, phase):
    // Layer 1: Keyword-based detection
    keyword_risk ← (features.acknowledgment_count × 0.15
                   + features.exclamation_ratio × 0.10)

    // Layer 2: Structural polarity adjustment
    IF scenario.structural_polarity > 0.7:  // High-conflict scenario
        keyword_risk ← keyword_risk × 1.3  // Amplify penalty

    // Layer 3: Strategic disposition adjustment
    IF actor.strategic_disposition IN {adversarial, competitive}:
        keyword_risk ← keyword_risk × 1.5  // Agreement from adversarial actor is more suspicious

    // Layer 4: Low Agreeableness adjustment
    IF actor_prior.A < 0.4:
        keyword_risk ← keyword_risk × 1.2  // Low-A actors should not be agreeable

    RETURN clip(keyword_risk, 0, 1)
```

### 3.6 Commitment Lifecycle

**Problem:** Agents make commitments ("I will prepare the draft by Friday") but fail to follow through or contradict themselves in subsequent turns.

**Design Decision:** Track all commitments in a state ledger with lifecycle management: extraction → monitoring → fulfillment detection → staleness resolution.

A critical design insight emerged from early experiments: instructing agents to "stay consistent" (directive approach) caused diversity to collapse to 0.45 as agents rigidly maintained their initial positions. The successful approach is informational: presenting "Your prior positions: [list]" without any instruction, allowing the LLM to decide how to use that information. This soft prompt injection achieves zero contradictions while maintaining behavioral diversity.

```pseudocode
FUNCTION manage_commitments(actor_id, turn_content, phase, ledger):
    // Step 1: Extract new commitments
    new_commitments ← extract_commitments(turn_content)
    FOR EACH commitment IN new_commitments:
        ledger.add({
            owner: actor_id,
            content: commitment.text,
            created_phase: phase,
            status: "open"
        })

    // Step 2: Check fulfillment of existing commitments
    FOR EACH open_commitment IN ledger.get_open(actor_id):
        IF fulfillment_detected(turn_content, open_commitment):
            open_commitment.status ← "fulfilled"

    // Step 3: Detect stale commitments (phase boundary)
    IF phase_transition_occurred:
        FOR EACH open_commitment IN ledger.get_open(actor_id):
            IF open_commitment.created_phase < current_phase - 1:
                open_commitment.status ← "stale_resolved"

    // Step 4: Inject prior positions into next generation prompt
    prior_positions ← ledger.get_position_summary(actor_id)
    RETURN "Your prior positions:\n" + prior_positions  // Information only, no instruction
```

### 3.7 Action Layer

**Problem:** Dialogue text alone cannot capture the structural actions stakeholders take during deliberation (assigning tasks, requesting evidence, escalating to authority). Without action extraction, the simulation produces conversation but not traceable decision-making.

**Design Decision:** Define 12 structured action types organized in 7 families, with a hybrid extraction pipeline (deterministic keyword matching with LLM fallback) and phase-gated validation.

**12 Action Types:**

| Family | Action Type | Description | World State Delta |
|--------|------------|-------------|-------------------|
| Ownership | assign_owner | Assign task to specific actor | trust +0.04 |
| Evidence | request_evidence | Demand supporting data | uncertainty −0.04 |
| Communication | publish_update | Share information with group | alignment +0.04 |
| Scope | narrow_scope | Reduce scope of proposal | uncertainty −0.04 |
| Scope | pilot | Propose limited trial | risk −0.08 |
| Resourcing | commit_resource | Pledge resources | execution_confidence +0.08 |
| Resourcing | allocate_budget | Assign financial resources | execution_confidence +0.08 |
| Timing | set_deadline | Establish timeline | uncertainty −0.04 |
| Timing | defer_decision | Postpone to later phase | tension −0.04 |
| Governance | preserve_autonomy | Protect decision-making authority | tension +0.08 |
| Governance | escalate | Raise to higher authority | tension +0.12 |
| Governance | audit_compliance | Request formal review | uncertainty −0.08 |

```pseudocode
FUNCTION extract_and_execute_action(turn_text, actor, phase, world_state):
    // Step 1: Detect action-bearing turn (deterministic)
    IF NOT contains_action_cues(turn_text):
        RETURN null

    // Step 2: Extract action type (keyword matching first)
    action_type ← first_matching_action_type(turn_text)
    IF action_type IS null:
        action_type ← LLM_extract_action(turn_text)  // Fallback

    // Step 3: Phase gate (sparse gate)
    IF phase == "OPENING" AND action_type NOT IN {publish_update}:
        RETURN null  // Shadow mode: no actions in OPENING

    // Step 4: Extract metadata
    target_key ← detect_target_state_key(turn_text)
    strength ← detect_strength(turn_text)  // low/medium/high

    // Step 5: Validate and execute
    delta ← DELTA_PALETTE[strength]  // low=0.04, medium=0.08, high=0.12
    world_state[target_key] ← clip(world_state[target_key] ± delta, 0, 1)

    RETURN ActionProposal(action_type, target_key, strength, delta)
```

### 3.8 Strategic Disposition

**Problem:** Without differentiated strategic orientations, all actors default to neutral-cooperative behavior, weakening the conflict dynamics essential to realistic deliberation.

**Design Decision:** Each actor in the simulation script is assigned a `strategic_disposition` (cooperative, neutral, competitive, adversarial) with a `disposition_strength` (0.0–1.0). This disposition operates at three levels: system prompt tone, action type bias, and sycophancy detection threshold.

```pseudocode
DISPOSITION_EFFECTS = {
    "adversarial": {
        system_prompt_modifier: "You strongly challenge assumptions and resist compromise.",
        preferred_actions: [escalate, preserve_autonomy, request_evidence],
        sycophancy_threshold_multiplier: 1.5
    },
    "competitive": {
        system_prompt_modifier: "You advocate firmly for your position.",
        preferred_actions: [preserve_autonomy, narrow_scope],
        sycophancy_threshold_multiplier: 1.3
    },
    "neutral": {
        system_prompt_modifier: "",  // No modification
        preferred_actions: [],  // No bias
        sycophancy_threshold_multiplier: 1.0
    },
    "cooperative": {
        system_prompt_modifier: "You seek collaborative solutions.",
        preferred_actions: [assign_owner, commit_resource, publish_update],
        sycophancy_threshold_multiplier: 0.8
    }
}
```

The default disposition is "neutral," ensuring backward compatibility with existing simulation scripts.

---

## Chapter 4: Experimental Setup

### 4.1 Scenarios

The benchmark comprises 20 real-world policy and corporate scenarios drawn from six domains:

| Domain | Scenarios | Examples |
|--------|-----------|----------|
| Policy / Regulatory | 7 | EU GDPR Enforcement, NYC Congestion Pricing, California AB5 Gig Worker Law, Australia Robodebt |
| Corporate Crisis | 4 | FTX Collapse, Boeing 737 MAX, WeWork IPO Collapse, Theranos |
| Labor / Workplace | 3 | Starbucks Unionization, Amazon Labor Practices, Zoom Return-to-Office |
| Ethics / Technology | 3 | Facial Recognition Ban (San Francisco), Autonomous Vehicle Liability, Social Media Child Safety |
| Financial / Consumer | 2 | Netflix Password Crackdown, Peloton Demand Cliff |
| Public Health / Infrastructure | 2 | Flint Water Crisis, Fukushima Nuclear Restart |

Each scenario is instantiated at three actor scales: 3 actors, 5 actors, and 10 actors, yielding 60 unique simulation scripts. Real-world scenarios were selected to leverage LLM pre-training knowledge, enabling richer and more contextually grounded stakeholder responses. This design choice is acknowledged as a limitation: LLMs may exhibit training data leakage effects when simulating well-documented events.

### 4.2 Experimental Conditions

Two experimental conditions are compared:

**Engine Structural (engine_structural):** The full simulation engine with all six components active — Persona State Controller, 4-Slot Candidate Pool, Sycophancy Detection, Commitment Lifecycle, Action Layer, and Strategic Disposition. The controller performs deterministic candidate scoring and selection at every turn.

**Naive Baseline (naive):** Each actor receives only a persona prompt (OCEAN personality priors, role description, incentives, and concerns) and generates a single response per turn without candidate pooling, scoring, or any engine-level control. This represents the standard approach to LLM-based role-playing.

The choice of a binary comparison (full engine vs. no engine) rather than component-level ablation is motivated by prior iterative experimentation (Experiments 1–6, Arms A/B) that already validated individual component contributions. The present benchmark focuses on the practical question: does the complete engine deliver meaningful improvement over uncontrolled generation?

### 4.3 Scale

| Parameter | Value |
|-----------|-------|
| Simulation scripts | 60 (20 scenarios × 3 actor scales) |
| Conditions | 2 (engine_structural, naive) |
| Repetitions | ~34 per script (variable by configuration) |
| **Total runs** | **4,080** (2,056 engine + 2,024 naive) |
| Average turns per run | 11 |
| LLM calls per run | ~88 (engine) / ~22 (naive) |
| Total LLM calls | ~120,000+ |
| Approximate runtime | ~50 hours |
| Generation model | DeepSeek V3 |

### 4.4 Metrics

**Primary Metrics:**

| Metric | Definition | Measures |
|--------|-----------|----------|
| Persona Drift MAE | mean(\|OCEAN_inferred − OCEAN_prior\|) across all traits and turns | How well agents maintain assigned personality |
| Envelope Violations | Count of traits exceeding ±threshold from prior per run | Frequency of personality boundary breaches |

**Secondary Metrics:**

| Metric | Definition | Measures |
|--------|-----------|----------|
| Commitment Contradiction | Self-contradicting positions within a run | Positional consistency |
| Commitment Fulfillment | Proportion of stated commitments fulfilled | Follow-through reliability |
| Action-Plan Alignment | Actions consistent with stated policy plan | Behavioral coherence |
| Action Validity Rate | Proportion of structurally valid actions | Action extraction quality |
| Convergence | Pairwise semantic similarity across actors | Opinion homogenization |
| Diversity | Unique action types / total actions | Behavioral diversity |
| Acknowledgment Count | Sycophantic agreement expressions per turn | Sycophancy level |
| Disagreement Count | Explicit disagreement expressions per turn | Authentic conflict |
| Idea Count | Novel proposals per turn | Creative contribution |

### 4.5 Statistical Methods

All comparisons employ a **paired design**: the same simulation script is run under both conditions, and differences are computed within each script pair. This design eliminates between-script variability (different scenarios, actor counts, and inherent difficulty levels) and increases statistical power.

**Paired t-test:** Used for primary comparisons of drift MAE and envelope violations. The null hypothesis is that the engine produces no improvement over the naive baseline (H₀: μ_diff = 0).

**Cohen's d (paired):** Effect size calculated as the mean of paired differences divided by the standard deviation of differences. Interpreted as small (d < 0.2), medium (d ≈ 0.5), and large (d > 0.8).

**95% Confidence Intervals:** Computed for all primary metrics to assess the precision of estimated effects.

**Bonferroni Correction:** Applied when conducting multiple comparisons (e.g., 20 scenarios × 5 traits = 100 per-trait per-scenario tests) to control the family-wise error rate at α = 0.05.

---

## Chapter 5: Results

### 5.1 Overall Engine vs. Naive Comparison

**Table 1: Primary Benchmark Results (4,080 runs)**

| Metric | Engine (n=2,056) | Naive (n=2,024) | Δ | Cohen's d | p-value |
|--------|-----------------|-----------------|---|-----------|---------|
| Persona Drift MAE | 0.1678 (±0.017) | 0.1780 (±0.018) | −5.7% | −0.94 | 3.58 × 10⁻⁴⁸ |
| Envelope Violations | 2.057 | 2.283 | −9.9% | −0.603 | < 0.001 |
| Commitment Contradiction | 0.000 | 0.000 | 0.0% | — | — |
| Commitment Fulfillment | 0.781 | 0.675 | +15.7% | — | < 0.001 |
| Action-Plan Alignment | 0.968 | — | — | — | — |
| Action Validity | 0.641 | — | — | — | — |
| Acknowledgment Count | 0.061 | 0.194 | −69% | — | < 0.001 |
| Disagreement Count | 0.083 | 0.061 | +37% | — | < 0.001 |
| Idea Count | 0.370 | 0.101 | +267% | — | < 0.001 |

The engine achieves statistically significant improvements across all primary metrics. The persona drift reduction of 5.7% corresponds to a large effect size (Cohen's d = −0.94), indicating a practically meaningful improvement. The 95% confidence intervals for drift MAE do not overlap: Engine [0.1670, 0.1685] vs. Naive [0.1773, 0.1788], confirming that the improvement is robust.

The engine demonstrates universal advantage: it produces lower persona drift than the naive baseline in all 20 of 20 scenarios.

### 5.2 Per-Trait OCEAN Analysis

**Table 2: Per-Trait Persona Drift Error**

| Trait | Engine Error | Naive Error | Δ | Interpretation |
|-------|-------------|-------------|---|----------------|
| Extraversion (E) | 0.1203 | 0.1438 | −16.3% | Best-controlled trait; verbal features (word count, questions) are most measurable |
| Openness (O) | 0.1650 | 0.1834 | −10.0% | Well-controlled; idea generation and hypotheticals are distinctive markers |
| Agreeableness (A) | 0.1628 | 0.1706 | −4.6% | Moderate control; low-A is difficult due to sycophancy bias |
| Neuroticism (N) | 0.1700 | 0.1681 | +1.1% | **Engine slightly worse**; RLHF suppresses anxiety/doubt expressions |
| Conscientiousness (C) | 0.2207 | 0.2243 | −1.6% | Both conditions struggle; abstract trait with fewer linguistic markers |

**Critical finding:** Neuroticism is the only trait where the engine performs marginally worse than the naive baseline (+0.002 absolute). This is attributed to the RLHF behavioral ceiling: self_doubt_count = 0.000 and reassurance_seeking_count ≈ 0.000 across both conditions. When the engine attempts to steer toward higher Neuroticism expression, it encounters LLM refusal to generate such content, and the additional steering pressure marginally increases measurement noise.

**Figure 2: Per-Trait Error Bar Chart** *(to be created)* — Engine vs. Naive with 95% CI for each OCEAN trait.

### 5.3 Per-Scenario Analysis

**Table 3: Top 5 and Bottom 5 Scenarios by Engine Drift MAE**

| Rank | Scenario | Engine Drift | Naive Drift | Δ |
|------|----------|-------------|-------------|---|
| 1 (Best) | Flint Water Crisis | 0.149 | 0.168 | −11.3% |
| 2 | FTX Collapse | 0.152 | 0.172 | −11.6% |
| 3 | Boeing 737 MAX | 0.155 | 0.171 | −9.4% |
| 4 | EU GDPR Enforcement | 0.158 | 0.174 | −9.2% |
| 5 | Starbucks Unionization | 0.161 | 0.176 | −8.5% |
| 16 | Social Media Child Safety | 0.178 | 0.184 | −3.3% |
| 17 | Autonomous Vehicle Liability | 0.180 | 0.183 | −1.6% |
| 18 | Amazon Labor Practices | 0.181 | 0.185 | −2.2% |
| 19 | Netflix Password Crackdown | 0.184 | 0.188 | −2.1% |
| 20 (Worst) | Zoom Return to Office | 0.187 | 0.190 | −1.6% |

Policy scenarios (average drift 0.163) show stronger engine effects than corporate scenarios (average drift 0.174). Scenarios with clear stakeholder polarization (Flint Water, FTX Collapse) show the largest improvements, suggesting that the engine's sycophancy detection is most valuable when agents face strong pressure to converge.

### 5.4 Actor Scaling Analysis

**Table 4: Performance by Actor Count**

| Actors | Engine Drift | Naive Drift | Diversity | Convergence |
|--------|-------------|-------------|-----------|-------------|
| 3 | 0.1710 | 0.1810 | 0.636 | 0.657 |
| **5** | **0.1646** | **0.1770** | **0.561** | **0.650** |
| 10 | 0.1675 | 0.1760 | 0.339 | 0.816 |

The 5-actor configuration emerges as optimal: it achieves the lowest drift (0.1646) and envelope violations (2.002) while maintaining reasonable diversity (0.561). The 10-actor configuration reveals a structural scaling limitation: convergence increases sharply to 0.816 (+25% vs. 5-actor) while diversity drops to 0.339 (−40% vs. 5-actor). In large groups, the LLM's tendency to synthesize and summarize previous speakers' points overwhelms the engine's ability to maintain distinctive viewpoints.

### 5.5 Phase-Level Analysis

**Table 5: Metrics by Deliberation Phase**

| Phase | Engine Drift | Naive Drift | Convergence | Idea Count |
|-------|-------------|-------------|-------------|------------|
| OPENING | 0.171 | 0.180 | 0.72 | 0.21 |
| TENSION | 0.173 | 0.182 | 0.58 | 0.35 |
| NEGOTIATION | 0.171 | 0.179 | 0.61 | 0.52 |
| **CLOSING** | **0.179** | **0.183** | **0.84** | **0.12** |

CLOSING phase exhibits the worst drift (0.179) and highest convergence (0.84) across both conditions. All actors default to a "summarize and agree" pattern, functioning as a convergence magnet that pulls all agents toward consensus regardless of their assigned dispositions. The NEGOTIATION phase is the most productive, with the highest idea generation (0.52) and lowest convergence (0.61), suggesting that the engine's action layer and commitment tracking are most effective during this phase.

### 5.6 Behavioral Feature Analysis

**Table 6: Most Differentiated Behavioral Features (Engine vs. Naive)**

| Feature | Engine | Naive | Δ | Interpretation |
|---------|--------|-------|---|----------------|
| exclamation_ratio | 0.011 | 0.051 | −78% | Engine suppresses enthusiastic agreement markers |
| acknowledgment_count | 0.061 | 0.194 | −69% | Sycophantic agreement sharply reduced |
| idea_count | 0.370 | 0.101 | +267% | Candidate pool diversity drives novel proposals |
| question_ratio | 0.145 | 0.118 | +23% | Engine candidates ask more probing questions |
| disagreement_count | 0.083 | 0.061 | +37% | Authentic conflict preserved |
| hedge_ratio | 0.072 | 0.085 | −15% | Engine reduces hedging (more decisive positions) |
| self_doubt_count | 0.000 | 0.000 | 0% | RLHF ceiling — neither condition expresses doubt |

The behavioral feature analysis reveals that the engine produces a qualitatively different conversation pattern: fewer sycophantic markers (exclamation, acknowledgment), more substantive contributions (ideas, questions, disagreement), and equivalent absence of Neuroticism markers (self-doubt, reassurance-seeking) — the latter reflecting the RLHF behavioral ceiling.

---

## Chapter 6: Discussion

### 6.1 Interpretation of Key Findings

The primary finding — a 5.7% reduction in persona drift with Cohen's d = −0.94 — requires careful interpretation. The absolute magnitude of improvement is modest, yet the effect size is large. This apparent paradox is explained by the paired experimental design: by comparing the same script under both conditions, between-script variability is eliminated, allowing even small systematic differences to emerge with high statistical power. The practical significance lies not in the absolute drift value but in the consistency of improvement: the engine outperforms the naive baseline in every one of the 20 scenarios, with non-overlapping 95% confidence intervals.

The more transformative finding is the qualitative shift in conversation dynamics. The 69% reduction in sycophantic acknowledgment and 267% increase in idea generation indicate that the engine does not merely preserve assigned personalities but fundamentally changes the informational value of the simulation. A naive simulation produces "I agree" — "Yes, good point" — "Let's all agree" cycles, whereas the engine-controlled simulation generates novel proposals, probing questions, and authentic disagreement. For a policymaker evaluating stakeholder reactions, this qualitative difference determines whether the simulation provides actionable insight or vacuous affirmation.

### 6.2 The Fidelity-Authenticity Tension

The central intellectual contribution of this study is the identification and partial resolution of the fidelity-authenticity tension in LLM-based simulation:

- **No constraint (full freedom):** LLM sycophancy drives rapid consensus. All agents agree. The simulation is meaningless.
- **Excessive constraint (full control):** Agents follow scripts rigidly. No genuine interaction occurs. The simulation is theater.
- **Calibrated constraint (the engine's approach):** Agents maintain their assigned identities while genuinely responding to each other. The simulation is informative.

The engine's approach is fundamentally informational rather than directive. The "Your prior positions:" soft prompt does not tell the agent how to behave; it reminds the agent who it is. The distinction matters: the directive approach ("Stay consistent with your assigned personality") caused diversity to collapse to 0.45 in early experiments, as agents interpreted the instruction as a command to avoid any position change. The informational approach achieves zero contradictions while maintaining behavioral diversity — a result consistent with the psychological principle that identity awareness promotes consistency more effectively than behavioral commands.

This framing rejects the assumption that fidelity and authenticity are competing objectives. Instead, this study argues that appropriate persona fidelity is a prerequisite for authentic interaction: without stable identities, agents cannot meaningfully disagree, negotiate, or compromise, because they have no positions from which to negotiate.

### 6.3 RLHF as a Fundamental Ceiling

The Neuroticism finding — self_doubt_count = 0.000 across all 4,080 runs in both conditions — constitutes the study's most important negative result. RLHF safety training has structurally eliminated the LLM's ability to express anxiety, self-doubt, and emotional vulnerability, regardless of how the persona prompt is configured or how aggressively the engine steers toward these behaviors.

This has two implications. First, it defines a boundary of feasibility for LLM-based persona simulation: researchers and practitioners must understand that certain personality dimensions are not merely difficult to simulate but fundamentally inaccessible with current RLHF-aligned models. Second, it suggests that the solution lies not at the engine level but at the model training level — either through targeted fine-tuning that relaxes safety constraints for simulation contexts or through alternative alignment approaches that preserve the model's capacity for emotional range.

The per-trait analysis supports this interpretation: Extraversion (−16.3% improvement) and Openness (−10.0%) respond well to engine intervention because their behavioral correlates (word count, question frequency, idea generation) are safely expressible. Agreeableness improvement is moderate (−4.6%) because low Agreeableness (disagreement, confrontation) conflicts with RLHF's preference for helpful, agreeable responses. Neuroticism (+1.1%, engine slightly worse) represents the floor — the point at which engine intervention encounters model-level refusal.

### 6.4 Iterative Refinement

The main 4,080-run benchmark identified two specific weaknesses: relationship overshoot (+23.9% in relationship change metrics) and suboptimal action validity (64.1%). A follow-up experiment of 240 runs was conducted after applying targeted calibrations:

1. **Relationship delta clamping:** Negative trust delta reduced from −0.18 to −0.10; tension delta reduced from +0.22 to +0.14; per-turn clamping added to prevent runaway relationship shifts.
2. **Fuzzy action validation:** Four additional validation pathways added for action_type, target_key, actor_id, and phase matching, reducing false invalidation.

The iterative refinement results:

| Metric | Pre-refinement | Post-refinement | Δ |
|--------|---------------|----------------|---|
| Persona Drift MAE | 0.1678 | 0.1654 | −1.4% |
| Envelope Violations | 2.057 | 1.957 | −4.9% |

These improvements, while modest, demonstrate that the main experiment → weakness identification → calibration → validation cycle is reproducible and productive. The refinement represents hyperparameter tuning (3 of 5 changes) and minor architectural additions (2 of 5), not fundamental redesign.

### 6.5 Application Domain

The engine's optimal application is multi-stakeholder policy deliberation simulation: previewing how 5–10 identified stakeholders would argue, negotiate, and potentially compromise around a specific policy proposal. This positioning aligns with the engine's demonstrated capabilities and avoids the gaps that would require fundamental architectural additions:

| Application | Suitability | Rationale |
|------------|-------------|-----------|
| Policy deliberation simulation | 9/10 | Exact match with benchmark scenarios and engine capabilities |
| Organizational dynamics / team simulation | 8/10 | OCEAN is designed for individual behavioral modeling |
| Communication training (medical, crisis) | 7/10 | "Angry stakeholder" personas are well-served by engine |
| UX research persona testing | 6/10 | Persona simulation applicable but trust/validity concerns |
| Business strategy simulation | 4/10 | Requires quantitative modeling, scenario branching, RAG |
| Financial / supply chain modeling | 2/10 | Structural/mathematical factors dominate; personality is peripheral |

Within the broader strategic simulation stack, the present engine constitutes the stakeholder agent engine — one layer of a full platform:

```
Full Strategic Simulation Platform
  ├── Domain Knowledge Layer (RAG / real-time search)         — not present
  ├── Scenario Tree Engine (Monte Carlo branching)            — not present
  ├── Quantitative Model (market / fiscal projections)        — not present
  ├── Stakeholder Agent Engine (persona-faithful deliberation) — THIS STUDY
  ├── Causal Reasoning Engine (commitment tracking, partial)  — partially present
  └── Decision Support Interface (executive summary, UI)      — not present
```

Persona fidelity is a prerequisite for this full stack: if individual agents cannot maintain consistent positions, no amount of additional modeling produces reliable results. The present study validates the foundational layer upon which the remaining components can be built.

The market context reinforces this positioning. While Simile ($100M) and Aaru (~$1B) have attracted substantial funding for population-scale prediction — simulating how thousands or millions of people might react — no funded product addresses the small-group deliberation gap: how 5–10 specific, named stakeholders negotiate, form coalitions, and reach or fail to reach consensus. This is the niche the present engine occupies, and it is a niche that consulting firms currently fill with $500K+ manual war-gaming exercises.

### 6.6 Limitations

1. **Single LLM dependency.** All experiments use DeepSeek V3 as the generation model. Results may not generalize to other model families (GPT-4o, Claude, Gemini), each of which has different RLHF characteristics and behavioral ranges.

2. **Absence of human evaluation.** All metrics are computed automatically through deterministic feature extraction. No policy experts or domain specialists have qualitatively assessed whether the simulated deliberations produce realistic or useful insights.

3. **Training data leakage.** Scenarios are drawn from well-documented real-world events (FTX Collapse, Boeing 737 MAX). LLMs may produce responses informed by their training data rather than genuine reasoning from assigned personas, artificially inflating performance.

4. **CLOSING phase convergence.** The engine does not fully resolve the convergence magnet effect in the CLOSING phase, where all agents default to summarizing and agreeing regardless of engine intervention.

5. **OCEAN framework adequacy.** The Big Five personality model was designed for individual psychology, not institutional stakeholder behavior. Whether OCEAN is the appropriate framework for modeling how an organization's representative negotiates remains an open question.

6. **Action validity rate.** At 64.1%, more than one-third of extracted actions are structurally invalid, indicating room for improvement in the hybrid extraction pipeline.

### 6.7 Future Work

1. **Multi-model comparison.** Benchmarking persona fidelity across DeepSeek V3, GPT-4o, Claude 3.5, and Gemini to identify model-specific behavioral ceilings and optimal model-engine pairings.

2. **Human evaluation.** Engaging 5–10 policy professionals to qualitatively assess simulation realism, informational value, and actionability through structured interviews and Likert-scale ratings.

3. **Interactive mode.** Enabling a human user to assume one stakeholder role while AI agents play the remaining roles, creating a training and rehearsal tool for negotiation preparation.

4. **CLOSING anti-convergence.** Implementing phase-specific sycophancy thresholds and diversity-preserving interventions to combat the convergence magnet effect in final deliberation phases.

5. **Action vocabulary expansion.** Extending from 12 to 18+ action types with domain-specific actions (e.g., file_regulatory_comment, propose_amendment) and improved semantic extraction.

6. **Strategic simulation platform.** Integrating RAG-based domain knowledge, quantitative scenario branching (Monte Carlo simulation), and decision support dashboards to evolve from a stakeholder agent engine to a complete policy simulation platform.

---

## Chapter 7: Conclusion

Multi-stakeholder policy deliberation is among the highest-stakes communicative processes in governance, yet policymakers currently lack tools to preview how diverse stakeholders will react to, argue against, and negotiate around proposed policies. This study addresses the technical prerequisites for such a tool by tackling three fundamental problems in LLM-based multi-agent simulation: persona drift, sycophancy convergence, and the RLHF behavioral ceiling.

The simulation engine presented in this study integrates six components — a Persona State Controller monitoring 30 behavioral features, a 4-Slot Candidate Pool generating diverse rhetorical styles, Sycophancy Detection calibrated to scenario polarity and actor disposition, a Commitment Lifecycle tracker maintaining positional consistency, an Action Layer extracting 12 structured action types with world-state deltas, and Strategic Disposition calibration enabling per-actor behavioral differentiation. Together, these components constitute a comprehensive approach to maintaining individual behavioral fidelity in multi-agent deliberation.

A benchmark of 4,080 simulation runs across 20 real-world scenarios demonstrates that the engine reduces persona drift by 5.7% (Cohen's d = −0.94, large effect), envelope violations by 9.9%, and sycophantic acknowledgment by 69%, while increasing idea generation by 267% and authentic disagreement by 37%. The engine achieves universal advantage across all 20 scenarios, with non-overlapping 95% confidence intervals. These results establish that structured persona control produces not merely statistical improvement but a qualitative transformation in conversation dynamics — from sycophantic consensus to substantive deliberation.

However, this study also reveals the boundaries of what current LLM-based approaches can achieve. The RLHF behavioral ceiling — evidenced by zero self-doubt expression across all 4,080 runs — demonstrates that certain personality dimensions (particularly high Neuroticism and low Agreeableness) are structurally inaccessible in RLHF-aligned models, regardless of engine sophistication. This finding defines a research frontier that requires intervention at the model training level rather than the application level.

The tension between persona fidelity and interaction authenticity emerges as the central theoretical contribution. This study demonstrates that these are not competing objectives but complementary requirements: calibrated persona fidelity — achieved through informational nudging rather than behavioral commands — is a prerequisite for authentic multi-stakeholder interaction. Without stable identities, agents cannot meaningfully disagree; without meaningful disagreement, deliberation simulation provides no insight.

As LLM-based simulation moves from research prototypes toward production systems, persona fidelity is not merely a desirable property but a prerequisite for meaningful multi-stakeholder deliberation. This study demonstrates both the feasibility and the boundaries of achieving such fidelity, providing a foundation for the next generation of policy simulation tools.

---

## References

*(Organized by appearance in text. Citations marked with [REF: filename.pdf] indicate papers available in the project reference folders.)*

### From "LLM papers for personality trait" folder:
1. Park, J. S., Zou, C. Q., Shaw, A. et al. "Generative Agent Simulations of 1,000 People." Stanford University, Google DeepMind. [REF: Generative Agent Simulations of 1,000 People.pdf]
2. Wei, J., Huang, D., Lu, Y., Zhou, D., Le, Q. V. (2024). "Simple Synthetic Data Reduces Sycophancy in Large Language Models." Google DeepMind. [REF: SIMPLE SYNTHETIC DATA REDUCES SYCOPHANCY IN LLM.pdf]
3. Jain, S., Park, C., Viana, M., Wilson, A., Calacci, D. (2026). "Interaction Context Often Increases Sycophancy in LLMs." MIT, Penn State. CHI 2026. [REF: Interaction Context Often Increases Sycophancy in LLMs.pdf]
4. Abdulhai, M., Cheng, R., Clay, D. et al. (2025). "Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning." UC Berkeley, Google DeepMind. NeurIPS 2025. [REF: Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning.pdf]
5. Liu, Y., Wei, W., Liu, J. et al. (2022). "Improving Personality Consistency in Conversation by Persona Extending." CIKM 2022. [REF: Improving Personality Consistency in Conversation by Persona Extending.pdf]
6. Du, B., Guo, M., He, S. et al. (2025). "A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona (TwinVoice)." Tsinghua University. [REF: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona.pdf]
7. Li, R., Xia, H., Yuan, X. et al. (2025). "How Far are LLMs from Being Our Digital Twins? A Benchmark for Persona-Based Behavior Chain Simulation." ACL 2025. [REF: How Far are LLMs from Being Our Digital Twins?.pdf]
8. Paglieri, D., Cross, L., Cunningham, W. A., Leibo, J. Z., Vezhnevets, A. S. (2026). "Persona Generators: Generating Diverse Synthetic Personas at Scale." Google DeepMind. [REF: google-deepmind-Persona Generators.pdf]
9. Lee, S., Lim, S., Han, S. et al. (2025). "Do LLMs Have Distinct and Consistent Personality? TRAIT: Personality Testset designed for LLMs with Psychometrics." NAACL 2025. [REF: Do LLMs Have Distinct and Consistent Personality?.pdf]
10. Hilliard, A., Munoz, C., Wu, Z. et al. (2024). "Eliciting Personality Traits in Large Language Models." FAccT 2024. [REF: Eliciting Personality Traits in Large Language Models.pdf]
11. Wang, P., Zou, H., Chen, H. et al. (2025). "Personality Structured Interview for Large Language Model Simulation in Personality Research." [REF: Personality Structured Interview for Large Language Model Simulation in Personality Research.pdf]
12. Wuttke, A., Aßenmacher, M., Klamm, C. et al. (2025). "AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers." ACL 2025. [REF: AI Conversational Interviewing: Transforming Surveys with LLMs as Adaptive Interviewers.pdf]
13. Gupta, A., Sheikh, F. R. (2026). "LLM-Powered Social Digital Twins: A Framework for Simulating Population Behavioral Response to Policy Interventions." PwC. [REF: LLM-Powered Social Digital Twins.pdf]
14. Stureborg, R., Alikaniotis, D., Suhara, Y. et al. (2024). "Large Language Models are Inconsistent and Biased Evaluators." [REF: Large Language Models are Inconsistent and Biased Evaluators.pdf]
15. Verga, P., Hofstätter, S., Althammer, S. et al. (2024). "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models." [REF: Replacing Judges with Juries.pdf]
16. Li, B., Wei, Q., Wang, X. et al. "Predicting Behaviors with Large Language Model (LLM)-Powered Digital Twins of Consumers." [REF: Predicting Behaviors with Large Language Model (LLM)-Powered Digital Twins of Consumers.pdf]
17. John, O. P. & Srivastava, S. (1999). "The Big Five Trait Taxonomy: History, Measurement, and Theoretical Perspectives." In Handbook of Personality. [REF: BigFiveInventory.pdf]
18. Laban, P., Hayashi, H., Zhou, Y., Neville, J. (2025). "LLMs Get Lost in Multi-Turn Conversation." Microsoft Research, Salesforce. [REF: LLMS GET LOST IN MULTI-TURN CONVERSATION.pdf]

### From "papers for LLM simulation" folder:
19. Shapira, N., Wendler, C., Yen, A. et al. (2026). "Agents of Chaos." Northeastern, Stanford, Harvard et al. [REF: Agents of Chaos.pdf]

### From "papers for group discussion with AI" folder:
20. Hu, E., Chen, Y., Li, M., Phadnis, V., Xu, P., Qian, X. (2025). "DialogLab: Authoring, Simulating, and Testing Dynamic Human-AI Group Conversations." UIST 2025. [REF: google dialoglab.pdf]

### External References (not in project folders):
21. Costa, P. T. & McCrae, R. R. (1992). Revised NEO Personality Inventory (NEO-PI-R) and NEO Five-Factor Inventory (NEO-FFI) professional manual.
22. Bakker, M., Tessler, M. H. et al. (2024). "Fine-tuning language models to find agreement among humans with diverse preferences." Science.
23. Council on Environmental Quality (2024). Environmental Impact Statement Timeline Report.

---

## Appendices

### Appendix A: Complete Scenario List

*(20 scenarios with actor counts, structural polarity, and domain classification — to be populated from manual_scripts.py)*

### Appendix B: 30 Behavioral Features — Complete Definition and OCEAN Mapping

*(Full table with feature name, extraction method, primary trait association, and weight in OCEAN estimation formula — to be populated from metrics.py)*

### Appendix C: Scoring Function Detailed Formulation

*(Complete mathematical specification of the candidate scoring function, including all weight parameters, penalty terms, and phase modifiers — to be populated from controller.py)*

### Appendix D: Sample Simulation Transcript

*(A complete 11-turn simulation transcript from the Starbucks Unionization 3-actor scenario, with annotations showing candidate scoring, action extraction, and persona drift at each turn)*

### Appendix E: Iterative Refinement Detailed Results

*(Complete 240-run benchmark results comparing pre- and post-refinement metrics, with per-scenario breakdowns)*
