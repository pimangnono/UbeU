# Behavioral Fidelity Experiment Report

Generated: 2026-03-05 22:11

---

## RQ1: Personality Fidelity

Do assigned personality profiles produce matching behavioral signals?

| Trait | Pearson r | p-value | MAE | N |
|-------|----------|---------|-----|---|
| Openness | 0.5496 | 0.125349 | 0.1689 | 9 |
| Conscientiousness | 0.4588 | 0.214165 | 0.2006 | 9 |
| Extraversion | 0.958* | 4.8e-05 | 0.1556 | 9 |
| Agreeableness | 0.8626* | 0.002759 | 0.2117 | 9 |
| Neuroticism | 0.7606* | 0.017336 | 0.3556 | 9 |

**Overall mean r:** 0.7179
**Overall mean MAE:** 0.2184

---

## RQ2: Assessment Consistency

Are personality assessments consistent across repeated sessions?

| Trait | ICC(3,k) | 95% CI | Mean within-profile SD |
|-------|---------|--------|------------------------|
| Openness | insufficient multi-rep data | - | 0.1919 |
| Conscientiousness | insufficient multi-rep data | - | 0.1735 |
| Extraversion | insufficient multi-rep data | - | 0.0381 |
| Agreeableness | insufficient multi-rep data | - | 0.0307 |
| Neuroticism | insufficient multi-rep data | - | 0.0997 |

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
| Openness | 0.05 | 0.4 | 2 | Yes (78%) |
| Conscientiousness | 0.05 | 0.275 | 3 | Yes (22%) |
| Extraversion | 0.03 | 0.28 | 1 | Yes (33%) |
| Agreeableness | 0.0 | 0.15 | 2 | Yes (33%) |
| Neuroticism | 0.02 | 0.115 | 1 | Yes (22%) |

**Uncertain traits (>15% sessions):** Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism

**Total sessions analyzed:** 9

---

## Rule-Based Validation

Feature-trait correlation checks:

| Check | Pearson r | p-value | Expected | Correct? |
|-------|----------|---------|----------|----------|
| Words per turn -> Extraversion | 0.8851 | 0.001512 | positive | Yes |
| Disagreements -> -Agreeableness | -0.4611 | 0.211597 | negative | Yes |
| Acknowledgments -> Agreeableness | -0.0023 | 0.995415 | positive | No |
| New ideas -> Openness | 0.3852 | 0.305932 | positive | Yes |
| Questions asked -> Extraversion | -0.5847 | 0.098231 | positive | No |
| Name mentions -> Extraversion | 0.647 | 0.059651 | positive | Yes |

---

## Dual Evaluation: LLM vs Rule-Based

Convergent validity between LLM ensemble and deterministic rule-based evaluator.

| Trait | LLM vs RB (r) | p-value | LLM vs Assigned (r) | RB vs Assigned (r) | N |
|-------|--------------|---------|---------------------|-------------------|---|
| Openness | 0.5332 | 0.139335 | 0.5496 | -0.1468 | 9 |
| Conscientiousness | 0.5541 | 0.121634 | 0.4588 | 0.693 | 9 |
| Extraversion | 0.7788 | 0.013404 | 0.958 | 0.8167 | 9 |
| Agreeableness | 0.013 | 0.973435 | 0.8626 | 0.0788 | 9 |
| Neuroticism | 0.4933 | 0.177193 | 0.7606 | 0.8002 | 9 |

**Convergent validity: MODERATE** (mean r = 0.474)

---

## Expanded Feature-Trait Validation (22 Features)

Top significant feature-trait correlations:

| Feature -> Trait | Pearson r | p-value | Expected | Correct? |
|-----------------|----------|---------|----------|----------|
| Apologies -> N | nan | nan | positive | No |
| Structure markers -> C | nan | nan | positive | No |
| Long sentences -> C | -0.8797* | 0.001763 | positive | No |
| Positive emotion -> A | nan | nan | positive | No |
| Hypotheticals -> O | nan | nan | positive | No |
| Reference back -> C | nan | nan | positive | No |
| Self-doubt -> N | nan | nan | positive | No |
| Avg words -> E | 0.936* | 0.000205 | positive | Yes |
| Planning -> C | 0.8697* | 0.002307 | positive | Yes |
| Max words -> E | 0.8513* | 0.003599 | positive | Yes |
| Hedges -> N | 0.85* | 0.003706 | positive | Yes |
| Conditionals -> C | 0.8235* | 0.006376 | positive | Yes |
| Negations -> -A | -0.8012* | 0.009439 | negative | Yes |
| Turn initiation -> E | -0.7878* | 0.011691 | positive | No |
| Name mentions -> E | 0.6877* | 0.040607 | positive | Yes |

---

## Inter-Model Agreement

Per-trait variance across ensemble models (lower = more agreement).

| Trait | Mean Stdev | Mean Variance | Max Variance | N |
|-------|-----------|--------------|-------------|---|
| Openness | 0.155 | 0.024 | 0.0527 | 9 |
| Conscientiousness | 0.1117 | 0.0125 | 0.05 | 9 |
| Extraversion | 0.113 | 0.0128 | 0.0292 | 9 |
| Agreeableness | 0.0827 | 0.0068 | 0.022 | 9 |
| Neuroticism | 0.0848 | 0.0072 | 0.0289 | 9 |

**Uncertain sessions (high inter-model variance):** 2

---

## Evaluator Positivity Bias Analysis

Systematic signed error (inferred - assigned) per trait. Positive = overestimated.

| Trait | LLM Bias | Sig? | Rule-Based Bias | LLM-Specific Bias |
|-------|----------|------|-----------------|-------------------|
| Openness | -0.0700 | No | -0.0648 | -0.0052 |
| Conscientiousness | -0.0494 | No | -0.0860 | +0.0365 |
| Extraversion | +0.1556* | Yes | +0.1251 | +0.0304 |
| Agreeableness | +0.1228 | No | +0.0517 | +0.0711 |
| Neuroticism | -0.3556* | Yes | -0.1702 | -0.1854 |

**Significantly biased traits: Neuroticism (-0.356), Extraversion (+0.156)**

---

## Trait Confidence Matrix

Overall evidence quality per trait across all analysis dimensions.

| Trait | Detectability | Consistency | Judge Robustness | Phase Stability | Evaluator Bias |
|-------|--------------|-------------|-----------------|-----------------|---------------|
| Openness | weak | no_data | fragile | no_data | unbiased |
| Conscientiousness | weak | no_data | fragile | no_data | unbiased |
| Extraversion | strong | no_data | fragile | no_data | biased (+0.156) |
| Agreeableness | strong | no_data | fragile | no_data | unbiased |
| Neuroticism | strong | no_data | fragile | no_data | biased (-0.356) |
---

## RQ5: BCFC Cost Overhead

N sessions: 9

| Metric | Mean | Median | Max |
|--------|------|--------|-----|
| Nudge rate | 0.403 | 0.417 | 0.417 |
| Regen rate | 0.0 | 0.0 | 0.0 |

**Estimated cost overhead: 0.0%** (PASS: < 50% threshold for <1.5x budget)
**Mean session cost (USD): 0.0**

---

## BoN Pool Ablation (Offline)

Pools analyzed: 96

| Policy | Contract Distance (avg) | Adequacy Penalty (avg) |
|--------|--------------------------|------------------------|
| full_score | 0.6341 | 0.0063 |
| contract_only | 0.6334 | 0.0146 |
| relevance_only | 0.7058 | 0.0292 |
| first | 0.7068 | 0.0344 |
| random_expected | 0.7066 | 0.0302 |

---

## Candidate Diversity

Pools analyzed: 96

| Metric | Value |
|--------|-------|
| Avg Jaccard overlap | 0.2308 |
| Avg diversity (1 - overlap) | 0.7692 |

