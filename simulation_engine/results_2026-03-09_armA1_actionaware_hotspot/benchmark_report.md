# Simulation Benchmark Report

## Suite Config
- Total runs: 12
- Conditions: engine_action_v0
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch
- Repetitions per condition: 3

## Condition Summary
### engine_action_v0
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1211 (+/- 0.0118)
- Clean persona drift MAE: 0.1211
- Per-trait absolute error: O 0.1192, C 0.1665, E 0.0671, A 0.0717, N 0.1811
- Relationship inconsistency: 0.0438
- Relationship shift rate: 0.1966
- Relationship overshoot rate: 0.0375
- Commitment contradiction: 0.0139
- Clean commitment contradiction: 0.0139
- Envelope violations: 3.8333
- Clean envelope violations: 3.8333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9568
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0008
- Mean turns: 11.00
- Persona drift 95% CI: [0.1144, 0.1278]

- Zero-variance metrics: negotiation_uniqueness, fallback_utterance_rate


## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1148 (+/- 0.0060)
- Clean persona drift MAE: 0.1148
- Per-trait absolute error: O 0.1278, C 0.1800, E 0.0530, A 0.0666, N 0.1467
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1219
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.3333
- Clean envelope violations: 3.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.108, 0.1216]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### housing_support_policy:engine_action_v0
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1128 (+/- 0.0042)
- Clean persona drift MAE: 0.1128
- Per-trait absolute error: O 0.0689, C 0.1762, E 0.0733, A 0.0722, N 0.1733
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1611
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Clean envelope violations: 3.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1081, 0.1175]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### new_product_launch:engine_action_v0
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1256 (+/- 0.0137)
- Clean persona drift MAE: 0.1256
- Per-trait absolute error: O 0.1355, C 0.1339, E 0.0643, A 0.0644, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2029
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0556
- Clean commitment contradiction: 0.0556
- Envelope violations: 4.0000
- Clean envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0003
- Mean turns: 11.00
- Persona drift 95% CI: [0.1101, 0.1412]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### youth_employment_policy:engine_action_v0
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1312 (+/- 0.0091)
- Clean persona drift MAE: 0.1312
- Per-trait absolute error: O 0.1444, C 0.1758, E 0.0778, A 0.0833, N 0.1745
- Relationship inconsistency: 0.1750
- Relationship shift rate: 0.3006
- Relationship overshoot rate: 0.1500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1208, 0.1415]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate


## Mode Summary
### guided:engine_action_v0
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1211 (+/- 0.0118)
- Clean persona drift MAE: 0.1211
- Per-trait absolute error: O 0.1192, C 0.1665, E 0.0671, A 0.0717, N 0.1811
- Relationship inconsistency: 0.0438
- Relationship shift rate: 0.1966
- Relationship overshoot rate: 0.0375
- Commitment contradiction: 0.0139
- Clean commitment contradiction: 0.0139
- Envelope violations: 3.8333
- Clean envelope violations: 3.8333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9568
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0008
- Mean turns: 11.00
- Persona drift 95% CI: [0.1144, 0.1278]

- Zero-variance metrics: negotiation_uniqueness, fallback_utterance_rate


## Family Summary
### launch_pressure:engine_action_v0
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1256 (+/- 0.0137)
- Clean persona drift MAE: 0.1256
- Per-trait absolute error: O 0.1355, C 0.1339, E 0.0643, A 0.0644, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2029
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0556
- Clean commitment contradiction: 0.0556
- Envelope violations: 4.0000
- Clean envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0003
- Mean turns: 11.00
- Persona drift 95% CI: [0.1101, 0.1412]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### policy_spillover:engine_action_v0
- Runs: 9
- Clean runs: 9
- Contaminated runs: 0
- Persona drift MAE: 0.1196 (+/- 0.0107)
- Clean persona drift MAE: 0.1196
- Per-trait absolute error: O 0.1137, C 0.1773, E 0.0680, A 0.0741, N 0.1648
- Relationship inconsistency: 0.0583
- Relationship shift rate: 0.1945
- Relationship overshoot rate: 0.0500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.7778
- Clean envelope violations: 3.7778
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9576
- Planned action coverage: 1.0000
- Action family convergence: 0.8333
- Role action diversity: 0.4861
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0005
- Mean turns: 11.00
- Persona drift 95% CI: [0.1126, 0.1265]

- Zero-variance metrics: commitment_contradiction, negotiation_uniqueness, fallback_utterance_rate
