# Simulation Benchmark Report

## Suite Config
- Total runs: 9
- Conditions: naive, engine, engine_controller
- Script ids: post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine
- Runs: 3
- Persona drift MAE: 0.1823 (+/- 0.0049)
- Per-trait absolute error: O 0.1322, C 0.3444, E 0.1068, A 0.0867, N 0.2411
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1528
- Envelope violations: 5.6667
- Mean turns: 11.00

### engine_controller
- Runs: 3
- Persona drift MAE: 0.1440 (+/- 0.0154)
- Per-trait absolute error: O 0.1189, C 0.1667, E 0.1001, A 0.0756, N 0.2589
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.3333
- Mean turns: 11.00

### naive
- Runs: 3
- Persona drift MAE: 0.1750 (+/- 0.0161)
- Per-trait absolute error: O 0.1322, C 0.3133, E 0.0906, A 0.0844, N 0.2544
- Relationship inconsistency: 0.1000
- Commitment contradiction: 0.0667
- Envelope violations: 6.0000
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0310
- Per-trait error delta: O -0.0133, C -0.1466, E +0.0095, A -0.0088, N +0.0045
- Relationship inconsistency delta: -0.1000
- Commitment contradiction delta: -0.0667

## Script-Level Summary
### post_merger_integration:engine
- Runs: 3
- Persona drift MAE: 0.1823 (+/- 0.0049)
- Per-trait absolute error: O 0.1322, C 0.3444, E 0.1068, A 0.0867, N 0.2411
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1528
- Envelope violations: 5.6667
- Mean turns: 11.00

### post_merger_integration:engine_controller
- Runs: 3
- Persona drift MAE: 0.1440 (+/- 0.0154)
- Per-trait absolute error: O 0.1189, C 0.1667, E 0.1001, A 0.0756, N 0.2589
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.3333
- Mean turns: 11.00

### post_merger_integration:naive
- Runs: 3
- Persona drift MAE: 0.1750 (+/- 0.0161)
- Per-trait absolute error: O 0.1322, C 0.3133, E 0.0906, A 0.0844, N 0.2544
- Relationship inconsistency: 0.1000
- Commitment contradiction: 0.0667
- Envelope violations: 6.0000
- Mean turns: 11.00
