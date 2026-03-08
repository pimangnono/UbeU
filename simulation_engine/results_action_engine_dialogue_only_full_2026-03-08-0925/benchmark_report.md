# Simulation Benchmark Report

## Suite Config
- Total runs: 18
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
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
- State trajectory variance: 0.0014
- Mean turns: 11.00

### naive_action_baseline
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
- State trajectory variance: 0.0008
- Mean turns: 11.00
