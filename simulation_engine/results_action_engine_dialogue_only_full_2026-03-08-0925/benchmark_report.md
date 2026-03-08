# Simulation Benchmark Report

## Suite Config
- Total runs: 30
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 15
- Persona drift MAE: 0.1608 (+/- 0.0232)
- Per-trait absolute error: O 0.1058, C 0.2918, E 0.1767, A 0.0760, N 0.1536
- Relationship inconsistency: 0.0300
- Commitment contradiction: 0.0000
- Envelope violations: 5.2667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2667
- Action-plan alignment: 0.9627
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.4916
- Negotiation uniqueness: 0.4000
- Fallback utterance rate: 0.2667
- State trajectory variance: 0.0014
- Mean turns: 11.00

### naive_action_baseline
- Runs: 15
- Persona drift MAE: 0.1853 (+/- 0.0175)
- Per-trait absolute error: O 0.1156, C 0.3780, E 0.1555, A 0.0796, N 0.1980
- Relationship inconsistency: 0.0450
- Commitment contradiction: 0.0945
- Envelope violations: 6.8667
- Structured action validity: 0.7111
- Owner resolution rate: 0.7333
- Executed action contradiction: 0.0000
- State transition coherence: 0.7333
- Action feedback utilization: 0.2000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.3167
- Role action diversity: 0.7176
- Negotiation uniqueness: 0.5333
- Fallback utterance rate: 0.2000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### commuting_support_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1331 (+/- 0.0237)
- Per-trait absolute error: O 0.0745, C 0.1622, E 0.2043, A 0.0955, N 0.1289
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.0000
- Envelope violations: 3.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1628 (+/- 0.0121)
- Per-trait absolute error: O 0.0833, C 0.3133, E 0.1307, A 0.0755, N 0.2111
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1083
- Envelope violations: 5.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.1667
- Role action diversity: 0.9583
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0005
- Mean turns: 11.00

### housing_support_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1474 (+/- 0.0181)
- Per-trait absolute error: O 0.0778, C 0.2500, E 0.1990, A 0.0767, N 0.1333
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 3.3333
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
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### housing_support_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.2106 (+/- 0.0090)
- Per-trait absolute error: O 0.0867, C 0.4633, E 0.1752, A 0.1100, N 0.2178
- Relationship inconsistency: 0.1500
- Commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.3333
- Role action diversity: 0.9444
- Negotiation uniqueness: 1.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1696 (+/- 0.0072)
- Per-trait absolute error: O 0.1467, C 0.3111, E 0.1582, A 0.0578, N 0.1745
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1873 (+/- 0.0054)
- Per-trait absolute error: O 0.1800, C 0.3133, E 0.1552, A 0.0489, N 0.2389
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.2143
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.9167
- Role action diversity: 0.7407
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0001
- Mean turns: 11.00

### post_merger_integration:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1764 (+/- 0.0145)
- Per-trait absolute error: O 0.1000, C 0.2889, E 0.1819, A 0.0567, N 0.2544
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1887 (+/- 0.0064)
- Per-trait absolute error: O 0.0978, C 0.3533, E 0.1766, A 0.0700, N 0.2456
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1500
- Envelope violations: 7.6667
- Structured action validity: 0.8889
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.1667
- Role action diversity: 0.9444
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0008
- Mean turns: 11.00


## Mode Summary
### guided:engine_dialogue_only
- Runs: 6
- Persona drift MAE: 0.1734 (+/- 0.0064)
- Per-trait absolute error: O 0.1383, C 0.3789, E 0.1491, A 0.0755, N 0.1256
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1667
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.6667
- State trajectory variance: 0.0013
- Mean turns: 11.00

### guided:naive_action_baseline
- Runs: 6
- Persona drift MAE: 0.1823 (+/- 0.0063)
- Per-trait absolute error: O 0.1550, C 0.3800, E 0.1476, A 0.0711, N 0.1578
- Relationship inconsistency: 0.0375
- Commitment contradiction: 0.1071
- Envelope violations: 7.0000
- Structured action validity: 0.5000
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.1667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4583
- Role action diversity: 0.3704
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### unknown:engine_dialogue_only
- Runs: 9
- Persona drift MAE: 0.1523 (+/- 0.0263)
- Per-trait absolute error: O 0.0841, C 0.2337, E 0.1951, A 0.0763, N 0.1722
- Relationship inconsistency: 0.0500
- Commitment contradiction: 0.0000
- Envelope violations: 4.7778
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9621
- Planned action coverage: 1.0000
- Action family convergence: 0.9167
- Role action diversity: 0.4305
- Negotiation uniqueness: 0.4444
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0014
- Mean turns: 11.00

### unknown:naive_action_baseline
- Runs: 9
- Persona drift MAE: 0.1874 (+/- 0.0217)
- Per-trait absolute error: O 0.0893, C 0.3767, E 0.1608, A 0.0852, N 0.2248
- Relationship inconsistency: 0.0500
- Commitment contradiction: 0.0861
- Envelope violations: 6.7778
- Structured action validity: 0.8519
- Owner resolution rate: 0.8889
- Executed action contradiction: 0.0000
- State transition coherence: 0.8889
- Action feedback utilization: 0.2222
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.2222
- Role action diversity: 0.9491
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### generic:engine_dialogue_only
- Runs: 9
- Persona drift MAE: 0.1523 (+/- 0.0263)
- Per-trait absolute error: O 0.0841, C 0.2337, E 0.1951, A 0.0763, N 0.1722
- Relationship inconsistency: 0.0500
- Commitment contradiction: 0.0000
- Envelope violations: 4.7778
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9621
- Planned action coverage: 1.0000
- Action family convergence: 0.9167
- Role action diversity: 0.4305
- Negotiation uniqueness: 0.4444
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0014
- Mean turns: 11.00

### generic:naive_action_baseline
- Runs: 9
- Persona drift MAE: 0.1874 (+/- 0.0217)
- Per-trait absolute error: O 0.0893, C 0.3767, E 0.1608, A 0.0852, N 0.2248
- Relationship inconsistency: 0.0500
- Commitment contradiction: 0.0861
- Envelope violations: 6.7778
- Structured action validity: 0.8519
- Owner resolution rate: 0.8889
- Executed action contradiction: 0.0000
- State transition coherence: 0.8889
- Action feedback utilization: 0.2222
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.2222
- Role action diversity: 0.9491
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### integration_trust:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### integration_trust:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### launch_pressure:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1696 (+/- 0.0072)
- Per-trait absolute error: O 0.1467, C 0.3111, E 0.1582, A 0.0578, N 0.1745
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### launch_pressure:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1873 (+/- 0.0054)
- Per-trait absolute error: O 0.1800, C 0.3133, E 0.1552, A 0.0489, N 0.2389
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.2143
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.9167
- Role action diversity: 0.7407
- Negotiation uniqueness: 0.6667
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0001
- Mean turns: 11.00
