# Simulation Benchmark Report

## Suite Config
- Total runs: 3
- Conditions: naive, engine, engine_controller
- Script ids: post_merger_integration
- Repetitions per condition: 1

## Condition Summary
### engine
- Runs: 1
- Persona drift MAE: 0.1527 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.2000, E 0.0837, A 0.1267, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### engine_controller
- Runs: 1
- Persona drift MAE: 0.1565 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.1533, E 0.1428, A 0.1333, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Mean turns: 11.00

### naive
- Runs: 1
- Persona drift MAE: 0.1651 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.2467, E 0.0522, A 0.1200, N 0.2767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1250
- Envelope violations: 7.0000
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0086
- Per-trait error delta: O +0.0000, C -0.0934, E +0.0906, A +0.0133, N -0.0534
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.1250

## Script-Level Summary
### post_merger_integration:engine
- Runs: 1
- Persona drift MAE: 0.1527 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.2000, E 0.0837, A 0.1267, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### post_merger_integration:engine_controller
- Runs: 1
- Persona drift MAE: 0.1565 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.1533, E 0.1428, A 0.1333, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Mean turns: 11.00

### post_merger_integration:naive
- Runs: 1
- Persona drift MAE: 0.1651 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.2467, E 0.0522, A 0.1200, N 0.2767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1250
- Envelope violations: 7.0000
- Mean turns: 11.00
