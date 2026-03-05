# 2026‑03‑05 Revised Plan (v1.1) — Failure‑Driven BCFC With Staged Execution

**Summary**
This plan revises BCFC to directly address v0 failure modes, adds reviewer‑critical controls, and formalizes a 3‑stage execution path (freeze pilot → mid‑check → full run). It integrates all 7 upgrades, fixes remaining gaps, and keeps the primary endpoint consistent with v0 while adding robustness and trajectory diagnostics. The design is implementation‑complete and paper‑ready.

---

## 0. Staged Execution (Required)

### Stage 1 — Freeze Pilot (6 sessions)
**Goal:** lock the four elements before any main run.

**Frozen items:**
- Judge prompt final
- Trajectory judge rubric final
- BoN scoring weights
- Drift / escalation thresholds

**Pilot matrix (not in main analysis):**
- 3 profiles × 1 scenario × 1 rep × 2 conditions = 6
- Profiles: `anxious_perfectionist`, `creative_rebel`, `neutral_observer`
- Scenario: `crisis_management` (high pressure)
- Output dir: `experiment/results_bcfc_freeze_pilot`

### Stage 2 — Mid‑Check (20 sessions)
**Goal:** catch failure modes early without changing frozen parameters.

**Checks:**
- Hard‑constraint violation rate ≤ 25% of candidate turns
- Trajectory coherence/appropriateness not worse than baseline by > 0.10
- Full‑score BoN beats random/first in offline pool ablation
- Escalation rate ≤ 30% of sessions

**Mid‑check matrix:**
- First 20 sessions from the full matrix with fixed seed and logging
- Output dir: `experiment/results_bcfc_midcheck`

### Stage 3 — Full Run
Complete the full matrix after Stage‑2 passes.

---

## 1. Research Framing (Upgrade #1 + v0 Negative Result)

**Thesis statement**
BCFC is an inference‑time control system that stabilizes persona fidelity in multi‑turn, high‑pressure discussions using behavioral contracts, drift‑bounded monitoring, and best‑of‑N selection — without regeneration or fine‑tuning.

**Negative result integrated**
BCFC v0 degraded fidelity (MAE 0.1607 → 0.176, p=0.0226; all trait correlations dropped) and over‑intervened. This redesign directly targets trajectory breakage and proxy‑target mismatch.

---

## 2. System Architecture (Direction 1)

**Module A — Persona Compiler**
Deterministic contract from OCEAN vectors.

**Module B — Fidelity Controller**
Weighted drift monitoring over a sliding window and nudge injection.

**Module C — Best‑of‑N Selector**
Generate N candidates and select by contract‑aware scoring (no regeneration).

**Module D — Reliability Layer (Direction 3)**
Primary endpoint uses the base 5‑model dual‑order ensemble; escalation is secondary only.

---

## 3. Behavioral Contract and Drift (Upgrades #2 and #4)

**Drift definition**
- Violation rate \(V_t\)
- Normalized distance \(D_t\)
- Composite \(\Delta_t = \alpha V_t + (1-\alpha)D_t\), with `alpha=0.5`
- Threshold `Δ_t ≥ 0.30` triggers a nudge

**Feature reliability weighting**
Feature weights derive from validation correlation and sign:
- Strong: |r| ≥ 0.30 and correct sign → weight 1.0
- Moderate: 0.15 ≤ |r| < 0.30 and correct sign → weight 0.5
- Weak/unstable: |r| < 0.15 or wrong sign → weight 0.1 or soft‑only

**Hard constraints**
Only strong features can be hard‑gated. Weak features are nudge‑only.

---

## 4. Best‑of‑N Scoring (Upgrade #1 + Gap #5)

**Generation**
N=4 by default, same prompt, same temperature, no regeneration.

**Adequacy gate (persona‑neutral)**
Penalize only if a response fails a basic conversational requirement.

**Scoring formula**
`score = 1.0 - (0.65 * contract_distance + 0.20 * relevance_penalty + 0.10 * adequacy_penalty + 0.05 * redundancy_penalty)`

**Bias guardrail**
Name‑mention and length are not directly penalized unless they violate adequacy.

---

## 5. Compute‑Effect Separation (Gap #1)

**Offline pool ablation (primary evidence)**
From each candidate pool, compute counterfactual selections:
- first candidate
- random candidate (expected)
- relevance‑only
- contract‑only
- full score

Report per‑turn contract distance and adequacy improvements.

**Compute‑control subset (secondary evidence)**
- 13 profiles × 1 scenario × 2 reps × 1 condition = 26 sessions
- Condition: BoN‑random (N=4, random selection)
- Included in final analysis, reported as compute‑only control

---

## 6. Evaluation Reliability (Direction 3 + Gap #2)

**Primary endpoint (frozen)**
Base 5‑model dual‑order ensemble only.

**Secondary robustness analysis**
Selective escalation triggered by `uncertain=True`, `confidence < 0.5`, or `model_range > 0.20`. Add 2 models and recompute medians. Report separately.

---

## 7. Trajectory Continuity Metrics (Gap #7)

**Primary trajectory metric**
LLM ensemble judge scores appropriateness + coherence per candidate turn.

**Secondary deterministic diagnostics**
- Direct‑question answer rate
- Contradiction rate
- Unsolicited structure rate
- Over‑verbosity rate

---

## 8. Pressure Manipulation and Checks (Upgrade #5 + Gap #6)

**Low‑pressure condition**
`crisis_management_low`, a softened variant of crisis management.

**Manipulation checks**
- LLM perceived‑pressure rating
- Deterministic stress index (urgency markers, time‑pressure phrases, conflict cues)

**Claim scope**
A focused manipulation within crisis management only.

---

## 9. Trait Difficulty Framing (Gap #3)

Replace “C/O are hard” with:
- Openness is less robustly measured and shows higher evaluator bias.
- C and O appear control‑sensitive under pressure and intervention.

---

## 10. Hyperparameter Freeze (Gap #8)

**Freeze pilot outcome**
Lock all four items after Stage 1.

**Sensitivity analysis**
Offline ±20% perturbations of weights and thresholds.

---

## 11. Experiment Matrix (Final)

High‑pressure main:
- 13 profiles × 4 scenarios × 1 rep × 2 conditions = 104

Low‑pressure main:
- 13 profiles × 1 scenario × 1 rep × 2 conditions = 26

Baseline A:
- 1 profile × 4 scenarios × 1 rep = 4

Baseline B:
- 2 profiles × 4 scenarios × 1 rep × 2 conditions = 16

Compute‑control subset:
- 13 profiles × 1 scenario × 2 reps × 1 condition = 26

**Total sessions:** 176

---

## 12. Logging and Cost Accounting (Gap D)

Add session‑level usage fields:
- `candidate_generation_input_tokens`
- `candidate_generation_output_tokens`
- `judge_input_tokens`
- `judge_output_tokens`
- `escalation_extra_tokens`
- `total_session_cost_usd`
- `wall_clock_seconds`

---

## 13. Implementation Mapping (Repo‑Aligned)

**Create**
- `experiment/bcfc_config.py`
- `experiment/profile_coverage.py`
- `evaluation/trajectory_judge.py`

**Modify**
- `experiment/candidate_agent.py`
- `experiment/fidelity_controller.py`
- `evaluation/trait_evaluator.py`
- `experiment/analysis.py`
- `config/group_scenarios.py`
- `experiment/run_experiment.py`
- `clients/llm_client.py`
- `utils/models.py` (optional if strict typing needed)

---

## 14. Tests and Validation

- Unit: drift metric and weight application
- Unit: BoN scoring and selection
- Unit: escalation triggers
- Integration: candidate pool logging and usage accounting
- Analysis smoke test: full report generation

---

## 15. Acceptance Criteria

- Stage 1 freezes all parameters without revision
- Stage 2 passes mid‑check thresholds
- Stage 3 completes full run with logged cost fields
- Primary endpoint remains base ensemble, escalation reported separately
- Low‑pressure manipulation check shows clear pressure separation

