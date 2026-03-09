# Simulation Benchmark Report

## Suite Config
- Total runs: 28
- Conditions: engine_dialogue_only
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration, brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 4

## Condition Summary
### engine_dialogue_only
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1201 (+/- 0.0129)
- Clean persona drift MAE: 0.1201
- Per-trait absolute error: O 0.1005, C 0.1706, E 0.0558, A 0.0762, N 0.1971
- Relationship inconsistency: 0.0214
- Relationship shift rate: 0.1880
- Relationship overshoot rate: 0.0482
- Commitment contradiction: 0.0179
- Clean commitment contradiction: 0.0179
- Envelope violations: 3.8214
- Clean envelope violations: 3.8214
- Structured action validity: 0.7976
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3929
- Action-plan alignment: 0.9597
- Planned action coverage: 1.0000
- Action family convergence: 0.7321
- Role action diversity: 0.5357
- Negotiation uniqueness: 0.3376
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0009
- Mean turns: 11.00
- Persona drift 95% CI: [0.1153, 0.1248]

- Zero-variance metrics: fallback_utterance_rate


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1268 (+/- 0.0055)
- Clean persona drift MAE: 0.1268
- Per-trait absolute error: O 0.0783, C 0.1633, E 0.0522, A 0.1000, N 0.2400
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1773
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.5000
- Clean envelope violations: 4.5000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1214, 0.1322]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### commuting_support_policy:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1056 (+/- 0.0134)
- Clean persona drift MAE: 0.1056
- Per-trait absolute error: O 0.0800, C 0.1849, E 0.0467, A 0.0867, N 0.1300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1725
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.0925, 0.1187]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### housing_support_policy:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1128 (+/- 0.0112)
- Clean persona drift MAE: 0.1128
- Per-trait absolute error: O 0.0817, C 0.1759, E 0.0733, A 0.0633, N 0.1700
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1638
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0625
- Clean commitment contradiction: 0.0625
- Envelope violations: 2.7500
- Clean envelope violations: 2.7500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1018, 0.1238]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### new_product_launch:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1214 (+/- 0.0103)
- Clean persona drift MAE: 0.1214
- Per-trait absolute error: O 0.1384, C 0.1382, E 0.0503, A 0.0367, N 0.2434
- Relationship inconsistency: 0.1313
- Relationship shift rate: 0.2462
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0625
- Clean commitment contradiction: 0.0625
- Envelope violations: 4.2500
- Clean envelope violations: 4.2500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1113, 0.1314]

- Zero-variance metrics: action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### post_merger_integration:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1288 (+/- 0.0066)
- Clean persona drift MAE: 0.1288
- Per-trait absolute error: O 0.1333, C 0.1850, E 0.0504, A 0.0583, N 0.2167
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2003
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.7500
- Clean envelope violations: 4.7500
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1223, 0.1352]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### resource_reallocation_crunch:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1322 (+/- 0.0071)
- Clean persona drift MAE: 0.1322
- Per-trait absolute error: O 0.0917, C 0.1838, E 0.0437, A 0.1050, N 0.2366
- Relationship inconsistency: 0.0187
- Relationship shift rate: 0.2027
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.7500
- Clean envelope violations: 4.7500
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1252, 0.1392]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### youth_employment_policy:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1129 (+/- 0.0070)
- Clean persona drift MAE: 0.1129
- Per-trait absolute error: O 0.1000, C 0.1633, E 0.0743, A 0.0833, N 0.1433
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1533
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.2500
- Clean envelope violations: 3.2500
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.106, 0.1197]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1295 (+/- 0.0069)
- Clean persona drift MAE: 0.1295
- Per-trait absolute error: O 0.0850, C 0.1736, E 0.0479, A 0.1025, N 0.2383
- Relationship inconsistency: 0.0094
- Relationship shift rate: 0.1900
- Relationship overshoot rate: 0.0563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.6250
- Clean envelope violations: 4.6250
- Structured action validity: 0.5834
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5625
- Role action diversity: 0.6459
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0014
- Mean turns: 11.00
- Persona drift 95% CI: [0.1247, 0.1343]

- Zero-variance metrics: commitment_contradiction, negotiation_uniqueness, fallback_utterance_rate

### guided:engine_dialogue_only
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1163 (+/- 0.0128)
- Clean persona drift MAE: 0.1163
- Per-trait absolute error: O 0.1067, C 0.1695, E 0.0590, A 0.0657, N 0.1807
- Relationship inconsistency: 0.0262
- Relationship shift rate: 0.1872
- Relationship overshoot rate: 0.0450
- Commitment contradiction: 0.0250
- Clean commitment contradiction: 0.0250
- Envelope violations: 3.5000
- Clean envelope violations: 3.5000
- Structured action validity: 0.8833
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1500
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.4917
- Negotiation uniqueness: 0.3272
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0010
- Mean turns: 11.00
- Persona drift 95% CI: [0.1107, 0.1219]

- Zero-variance metrics: fallback_utterance_rate


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1268 (+/- 0.0055)
- Clean persona drift MAE: 0.1268
- Per-trait absolute error: O 0.0783, C 0.1633, E 0.0522, A 0.1000, N 0.2400
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1773
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.5000
- Clean envelope violations: 4.5000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1214, 0.1322]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### integration_trust:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1288 (+/- 0.0066)
- Clean persona drift MAE: 0.1288
- Per-trait absolute error: O 0.1333, C 0.1850, E 0.0504, A 0.0583, N 0.2167
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2003
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.7500
- Clean envelope violations: 4.7500
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1223, 0.1352]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### launch_pressure:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1214 (+/- 0.0103)
- Clean persona drift MAE: 0.1214
- Per-trait absolute error: O 0.1384, C 0.1382, E 0.0503, A 0.0367, N 0.2434
- Relationship inconsistency: 0.1313
- Relationship shift rate: 0.2462
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0625
- Clean commitment contradiction: 0.0625
- Envelope violations: 4.2500
- Clean envelope violations: 4.2500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1113, 0.1314]

- Zero-variance metrics: action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### policy_spillover:engine_dialogue_only
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1104 (+/- 0.0114)
- Clean persona drift MAE: 0.1104
- Per-trait absolute error: O 0.0872, C 0.1747, E 0.0648, A 0.0778, N 0.1478
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1632
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0208
- Clean commitment contradiction: 0.0208
- Envelope violations: 2.8333
- Clean envelope violations: 2.8333
- Structured action validity: 0.9167
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9530
- Planned action coverage: 1.0000
- Action family convergence: 0.9583
- Role action diversity: 0.4028
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0004
- Mean turns: 11.00
- Persona drift 95% CI: [0.104, 0.1169]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, negotiation_uniqueness, fallback_utterance_rate

### resource_scarcity:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1322 (+/- 0.0071)
- Clean persona drift MAE: 0.1322
- Per-trait absolute error: O 0.0917, C 0.1838, E 0.0437, A 0.1050, N 0.2366
- Relationship inconsistency: 0.0187
- Relationship shift rate: 0.2027
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.7500
- Clean envelope violations: 4.7500
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1252, 0.1392]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate
