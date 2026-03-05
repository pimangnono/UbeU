# Behavioral Fidelity Experiment Report

Generated: 2026-03-04 21:17

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.5275* | 0.0 | 0.2178 | 104 |
| Conscientiousness | 0.6313* | 0.0 | 0.1316 | 104 |
| Extraversion | 0.8508* | 0.0 | 0.1132 | 104 |
| Agreeableness | 0.8078* | 0.0 | 0.1692 | 104 |
| Neuroticism | 0.7517* | 0.0 | 0.2156 | 104 |

**Overall mean r:** 0.7138
**Overall mean MAE:** 0.1695

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.0841 |
| Conscientiousness | insufficient multi-rep data | - | 0.1026 |
| Extraversion | insufficient multi-rep data | - | 0.0709 |
| Agreeableness | insufficient multi-rep data | - | 0.0741 |
| Neuroticism | insufficient multi-rep data | - | 0.1042 |

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
| Openness | 0.0 | 0.25 | 11 | Yes (40%) |
| Conscientiousness | 0.04 | 0.2125 | 21 | Yes (27%) |
| Extraversion | 0.03 | 0.275 | 22 | Yes (46%) |
| Agreeableness | 0.0 | 0.165 | 40 | No |
| Neuroticism | 0.0 | 0.125 | 28 | Yes (21%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion, Neuroticism

**Total sessions analyzed:** 124

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.7511 | 0.0 | positive | Yes |
| Disagreements -> -Agreeableness | -0.0952 | 0.336265 | negative | Yes |
| Acknowledgments -> Agreeableness | 0.1902 | 0.053179 | positive | Yes |
| New ideas -> Openness | 0.318 | 0.001004 | positive | Yes |
| Questions asked -> Extraversion | 0.0431 | 0.663787 | positive | Yes |
| Name mentions -> Extraversion | 0.6772 | 0.0 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.4544 | 1e-06 | 0.5275 | 0.0966 | 104 |
| Conscientiousness | 0.5136 | 0.0 | 0.6313 | 0.4041 | 104 |
| Extraversion | 0.7386 | 0.0 | 0.8508 | 0.7787 | 104 |
| Agreeableness | 0.4689 | 1e-06 | 0.8078 | 0.4707 | 104 |
| Neuroticism | 0.3764 | 8.2e-05 | 0.7517 | 0.395 | 104 |

**Convergent validity: MODERATE** (mean r = 0.510)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Avg words -> E | 0.8794* | 0.0 | positive | Yes |
| Max words -> E | 0.7367* | 0.0 | positive | Yes |
| Negations -> -A | -0.6443* | 0.0 | negative | Yes |
| Name mentions -> E | 0.6438* | 0.0 | positive | Yes |
| Planning -> C | 0.4658* | 1e-06 | positive | Yes |
| Exclamation ratio -> E | 0.4477* | 2e-06 | positive | Yes |
| Positive emotion -> A | 0.3166* | 0.001059 | positive | Yes |
| Hedges -> N | 0.2903* | 0.002796 | positive | Yes |
| Emotional words -> N | 0.2845* | 0.00342 | positive | Yes |
| First-person -> N | 0.2662* | 0.006313 | positive | Yes |
| Word variance -> O | 0.2274* | 0.020243 | positive | Yes |
| Acknowledgments -> A | 0.1952* | 0.047028 | positive | Yes |
| Action items -> C | 0.1908 | 0.05238 | positive | Yes |
| Certainty -> E | 0.1586 | 0.107747 | positive | Yes |
| Ideas -> O | -0.1396 | 0.157428 | positive | No |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.1189 | 0.0141 | 0.0737 | 104 |
| Conscientiousness | 0.0966 | 0.0093 | 0.0387 | 104 |
| Extraversion | 0.1189 | 0.0141 | 0.0687 | 104 |
| Agreeableness | 0.0953 | 0.0091 | 0.0901 | 104 |
| Neuroticism | 0.105 | 0.011 | 0.0874 | 104 |

**Uncertain sessions (high inter-model variance):** 20

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.2136* | Yes | -0.0574 | -0.1561 |
| Conscientiousness | -0.0125 | No | -0.0822 | +0.0698 |
| Extraversion | +0.0427* | Yes | +0.1071 | -0.0644 |
| Agreeableness | +0.0983* | Yes | +0.0357 | +0.0626 |
| Neuroticism | -0.2066* | Yes | -0.1061 | -0.1004 |

**Significantly biased traits: Openness (-0.214), Neuroticism (-0.207), Agreeableness (+0.098), Extraversion (+0.043)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | strong | no_data | fragile | no_data | biased (-0.214) |
| Conscientiousness | strong | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | biased (+0.043) |
| Agreeableness | strong | no_data | moderate | no_data | biased (+0.098) |
| Neuroticism | strong | no_data | fragile | no_data | biased (-0.207) |

---

## BCFC Paired Analysis

Within-subject comparison: 52 matched profile-scenario pairs.

### RQ1: Overall Fidelity Improvement

| Metric | Baseline | BCFC | Delta |
|--------|----------|------|-------|
| Mean MAE | 0.1607 | 0.176 | -0.0153 |

Paired t-test: t=-2.351, p=0.022624*, Cohen's d=-0.326, N=52

### RQ2: Per-Trait Improvement

| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |
|-------|-----------|--------|---------|-------------|---------|-----------|---------|
| Openness | 0.5312 | 0.5017 | -0.0295 | 0.1969 | 0.2328 | -0.0359 | 0.014672* |
| Conscientiousness | 0.6354 | 0.535 | -0.1004 | 0.1356 | 0.1464 | -0.0109 | 0.467359 |
| Extraversion | 0.8626 | 0.8098 | -0.0528 | 0.1087 | 0.1201 | -0.0114 | 0.380896 |
| Agreeableness | 0.8539 | 0.8237 | -0.0302 | 0.1512 | 0.1618 | -0.0106 | 0.318492 |
| Neuroticism | 0.7561 | 0.7448 | -0.0113 | 0.2109 | 0.2188 | -0.0079 | 0.684735 |

### RQ4: Within-Profile Variance Reduction

| Trait | Baseline SD | BCFC SD | Reduction |
|-------|-----------|---------|-----------|
| Openness | 0.0803 | 0.078 | 0.0024 |
| Conscientiousness | 0.093 | 0.1001 | -0.0071 |
| Extraversion | 0.0639 | 0.0752 | -0.0113 |
| Agreeableness | 0.0611 | 0.0668 | -0.0057 |
| Neuroticism | 0.1005 | 0.1153 | -0.0148 |

---

## BCFC Ablation Analysis

Controller interventions across 60 BCFC sessions.

- Total nudges: 180
- Total regenerations: 114
- Mean nudge rate: 37.5%
- Mean regeneration rate: 23.7%

### Corrections by Trait

| Trait | Nudge Count | Violation Count |
|-------|------------|-----------------|
| Openness | 646 | 0 |
| Conscientiousness | 823 | 87 |
| Extraversion | 823 | 7 |
| Agreeableness | 541 | 20 |
| Neuroticism | 447 | 0 |

### Violation Types

| Type | Count |
|------|-------|
| no_organizational_element | 74 |
| agreed_without_concern | 20 |
| imposed_unsolicited_structure | 13 |
| response_too_long | 5 |
| no_name_mention | 2 |

---

## RQ5: BCFC Cost Overhead

N sessions: 60

| Metric | Mean | Median | Max |
|--------|------|--------|-----|
| Nudge rate | 0.375 | 0.375 | 0.375 |
| Regen rate | 0.237 | 0.125 | 1.125 |

**Estimated cost overhead: 23.8%** (PASS: < 50% threshold for <1.5x budget)

