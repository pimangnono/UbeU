# Simulation Benchmark Report

## Suite Config
- Total runs: 12
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 6
- Persona drift MAE: 0.1804 (+/- 0.0046)
- Per-trait absolute error: O 0.1000, C 0.4717, E 0.1189, A 0.1100, N 0.1016
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0014
- Mean turns: 11.00

### naive_action_baseline
- Runs: 6
- Persona drift MAE: 0.1804 (+/- 0.0046)
- Per-trait absolute error: O 0.1000, C 0.4717, E 0.1189, A 0.1100, N 0.1016
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.5000
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
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1851 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4633, E 0.1422, A 0.1233, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis_response:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1851 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4633, E 0.1422, A 0.1233, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
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
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_reallocation_crunch:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1758 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.4800, E 0.0956, A 0.0967, N 0.1100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_reallocation_crunch:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1758 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.4800, E 0.0956, A 0.0967, N 0.1100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
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
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 6
- Persona drift MAE: 0.1804 (+/- 0.0046)
- Per-trait absolute error: O 0.1000, C 0.4717, E 0.1189, A 0.1100, N 0.1016
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0014
- Mean turns: 11.00

### exploratory:naive_action_baseline
- Runs: 6
- Persona drift MAE: 0.1804 (+/- 0.0046)
- Per-trait absolute error: O 0.1000, C 0.4717, E 0.1189, A 0.1100, N 0.1016
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.5000
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
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1851 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4633, E 0.1422, A 0.1233, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1851 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4633, E 0.1422, A 0.1233, N 0.0933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
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
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_scarcity:engine_dialogue_only
- Runs: 3
- Persona drift MAE: 0.1758 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.4800, E 0.0956, A 0.0967, N 0.1100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_scarcity:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.1758 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.4800, E 0.0956, A 0.0967, N 0.1100
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
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
- State trajectory variance: 0.0000
- Mean turns: 11.00
