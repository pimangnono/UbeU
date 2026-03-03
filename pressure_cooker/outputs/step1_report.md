# Step 1 Analysis: Agent Trait Consistency Report

**Batch**: `8aec86a0`
**Sessions**: 48
**Judges**: default, x-ai_grok-4.1-fast, google_gemini-2.5-flash
**Profiles**: 12
**Scenarios**: 4

---
## Judge: `default`

### Per-Trait Metrics

| Trait | r | p-value | MAE | RMSE | Bias |
|-------|---|---------|-----|------|------|
| O (openness) | 0.784 *** | 0.0000 | 0.137 | 0.189 | +0.125 |
| C (conscientiousness) | 0.487 *** | 0.0004 | 0.196 | 0.228 | +0.154 |
| E (extraversion) | 0.766 *** | 0.0000 | 0.124 | 0.163 | +0.061 |
| A (agreeableness) | 0.777 *** | 0.0000 | 0.131 | 0.161 | +0.098 |
| N (neuroticism) | 0.766 *** | 0.0000 | 0.135 | 0.166 | -0.090 |

### Per-Profile Accuracy

| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |
|---------|---|----------|-----|-------------------|----------------|
| stoic_pragmatist | 4 | 0.790 | 0.064 | O: 0.350 | O over (+0.35) |
| cautious_skeptic | 4 | 0.795 | 0.030 | E: 0.325 | E over (+0.33) |
| assertive_challenger | 4 | 0.845 | 0.026 | A: 0.225 | A over (+0.23) |
| social_butterfly | 4 | 0.845 | 0.005 | C: 0.350 | C over (+0.35) |
| anxious_perfectionist | 4 | 0.850 | 0.052 | N: 0.225 | N under (-0.23) |
| creative_maverick | 4 | 0.855 | 0.017 | C: 0.275 | C over (+0.28) |
| meticulous_planner | 4 | 0.860 | 0.020 | O: 0.325 | O over (+0.33) |
| harmonious_mediator | 4 | 0.880 | 0.000 | C: 0.275 | C over (+0.28) |
| balanced_leader | 4 | 0.885 | 0.026 | C: 0.200 | C over (+0.20) |
| quiet_analyst | 4 | 0.885 | 0.009 | E: 0.250 | E over (+0.25) |
| stressed_reactor | 4 | 0.885 | 0.036 | C: 0.175 | C over (+0.17) |
| enthusiastic_innovator | 4 | 0.888 | 0.018 | N: 0.200 | N under (-0.20) |

### Per-Scenario Accuracy

| Scenario | N | Mean Acc | Std |
|----------|---|----------|-----|
| process_change | 12 | 0.845 | 0.055 |
| credit_dispute | 12 | 0.849 | 0.035 |
| deadline_pressure | 12 | 0.857 | 0.049 |
| resource_conflict | 12 | 0.870 | 0.031 |

### Weak Spots

**Bottom 3 profiles by accuracy:**
- `stoic_pragmatist`: 0.790
- `cautious_skeptic`: 0.795
- `assertive_challenger`: 0.845

**Weakest traits by correlation:**
- `conscientiousness`: r = 0.487
- `extraversion`: r = 0.766

**Profile-trait combinations with MAE > 0.15:**
- `anxious_perfectionist` / `neuroticism`: MAE = 0.225
- `assertive_challenger` / `agreeableness`: MAE = 0.225
- `balanced_leader` / `conscientiousness`: MAE = 0.200
- `cautious_skeptic` / `extraversion`: MAE = 0.325
- `creative_maverick` / `conscientiousness`: MAE = 0.275
- `enthusiastic_innovator` / `neuroticism`: MAE = 0.200
- `harmonious_mediator` / `conscientiousness`: MAE = 0.275
- `meticulous_planner` / `openness`: MAE = 0.325
- `quiet_analyst` / `extraversion`: MAE = 0.250
- `social_butterfly` / `conscientiousness`: MAE = 0.350
- `stoic_pragmatist` / `openness`: MAE = 0.350
- `stressed_reactor` / `conscientiousness`: MAE = 0.175

---
## Judge: `x-ai_grok-4.1-fast`

### Per-Trait Metrics

| Trait | r | p-value | MAE | RMSE | Bias |
|-------|---|---------|-----|------|------|
| O (openness) | 0.735 *** | 0.0000 | 0.147 | 0.191 | +0.014 |
| C (conscientiousness) | 0.673 *** | 0.0000 | 0.209 | 0.242 | +0.178 |
| E (extraversion) | 0.746 *** | 0.0000 | 0.151 | 0.197 | +0.094 |
| A (agreeableness) | 0.795 *** | 0.0000 | 0.186 | 0.222 | +0.130 |
| N (neuroticism) | 0.902 *** | 0.0000 | 0.190 | 0.218 | -0.165 |

### Per-Profile Accuracy

| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |
|---------|---|----------|-----|-------------------|----------------|
| quiet_analyst | 4 | 0.775 | 0.044 | A: 0.338 | A over (+0.34) |
| cautious_skeptic | 4 | 0.790 | 0.060 | E: 0.350 | E over (+0.35) |
| social_butterfly | 4 | 0.790 | 0.016 | C: 0.375 | C over (+0.38) |
| creative_maverick | 4 | 0.798 | 0.041 | A: 0.312 | A over (+0.31) |
| balanced_leader | 4 | 0.810 | 0.014 | A: 0.287 | A over (+0.29) |
| harmonious_mediator | 4 | 0.810 | 0.029 | C: 0.350 | C over (+0.35) |
| stoic_pragmatist | 4 | 0.818 | 0.089 | E: 0.262 | E over (+0.24) |
| stressed_reactor | 4 | 0.820 | 0.046 | C: 0.250 | C over (+0.25) |
| enthusiastic_innovator | 4 | 0.848 | 0.014 | N: 0.313 | N under (-0.31) |
| assertive_challenger | 4 | 0.855 | 0.038 | C: 0.238 | C over (+0.24) |
| anxious_perfectionist | 4 | 0.883 | 0.029 | A: 0.250 | A over (+0.25) |
| meticulous_planner | 4 | 0.885 | 0.009 | N: 0.300 | N under (-0.30) |

### Per-Scenario Accuracy

| Scenario | N | Mean Acc | Std |
|----------|---|----------|-----|
| process_change | 12 | 0.799 | 0.066 |
| credit_dispute | 12 | 0.820 | 0.053 |
| deadline_pressure | 12 | 0.833 | 0.038 |
| resource_conflict | 12 | 0.842 | 0.047 |

### Weak Spots

**Bottom 3 profiles by accuracy:**
- `quiet_analyst`: 0.775
- `cautious_skeptic`: 0.790
- `social_butterfly`: 0.790

**Weakest traits by correlation:**
- `conscientiousness`: r = 0.673
- `openness`: r = 0.735

**Profile-trait combinations with MAE > 0.15:**
- `anxious_perfectionist` / `agreeableness`: MAE = 0.250
- `assertive_challenger` / `conscientiousness`: MAE = 0.238
- `balanced_leader` / `agreeableness`: MAE = 0.287
- `cautious_skeptic` / `extraversion`: MAE = 0.350
- `creative_maverick` / `agreeableness`: MAE = 0.312
- `enthusiastic_innovator` / `neuroticism`: MAE = 0.313
- `harmonious_mediator` / `conscientiousness`: MAE = 0.350
- `meticulous_planner` / `neuroticism`: MAE = 0.300
- `quiet_analyst` / `agreeableness`: MAE = 0.338
- `social_butterfly` / `conscientiousness`: MAE = 0.375
- `stoic_pragmatist` / `extraversion`: MAE = 0.262
- `stressed_reactor` / `conscientiousness`: MAE = 0.250

---
## Judge: `google_gemini-2.5-flash`

### Per-Trait Metrics

| Trait | r | p-value | MAE | RMSE | Bias |
|-------|---|---------|-----|------|------|
| O (openness) | 0.793 *** | 0.0000 | 0.102 | 0.146 | +0.027 |
| C (conscientiousness) | 0.815 *** | 0.0000 | 0.135 | 0.166 | +0.123 |
| E (extraversion) | 0.722 *** | 0.0000 | 0.135 | 0.177 | +0.052 |
| A (agreeableness) | 0.858 *** | 0.0000 | 0.104 | 0.137 | +0.071 |
| N (neuroticism) | 0.850 *** | 0.0000 | 0.135 | 0.153 | -0.077 |

### Per-Profile Accuracy

| Profile | N | Mean Acc | Std | Worst Trait (MAE) | Bias Direction |
|---------|---|----------|-----|-------------------|----------------|
| stoic_pragmatist | 4 | 0.825 | 0.071 | O: 0.200 | O over (+0.20) |
| cautious_skeptic | 4 | 0.830 | 0.036 | E: 0.300 | E over (+0.30) |
| quiet_analyst | 4 | 0.850 | 0.041 | E: 0.275 | E over (+0.28) |
| social_butterfly | 4 | 0.855 | 0.017 | C: 0.250 | C over (+0.25) |
| assertive_challenger | 4 | 0.875 | 0.030 | C: 0.225 | C over (+0.23) |
| creative_maverick | 4 | 0.875 | 0.022 | A: 0.225 | A over (+0.23) |
| meticulous_planner | 4 | 0.885 | 0.017 | N: 0.200 | N under (-0.20) |
| stressed_reactor | 4 | 0.885 | 0.022 | E: 0.200 | E under (-0.20) |
| balanced_leader | 4 | 0.900 | 0.014 | C: 0.175 | C over (+0.17) |
| anxious_perfectionist | 4 | 0.915 | 0.030 | E: 0.125 | E under (-0.12) |
| enthusiastic_innovator | 4 | 0.915 | 0.022 | N: 0.200 | N under (-0.20) |
| harmonious_mediator | 4 | 0.920 | 0.014 | C: 0.175 | C over (+0.17) |

### Per-Scenario Accuracy

| Scenario | N | Mean Acc | Std |
|----------|---|----------|-----|
| process_change | 12 | 0.862 | 0.049 |
| credit_dispute | 12 | 0.877 | 0.043 |
| deadline_pressure | 12 | 0.877 | 0.039 |
| resource_conflict | 12 | 0.895 | 0.039 |

### Weak Spots

**Bottom 3 profiles by accuracy:**
- `stoic_pragmatist`: 0.825
- `cautious_skeptic`: 0.830
- `quiet_analyst`: 0.850

**Weakest traits by correlation:**
- `extraversion`: r = 0.722
- `openness`: r = 0.793

**Profile-trait combinations with MAE > 0.15:**
- `assertive_challenger` / `conscientiousness`: MAE = 0.225
- `balanced_leader` / `conscientiousness`: MAE = 0.175
- `cautious_skeptic` / `extraversion`: MAE = 0.300
- `creative_maverick` / `agreeableness`: MAE = 0.225
- `enthusiastic_innovator` / `neuroticism`: MAE = 0.200
- `harmonious_mediator` / `conscientiousness`: MAE = 0.175
- `meticulous_planner` / `neuroticism`: MAE = 0.200
- `quiet_analyst` / `extraversion`: MAE = 0.275
- `social_butterfly` / `conscientiousness`: MAE = 0.250
- `stoic_pragmatist` / `openness`: MAE = 0.200
- `stressed_reactor` / `extraversion`: MAE = 0.200

---
## Inter-Judge Agreement

**Judges**: default, x-ai_grok-4.1-fast, google_gemini-2.5-flash
**Common sessions**: 48
**Overall mean pairwise r**: 0.842
**Overall mean pairwise MAD**: 0.104

| Trait | Pairwise r | Pairwise MAD |
|-------|-----------|-------------|
| O (openness) | 0.864 | 0.119 |
| C (conscientiousness) | 0.721 | 0.099 |
| E (extraversion) | 0.854 | 0.091 |
| A (agreeableness) | 0.881 | 0.101 |
| N (neuroticism) | 0.890 | 0.112 |

---
## Coverage Matrix (Profile x Scenario)

| Profile | credit_dispute | deadline_pressure | process_change | resource_conflict | Total |
|---|---|---|---|---|---|
| anxious_perfectionist | 1 | 1 | 1 | 1 | 4 |
| assertive_challenger | 1 | 1 | 1 | 1 | 4 |
| balanced_leader | 1 | 1 | 1 | 1 | 4 |
| cautious_skeptic | 1 | 1 | 1 | 1 | 4 |
| creative_maverick | 1 | 1 | 1 | 1 | 4 |
| enthusiastic_innovator | 1 | 1 | 1 | 1 | 4 |
| harmonious_mediator | 1 | 1 | 1 | 1 | 4 |
| meticulous_planner | 1 | 1 | 1 | 1 | 4 |
| quiet_analyst | 1 | 1 | 1 | 1 | 4 |
| social_butterfly | 1 | 1 | 1 | 1 | 4 |
| stoic_pragmatist | 1 | 1 | 1 | 1 | 4 |
| stressed_reactor | 1 | 1 | 1 | 1 | 4 |

---
## Recommendations

1. **Trait correlations** are acceptable across all traits.
2. **Underperforming profiles**: cautious_skeptic, stoic_pragmatist have mean accuracy < 0.80. Review their system prompts and behavioral tendencies.
3. **Inter-judge agreement** is reasonable (r = 0.842).
4. **Only 1.0 rep(s) per combination**. Recommend expanding to 3 reps to compute within-profile consistency (SD, ICC).
