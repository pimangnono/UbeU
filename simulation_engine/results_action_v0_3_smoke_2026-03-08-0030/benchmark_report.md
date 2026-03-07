# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy, new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 2
- Persona drift MAE: 0.1731 (+/- 0.0295)
- Per-trait absolute error: O 0.1216, C 0.2434, E 0.2155, A 0.0700, N 0.2150
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0625
- Envelope violations: 6.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- State trajectory variance: 0.0030
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1682 (+/- 0.0028)
- Per-trait absolute error: O 0.1183, C 0.2200, E 0.2143, A 0.0600, N 0.2283
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- State trajectory variance: 0.0030
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1684 (+/- 0.0072)
- Per-trait absolute error: O 0.1283, C 0.2666, E 0.1456, A 0.0933, N 0.2084
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.1714
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1666
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- State trajectory variance: 0.0003
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): +0.0047
- Per-trait error delta: O -0.0067, C -0.0232, E +0.0699, A -0.0233, N +0.0066
- Relationship inconsistency delta: -0.0750
- Commitment contradiction delta: -0.1089
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.9659
- State trajectory variance delta: +0.0027

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1437 (+/- 0.0000)
- Per-trait absolute error: O 0.0633, C 0.2000, E 0.1883, A 0.0933, N 0.1733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1654 (+/- 0.0000)
- Per-trait absolute error: O 0.0567, C 0.2200, E 0.2239, A 0.1000, N 0.2267
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1612 (+/- 0.0000)
- Per-trait absolute error: O 0.0767, C 0.2733, E 0.1361, A 0.1200, N 0.2000
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.2026 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.2867, E 0.2428, A 0.0467, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1250
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1710 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.2200, E 0.2048, A 0.0200, N 0.2300
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1757 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.2600, E 0.1550, A 0.0667, N 0.2167
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.1429
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
