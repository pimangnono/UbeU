# Simulation Benchmark Report

## Suite Config
- Total runs: 3
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1373 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.2067, E 0.1433, A 0.1000, N 0.1333
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1319 (+/- 0.0000)
- Per-trait absolute error: O 0.0900, C 0.1600, E 0.1827, A 0.1333, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1820 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.3800, E 0.1336, A 0.1000, N 0.2267
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): -0.0447
- Per-trait error delta: O +0.0333, C -0.1733, E +0.0097, A +0.0000, N -0.0934
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: +0.0000
- Structured action validity delta: +0.2000
- Executed action contradiction delta: +0.0000
- State trajectory variance delta: +0.0000

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1373 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.2067, E 0.1433, A 0.1000, N 0.1333
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1319 (+/- 0.0000)
- Per-trait absolute error: O 0.0900, C 0.1600, E 0.1827, A 0.1333, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1820 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.3800, E 0.1336, A 0.1000, N 0.2267
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
