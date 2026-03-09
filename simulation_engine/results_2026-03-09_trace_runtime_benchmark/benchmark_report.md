# Simulation Benchmark Report

## Suite Config
- Total runs: 8
- Conditions: engine_dialogue_only
- Script ids: new_product_launch, post_merger_integration, brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 2

## Condition Summary
### engine_dialogue_only
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1345 (+/- 0.0065)
- Clean persona drift MAE: 0.1345
- Per-trait absolute error: O 0.1158, C 0.1751, E 0.0718, A 0.0858, N 0.2242
- Relationship inconsistency: 0.0234
- Relationship shift rate: 0.2158
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.6250
- Clean envelope violations: 4.6250
- Structured action validity: 0.8334
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9613
- Planned action coverage: 1.0000
- Action family convergence: 0.5625
- Role action diversity: 0.6354
- Negotiation uniqueness: 0.3863
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0012
- Mean turns: 11.00
- Persona drift 95% CI: [0.13, 0.139]

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1400 (+/- 0.0053)
- Clean persona drift MAE: 0.1400
- Per-trait absolute error: O 0.1033, C 0.1990, E 0.0778, A 0.0934, N 0.2267
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2250
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1327, 0.1473]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### new_product_launch:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1360 (+/- 0.0081)
- Clean persona drift MAE: 0.1360
- Per-trait absolute error: O 0.1300, C 0.1620, E 0.1014, A 0.0700, N 0.2167
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.2170
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.5000
- Clean envelope violations: 3.5000
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
- Persona drift 95% CI: [0.1248, 0.1472]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### post_merger_integration:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1311 (+/- 0.0019)
- Clean persona drift MAE: 0.1311
- Per-trait absolute error: O 0.1333, C 0.1593, E 0.0597, A 0.0800, N 0.2233
- Relationship inconsistency: 0.0375
- Relationship shift rate: 0.2240
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1284, 0.1339]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### resource_reallocation_crunch:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1310 (+/- 0.0038)
- Clean persona drift MAE: 0.1310
- Per-trait absolute error: O 0.0967, C 0.1800, E 0.0484, A 0.1000, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1972
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1257, 0.1363]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1355 (+/- 0.0064)
- Clean persona drift MAE: 0.1355
- Per-trait absolute error: O 0.1000, C 0.1895, E 0.0631, A 0.0967, N 0.2283
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2111
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.8334
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.5625
- Role action diversity: 0.6459
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0014
- Mean turns: 11.00
- Persona drift 95% CI: [0.1292, 0.1418]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, negotiation_uniqueness, fallback_utterance_rate

### guided:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1336 (+/- 0.0064)
- Clean persona drift MAE: 0.1336
- Per-trait absolute error: O 0.1317, C 0.1607, E 0.0806, A 0.0750, N 0.2200
- Relationship inconsistency: 0.0469
- Relationship shift rate: 0.2205
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 4.2500
- Clean envelope violations: 4.2500
- Structured action validity: 0.8334
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9568
- Planned action coverage: 1.0000
- Action family convergence: 0.5625
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4091
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0012
- Mean turns: 11.00
- Persona drift 95% CI: [0.1273, 0.1398]

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1400 (+/- 0.0053)
- Clean persona drift MAE: 0.1400
- Per-trait absolute error: O 0.1033, C 0.1990, E 0.0778, A 0.0934, N 0.2267
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2250
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1327, 0.1473]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### integration_trust:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1311 (+/- 0.0019)
- Clean persona drift MAE: 0.1311
- Per-trait absolute error: O 0.1333, C 0.1593, E 0.0597, A 0.0800, N 0.2233
- Relationship inconsistency: 0.0375
- Relationship shift rate: 0.2240
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1284, 0.1339]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### launch_pressure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1360 (+/- 0.0081)
- Clean persona drift MAE: 0.1360
- Per-trait absolute error: O 0.1300, C 0.1620, E 0.1014, A 0.0700, N 0.2167
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.2170
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.5000
- Clean envelope violations: 3.5000
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
- Persona drift 95% CI: [0.1248, 0.1472]

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### resource_scarcity:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1310 (+/- 0.0038)
- Clean persona drift MAE: 0.1310
- Per-trait absolute error: O 0.0967, C 0.1800, E 0.0484, A 0.1000, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1972
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1257, 0.1363]

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate
