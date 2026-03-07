# Simulation Benchmark Report

## Suite Config
- Total runs: 15
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 5
- Persona drift MAE: 0.1676 (+/- 0.0281)
- Per-trait absolute error: O 0.1040, C 0.2753, E 0.1769, A 0.0880, N 0.1940
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.2000
- Structured action validity: 0.4739
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.4667
- State trajectory variance: 0.0018
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 5
- Persona drift MAE: 0.1568 (+/- 0.0079)
- Per-trait absolute error: O 0.0893, C 0.2660, E 0.1746, A 0.0707, N 0.1833
- Relationship inconsistency: 0.0675
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.2933
- Owner resolution rate: 0.8000
- Executed action contradiction: 0.0000
- State transition coherence: 0.8000
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### naive_action_baseline
- Runs: 5
- Persona drift MAE: 0.1851 (+/- 0.0117)
- Per-trait absolute error: O 0.1173, C 0.3233, E 0.1311, A 0.1013, N 0.2527
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0857
- Envelope violations: 6.8000
- Structured action validity: 0.6267
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- State trajectory variance: 0.0006
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): -0.0175
- Per-trait error delta: O -0.0133, C -0.0480, E +0.0458, A -0.0133, N -0.0587
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.0857
- Structured action validity delta: -0.1528
- Executed action contradiction delta: +0.0000
- State trajectory variance delta: +0.0012

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1153 (+/- 0.0000)
- Per-trait absolute error: O 0.0900, C 0.1533, E 0.1800, A 0.0600, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1451 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.2933, E 0.1487, A 0.0667, N 0.1467
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1648 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.2467, E 0.1542, A 0.1067, N 0.2133
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### housing_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1719 (+/- 0.0000)
- Per-trait absolute error: O 0.0667, C 0.3500, E 0.2194, A 0.0767, N 0.1467
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Structured action validity: 0.6250
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### housing_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1636 (+/- 0.0000)
- Per-trait absolute error: O 0.0667, C 0.3300, E 0.2047, A 0.0567, N 0.1600
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.5556
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### housing_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1974 (+/- 0.0000)
- Per-trait absolute error: O 0.1133, C 0.3233, E 0.1605, A 0.1233, N 0.2667
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 9.0000
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1796 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2400, E 0.1747, A 0.0800, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.4444
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1602 (+/- 0.0000)
- Per-trait absolute error: O 0.1133, C 0.2067, E 0.2044, A 0.0600, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1958 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3333, E 0.1423, A 0.0667, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2857
- Envelope violations: 7.0000
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1716 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.2867, E 0.0978, A 0.1200, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.3000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1500 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.1933, E 0.1167, A 0.1000, N 0.2100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.2857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1852 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.3333, E 0.0727, A 0.1133, N 0.2767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1429
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1998 (+/- 0.0000)
- Per-trait absolute error: O 0.0867, C 0.3467, E 0.2125, A 0.1033, N 0.2500
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1651 (+/- 0.0000)
- Per-trait absolute error: O 0.0667, C 0.3067, E 0.1986, A 0.0700, N 0.1833
- Relationship inconsistency: 0.3375
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.3750
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1825 (+/- 0.0000)
- Per-trait absolute error: O 0.0600, C 0.3800, E 0.1259, A 0.0967, N 0.2500
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.8333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
