# Simulation Benchmark Report

## Suite Config
- Total runs: 63
- Conditions: naive, engine, engine_controller, engine_controller_no_trait_poles, engine_controller_no_banded_target_matching, engine_controller_no_extended_ledger, engine_controller_no_tie_routing
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy
- Repetitions per condition: 3

## Condition Summary
### engine
- Runs: 9
- Persona drift MAE: 0.1866 (+/- 0.0277)
- Per-trait absolute error: O 0.1063, C 0.3241, E 0.2097, A 0.0926, N 0.2004
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0278
- Envelope violations: 6.6667
- Mean turns: 11.00

### engine_controller
- Runs: 9
- Persona drift MAE: 0.1493 (+/- 0.0218)
- Per-trait absolute error: O 0.0841, C 0.2389, E 0.2022, A 0.0711, N 0.1500
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0159
- Envelope violations: 4.3333
- Mean turns: 11.00

### engine_controller_no_banded_target_matching
- Runs: 9
- Persona drift MAE: 0.1596 (+/- 0.0267)
- Per-trait absolute error: O 0.0900, C 0.2737, E 0.2338, A 0.0800, N 0.1204
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.8889
- Mean turns: 11.00

### engine_controller_no_extended_ledger
- Runs: 9
- Persona drift MAE: 0.1637 (+/- 0.0187)
- Per-trait absolute error: O 0.1041, C 0.2744, E 0.2424, A 0.0681, N 0.1293
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0370
- Envelope violations: 5.4444
- Mean turns: 11.00

### engine_controller_no_tie_routing
- Runs: 9
- Persona drift MAE: 0.1618 (+/- 0.0286)
- Per-trait absolute error: O 0.0981, C 0.2574, E 0.2084, A 0.0755, N 0.1693
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Mean turns: 11.00

### engine_controller_no_trait_poles
- Runs: 9
- Persona drift MAE: 0.1645 (+/- 0.0251)
- Per-trait absolute error: O 0.1078, C 0.2737, E 0.2253, A 0.0637, N 0.1522
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.3333
- Mean turns: 11.00

### naive
- Runs: 9
- Persona drift MAE: 0.1947 (+/- 0.0128)
- Per-trait absolute error: O 0.0893, C 0.3930, E 0.1537, A 0.1015, N 0.2359
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1815
- Envelope violations: 6.4444
- Mean turns: 11.00


## Engine vs Naive
- Persona drift delta (`engine_controller - naive`): -0.0454
- Per-trait error delta: O -0.0052, C -0.1541, E +0.0485, A -0.0304, N -0.0859
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.1656

## Script-Level Summary
### commuting_support_policy:engine
- Runs: 3
- Persona drift MAE: 0.1571 (+/- 0.0123)
- Per-trait absolute error: O 0.0833, C 0.2200, E 0.1935, A 0.0889, N 0.2000
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Mean turns: 11.00

### commuting_support_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1415 (+/- 0.0195)
- Per-trait absolute error: O 0.0678, C 0.2156, E 0.1863, A 0.0778, N 0.1600
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.3333
- Mean turns: 11.00

### commuting_support_policy:engine_controller_no_banded_target_matching
- Runs: 3
- Persona drift MAE: 0.1314 (+/- 0.0185)
- Per-trait absolute error: O 0.0989, C 0.1889, E 0.1871, A 0.0578, N 0.1245
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Mean turns: 11.00

### commuting_support_policy:engine_controller_no_extended_ledger
- Runs: 3
- Persona drift MAE: 0.1469 (+/- 0.0072)
- Per-trait absolute error: O 0.0856, C 0.1933, E 0.2242, A 0.0800, N 0.1511
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1111
- Envelope violations: 3.6667
- Mean turns: 11.00

### commuting_support_policy:engine_controller_no_tie_routing
- Runs: 3
- Persona drift MAE: 0.1296 (+/- 0.0048)
- Per-trait absolute error: O 0.1078, C 0.1667, E 0.1824, A 0.0667, N 0.1244
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.3333
- Mean turns: 11.00

### commuting_support_policy:engine_controller_no_trait_poles
- Runs: 3
- Persona drift MAE: 0.1426 (+/- 0.0132)
- Per-trait absolute error: O 0.1167, C 0.1911, E 0.1921, A 0.0822, N 0.1311
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Mean turns: 11.00

### commuting_support_policy:naive
- Runs: 3
- Persona drift MAE: 0.1812 (+/- 0.0037)
- Per-trait absolute error: O 0.0722, C 0.3933, E 0.1361, A 0.0956, N 0.2089
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.3500
- Envelope violations: 5.6667
- Mean turns: 11.00

### housing_support_policy:engine
- Runs: 3
- Persona drift MAE: 0.1911 (+/- 0.0194)
- Per-trait absolute error: O 0.1111, C 0.3655, E 0.2021, A 0.0989, N 0.1778
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### housing_support_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1523 (+/- 0.0281)
- Per-trait absolute error: O 0.0867, C 0.2545, E 0.2148, A 0.0722, N 0.1333
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.3333
- Mean turns: 11.00

### housing_support_policy:engine_controller_no_banded_target_matching
- Runs: 3
- Persona drift MAE: 0.1836 (+/- 0.0173)
- Per-trait absolute error: O 0.1044, C 0.3478, E 0.2492, A 0.1011, N 0.1156
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Mean turns: 11.00

### housing_support_policy:engine_controller_no_extended_ledger
- Runs: 3
- Persona drift MAE: 0.1753 (+/- 0.0066)
- Per-trait absolute error: O 0.1156, C 0.3633, E 0.2409, A 0.0855, N 0.0711
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Mean turns: 11.00

### housing_support_policy:engine_controller_no_tie_routing
- Runs: 3
- Persona drift MAE: 0.1591 (+/- 0.0081)
- Per-trait absolute error: O 0.0867, C 0.3011, E 0.2088, A 0.0789, N 0.1200
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Mean turns: 11.00

### housing_support_policy:engine_controller_no_trait_poles
- Runs: 3
- Persona drift MAE: 0.1768 (+/- 0.0259)
- Per-trait absolute error: O 0.1267, C 0.3256, E 0.2505, A 0.0567, N 0.1244
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### housing_support_policy:naive
- Runs: 3
- Persona drift MAE: 0.1997 (+/- 0.0083)
- Per-trait absolute error: O 0.1089, C 0.3878, E 0.1784, A 0.1011, N 0.2222
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0833
- Envelope violations: 6.0000
- Mean turns: 11.00

### youth_employment_policy:engine
- Runs: 3
- Persona drift MAE: 0.2116 (+/- 0.0163)
- Per-trait absolute error: O 0.1244, C 0.3867, E 0.2336, A 0.0900, N 0.2234
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0833
- Envelope violations: 8.3333
- Mean turns: 11.00

### youth_employment_policy:engine_controller
- Runs: 3
- Persona drift MAE: 0.1540 (+/- 0.0125)
- Per-trait absolute error: O 0.0978, C 0.2467, E 0.2055, A 0.0634, N 0.1567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0476
- Envelope violations: 5.3333
- Mean turns: 11.00

### youth_employment_policy:engine_controller_no_banded_target_matching
- Runs: 3
- Persona drift MAE: 0.1637 (+/- 0.0105)
- Per-trait absolute error: O 0.0667, C 0.2844, E 0.2652, A 0.0811, N 0.1211
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### youth_employment_policy:engine_controller_no_extended_ledger
- Runs: 3
- Persona drift MAE: 0.1689 (+/- 0.0225)
- Per-trait absolute error: O 0.1111, C 0.2667, E 0.2620, A 0.0389, N 0.1656
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Mean turns: 11.00

### youth_employment_policy:engine_controller_no_tie_routing
- Runs: 3
- Persona drift MAE: 0.1966 (+/- 0.0108)
- Per-trait absolute error: O 0.1000, C 0.3045, E 0.2341, A 0.0811, N 0.2633
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Mean turns: 11.00

### youth_employment_policy:engine_controller_no_trait_poles
- Runs: 3
- Persona drift MAE: 0.1742 (+/- 0.0180)
- Per-trait absolute error: O 0.0800, C 0.3045, E 0.2332, A 0.0522, N 0.2011
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Mean turns: 11.00

### youth_employment_policy:naive
- Runs: 3
- Persona drift MAE: 0.2031 (+/- 0.0115)
- Per-trait absolute error: O 0.0867, C 0.3978, E 0.1464, A 0.1078, N 0.2767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1111
- Envelope violations: 7.6667
- Mean turns: 11.00
