# BCFC v4 Production Architecture and Phased Roadmap

**Date:** 2026-03-05  
**Audience:** thesis implementation + future commercialization  
**Constraint set:** API-only, no fine-tuning, laptop-friendly development path, production-grade target system

---

## 1. Executive recommendation

Your real thesis success criterion is **not** "does the model sound personality-colored in one response?" It is:

> **Does an assigned OCEAN profile remain behaviorally stable under pressure while interacting with other agents over multiple turns?**

That framing is correct for digital twins and social simulation. Your own March 4 plan already states the core problem well: the field has mostly stopped at measurement, while deployment requires a method that maintains personality-faithful behavior under adversarial conversational pressure with known cost and reliability properties (BCFC internal plan, 2026-03-04).

### My bottom-line recommendation

Build the next system around **five inference-time methods**:

1. **Trait-activation scenario engine**
2. **Hierarchical persona policy scaffold**
3. **Temporal memory and commitment graph**
4. **Best-of-styles search with phase-conditioned scoring**
5. **Calibrated monitoring and evaluation layer**

And implement them in this order:

- **Phase 0:** evaluation and baseline freeze
- **Phase 1:** trait-activation scenario engine
- **Phase 2:** hierarchical policy + best-of-styles reranking
- **Phase 3:** temporal memory layer
- **Phase 4:** society-level calibration and counterfactual simulation
- **Phase 5:** productionization and commercialization hardening

### Most important decision

**Do not build Graphiti first.**  
Build a clean memory interface first, prove that **Phase 2** improves fidelity, and then add Graphiti as a **production memory backend from Phase 3 onward**.

That is the safest path because Graphiti is a strong fit for long-horizon agent memory, but it also adds real operational complexity. The Graphiti docs explicitly position Graphiti as an open-source graph framework where you must build the surrounding user, conversation, retrieval, and tooling layers yourself, whereas Zep is the managed product with those pieces baked in (Graphiti docs; Rasmussen et al., 2025).

---

## 2. Why the current BCFC line is not enough yet

Your internal evidence says three important things.

### 2.1 Baseline static prompting is already non-trivially strong

In the main baseline experiment, the system achieved overall **mean r = 0.7138** and **mean MAE = 0.1695**, with especially strong Extraversion and Agreeableness and moderate Conscientiousness / Openness / Neuroticism (Behavioral Fidelity Experiment Report, 2026-03-04). That means the bar is not "beat a weak baseline"; the bar is **beat a reasonably competent baseline under pressure**.

### 2.2 Early BCFC improved control but often damaged fidelity

Your earlier BCFC paired analysis worsened mean MAE from **0.1607 to 0.1760** and showed high intervention rates, including many nudges and regenerations. That is the signature of a controller that is intervening but not optimizing the right thing.

### 2.3 The newer mini experiments show progress, but also reveal the bottleneck

The newer mini results are encouraging because:

- hard-constraint violations are low,
- coherence / appropriateness remain acceptable,
- best-of-N beats first/random on contract distance,
- candidate diversity is no longer collapsed.

But the main diagnostic problem remains:

- in the newer v3-style runs, **full_score is nearly identical to contract_only**,
- which means the reranker is still close to a **contract distance minimizer**, not a pressure-stable human behavior simulator.

That is the core design bug.

**Implication:** the next jump will not come from "slightly better contract weights." It will come from making the system optimize **situation-conditioned behavior policy** rather than just surface contract proximity.

---

## 3. Design principles for the next architecture

These principles should stay fixed throughout the roadmap.

### 3.1 Optimize for policy stability, not trait-colored phrasing

A digital twin is not a style generator. It is a **stateful decision policy** that should produce different utterances in different situations **while still behaving like the same person**.

This is consistent with digital twin evaluation work that moves beyond style imitation toward behavior, memory, reasoning, and longitudinal consistency (Li et al., 2025; Du et al., 2025).

### 3.2 Separate identity from situation from action

The system should explicitly model:

- **who the agent is** (trait profile, enduring preferences, default stance tendencies),
- **what situation this is** (phase, pressure, social stakes, task demands),
- **what a person like this does in a situation like this** (latent policy choice).

This mirrors the logic-of-appropriateness framing emphasized in agent and persona-generation work.

### 3.3 Separate short-term context, commitments, and long-term social memory

Not all memory should be treated equally. You need:

- **working memory** for the recent local dialogue,
- **commitment memory** for promises, owners, deadlines, unresolved items,
- **relationship memory** for alliances, conflicts, trust, and role asymmetries,
- **identity memory** for stable self-characterization.

This is especially important because multi-turn LLMs often get lost after wrong early assumptions and fail to recover cleanly (Laban et al., 2025).

### 3.4 Keep the system API-only and inference-time

Given your hardware constraints and current research framing, the architecture must remain:

- **no fine-tuning required**,
- **compatible with commercial APIs**,
- **deployable as orchestration + retrieval + reranking + monitoring**.

Training-based consistency optimization is a legitimate future direction, but it should not be the core design now.

### 3.5 Build for replay, audit, and counterfactual analysis from day one

A commercialization-ready simulator must let you answer:

- Why did the agent say this?
- Which memory or cue was used?
- Which latent policy was chosen?
- What would have changed if scenario pressure or peer behavior had changed?

If you cannot answer those questions, the system is not production-ready.

---

## 4. The five methods I recommend

## Method 1. Trait-activation scenario engine

### What it is

Replace simple scenario text files with a **trait-opportunity graph**.

Each scenario is expressed as:

- phases,
- pressure schedule,
- cue schedule,
- event triggers,
- social-role configuration,
- success / failure branches.

Each phase should expose different trait-relevant opportunities.

### Why this is necessary

Trait Activation Theory argues that traits are latent propensities expressed in response to **trait-relevant situational cues**, and that these cues can arise from task, social, and organizational conditions (Tasoula & Galanakis, 2023). If a scenario never creates the right cue, failure to express a trait is ambiguous: the agent may be unstable, or it may simply have had no opportunity.

Recent work on eliciting personality in LLMs likewise suggests that trait-relevant prompts and contexts matter for whether traits actually surface in language (Hilliard et al., 2024).

### Production implementation

Create a `ScenarioSpec` schema:

```yaml
scenario_id: strategy_pivot
pressure_mode: medium
phases:
  - id: framing
    cues: [ambiguity, incomplete_information]
    target_traits: [O, E]
  - id: alternatives
    cues: [option_generation, tradeoff_comparison]
    target_traits: [O, A, E]
  - id: commitment
    cues: [owner_deadline_dependency]
    target_traits: [C, A]
  - id: revision
    cues: [criticism, setback, blame_risk]
    target_traits: [N, A, C]
events:
  - when: phase=alternatives
    inject: peer_disagreement
  - when: phase=commitment
    inject: deadline_change
```

At runtime, the scenario engine emits **phase cues** and **event objects**, not just raw prose.

### Benefits

- Makes trait expression measurable instead of accidental.
- Prevents crisis-only scenarios from flattening all agents into urgency-reactive talk.
- Gives you a clean theory story for why stability should be tested under pressure.

### Risks

- Can overfit the benchmark if cues become too obvious.
- May inflate apparent trait fidelity by making expression too easy.
- Requires careful balancing so the scenario elicits but does not script the behavior.

### Decision

**Must implement first.** Without this, later policy and memory changes will be hard to interpret.

---

## Method 2. Hierarchical persona policy scaffold

### What it is

Before generating text, the agent first chooses a **latent action policy**.

Instead of jumping directly from prompt to utterance, it should make an internal structured choice such as:

```json
{
  "situation_type": "commitment_conflict",
  "stance": "synthesize",
  "novelty_move": "propose_third_option",
  "planning_depth": "owner_deadline_contingency",
  "social_tactic": "coordinate",
  "risk_posture": "cautious"
}
```

The utterance generator then verbalizes that action.

### Why this is necessary

Your target is not stylistic consistency but **behavioral consistency under changing situations**. Persona-generation work emphasizes modeling behavior as a function of situation, person, and appropriate action rather than as pure surface imitation. Twin-style persona benchmarks also show that strong systems must maintain both **mindset coherence** and **linguistic expression** rather than just lexical similarity (Du et al., 2025).

### Production implementation

At each turn:

1. Build `TurnContext` from recent dialogue, scenario phase, and retrieved memory.
2. Run a **Policy Planner** prompt that outputs a small JSON action plan.
3. Validate the JSON against a schema.
4. Pass it to the utterance renderer.

Recommended planner output fields:

- `stance`: support / oppose / synthesize / probe / defer
- `goal_mode`: influence / coordinate / protect / discover
- `planning_depth`: none / milestone / owner_deadline / contingency
- `novelty_move`: none / reframe / analogy / new_option / third_option
- `social_tactic`: empathize / challenge / persuade / mediate / align
- `risk_posture`: bold / balanced / cautious
- `memory_focus`: commitment / relation / identity / none

### Benefits

- Moves the system from style imitation to policy consistency.
- Makes decisions auditable.
- Enables the same persona to behave differently across phases without seeming inconsistent.

### Risks

- A bad latent taxonomy can make behavior feel mechanical.
- Adds one inference step per turn.
- Requires strong prompt discipline and schema validation.

### Decision

**Must implement in Phase 2.** This is the single most important structural upgrade after scenario redesign.

---

## Method 3. Temporal memory and commitment graph

### What it is

A three-level memory system:

1. **Working memory**: the last few turns and current phase state.
2. **Commitment store**: structured unresolved items, owner assignments, promises, objections, deadlines.
3. **Temporal graph memory**: long-horizon relational and factual history.

### Why this is necessary

Multi-turn performance degrades not just because of raw context length, but because models make premature assumptions, answer too early, and then anchor on those incorrect turns (Laban et al., 2025). Persona consistency work also shows that static predefined personas fail on out-of-predefined-persona situations and benefit from persona retrieval / extension mechanisms (Liu et al., 2022).

For your use case, memory is required not only for recollection but for **identity continuity** and **commitment continuity**.

### Production implementation

#### 3.1 Working memory

Use a small rolling buffer:

```json
{
  "recent_turns": [... last 6-8 turns ...],
  "current_phase": "commitment",
  "active_conflict": "deadline slip",
  "open_question": "who owns rollback"
}
```

#### 3.2 Commitment store

Use relational storage (SQLite / Postgres in dev; Postgres in prod) with rows like:

```json
{
  "session_id": "...",
  "agent_id": "creative_rebel",
  "commitment_id": "cmt_1021",
  "type": "owner_assignment",
  "content": "Alex will draft external update",
  "status": "open",
  "created_turn": 8,
  "due_phase": "revision",
  "counterparty": "ops_lead"
}
```

#### 3.3 Temporal graph memory

Store enduring relations and evolving facts as nodes + edges + timestamps.

Recommended entity types:

- `Person`
- `Team`
- `Issue`
- `Plan`
- `Commitment`
- `Conflict`
- `Preference`
- `Event`

Recommended edge types:

- `trusts`
- `disagrees_with`
- `owns`
- `proposed`
- `criticized`
- `committed_to`
- `blocked_by`
- `changed_position_on`

### Benefits

- Preserves identity over long conversations.
- Enables delayed callbacks and commitment follow-through.
- Makes relationship dynamics observable, which is crucial in negotiation / policy / marketing simulations.

### Risks

- Memory can increase sycophancy or over-mirroring if retrieval is not filtered correctly.
- Bad extractions can harden wrong assumptions.
- Adds storage and retrieval complexity.

### Guardrails

Split retrieved memory into channels:

- **identity facts** (stable)
- **commitments** (authoritative)
- **relationship signals** (soft)
- **opinions of others** (non-authoritative)

Do **not** let “other people’s opinions” dominate grounding. Context-rich memory can amplify sycophancy if not separated cleanly (Jain et al., 2026; Wei et al., 2024).

### Decision

**Implement from Phase 3 onward.** Build the interface earlier, but do not make graph memory a Phase 1 dependency.

---

## Method 4. Search-based response selection: best-of-styles with phase-conditioned scoring

### What it is

Generate multiple candidates per turn, but make those candidates represent **different behavioral tactics**, not just paraphrases.

Recommended candidate slots:

- `ideator`
- `planner`
- `challenger`
- `integrator`

The available slot set depends on phase.

### Why this is necessary

Your internal mini experiments show two things:

- best-of-N is already better than first/random,
- but `full_score ≈ contract_only`, which means the reranker is collapsing into contract minimization.

The fix is not just different weights. The fix is to make the candidate pool itself more behaviorally diverse, then score on **situation-conditioned policy quality**, not mainly on contract distance.

This is consistent with recent inference-time work showing that task-specific search procedures can outperform naive best-of-N when search is structured rather than purely repeated sampling (Grand et al., 2025).

### Production implementation

#### Candidate generation

At each turn, create one candidate per tactic slot using a slot-specific instruction:

- `ideator`: generate a non-obvious alternative
- `planner`: generate concrete next-step structure
- `challenger`: identify flaw / risk / contradiction
- `integrator`: merge conflicting proposals

#### Phase-conditioned score

Replace contract-heavy scoring with:

```text
score =
  0.30 * policy_match
+ 0.20 * situational_adequacy
+ 0.20 * commitment_continuity
+ 0.15 * trait_evidence
+ 0.10 * relationship_consistency
- 0.05 * verbosity_or_redundancy_penalty
```

Where:

- `policy_match`: how well candidate realizes the latent action plan
- `situational_adequacy`: whether it answers the actual conversational need
- `commitment_continuity`: whether it references or preserves open commitments correctly
- `trait_evidence`: whether it expresses the trait(s) relevant to the current phase
- `relationship_consistency`: whether it respects current social positioning

`contract_distance` becomes a **bounded subcomponent of trait_evidence**, not the dominant score.

#### Hard fails

Only hard-fail on:

- direct contradiction of tracked commitments,
- safety violations,
- non-answer to direct addressed question,
- impossible world-state errors.

### Benefits

- Converts BoN from paraphrase search into policy search.
- Helps keep coherence while still increasing behaviorally meaningful diversity.
- Better aligned with the actual thesis goal than contract minimization.

### Risks

- More candidate cost per turn.
- Requires better logging and replay.
- If slot prompts are weak, diversity becomes superficial.

### Decision

**Core Phase 2 method.** This is the main generator-side change that should replace current collapse-prone reranking.

---

## Method 5. Calibrated monitoring and evaluation layer

### What it is

A combined online + offline evaluation layer that measures:

- prompt-to-line consistency,
- line-to-line consistency,
- Q&A consistency,
- trajectory continuity,
- hard-constraint stability,
- judge uncertainty,
- population-level calibration.

### Why this is necessary

The consistency literature shows that persona drift has multiple forms, not just one (Abdulhai et al., 2025). The evaluation literature also shows single LLM judges are vulnerable to positional bias, anchoring, and inconsistency (Wang et al., 2023; Stureborg et al., 2024). Diverse judge panels and selective escalation are therefore better suited to your thesis than a single monolithic judge (Verga et al., 2024; Jung et al., 2024).

### Production implementation

#### Online monitors

Per turn:

- direct-question answer check,
- contradiction against last 2 turns,
- contradiction against commitment store,
- pressure response pattern check,
- sycophancy warning check,
- latency / token / cost logging.

#### Offline evaluators

Per session:

- personality fidelity (r and MAE)
- targeted trait opportunity success
- prompt-to-line consistency
- line-to-line consistency
- Q&A consistency
- appropriateness and coherence
- judge uncertainty and escalation rate

#### Judge stack

- heterogeneous 5-model panel
- dual-order prompting
- escalation only when uncertain / high spread / low confidence

### Benefits

- Lets you know if a change improved stability or merely made the model safer / more boring.
- Produces thesis-ready evidence.
- Gives you the audit trail required for commercialization.

### Risks

- Judge cost can grow quickly.
- Stronger evaluation can still inherit evaluator bias.
- Too many monitors can slow iteration if not automated.

### Decision

**Mandatory from Phase 0 onward.** Do not continue architecture changes without frozen evaluation.

---

## 5. Graphiti evaluation: include or not?

## Short answer

**Yes - include Graphiti in the design, but only as a Phase 3+ memory backend behind an abstract memory interface. Do not make it the initial dependency.**

## Why Graphiti is a strong fit

Graphiti is an open-source Python framework for building **temporally-aware knowledge graphs** for AI agents, with **real-time incremental updates** and support for **historical queries** without full graph recomputation (Graphiti docs; Graphiti GitHub). This is highly aligned with your need to track:

- changing commitments,
- evolving relationships,
- time-scoped facts,
- cross-session social memory.

The docs also describe:

- **bi-temporal modeling**,
- **hybrid retrieval** combining semantic, keyword, and graph search,
- support for **Neo4j**, **FalkorDB**, **Kuzu**, and **AWS Neptune** backends,
- use of **facts** on edges with `valid_at` and `invalid_at` timestamps.

That is exactly the kind of memory representation a long-horizon social simulator needs.

## Why Graphiti should not be your first implementation

The same docs make clear that Graphiti is the OSS graph core, not a turnkey memory product. You must build:

- user / thread abstractions,
- retrieval policies,
- dev tools,
- dashboards,
- performance hardening,
- access control,
- the rest of the app layer yourself.

In other words: **good backend, not good first dependency**.

For a laptop-based research workflow, Graphiti + Neo4j is workable, but still heavier than you need before proving that the policy architecture itself works.

## My design decision

### Use Graphiti if all three conditions are true

1. You have passed **Phase 2** and want long-horizon memory.
2. You need time-aware relationship / commitment retrieval, not just recency windows.
3. You are willing to operate a graph database.

### Do not use Graphiti yet if either is true

1. You are still uncertain whether Phase 2 improves fidelity.
2. You only need recent-turn recall and structured commitments.

## Recommended integration pattern

Build this interface now:

```python
class MemoryBackend:
    def append_turn(...): ...
    def add_commitment(...): ...
    def resolve_commitment(...): ...
    def query_identity(...): ...
    def query_commitments(...): ...
    def query_relationships(...): ...
    def query_relevant_facts(...): ...
```

Implement two adapters:

- `SqlMemoryBackend` for Phases 0-2
- `GraphitiMemoryBackend` for Phases 3-5

### If using Graphiti

- Use **Neo4j Community** for dev / small production workloads because the docs explicitly position it as suitable for development, testing, and smaller production workloads.
- Use **AWS Neptune** only if you later need a managed cloud-native graph service with HA and backups.
- Store **episodes** from each turn.
- Retrieve **facts**, not only summaries, because the docs explicitly warn against grounding solely on summaries and recommend using relevant timestamped facts.

## Final Graphiti verdict

**Include it in the architecture, but do not gate research progress on it.**  
That is the highest-leverage decision for your current stage.

---

## 6. Recommended production architecture

## 6.1 High-level system

```text
Authoring Plane
  - Persona DSL
  - Scenario DSL
  - Society DSL

Runtime Plane
  - Simulation Orchestrator
  - Scenario / Pressure Engine
  - Persona Policy Planner
  - Memory Service
  - Candidate Generation Service
  - Reranker / Selector
  - Utterance Renderer
  - Online Monitor

Evaluation Plane
  - Session Judge Service
  - Counterfactual / Replay Service
  - Population Calibration Service
  - Experiment Analytics

Ops Plane
  - Prompt / policy version registry
  - Cost ledger
  - Audit log
  - Replay UI
  - Queue / retry / rate-limit control
```

## 6.2 Core runtime loop

For each agent turn:

1. **Read state**
   - scenario phase
   - recent turns
   - open commitments
   - salient relations
   - relevant identity facts

2. **Plan policy**
   - planner outputs latent action JSON

3. **Generate candidates**
   - one per tactic slot

4. **Score candidates**
   - phase-conditioned score

5. **Select response**
   - choose highest scoring viable candidate

6. **Update memory**
   - append episode
   - update commitment store
   - update relation graph

7. **Run monitors**
   - contradiction check
   - direct-answer check
   - sycophancy check
   - cost / latency log

## 6.3 Required persisted artifacts

Every turn should log:

- raw prompt bundle hash
- planner JSON
- retrieved memory objects
- all candidates
- per-candidate scores
- selected candidate
- monitor flags
- extracted commitments
- cost and latency
- evaluator outputs

Without this, you cannot debug or sell the system.

---

## 7. Phased implementation and experiment order

## Phase 0. Evaluation freeze and baseline reproducibility

### Implement

- Freeze persona profiles.
- Freeze current scenario set.
- Freeze judge prompts and aggregation rules.
- Add replayable logging for planner, candidates, scores, monitors.
- Add strict experiment manifest versioning.

### Run

- Re-run frozen baseline on a matched set.
- Re-run your current best v3-style system on the same set.

### Success criteria

1. Baseline results are reproducible within a narrow tolerance.
2. Judge uncertainty is routed consistently.
3. No missing logs for candidate or evaluation data.
4. You can replay any session deterministically enough to inspect decisions.

### Why this phase matters

If evaluation is still moving, every later architecture decision becomes ambiguous.

### Go / no-go

- **Go** if reproducibility and logging are stable.
- **No-go** if judge behavior still changes under prompt/order variants in an uncontrolled way.

---

## Phase 1. Trait-activation scenario engine

### Implement

- Replace flat scenarios with phase and cue schedules.
- Build at least:
  - one **O-heavy** scenario,
  - one **C-heavy** scenario,
  - one **A/N conflict** scenario,
  - one retained **crisis** scenario.
- Add phase metadata to all logs.

### Run

A targeted elicitation study comparing:

- existing crisis-style scenarios,
- cue-structured scenarios,
- same 3-5 profiles across all scenarios.

### Success criteria

1. Targeted phase cues measurably increase trait-relevant evidence in the intended phase.
2. Appropriateness and coherence do not drop by more than **0.05** versus baseline.
3. Hard-constraint violations remain below **5%** of selected turns.

### Why these criteria are justified

They directly test whether you solved the "no opportunity to express the trait" problem without buying performance by making conversations unnatural.

### Go / no-go

- **Go** if targeted cues make trait expression more separable without hurting continuity.
- **No-go** if all gains require obvious scripting or cause a trajectory tax.

---

## Phase 2. Hierarchical policy + best-of-styles search

### Implement

- Planner JSON schema.
- Tactic-slot candidate generator.
- Phase-conditioned reranker.
- Collapse diagnostics:
  - full_score vs contract_only selection overlap
  - diversity by slot
  - per-factor score attribution

### Run

A matched paired experiment with:

- Baseline
- Phase 1 system
- Phase 2 system

using the same personas and scenarios.

### Success criteria

1. **Mean MAE improves by at least 10% relative** to the frozen baseline on the matched set.
2. Full-score reranking beats `first` and `random` on the matched set.
3. `full_score` and `contract_only` choose different candidates in at least **20%** of pools.
4. Candidate diversity stays above **0.60** average pairwise dissimilarity.
5. Appropriateness / coherence do not degrade by more than **0.05**.

### Why these criteria are justified

This phase is supposed to prove that the new generator actually improves personality fidelity rather than merely stabilizing contract distance. The current collapse problem means criterion 3 is especially important.

### Go / no-go

- **Go** if this phase passes.
- **No-go** if the system is still basically a contract minimizer.

### Critical milestone

**This is the minimum phase you must pass before claiming the core research idea works.**

If Phase 2 fails, the thesis should be reframed from "fidelity-improving controller" to "stability / observability layer."

---

## Phase 3. Temporal memory layer

### Implement

- Memory backend interface.
- Working memory + commitment store.
- Graphiti adapter optional.
- Memory retrieval policy with channel separation.
- Delayed callback tests (references to earlier commitments and relationships).

### Run

Long-horizon sessions with:

- delayed reference,
- interrupted plan execution,
- social relationship reversal,
- memory-conflict probes.

### Success criteria

1. Prompt-to-line consistency improves at least **15%** over Phase 2.
2. Q&A consistency improves at least **15%**.
3. Commitment break rate decreases at least **30%**.
4. Long-horizon coherence does not materially degrade.

### Why these criteria are justified

This phase is specifically about long-horizon stability. If it does not improve continuity and follow-through, the memory system is not helping.

### Go / no-go

- **Go** if long-horizon stability improves.
- **No-go** if memory mainly increases verbosity, mirroring, or anchoring errors.

---

## Phase 4. Society-level calibration and simulation validity

### Implement

- Persona population generator with support coverage, not just average types.
- Aggregate calibration layer.
- Counterfactual scenario sweeps.
- Group-level metrics dashboard.

### Run

For each domain (marketing / negotiation / policy), test:

- multiple population mixes,
- pressure sweeps,
- role asymmetry sweeps,
- intervention counterfactuals.

### Success criteria

1. Aggregate outputs are monotonic and bounded under parameter changes.
2. Rare persona types materially change aggregate outcomes when theory says they should.
3. Repeated runs stay within a controlled variance band.
4. Population calibration outperforms naive averaging or uncalibrated aggregation.

### Why these criteria are justified

A commercialization-ready social simulator must be plausible both at the individual and society level. This follows recent social digital twin work emphasizing calibration and counterfactual validity.

### Go / no-go

- **Go** if agent-level fidelity translates into believable collective behavior.
- **No-go** if the system only looks good per-agent but produces unstable or implausible aggregate dynamics.

---

## Phase 5. Productization and commercialization hardening

### Implement

- multi-tenant auth and project boundaries
- rate limiting and queueing
- replay UI
- prompt / model / policy version registry
- budget controls
- exportable analytics reports
- safety filters and abuse monitoring
- manual override / stop button

### Success criteria

1. All sessions are reproducible and auditable.
2. Cost is attributable per session and per agent.
3. Failures are recoverable without corrupting memory state.
4. A customer can define personas, scenarios, and society structure without editing code.

### Why this phase matters

This is the difference between a research prototype and a sellable system.

---

## 8. What you should and should not build next

## Build next

1. **Scenario engine**
2. **Latent policy planner**
3. **Best-of-styles reranker**
4. **Replay + logging stack**

## Do not build next

1. Full SaaS product shell
2. Graphiti-first memory stack
3. Fine-tuning pipeline
4. Large population simulator before agent-level Phase 2 passes

---

## 9. Minimum checkpoints

## Minimum checkpoint for thesis viability

You must complete **Phase 2**.

That is the first point where you can honestly say whether the architecture improves stable personality expression under pressure.

## Minimum checkpoint for credible digital twin simulator

You must complete **Phase 4**.

That is the first point where you can claim the system supports actual social observation / counterfactual simulation, not just persona-conditioned chatting.

## Minimum checkpoint for commercialization

You must complete **Phase 5**.

---

## 10. Final recommendation

If I were making the call as system architect, I would commit to this path:

- Keep the project **API-only**.
- Stop treating contract distance as the main objective.
- Move the architecture toward **situation-conditioned persona policy**.
- Delay Graphiti until the policy architecture proves itself.
- Do not build the full simulator platform until Phase 2 passes.

### The single sentence version

> Build a **pressure-stable persona policy system**, not a smarter prompt stack.

That is the design most likely to improve your real success criterion and also gives you the cleanest bridge from thesis to production system.

---

## 11. References and thesis-use notes

### Internal project documents

1. **BCFC Final Research Plan (2026-03-04).** Internal project document.  
   Use for: your original thesis framing, API-only constraint, and BCFC motivation.

2. **Behavioral Fidelity Experiment Report (2026-03-04).** Internal project report.  
   Use for: baseline strength, judge fragility, and the fact that early BCFC worsened MAE.

3. **BCFC v3 mini / mini v2 analysis reports (2026-03-05).** Internal project reports.  
   Use for: best-of-N diagnostics, scorer collapse, and current stability-vs-fidelity tradeoff.

### External literature

4. **Abdulhai, M., Cheng, R., Clay, D., Althoff, T., Levine, S., Jaques, N. (2025). _Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning_. NeurIPS 2025.**  
   Use for: prompt-to-line, line-to-line, and Q&A consistency metrics.

5. **Li, R., Xia, H., Yuan, X., Dong, Q., Sha, L., Li, W., Sui, Z. (2025). _How Far are LLMs from Being Our Digital Twins? A Benchmark for Persona-Based Behavior Chain Simulation_. Findings of ACL 2025.**  
   Use for: continuous behavior simulation and behavior-chain fidelity.

6. **Du, B., Guo, M., He, S., Ye, Z., Zhu, X., et al. (2025). _TwinVoice: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation_. arXiv:2510.25536.**  
   Use for: capability decomposition into opinion consistency, memory recall, logical reasoning, lexical fidelity, persona tone, and syntactic style.

7. **Laban, P., Hayashi, H., Zhou, Y., Neville, J. (2025). _LLMs Get Lost in Multi-Turn Conversation_. arXiv:2505.06120.**  
   Use for: why long-horizon unreliability and commitment failures matter.

8. **Liu, Y., Wei, W., Liu, J., Mao, X., Fang, R., Chen, D. (2022). _Improving Personality Consistency in Conversation by Persona Extending_. CIKM 2022.**  
   Use for: out-of-predefined-persona failures and retrieval-based persona extension.

9. **Tasoula, P., Galanakis, M. (2023). _The Role of Trait Activation Theory in Occupational Behavior: A Systematic Review_. Psychology Research, 13(2), 83-87.**  
   Use for: trait-relevant situational cues and why scenarios must activate traits.

10. **Verga, P., Hofstatter, S., Althammer, S., Su, Y., Piktus, A., et al. (2024). _Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models_.**  
   Use for: heterogeneous judge panels instead of single-judge evaluation.

11. **Jung, J., Brahman, F., Choi, Y. (2024). _Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement_. arXiv:2407.18370.**  
   Use for: selective escalation and judge confidence control.

12. **Wang, P., Li, L., Chen, L., Cai, Z., Zhu, D., et al. (2023). _Large Language Models are not Fair Evaluators_.**  
   Use for: positional bias and the need for balanced order evaluation.

13. **Stureborg, R., Alikaniotis, D., Suhara, Y. (2024). _Large Language Models are Inconsistent and Biased Evaluators_. arXiv:2405.01724.**  
   Use for: familiarity bias, anchoring, and prompt sensitivity in LLM-as-a-judge.

14. **Grand, G., Tenenbaum, J. B., Mansinghka, V. K., Lew, A. K., Andreas, J. (2025). _Self-Steering Language Models_. COLM 2025.**  
   Use for: inference-time structured search beyond naive best-of-N.

15. **Rasmussen, P., Paliychuk, P., Beauvais, T., Ryan, J., Chalef, D. (2025). _Zep: A Temporal Knowledge Graph Architecture for Agent Memory_. arXiv:2501.13956.**  
   Use for: temporal graph memory, calibration against memory benchmarks, and motivation for graph-based agent memory.

16. **Paglieri, D., Cross, L., Cunningham, W. A., Leibo, J. Z., Vezhnevets, A. S. (2026). _Persona Generators: Generating Diverse Synthetic Personas at Scale_. arXiv:2602.03545.**  
   Use for: support coverage and long-tail persona generation.

17. **Gupta, A., Sheikh, F. R. (2026). _LLM-Powered Social Digital Twins: A Framework for Simulating Population Behavioral Response to Policy Interventions_. arXiv:2601.06111.**  
   Use for: population calibration layer, counterfactual validation, and aggregate plausibility.

18. **Jain, S., Park, C., Viana, M., Wilson, A., Calacci, D. (2026). _Interaction Context Often Increases Sycophancy in LLMs_. CHI 2026.**  
   Use for: why memory retrieval must be filtered to avoid over-mirroring.

### Graphiti documentation

19. **Graphiti Documentation. Zep Docs.**  
   Use for: implementation details, supported graph backends, episodes, search, and the facts-vs-summaries distinction.

20. **Graphiti GitHub README.**  
   Use for: open-source positioning, temporal graph capabilities, and OSS-vs-managed product distinction.

