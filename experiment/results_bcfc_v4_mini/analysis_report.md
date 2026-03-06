# Behavioral Fidelity Experiment Report

Generated: 2026-03-06 09:38

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.494 | 0.176476 | 0.1728 | 9 |
| Conscientiousness | 0.2287 | 0.553843 | 0.2528 | 9 |
| Extraversion | 0.9396* | 0.000168 | 0.1167 | 9 |
| Agreeableness | 0.8432* | 0.004298 | 0.2133 | 9 |
| Neuroticism | 0.5477 | 0.126854 | 0.2878 | 9 |

**Overall mean r:** 0.6107
**Overall mean MAE:** 0.2087

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.2204 |
| Conscientiousness | insufficient multi-rep data | - | 0.202 |
| Extraversion | insufficient multi-rep data | - | 0.0744 |
| Agreeableness | insufficient multi-rep data | - | 0.0444 |
| Neuroticism | insufficient multi-rep data | - | 0.1887 |

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
| Openness | 0.0 | 0.21 | 2 | Yes (44%) |
| Conscientiousness | 0.0 | 0.215 | 0 | Yes (33%) |
| Extraversion | 0.05 | 0.355 | 4 | Yes (56%) |
| Agreeableness | 0.0 | 0.15 | 4 | Yes (22%) |
| Neuroticism | 0.03 | 0.225 | 2 | Yes (33%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism

**Total sessions analyzed:** 9

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.8382 | 0.004772 | positive | Yes |
| Disagreements -> -Agreeableness | -0.0309 | 0.937007 | negative | Yes |
| Acknowledgments -> Agreeableness | -0.2641 | 0.492212 | positive | No |
| New ideas -> Openness | 0.2926 | 0.444867 | positive | Yes |
| Questions asked -> Extraversion | -0.5734 | 0.106506 | positive | No |
| Name mentions -> Extraversion | 0.5337 | 0.138922 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.4176 | 0.26347 | 0.494 | -0.3368 | 9 |
| Conscientiousness | 0.6661 | 0.050127 | 0.2287 | 0.5983 | 9 |
| Extraversion | 0.5109 | 0.159885 | 0.9396 | 0.5866 | 9 |
| Agreeableness | 0.243 | 0.528662 | 0.8432 | 0.2385 | 9 |
| Neuroticism | 0.1589 | 0.683073 | 0.5477 | 0.6321 | 9 |

**Convergent validity: MODERATE** (mean r = 0.399)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Apologies -> N | nan | nan | positive | No |
| Self-doubt -> N | nan | nan | positive | No |
| Hypotheticals -> O | nan | nan | positive | No |
| Avg words -> E | 0.7179* | 0.029389 | positive | Yes |
| Question ratio -> E | -0.698* | 0.036543 | positive | No |
| Structure markers -> C | nan | nan | positive | No |
| Reference back -> C | nan | nan | positive | No |
| Positive emotion -> A | nan | nan | positive | No |
| Hedges -> N | 0.8237* | 0.006343 | positive | Yes |
| Negations -> -A | -0.7749* | 0.014191 | negative | Yes |
| Turn initiation -> E | -0.7606* | 0.017337 | positive | No |
| Max words -> E | 0.6554 | 0.055352 | positive | Yes |
| Certainty -> E | -0.6547 | 0.055702 | positive | No |
| Word variance -> O | 0.6155 | 0.077649 | positive | Yes |
| Exclamation ratio -> E | 0.5923 | 0.092847 | positive | Yes |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.127 | 0.0161 | 0.0691 | 9 |
| Conscientiousness | 0.1056 | 0.0112 | 0.0358 | 9 |
| Extraversion | 0.1286 | 0.0165 | 0.0422 | 9 |
| Agreeableness | 0.0867 | 0.0075 | 0.025 | 9 |
| Neuroticism | 0.1238 | 0.0153 | 0.0504 | 9 |

**Uncertain sessions (high inter-model variance):** 4

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.1439 | No | -0.0855 | -0.0584 |
| Conscientiousness | -0.0583 | No | -0.0491 | -0.0092 |
| Extraversion | +0.1167* | Yes | +0.1540 | -0.0373 |
| Agreeableness | +0.1144 | No | +0.0555 | +0.0589 |
| Neuroticism | -0.1989* | Yes | -0.1521 | -0.0468 |

**Significantly biased traits: Neuroticism (-0.199), Extraversion (+0.117)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | weak | no_data | fragile | no_data | unbiased |
| Conscientiousness | weak | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | biased (+0.117) |
| Agreeableness | strong | no_data | fragile | no_data | unbiased |
| Neuroticism | weak | no_data | fragile | no_data | biased (-0.199) |
---

## BoN Pool Ablation (Offline)

Pools analyzed: 96

| Policy | Contract Distance (avg) | Adequacy Penalty (avg) |
|--------|--------------------------|------------------------|
| full_score | 1.0 | 1.0 |
| contract_only | 1.0 | 1.0 |
| relevance_only | 1.0 | 1.0 |
| first | 1.0 | 1.0 |
| random_expected | 1.0 | 1.0 |

---

## Candidate Diversity

Pools analyzed: 96

| Metric | Value |
|--------|-------|
| Avg Jaccard overlap | 0.2268 |
| Avg diversity (1 - overlap) | 0.7732 |

