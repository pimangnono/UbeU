# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy, new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 2
- Persona drift MAE: 0.1540 (+/- 0.0200)
- Per-trait absolute error: O 0.1083, C 0.2167, E 0.1734, A 0.0700, N 0.2017
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.5000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.4166
- State trajectory variance: 0.0006
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1423 (+/- 0.0147)
- Per-trait absolute error: O 0.1250, C 0.2034, E 0.1751, A 0.0333, N 0.1750
- Relationship inconsistency: 0.0791
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0006
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1888 (+/- 0.0071)
- Per-trait absolute error: O 0.1416, C 0.3867, E 0.1474, A 0.0533, N 0.2150
- Relationship inconsistency: 0.1688
- Commitment contradiction: 0.1250
- Envelope violations: 6.0000
- Structured action validity: 0.2916
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0006
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): -0.0348
- Per-trait error delta: O -0.0333, C -0.1700, E +0.0260, A +0.0167, N -0.0133
- Relationship inconsistency delta: -0.1688
- Commitment contradiction delta: -0.1250
- Structured action validity delta: +0.2084
- Executed action contradiction delta: +0.0000
- State trajectory variance delta: +0.0000

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1340 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.1733, E 0.1669, A 0.0800, N 0.1467
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Structured action validity: 0.4545
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1276 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.1267, E 0.1945, A 0.0467, N 0.2000
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1959 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4600, E 0.1763, A 0.0667, N 0.1733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1740 (+/- 0.0000)
- Per-trait absolute error: O 0.1133, C 0.2600, E 0.1800, A 0.0600, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.5455
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1571 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.2800, E 0.1557, A 0.0200, N 0.1500
- Relationship inconsistency: 0.1583
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1817 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3133, E 0.1186, A 0.0400, N 0.2567
- Relationship inconsistency: 0.3375
- Commitment contradiction: 0.2500
- Envelope violations: 6.0000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
