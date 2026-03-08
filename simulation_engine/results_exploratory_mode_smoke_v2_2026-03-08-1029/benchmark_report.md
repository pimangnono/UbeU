# Simulation Benchmark Report

## Suite Config
- Total runs: 4
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 1

## Condition Summary
### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1619 (+/- 0.0145)
- Per-trait absolute error: O 0.0967, C 0.2250, E 0.1462, A 0.0967, N 0.2450
- Relationship inconsistency: 0.0282
- Commitment contradiction: 0.0000
- Envelope violations: 5.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0014
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1764 (+/- 0.0191)
- Per-trait absolute error: O 0.1000, C 0.3083, E 0.0953, A 0.1267, N 0.2516
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2500
- Envelope violations: 6.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1765 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.2633, E 0.1590, A 0.1167, N 0.2467
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
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis_response:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1955 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.3833, E 0.1074, A 0.1233, N 0.2600
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_reallocation_crunch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1474 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.1867, E 0.1334, A 0.0767, N 0.2433
- Relationship inconsistency: 0.0563
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
- Runs: 1
- Persona drift MAE: 0.1573 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.2333, E 0.0832, A 0.1300, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.5000
- Envelope violations: 5.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1619 (+/- 0.0145)
- Per-trait absolute error: O 0.0967, C 0.2250, E 0.1462, A 0.0967, N 0.2450
- Relationship inconsistency: 0.0282
- Commitment contradiction: 0.0000
- Envelope violations: 5.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0014
- Mean turns: 11.00

### exploratory:naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1764 (+/- 0.0191)
- Per-trait absolute error: O 0.1000, C 0.3083, E 0.0953, A 0.1267, N 0.2516
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2500
- Envelope violations: 6.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1765 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.2633, E 0.1590, A 0.1167, N 0.2467
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
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1955 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.3833, E 0.1074, A 0.1233, N 0.2600
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_scarcity:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1474 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.1867, E 0.1334, A 0.0767, N 0.2433
- Relationship inconsistency: 0.0563
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
- Runs: 1
- Persona drift MAE: 0.1573 (+/- 0.0000)
- Per-trait absolute error: O 0.0967, C 0.2333, E 0.0832, A 0.1300, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.5000
- Envelope violations: 5.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 1.0000
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
