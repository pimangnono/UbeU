# Outcome Analysis Report

## Executive Summary

Analyzed **40** scenario-condition pairs across **4080** simulation runs.
Mean outcome fidelity score: **0.232** (0 = no match, 1 = perfect match with reality).

- **engine_structural**: mean fidelity = 0.302 (n=20)
- **naive**: mean fidelity = 0.161 (n=20)

## 1. Per-Scenario Outcome vs Reality

### 1.1 Guided Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| singapore_hdb_waittime_crisis | engine_structural | 70 | 0.74 | 0.46 | 0.39 | 0.00 | 0.56 | 0.61 | **0.487** | 0.482 | 0.3937 |
| japan_intern_training_reform | naive | 124 | 1.00 | 0.29 | 0.30 | 0.00 | 0.62 | 0.00 | **0.425** | 0.588 | 0.2973 |
| japan_intern_training_reform | engine_structural | 128 | 0.53 | 0.39 | 0.38 | 0.00 | 0.45 | 0.66 | **0.414** | 0.588 | 0.2854 |
| california_ab5_gig_classification | engine_structural | 176 | 0.00 | 0.40 | 0.47 | 0.00 | 0.20 | 0.76 | **0.299** | 0.762 | 0.2000 |
| eu_gdpr_implementation | engine_structural | 166 | 0.34 | 0.09 | 0.41 | 0.00 | 0.19 | 0.78 | **0.278** | 0.762 | 0.2044 |
| singapore_hdb_waittime_crisis | naive | 68 | 1.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.267** | 0.482 | 0.4170 |
| nyc_congestion_pricing | engine_structural | 96 | 0.00 | 0.11 | 0.44 | 0.00 | 0.07 | 0.69 | **0.194** | 0.825 | 0.1875 |
| california_ab5_gig_classification | naive | 172 | 0.00 | 0.39 | 0.30 | 0.00 | 0.16 | 0.00 | **0.182** | 0.762 | 0.2174 |
| nyc_congestion_pricing | naive | 96 | 0.00 | 0.34 | 0.30 | 0.00 | 0.20 | 0.00 | **0.175** | 0.825 | 0.1984 |
| eu_gdpr_implementation | naive | 164 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 0.762 | 0.2219 |

### 1.2 Guided Non-Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| boeing_737max_return | engine_structural | 184 | 0.67 | 0.57 | 0.70 | 0.00 | 0.64 | 0.67 | **0.581** | 0.588 | 0.2816 |
| microsoft_activision_merger | engine_structural | 118 | 0.00 | 0.51 | 0.72 | 0.00 | 0.61 | 0.85 | **0.448** | 0.570 | 0.2983 |
| boeing_737max_return | naive | 182 | 1.00 | 0.11 | 0.65 | 0.00 | 0.10 | 0.00 | **0.372** | 0.588 | 0.2825 |
| zoom_return_to_office | engine_structural | 12 | 0.00 | 0.38 | 0.43 | 0.00 | 0.64 | 0.72 | **0.348** | 0.657 | 0.2822 |
| netflix_password_crackdown | engine_structural | 108 | 0.00 | 0.25 | 0.46 | 0.00 | 0.45 | 0.81 | **0.301** | 0.675 | 0.2799 |
| microsoft_activision_merger | naive | 116 | 0.00 | 0.03 | 0.65 | 0.00 | 0.10 | 0.00 | **0.151** | 0.570 | 0.3204 |
| starbucks_unionization | engine_structural | 60 | 0.00 | 0.03 | 0.41 | 0.00 | 0.00 | 0.60 | **0.149** | 0.825 | 0.1935 |
| netflix_password_crackdown | naive | 108 | 0.00 | 0.15 | 0.30 | 0.00 | 0.00 | 0.00 | **0.098** | 0.675 | 0.3074 |
| zoom_return_to_office | naive | 12 | 0.00 | 0.15 | 0.30 | 0.00 | 0.00 | 0.00 | **0.098** | 0.657 | 0.3038 |
| starbucks_unionization | naive | 60 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 0.825 | 0.2066 |

### 1.3 Exploratory Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| fukushima_nuclear_restart | engine_structural | 136 | 1.00 | 0.43 | 0.47 | 0.00 | 0.20 | 0.63 | **0.493** | 0.675 | 0.2496 |
| australia_robodebt | engine_structural | 192 | 0.60 | 0.20 | 0.41 | 0.00 | 0.48 | 0.77 | **0.401** | 0.762 | 0.2228 |
| fukushima_nuclear_restart | naive | 134 | 1.00 | 0.27 | 0.30 | 0.00 | 0.40 | 0.00 | **0.389** | 0.675 | 0.2618 |
| uk_post_office_horizon | engine_structural | 32 | 0.60 | 0.13 | 0.43 | 0.00 | 0.28 | 0.67 | **0.347** | 0.850 | 0.2109 |
| uk_post_office_horizon | naive | 28 | 0.60 | 0.07 | 0.30 | 0.00 | 0.10 | 0.00 | **0.214** | 0.850 | 0.2206 |
| flint_water_crisis | engine_structural | 156 | 0.00 | 0.11 | 0.41 | 0.00 | 0.10 | 0.76 | **0.201** | 1.000 | 0.1791 |
| sf_homelessness_policy | engine_structural | 80 | 0.00 | 0.09 | 0.42 | 0.00 | 0.00 | 0.85 | **0.191** | 0.912 | 0.1766 |
| australia_robodebt | naive | 192 | 0.60 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.186** | 0.762 | 0.2349 |
| sf_homelessness_policy | naive | 76 | 0.00 | 0.09 | 0.30 | 0.00 | 0.00 | 0.00 | **0.083** | 0.912 | 0.1958 |
| flint_water_crisis | naive | 156 | 0.00 | 0.03 | 0.30 | 0.00 | 0.10 | 0.00 | **0.081** | 1.000 | 0.1924 |

### 1.4 Exploratory Non-Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| svb_bank_run | engine_structural | 48 | 0.00 | 0.18 | 0.44 | 0.00 | 0.19 | 0.73 | **0.235** | 0.588 | 0.2710 |
| wework_ipo_collapse | engine_structural | 22 | 0.00 | 0.03 | 0.44 | 0.00 | 0.00 | 0.90 | **0.185** | 1.000 | 0.1765 |
| theranos_whistleblower | engine_structural | 40 | 0.00 | 0.08 | 0.39 | 0.00 | 0.14 | 0.58 | **0.176** | 1.000 | 0.1793 |
| ftx_collapse | engine_structural | 144 | 0.00 | 0.05 | 0.41 | 0.00 | 0.05 | 0.58 | **0.161** | 1.000 | 0.1725 |
| peloton_demand_cliff | engine_structural | 88 | 0.00 | 0.07 | 0.39 | 0.00 | 0.00 | 0.58 | **0.155** | 0.912 | 0.1770 |
| svb_bank_run | naive | 48 | 0.00 | 0.03 | 0.30 | 0.00 | 0.10 | 0.00 | **0.081** | 0.588 | 0.2901 |
| peloton_demand_cliff | naive | 86 | 0.00 | 0.07 | 0.30 | 0.00 | 0.00 | 0.00 | **0.079** | 0.912 | 0.1884 |
| ftx_collapse | naive | 144 | 0.00 | 0.05 | 0.30 | 0.00 | 0.00 | 0.00 | **0.072** | 1.000 | 0.1805 |
| wework_ipo_collapse | naive | 20 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.068** | 1.000 | 0.1839 |
| theranos_whistleblower | naive | 38 | 0.00 | 0.02 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 1.000 | 0.1860 |

## 2. Guided vs Exploratory: Does Outcome Anchoring Help?

- Guided mean fidelity: 0.270 (n=20)
- Exploratory mean fidelity: 0.193 (n=20)
- **Guided** produces 0.077 higher outcome fidelity.

## 3. Actor Count Effect on Outcome Quality

- 10:engine_structural: mean fidelity = 0.302 (n=20)
- 10:naive: mean fidelity = 0.161 (n=20)

## 4. Engine vs Naive: Does Better Fidelity = Better Outcomes?

- Engine (engine_structural) mean fidelity: 0.302 (n=20)
- Naive (naive) mean fidelity: 0.161 (n=20)
- Delta (engine - naive): +0.141
- **Yes**: Better persona fidelity (engine) produces more realistic outcomes.

- Welch's t-test: t=3.588, df=37.5, p=0.0004
- Cohen's d: +1.135 (large)
- 95% CI for delta: [+0.064, +0.218]

## 5. Diagnostic Findings

### 5.1 Trait Errors Predicting Outcome Failures

Per-trait error correlations with outcome fidelity: O=-0.056, C=0.200, E=-0.192, A=-0.059, N=0.011. Overall drift r=-0.0825. Most negative trait: E (r=-0.192).

### 5.2 Action Type Biases

Overused families: none. Underused families: communication, resourcing, timing, governance. Bias vector: {'ownership': 0.0123, 'evidence': -0.0068, 'communication': -0.1187, 'scope': -0.016, 'resourcing': -0.1168, 'timing': -0.1333, 'governance': -0.2025}.

### 5.3 Phase Attribution

Phase accuracy: {'NEGOTIATION': 0.4514, 'CLOSING': 0.517}. Best phase: CLOSING. Worst phase: NEGOTIATION.

### 5.4 Convergence-Outcome Relationship

Convergence-outcome Pearson r=0.038 (n=4080). Q1 fidelity: 0.1974, Q4 fidelity: 0.2012.

### 5.5 Relationship Dynamics Gap

De-escalation bias: 100.0% of adversarial scenarios simulated as non-adversarial (n=231000). Mean tension in expected-high scenarios: 0.000. Mean tension in expected-low/medium scenarios: 0.000.

### 5.6 Archetype Difficulty Ranking

Hardest archetypes to simulate (highest trait error): pediatrician (0.251), urban_planner (0.241), activist_investor (0.240), community_pastor (0.234), vpn_product_manager (0.232).

## 6. Engine Parameter Recommendations

| # | Finding | Parameter | File | Confidence |
|---|---------|-----------|------|-----------|
| 1 | Action family 'communication' is underused (bias=-0.119) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 2 | Action family 'resourcing' is underused (bias=-0.117) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 3 | Action family 'timing' is underused (bias=-0.133) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 4 | Action family 'governance' is underused (bias=-0.203) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 5 | De-escalation bias: 100.0% of adversarial scenarios are too cooperative | `NEGATIVE/CHALLENGE keyword sets, tension_delta values` | `state_ledger.py` | high |

### Recommendation 1: action vocabulary rotation

**Finding**: Action family 'communication' is underused (bias=-0.119)

**Recommendation**: Add explicit cues for 'communication' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 2: action vocabulary rotation

**Finding**: Action family 'resourcing' is underused (bias=-0.117)

**Recommendation**: Add explicit cues for 'resourcing' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 3: action vocabulary rotation

**Finding**: Action family 'timing' is underused (bias=-0.133)

**Recommendation**: Add explicit cues for 'timing' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 4: action vocabulary rotation

**Finding**: Action family 'governance' is underused (bias=-0.203)

**Recommendation**: Add explicit cues for 'governance' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 5: NEGATIVE/CHALLENGE keyword sets, tension_delta values

**Finding**: De-escalation bias: 100.0% of adversarial scenarios are too cooperative

**Recommendation**: Expand _NEGATIVE_REL and _CHALLENGE_REL keyword tuples in state_ledger.py. Increase tension_delta magnitude for detected conflict. Consider adding sycophancy penalty increase for high-tension scenarios.

**Rationale**: Engine systematically de-escalates when reality was adversarial (RLHF sycophancy)

**Confidence**: high
