# Simulation Benchmark Report

## Suite Config
- Total runs: 3
- Conditions: naive, engine, engine_controller
- Script ids: new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine
- Runs: 1
- Persona drift MAE: 0.1692 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2400, E 0.1428, A 0.0600, N 0.2567
- Relationship inconsistency: 0.4500
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Mean turns: 11.00

### engine_controller
- Runs: 1
- Persona drift MAE: 0.1502 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.1400, E 0.1275, A 0.0467, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### naive
- Runs: 1
- Persona drift MAE: 0.1769 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3133, E 0.1212, A 0.0667, N 0.2033
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2857
- Envelope violations: 6.0000
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0267
- Per-trait error delta: O +0.0000, C -0.1733, E +0.0063, A -0.0200, N +0.0534
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.2857

## Script-Level Summary
### new_product_launch:engine
- Runs: 1
- Persona drift MAE: 0.1692 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2400, E 0.1428, A 0.0600, N 0.2567
- Relationship inconsistency: 0.4500
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Mean turns: 11.00

### new_product_launch:engine_controller
- Runs: 1
- Persona drift MAE: 0.1502 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.1400, E 0.1275, A 0.0467, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### new_product_launch:naive
- Runs: 1
- Persona drift MAE: 0.1769 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3133, E 0.1212, A 0.0667, N 0.2033
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2857
- Envelope violations: 6.0000
- Mean turns: 11.00
