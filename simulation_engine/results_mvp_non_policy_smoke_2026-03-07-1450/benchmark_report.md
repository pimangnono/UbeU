# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive, engine, engine_controller
- Script ids: new_product_launch, post_merger_integration
- Repetitions per condition: 1

## Condition Summary
### engine
- Runs: 2
- Persona drift MAE: 0.1840 (+/- 0.0169)
- Per-trait absolute error: O 0.1416, C 0.2633, E 0.1817, A 0.0733, N 0.2600
- Relationship inconsistency: 0.2250
- Commitment contradiction: 0.0714
- Envelope violations: 7.5000
- Mean turns: 11.00

### engine_controller
- Runs: 2
- Persona drift MAE: 0.1572 (+/- 0.0158)
- Per-trait absolute error: O 0.1550, C 0.2167, E 0.1110, A 0.0833, N 0.2200
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.5000
- Mean turns: 11.00

### naive
- Runs: 2
- Persona drift MAE: 0.1875 (+/- 0.0016)
- Per-trait absolute error: O 0.1550, C 0.3667, E 0.0727, A 0.0766, N 0.2667
- Relationship inconsistency: 0.1875
- Commitment contradiction: 0.1625
- Envelope violations: 6.5000
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0303
- Per-trait error delta: O +0.0000, C -0.1500, E +0.0383, A +0.0067, N -0.0467
- Relationship inconsistency delta: -0.1875
- Commitment contradiction delta: -0.1625

## Script-Level Summary
### new_product_launch:engine
- Runs: 1
- Persona drift MAE: 0.2009 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3267, E 0.2211, A 0.0333, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 9.0000
- Mean turns: 11.00

### new_product_launch:engine_controller
- Runs: 1
- Persona drift MAE: 0.1730 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.2800, E 0.1349, A 0.0533, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Mean turns: 11.00

### new_product_launch:naive
- Runs: 1
- Persona drift MAE: 0.1891 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.3667, E 0.1024, A 0.0400, N 0.2567
- Relationship inconsistency: 0.2250
- Commitment contradiction: 0.1250
- Envelope violations: 7.0000
- Mean turns: 11.00

### post_merger_integration:engine
- Runs: 1
- Persona drift MAE: 0.1672 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.2000, E 0.1424, A 0.1133, N 0.2767
- Relationship inconsistency: 0.4500
- Commitment contradiction: 0.1429
- Envelope violations: 6.0000
- Mean turns: 11.00

### post_merger_integration:engine_controller
- Runs: 1
- Persona drift MAE: 0.1414 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.1533, E 0.0872, A 0.1133, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Mean turns: 11.00

### post_merger_integration:naive
- Runs: 1
- Persona drift MAE: 0.1859 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.3667, E 0.0430, A 0.1133, N 0.2767
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.2000
- Envelope violations: 6.0000
- Mean turns: 11.00
