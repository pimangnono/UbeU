# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy, new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 2
- Persona drift MAE: 0.1817 (+/- 0.0116)
- Per-trait absolute error: O 0.1084, C 0.3133, E 0.2354, A 0.0700, N 0.1816
- Relationship inconsistency: 0.1125
- Commitment contradiction: 0.0000
- Envelope violations: 6.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.8334
- State trajectory variance: 0.0017
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1483 (+/- 0.0237)
- Per-trait absolute error: O 0.1084, C 0.2434, E 0.1613, A 0.0467, N 0.1817
- Relationship inconsistency: 0.1125
- Commitment contradiction: 0.0625
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.8334
- State trajectory variance: 0.0030
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1625 (+/- 0.0011)
- Per-trait absolute error: O 0.1117, C 0.2200, E 0.1458, A 0.0800, N 0.2550
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2857
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0009
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): +0.0192
- Per-trait error delta: O -0.0033, C +0.0933, E +0.0896, A -0.0100, N -0.0734
- Relationship inconsistency delta: +0.1125
- Commitment contradiction delta: -0.2857
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- State trajectory variance delta: +0.0008

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1701 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.3733, E 0.2074, A 0.0800, N 0.1200
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1246 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.2400, E 0.1795, A 0.0267, N 0.1067
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1614 (+/- 0.0000)
- Per-trait absolute error: O 0.0767, C 0.2400, E 0.1504, A 0.0867, N 0.2533
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1934 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2533, E 0.2634, A 0.0600, N 0.2433
- Relationship inconsistency: 0.2250
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1720 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2467, E 0.1431, A 0.0667, N 0.2567
- Relationship inconsistency: 0.2250
- Commitment contradiction: 0.1250
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1636 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2000, E 0.1412, A 0.0733, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.5714
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
