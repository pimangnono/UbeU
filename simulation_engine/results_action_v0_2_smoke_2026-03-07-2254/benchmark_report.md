# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy, new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 2
- Persona drift MAE: 0.1738 (+/- 0.0140)
- Per-trait absolute error: O 0.1350, C 0.2500, E 0.2021, A 0.0733, N 0.2084
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9875
- Planned action coverage: 0.5000
- State trajectory variance: 0.0034
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1453 (+/- 0.0047)
- Per-trait absolute error: O 0.0784, C 0.1900, E 0.2033, A 0.0667, N 0.1884
- Relationship inconsistency: 0.1125
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9929
- Planned action coverage: 0.5454
- State trajectory variance: 0.0032
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1697 (+/- 0.0282)
- Per-trait absolute error: O 0.1250, C 0.2933, E 0.1051, A 0.0967, N 0.2283
- Relationship inconsistency: 0.2250
- Commitment contradiction: 0.3304
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- State trajectory variance: 0.0009
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): +0.0041
- Per-trait error delta: O +0.0100, C -0.0433, E +0.0970, A -0.0234, N -0.0199
- Relationship inconsistency delta: -0.2250
- Commitment contradiction delta: -0.3304
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.9875
- State trajectory variance delta: +0.0025

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1598 (+/- 0.0000)
- Per-trait absolute error: O 0.1233, C 0.1933, E 0.2158, A 0.0800, N 0.1867
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9750
- Planned action coverage: 0.5455
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1407 (+/- 0.0000)
- Per-trait absolute error: O 0.0767, C 0.1600, E 0.1800, A 0.1000, N 0.1867
- Relationship inconsistency: 0.2250
- Commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9857
- Planned action coverage: 0.6364
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1415 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.2200, E 0.1308, A 0.0867, N 0.2000
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2857
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1877 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.3067, E 0.1885, A 0.0667, N 0.2300
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 1.0000
- Planned action coverage: 0.4545
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1500 (+/- 0.0000)
- Per-trait absolute error: O 0.0800, C 0.2200, E 0.2266, A 0.0333, N 0.1900
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 1.0000
- Planned action coverage: 0.4545
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1979 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3667, E 0.0794, A 0.1067, N 0.2567
- Relationship inconsistency: 0.4500
- Commitment contradiction: 0.3750
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
