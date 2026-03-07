# Simulation Benchmark Report

## Suite Config
- Total runs: 18
- Conditions: naive, engine, engine_controller
- Script ids: new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine
- Runs: 6
- Persona drift MAE: 0.1856 (+/- 0.0108)
- Per-trait absolute error: O 0.1561, C 0.3189, E 0.1320, A 0.0767, N 0.2445
- Relationship inconsistency: 0.1825
- Commitment contradiction: 0.1419
- Envelope violations: 7.3333
- Mean turns: 11.00

### engine_controller
- Runs: 6
- Persona drift MAE: 0.1577 (+/- 0.0113)
- Per-trait absolute error: O 0.1228, C 0.2000, E 0.1615, A 0.0800, N 0.2244
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### naive
- Runs: 6
- Persona drift MAE: 0.1764 (+/- 0.0161)
- Per-trait absolute error: O 0.1550, C 0.2822, E 0.0924, A 0.0877, N 0.2645
- Relationship inconsistency: 0.0015
- Commitment contradiction: 0.1468
- Envelope violations: 6.0000
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0187
- Per-trait error delta: O -0.0322, C -0.0822, E +0.0691, A -0.0077, N -0.0401
- Relationship inconsistency delta: -0.0015
- Commitment contradiction delta: -0.1468

## Script-Level Summary
### new_product_launch:engine
- Runs: 3
- Persona drift MAE: 0.1878 (+/- 0.0040)
- Per-trait absolute error: O 0.1800, C 0.2778, E 0.1576, A 0.0756, N 0.2478
- Relationship inconsistency: 0.1650
- Commitment contradiction: 0.2004
- Envelope violations: 7.6667
- Mean turns: 11.00

### new_product_launch:engine_controller
- Runs: 3
- Persona drift MAE: 0.1594 (+/- 0.0080)
- Per-trait absolute error: O 0.1133, C 0.2222, E 0.1896, A 0.0555, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### new_product_launch:naive
- Runs: 3
- Persona drift MAE: 0.1653 (+/- 0.0115)
- Per-trait absolute error: O 0.1800, C 0.2245, E 0.0987, A 0.0666, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1429
- Envelope violations: 5.3333
- Mean turns: 11.00

### post_merger_integration:engine
- Runs: 3
- Persona drift MAE: 0.1835 (+/- 0.0144)
- Per-trait absolute error: O 0.1322, C 0.3600, E 0.1063, A 0.0778, N 0.2411
- Relationship inconsistency: 0.2000
- Commitment contradiction: 0.0833
- Envelope violations: 7.0000
- Mean turns: 11.00

### post_merger_integration:engine_controller
- Runs: 3
- Persona drift MAE: 0.1560 (+/- 0.0135)
- Per-trait absolute error: O 0.1322, C 0.1778, E 0.1333, A 0.1045, N 0.2322
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### post_merger_integration:naive
- Runs: 3
- Persona drift MAE: 0.1875 (+/- 0.0119)
- Per-trait absolute error: O 0.1300, C 0.3400, E 0.0861, A 0.1089, N 0.2722
- Relationship inconsistency: 0.0030
- Commitment contradiction: 0.1508
- Envelope violations: 6.6667
- Mean turns: 11.00
