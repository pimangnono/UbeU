# Behavioral Fidelity Experiment Report

Generated: 2026-03-05 13:54

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.5059 | 0.305875 | 0.1975 | 6 |
| Conscientiousness | 0.4901 | 0.323767 | 0.1867 | 6 |
| Extraversion | 0.9287* | 0.007435 | 0.0625 | 6 |
| Agreeableness | 0.9291* | 0.00736 | 0.1508 | 6 |
| Neuroticism | 0.8193* | 0.046023 | 0.2142 | 6 |

**Overall mean r:** 0.7346
**Overall mean MAE:** 0.1623

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.1685 |
| Conscientiousness | insufficient multi-rep data | - | 0.0401 |
| Extraversion | insufficient multi-rep data | - | 0.0884 |
| Agreeableness | insufficient multi-rep data | - | 0.1049 |
| Neuroticism | insufficient multi-rep data | - | 0.0907 |

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
| Openness | 0.0 | 0.1675 | 0 | Yes (33%) |
| Conscientiousness | 0.05 | 0.2775 | 2 | Yes (33%) |
| Extraversion | 0.03 | 0.22 | 1 | Yes (33%) |
| Agreeableness | 0.0 | 0.2075 | 1 | No |
| Neuroticism | 0.0 | 0.175 | 1 | Yes (33%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion, Neuroticism

**Total sessions analyzed:** 6

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.9358 | 0.006058 | positive | Yes |
| Disagreements -> -Agreeableness | -0.1952 | 0.710989 | negative | Yes |
| Acknowledgments -> Agreeableness | -0.0928 | 0.861146 | positive | No |
| New ideas -> Openness | 0.1438 | 0.785739 | positive | Yes |
| Questions asked -> Extraversion | -0.6466 | 0.165252 | positive | No |
| Name mentions -> Extraversion | 0.4768 | 0.339014 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | -0.0742 | 0.888915 | 0.5059 | -0.4177 | 6 |
| Conscientiousness | 0.7116 | 0.112792 | 0.4901 | 0.8353 | 6 |
| Extraversion | 0.8382 | 0.037165 | 0.9287 | 0.7228 | 6 |
| Agreeableness | 0.2098 | 0.68989 | 0.9291 | 0.1902 | 6 |
| Neuroticism | 0.9006 | 0.014316 | 0.8193 | 0.8783 | 6 |

**Convergent validity: MODERATE** (mean r = 0.517)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Hypotheticals -> O | nan | nan | positive | No |
| Avg words -> E | 0.9644* | 0.001874 | positive | Yes |
| Hedges -> N | 0.9363* | 0.005965 | positive | Yes |
| Negations -> -A | -0.9117* | 0.011358 | negative | Yes |
| Max words -> E | 0.8102 | 0.050608 | positive | Yes |
| Word variance -> O | 0.7653 | 0.076183 | positive | Yes |
| Reference back -> C | nan | nan | positive | No |
| Apologies -> N | nan | nan | positive | No |
| Reassurance seeking -> N | nan | nan | positive | No |
| Positive emotion -> A | nan | nan | positive | No |
| Structure markers -> C | nan | nan | positive | No |
| Conditionals -> C | 0.933* | 0.006576 | positive | Yes |
| Question ratio -> E | -0.7778 | 0.068564 | positive | No |
| Planning -> C | 0.7291 | 0.100131 | positive | Yes |
| Name mentions -> E | 0.6911 | 0.128384 | positive | Yes |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.1268 | 0.0161 | 0.0671 | 6 |
| Conscientiousness | 0.1017 | 0.0103 | 0.0226 | 6 |
| Extraversion | 0.1248 | 0.0156 | 0.0619 | 6 |
| Agreeableness | 0.0736 | 0.0054 | 0.0092 | 6 |
| Neuroticism | 0.1148 | 0.0132 | 0.0453 | 6 |

**Uncertain sessions (high inter-model variance):** 2

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.1975 | No | -0.1554 | -0.0421 |
| Conscientiousness | -0.0533 | No | -0.0722 | +0.0188 |
| Extraversion | -0.0042 | No | +0.0836 | -0.0877 |
| Agreeableness | +0.0408 | No | +0.0513 | -0.0105 |
| Neuroticism | -0.1808* | Yes | -0.2009 | +0.0201 |

**Significantly biased traits: Neuroticism (-0.181)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | weak | no_data | fragile | no_data | unbiased |
| Conscientiousness | weak | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | unbiased |
| Agreeableness | strong | no_data | robust | no_data | unbiased |
| Neuroticism | strong | no_data | fragile | no_data | biased (-0.181) |

---

## BCFC Paired Analysis

Within-subject comparison: 3 matched profile-scenario pairs.

### RQ1: Overall Fidelity Improvement

| Metric | Baseline | BCFC | Delta |
|--------|----------|------|-------|
| Mean MAE | 0.1773 | 0.1473 | 0.03 |

Paired t-test: t=0.6751, p=0.569225, Cohen's d=0.3897, N=3

### RQ2: Per-Trait Improvement

| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |
|-------|-----------|--------|---------|-------------|---------|-----------|---------|
| Openness | -0.982 | 0.9866 | +1.9686 | 0.3167 | 0.0783 | +0.2383 | 0.318328 |
| Conscientiousness | 0.3764 | 0.6043 | +0.2279 | 0.2083 | 0.165 | +0.0433 | 0.204413 |
| Extraversion | 0.9897 | 0.9359 | -0.0539 | 0.0333 | 0.0917 | -0.0583 | 0.397536 |
| Agreeableness | 0.9993 | 0.9154 | -0.0839 | 0.1333 | 0.1683 | -0.0350 | 0.762268 |
| Neuroticism | 0.6986 | 0.982 | +0.2834 | 0.195 | 0.2333 | -0.0383 | 0.433264 |

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
| Openness | 38 | 0 |
| Conscientiousness | 40 | 1 |
| Extraversion | 40 | 1 |
| Agreeableness | 23 | 2 |
| Neuroticism | 22 | 0 |

### Violation Types

| Type | Count |
|------|-------|
| agreed_without_concern | 2 |
| imposed_unsolicited_structure | 1 |
| no_name_mention | 1 |

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
| full_score | 3347.2607 | 0.0333 |
| contract_only | 3347.2587 | 0.0417 |
| relevance_only | 8902.9395 | 0.0333 |
| first | 6125.153 | 0.0333 |
| random_expected | 6819.5998 | 0.0438 |

---

## Trajectory Continuity Metrics

| Metric | Baseline | BCFC |
|--------|----------|------|
| Avg Appropriateness | 0.6908 | 0.6988 |
| Avg Coherence | 0.8713 | 0.8454 |

