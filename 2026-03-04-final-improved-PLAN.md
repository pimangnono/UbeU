# Final Research Plan: Behavior Contract Fidelity Control (BCFC) for Digital Twin Personality Simulation

**Date:** 2026-03-04
**Status:** Ready for implementation

---

## 1. Research Objective

**Thesis statement:**

> We propose Behavior Contract Fidelity Control (BCFC), a closed-loop method for maintaining personality-faithful LLM agents in digital twin social simulations using only API access — no fine-tuning required. We validate BCFC through a within-subject experiment showing that closed-loop behavioral correction significantly improves trait simulation fidelity, particularly for traits that static prompting alone fails to produce (Conscientiousness, Openness).

**Why this matters:** Current LLM personality simulation research stops at measurement — "can the model follow instructions?" That is necessary but insufficient for digital twin deployment. Practitioners need a *method* that reliably produces personality-faithful behavior under adversarial conversational pressure, with known cost and reliability guarantees. BCFC provides this.

---

## 2. My Honest Assessment of the Codex Plan

Codex proposed BCFC with 3 conditions (Baseline / Compiler-only / Full BCFC). I agree with the core concept but have 5 specific improvements:

### What I changed and why:

| Codex proposal | My improvement | Justification |
|---|---|---|
| **3 conditions** (Baseline, Compiler-only, Full BCFC) | **2 conditions** (Baseline vs BCFC) + analytical ablation | 3 conditions triples cost. A within-subject paired design is more powerful at lower N. Ablation can be done analytically by logging controller interventions. |
| **Repair Gate rewrites turns post-emission** | **Generate-Check-Regenerate pre-emission** | A post-emission rewrite breaks conversational coherence — NPCs already responded to the original. Pre-emission check is cleaner: generate → check against contract → regenerate if needed (max 2 retries). |
| **LLM-based Persona Compiler** | **Deterministic compiler from rule-based weights** | We already have feature-trait weight mappings in `rule_based_evaluator.py`. Inverting these to produce target ranges is cheaper, reproducible, and avoids circular LLM dependency. |
| **Full feature extraction every turn** | **Incremental lightweight check every 2 turns** | Current `extract_features()` operates on full transcript. Running it every turn is wasteful. A lightweight incremental check on recent turns (last 2-4) is sufficient for drift detection. Full extraction still runs post-session for evaluation. |
| **Dev/test split with held-out scenarios** | **Within-subject: same profile-scenario pairs under both conditions** | Paired comparison is statistically more powerful. Each profile-scenario unit serves as its own control. Generalization is tested via the 13×4 diversity of profiles and scenarios, not via held-out splits. |

### What I kept from Codex:
- The BCFC concept itself — framing personality simulation as a control problem
- Behavior contracts with target feature ranges and action policies
- Runtime corrective prompt injection
- The "digital twin deployment recipe" framing
- Cost/reliability analysis as a first-class research outcome

---

## 3. BCFC Architecture (3 Modules)

### Module 1: Persona Compiler (offline, deterministic)

**Input:** OCEAN vector (e.g., {O:0.6, C:0.8, E:0.9, A:0.4, N:0.2})
**Output:** Behavior Contract

The compiler inverts the rule-based evaluator weights to produce:

```
BehaviorContract:
  target_features:        # Feature target ranges derived from OCEAN vector
    planning_count:       [5, 8]     # High C → more planning
    structure_markers:    [3, 6]     # High C → structured discussion
    idea_count:           [3, 5]     # High O → more ideas
    hedge_count:          [0, 1]     # Low N → fewer hedges
    disagreement_count:   [2, 4]     # Low A → more disagreements
    ...
  action_policies:        # Per-turn behavioral mandates
    C_actions: ["set milestone", "assign owner", "recap decision", ...]
    O_actions: ["propose alternative", "draw analogy", "ask what-if", ...]
  hard_constraints:       # Never-violate rules
    - "Never agree without first stating a concern" (Low A)
    - "Always reference at least one prior commitment" (High C)
  pressure_rule: "If challenged, first acknowledge, then execute trait action"
  continuity_rule: "Reference at least one open item from prior turns"
```

**Implementation:** `experiment/persona_compiler.py` — deterministic function, no API calls.

### Module 2: Fidelity Controller (online, every 2 candidate turns)

After every 2nd candidate turn:
1. Run incremental feature extraction on recent turns (lightweight)
2. Compare features against behavior contract targets
3. Compute deviation vector (which traits are drifting?)
4. Generate a corrective nudge appended to the system prompt

**Example corrective nudge:**
```
[FIDELITY NOTE: Your planning specificity is below target. In your next response,
include at least one concrete action item with an owner. Your disagreement rate is
also low — take a clear opposing position on the current proposal.]
```

**Implementation:** Integrated into `_run_session_loop()` in `batch_runner.py`. The nudge is injected into `candidate.system_prompt` before the next generation call.

**Cost:** Zero additional API calls. The nudge is just text appended to the existing system prompt. Feature extraction is deterministic.

### Module 3: Generate-Check-Regenerate (online, per candidate turn)

Before a candidate turn enters the conversation:
1. Generate candidate response (normal flow)
2. Quick check: does this response violate any hard constraints?
   - E.g., High-C agent produced zero planning markers
   - E.g., Low-A agent agreed without pushback when challenged
3. If violation detected: regenerate with strengthened constraint (max 2 retries)
4. Log: `{turn, original_text, violation_type, retry_count, final_text}`

**Cost:** ~10-20% more generation calls (only triggers on violations). Based on pilot data, C and O violations would trigger most often.

---

## 4. Experimental Design

### Conditions (within-subject, paired)

| Condition | Description | N sessions |
|-----------|-------------|------------|
| **Baseline** | V5.1 static prompting (already have pilot data) | 76 |
| **BCFC** | Persona Compiler + Fidelity Controller + Generate-Check | 76 |

Each of the 76 sessions is a unique profile-scenario-rep combination run under BOTH conditions. This enables paired statistical comparison.

### Session Matrix

```
Main:       13 profiles × 4 scenarios × 1 rep = 52 per condition
Baseline_A:  1 none     × 4 scenarios × 1 rep =  4 per condition (BCFC has no contract → identical)
Baseline_B:  2 shuffled × 4 scenarios × 1 rep =  8 per condition
                                          Total: 64 unique per condition
                                          Grand: 128 sessions (64 Baseline + 64 BCFC)
```

Baselines A run only once (no BCFC intervention since there's no personality target). Baseline B runs under both to test whether BCFC can also improve shuffled-vector fidelity.

### Research Questions & Hypotheses

| RQ | Hypothesis | Test | Success criterion |
|----|-----------|------|-------------------|
| **RQ1** | BCFC improves overall fidelity | Paired t-test on MAE(baseline) vs MAE(bcfc) | p < 0.05, mean MAE reduction > 0.05 |
| **RQ2** | BCFC specifically improves C and O | Per-trait paired comparison | C: r > 0.5 (up from 0.25), O: r > 0.75 (up from 0.69) |
| **RQ3** | BCFC reduces trait drift over turns | Compare early/late window correlation delta | Smaller delta under BCFC |
| **RQ4** | BCFC reduces inter-session variance | Compare within-profile SD | Lower SD under BCFC |
| **RQ5** | BCFC cost overhead is practical | Measure total cost and latency | < 1.5x baseline cost per session |

### Ablation (analytical, no extra sessions)

Every controller intervention is logged:
- `{turn, trait, deviation, nudge_text, pre_features, post_features}`
- `{turn, violation_type, retry_count, original_text, final_text}`

This enables post-hoc analysis of:
- Which traits needed most correction? (expected: C, O)
- Did corrections actually improve subsequent behavior?
- How often did regeneration trigger? (cost analysis)
- Did nudges help or cause unnatural behavior?

---

## 5. Implementation Plan

### Files to create (3 new):

| File | Purpose |
|------|---------|
| `experiment/persona_compiler.py` | BehaviorContract generation from OCEAN vector |
| `experiment/fidelity_controller.py` | Runtime deviation check + nudge generation |
| `experiment/incremental_features.py` | Lightweight per-turn feature extraction |

### Files to modify (3 existing):

| File | Change |
|------|--------|
| `experiment/batch_runner.py` | Add `condition` parameter, BCFC session loop variant, controller logging |
| `experiment/candidate_agent.py` | Accept dynamic system prompt updates (nudge injection) |
| `experiment/run_experiment.py` | Add `--bcfc` flag, paired experiment orchestration |

### Files unchanged but used:

| File | Role |
|------|------|
| `experiment/profiles.py` | Same 13 profiles, same prompts (baseline) |
| `evaluation/trait_evaluator.py` | Same dual-order ensemble evaluation |
| `evaluation/rule_based_evaluator.py` | Provides weight inversion for Persona Compiler |
| `experiment/analysis.py` | Extended with paired comparison analysis |

---

## 6. Cost & Time Estimates

### Per-session cost breakdown:

| Component | Baseline | BCFC | Delta |
|-----------|----------|------|-------|
| Generation (17 turns) | $0.03 | $0.035 | +$0.005 (regeneration) |
| Evaluation (50 calls) | $0.14 | $0.14 | $0 (identical) |
| Controller | $0 | $0 | $0 (deterministic) |
| **Total/session** | **$0.17** | **$0.175** | **+3%** |

### Full experiment:

| Item | Count | Cost | Time |
|------|-------|------|------|
| Baseline sessions | 64 | ~$11 | ~3.7 hrs |
| BCFC sessions | 64 | ~$11.5 | ~4 hrs |
| Baseline_A (shared) | 4 | ~$0.7 | ~14 min |
| **Total** | **132** | **~$23** | **~8 hrs** |

**Conservative estimate with retries/overhead: $28-32, 9-10 hours**

This is UNDER the $30-35 budget and well within a single day of serial execution.

### Comparison to Codex's 3-condition estimate:

| Design | Sessions | Cost | Statistical power |
|--------|----------|------|-------------------|
| Codex (3 conditions) | 192+ | $45-60 | Split across 3 groups |
| Mine (2 conditions, paired) | 132 | $28-32 | Paired = more powerful |

---

## 7. Execution Timeline

| Day | Task | Hours | Output |
|-----|------|-------|--------|
| **Day 1** | Implement Persona Compiler + Fidelity Controller + incremental features | 4-6 | 3 new modules, unit tested |
| **Day 1** | Modify batch_runner + candidate_agent for BCFC loop | 2-3 | BCFC session flow working |
| **Day 2 AM** | Run baseline experiment (64 sessions) | 4 | Baseline results |
| **Day 2 PM** | Run BCFC experiment (64 sessions) | 4 | BCFC results |
| **Day 3 AM** | Run analysis: paired comparison + ablation | 2 | Analysis report |
| **Day 3 PM** | Review results, write findings | 3 | Publishable tables + figures |

---

## 8. Expected Outcomes

### Optimistic scenario (BCFC works well):
- C fidelity: r > 0.6 (up from 0.25) — "BCFC rescues a failed trait"
- O fidelity: r > 0.8, bias < 0.05 (up from 0.69, bias -0.18)
- E/A/N maintained or improved
- Clear ablation: controller interventions correlate with improved behavior
- **Story:** "Static prompting isn't enough. Closed-loop control makes LLM personality simulation reliable."

### Realistic scenario (partial improvement):
- C fidelity: r ~ 0.45-0.55 (meaningful improvement but still weak)
- O calibration improved, bias < 0.10
- Controller helps but doesn't fully solve C
- **Story:** "BCFC significantly improves fidelity. C remains the hardest trait — here's what that means for digital twin design (structural elicitation, task design, potentially fine-tuning)."

### Pessimistic scenario (BCFC doesn't help much):
- C/O unchanged despite intervention
- Controller triggers but corrections don't stick
- **Story:** "The fundamental limit isn't prompting — it's RLHF alignment. Here's the evidence, and here's why fine-tuning or structural approaches are necessary for digital twin C/O simulation."

**All three scenarios produce publishable, valuable findings.** This is a strength of the interventionist design — you learn something useful regardless of outcome.

---

## 9. Digital Twin Deployment Recipe (the practical contribution)

The paper delivers a concrete recipe for practitioners:

### For traits that work with static prompting (E, A, N):
1. Use personality profile prompts with behavioral instructions
2. Validate with ensemble evaluation + rule-based cross-check
3. Deploy with confidence intervals from your validation data

### For traits that need closed-loop control (C, O):
1. Compile OCEAN vector into a Behavior Contract
2. Run Fidelity Controller with per-turn deviation monitoring
3. Use Generate-Check-Regenerate for hard constraint enforcement
4. Monitor controller intervention rate as a reliability metric
5. Set deployment readiness threshold: intervention rate < X%

### For traits that resist API-only approaches:
1. Document the behavioral floor from your experiments
2. Recommend task/scenario design that naturally elicits the trait
3. If fidelity threshold is not met, recommend fine-tuning with DPO/RL on trait-expression rewards

This tiered recommendation is the practical value-add that makes the paper useful beyond academia.

---

## 10. What Makes This Publishable

| Criterion | How we meet it |
|-----------|----------------|
| **Novel method** | BCFC: first closed-loop personality fidelity control for LLM agents |
| **Causal evidence** | Within-subject paired comparison, not just correlational |
| **Practical value** | Deployment recipe with cost/reliability guarantees |
| **Rigor** | 5-model ensemble, dual-order bias control, rule-based cross-validation, bootstrap CIs |
| **Honest limitations** | Pre-registered expectations per trait, all outcomes informative |
| **Reproducibility** | Deterministic compiler, logged interventions, open pipeline |
