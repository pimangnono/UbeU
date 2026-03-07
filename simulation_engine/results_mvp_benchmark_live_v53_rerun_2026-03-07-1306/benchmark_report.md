# Simulation Benchmark Report

## Suite Config
- Total runs: 27
- Conditions: naive, engine, engine_controller
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy
- Repetitions per condition: 3

## Condition Summary
### engine
- Runs: 9
- Persona drift MAE: 0.1915 (+/- 0.0174)
- Per-trait absolute error: O 0.0952, C 0.3404, E 0.2224, A 0.0815, N 0.2181
- Relationship inconsistency: 0.0250
- Commitment contradiction: 0.1018
- Envelope violations: 7.1111
- Mean turns: 11.00

### engine_controller
- Runs: 9
- Persona drift MAE: 0.1584 (+/- 0.0149)
- Per-trait absolute error: O 0.0930, C 0.2485, E 0.1978, A 0.0748, N 0.1782
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.2222
- Mean turns: 11.00

### naive
- Runs: 9
- Persona drift MAE: 0.1891 (+/- 0.0202)
- Per-trait absolute error: O 0.0922, C 0.3804, E 0.1576, A 0.0867, N 0.2285
- Relationship inconsistency: 0.0306
- Commitment contradiction: 0.1204
- Envelope violations: 6.6667
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0307
- Per-trait error delta: O +0.0008, C -0.1319, E +0.0402, A -0.0119, N -0.0503
- Relationship inconsistency delta: -0.0306
- Commitment contradiction delta: -0.1204

## Script-Level Summary
### commuting_support_policy:engine
- Runs: 3
- Persona drift MAE: 0.1722 (+/- 0.0077)
- Per-trait absolute error: O 0.0789, C 0.2511, E 0.2355, A 0.0911, N 0.2044
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.3055
- Envelope violations: 6.0000
- Mean turns: 11.00

### commuting_support_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1437 (+/- 0.0157)
- Per-trait absolute error: O 0.0900, C 0.1911, E 0.2039, A 0.0867, N 0.1467
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Mean turns: 11.00

### commuting_support_policy:naive
- Runs: 3
- Persona drift MAE: 0.1734 (+/- 0.0261)
- Per-trait absolute error: O 0.0944, C 0.3267, E 0.1548, A 0.0911, N 0.2000
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1111
- Envelope violations: 6.0000
- Mean turns: 11.00

### housing_support_policy:engine
- Runs: 3
- Persona drift MAE: 0.2039 (+/- 0.0135)
- Per-trait absolute error: O 0.1156, C 0.4078, E 0.2241, A 0.0811, N 0.1911
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Mean turns: 11.00

### housing_support_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1713 (+/- 0.0047)
- Per-trait absolute error: O 0.1045, C 0.3522, E 0.1941, A 0.0722, N 0.1334
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Mean turns: 11.00

### housing_support_policy:naive
- Runs: 3
- Persona drift MAE: 0.2032 (+/- 0.0036)
- Per-trait absolute error: O 0.1022, C 0.4367, E 0.1628, A 0.0967, N 0.2178
- Relationship inconsistency: 0.0917
- Commitment contradiction: 0.2500
- Envelope violations: 6.6667
- Mean turns: 11.00

### youth_employment_policy:engine
- Runs: 3
- Persona drift MAE: 0.1984 (+/- 0.0094)
- Per-trait absolute error: O 0.0911, C 0.3622, E 0.2078, A 0.0722, N 0.2589
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.0000
- Envelope violations: 8.3333
- Mean turns: 11.00

### youth_employment_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1604 (+/- 0.0033)
- Per-trait absolute error: O 0.0845, C 0.2022, E 0.1953, A 0.0655, N 0.2544
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.6667
- Mean turns: 11.00

### youth_employment_policy:naive
- Runs: 3
- Persona drift MAE: 0.1906 (+/- 0.0087)
- Per-trait absolute error: O 0.0800, C 0.3778, E 0.1552, A 0.0722, N 0.2678
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Mean turns: 11.00
