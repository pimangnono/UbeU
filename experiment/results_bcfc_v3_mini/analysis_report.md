# Behavioral Fidelity Experiment Report

Generated: 2026-03-05 20:01

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | -0.0058 | 0.977129 | 0.232 | 27 |
| Conscientiousness | 0.1873 | 0.349583 | 0.2374 | 27 |
| Extraversion | -0.0767 | 0.703636 | 0.2037 | 27 |
| Agreeableness | -0.1813 | 0.365519 | 0.3252 | 27 |
| Neuroticism | -0.0468 | 0.816585 | 0.4385 | 27 |

**Overall mean r:** -0.0247
**Overall mean MAE:** 0.2874

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.124 |
| Conscientiousness | insufficient multi-rep data | - | 0.0891 |
| Extraversion | insufficient multi-rep data | - | 0.1193 |
| Agreeableness | insufficient multi-rep data | - | 0.1683 |
| Neuroticism | insufficient multi-rep data | - | 0.0151 |

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
| Openness | 0.0 | 0.4 | 6 | Yes (70%) |
| Conscientiousness | 0.05 | 0.225 | 7 | Yes (30%) |
| Extraversion | 0.03 | 0.41 | 1 | Yes (93%) |
| Agreeableness | 0.0 | 0.165 | 6 | No |
| Neuroticism | 0.0 | 0.1 | 0 | No |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion

**Total sessions analyzed:** 27

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.74 | 1e-05 | positive | Yes |
| Disagreements -> -Agreeableness | -0.4939 | 0.00883 | negative | Yes |
| Acknowledgments -> Agreeableness | 0.36 | 0.065085 | positive | Yes |
| New ideas -> Openness | 0.7806 | 2e-06 | positive | Yes |
| Questions asked -> Extraversion | 0.2272 | 0.254434 | positive | Yes |
| Name mentions -> Extraversion | 0.0467 | 0.816973 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.7342 | 1.3e-05 | -0.0058 | -0.0704 | 27 |
| Conscientiousness | 0.3251 | 0.098047 | 0.1873 | -0.0574 | 27 |
| Extraversion | 0.5551 | 0.00265 | -0.0767 | -0.2682 | 27 |
| Agreeableness | 0.4755 | 0.012194 | -0.1813 | -0.1137 | 27 |
| Neuroticism | 0.0688 | 0.732992 | -0.0468 | -0.0349 | 27 |

**Convergent validity: MODERATE** (mean r = 0.432)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Self-doubt -> N | nan | nan | positive | No |
| Apologies -> N | nan | nan | positive | No |
| Reassurance seeking -> N | nan | nan | positive | No |
| Hypotheticals -> O | nan | nan | positive | No |
| Name mentions -> E | -0.2688 | 0.175178 | positive | No |
| Acknowledgments -> A | -0.2665 | 0.179086 | positive | No |
| Structure markers -> C | 0.2621 | 0.186653 | positive | Yes |
| First-person -> N | -0.2528 | 0.203249 | positive | No |
| Inclusive pronouns -> A | -0.2317 | 0.244919 | positive | No |
| Question ratio -> E | -0.2055 | 0.303699 | positive | No |
| Turn initiation -> E | -0.1924 | 0.336398 | positive | No |
| Disagreements -> -A | -0.1454 | 0.469446 | negative | Yes |
| Long sentences -> C | -0.1249 | 0.534723 | positive | No |
| Avg words -> E | -0.1046 | 0.603625 | positive | No |
| Word variance -> O | -0.0934 | 0.643144 | positive | No |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.1409 | 0.0199 | 0.0376 | 27 |
| Conscientiousness | 0.0906 | 0.0082 | 0.0174 | 27 |
| Extraversion | 0.1438 | 0.0207 | 0.0357 | 27 |
| Agreeableness | 0.0916 | 0.0084 | 0.0526 | 27 |
| Neuroticism | 0.0388 | 0.0015 | 0.0046 | 27 |

**Uncertain sessions (high inter-model variance):** 2

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.1857* | Yes | -0.0954 | -0.0904 |
| Conscientiousness | +0.1033* | Yes | -0.0320 | +0.1353 |
| Extraversion | +0.1481* | Yes | +0.0274 | +0.1207 |
| Agreeableness | +0.2678* | Yes | +0.0889 | +0.1789 |
| Neuroticism | -0.4385* | Yes | -0.1959 | -0.2426 |

**Significantly biased traits: Neuroticism (-0.439), Agreeableness (+0.268), Openness (-0.186), Extraversion (+0.148), Conscientiousness (+0.103)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | weak | no_data | fragile | no_data | biased (-0.186) |
| Conscientiousness | weak | no_data | fragile | no_data | biased (+0.103) |
| Extraversion | weak | no_data | fragile | no_data | biased (+0.148) |
| Agreeableness | weak | no_data | moderate | no_data | biased (+0.268) |
| Neuroticism | weak | no_data | robust | no_data | biased (-0.439) |

---

## BCFC Paired Analysis

Within-subject comparison: 9 matched profile-scenario pairs.

### RQ1: Overall Fidelity Improvement

| Metric | Baseline | BCFC | Delta |
|--------|----------|------|-------|
| Mean MAE | 0.2888 | 0.275 | 0.0138 |

Paired t-test: t=1.0436, p=0.32718, Cohen's d=0.3479, N=9

### RQ2: Per-Trait Improvement

| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |
|-------|-----------|--------|---------|-------------|---------|-----------|---------|
| Openness | 0.0509 | 0.2149 | +0.1640 | 0.215 | 0.2444 | -0.0294 | 0.442932 |
| Conscientiousness | -0.0707 | 0.2857 | +0.3564 | 0.2433 | 0.225 | +0.0183 | 0.650604 |
| Extraversion | -0.5807 | 0.3347 | +0.9154 | 0.2556 | 0.1528 | +0.1028 | 0.035539* |
| Agreeableness | -0.0221 | -0.1441 | -0.1220 | 0.2894 | 0.3172 | -0.0278 | 0.526715 |
| Neuroticism | 0.3449 | -0.2722 | -0.6170 | 0.4406 | 0.4356 | +0.0050 | 0.49666 |

### RQ4: Within-Profile Variance Reduction

| Trait | Baseline SD | BCFC SD | Reduction |
|-------|-----------|---------|-----------|
| Openness | 0.1432 | 0.0605 | 0.0827 |
| Conscientiousness | 0.0512 | 0.116 | -0.0647 |
| Extraversion | 0.114 | 0.1198 | -0.0058 |
| Agreeableness | 0.1765 | 0.2017 | -0.0252 |
| Neuroticism | 0.0179 | 0.016 | 0.0018 |

---

## RQ5: BCFC Cost Overhead

N sessions: 18

| Metric | Mean | Median | Max |
|--------|------|--------|-----|
| Nudge rate | None | None | None |
| Regen rate | None | None | None |

**Mean session cost (USD): 0.0**

---

## Trajectory Continuity Metrics

| Metric | Baseline | BCFC |
|--------|----------|------|
| Avg Appropriateness | 0.9027 | 0.9057 |
| Avg Coherence | 0.9517 | 0.9658 |

