# Simulation Benchmark Report

## Suite Config
- Total runs: 9
- Conditions: naive, engine, engine_controller
- Script ids: new_product_launch
- Repetitions per condition: 3

## Condition Summary
### engine
- Runs: 3
- Persona drift MAE: 0.1750 (+/- 0.0016)
- Per-trait absolute error: O 0.1578, C 0.2289, E 0.1763, A 0.0733, N 0.2389
- Relationship inconsistency: 0.0708
- Commitment contradiction: 0.0476
- Envelope violations: 7.3333
- Mean turns: 11.00

### engine_controller
- Runs: 3
- Persona drift MAE: 0.1738 (+/- 0.0127)
- Per-trait absolute error: O 0.1467, C 0.2822, E 0.1567, A 0.0667, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.3333
- Mean turns: 11.00

### naive
- Runs: 3
- Persona drift MAE: 0.1777 (+/- 0.0048)
- Per-trait absolute error: O 0.1800, C 0.2733, E 0.1137, A 0.0733, N 0.2478
- Relationship inconsistency: 0.1429
- Commitment contradiction: 0.2381
- Envelope violations: 6.3333
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0039
- Per-trait error delta: O -0.0333, C +0.0089, E +0.0430, A -0.0066, N -0.0311
- Relationship inconsistency delta: -0.1429
- Commitment contradiction delta: -0.2381

## Script-Level Summary
### new_product_launch:engine
- Runs: 3
- Persona drift MAE: 0.1750 (+/- 0.0016)
- Per-trait absolute error: O 0.1578, C 0.2289, E 0.1763, A 0.0733, N 0.2389
- Relationship inconsistency: 0.0708
- Commitment contradiction: 0.0476
- Envelope violations: 7.3333
- Mean turns: 11.00

### new_product_launch:engine_controller
- Runs: 3
- Persona drift MAE: 0.1738 (+/- 0.0127)
- Per-trait absolute error: O 0.1467, C 0.2822, E 0.1567, A 0.0667, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.3333
- Mean turns: 11.00

### new_product_launch:naive
- Runs: 3
- Persona drift MAE: 0.1777 (+/- 0.0048)
- Per-trait absolute error: O 0.1800, C 0.2733, E 0.1137, A 0.0733, N 0.2478
- Relationship inconsistency: 0.1429
- Commitment contradiction: 0.2381
- Envelope violations: 6.3333
- Mean turns: 11.00
