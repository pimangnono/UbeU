# Step 2 Aggregate Analysis Report

## 1. Overview

| Metric | Count |
|--------|-------|
| Total participants registered | 34 |
| Completed sessions | 4 |
| With post-session survey | 1 |
| With logic validation | 3 |

**Scenario distribution:**
- greenleaf: 9
- medicore: 8
- swiftcart: 8
- techflow: 8
- resource_conflict: 1

**Completion rate**: 4/34 (12%)

---
## 2. BFI-44 Ground Truth Distribution

| Trait | N | Mean | Std | Min | Max | Median |
|-------|---|------|-----|-----|-----|--------|
| Openness | 33 | 0.486 | 0.064 | 0.200 | 0.550 | 0.500 |
| Conscientiousness | 33 | 0.492 | 0.044 | 0.250 | 0.528 | 0.500 |
| Extraversion | 33 | 0.494 | 0.024 | 0.375 | 0.500 | 0.500 |
| Agreeableness | 33 | 0.507 | 0.049 | 0.444 | 0.778 | 0.500 |
| Neuroticism | 33 | 0.496 | 0.037 | 0.375 | 0.625 | 0.500 |

---
## 3. Session Statistics (Completed Sessions Only)

| Metric | N | Mean | Std | Min | Max | Median |
|--------|---|------|-----|-----|-----|--------|
| Duration (seconds) | 4 | 133.4 | 33.3 | 99.2 | 169.9 | 132.2 |
| Total turns | 4 | 16.5 | 3.2 | 13.0 | 21.0 | 16.0 |
| Candidate turns | 4 | 3.2 | 0.4 | 3.0 | 4.0 | 3.0 |
| Candidate words/turn | 13 | 10.7 | 7.3 | 5.0 | 34.0 | 9.0 |

---
## 4. Assessment Scores

| Dimension | N | Mean | Std | Min | Max | Median |
|-----------|---|------|-----|-----|-----|--------|
| Collaboration | 4 | 0.003 | 0.000 | 0.003 | 0.003 | 0.003 |
| Leadership | 4 | 0.074 | 0.043 | 0.002 | 0.119 | 0.087 |
| Stress Management | 4 | 0.789 | 0.017 | 0.771 | 0.806 | 0.788 |
| Communication | 4 | 0.055 | 0.031 | 0.002 | 0.085 | 0.066 |
| Problem Solving | 4 | 0.059 | 0.042 | 0.000 | 0.117 | 0.059 |

---
## 5. Intent Distribution (Candidate Turns)

| Intent | Mean % | Std | Max % |
|--------|--------|-----|-------|
| Neutral | 77.1 | 13.7 | 100.0 |
| Assertive | 14.6 | 14.9 | 33.3 |
| Analytical | 8.3 | 14.4 | 33.3 |
| Cooperative | 0.0 | 0.0 | 0.0 |
| Avoidant | 0.0 | 0.0 | 0.0 |
| Aggressive | 0.0 | 0.0 | 0.0 |
| Anxious | 0.0 | 0.0 | 0.0 |
| Creative | 0.0 | 0.0 | 0.0 |
| Empathetic | 0.0 | 0.0 | 0.0 |
| Defensive | 0.0 | 0.0 | 0.0 |

**Dominant intent distribution:**
- neutral: 4 (100%)

---
## 6. Logic Validation (Senior Analyst — Multi-Pass)

### Aggregated Scores (median across passes)

| Metric | N | Mean | Std | Min | Max | Median |
|--------|---|------|-----|-----|-----|--------|
| Analytical Depth (1-5) | 2 | 2.0 | 0.0 | 2.0 | 2.0 | 2.0 |
| Recommendation Quality (1-5) | 2 | 1.5 | 0.5 | 1.0 | 2.0 | 1.5 |
| Logical Gaps (count) | 2 | 7.5 | 0.5 | 7.0 | 8.0 | 7.5 |
| Assumptions Made (count) | 2 | 3.5 | 0.5 | 3.0 | 4.0 | 3.5 |

### Sample Logical Gaps Identified

- Did not request cohort-level retention trend data to determine if the 13-point drop is concentrated in power users or spread across all segments
- Did not analyze the timing of the retention drop against specific operational or strategic changes (loyalty program, pricing, product mix shifts)
- Did not quantify the revenue impact of losing power users vs. one-time buyers to prioritize efforts
- Did not examine whether the CAC increase ($14→$19) and LTV:CAC ratio decline (3.5→2.8) correlate with the retention drop or are separate issues
- Did not explore category-level retention patterns (Electronics 15% repeat vs. Home & Living 48%) to identify if product mix shift is a factor
- _...and 10 more_

---
## 7. Post-Session Survey

| Item | N | Mean | Std | Min | Max |
|------|---|------|-----|-----|-----|
| Naturalness | 1 | 4.00 | 0.00 | 4 | 4 |
| Authenticity | 1 | 4.00 | 0.00 | 4 | 4 |
| Realism | 1 | 5.00 | 0.00 | 5 | 5 |
| Engagement | 1 | 5.00 | 0.00 | 5 | 5 |
| Recommendation | 1 | 4.00 | 0.00 | 4 | 4 |

**Overall survey mean**: 4.40 (std=0.00, n=1)

### Open Feedback

- **P006**: Good case study discussion. The data gating was interesting.

---
## 8. Per-Participant Summary

| PID | Name | Scenario | Completed | Turns | Duration | Depth | Rec. Quality | Survey Mean |
|-----|------|----------|-----------|-------|----------|-------|-------------|-------------|
| P001 | J | resource_conflict | No | - | - | - | - | - |
| P002 | VerifyUser | greenleaf | Yes | 21 | 170s | - | - | - |
| P003 | ValTest | medicore | Yes | 13 | 101s | - | - | - |
| P004 | ValTest2 | swiftcart | Yes | 14 | 99s | 2 | 2 | - |
| P005 | BFITest | techflow | No | - | - | - | - | - |
| P006 | E2EUser | greenleaf | Yes | 18 | 163s | 2 | 1 | 4.4 |
| P007 | J | medicore | No | - | - | - | - | - |
| P008 | F | swiftcart | No | - | - | - | - | - |
| P009 | Jex | techflow | No | - | - | - | - | - |
| P010 | TestUser | greenleaf | No | - | - | - | - | - |
| P011 | l | medicore | No | - | - | - | - | - |
| P012 | a | swiftcart | No | - | - | - | - | - |
| P013 | Alex | techflow | No | - | - | - | - | - |
| P014 | alex | greenleaf | No | - | - | - | - | - |
| P015 | alex | medicore | No | - | - | - | - | - |
| P016 | alex | swiftcart | No | - | - | - | - | - |
| P017 | alex | techflow | No | - | - | - | - | - |
| P018 | alex | greenleaf | No | - | - | - | - | - |
| P019 | Alex | medicore | No | - | - | - | - | - |
| P020 | Alex | swiftcart | No | - | - | - | - | - |
| P021 | Alex | techflow | No | - | - | - | - | - |
| P022 | Alex | greenleaf | No | - | - | - | - | - |
| P023 | Alex | medicore | No | - | - | - | - | - |
| P024 | Alex | swiftcart | No | - | - | - | - | - |
| P025 | aa | techflow | No | - | - | - | - | - |
| P026 | Alex | greenleaf | No | - | - | - | - | - |
| P027 | Alex | medicore | No | - | - | - | - | - |
| P028 | aa | swiftcart | No | - | - | - | - | - |
| P029 | aaa | techflow | No | - | - | - | - | - |
| P030 | aaaa | greenleaf | No | - | - | - | - | - |
| P031 | aaaa | medicore | No | - | - | - | - | - |
| P032 | aaaa | swiftcart | No | - | - | - | - | - |
| P033 | aaaa | techflow | No | - | - | - | - | - |
| P034 | aaaaa | greenleaf | No | - | - | - | - | - |
