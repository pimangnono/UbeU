# Game Theory Analysis Report

## Executive Summary

- **180 runs analyzed** (engine: 92, naive: 88)
- Engine cooperation rate: 0.320 vs Naive: 0.223 (p=0.0006, d=0.522)
- Rational strategy adoption: Engine 8.3% vs Naive 21.6% (p=0.0000)

## 1. Strategy Distribution by Condition

| Strategy | engine_structural (%) | naive (%) |
|--------|--------|--------|
| always_cooperate | 57.4% | 46.1% |
| always_defect | 34.0% | 32.3% |
| gradual | 0.4% | 0.0% |
| pavlov * | 0.9% | 0.0% |
| tit_for_tat * | 7.4% | 21.6% |

\* = rational strategy (Axelrod-optimal)

## 2. Cooperation & Rationality Metrics

| Metric | Engine | Naive | Cohen's d | p-value |
|--------|--------|-------|-----------|---------|
| cooperation_rate | 0.3196 | 0.2227 | 0.522 | 0.0006 |
| conditional_cooperation_rate | 0.6487 | 0.7001 | -0.226 | 0.1323 |
| rationality_score | 0.5195 | 0.5177 | 0.058 | 0.6972 |
| exploitability | 0.1225 | 0.0774 | 0.424 | 0.0048 |

## 3. By Actor Count

| Actor Count | Condition | N | Coop Rate | Rationality | Exploitability |
|-------------|-----------|---|-----------|-------------|----------------|
| 3 | engine_structural | 32 | 0.2651 | 0.5188 | 0.0825 |
| 3 | naive | 28 | 0.1913 | 0.5108 | 0.0437 |
| 5 | engine_structural | 28 | 0.3175 | 0.5156 | 0.1795 |
| 5 | naive | 28 | 0.2268 | 0.5189 | 0.0920 |
| 10 | engine_structural | 32 | 0.3759 | 0.5235 | 0.1126 |
| 10 | naive | 32 | 0.2465 | 0.5226 | 0.0941 |

## 4. Per-Scenario Breakdown

### 4a. Cooperation Rate by Scenario

| Scenario | engine_structural | naive | Delta | p-value |
|----------|----------|----------|----------|----------|
| australia_robodebt | 0.101 | 0.121 | -0.021 | 0.610 |
| boeing_737max_return | 0.376 | 0.312 | +0.064 | 0.356 |
| california_ab5_gig_classification | 0.407 | 0.082 | +0.325 | 0.000* |
| eu_gdpr_implementation | 0.489 | 0.227 | +0.262 | 0.001* |
| flint_water_crisis | 0.391 | 0.330 | +0.062 | 0.396 |
| ftx_collapse | 0.176 | 0.286 | -0.110 | 0.143 |
| fukushima_nuclear_restart | 0.395 | 0.224 | +0.171 | 0.025* |
| japan_intern_training_reform | 0.173 | 0.149 | +0.024 | 0.773 |

### 4b. Dominant Strategy by Scenario

| Scenario | Condition | Top Strategy | % | 2nd Strategy | % |
|----------|-----------|-------------|---|-------------|---|
| australia_robodebt | engine_structural | always_defect | 78% | always_cooperate | 21% |
| australia_robodebt | naive | always_defect | 51% | always_cooperate | 34% |
| boeing_737max_return | engine_structural | always_cooperate | 71% | always_defect | 16% |
| boeing_737max_return | naive | always_cooperate | 65% | tit_for_tat | 23% |
| california_ab5_gig_classification | engine_structural | always_cooperate | 66% | always_defect | 31% |
| california_ab5_gig_classification | naive | always_defect | 59% | always_cooperate | 27% |
| eu_gdpr_implementation | engine_structural | always_cooperate | 74% | always_defect | 18% |
| eu_gdpr_implementation | naive | always_defect | 43% | always_cooperate | 35% |
| flint_water_crisis | engine_structural | always_cooperate | 57% | always_defect | 28% |
| flint_water_crisis | naive | always_cooperate | 51% | always_defect | 28% |
| ftx_collapse | engine_structural | always_defect | 47% | always_cooperate | 45% |
| ftx_collapse | naive | always_cooperate | 47% | always_defect | 35% |
| fukushima_nuclear_restart | engine_structural | always_cooperate | 56% | always_defect | 33% |
| fukushima_nuclear_restart | naive | always_cooperate | 46% | tit_for_tat | 32% |
| japan_intern_training_reform | engine_structural | always_defect | 52% | always_cooperate | 42% |
| japan_intern_training_reform | naive | always_defect | 43% | always_cooperate | 36% |

### 4c. Per-Scenario Statistical Tests (Engine vs Naive)

| Scenario | Metric | Engine | Naive | Delta | Cohen's d | p-value |
|----------|--------|--------|-------|-------|-----------|---------|
| australia_robodebt | cooperation_rate | 0.101 | 0.121 | -0.021 | -0.21 | 0.610 |
| australia_robodebt | rationality_score | 0.471 | 0.485 | -0.014 | -1.23 | 0.008* |
| australia_robodebt | exploitability | 0.132 | 0.072 | +0.060 | 0.47 | 0.267 |
| boeing_737max_return | cooperation_rate | 0.376 | 0.312 | +0.064 | 0.39 | 0.356 |
| boeing_737max_return | rationality_score | 0.506 | 0.505 | +0.001 | 0.05 | 0.912 |
| boeing_737max_return | exploitability | 0.129 | 0.072 | +0.057 | 0.53 | 0.204 |
| california_ab5_gig_classification | cooperation_rate | 0.407 | 0.082 | +0.325 | 3.19 | 0.000* |
| california_ab5_gig_classification | rationality_score | 0.554 | 0.548 | +0.006 | 0.47 | 0.264 |
| california_ab5_gig_classification | exploitability | 0.197 | 0.072 | +0.125 | 1.29 | 0.004* |
| eu_gdpr_implementation | cooperation_rate | 0.489 | 0.227 | +0.262 | 1.67 | 0.001* |
| eu_gdpr_implementation | rationality_score | 0.545 | 0.542 | +0.003 | 0.25 | 0.550 |
| eu_gdpr_implementation | exploitability | 0.157 | 0.084 | +0.073 | 0.78 | 0.071 |
| flint_water_crisis | cooperation_rate | 0.391 | 0.330 | +0.062 | 0.36 | 0.396 |
| flint_water_crisis | rationality_score | 0.541 | 0.538 | +0.003 | 0.15 | 0.717 |
| flint_water_crisis | exploitability | 0.072 | 0.092 | -0.021 | -0.20 | 0.622 |
| ftx_collapse | cooperation_rate | 0.176 | 0.286 | -0.110 | -0.62 | 0.143 |
| ftx_collapse | rationality_score | 0.486 | 0.500 | -0.014 | -0.67 | 0.117 |
| ftx_collapse | exploitability | 0.056 | 0.106 | -0.049 | -0.41 | 0.329 |
| fukushima_nuclear_restart | cooperation_rate | 0.395 | 0.224 | +0.171 | 0.99 | 0.025* |
| fukushima_nuclear_restart | rationality_score | 0.509 | 0.500 | +0.009 | 0.52 | 0.214 |
| fukushima_nuclear_restart | exploitability | 0.133 | 0.053 | +0.080 | 0.99 | 0.024* |
| japan_intern_training_reform | cooperation_rate | 0.173 | 0.149 | +0.024 | 0.14 | 0.773 |
| japan_intern_training_reform | rationality_score | 0.557 | 0.534 | +0.022 | 1.52 | 0.022* |
| japan_intern_training_reform | exploitability | 0.096 | 0.050 | +0.046 | 0.41 | 0.409 |

## 5. Phase-Level Dynamics

| Phase | engine_structural Coop% | naive Coop% | engine_structural Defect% | naive Defect% |
|-------|-------|-------|-------|-------|
| OPENING | 23.6% | 26.4% | 44.1% | 23.2% |
| NEGOTIATION | 52.5% | 19.9% | 19.0% | 29.1% |
| CLOSING | 69.7% | 30.7% | 10.0% | 22.6% |
| TENSION | 17.0% | 24.8% | 44.5% | 25.7% |

## 6. Aggregate Statistical Tests

### Welch t-test + Cohen's d (Engine vs Naive)

| Metric | t-stat | p-value | Cohen's d | Significant? |
|--------|--------|---------|-----------|-------------|
| cooperation_rate | 3.505 | 0.0006 | 0.522 | Yes |
| conditional_cooperation_rate | -1.512 | 0.1323 | -0.226 | No |
| rationality_score | 0.390 | 0.6972 | 0.058 | No |
| exploitability | 2.853 | 0.0048 | 0.424 | Yes |

### Rational Strategy Proportion (Z-test)

- Engine: 115/1384 = 8.3%
- Naive: 252/1164 = 21.6%
- z = -9.553, p = 0.0000 (Yes)
