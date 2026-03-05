# Behavioral Fidelity Experiment Report

Generated: 2026-03-04 11:49

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.6908 | 0.057837 | 0.1813 | 8 |
| Conscientiousness | 0.2545 | 0.543024 | 0.2056 | 8 |
| Extraversion | 0.9789* | 2.3e-05 | 0.0594 | 8 |
| Agreeableness | 0.8693* | 0.005051 | 0.1212 | 8 |
| Neuroticism | 0.9076* | 0.001839 | 0.1138 | 8 |

**Overall mean r:** 0.7402
**Overall mean MAE:** 0.1362

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.0265 |
| Conscientiousness | insufficient multi-rep data | - | 0.0698 |
| Extraversion | insufficient multi-rep data | - | 0.0398 |
| Agreeableness | insufficient multi-rep data | - | 0.0654 |
| Neuroticism | insufficient multi-rep data | - | 0.053 |

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
| Openness | 0.0 | 0.1425 | 0 | No |
| Conscientiousness | 0.025 | 0.2375 | 2 | Yes (25%) |
| Extraversion | 0.045 | 0.23 | 2 | Yes (50%) |
| Agreeableness | 0.0 | 0.215 | 3 | Yes (42%) |
| Neuroticism | 0.015 | 0.15 | 1 | Yes (25%) |

**Uncertain traits (>15% sessions):** Conscientiousness, Extraversion, Agreeableness, Neuroticism

**Total sessions analyzed:** 12

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.8741 | 0.004531 | positive | Yes |
| Disagreements -> -Agreeableness | 0.3602 | 0.380781 | negative | No |
| Acknowledgments -> Agreeableness | 0.2897 | 0.486428 | positive | Yes |
| New ideas -> Openness | 0.2997 | 0.470783 | positive | Yes |
| Questions asked -> Extraversion | -0.5741 | 0.136659 | positive | No |
| Name mentions -> Extraversion | 0.8338 | 0.010099 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.8071 | 0.01545 | 0.6908 | 0.2957 | 8 |
| Conscientiousness | -0.1127 | 0.790476 | 0.2545 | 0.5743 | 8 |
| Extraversion | 0.8171 | 0.013274 | 0.9789 | 0.8188 | 8 |
| Agreeableness | 0.6011 | 0.11496 | 0.8693 | 0.2631 | 8 |
| Neuroticism | 0.7221 | 0.043106 | 0.9076 | 0.4697 | 8 |

**Convergent validity: MODERATE** (mean r = 0.567)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Avg words -> E | 0.8547* | 0.006863 | positive | Yes |
| Max words -> E | 0.6714 | 0.06827 | positive | Yes |
| Question ratio -> E | -0.5209 | 0.185615 | positive | No |
| Reassurance seeking -> N | nan | nan | positive | No |
| Name mentions -> E | 0.7998* | 0.017157 | positive | Yes |
| Unique words -> O | -0.5118 | 0.194785 | positive | No |
| Inclusive pronouns -> A | 0.4881 | 0.219771 | positive | Yes |
| Ideas -> O | -0.4041 | 0.320763 | positive | No |
| Apologies -> N | nan | nan | positive | No |
| Disagreements -> -A | 0.5447 | 0.162716 | negative | No |
| Planning -> C | 0.5098 | 0.196882 | positive | Yes |
| Hedges -> N | 0.4972 | 0.209976 | positive | Yes |
| Long sentences -> C | 0.4371 | 0.278887 | positive | Yes |
| Exclamation ratio -> E | 0.3961 | 0.331393 | positive | Yes |
| Turn initiation -> E | 0.3859 | 0.34506 | positive | Yes |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.0563 | 0.0032 | 0.0055 | 8 |
| Conscientiousness | 0.1017 | 0.0104 | 0.0258 | 8 |
| Extraversion | 0.1122 | 0.0126 | 0.0571 | 8 |
| Agreeableness | 0.1189 | 0.0141 | 0.0413 | 8 |
| Neuroticism | 0.1522 | 0.0232 | 0.0892 | 8 |

**Uncertain sessions (high inter-model variance):** 3

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.1813* | Yes | +0.0166 | -0.1979 |
| Conscientiousness | -0.0519 | No | -0.1046 | +0.0527 |
| Extraversion | -0.0219 | No | +0.1695 | -0.1914 |
| Agreeableness | +0.1162 | No | +0.0017 | +0.1145 |
| Neuroticism | -0.0825 | No | -0.2469 | +0.1644 |

**Significantly biased traits: Openness (-0.181)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | weak | no_data | robust | no_data | biased (-0.181) |
| Conscientiousness | weak | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | unbiased |
| Agreeableness | strong | no_data | fragile | no_data | unbiased |
| Neuroticism | strong | no_data | fragile | no_data | unbiased |
