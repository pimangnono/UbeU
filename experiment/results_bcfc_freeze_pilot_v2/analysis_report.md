# Behavioral Fidelity Experiment Report

Generated: 2026-03-05 15:49

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.3105 | 0.549178 | 0.2833 | 6 |
| Conscientiousness | 0.6166 | 0.192331 | 0.1808 | 6 |
| Extraversion | 0.9368* | 0.005861 | 0.0875 | 6 |
| Agreeableness | 0.9022* | 0.01387 | 0.2008 | 6 |
| Neuroticism | 0.8857* | 0.018866 | 0.2117 | 6 |

**Overall mean r:** 0.7304
**Overall mean MAE:** 0.1928

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.0236 |
| Conscientiousness | insufficient multi-rep data | - | 0.0483 |
| Extraversion | insufficient multi-rep data | - | 0.0059 |
| Agreeableness | insufficient multi-rep data | - | 0.013 |
| Neuroticism | insufficient multi-rep data | - | 0.0542 |

---

## RQ3: Temporal Decay

Do personality signals weaken over the course of a session?

| Trait | t-stat | p-value | Cohen's d | r(early) | r(late) | Delta-r |
|-------|--------|---------|----------|----------|---------|---------|
| Openness | - | - | - | - | - | - |
| Conscientiousness | - | - | - | - | - | - |
| Extraversion | - | - | - | - | - | - |
| Agreeableness | - | - | - | - | - | - |
| Neuroticism | - | - | - | - | - | - |

**Caveat (Phase-Content Confound):** The Early/Peak/Late windows differ in both time AND conversational content (introduction vs. conflict vs. resolution). Changes in personality signals across windows may reflect phase-appropriate behavior shifts rather than pure temporal decay. These results should be interpreted as *phase-specific fidelity* rather than *temporal decay* in the strict sense. See Section 4.3 of the research design for full discussion.

---

## Judge Order-Bias Analysis

Per-trait diagnostics from dual-order evaluation (Order A: transcript→features, B: features→transcript).

| Trait | Order Effect | Model Range | Parse Errors | Uncertain? |
|-------|-------------|-------------|-------------|-----------|
| Openness | 0.05 | 0.2875 | 0 | Yes (50%) |
| Conscientiousness | 0.07 | 0.275 | 2 | Yes (33%) |
| Extraversion | 0.0 | 0.2475 | 0 | Yes (33%) |
| Agreeableness | 0.0 | 0.14 | 0 | No |
| Neuroticism | 0.0 | 0.1725 | 1 | Yes (17%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion, Neuroticism

**Total sessions analyzed:** 6

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.9064 | 0.012742 | positive | Yes |
| Disagreements -> -Agreeableness | -0.8636 | 0.026636 | negative | Yes |
| Acknowledgments -> Agreeableness | 0.0284 | 0.957423 | positive | Yes |
| New ideas -> Openness | 0.0598 | 0.910465 | positive | Yes |
| Questions asked -> Extraversion | 0.0436 | 0.934637 | positive | Yes |
| Name mentions -> Extraversion | 0.0399 | 0.940173 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.0635 | 0.904817 | 0.3105 | 0.4282 | 6 |
| Conscientiousness | 0.8954 | 0.015841 | 0.6166 | 0.3339 | 6 |
| Extraversion | 0.8524 | 0.031055 | 0.9368 | 0.6282 | 6 |
| Agreeableness | 0.8948 | 0.016025 | 0.9022 | 0.7938 | 6 |
| Neuroticism | 0.8947 | 0.016035 | 0.8857 | 0.9501 | 6 |

**Convergent validity: STRONG** (mean r = 0.720)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Reference back -> C | nan | nan | positive | No |
| First-person -> N | 0.92* | 0.009353 | positive | Yes |
| Word variance -> O | 0.8973* | 0.015291 | positive | Yes |
| Hypotheticals -> O | nan | nan | positive | No |
| Positive emotion -> A | nan | nan | positive | No |
| Apologies -> N | nan | nan | positive | No |
| Reassurance seeking -> N | nan | nan | positive | No |
| Hedges -> N | 0.9342* | 0.006359 | positive | Yes |
| Structure markers -> C | nan | nan | positive | No |
| Avg words -> E | 0.9066* | 0.012665 | positive | Yes |
| Max words -> E | 0.8285* | 0.041616 | positive | Yes |
| Long sentences -> C | -0.8225* | 0.04448 | positive | No |
| Exclamation ratio -> E | 0.8018 | 0.055041 | positive | Yes |
| Negations -> -A | -0.7452 | 0.089137 | negative | Yes |
| Disagreements -> -A | -0.7385 | 0.093599 | negative | Yes |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.1384 | 0.0191 | 0.0606 | 6 |
| Conscientiousness | 0.1132 | 0.0128 | 0.0391 | 6 |
| Extraversion | 0.0983 | 0.0097 | 0.0194 | 6 |
| Agreeableness | 0.063 | 0.004 | 0.0095 | 6 |
| Neuroticism | 0.1057 | 0.0112 | 0.0482 | 6 |

**Uncertain sessions (high inter-model variance):** 2

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.2833* | Yes | -0.1355 | -0.1478 |
| Conscientiousness | -0.0575 | No | -0.0691 | +0.0116 |
| Extraversion | +0.0208 | No | +0.1158 | -0.0949 |
| Agreeableness | +0.0908 | No | +0.0347 | +0.0561 |
| Neuroticism | -0.2117* | Yes | -0.1830 | -0.0287 |

**Significantly biased traits: Openness (-0.283), Neuroticism (-0.212)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | weak | no_data | fragile | no_data | biased (-0.283) |
| Conscientiousness | weak | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | unbiased |
| Agreeableness | strong | no_data | robust | no_data | unbiased |
| Neuroticism | strong | no_data | moderate | no_data | biased (-0.212) |

---

## BCFC Paired Analysis

Within-subject comparison: 3 matched profile-scenario pairs.

### RQ1: Overall Fidelity Improvement

| Metric | Baseline | BCFC | Delta |
|--------|----------|------|-------|
| Mean MAE | 0.188 | 0.1977 | -0.0097 |

Paired t-test: t=-0.6511, p=0.581813, Cohen's d=-0.3759, N=3

### RQ2: Per-Trait Improvement

| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |
|-------|-----------|--------|---------|-------------|---------|-----------|---------|
| Openness | 0.189 | 0.6547 | +0.4657 | 0.3 | 0.2667 | +0.0333 | 0.183503 |
| Conscientiousness | 0.6698 | 0.6169 | -0.0530 | 0.1633 | 0.1983 | -0.0350 | 0.05612 |
| Extraversion | 0.9387 | 0.9359 | -0.0028 | 0.0833 | 0.0917 | -0.0083 | 0.42265 |
| Agreeableness | 0.895 | 0.9107 | +0.0156 | 0.21 | 0.1917 | +0.0183 | 0.186857 |
| Neuroticism | 0.7963 | 0.982 | +0.1857 | 0.1833 | 0.24 | -0.0567 | 0.514682 |

### RQ4: Within-Profile Variance Reduction

| Trait | Baseline SD | BCFC SD | Reduction |
|-------|-----------|---------|-----------|
| Openness | - | - | insufficient profile data |
| Conscientiousness | - | - | insufficient profile data |
| Extraversion | - | - | insufficient profile data |
| Agreeableness | - | - | insufficient profile data |
| Neuroticism | - | - | insufficient profile data |

---

## BCFC Ablation Analysis

Controller interventions across 3 BCFC sessions.

- Total nudges: 9
- Total regenerations: 0
- Mean nudge rate: 37.5%
- Mean regeneration rate: 0.0%

### Corrections by Trait

| Trait | Nudge Count | Violation Count |
|-------|------------|-----------------|
| Openness | 34 | 0 |
| Conscientiousness | 32 | 0 |
| Extraversion | 38 | 0 |
| Agreeableness | 23 | 0 |
| Neuroticism | 22 | 0 |

---

## RQ5: BCFC Cost Overhead

N sessions: 3

| Metric | Mean | Median | Max |
|--------|------|--------|-----|
| Nudge rate | 0.375 | 0.375 | 0.375 |
| Regen rate | 0.0 | 0.0 | 0.0 |

**Estimated cost overhead: 0.0%** (PASS: < 50% threshold for <1.5x budget)
**Mean session cost (USD): 0.0**

---

## BoN Pool Ablation (Offline)

Pools analyzed: 24

| Policy | Contract Distance (avg) | Adequacy Penalty (avg) |
|--------|--------------------------|------------------------|
| full_score | 0.6313 | 0.0 |
| contract_only | 0.628 | 0.0 |
| relevance_only | 0.7056 | 0.0292 |
| first | 0.7047 | 0.0375 |
| random_expected | 0.7009 | 0.0187 |

---

## Trajectory Continuity Metrics

| Metric | Baseline | BCFC |
|--------|----------|------|
| Avg Appropriateness | 0.6775 | 0.73 |
| Avg Coherence | 0.8696 | 0.8763 |

