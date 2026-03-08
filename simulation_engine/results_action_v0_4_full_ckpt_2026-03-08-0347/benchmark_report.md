# Simulation Benchmark Report

## Suite Config
- Total runs: 39
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_action_v0
- Runs: 12
- Persona drift MAE: 0.1737 (+/- 0.0159)
- Per-trait absolute error: O 0.1325, C 0.2797, E 0.2193, A 0.0756, N 0.1611
- Relationship inconsistency: 0.0075
- Commitment contradiction: 0.0278
- Envelope violations: 6.1667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3055
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8438
- Role action diversity: 0.4687
- Negotiation uniqueness: 0.4166
- State trajectory variance: 0.0029
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 12
- Persona drift MAE: 0.1543 (+/- 0.0225)
- Per-trait absolute error: O 0.1042, C 0.2342, E 0.1855, A 0.0678, N 0.1800
- Relationship inconsistency: 0.0450
- Commitment contradiction: 0.0167
- Envelope violations: 5.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8438
- Role action diversity: 0.4687
- Negotiation uniqueness: 0.4166
- State trajectory variance: 0.0029
- Mean turns: 11.00

### naive_action_baseline
- Runs: 15
- Persona drift MAE: 0.1807 (+/- 0.0173)
- Per-trait absolute error: O 0.1093, C 0.3447, E 0.1289, A 0.0822, N 0.2385
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1084
- Envelope violations: 6.2000
- Structured action validity: 0.9917
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2889
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4917
- Role action diversity: 0.8074
- Negotiation uniqueness: 0.4444
- State trajectory variance: 0.0006
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): -0.0070
- Per-trait error delta: O +0.0232, C -0.0650, E +0.0904, A -0.0066, N -0.0774
- Relationship inconsistency delta: +0.0075
- Commitment contradiction delta: -0.0806
- Structured action validity delta: +0.0083
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.9682
- Action family convergence delta: +0.3521
- Role action diversity delta: -0.3387
- Negotiation uniqueness delta: -0.0278
- State trajectory variance delta: +0.0023

## Action Engine vs Dialogue-Only
- Persona drift delta (`controlled - baseline`): +0.0194
- Per-trait error delta: O +0.0283, C +0.0455, E +0.0338, A +0.0078, N -0.0189
- Relationship inconsistency delta: -0.0375
- Commitment contradiction delta: +0.0111
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.0000
- Action family convergence delta: +0.0000
- Role action diversity delta: +0.0000
- Negotiation uniqueness delta: +0.0000
- State trajectory variance delta: +0.0000

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1641 (+/- 0.0133)
- Per-trait absolute error: O 0.1211, C 0.2778, E 0.2192, A 0.0822, N 0.1200
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2222
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1255 (+/- 0.0104)
- Per-trait absolute error: O 0.1033, C 0.1400, E 0.1910, A 0.0689, N 0.1245
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0667
- Envelope violations: 3.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1111
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1830 (+/- 0.0077)
- Per-trait absolute error: O 0.0722, C 0.3889, E 0.1714, A 0.0822, N 0.2000
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1111
- Envelope violations: 6.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1111
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4167
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5000
- State trajectory variance: 0.0003
- Mean turns: 11.00

### housing_support_policy:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1790 (+/- 0.0017)
- Per-trait absolute error: O 0.1244, C 0.3922, E 0.2348, A 0.0456, N 0.0978
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00

### housing_support_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1690 (+/- 0.0115)
- Per-trait absolute error: O 0.1022, C 0.3211, E 0.1985, A 0.0900, N 0.1333
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.0000
- Envelope violations: 4.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2222
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00

### housing_support_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1900 (+/- 0.0040)
- Per-trait absolute error: O 0.0689, C 0.4256, E 0.1278, A 0.1233, N 0.2044
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0004
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1695 (+/- 0.0102)
- Per-trait absolute error: O 0.1689, C 0.1466, E 0.2129, A 0.1022, N 0.2167
- Relationship inconsistency: 0.0300
- Commitment contradiction: 0.0000
- Envelope violations: 6.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5556
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1538 (+/- 0.0159)
- Per-trait absolute error: O 0.1244, C 0.1889, E 0.1635, A 0.0622, N 0.2300
- Relationship inconsistency: 0.0300
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1820 (+/- 0.0015)
- Per-trait absolute error: O 0.1800, C 0.2933, E 0.1269, A 0.0533, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1310
- Envelope violations: 6.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.4444
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.8750
- Role action diversity: 0.6111
- Negotiation uniqueness: 0.5000
- State trajectory variance: 0.0009
- Mean turns: 11.00

### post_merger_integration:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1610 (+/- 0.0110)
- Per-trait absolute error: O 0.1300, C 0.2667, E 0.0718, A 0.0689, N 0.2678
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.3000
- Envelope violations: 5.3333
- Structured action validity: 0.9583
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.6667
- Role action diversity: 0.6898
- Negotiation uniqueness: 0.3889
- State trajectory variance: 0.0029
- Mean turns: 11.00

### youth_employment_policy:engine_action_v0
- Runs: 3
- Persona drift MAE: 0.1821 (+/- 0.0228)
- Per-trait absolute error: O 0.1156, C 0.3022, E 0.2105, A 0.0722, N 0.2100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1111
- Envelope violations: 6.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1111
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1689 (+/- 0.0167)
- Per-trait absolute error: O 0.0867, C 0.2867, E 0.1890, A 0.0500, N 0.2322
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1875 (+/- 0.0278)
- Per-trait absolute error: O 0.0956, C 0.3489, E 0.1467, A 0.0833, N 0.2633
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2222
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5000
- Role action diversity: 0.9028
- Negotiation uniqueness: 0.5000
- State trajectory variance: 0.0005
- Mean turns: 11.00
