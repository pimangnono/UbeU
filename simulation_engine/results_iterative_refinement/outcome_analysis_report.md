# Outcome Analysis Report

## Executive Summary

Analyzed **40** scenario-condition pairs across **1080** simulation runs.
Mean outcome fidelity score: **0.225** (0 = no match, 1 = perfect match with reality).

- **engine_structural**: mean fidelity = 0.290 (n=20)
- **naive**: mean fidelity = 0.161 (n=20)

## 1. Per-Scenario Outcome vs Reality

### 1.1 Guided Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| singapore_hdb_waittime_crisis | engine_structural | 18 | 0.73 | 0.46 | 0.35 | 0.00 | 0.56 | 0.64 | **0.480** | 0.482 | 0.3990 |
| japan_intern_training_reform | naive | 32 | 1.00 | 0.29 | 0.30 | 0.00 | 0.62 | 0.00 | **0.426** | 0.588 | 0.2976 |
| japan_intern_training_reform | engine_structural | 34 | 0.53 | 0.39 | 0.36 | 0.00 | 0.45 | 0.64 | **0.406** | 0.588 | 0.2935 |
| california_ab5_gig_classification | engine_structural | 46 | 0.00 | 0.39 | 0.47 | 0.00 | 0.20 | 0.80 | **0.303** | 0.762 | 0.2100 |
| singapore_hdb_waittime_crisis | naive | 18 | 1.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.266** | 0.482 | 0.4065 |
| eu_gdpr_implementation | engine_structural | 42 | 0.33 | 0.09 | 0.41 | 0.00 | 0.15 | 0.73 | **0.266** | 0.762 | 0.2023 |
| nyc_congestion_pricing | engine_structural | 24 | 0.00 | 0.11 | 0.44 | 0.00 | 0.07 | 0.68 | **0.194** | 0.825 | 0.1872 |
| california_ab5_gig_classification | naive | 44 | 0.00 | 0.39 | 0.30 | 0.00 | 0.16 | 0.00 | **0.180** | 0.762 | 0.2195 |
| nyc_congestion_pricing | naive | 24 | 0.00 | 0.34 | 0.30 | 0.00 | 0.20 | 0.00 | **0.175** | 0.825 | 0.1920 |
| eu_gdpr_implementation | naive | 42 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 0.762 | 0.2193 |

### 1.2 Guided Non-Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| boeing_737max_return | engine_structural | 48 | 0.40 | 0.45 | 0.68 | 0.00 | 0.52 | 0.64 | **0.471** | 0.588 | 0.2787 |
| microsoft_activision_merger | engine_structural | 30 | 0.00 | 0.50 | 0.68 | 0.00 | 0.61 | 0.83 | **0.435** | 0.570 | 0.3025 |
| boeing_737max_return | naive | 48 | 1.00 | 0.11 | 0.65 | 0.00 | 0.10 | 0.00 | **0.372** | 0.588 | 0.2883 |
| zoom_return_to_office | engine_structural | 6 | 0.00 | 0.36 | 0.40 | 0.00 | 0.63 | 0.67 | **0.332** | 0.657 | 0.2836 |
| netflix_password_crackdown | engine_structural | 30 | 0.00 | 0.22 | 0.43 | 0.00 | 0.34 | 0.76 | **0.269** | 0.675 | 0.2769 |
| microsoft_activision_merger | naive | 30 | 0.00 | 0.03 | 0.65 | 0.00 | 0.10 | 0.00 | **0.151** | 0.570 | 0.3136 |
| starbucks_unionization | engine_structural | 18 | 0.00 | 0.03 | 0.41 | 0.00 | 0.00 | 0.60 | **0.149** | 0.825 | 0.1982 |
| netflix_password_crackdown | naive | 30 | 0.00 | 0.15 | 0.30 | 0.00 | 0.00 | 0.00 | **0.098** | 0.675 | 0.3011 |
| zoom_return_to_office | naive | 6 | 0.00 | 0.15 | 0.30 | 0.00 | 0.00 | 0.00 | **0.098** | 0.657 | 0.3068 |
| starbucks_unionization | naive | 18 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 0.825 | 0.2061 |

### 1.3 Exploratory Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| fukushima_nuclear_restart | engine_structural | 36 | 1.00 | 0.39 | 0.44 | 0.00 | 0.20 | 0.62 | **0.479** | 0.675 | 0.2478 |
| australia_robodebt | engine_structural | 48 | 0.60 | 0.20 | 0.43 | 0.00 | 0.43 | 0.77 | **0.398** | 0.762 | 0.2220 |
| fukushima_nuclear_restart | naive | 36 | 1.00 | 0.28 | 0.30 | 0.00 | 0.40 | 0.00 | **0.389** | 0.675 | 0.2585 |
| uk_post_office_horizon | engine_structural | 10 | 0.60 | 0.11 | 0.42 | 0.00 | 0.21 | 0.66 | **0.330** | 0.850 | 0.2106 |
| uk_post_office_horizon | naive | 8 | 0.60 | 0.07 | 0.30 | 0.00 | 0.10 | 0.00 | **0.214** | 0.850 | 0.2177 |
| flint_water_crisis | engine_structural | 42 | 0.00 | 0.08 | 0.41 | 0.00 | 0.10 | 0.76 | **0.193** | 1.000 | 0.1795 |
| sf_homelessness_policy | engine_structural | 22 | 0.00 | 0.09 | 0.42 | 0.00 | 0.00 | 0.87 | **0.192** | 0.912 | 0.1802 |
| australia_robodebt | naive | 48 | 0.60 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.186** | 0.762 | 0.2331 |
| sf_homelessness_policy | naive | 20 | 0.00 | 0.09 | 0.30 | 0.00 | 0.00 | 0.00 | **0.083** | 0.912 | 0.1960 |
| flint_water_crisis | naive | 42 | 0.00 | 0.03 | 0.30 | 0.00 | 0.10 | 0.00 | **0.081** | 1.000 | 0.1917 |

### 1.4 Exploratory Non-Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| svb_bank_run | engine_structural | 12 | 0.00 | 0.18 | 0.44 | 0.00 | 0.19 | 0.68 | **0.230** | 0.588 | 0.2678 |
| wework_ipo_collapse | engine_structural | 6 | 0.00 | 0.03 | 0.44 | 0.00 | 0.00 | 0.92 | **0.186** | 1.000 | 0.1690 |
| theranos_whistleblower | engine_structural | 12 | 0.00 | 0.05 | 0.40 | 0.00 | 0.14 | 0.56 | **0.171** | 1.000 | 0.1755 |
| ftx_collapse | engine_structural | 36 | 0.00 | 0.05 | 0.41 | 0.00 | 0.05 | 0.59 | **0.162** | 1.000 | 0.1704 |
| peloton_demand_cliff | engine_structural | 24 | 0.00 | 0.07 | 0.39 | 0.00 | 0.00 | 0.56 | **0.153** | 0.912 | 0.1748 |
| svb_bank_run | naive | 12 | 0.00 | 0.03 | 0.30 | 0.00 | 0.10 | 0.00 | **0.081** | 0.588 | 0.2908 |
| peloton_demand_cliff | naive | 24 | 0.00 | 0.07 | 0.30 | 0.00 | 0.00 | 0.00 | **0.079** | 0.912 | 0.1878 |
| ftx_collapse | naive | 36 | 0.00 | 0.05 | 0.30 | 0.00 | 0.00 | 0.00 | **0.072** | 1.000 | 0.1820 |
| wework_ipo_collapse | naive | 6 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 1.000 | 0.1857 |
| theranos_whistleblower | naive | 12 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 1.000 | 0.1876 |

## 2. Guided vs Exploratory: Does Outcome Anchoring Help?

- Guided mean fidelity: 0.260 (n=20)
- Exploratory mean fidelity: 0.191 (n=20)
- **Guided** produces 0.070 higher outcome fidelity.

## 3. Actor Count Effect on Outcome Quality

- 10:engine_structural: mean fidelity = 0.290 (n=20)
- 10:naive: mean fidelity = 0.161 (n=20)

## 4. Engine vs Naive: Does Better Fidelity = Better Outcomes?

- Engine (engine_structural) mean fidelity: 0.290 (n=20)
- Naive (naive) mean fidelity: 0.161 (n=20)
- Delta (engine - naive): +0.129
- **Yes**: Better persona fidelity (engine) produces more realistic outcomes.

- Welch's t-test: t=3.470, df=38.0, p=0.0006
- Cohen's d: +1.097 (large)
- 95% CI for delta: [+0.056, +0.202]

## 5. Diagnostic Findings

### 5.1 Trait Errors Predicting Outcome Failures

Per-trait error correlations with outcome fidelity: O=-0.044, C=0.194, E=-0.213, A=-0.023, N=0.012. Overall drift r=-0.0679. Most negative trait: E (r=-0.213).

### 5.2 Action Type Biases

Overused families: none. Underused families: communication, resourcing, timing, governance. Bias vector: {'ownership': -0.0308, 'evidence': -0.0055, 'communication': -0.1189, 'scope': 0.0115, 'resourcing': -0.1023, 'timing': -0.1333, 'governance': -0.2038}.

### 5.3 Phase Attribution

Phase accuracy: {'NEGOTIATION': 0.3493, 'CLOSING': 0.4448}. Best phase: CLOSING. Worst phase: NEGOTIATION.

### 5.4 Convergence-Outcome Relationship

Convergence-outcome Pearson r=0.039 (n=1080). Q1 fidelity: 0.202, Q4 fidelity: 0.1936.

### 5.5 Relationship Dynamics Gap

De-escalation bias: 100.0% of adversarial scenarios simulated as non-adversarial (n=15660). Mean tension in expected-high scenarios: 0.000. Mean tension in expected-low/medium scenarios: 0.000.

### 5.6 Archetype Difficulty Ranking

Hardest archetypes to simulate (highest trait error): pediatrician (0.249), urban_planner (0.241), community_pastor (0.237), activist_investor (0.233), vpn_product_manager (0.231).

## 6. Engine Parameter Recommendations

| # | Finding | Parameter | File | Confidence |
|---|---------|-----------|------|-----------|
| 1 | Action family 'communication' is underused (bias=-0.119) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 2 | Action family 'resourcing' is underused (bias=-0.102) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 3 | Action family 'timing' is underused (bias=-0.133) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 4 | Action family 'governance' is underused (bias=-0.204) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 5 | De-escalation bias: 100.0% of adversarial scenarios are too cooperative | `NEGATIVE/CHALLENGE keyword sets, tension_delta values` | `state_ledger.py` | high |

### Recommendation 1: action vocabulary rotation

**Finding**: Action family 'communication' is underused (bias=-0.119)

**Recommendation**: Add explicit cues for 'communication' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 2: action vocabulary rotation

**Finding**: Action family 'resourcing' is underused (bias=-0.102)

**Recommendation**: Add explicit cues for 'resourcing' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 3: action vocabulary rotation

**Finding**: Action family 'timing' is underused (bias=-0.133)

**Recommendation**: Add explicit cues for 'timing' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 4: action vocabulary rotation

**Finding**: Action family 'governance' is underused (bias=-0.204)

**Recommendation**: Add explicit cues for 'governance' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 5: NEGATIVE/CHALLENGE keyword sets, tension_delta values

**Finding**: De-escalation bias: 100.0% of adversarial scenarios are too cooperative

**Recommendation**: Expand _NEGATIVE_REL and _CHALLENGE_REL keyword tuples in state_ledger.py. Increase tension_delta magnitude for detected conflict. Consider adding sycophancy penalty increase for high-tension scenarios.

**Rationale**: Engine systematically de-escalates when reality was adversarial (RLHF sycophancy)

**Confidence**: high
