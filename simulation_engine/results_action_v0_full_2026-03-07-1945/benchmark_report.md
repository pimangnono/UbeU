# Simulation Benchmark Report

## Suite Config
- Total runs: 45
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_action_v0
- Runs: 15
- Persona drift MAE: 0.1676 (+/- 0.0249)
- Per-trait absolute error: O 0.1178, C 0.2478, E 0.1905, A 0.0760, N 0.2060
- Relationship inconsistency: 0.0961
- Commitment contradiction: 0.0000
- Envelope violations: 6.4000
- Structured action validity: 0.5282
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0667
- State transition coherence: 1.0000
- Action feedback utilization: 0.5555
- State trajectory variance: 0.0014
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 15
- Persona drift MAE: 0.1692 (+/- 0.0180)
- Per-trait absolute error: O 0.1182, C 0.2642, E 0.1725, A 0.0827, N 0.2082
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0267
- Envelope violations: 5.6000
- Structured action validity: 0.5894
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5333
- State trajectory variance: 0.0008
- Mean turns: 11.00

### naive_action_baseline
- Runs: 15
- Persona drift MAE: 0.1793 (+/- 0.0241)
- Per-trait absolute error: O 0.1098, C 0.3078, E 0.1426, A 0.0898, N 0.2465
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2897
- Envelope violations: 6.0000
- Structured action validity: 0.4957
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.1000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): -0.0117
- Per-trait error delta: O +0.0080, C -0.0600, E +0.0479, A -0.0138, N -0.0405
- Relationship inconsistency delta: +0.0961
- Commitment contradiction delta: -0.2897
- Structured action validity delta: +0.0325
- Executed action contradiction delta: +0.0667
- State trajectory variance delta: +0.0014

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1387 (+/- 0.0217)
- Per-trait absolute error: O 0.0878, C 0.1511, E 0.2347, A 0.0667, N 0.1533
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 0.5348
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.3333
- State transition coherence: 1.0000
- Action feedback utilization: 0.2222
- State trajectory variance: 0.0003
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1511 (+/- 0.0168)
- Per-trait absolute error: O 0.1122, C 0.2155, E 0.1633, A 0.0822, N 0.1822
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1333
- Envelope violations: 5.0000
- Structured action validity: 0.5937
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3889
- State trajectory variance: 0.0004
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1691 (+/- 0.0070)
- Per-trait absolute error: O 0.1056, C 0.2755, E 0.1357, A 0.1022, N 0.2267
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.4444
- Envelope violations: 5.6667
- Structured action validity: 0.6389
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0008
- Mean turns: 11.00

### housing_support_policy:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1940 (+/- 0.0095)
- Per-trait absolute error: O 0.1089, C 0.3922, E 0.2143, A 0.0811, N 0.1733
- Relationship inconsistency: 0.1833
- Commitment contradiction: 0.0000
- Envelope violations: 6.6667
- Structured action validity: 0.6815
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.4444
- State trajectory variance: 0.0014
- Mean turns: 11.00

### housing_support_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1714 (+/- 0.0085)
- Per-trait absolute error: O 0.1089, C 0.3456, E 0.1992, A 0.0789, N 0.1244
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.3333
- Structured action validity: 0.5741
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- State trajectory variance: 0.0006
- Mean turns: 11.00

### housing_support_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1974 (+/- 0.0209)
- Per-trait absolute error: O 0.0578, C 0.4233, E 0.1739, A 0.0833, N 0.2489
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2222
- Envelope violations: 6.3333
- Structured action validity: 0.2778
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1825 (+/- 0.0170)
- Per-trait absolute error: O 0.1689, C 0.2111, E 0.2005, A 0.0800, N 0.2522
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Structured action validity: 0.2929
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- State trajectory variance: 0.0017
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1934 (+/- 0.0078)
- Per-trait absolute error: O 0.1578, C 0.2778, E 0.2169, A 0.0844, N 0.2300
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.4762
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5556
- State trajectory variance: 0.0016
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1811 (+/- 0.0053)
- Per-trait absolute error: O 0.1578, C 0.2667, E 0.1488, A 0.0844, N 0.2478
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.3651
- Envelope violations: 5.3333
- Structured action validity: 0.3750
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1501 (+/- 0.0099)
- Per-trait absolute error: O 0.1322, C 0.2045, E 0.1016, A 0.0800, N 0.2322
- Relationship inconsistency: 0.1750
- Commitment contradiction: 0.0000
- Envelope violations: 5.3333
- Structured action validity: 0.4242
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0057
- Mean turns: 11.00

### post_merger_integration:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1652 (+/- 0.0101)
- Per-trait absolute error: O 0.1322, C 0.2533, E 0.0858, A 0.0867, N 0.2678
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.3333
- Structured action validity: 0.6019
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- State trajectory variance: 0.0056
- Mean turns: 11.00

### post_merger_integration:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1534 (+/- 0.0157)
- Per-trait absolute error: O 0.1300, C 0.2222, E 0.0603, A 0.0867, N 0.2678
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.4167
- Envelope violations: 5.0000
- Structured action validity: 0.6250
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0003
- Mean turns: 11.00

### youth_employment_policy:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1727 (+/- 0.0078)
- Per-trait absolute error: O 0.0911, C 0.2800, E 0.2013, A 0.0722, N 0.2189
- Relationship inconsistency: 0.1222
- Commitment contradiction: 0.0000
- Envelope violations: 7.6667
- Structured action validity: 0.7074
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.4444
- State trajectory variance: 0.0006
- Mean turns: 11.00

### youth_employment_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1648 (+/- 0.0125)
- Per-trait absolute error: O 0.0800, C 0.2289, E 0.1973, A 0.0811, N 0.2367
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.3333
- Structured action validity: 0.7011
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3889
- State trajectory variance: 0.0011
- Mean turns: 11.00

### youth_employment_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1953 (+/- 0.0278)
- Per-trait absolute error: O 0.0978, C 0.3511, E 0.1942, A 0.0922, N 0.2411
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.6667
- Structured action validity: 0.5619
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- State trajectory variance: 0.0006
- Mean turns: 11.00
