# Simulation Benchmark Report

## Suite Config
- Total runs: 9
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
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

### naive_action_baseline
- Runs: 6
- Persona drift MAE: 0.1996 (+/- 0.0135)
- Per-trait absolute error: O 0.0922, C 0.4083, E 0.1759, A 0.0900, N 0.2317
- Relationship inconsistency: 0.0750
- Commitment contradiction: 0.0750
- Envelope violations: 7.5000
- Structured action validity: 0.7778
- Owner resolution rate: 0.8333
- Executed action contradiction: 0.0000
- State transition coherence: 0.8333
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.2500
- Role action diversity: 0.9444
- Negotiation uniqueness: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
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
