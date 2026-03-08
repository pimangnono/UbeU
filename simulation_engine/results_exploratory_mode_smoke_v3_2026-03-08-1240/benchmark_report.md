# Simulation Benchmark Report

## Suite Config
- Total runs: 4
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 1

## Condition Summary
### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1813 (+/- 0.0018)
- Per-trait absolute error: O 0.0834, C 0.2950, E 0.1533, A 0.1167, N 0.2583
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0014
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1842 (+/- 0.0275)
- Per-trait absolute error: O 0.1000, C 0.3783, E 0.1077, A 0.1167, N 0.2183
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1340
- Envelope violations: 5.5000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1795 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.2767, E 0.1610, A 0.1167, N 0.2733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis_response:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.2117 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4633, E 0.1483, A 0.1500, N 0.1933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1250
- Envelope violations: 6.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_reallocation_crunch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1831 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.3133, E 0.1457, A 0.1167, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_reallocation_crunch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1568 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.2933, E 0.0672, A 0.0833, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1429
- Envelope violations: 5.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1813 (+/- 0.0018)
- Per-trait absolute error: O 0.0834, C 0.2950, E 0.1533, A 0.1167, N 0.2583
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0014
- Mean turns: 11.00

### exploratory:naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1842 (+/- 0.0275)
- Per-trait absolute error: O 0.1000, C 0.3783, E 0.1077, A 0.1167, N 0.2183
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1340
- Envelope violations: 5.5000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1795 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.2767, E 0.1610, A 0.1167, N 0.2733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.2117 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.4633, E 0.1483, A 0.1500, N 0.1933
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1250
- Envelope violations: 6.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_scarcity:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1831 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.3133, E 0.1457, A 0.1167, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_scarcity:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1568 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.2933, E 0.0672, A 0.0833, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1429
- Envelope violations: 5.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
