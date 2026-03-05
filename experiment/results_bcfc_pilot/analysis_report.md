# Behavioral Fidelity Experiment Report

Generated: 2026-03-04 13:57

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.5972* | 0.014586 | 0.2369 | 16 |
| Conscientiousness | 0.3057 | 0.2496 | 0.2191 | 16 |
| Extraversion | 0.9326* | 0.0 | 0.0866 | 16 |
| Agreeableness | 0.8656* | 1.5e-05 | 0.1481 | 16 |
| Neuroticism | 0.8408* | 4.5e-05 | 0.1659 | 16 |

**Overall mean r:** 0.7084
**Overall mean MAE:** 0.1713

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.1194 |
| Conscientiousness | insufficient multi-rep data | - | 0.1389 |
| Extraversion | insufficient multi-rep data | - | 0.0473 |
| Agreeableness | insufficient multi-rep data | - | 0.0982 |
| Neuroticism | insufficient multi-rep data | - | 0.1233 |

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
| Openness | 0.0 | 0.175 | 1 | Yes (19%) |
| Conscientiousness | 0.01 | 0.215 | 1 | Yes (38%) |
| Extraversion | 0.0 | 0.16 | 3 | Yes (25%) |
| Agreeableness | 0.0 | 0.195 | 7 | Yes (19%) |
| Neuroticism | 0.0 | 0.2875 | 6 | Yes (50%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism

**Total sessions analyzed:** 16

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.9313 | 0.0 | positive | Yes |
| Disagreements -> -Agreeableness | -0.1554 | 0.565386 | negative | Yes |
| Acknowledgments -> Agreeableness | 0.5136 | 0.041878 | positive | Yes |
| New ideas -> Openness | 0.1981 | 0.462034 | positive | Yes |
| Questions asked -> Extraversion | -0.2173 | 0.418893 | positive | No |
| Name mentions -> Extraversion | 0.7994 | 0.000202 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.56 | 0.024079 | 0.5972 | 0.1688 | 16 |
| Conscientiousness | 0.0653 | 0.810048 | 0.3057 | 0.4143 | 16 |
| Extraversion | 0.84 | 4.7e-05 | 0.9326 | 0.7038 | 16 |
| Agreeableness | 0.5359 | 0.032378 | 0.8656 | 0.4614 | 16 |
| Neuroticism | 0.6014 | 0.013731 | 0.8408 | 0.7105 | 16 |

**Convergent validity: MODERATE** (mean r = 0.521)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Apologies -> N | nan | nan | positive | No |
| Avg words -> E | 0.8913* | 4e-06 | positive | Yes |
| Name mentions -> E | 0.8711* | 1.1e-05 | positive | Yes |
| Self-doubt -> N | nan | nan | positive | No |
| Hypotheticals -> O | nan | nan | positive | No |
| Max words -> E | 0.781* | 0.000354 | positive | Yes |
| Hedges -> N | 0.6767* | 0.003993 | positive | Yes |
| Acknowledgments -> A | 0.5832* | 0.017724 | positive | Yes |
| Action items -> C | -0.5721* | 0.020569 | positive | No |
| Conditionals -> C | 0.5673* | 0.021915 | positive | Yes |
| Negations -> -A | -0.5309* | 0.03434 | negative | Yes |
| Inclusive pronouns -> A | 0.4836 | 0.057742 | positive | Yes |
| Word variance -> O | 0.3865 | 0.139249 | positive | Yes |
| Planning -> C | 0.3738 | 0.153743 | positive | Yes |
| Question ratio -> E | -0.325 | 0.219292 | positive | No |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.1068 | 0.0114 | 0.0672 | 16 |
| Conscientiousness | 0.0957 | 0.0091 | 0.0261 | 16 |
| Extraversion | 0.1089 | 0.0119 | 0.0889 | 16 |
| Agreeableness | 0.1244 | 0.0155 | 0.077 | 16 |
| Neuroticism | 0.138 | 0.019 | 0.0561 | 16 |

**Uncertain sessions (high inter-model variance):** 7

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.2369* | Yes | -0.0977 | -0.1391 |
| Conscientiousness | -0.0878 | No | -0.1029 | +0.0151 |
| Extraversion | +0.0134 | No | +0.0895 | -0.0760 |
| Agreeableness | +0.0425 | No | +0.1358 | -0.0933 |
| Neuroticism | -0.1134* | Yes | -0.1869 | +0.0735 |

**Significantly biased traits: Openness (-0.237), Neuroticism (-0.113)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | strong | no_data | moderate | no_data | biased (-0.237) |
| Conscientiousness | weak | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | unbiased |
| Agreeableness | strong | no_data | moderate | no_data | unbiased |
| Neuroticism | strong | no_data | fragile | no_data | biased (-0.113) |

---

## BCFC Paired Analysis

Within-subject comparison: 8 matched profile-scenario pairs.

### RQ1: Overall Fidelity Improvement

| Metric | Baseline | BCFC | Delta |
|--------|----------|------|-------|
| Mean MAE | 0.185 | 0.1576 | 0.0274 |

Paired t-test: t=1.3667, p=0.213981, Cohen's d=0.4832, N=8

### RQ2: Per-Trait Improvement

| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |
|-------|-----------|--------|---------|-------------|---------|-----------|---------|
| Openness | 0.4817 | 0.7144 | +0.2327 | 0.2469 | 0.2269 | +0.0200 | 0.496966 |
| Conscientiousness | 0.0831 | 0.5088 | +0.4257 | 0.2519 | 0.1862 | +0.0656 | 0.217229 |
| Extraversion | 0.9177 | 0.9479 | +0.0302 | 0.1063 | 0.0669 | +0.0394 | 0.133091 |
| Agreeableness | 0.8674 | 0.8678 | +0.0004 | 0.1325 | 0.1638 | -0.0312 | 0.012047* |
| Neuroticism | 0.7755 | 0.917 | +0.1415 | 0.1875 | 0.1444 | +0.0431 | 0.471937 |

### RQ4: Within-Profile Variance Reduction

| Trait | Baseline SD | BCFC SD | Reduction |
|-------|-----------|---------|-----------|
| Openness | 0.1458 | 0.1264 | 0.0194 |
| Conscientiousness | 0.1618 | 0.099 | 0.0628 |
| Extraversion | 0.0619 | 0.0062 | 0.0557 |
| Agreeableness | 0.1078 | 0.1078 | 0.0 |
| Neuroticism | 0.1679 | 0.1052 | 0.0628 |

---

## BCFC Ablation Analysis

Controller interventions across 8 BCFC sessions.

- Total nudges: 24
- Total regenerations: 31
- Mean nudge rate: 37.5%
- Mean regeneration rate: 48.4%

### Corrections by Trait

| Trait | Nudge Count | Violation Count |
|-------|------------|-----------------|
| Openness | 76 | 0 |
| Conscientiousness | 104 | 21 |
| Extraversion | 104 | 8 |
| Agreeableness | 65 | 0 |
| Neuroticism | 65 | 2 |

### Violation Types

| Type | Count |
|------|-------|
| no_organizational_element | 18 |
| no_name_mention | 5 |
| response_too_long | 3 |
| imposed_unsolicited_structure | 3 |
| no_hedge_under_pressure | 2 |

---

## RQ5: BCFC Cost Overhead

N sessions: 8

| Metric | Mean | Median | Max |
|--------|------|--------|-----|
| Nudge rate | 0.375 | 0.375 | 0.375 |
| Regen rate | 0.484 | 0.25 | 1.125 |

**Estimated cost overhead: 48.4%** (PASS: < 50% threshold for <1.5x budget)

