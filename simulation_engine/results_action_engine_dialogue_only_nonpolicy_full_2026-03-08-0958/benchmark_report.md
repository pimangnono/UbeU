# Simulation Benchmark Report

## Suite Config
- Total runs: 12
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 6
- Persona drift MAE: 0.1683 (+/- 0.0187)
- Per-trait absolute error: O 0.1506, C 0.2222, E 0.1401, A 0.0933, N 0.2356
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0278
- Envelope violations: 6.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0013
- Mean turns: 11.00

### naive_action_baseline
- Runs: 6
- Persona drift MAE: 0.1871 (+/- 0.0141)
- Per-trait absolute error: O 0.1672, C 0.3089, E 0.1161, A 0.0900, N 0.2533
- Relationship inconsistency: 0.1408
- Commitment contradiction: 0.0447
- Envelope violations: 7.1667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.7083
- Role action diversity: 0.7847
- Negotiation uniqueness: 0.7500
- State trajectory variance: 0.0010
- Mean turns: 11.00


## Script-Level Summary
### new_product_launch:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1854 (+/- 0.0069)
- Per-trait absolute error: O 0.1689, C 0.2756, E 0.1661, A 0.0689, N 0.2478
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.6667
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
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1848 (+/- 0.0133)
- Per-trait absolute error: O 0.1800, C 0.3200, E 0.1142, A 0.0533, N 0.2567
- Relationship inconsistency: 0.1317
- Commitment contradiction: 0.0476
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5833
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.8333
- State trajectory variance: 0.0008
- Mean turns: 11.00

### post_merger_integration:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1513 (+/- 0.0083)
- Per-trait absolute error: O 0.1322, C 0.1689, E 0.1140, A 0.1178, N 0.2233
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0556
- Envelope violations: 5.0000
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

### post_merger_integration:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1893 (+/- 0.0145)
- Per-trait absolute error: O 0.1544, C 0.2978, E 0.1179, A 0.1267, N 0.2500
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.0417
- Envelope violations: 7.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.8333
- Role action diversity: 0.7361
- Negotiation uniqueness: 0.6667
- State trajectory variance: 0.0009
- Mean turns: 11.00
