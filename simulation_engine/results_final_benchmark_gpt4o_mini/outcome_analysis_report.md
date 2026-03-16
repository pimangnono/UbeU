# Outcome Analysis Report

## Executive Summary

Analyzed **60** scenario-condition pairs across **360** simulation runs.
Mean outcome fidelity score: **0.289** (0 = no match, 1 = perfect match with reality).

- **engine_dialogue_only**: mean fidelity = 0.346 (n=20)
- **naive**: mean fidelity = 0.172 (n=20)
- **naive_informed**: mean fidelity = 0.348 (n=20)

## 1. Per-Scenario Outcome vs Reality

### 1.1 Guided Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| singapore_hdb_waittime_crisis | engine_dialogue_only | 6 | 0.87 | 0.65 | 0.39 | 0.00 | 0.80 | 0.62 | **0.596** | 0.482 | 0.3877 |
| singapore_hdb_waittime_crisis | naive_informed | 6 | 0.87 | 0.65 | 0.39 | 0.00 | 0.80 | 0.62 | **0.596** | 0.482 | 0.3895 |
| japan_intern_training_reform | naive | 6 | 1.00 | 0.28 | 0.30 | 0.00 | 0.62 | 0.00 | **0.425** | 0.588 | 0.2959 |
| japan_intern_training_reform | engine_dialogue_only | 6 | 0.53 | 0.41 | 0.39 | 0.00 | 0.46 | 0.66 | **0.422** | 0.588 | 0.2832 |
| japan_intern_training_reform | naive_informed | 6 | 0.53 | 0.41 | 0.38 | 0.00 | 0.46 | 0.66 | **0.420** | 0.588 | 0.2845 |
| eu_gdpr_implementation | engine_dialogue_only | 6 | 0.33 | 0.11 | 0.41 | 0.00 | 0.27 | 0.80 | **0.295** | 0.762 | 0.2015 |
| eu_gdpr_implementation | naive_informed | 6 | 0.33 | 0.11 | 0.41 | 0.00 | 0.27 | 0.80 | **0.295** | 0.762 | 0.2206 |
| california_ab5_gig_classification | engine_dialogue_only | 6 | 0.00 | 0.24 | 0.47 | 0.00 | 0.42 | 0.77 | **0.295** | 0.762 | 0.1949 |
| california_ab5_gig_classification | naive_informed | 6 | 0.00 | 0.24 | 0.47 | 0.00 | 0.42 | 0.77 | **0.295** | 0.762 | 0.2116 |
| nyc_congestion_pricing | engine_dialogue_only | 6 | 0.00 | 0.40 | 0.43 | 0.00 | 0.20 | 0.70 | **0.285** | 0.825 | 0.1828 |
| nyc_congestion_pricing | naive_informed | 6 | 0.00 | 0.40 | 0.43 | 0.00 | 0.20 | 0.70 | **0.285** | 0.825 | 0.1931 |
| singapore_hdb_waittime_crisis | naive | 6 | 1.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.266** | 0.482 | 0.3994 |
| nyc_congestion_pricing | naive | 6 | 0.00 | 0.32 | 0.30 | 0.00 | 0.20 | 0.00 | **0.169** | 0.825 | 0.1941 |
| california_ab5_gig_classification | naive | 6 | 0.00 | 0.16 | 0.30 | 0.00 | 0.30 | 0.00 | **0.145** | 0.762 | 0.2176 |
| eu_gdpr_implementation | naive | 6 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 0.762 | 0.2229 |

### 1.2 Guided Non-Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| boeing_737max_return | engine_dialogue_only | 6 | 0.67 | 0.57 | 0.72 | 0.00 | 0.77 | 0.69 | **0.605** | 0.588 | 0.2829 |
| boeing_737max_return | naive_informed | 6 | 0.67 | 0.57 | 0.72 | 0.00 | 0.77 | 0.69 | **0.605** | 0.588 | 0.2851 |
| zoom_return_to_office | engine_dialogue_only | 6 | 0.00 | 0.39 | 0.87 | 1.00 | 0.73 | 0.63 | **0.544** | 0.657 | 0.2854 |
| zoom_return_to_office | naive_informed | 6 | 0.00 | 0.38 | 0.87 | 1.00 | 0.73 | 0.63 | **0.541** | 0.657 | 0.2925 |
| microsoft_activision_merger | naive_informed | 6 | 0.00 | 0.68 | 0.74 | 0.00 | 0.77 | 0.85 | **0.517** | 0.570 | 0.3050 |
| microsoft_activision_merger | engine_dialogue_only | 6 | 0.00 | 0.65 | 0.74 | 0.00 | 0.73 | 0.85 | **0.507** | 0.570 | 0.3040 |
| boeing_737max_return | naive | 6 | 1.00 | 0.16 | 0.65 | 0.00 | 0.10 | 0.00 | **0.385** | 0.588 | 0.2943 |
| netflix_password_crackdown | engine_dialogue_only | 6 | 0.00 | 0.28 | 0.46 | 0.00 | 0.60 | 0.83 | **0.333** | 0.675 | 0.2832 |
| netflix_password_crackdown | naive_informed | 6 | 0.00 | 0.28 | 0.46 | 0.00 | 0.60 | 0.83 | **0.333** | 0.675 | 0.2867 |
| zoom_return_to_office | naive | 6 | 0.00 | 0.21 | 1.00 | 0.00 | 0.00 | 0.00 | **0.252** | 0.657 | 0.3033 |
| microsoft_activision_merger | naive | 6 | 0.00 | 0.05 | 0.65 | 0.00 | 0.10 | 0.00 | **0.158** | 0.570 | 0.3139 |
| starbucks_unionization | engine_dialogue_only | 6 | 0.00 | 0.03 | 0.40 | 0.00 | 0.00 | 0.59 | **0.145** | 0.825 | 0.1930 |
| starbucks_unionization | naive_informed | 6 | 0.00 | 0.03 | 0.40 | 0.00 | 0.00 | 0.59 | **0.145** | 0.825 | 0.2011 |
| netflix_password_crackdown | naive | 6 | 0.00 | 0.15 | 0.30 | 0.00 | 0.00 | 0.00 | **0.098** | 0.675 | 0.2958 |
| starbucks_unionization | naive | 6 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 0.825 | 0.2059 |

### 1.3 Exploratory Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| fukushima_nuclear_restart | engine_dialogue_only | 6 | 0.67 | 0.65 | 0.49 | 0.00 | 0.40 | 0.64 | **0.517** | 0.675 | 0.2476 |
| fukushima_nuclear_restart | naive_informed | 6 | 0.67 | 0.65 | 0.49 | 0.00 | 0.40 | 0.64 | **0.517** | 0.675 | 0.2547 |
| australia_robodebt | engine_dialogue_only | 6 | 0.60 | 0.28 | 0.40 | 0.00 | 0.67 | 0.78 | **0.447** | 0.762 | 0.2147 |
| australia_robodebt | naive_informed | 6 | 0.60 | 0.28 | 0.40 | 0.00 | 0.67 | 0.78 | **0.447** | 0.762 | 0.2262 |
| uk_post_office_horizon | naive_informed | 6 | 0.60 | 0.24 | 0.52 | 0.42 | 0.30 | 0.65 | **0.436** | 0.850 | 0.2103 |
| uk_post_office_horizon | engine_dialogue_only | 6 | 0.60 | 0.21 | 0.48 | 0.33 | 0.30 | 0.65 | **0.413** | 0.850 | 0.2023 |
| fukushima_nuclear_restart | naive | 6 | 1.00 | 0.28 | 0.30 | 0.00 | 0.40 | 0.00 | **0.389** | 0.675 | 0.2701 |
| uk_post_office_horizon | naive | 6 | 0.60 | 0.07 | 0.42 | 0.00 | 0.10 | 0.00 | **0.237** | 0.850 | 0.2170 |
| flint_water_crisis | engine_dialogue_only | 6 | 0.00 | 0.15 | 0.39 | 0.00 | 0.10 | 0.78 | **0.209** | 1.000 | 0.1832 |
| flint_water_crisis | naive_informed | 6 | 0.00 | 0.15 | 0.39 | 0.00 | 0.10 | 0.78 | **0.209** | 1.000 | 0.1806 |
| sf_homelessness_policy | engine_dialogue_only | 6 | 0.00 | 0.11 | 0.40 | 0.00 | 0.00 | 0.85 | **0.193** | 0.912 | 0.1822 |
| sf_homelessness_policy | naive_informed | 6 | 0.00 | 0.11 | 0.40 | 0.00 | 0.00 | 0.85 | **0.193** | 0.912 | 0.1869 |
| australia_robodebt | naive | 6 | 0.60 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.186** | 0.762 | 0.2309 |
| sf_homelessness_policy | naive | 6 | 0.00 | 0.11 | 0.30 | 0.00 | 0.00 | 0.00 | **0.087** | 0.912 | 0.1947 |
| flint_water_crisis | naive | 6 | 0.00 | 0.03 | 0.30 | 0.00 | 0.10 | 0.00 | **0.081** | 1.000 | 0.1939 |

### 1.4 Exploratory Non-Policy

| Scenario | Condition | Runs | Resolution | Stakeholder | Dynamics | Turning Pts | World State | Action Dist | **Fidelity** | Difficulty | Adj. Drift |
|----------|-----------|------|-----------|-------------|----------|------------|-------------|-------------|------------|------------|------------|
| wework_ipo_collapse | engine_dialogue_only | 6 | 0.00 | 0.22 | 0.44 | 1.00 | 0.00 | 0.89 | **0.332** | 1.000 | 0.1696 |
| wework_ipo_collapse | naive_informed | 6 | 0.00 | 0.20 | 0.44 | 1.00 | 0.00 | 0.89 | **0.328** | 1.000 | 0.1688 |
| svb_bank_run | engine_dialogue_only | 6 | 0.00 | 0.28 | 0.43 | 0.00 | 0.30 | 0.77 | **0.276** | 0.588 | 0.2791 |
| svb_bank_run | naive_informed | 6 | 0.00 | 0.28 | 0.43 | 0.00 | 0.30 | 0.77 | **0.276** | 0.588 | 0.2820 |
| theranos_whistleblower | engine_dialogue_only | 6 | 0.00 | 0.11 | 0.39 | 0.00 | 0.27 | 0.58 | **0.203** | 1.000 | 0.1829 |
| theranos_whistleblower | naive_informed | 6 | 0.00 | 0.11 | 0.39 | 0.00 | 0.27 | 0.58 | **0.203** | 1.000 | 0.1831 |
| ftx_collapse | engine_dialogue_only | 6 | 0.00 | 0.05 | 0.39 | 0.00 | 0.07 | 0.59 | **0.160** | 1.000 | 0.1695 |
| ftx_collapse | naive_informed | 6 | 0.00 | 0.05 | 0.39 | 0.00 | 0.07 | 0.59 | **0.160** | 1.000 | 0.1754 |
| peloton_demand_cliff | engine_dialogue_only | 6 | 0.00 | 0.07 | 0.38 | 0.00 | 0.00 | 0.56 | **0.150** | 0.912 | 0.1744 |
| peloton_demand_cliff | naive_informed | 6 | 0.00 | 0.07 | 0.38 | 0.00 | 0.00 | 0.56 | **0.150** | 0.912 | 0.1814 |
| wework_ipo_collapse | naive | 6 | 0.00 | 0.21 | 0.36 | 0.00 | 0.00 | 0.00 | **0.125** | 1.000 | 0.1828 |
| svb_bank_run | naive | 6 | 0.00 | 0.03 | 0.30 | 0.00 | 0.10 | 0.00 | **0.081** | 0.588 | 0.3020 |
| peloton_demand_cliff | naive | 6 | 0.00 | 0.07 | 0.30 | 0.00 | 0.00 | 0.00 | **0.079** | 0.912 | 0.1887 |
| ftx_collapse | naive | 6 | 0.00 | 0.05 | 0.30 | 0.00 | 0.00 | 0.00 | **0.072** | 1.000 | 0.1878 |
| theranos_whistleblower | naive | 6 | 0.00 | 0.03 | 0.30 | 0.00 | 0.00 | 0.00 | **0.066** | 1.000 | 0.1855 |

## 2. Guided vs Exploratory: Does Outcome Anchoring Help?

- Guided mean fidelity: 0.336 (n=30)
- Exploratory mean fidelity: 0.241 (n=30)
- **Guided** produces 0.095 higher outcome fidelity.

## 3. Actor Count Effect on Outcome Quality

- 10:engine_dialogue_only: mean fidelity = 0.346 (n=20)
- 10:naive: mean fidelity = 0.172 (n=20)
- 10:naive_informed: mean fidelity = 0.348 (n=20)

## 4. Engine vs Naive: Does Better Fidelity = Better Outcomes?

- Engine mean fidelity: 0.346 (n=20)
- Naive mean fidelity: 0.172 (n=20)
- Delta (engine - naive): +0.175
- **Yes**: Better persona fidelity (engine) produces more realistic outcomes.

## 5. Diagnostic Findings

### 5.1 Trait Errors Predicting Outcome Failures

Per-trait error correlations with outcome fidelity: O=0.058, C=0.358, E=-0.094, A=0.100, N=-0.075. Overall drift r=0.1699. Most negative trait: E (r=-0.094).

### 5.2 Action Type Biases

Overused families: none. Underused families: communication, resourcing, timing, governance. Bias vector: {'ownership': -0.0012, 'evidence': -0.0108, 'communication': -0.103, 'scope': -0.0292, 'resourcing': -0.1181, 'timing': -0.1475, 'governance': -0.209}.

### 5.3 Phase Attribution

Phase accuracy: {'NEGOTIATION': 0.4423, 'CLOSING': 0.6012}. Best phase: CLOSING. Worst phase: NEGOTIATION.

### 5.4 Convergence-Outcome Relationship

Convergence-outcome Pearson r=-0.036 (n=360). Q1 fidelity: 0.3445, Q4 fidelity: 0.3161.

### 5.5 Relationship Dynamics Gap

De-escalation bias: 87.4% of adversarial scenarios simulated as non-adversarial (n=1188). Mean tension in expected-high scenarios: 0.113. Mean tension in expected-low/medium scenarios: 0.155.

### 5.6 Archetype Difficulty Ranking

Hardest archetypes to simulate (highest trait error): community_pastor (0.243), urban_planner (0.243), vc_partner (0.238), outreach_worker (0.229), vpn_product_manager (0.228).

## 6. Engine Parameter Recommendations

| # | Finding | Parameter | File | Confidence |
|---|---------|-----------|------|-----------|
| 1 | Action family 'communication' is underused (bias=-0.103) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 2 | Action family 'resourcing' is underused (bias=-0.118) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 3 | Action family 'timing' is underused (bias=-0.147) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 4 | Action family 'governance' is underused (bias=-0.209) | `action vocabulary rotation` | `controller.py / script phases` | medium |
| 5 | De-escalation bias: 87.4% of adversarial scenarios are too cooperative | `NEGATIVE/CHALLENGE keyword sets, tension_delta values` | `state_ledger.py` | high |

### Recommendation 1: action vocabulary rotation

**Finding**: Action family 'communication' is underused (bias=-0.103)

**Recommendation**: Add explicit cues for 'communication' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 2: action vocabulary rotation

**Finding**: Action family 'resourcing' is underused (bias=-0.118)

**Recommendation**: Add explicit cues for 'resourcing' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 3: action vocabulary rotation

**Finding**: Action family 'timing' is underused (bias=-0.147)

**Recommendation**: Add explicit cues for 'timing' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 4: action vocabulary rotation

**Finding**: Action family 'governance' is underused (bias=-0.209)

**Recommendation**: Add explicit cues for 'governance' family in generated scripts.

**Rationale**: Systematic underused bias across scenarios

**Confidence**: medium

### Recommendation 5: NEGATIVE/CHALLENGE keyword sets, tension_delta values

**Finding**: De-escalation bias: 87.4% of adversarial scenarios are too cooperative

**Recommendation**: Expand _NEGATIVE_REL and _CHALLENGE_REL keyword tuples in state_ledger.py. Increase tension_delta magnitude for detected conflict. Consider adding sycophancy penalty increase for high-tension scenarios.

**Rationale**: Engine systematically de-escalates when reality was adversarial (RLHF sycophancy)

**Confidence**: high
