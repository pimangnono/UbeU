# Simulation Benchmark Report

## Suite Config
- Total runs: 12
- Conditions: engine_dialogue_only
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1160 (+/- 0.0119)
- Clean persona drift MAE: 0.1160
- Per-trait absolute error: O 0.0958, C 0.1620, E 0.0634, A 0.0778, N 0.1811
- Relationship inconsistency: 0.0458
- Relationship shift rate: 0.1701
- Relationship overshoot rate: 0.0375
- Commitment contradiction: 0.0863
- Clean commitment contradiction: 0.0863
- Envelope violations: 3.2500
- Clean envelope violations: 3.2500
- Structured action validity: 0.9500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9579
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0076
- Fallback taxonomy: empty_pool_fallback 0.0076
- State trajectory variance: 0.0006
- Mean turns: 11.00
- Persona drift 95% CI: [0.1093, 0.1228]


## Script-Level Summary
### commuting_support_policy:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1020 (+/- 0.0034)
- Clean persona drift MAE: 0.1020
- Per-trait absolute error: O 0.0744, C 0.1604, E 0.0549, A 0.0867, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1456
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.0982, 0.1058]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### housing_support_policy:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1232 (+/- 0.0136)
- Clean persona drift MAE: 0.1232
- Per-trait absolute error: O 0.0978, C 0.1771, E 0.0733, A 0.0989, N 0.1689
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1656
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.2500
- Clean commitment contradiction: 0.2500
- Envelope violations: 3.6667
- Clean envelope violations: 3.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1078, 0.1386]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### new_product_launch:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1233 (+/- 0.0076)
- Clean persona drift MAE: 0.1233
- Per-trait absolute error: O 0.1356, C 0.1473, E 0.0435, A 0.0600, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1684
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0476
- Clean commitment contradiction: 0.0476
- Envelope violations: 3.6667
- Clean envelope violations: 3.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1147, 0.1319]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### youth_employment_policy:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1157 (+/- 0.0030)
- Clean persona drift MAE: 0.1157
- Per-trait absolute error: O 0.0756, C 0.1632, E 0.0819, A 0.0655, N 0.1922
- Relationship inconsistency: 0.1833
- Relationship shift rate: 0.2008
- Relationship overshoot rate: 0.1500
- Commitment contradiction: 0.0476
- Clean commitment contradiction: 0.0476
- Envelope violations: 3.3333
- Clean envelope violations: 3.3333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0303
- Fallback taxonomy: empty_pool_fallback 0.0303
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1123, 0.1191]

- Zero-variance metrics: action_family_convergence, role_action_diversity, negotiation_uniqueness


## Mode Summary
### guided:engine_dialogue_only
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1160 (+/- 0.0119)
- Clean persona drift MAE: 0.1160
- Per-trait absolute error: O 0.0958, C 0.1620, E 0.0634, A 0.0778, N 0.1811
- Relationship inconsistency: 0.0458
- Relationship shift rate: 0.1701
- Relationship overshoot rate: 0.0375
- Commitment contradiction: 0.0863
- Clean commitment contradiction: 0.0863
- Envelope violations: 3.2500
- Clean envelope violations: 3.2500
- Structured action validity: 0.9500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9579
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0076
- Fallback taxonomy: empty_pool_fallback 0.0076
- State trajectory variance: 0.0006
- Mean turns: 11.00
- Persona drift 95% CI: [0.1093, 0.1228]


## Family Summary
### launch_pressure:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1233 (+/- 0.0076)
- Clean persona drift MAE: 0.1233
- Per-trait absolute error: O 0.1356, C 0.1473, E 0.0435, A 0.0600, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1684
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0476
- Clean commitment contradiction: 0.0476
- Envelope violations: 3.6667
- Clean envelope violations: 3.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1147, 0.1319]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### policy_spillover:engine_dialogue_only
- Runs: 9
- Clean runs: 9
- Contaminated runs: 0
- Persona drift MAE: 0.1136 (+/- 0.0121)
- Clean persona drift MAE: 0.1136
- Per-trait absolute error: O 0.0826, C 0.1669, E 0.0701, A 0.0837, N 0.1648
- Relationship inconsistency: 0.0611
- Relationship shift rate: 0.1707
- Relationship overshoot rate: 0.0500
- Commitment contradiction: 0.0992
- Clean commitment contradiction: 0.0992
- Envelope violations: 3.1111
- Clean envelope violations: 3.1111
- Structured action validity: 0.9333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.8333
- Role action diversity: 0.4861
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0101
- Fallback taxonomy: empty_pool_fallback 0.0101
- State trajectory variance: 0.0002
- Mean turns: 11.00
- Persona drift 95% CI: [0.1057, 0.1215]

- Zero-variance metrics: negotiation_uniqueness
