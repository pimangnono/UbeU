# Simulation Benchmark Report

## Suite Config
- Total runs: 12
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0146)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1250, C 0.2567, E 0.1480, A 0.0778, N 0.2222
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.0208
- Clean commitment contradiction: 0.0208
- Envelope violations: 6.1667
- Clean envelope violations: 6.1667
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0011
- Mean turns: 11.00

### naive_action_baseline
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1897 (+/- 0.0161)
- Clean persona drift MAE: 0.1897
- Per-trait absolute error: O 0.1561, C 0.3167, E 0.1002, A 0.1089, N 0.2667
- Relationship inconsistency: 0.1096
- Commitment contradiction: 0.2133
- Clean commitment contradiction: 0.2133
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5972
- Role action diversity: 0.6991
- Negotiation uniqueness: 0.8333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### new_product_launch:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1769 (+/- 0.0134)
- Clean persona drift MAE: 0.1769
- Per-trait absolute error: O 0.1355, C 0.2711, E 0.1896, A 0.0667, N 0.2211
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.0417
- Clean commitment contradiction: 0.0417
- Envelope violations: 6.6667
- Clean envelope violations: 6.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.2011 (+/- 0.0111)
- Clean persona drift MAE: 0.2011
- Per-trait absolute error: O 0.1800, C 0.3400, E 0.1398, A 0.0889, N 0.2567
- Relationship inconsistency: 0.0691
- Commitment contradiction: 0.2004
- Clean commitment contradiction: 0.2004
- Envelope violations: 8.0000
- Clean envelope violations: 8.0000
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4722
- Role action diversity: 0.7778
- Negotiation uniqueness: 1.0000
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1550 (+/- 0.0028)
- Clean persona drift MAE: 0.1550
- Per-trait absolute error: O 0.1144, C 0.2422, E 0.1063, A 0.0889, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Clean envelope violations: 5.6667
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1784 (+/- 0.0117)
- Clean persona drift MAE: 0.1784
- Per-trait absolute error: O 0.1322, C 0.2933, E 0.0606, A 0.1289, N 0.2767
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.2262
- Clean commitment contradiction: 0.2262
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.7222
- Role action diversity: 0.6204
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Mode Summary
### guided:engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0146)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1250, C 0.2567, E 0.1480, A 0.0778, N 0.2222
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.0208
- Clean commitment contradiction: 0.0208
- Envelope violations: 6.1667
- Clean envelope violations: 6.1667
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0011
- Mean turns: 11.00

### guided:naive_action_baseline
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1897 (+/- 0.0161)
- Clean persona drift MAE: 0.1897
- Per-trait absolute error: O 0.1561, C 0.3167, E 0.1002, A 0.1089, N 0.2667
- Relationship inconsistency: 0.1096
- Commitment contradiction: 0.2133
- Clean commitment contradiction: 0.2133
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5972
- Role action diversity: 0.6991
- Negotiation uniqueness: 0.8333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### integration_trust:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1550 (+/- 0.0028)
- Clean persona drift MAE: 0.1550
- Per-trait absolute error: O 0.1144, C 0.2422, E 0.1063, A 0.0889, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.6667
- Clean envelope violations: 5.6667
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### integration_trust:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1784 (+/- 0.0117)
- Clean persona drift MAE: 0.1784
- Per-trait absolute error: O 0.1322, C 0.2933, E 0.0606, A 0.1289, N 0.2767
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.2262
- Clean commitment contradiction: 0.2262
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.7222
- Role action diversity: 0.6204
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### launch_pressure:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1769 (+/- 0.0134)
- Clean persona drift MAE: 0.1769
- Per-trait absolute error: O 0.1355, C 0.2711, E 0.1896, A 0.0667, N 0.2211
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.0417
- Clean commitment contradiction: 0.0417
- Envelope violations: 6.6667
- Clean envelope violations: 6.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### launch_pressure:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.2011 (+/- 0.0111)
- Clean persona drift MAE: 0.2011
- Per-trait absolute error: O 0.1800, C 0.3400, E 0.1398, A 0.0889, N 0.2567
- Relationship inconsistency: 0.0691
- Commitment contradiction: 0.2004
- Clean commitment contradiction: 0.2004
- Envelope violations: 8.0000
- Clean envelope violations: 8.0000
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4722
- Role action diversity: 0.7778
- Negotiation uniqueness: 1.0000
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
