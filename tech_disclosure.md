# UbeU: A Behavioral Fidelity Engine for Multi-Stakeholder LLM Persona Simulation Using OCEAN-Anchored Drift Control and Ensemble Evaluation

---

## 1. Background of the Application

### 1.1 General Overview of the Problem

In computational social simulation, researchers and practitioners increasingly rely on large language model (LLM) agents as synthetic substitutes for human participants — for user testing [1], policy impact forecasting [2], negotiation training [3], and consumer behavior modeling [4]. These applications assign personality profiles (typically Big Five / OCEAN traits) to LLM agents and expect them to behave accordingly across sustained, multi-turn interactions.

This problem is becoming more urgent because deployment is outpacing validation. Organizations are building digital twins [5], population-scale policy simulators [2], and interactive training environments on the assumption that personality-conditioned LLMs actually express the traits they are assigned. If this assumption is wrong, every downstream decision based on these simulations — from product design to public policy — rests on unreliable behavioral proxies.

The core issue is that **RLHF-tuned LLMs systematically collapse toward a cooperative, conflict-avoidant communication style regardless of assigned personality** [6]. A persona assigned low Agreeableness still says "That's a great point." A persona assigned high Neuroticism still responds calmly to criticism. In casual conversation, all LLM personas look the same. This persona convergence renders personality assignment cosmetic — labels without behavioral substance.

### 1.2 Why Pressure Is a Diagnostic Necessity

Personality traits are most observable under social pressure. Just as cardiac stress tests reveal vulnerabilities invisible in resting ECGs, social friction and conflict expose trait differences invisible in calm dialogue [7]. Without pressure, trait discrimination between agents approaches zero: a high-Extraversion agent and a low-Extraversion agent produce responses of similar length, structure, and tone. This means any simulation system that aims to model realistic stakeholder behavior must create conditions where personality differences become observable — and then maintain those differences throughout extended conversations without drift.

---

## 2. Reviewing Existing Potential Solutions

### 2.1 Traditional Role-Play and Manual Simulation

Traditional stakeholder simulations use human role-players in facilitated workshops. While these produce authentic behavioral diversity, they are expensive ($500–2,000 per session), difficult to scale beyond 5–10 participants, and impossible to reproduce exactly [8]. Each session yields unique dynamics that cannot be systematically compared or ablated.

### 2.2 Commercial LLM-Based Persona Platforms

Commercial platforms such as Synthetic Users and character.ai allow persona specification through natural language prompts. These systems handle single-turn or short multi-turn interactions well but suffer from **persona leakage** — gradual reversion to generic LLM behavior over extended conversations [9]. They provide no mechanism for trait drift monitoring, commitment consistency tracking, or behavioral fidelity measurement. The persona is a prompt, not a maintained state.

### 2.3 Recent Multi-Agent AI Frameworks

Research frameworks such as Concordia [10], Generative Agents [11], and CAMEL [12] demonstrate multi-agent LLM interaction with memory and planning capabilities. However, these systems optimize for task completion or narrative coherence rather than **behavioral fidelity** — the accuracy with which an agent's observable behavior matches its assigned personality profile. They lack mechanisms for persona drift control, trait-conditioned candidate selection, or systematic evaluation of personality expression.

### 2.4 The Remaining Gap

Existing solutions either produce authentic behavior without scalability (human role-play), scale without fidelity (commercial platforms), or coordinate multiple agents without personality stability guarantees (research frameworks). There remains a need for a simulation engine that (a) maintains assigned personality traits across extended multi-stakeholder conversations, (b) provides real-time drift detection and correction, (c) evaluates behavioral fidelity through independent, non-circular metrics, and (d) scales to arbitrary numbers of actors and scenarios while preserving persona integrity.

---

## 3. Summary of Literature Reviews that Guided the Approach

### 3.1 Personality Expression in LLM Agents

PersonaLLM [13] demonstrated that assigning Big Five trait labels to LLMs produces detectable personality differences in generated text, with human perception accuracy of approximately 80% and large effect sizes (Cohen's d = 0.65–1.80 across traits) on BFI self-report measures. However, this validation used single-turn questionnaire responses, not sustained behavioral expression in interactive settings. The PERSONAGE system [14] empirically validated mappings between Big Five traits and 67 linguistic parameters (verbosity, hedging, lexical choice) based on 2,000+ personality ratings. Based on these findings, UbeU adopts a **hybrid prompt design** — combining trait labels for interpretability with empirically grounded behavioral descriptors for precision, rather than relying on either approach alone.

### 3.2 RLHF Sycophancy and Trait Suppression

Santurkar et al. [6] demonstrated that RLHF tuning causes LLMs to converge toward opinions and behaviors aligned with the training distribution, systematically suppressing disagreeable, anxious, or emotionally volatile expression. This finding directly informed UbeU's design: traits most affected by RLHF suppression (Agreeableness and Neuroticism) require **active generation-level intervention** — not just post-hoc scoring — to produce authentic behavioral variation. The system addresses this through personality-conditioned candidate pool generation with style-diverse slots and trait-specific behavioral instructions grounded in psycholinguistic research [14][15][16].

### 3.3 Behavioral Feature Extraction from Text

Pennebaker and King [15] established robust correlations between word categories (analyzed via LIWC) and personality traits across 2,400 essays. Mehl et al. [16] extended this to naturalistic speech, showing that extraverts speak more in group settings and neurotics exhibit more negative affect. A group discussion study [17] demonstrated that LIWC-based features — certainty words, negative emotions, positive emotions, and discrepancy words — predict Big Five traits in interactive, multi-party contexts closely matching UbeU's simulation format. These findings guided UbeU's 30-feature behavioral extraction battery, which provides a **fully deterministic, non-LLM evaluation pathway** that avoids the circularity of using language models to evaluate language model output.

### 3.4 Multi-Agent Simulation Architectures

Concordia [10] introduced the Logic of Appropriateness framework, where agents reason per-turn about "what would a person like me do in this situation?" Paglieri et al. [1] extended this with AlphaEvolve-optimized persona generation for diversity. However, their evaluation metric is persona diversity (how different are generated personas from each other), not behavioral fidelity (does a high-E persona actually behave extraverted?). Based on this distinction, UbeU adopts a **modular architecture** separating generation, scoring, selection, and evaluation into independent components — enabling ablation studies that isolate the contribution of each mechanism to fidelity outcomes.

### 3.5 Synthesis of Findings

The literature converges on three design implications: (1) personality expression is detectable in LLM output but decays without active maintenance, (2) RLHF suppression disproportionately affects Agreeableness and Neuroticism expression, requiring generation-level rather than selection-level intervention, and (3) behavioral fidelity evaluation requires non-circular methods combining rule-based feature extraction with cross-model ensemble scoring. UbeU's architecture directly addresses all three findings through its persona drift controller, style-diverse candidate generation, and dual-track evaluation pipeline.

---

## 4. Novelty of UbeU

The novelty of UbeU lies in combining **OCEAN-anchored persona drift control**, **action-conditioned multi-stakeholder dialogue generation**, and **dual-track behavioral fidelity evaluation** into a unified simulation engine. Unlike existing multi-agent frameworks that optimize for task completion or narrative coherence, UbeU treats personality stability as a first-class runtime constraint, continuously measured and corrected throughout the simulation.

Specifically, UbeU introduces five mechanisms not present in prior systems:

1. **Commitment lifecycle management**: The system automatically extracts commitments from dialogue text, tracks their fulfillment across turns, detects contradictions in real-time, and resolves stale commitments at phase boundaries. A soft context injection approach ("Your prior positions: [list]") eliminates contradictions entirely (0.0 rate across 144 experimental runs) without suppressing behavioral diversity — solving a tension that directive approaches ("stay consistent unless explicitly revising") could not [18].

2. **Dynamic trait calibration**: Rather than measuring Conscientiousness against absolute behavioral feature thresholds (which are biased by the LLM's structural tendency toward organized output), UbeU measures trait expression relative to the conversation baseline. This approach reduced Conscientiousness evaluation error by 38% (0.280 to 0.173) where static coefficient adjustments repeatedly failed [18].

3. **Style-diverse candidate pool generation with per-slot action vocabulary rotation**: Each turn generates 4–5 candidate responses using distinct "style slots" (integrator, planner, challenger, skeptic), each seeded with different action vocabularies. This produces behavioral diversity at the **generation level** rather than relying on selection-level mechanisms like softmax sampling, which experiments showed adds +12.7% drift with zero diversity improvement [18].

4. **Guided and exploratory dual-track simulation modes**: Guided mode anchors simulations to target end-states (e.g., policy alignment should increase, uncertainty should decrease), while exploratory mode preserves authentic disagreements and divergent trajectories. This enables modeling both structured decision-making processes and open-ended crisis deliberations within the same engine.

5. **Cross-model ensemble evaluation with rule-based convergent validity**: Five LLM judges from five different providers (DeepSeek V3, Gemini 2.5 Flash, Grok 4.1 Fast, Claude Haiku 4.5, GPT-4o-mini) evaluate personality expression using dual-order prompting, with median aggregation. An independent deterministic scorer using 30 sigmoid-normalized behavioral features provides a fully non-LLM evaluation pathway. Agreement between methods establishes convergent validity; divergence identifies LLM-biased traits.

---

## 5. System Architecture and Technical Workflow

### 5.1 Overall Architecture

UbeU operates as a phased simulation runtime built on a LangGraph state machine. A simulation script defines the scenario, stakeholders, phase structure, world state schema, action transition rules, and evaluation targets. The engine executes turn-by-turn within each phase, generating, scoring, and selecting dialogue for each actor while maintaining a persistent state ledger that tracks personality drift, commitment fulfillment, relationship dynamics, and world state evolution.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SIMULATION RUNTIME                           │
│                                                                     │
│  ┌──────────┐   ┌──────────────┐   ┌────────────┐   ┌───────────┐ │
│  │ Script   │──▶│ Actor Pool   │──▶│ Candidate  │──▶│ State     │ │
│  │ & Config │   │ Generation   │   │ Scoring &  │   │ Ledger    │ │
│  │          │   │ (5 slots)    │   │ Selection  │   │ Update    │ │
│  └──────────┘   └──────────────┘   └────────────┘   └───────────┘ │
│       │                                    │               │       │
│       │         ┌──────────────┐           │               │       │
│       └────────▶│ Phase &      │◀──────────┘               │       │
│                 │ Action Layer │◀───────────────────────────┘       │
│                 └──────────────┘                                    │
│                        │                                            │
│                        ▼                                            │
│              ┌──────────────────┐                                   │
│              │ Dual-Track       │                                   │
│              │ Evaluation       │                                   │
│              │ (Ensemble + Rule)│                                   │
│              └──────────────────┘                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Core Modules

**Simulation Script**: Defines the scenario contract — stakeholder specifications (OCEAN priors, personality envelopes, incentives, concerns, communication style), phase definitions (name, goal, style, cues, max turns), world state schema with initial values, action transition rules, world events, and outcome specifications. A builder module enriches user-provided briefs into complete scripts using scenario family detection and deterministic defaults.

**Stakeholder Actor**: Each actor wraps a candidate agent with a persistent identity. The system prompt includes stable identity core (role, incentives, concerns), OCEAN personality prior with empirically grounded behavioral instructions, communication style parameters, salient memories, experience summary, open commitments ("Your prior positions"), and world brief context. Actors generate policy plans and candidate response pools asynchronously.

**Persona State Controller**: The deterministic scoring engine that maintains behavioral fidelity. For each turn, it receives 4–5 candidate responses and scores them across 15+ weighted dimensions: persona consistency (trait drift from prior), identity consistency (keyword alignment to role specification), commitment continuity (contradiction detection against open commitments), relationship consistency (trust/tension directional coherence), social trait alignment (Extraversion, Agreeableness, Neuroticism stability bands), trait target alignment (Openness, Conscientiousness opportunity-based banded signals), and action-layer components (executability, state consistency, plan alignment, role fit, diversity). The final score is a weighted sum clamped to [0, 1], with tie-breaking via trait-opportunity axis routing.

**State Ledger**: The central persistence layer tracking all simulation state. It maintains per-turn records, per-actor dynamic state (beliefs, stress, trait estimates, drift history), directed relationship edges (trust, tension, sentiment between each actor pair), commitment lifecycle (extraction, fulfillment, staleness, contradiction), action proposals and executions, and world state snapshots per phase. The ledger enables context-aware generation: each actor's prompt includes their current commitments, relationship map, and relevant state trajectory.

**Action Layer**: Separates "what to say" (dialogue generation) from "what to do" (structured actions). Eight action types map to seven semantic families: ownership, evidence, communication, scope, resourcing, timing, and governance. Actions are proposed via heuristic extraction from turn text, arbitrated per-phase, and executed as state deltas to global and local actor state via configurable transition rules.

**Metrics Engine**: Computes simulation-level quality metrics including persona drift MAE, per-trait absolute errors, commitment contradiction rate, relationship inconsistency/shift/overshoot rates, envelope violations, action family convergence, role action diversity, fallback utterance rate, and phase-end world state trajectory variance.

### 5.3 User Workflow

1. **Brief Input**: The user provides a natural language scenario brief describing the decision context and key stakeholders (e.g., "A hospital is deciding whether to adopt AI-assisted diagnostics").

2. **Script Generation**: An LLM generates a structured simulation script from the brief, specifying stakeholders with OCEAN personality priors, phase structure, world state schema, and action rules. A deterministic builder enriches the generated script with scenario-family-specific defaults, transition rules, and action policies.

3. **Simulation Execution**: The engine runs the multi-phase simulation, generating dialogue turn-by-turn. For each turn: a policy plan is produced, 4–5 candidate responses are generated across diverse style slots, the persona controller scores and selects the best candidate, the state ledger is updated with commitment tracking, relationship dynamics, and trait estimates, and any structured actions are proposed and executed.

4. **Evaluation**: After simulation completion, behavioral features are extracted from each actor's dialogue. The rule-based evaluator produces deterministic OCEAN scores. The 5-model LLM ensemble produces evidence-traced OCEAN scores with dual-order prompting. Both evaluation tracks are compared for convergent validity.

5. **Analysis**: Results are aggregated across conditions, scenarios, and actor configurations. Persona drift, contradiction rates, action diversity, and envelope violations are reported with 95% confidence intervals. Engine vs. naive baseline comparisons quantify the contribution of each system component.

---

## 6. Advantages Over Existing Approaches

**Behavioral fidelity as a runtime constraint, not a post-hoc hope.** Unlike existing multi-agent systems that generate dialogue and hope personality emerges, UbeU continuously measures trait drift per actor per turn and actively corrects deviations through candidate selection, drift nudging, and commitment context injection. Experimental results show the engine reduces persona drift by 13–23% compared to naive LLM generation [18].

**Zero commitment contradictions.** The commitment lifecycle system — combining automatic extraction, fulfillment tracking, staleness resolution, and soft context injection — achieves a 0.0 contradiction rate across 144+ experimental runs. Directive approaches ("stay consistent") suppress diversity; UbeU's listing-only approach ("Your prior positions:") preserves diversity while eliminating contradictions [18].

**Non-circular evaluation.** The dual-track evaluation design (5-model cross-provider ensemble + 30-feature deterministic scorer) avoids the methodological trap of using LLMs to evaluate LLM output. Every evaluation score is auditable against specific transcript quotes with turn numbers, signal directions, and signal strengths.

**Scalable to arbitrary actor counts.** The engine has been validated from 2 to 10 actors with only +0.009 drift increase when scaling from 2 to 5 actors [18]. Dynamic max-turns scaling adjusts phase length to accommodate more speakers, and per-actor action vocabulary rotation maintains diversity as the participant count grows.

**Ablation-ready architecture.** Every design decision can be isolated and tested. The ablation framework supports 11 benchmark conditions, enabling systematic comparison of naive baseline, dialogue-only engine, action-aware engine, softmax sampling, and individual component knockouts. This makes the system a research platform, not just an application.

---

## 7. Potential Applications and Impact

**Negotiation training and preparation.** Organizations can simulate stakeholder negotiations before actual meetings, exploring how different personality compositions and pressure dynamics affect outcomes. Trainees interact with persona-stable agents that maintain realistic positions, commitments, and emotional responses throughout extended sessions.

**Policy impact forecasting.** Governments and NGOs can model how proposed policies affect diverse stakeholder groups — simulating reactions from affected populations, industry representatives, regulators, and advocacy groups with distinct personality profiles and incentive structures. The system's real-world scenario grounding (tested on 20 historical events including California AB5, EU GDPR, Flint water crisis, and FTX collapse) demonstrates generalization beyond synthetic benchmarks.

**Enterprise onboarding and scenario planning.** Companies can simulate post-merger integration dynamics, product launch stakeholder alignment, organizational change management, and crisis response — with agents that realistically represent engineering leads, finance controllers, community managers, and affected employees.

**Behavioral research platform.** The system provides a controlled environment for studying personality expression in LLM agents, RLHF sycophancy effects, commitment consistency, and group dynamics. The ablation framework, checkpoint system, and comprehensive metrics suite make it suitable for systematic computational behavioral research.

**Educational simulation.** Students and educators can use the system to explore historical decision-making scenarios with realistic multi-stakeholder dynamics — understanding how different interests, personalities, and power structures shaped outcomes in documented real-world events.

---

## 8. Conclusion

In summary, the behavioral fidelity of LLM-based synthetic personas remains insufficiently addressed by current tools, which either lack mechanisms for personality drift control, fail to detect commitment contradictions, or rely on circular evaluation methods. This disclosure proposes UbeU, a multi-stakeholder simulation engine that treats personality stability as a continuously measured and corrected runtime constraint rather than a static prompt instruction.

By combining OCEAN-anchored persona drift control, commitment lifecycle management, style-diverse candidate generation, action-conditioned dialogue, and dual-track non-circular evaluation, UbeU provides a measurably more faithful simulation of personality-driven group dynamics. Experimental validation across 480+ benchmark runs on 20 real-world historical scenarios with 3 to 10 actors demonstrates consistent improvement over naive baselines — reduced persona drift, zero commitment contradictions, and maintained behavioral diversity at scale.

---

## References

[1] Paglieri, S., et al. "Persona Generators: Generating Diverse Synthetic Personas with LLMs." *Proceedings of NeurIPS*, 2026.

[2] Social Digital Twins Consortium. "Population-Scale Policy Simulation Using LLM-Based Digital Twins." Technical Report, 2026.

[3] Li, X., et al. "BehaviorChain: Behavioral Prediction with LLM-Based Digital Twins." *Proceedings of ACL*, 2025.

[4] Marketing Science Institute. "Consumer Modeling with Synthetic Personas." MSI Working Paper Series, 2025.

[5] TwinVoice Research Group. "TwinVoice: Digital Twin Voice Agents for Behavioral Simulation." Technical Report, 2025.

[6] Santurkar, S., et al. "Whose Opinions Do Language Models Reflect?" *Proceedings of ICML*, 2023.

[7] Scherer, K. "Personality Inference from Voice Quality: The Loud Voice of Extraversion." *European Journal of Social Psychology*, 9(4), 1979.

[8] Lewicki, R., Barry, B., & Saunders, D. *Negotiation: Readings, Exercises, and Cases.* McGraw-Hill, 2020.

[9] Shanahan, M., et al. "Role-Play with Large Language Models." *Nature*, 623, 2023.

[10] Leibo, J.Z., et al. "Concordia: A Library for Generative Social Simulation." *Proceedings of AAMAS*, 2024.

[11] Park, J.S., et al. "Generative Agents: Interactive Simulacra of Human Behavior." *Proceedings of UIST*, 2023.

[12] Li, G., et al. "CAMEL: Communicative Agents for 'Mind' Exploration of Large Language Models." *Proceedings of NeurIPS*, 2023.

[13] Jiang, H., et al. "PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits." *Proceedings of NAACL*, 2024.

[14] Mairesse, F. & Walker, M. "PERSONAGE: Personality Generation for Dialogue." *Journal of Artificial Intelligence Research*, 30, 2007.

[15] Pennebaker, J. & King, L. "Linguistic Styles: Language Use as an Individual Difference." *Journal of Personality and Social Psychology*, 77(6), 1999.

[16] Mehl, M., et al. "Personality in Its Natural Habitat: Manifestations and Implicit Folk Theories of Personality in Daily Life." *Journal of Personality and Social Psychology*, 90(5), 2006.

[17] PMC 9523152. "Big Five Personality Traits and Linguistic Features in Group Discussion Contexts." *PLOS ONE*, 2022.

[18] Park, J. "UbeU V5 Simulation Engine: Experimental Results Log." Internal Technical Report, 2026.
