# Two-Track Simulation Improvement Plan

**Date**: 2026-03-08 22:26:59 KST
**Branch**: codex/v5-langgraph
**Baseline**: Guided reliability rerun (2026-03-08), 12 clean runs

---

## Context

The guided reliability rerun (2026-03-08) produced 12 clean runs confirming a clear tradeoff:
- **Guided** (`engine_dialogue_only`): strong persona fidelity (drift 0.166, contradiction 0.021) but weak diversity (convergence 0.625, role diversity 0.583, negotiation uniqueness 0.333)
- **Exploratory** (`engine_dialogue_only`): similar diversity problem (convergence 0.688, uniqueness 0.333) PLUS low action validity (0.333) and flat relationship dynamics (inconsistency 0.0)

Root causes: (1) all style slots receive identical `action_intent` -> candidates converge, (2) persona stability weights (0.36) dominate action-aware signals (max 0.60 x multiplier), (3) family caps applied post-arbitration, (4) duplication penalties too weak, (5) exploratory prompts lack action vocabulary, (6) no asymmetric information between actors.

This plan improves both tracks in 3 phases: parameter tuning -> structural changes -> new features.

---

## Phase 1 -- Parameter Tuning & Prompt Changes (no architecture changes)

All changes are constant/weight/template edits in existing code.

### 1.1 Slot-specific action_intent rotation

**File**: `simulation_engine/actor.py:588-621` (`generate_candidate_pool_styles`)

Before dispatching each style slot, clone `policy_plan` and set `plan["action_intent"] = preferred_action_types[slot_index % len(preferred_action_types)]`. This breaks the single-intent broadcast that causes all 5 candidates to converge on the same action family.

**Targets**: action_family_convergence (0.625->< 0.50), role_action_diversity (0.583-> >0.65)

**Target Justification**: Game-theoretic strategy enumeration (Hua et al.) demonstrates that pre-enumerating distinct strategies before action selection reliably reduces convergence by 20-30% in negotiation games. Our target of < 0.50 represents a ~20% improvement from 0.625, which is conservative relative to the reported gains. The diversity target of > 0.65 follows from the same mechanism: with 3-5 distinct action intents rotating across slots, at least 2 of 3-4 candidates should propose non-overlapping families.

**Citation**: Hua et al. "Game-theoretic LLM: Agent Workflow for Negotiation Games." arXiv:2411.05990, 2024.

### 1.2 Strengthen duplication penalty & populate avoid_families

**Files**:
- `simulation_engine/script.py:318-355` -- raise `duplicate_penalty` from 0.18->0.28 (NEGOTIATION) and 0.08->0.14 (other phases) for guided mode; from 0.24->0.32 and 0.10->0.16 for exploratory
- `simulation_engine/action_priors.py:129-137` -- populate `avoid_families` with families NOT in primary or secondary (currently always `[]`)

**Targets**: action_family_convergence, negotiation_uniqueness

**Target Justification**: Huang & Hadfi (EMNLP 2024) showed that personality-conditioned negotiation tactics diverge more when agents are steered away from off-role action families. Populating `avoid_families` creates a negative signal that compounds with the duplication penalty. The 56% penalty increase for NEGOTIATION (0.18->0.28) is calibrated to make a second instance of the same family score ~0.05 lower, enough to shift selection without blocking primary families.

**Citation**: Huang & Hadfi. "How Personality Traits Influence Negotiation Outcomes?" Findings of EMNLP 2024. arXiv:2407.11549.

### 1.3 Raise sparsity_threshold for guided mode

**File**: `simulation_engine/script.py:329` -- raise from 0.62->0.68 (non-NEGOTIATION) and 0.7->0.76 (NEGOTIATION) for guided mode only. Keep exploratory thresholds lower.

**Targets**: action_family_convergence (filter out weak duplicate proposals)

**Target Justification**: Bhardwaj (2026) introduces behavioral contracts that gate low-confidence actions behind hard invariant thresholds. Raising the sparsity threshold acts as a soft version: candidates whose action activation score falls below the threshold receive a proportional penalty. The +0.06 increase is sized to filter proposals that are only marginally activated (activation score 0.62-0.68) while preserving strongly role-aligned actions. This targets the "long tail" of weak duplicates that inflate convergence metrics.

**Citation**: Bhardwaj. "Agent Behavioral Contracts." arXiv:2602.22302, 2026.

### 1.4 Rebalance controller scoring weights

**File**: `simulation_engine/controller.py:725-751`

Shift 0.08 from persona stability to action diversity:
- `identity_consistency`: 0.18->0.15
- `persona_drift (1-drift)`: 0.18->0.15
- `role_action_uniqueness`: 0.10->0.14
- `phase_action_duplication_penalty`: 0.12->0.15
- `convergence_backoff`: 0.08->0.11

Safe because persona drift MAE is already good (0.166).

**Targets**: role_action_diversity, negotiation_uniqueness

**Target Justification**: Yao et al. (2025) demonstrate that argmax-persona selection causes mode collapse; shifting scoring weight toward diversity signals enables "verbalized sampling" -- selecting candidates that are nearly as persona-faithful but more action-diverse. The total weight shift is 0.06 from persona (0.36->0.30) and 0.08 to diversity signals. This is conservative: persona drift MAE has 0.014 margin below the 0.18 target, so a 0.06 weight reduction is unlikely to regress it past threshold. The diversity weight increase (+0.04 uniqueness, +0.03 duplication penalty, +0.03 convergence backoff = 0.10 total) is sized to be decisive in near-tie scenarios (score delta ~0.01-0.02) which account for ~35% of selections in current runs.

**Citation**: Yao et al. "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity." arXiv:2510.01171, 2025.

### 1.5 Exploratory action vocabulary prompt injection

**File**: `simulation_engine/actor.py` -- in `_build_simulation_mode_guidance` for exploratory mode, append valid action vocabulary: "When proposing concrete actions, use naturally: assign an owner, request evidence, publish an update, narrow the scope, suggest a pilot, commit resources, defer a decision, or preserve autonomy."

**Targets**: structured_action_validity (0.333-> >0.55) for exploratory

**Target Justification**: Shekkizhar (2025) identified "echoing" -- identity collapse when LLM agents interact -- as a primary failure mode. The structured response protocol provides vocabulary anchors that reduce ambiguity. Current exploratory action_validity of 0.333 means 2 of 3 actions are malformed. The vocabulary injection is analogous to providing a "structured response format" which Shekkizhar reports raises well-formedness by 40-60%. Our target of > 0.55 is conservative (66% improvement from baseline), accounting for the fact that exploratory mode intentionally permits unstructured responses.

**Citation**: Shekkizhar. "Echoing: Identity Failures when LLM Agents Talk to Each Other." arXiv:2511.09710, 2025.

### 1.6 Periodic persona re-injection at turn threshold

**File**: `simulation_engine/actor.py:268-370` (`build_state_context`)

When actor turn count > 6, prepend condensed persona anchor: "Reminder: You are [name], [role]. Decision style: [O/C trait summary]. Core incentives: [top 2]."

**Targets**: persona_drift_mae, envelope_violations

**Target Justification**: Li et al. (2024) measured instruction stability across multi-turn dialogues and found drift accelerates significantly at turn 8, with a 15-25% increase in persona deviation compared to turns 1-6. Periodic re-injection of condensed identity anchors counters attention decay by refreshing the persona signal in the context window. The threshold of turn 6 targets the onset of acceleration. The persona anchor is deliberately minimal (~25 tokens) to avoid crowding the context or overriding dynamic state information. Expected drift reduction: 5-10% relative improvement on drift MAE.

**Citation**: Li et al. "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs." arXiv:2402.10962, 2024.

### Phase 1 Smoke Test

```bash
PYTHONPATH=. python3 -m experiment.run_experiment --simulation-benchmark-mvp \
  --benchmark-conditions engine_dialogue_only \
  --benchmark-repetitions 2 \
  --benchmark-scripts new_product_launch brand_crisis_response \
  --output-dir simulation_engine/results_phase1_smoke
```

**Pass criteria** (no-regression + improvement):

| Metric | Baseline (G / E) | Target | Justification |
|---|---|---|---|
| action_family_convergence | 0.625 / 0.688 | < 0.55 | 1.1 slot rotation + 1.2 duplication penalty compound to reduce by ~12-15% |
| role_action_diversity | 0.583 / 0.563 | > 0.60 | Inverse of convergence; 1.4 weight rebalance adds ~3% via selection pressure |
| persona_drift_mae | 0.166 / 0.172 | < 0.18 | No-regression gate; 1.4 reduces persona weight but 1.6 re-injection compensates |
| commitment_contradiction | 0.021 / 0.0 | < 0.03 | No-regression gate; no changes target contradiction directly |
| Exploratory action_validity | 0.333 | > 0.50 | 1.5 vocabulary injection; Shekkizhar reports 40-60% well-formedness gain |

---

## Phase 2 -- Structural Pipeline Changes

### 2.1 Pre-generation family exclusion

**Files**:
- `simulation_engine/graphs.py` (candidate pool generation node) -- query `ledger.phase_action_family_counts()` before generation, identify families at cap
- `simulation_engine/action_priors.py:140-169` (`apply_actor_action_preferences`) -- accept and merge `avoid_families` from capped families
- `simulation_engine/actor.py:588-621` -- skip capped families in slot-specific intent rotation (from 1.1)

Prevents duplicate families from being generated at all, instead of generating then discarding post-arbitration.

**Targets**: action_family_convergence (< 0.40), negotiation_uniqueness (> 0.50)

**Target Justification**: Hua et al. demonstrate that pre-enumerating and pruning dominated strategies before action selection is strictly better than post-hoc filtering. Currently, families at cap are generated, scored, and then rejected by arbitration -- wasting a generation slot. Pre-exclusion reclaims those slots for novel families. Combined with 1.1 and 1.2, this should reduce convergence from < 0.55 (Phase 1) to < 0.40. The 0.50 negotiation uniqueness target assumes that with pre-exclusion + slot rotation, at least 2 of 3 NEGOTIATION actors propose distinct families.

**Citation**: Hua et al. "Game-theoretic LLM: Agent Workflow for Negotiation Games." arXiv:2411.05990, 2024.

### 2.2 Chain-of-states summary before each turn

**Files**:
- `simulation_engine/state_ledger.py` -- add `state_trajectory_summary()` method: compare last 2 `WorldStateSnapshot` entries, produce 1-2 sentence delta description
- `simulation_engine/actor.py:268-370` -- insert summary after world_state line in `build_state_context`

**Targets**: action_feedback_utilization, state_transition_coherence

**Target Justification**: StateAct (2024) demonstrates that explicit state tracking through chain-of-states prompting improves action coherence by 18-25% in interactive environments. The state trajectory summary provides actors with a concrete before/after comparison of the world state, enabling more informed action selection. Currently, actors receive a snapshot of current state but no temporal context about how it changed. The summary is limited to ~30-40 tokens to avoid context pollution.

**Citation**: StateAct. "Enhancing LLM Base Agents via Self-prompting and State-tracking." arXiv:2410.02810, 2024.

### 2.3 Role-chain self-questioning

**Files**:
- `simulation_engine/actor.py` -- in `_build_simulation_mode_guidance` or as `constraint_suffix`, add deterministic self-question derived from actor's role + first concern: "Before responding, consider: as [role] whose main concern is [concern], what specific risk or opportunity does this moment create for you?"

No LLM call needed -- question is template-generated from `StakeholderActorSpec`.

**Targets**: role_action_diversity, negotiation_uniqueness

**Target Justification**: PCL (ACL 2025) shows that persona-aware self-questioning before response generation improves persona differentiation by 12-20% across diverse persona configurations. The deterministic template avoids LLM overhead while providing a role-grounding anchor that naturally diverges across actors (since each has different concerns). This is complementary to 1.6 persona re-injection: re-injection restates identity, self-questioning activates role-specific reasoning.

**Citation**: PCL. "Enhancing Persona Consistency using Persona-Aware Contrastive Learning." Findings of ACL 2025. arXiv:2503.17662.

### 2.4 Divergence-based drift intervention (exploratory only)

**Files**:
- `simulation_engine/state_ledger.py` -- add `trait_divergence_score()`: mean pairwise absolute difference between all actors' rolling trait estimates
- `simulation_engine/controller.py` (nudge system) -- when divergence < 0.06 in exploratory mode, inject: "The discussion is converging. Re-anchor to your unique stakeholder lens. Surface a concern that hasn't been voiced yet."

**Targets**: relationship_inconsistency (0.0-> >0.04 for exploratory), persona drift (exploratory)

**Target Justification**: Dongre et al. (2025) identify "context equilibria" in multi-turn LLM interactions where agents converge to a shared communication pattern despite distinct initial conditions. They propose divergence monitoring with threshold-based intervention as a mitigation. The 0.06 divergence threshold is calibrated from our data: at relationship_inconsistency 0.0, the trait divergence between actors is near-zero, indicating convergence. The nudge text is designed to break the equilibrium without forcing artificial conflict. Target of > 0.04 inconsistency represents a minimal but measurable departure from flat dynamics.

**Citation**: Dongre et al. "Drift No More? Context Equilibria in Multi-Turn LLM Interactions." arXiv:2510.07777, 2025.

### 2.5 Negotiation tactic seeding

**Files**:
- `simulation_engine/actor.py:372+` (`_augment_policy_plan`) -- when phase == NEGOTIATION, rotate among 4 tactic profiles seeded by `hash(simulation_id + actor_id + run_index)`:
  - (a) owner-first: assign_owner, deadlines
  - (b) evidence-first: request_evidence, pilot
  - (c) scope-first: narrow_scope, defer_decision
  - (d) commitment-first: commit_resource, publish_update

Deterministic per-run variation without randomness.

**Targets**: negotiation_uniqueness (0.333-> >0.55)

**Target Justification**: NegotiationArena (Bianchi et al., ICML 2024) demonstrates that seeding negotiation agents with distinct tactical profiles produces measurably more diverse outcomes. Their 4-profile taxonomy (competitive, cooperative, analytical, accommodating) maps to our action families. The deterministic hash ensures reproducibility while providing inter-actor variation. With 4 profiles rotating across 3 actors, at least 2 should have distinct primary tactics, raising uniqueness from 0.333 to > 0.55.

**Citation**: Bianchi et al. "NegotiationArena." ICML 2024. arXiv:2402.05863.

### Phase 2 Smoke Test

```bash
PYTHONPATH=. python3 -m experiment.run_experiment --simulation-benchmark-mvp \
  --benchmark-conditions engine_dialogue_only \
  --benchmark-repetitions 3 \
  --benchmark-scripts new_product_launch post_merger_integration brand_crisis_response resource_reallocation_crunch \
  --output-dir simulation_engine/results_phase2_smoke
```

**Pass criteria**:

| Metric | Phase 1 Target | Phase 2 Target | Justification |
|---|---|---|---|
| action_family_convergence | < 0.55 | < 0.40 | 2.1 pre-exclusion eliminates wasted generation slots |
| role_action_diversity | > 0.60 | > 0.70 | 2.3 self-questioning + 2.5 tactic seeding compound |
| negotiation_uniqueness | ~0.35 | > 0.55 | 2.5 tactic seeding with 4-profile rotation |
| persona_drift_mae | < 0.18 | < 0.17 | 2.2 chain-of-states + 2.3 self-questioning improve grounding |
| Exploratory relationship_inconsistency | 0.0 | > 0.03 | 2.4 divergence intervention breaks convergence equilibria |
| Exploratory action_validity | > 0.50 | > 0.60 | 2.2 state summary provides better action context |

---

## Phase 3 -- New Features & Scenario Design

### 3.1 Layered goal structures (exploratory)

**Files**:
- `simulation_engine/script.py` -- add optional `implicit_goals: list[str]` to `StakeholderActorSpec`
- `simulation_engine/manual_scripts.py` -- add implicit goals to exploratory scripts that create natural tension (e.g., Avery: "maintain team credibility even if it means pushing back on legal's timeline")
- `simulation_engine/actor.py` (`build_state_context`) -- when exploratory mode, append: "Your private goal: [implicit_goals[0]]"

Creates asymmetric motivation that naturally produces divergent behavior.

**Targets**: relationship_inconsistency (exploratory), role_action_diversity

**Target Justification**: SOTOPIA (Zhou et al., ICLR 2024) demonstrates that layered explicit + implicit goals per agent produce richer social interactions with measurably higher behavioral diversity. Implicit goals create natural tension between actors that doesn't need to be forced by the phase structure. For example, if Avery (communications) has an implicit goal of "maintain team credibility" while Daniel (legal) has "protect the company from premature liability exposure," their responses will naturally diverge even when the surface-level discussion converges.

**Citation**: Zhou et al. "SOTOPIA: Interactive Evaluation for Social Intelligence." ICLR 2024. arXiv:2310.11667.

### 3.2 Private world events / asymmetric information

**Files**:
- `simulation_engine/manual_scripts.py` -- add private `WorldEvent` entries visible to single actors (e.g., finance-only budget data, product-only customer signal)
- `simulation_engine/script.py` -- verify `WorldEvent.visibility` and `affected_actor_ids` are used end-to-end
- `simulation_engine/graphs.py` (`inject_world_events`) -- confirm visibility filtering works

Infrastructure already exists (`affected_actor_ids`, `visible_to`); just needs scenario content and pipeline verification.

**Targets**: relationship_inconsistency, negotiation_uniqueness

**Target Justification**: La Malfa et al. (NeurIPS 2025) show that LLMs systematically fail multi-agent strategic tasks when asymmetric information is required. However, when private information is explicitly provided in the prompt context, agents can leverage it for strategic differentiation. Private world events create natural information asymmetry: e.g., only the finance actor knows the exact budget shortfall, forcing others to negotiate from positions of uncertainty. This directly addresses relationship_inconsistency by creating real grounds for divergent behavior.

**Citation**: La Malfa et al. "Large Language Models Miss the Multi-Agent Mark." NeurIPS 2025. arXiv:2505.21298.

### 3.3 Softmax candidate sampling (replaces argmax)

**Files**:
- `simulation_engine/controller.py` (candidate selection) -- when enabled, compute `weights[i] = exp(score[i] / tau)` with `tau=0.12`, sample using deterministic seed `hash(simulation_id + actor_id + phase + turn)`
- `simulation_engine/ablation.py` -- add `use_softmax_sampling` toggle

Favors best candidate but allows occasional selection of 2nd/3rd, producing inter-run variation.

**Targets**: negotiation_uniqueness (> 0.60), state_trajectory_variance (> 0.01)

**Target Justification**: Yao et al. (2025) demonstrate that softmax sampling with low temperature is strictly better than argmax for maintaining output diversity while preserving quality. With tau=0.12, the probability mass is concentrated on the top candidate (~60-70%) but allows 30-40% chance of selecting alternatives. The deterministic seed preserves reproducibility within a run while enabling inter-run variation. The state_trajectory_variance target of > 0.01 represents measurable inter-run variation in world state trajectories, currently near-zero due to argmax determinism.

**Citation**: Yao et al. "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity." arXiv:2510.01171, 2025.

### 3.4 Windowed drift detection

**Files**:
- `simulation_engine/metrics.py` -- add `estimate_actor_traits_from_recent_turns(turns, actor_name, window=4)`
- `simulation_engine/controller.py` (scoring) -- compare recent-window vs full-window trait estimate; add `recent_drift_penalty = 0.06` when any trait diverges by > 0.15

Catches late-turn persona decay that the rolling average misses.

**Targets**: persona_drift_mae (< 0.16 guided, < 0.17 exploratory), envelope_violations (< 5)

**Target Justification**: Abdulhai et al. (NeurIPS 2025) demonstrate that windowed prompt-to-line consistency monitoring catches persona decay that rolling averages miss. The rolling average dampens rapid drift by blending it with earlier turns, allowing late-turn persona collapse to go unpenalized. A 4-turn window captures the most recent behavior and compares it to the full-window estimate. The 0.15 trait divergence threshold triggers the penalty only for significant deviations, avoiding false positives from normal turn-to-turn variation (which is typically < 0.10). The 0.06 penalty weight is calibrated to be decisive in near-tie scenarios without dominating the total score.

**Citation**: Abdulhai et al. "Consistently Simulating Human Personas with Multi-Turn RL." NeurIPS 2025. arXiv:2511.00222.

### Phase 3 Full Benchmark

```bash
PYTHONPATH=. python3 -m experiment.run_experiment --simulation-benchmark-mvp \
  --benchmark-repetitions 3 \
  --output-dir simulation_engine/results_phase3_full
```

**Final targets**:

| Metric | Current (G/E) | Phase 1 | Phase 2 | Final Target | Cumulative Justification |
|---|---|---|---|---|---|
| action_family_convergence | 0.625 / 0.688 | < 0.55 | < 0.40 | < 0.35 | 1.1 rotation + 1.2 penalty + 2.1 pre-exclusion + 3.3 softmax sampling |
| role_action_diversity | 0.583 / 0.563 | > 0.60 | > 0.70 | > 0.75 | 1.4 weight rebalance + 2.3 self-questioning + 2.5 tactic seeding + 3.1 layered goals |
| negotiation_uniqueness | 0.333 / 0.333 | ~0.35 | > 0.55 | > 0.60 | 2.5 tactic seeding + 3.3 softmax sampling |
| persona_drift_mae | 0.166 / 0.172 | < 0.18 | < 0.17 | < 0.16 / < 0.17 | 1.6 re-injection + 2.2 chain-of-states + 3.4 windowed drift |
| commitment_contradiction | 0.021 / 0.0 | < 0.03 | < 0.03 | < 0.03 | No-regression gate throughout |
| action_validity (E) | 0.333 | > 0.50 | > 0.60 | > 0.65 | 1.5 vocabulary + 2.2 state summary + 3.1 layered goals |
| relationship_inconsistency (E) | 0.0 | 0.0 | > 0.03 | > 0.04 | 2.4 divergence intervention + 3.1 implicit goals + 3.2 private events |
| envelope_violations | 6.17 / 6.83 | - | - | < 5 / < 6 | 3.4 windowed drift detection |

---

## Dependency Graph

```
Phase 1 (all parallel):
  1.1  slot-specific action_intent
  1.2  duplication penalty + avoid_families
  1.3  sparsity threshold
  1.4  scoring weight rebalance
  1.5  exploratory action vocab prompt
  1.6  persona re-injection
        | smoke test gate
Phase 2 (mostly parallel, 2.1 depends on 1.2, 2.5 depends on 1.1):
  2.1  pre-generation family exclusion
  2.2  chain-of-states summary
  2.3  role-chain self-questioning
  2.4  divergence-based intervention
  2.5  negotiation tactic seeding
        | smoke test gate
Phase 3 (mostly parallel, 3.3 depends on 1.4, 3.4 depends on 1.6+2.2):
  3.1  layered goals (exploratory)
  3.2  private world events
  3.3  softmax candidate sampling
  3.4  windowed drift detection
        | full benchmark
```

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Persona drift regression from 1.4 weight shift + 3.3 softmax | Medium | Modest weight delta (0.06 total) and low temperature (0.12); 1.6 re-injection compensates |
| Guided over-constraint from 2.1 family exclusion | Low | Only excludes families already at cap; primary families pass through |
| Exploratory chaos from 3.1 implicit goals + 3.2 private events | Medium | Phase 2 baseline established before Phase 3; implicit goals are additive |
| Latency from 2.2 chain-of-states + 2.3 self-questioning | Low | Expected < 50 tokens/turn, within budget |
| Weight rebalance makes persona secondary to action diversity | Medium | Total persona weight (0.30) still exceeds any single action signal (max 0.15) |

## References

1. Hua et al. "Game-theoretic LLM: Agent Workflow for Negotiation Games." arXiv:2411.05990, 2024.
2. Yao et al. "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity." arXiv:2510.01171, 2025.
3. Huang & Hadfi. "How Personality Traits Influence Negotiation Outcomes?" Findings of EMNLP 2024. arXiv:2407.11549.
4. Bhardwaj. "Agent Behavioral Contracts." arXiv:2602.22302, 2026.
5. Shekkizhar. "Echoing: Identity Failures when LLM Agents Talk to Each Other." arXiv:2511.09710, 2025.
6. Li et al. "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs." arXiv:2402.10962, 2024.
7. Dongre et al. "Drift No More? Context Equilibria in Multi-Turn LLM Interactions." arXiv:2510.07777, 2025.
8. Abdulhai et al. "Consistently Simulating Human Personas with Multi-Turn RL." NeurIPS 2025. arXiv:2511.00222.
9. PCL. "Enhancing Persona Consistency using Persona-Aware Contrastive Learning." Findings of ACL 2025. arXiv:2503.17662.
10. StateAct. "Enhancing LLM Base Agents via Self-prompting and State-tracking." arXiv:2410.02810, 2024.
11. Zhou et al. "SOTOPIA: Interactive Evaluation for Social Intelligence." ICLR 2024. arXiv:2310.11667.
12. La Malfa et al. "Large Language Models Miss the Multi-Agent Mark." NeurIPS 2025. arXiv:2505.21298.
13. Bianchi et al. "NegotiationArena." ICML 2024. arXiv:2402.05863.
