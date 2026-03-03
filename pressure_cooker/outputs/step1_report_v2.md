# Step 1 Analysis: Agent Trait Consistency Report

**Batch**: `4501beb2`
**Sessions**: 144
**Judges**: google_gemini-2.5-flash, x-ai_grok-4.1-fast, deepseek_deepseek-chat-v3-0324
**Profiles**: 12
**Scenarios**: 4

---
## Judge: `google_gemini-2.5-flash`

### Per-Trait Metrics

| Trait | r | p-value | MAE | RMSE | Bias |
|-------|---|---------|-----|------|------|
| O (openness) | 0.729 *** | 0.0000 | 0.157 | 0.207 | -0.100 |
| C (conscientiousness) | 0.746 *** | 0.0000 | 0.124 | 0.157 | +0.042 |
| E (extraversion) | 0.864 *** | 0.0000 | 0.085 | 0.127 | +0.012 |
| A (agreeableness) | 0.777 *** | 0.0000 | 0.133 | 0.167 | -0.023 |
| N (neuroticism) | 0.830 *** | 0.0000 | 0.169 | 0.201 | -0.119 |

### Per-Profile Accuracy

| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |
|---------|---|----------|-----|-------------------|----------------|
| creative_maverick | 12 | 0.827 | 0.009 | O: 0.200 | O under (-0.20) |
| balanced_leader | 12 | 0.852 | 0.038 | C: 0.200 | C over (+0.13) |
| stressed_reactor | 12 | 0.852 | 0.033 | O: 0.233 | O under (-0.23) |
| quiet_analyst | 12 | 0.855 | 0.032 | O: 0.333 | O under (-0.33) |
| assertive_challenger | 12 | 0.857 | 0.031 | O: 0.283 | O under (-0.27) |
| social_butterfly | 12 | 0.862 | 0.036 | O: 0.200 | O over (+0.20) |
| cautious_skeptic | 12 | 0.873 | 0.037 | N: 0.217 | N under (-0.18) |
| enthusiastic_innovator | 12 | 0.873 | 0.025 | N: 0.283 | N under (-0.27) |
| meticulous_planner | 12 | 0.875 | 0.026 | N: 0.283 | N under (-0.27) |
| anxious_perfectionist | 12 | 0.890 | 0.040 | A: 0.142 | A under (-0.06) |
| harmonious_mediator | 12 | 0.890 | 0.024 | N: 0.208 | N under (-0.16) |
| stoic_pragmatist | 12 | 0.892 | 0.044 | C: 0.192 | C over (+0.16) |

### Per-Scenario Accuracy

| Scenario | N | Mean Acc | Std |
|----------|---|----------|-----|
| deadline_pressure | 36 | 0.858 | 0.038 |
| resource_conflict | 36 | 0.867 | 0.035 |
| process_change | 36 | 0.869 | 0.041 |
| credit_dispute | 36 | 0.871 | 0.034 |

### Weak Spots

**Bottom 3 profiles by accuracy:**
- `creative_maverick`: 0.827
- `balanced_leader`: 0.852
- `stressed_reactor`: 0.852

**Weakest traits by correlation:**
- `openness`: r = 0.729
- `conscientiousness`: r = 0.746

**Profile-trait combinations with MAE > 0.15:**
- `assertive_challenger` / `openness`: MAE = 0.283
- `balanced_leader` / `conscientiousness`: MAE = 0.200
- `cautious_skeptic` / `neuroticism`: MAE = 0.217
- `creative_maverick` / `openness`: MAE = 0.200
- `enthusiastic_innovator` / `neuroticism`: MAE = 0.283
- `harmonious_mediator` / `neuroticism`: MAE = 0.208
- `meticulous_planner` / `neuroticism`: MAE = 0.283
- `quiet_analyst` / `openness`: MAE = 0.333
- `social_butterfly` / `openness`: MAE = 0.200
- `stoic_pragmatist` / `conscientiousness`: MAE = 0.192
- `stressed_reactor` / `openness`: MAE = 0.233

---
## Judge: `x-ai_grok-4.1-fast`

### Per-Trait Metrics

| Trait | r | p-value | MAE | RMSE | Bias |
|-------|---|---------|-----|------|------|
| O (openness) | 0.753 *** | 0.0000 | 0.180 | 0.236 | -0.111 |
| C (conscientiousness) | 0.758 *** | 0.0000 | 0.142 | 0.175 | +0.061 |
| E (extraversion) | 0.869 *** | 0.0000 | 0.126 | 0.172 | +0.118 |
| A (agreeableness) | 0.786 *** | 0.0000 | 0.195 | 0.223 | +0.057 |
| N (neuroticism) | 0.896 *** | 0.0000 | 0.207 | 0.236 | -0.184 |

### Per-Profile Accuracy

| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |
|---------|---|----------|-----|-------------------|----------------|
| balanced_leader | 12 | 0.778 | 0.021 | O: 0.312 | O under (-0.30) |
| creative_maverick | 12 | 0.809 | 0.010 | A: 0.371 | A over (+0.37) |
| quiet_analyst | 12 | 0.813 | 0.014 | O: 0.433 | O under (-0.43) |
| social_butterfly | 12 | 0.813 | 0.027 | O: 0.321 | O over (+0.30) |
| stressed_reactor | 12 | 0.817 | 0.024 | E: 0.229 | E over (+0.23) |
| harmonious_mediator | 12 | 0.824 | 0.032 | N: 0.300 | N under (-0.30) |
| assertive_challenger | 12 | 0.832 | 0.019 | O: 0.321 | O under (-0.30) |
| cautious_skeptic | 12 | 0.835 | 0.020 | N: 0.375 | N under (-0.38) |
| enthusiastic_innovator | 12 | 0.845 | 0.017 | A: 0.300 | A over (+0.30) |
| meticulous_planner | 12 | 0.848 | 0.025 | N: 0.300 | N under (-0.30) |
| anxious_perfectionist | 12 | 0.850 | 0.025 | E: 0.296 | E over (+0.30) |
| stoic_pragmatist | 12 | 0.893 | 0.019 | C: 0.200 | C over (+0.20) |

### Per-Scenario Accuracy

| Scenario | N | Mean Acc | Std |
|----------|---|----------|-----|
| credit_dispute | 36 | 0.826 | 0.034 |
| resource_conflict | 36 | 0.827 | 0.031 |
| process_change | 36 | 0.831 | 0.040 |
| deadline_pressure | 36 | 0.836 | 0.033 |

### Weak Spots

**Bottom 3 profiles by accuracy:**
- `balanced_leader`: 0.778
- `creative_maverick`: 0.809
- `quiet_analyst`: 0.813

**Weakest traits by correlation:**
- `openness`: r = 0.753
- `conscientiousness`: r = 0.758

**Profile-trait combinations with MAE > 0.15:**
- `anxious_perfectionist` / `extraversion`: MAE = 0.296
- `assertive_challenger` / `openness`: MAE = 0.321
- `balanced_leader` / `openness`: MAE = 0.312
- `cautious_skeptic` / `neuroticism`: MAE = 0.375
- `creative_maverick` / `agreeableness`: MAE = 0.371
- `enthusiastic_innovator` / `agreeableness`: MAE = 0.300
- `harmonious_mediator` / `neuroticism`: MAE = 0.300
- `meticulous_planner` / `neuroticism`: MAE = 0.300
- `quiet_analyst` / `openness`: MAE = 0.433
- `social_butterfly` / `openness`: MAE = 0.321
- `stoic_pragmatist` / `conscientiousness`: MAE = 0.200
- `stressed_reactor` / `extraversion`: MAE = 0.229

---
## Judge: `deepseek_deepseek-chat-v3-0324`

### Per-Trait Metrics

| Trait | r | p-value | MAE | RMSE | Bias |
|-------|---|---------|-----|------|------|
| O (openness) | 0.739 *** | 0.0000 | 0.123 | 0.169 | -0.009 |
| C (conscientiousness) | 0.666 *** | 0.0000 | 0.132 | 0.167 | +0.075 |
| E (extraversion) | 0.835 *** | 0.0000 | 0.092 | 0.137 | +0.031 |
| A (agreeableness) | 0.745 *** | 0.0000 | 0.111 | 0.151 | +0.029 |
| N (neuroticism) | 0.756 *** | 0.0000 | 0.148 | 0.179 | -0.085 |

### Per-Profile Accuracy

| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |
|---------|---|----------|-----|-------------------|----------------|
| creative_maverick | 12 | 0.855 | 0.034 | A: 0.233 | A over (+0.23) |
| social_butterfly | 12 | 0.855 | 0.032 | O: 0.250 | O over (+0.25) |
| stoic_pragmatist | 12 | 0.863 | 0.051 | C: 0.200 | C over (+0.10) |
| assertive_challenger | 12 | 0.867 | 0.022 | O: 0.242 | O under (-0.16) |
| quiet_analyst | 12 | 0.872 | 0.040 | O: 0.183 | O under (-0.18) |
| harmonious_mediator | 12 | 0.875 | 0.018 | N: 0.158 | N under (-0.11) |
| cautious_skeptic | 12 | 0.878 | 0.041 | N: 0.250 | N under (-0.25) |
| enthusiastic_innovator | 12 | 0.879 | 0.041 | N: 0.183 | N under (-0.15) |
| balanced_leader | 12 | 0.888 | 0.036 | C: 0.183 | C over (+0.12) |
| stressed_reactor | 12 | 0.893 | 0.030 | O: 0.150 | O under (-0.15) |
| meticulous_planner | 12 | 0.907 | 0.035 | N: 0.200 | N under (-0.18) |
| anxious_perfectionist | 12 | 0.913 | 0.057 | C: 0.100 | C under (-0.10) |

### Per-Scenario Accuracy

| Scenario | N | Mean Acc | Std |
|----------|---|----------|-----|
| deadline_pressure | 36 | 0.872 | 0.040 |
| credit_dispute | 36 | 0.877 | 0.042 |
| resource_conflict | 36 | 0.878 | 0.040 |
| process_change | 36 | 0.889 | 0.043 |

### Weak Spots

**Bottom 3 profiles by accuracy:**
- `creative_maverick`: 0.855
- `social_butterfly`: 0.855
- `stoic_pragmatist`: 0.863

**Weakest traits by correlation:**
- `conscientiousness`: r = 0.666
- `openness`: r = 0.739

**Profile-trait combinations with MAE > 0.15:**
- `assertive_challenger` / `openness`: MAE = 0.242
- `balanced_leader` / `conscientiousness`: MAE = 0.183
- `cautious_skeptic` / `neuroticism`: MAE = 0.250
- `creative_maverick` / `agreeableness`: MAE = 0.233
- `enthusiastic_innovator` / `neuroticism`: MAE = 0.183
- `harmonious_mediator` / `neuroticism`: MAE = 0.158
- `meticulous_planner` / `neuroticism`: MAE = 0.200
- `quiet_analyst` / `openness`: MAE = 0.183
- `social_butterfly` / `openness`: MAE = 0.250
- `stoic_pragmatist` / `conscientiousness`: MAE = 0.200

---
## Inter-Judge Agreement

**Judges**: google_gemini-2.5-flash, x-ai_grok-4.1-fast, deepseek_deepseek-chat-v3-0324
**Common sessions**: 144
**Overall mean pairwise r**: 0.805
**Overall mean pairwise MAD**: 0.124

| Trait | Pairwise r | Pairwise MAD |
|-------|-----------|-------------|
| O (openness) | 0.841 | 0.128 |
| C (conscientiousness) | 0.710 | 0.116 |
| E (extraversion) | 0.826 | 0.115 |
| A (agreeableness) | 0.824 | 0.138 |
| N (neuroticism) | 0.823 | 0.124 |

---
## Coverage Matrix (Profile x Scenario)

| Profile | credit_dispute | deadline_pressure | process_change | resource_conflict | Total |
|---|---|---|---|---|---|
| anxious_perfectionist | 3 | 3 | 3 | 3 | 12 |
| assertive_challenger | 3 | 3 | 3 | 3 | 12 |
| balanced_leader | 3 | 3 | 3 | 3 | 12 |
| cautious_skeptic | 3 | 3 | 3 | 3 | 12 |
| creative_maverick | 3 | 3 | 3 | 3 | 12 |
| enthusiastic_innovator | 3 | 3 | 3 | 3 | 12 |
| harmonious_mediator | 3 | 3 | 3 | 3 | 12 |
| meticulous_planner | 3 | 3 | 3 | 3 | 12 |
| quiet_analyst | 3 | 3 | 3 | 3 | 12 |
| social_butterfly | 3 | 3 | 3 | 3 | 12 |
| stoic_pragmatist | 3 | 3 | 3 | 3 | 12 |
| stressed_reactor | 3 | 3 | 3 | 3 | 12 |

---
## Recommendations

1. **Trait correlations** are acceptable across all traits.
2. **All profiles** have mean accuracy >= 0.80.
3. **Inter-judge agreement** is reasonable (r = 0.805).
