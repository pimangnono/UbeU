# Simulation Benchmark Report

## Suite Config
- Total runs: 27
- Conditions: naive, engine, engine_controller
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy
- Repetitions per condition: 3

## Condition Summary
### engine
- Runs: 9
- Persona drift MAE: 0.1907 (+/- 0.0148)
- Per-trait absolute error: O 0.1144, C 0.3522, E 0.2137, A 0.0830, N 0.1900
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1667
- Envelope violations: 6.6667
- Mean turns: 11.00

### engine_controller
- Runs: 9
- Persona drift MAE: 0.1625 (+/- 0.0187)
- Per-trait absolute error: O 0.1033, C 0.2693, E 0.2150, A 0.0674, N 0.1574
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.5556
- Mean turns: 11.00

### naive
- Runs: 9
- Persona drift MAE: 0.1895 (+/- 0.0180)
- Per-trait absolute error: O 0.0782, C 0.3715, E 0.1724, A 0.0978, N 0.2278
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.3146
- Envelope violations: 6.7778
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0270
- Per-trait error delta: O +0.0251, C -0.1022, E +0.0426, A -0.0304, N -0.0704
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.3146

## Script-Level Summary
### commuting_support_policy:engine
- Runs: 3
- Persona drift MAE: 0.1805 (+/- 0.0067)
- Per-trait absolute error: O 0.0967, C 0.3267, E 0.2147, A 0.0822, N 0.1822
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2833
- Envelope violations: 6.0000
- Mean turns: 11.00

### commuting_support_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1463 (+/- 0.0139)
- Per-trait absolute error: O 0.1145, C 0.1956, E 0.2036, A 0.0756, N 0.1422
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.6667
- Mean turns: 11.00

### commuting_support_policy:naive
- Runs: 3
- Persona drift MAE: 0.1729 (+/- 0.0155)
- Per-trait absolute error: O 0.0678, C 0.3089, E 0.1479, A 0.1133, N 0.2267
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.5270
- Envelope violations: 5.6667
- Mean turns: 11.00

### housing_support_policy:engine
- Runs: 3
- Persona drift MAE: 0.1924 (+/- 0.0026)
- Per-trait absolute error: O 0.1267, C 0.3678, E 0.2132, A 0.0767, N 0.1778
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0667
- Envelope violations: 6.0000
- Mean turns: 11.00

### housing_support_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1652 (+/- 0.0171)
- Per-trait absolute error: O 0.0867, C 0.3344, E 0.2217, A 0.0678, N 0.1156
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Mean turns: 11.00

### housing_support_policy:naive
- Runs: 3
- Persona drift MAE: 0.1980 (+/- 0.0084)
- Per-trait absolute error: O 0.0689, C 0.4278, E 0.1986, A 0.0767, N 0.2178
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1944
- Envelope violations: 7.0000
- Mean turns: 11.00

### youth_employment_policy:engine
- Runs: 3
- Persona drift MAE: 0.1991 (+/- 0.0206)
- Per-trait absolute error: O 0.1200, C 0.3622, E 0.2134, A 0.0900, N 0.2100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1500
- Envelope violations: 8.0000
- Mean turns: 11.00

### youth_employment_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1759 (+/- 0.0108)
- Per-trait absolute error: O 0.1089, C 0.2778, E 0.2196, A 0.0589, N 0.2144
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Mean turns: 11.00

### youth_employment_policy:naive
- Runs: 3
- Persona drift MAE: 0.1977 (+/- 0.0158)
- Per-trait absolute error: O 0.0978, C 0.3778, E 0.1708, A 0.1033, N 0.2389
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2222
- Envelope violations: 7.6667
- Mean turns: 11.00
