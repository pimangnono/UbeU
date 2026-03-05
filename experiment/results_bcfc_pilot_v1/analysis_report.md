# Behavioral Fidelity Experiment Report

Generated: 2026-03-04 12:51

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.8094* | 0.000257 | 0.1827 | 15 |
| Conscientiousness | 0.7795* | 0.000611 | 0.1293 | 15 |
| Extraversion | 0.9197* | 1e-06 | 0.0943 | 15 |
| Agreeableness | 0.8651* | 3.1e-05 | 0.1517 | 15 |
| Neuroticism | 0.6433* | 0.009673 | 0.2523 | 15 |

**Overall mean r:** 0.8034
**Overall mean MAE:** 0.1621

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.103 |
| Conscientiousness | insufficient multi-rep data | - | 0.0672 |
| Extraversion | insufficient multi-rep data | - | 0.0586 |
| Agreeableness | insufficient multi-rep data | - | 0.0976 |
| Neuroticism | insufficient multi-rep data | - | 0.1777 |

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
| Openness | 0.0 | 0.175 | 2 | Yes (20%) |
| Conscientiousness | 0.03 | 0.25 | 5 | Yes (33%) |
| Extraversion | 0.0 | 0.205 | 3 | No |
| Agreeableness | 0.0 | 0.15 | 3 | No |
| Neuroticism | 0.0 | 0.19 | 4 | Yes (40%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Neuroticism

**Total sessions analyzed:** 15

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.9052 | 3e-06 | positive | Yes |
| Disagreements -> -Agreeableness | -0.0355 | 0.900105 | negative | Yes |
| Acknowledgments -> Agreeableness | 0.7948 | 0.000399 | positive | Yes |
| New ideas -> Openness | -0.2371 | 0.39493 | positive | No |
| Questions asked -> Extraversion | 0.1011 | 0.719945 | positive | Yes |
| Name mentions -> Extraversion | 0.7011 | 0.003594 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.2837 | 0.305434 | 0.8094 | 0.3916 | 15 |
| Conscientiousness | 0.6019 | 0.017599 | 0.7795 | 0.8431 | 15 |
| Extraversion | 0.864 | 3.3e-05 | 0.9197 | 0.8466 | 15 |
| Agreeableness | 0.7946 | 0.000401 | 0.8651 | 0.6843 | 15 |
| Neuroticism | 0.4728 | 0.07512 | 0.6433 | 0.7105 | 15 |

**Convergent validity: STRONG** (mean r = 0.603)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Self-doubt -> N | nan | nan | positive | No |
| Avg words -> E | 0.971* | 0.0 | positive | Yes |
| Reassurance seeking -> N | nan | nan | positive | No |
| Name mentions -> E | 0.845* | 7.3e-05 | positive | Yes |
| Planning -> C | 0.7535* | 0.001179 | positive | Yes |
| Max words -> E | 0.7444* | 0.001457 | positive | Yes |
| Acknowledgments -> A | 0.7031* | 0.003453 | positive | Yes |
| Hedges -> N | 0.6954* | 0.003998 | positive | Yes |
| Conditionals -> C | 0.6732* | 0.005948 | positive | Yes |
| Inclusive pronouns -> A | 0.6702* | 0.006254 | positive | Yes |
| Negations -> -A | -0.6365* | 0.010733 | negative | Yes |
| First-person -> N | 0.4228 | 0.116423 | positive | Yes |
| Exclamation ratio -> E | 0.3677 | 0.177595 | positive | Yes |
| Ideas -> O | -0.3192 | 0.246132 | positive | No |
| Word variance -> O | 0.2854 | 0.302436 | positive | Yes |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.1276 | 0.0163 | 0.0779 | 15 |
| Conscientiousness | 0.0927 | 0.0086 | 0.0211 | 15 |
| Extraversion | 0.0853 | 0.0073 | 0.0321 | 15 |
| Agreeableness | 0.0652 | 0.0043 | 0.0195 | 15 |
| Neuroticism | 0.1339 | 0.0179 | 0.0884 | 15 |

**Uncertain sessions (high inter-model variance):** 3

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.1827* | Yes | -0.1044 | -0.0783 |
| Conscientiousness | -0.0787 | No | -0.1162 | +0.0375 |
| Extraversion | +0.0310 | No | +0.1031 | -0.0721 |
| Agreeableness | +0.0317 | No | +0.1229 | -0.0912 |
| Neuroticism | -0.2123* | Yes | -0.2095 | -0.0028 |

**Significantly biased traits: Neuroticism (-0.212), Openness (-0.183)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | strong | no_data | fragile | no_data | biased (-0.183) |
| Conscientiousness | strong | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | moderate | no_data | unbiased |
| Agreeableness | strong | no_data | robust | no_data | unbiased |
| Neuroticism | strong | no_data | fragile | no_data | biased (-0.212) |

---

## BCFC Paired Analysis

Within-subject comparison: 7 matched profile-scenario pairs.

### RQ1: Overall Fidelity Improvement

| Metric | Baseline | BCFC | Delta |
|--------|----------|------|-------|
| Mean MAE | 0.1489 | 0.1784 | -0.0296 |

Paired t-test: t=-1.2408, p=0.260976, Cohen's d=-0.469, N=7

### RQ2: Per-Trait Improvement

| Trait | Baseline r | BCFC r | Delta r | Baseline MAE | BCFC MAE | Delta MAE | p-value |
|-------|-----------|--------|---------|-------------|---------|-----------|---------|
| Openness | 0.9753 | 0.6851 | -0.2902 | 0.1414 | 0.1929 | -0.0514 | 0.568171 |
| Conscientiousness | 0.6539 | 0.8937 | +0.2398 | 0.1664 | 0.1036 | +0.0629 | 0.114413 |
| Extraversion | 0.9464 | 0.8962 | -0.0502 | 0.0771 | 0.1143 | -0.0371 | 0.288241 |
| Agreeableness | 0.8578 | 0.8891 | +0.0313 | 0.1736 | 0.1371 | +0.0364 | 0.099772 |
| Neuroticism | 0.742 | 0.6761 | -0.0659 | 0.1857 | 0.3443 | -0.1586 | 0.164952 |

### RQ4: Within-Profile Variance Reduction

| Trait | Baseline SD | BCFC SD | Reduction |
|-------|-----------|---------|-----------|
| Openness | 0.0177 | 0.165 | -0.1473 |
| Conscientiousness | 0.0707 | 0.0471 | 0.0236 |
| Extraversion | 0.033 | 0.0471 | -0.0141 |
| Agreeableness | 0.0247 | 0.0212 | 0.0035 |
| Neuroticism | 0.1827 | 0.1461 | 0.0365 |

---

## BCFC Ablation Analysis

Controller interventions across 7 BCFC sessions.

- Total nudges: 21
- Total regenerations: 72
- Mean nudge rate: 37.5%
- Mean regeneration rate: 128.6%

### Corrections by Trait

| Trait | Nudge Count | Violation Count |
|-------|------------|-----------------|
| Openness | 69 | 0 |
| Conscientiousness | 84 | 38 |
| Extraversion | 89 | 27 |
| Agreeableness | 51 | 4 |
| Neuroticism | 63 | 3 |

### Violation Types

| Type | Count |
|------|-------|
| no_organizational_element | 37 |
| response_too_long | 27 |
| agreed_without_concern | 4 |
| no_hedge_under_pressure | 3 |
| imposed_unsolicited_structure | 1 |

---

## RQ5: BCFC Cost Overhead

N sessions: 7

| Metric | Mean | Median | Max |
|--------|------|--------|-----|
| Nudge rate | 0.375 | 0.375 | 0.375 |
| Regen rate | 1.286 | 1.125 | 3.125 |

**Estimated cost overhead: 128.6%** (FAIL: > 50% threshold for <1.5x budget)

