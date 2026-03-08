# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy, new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 2
- Persona drift MAE: 0.1672 (+/- 0.0145)
- Per-trait absolute error: O 0.1084, C 0.2233, E 0.2059, A 0.0834, N 0.2150
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5208
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0015
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1515 (+/- 0.0134)
- Per-trait absolute error: O 0.1183, C 0.2500, E 0.1679, A 0.0667, N 0.1550
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5208
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0015
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1531 (+/- 0.0034)
- Per-trait absolute error: O 0.1183, C 0.2533, E 0.1186, A 0.0533, N 0.2217
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1965
- Envelope violations: 5.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.7500
- Role action diversity: 0.7292
- Negotiation uniqueness: 0.4166
- State trajectory variance: 0.0003
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): +0.0141
- Per-trait error delta: O -0.0099, C -0.0300, E +0.0873, A +0.0301, N -0.0067
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.1965
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.9500
- Action family convergence delta: +0.0000
- Role action diversity delta: -0.2084
- Negotiation uniqueness delta: -0.0833
- State trajectory variance delta: +0.0012

## Action Engine vs Dialogue-Only
- Persona drift delta (`controlled - baseline`): +0.0157
- Per-trait error delta: O -0.0099, C -0.0267, E +0.0380, A +0.0167, N +0.0600
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: +0.0000
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.0000
- Action family convergence delta: +0.0000
- Role action diversity delta: +0.0000
- Negotiation uniqueness delta: +0.0000
- State trajectory variance delta: +0.0000

## Script-Level Summary
### commuting_support_policy:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1527 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.2467, E 0.1936, A 0.0800, N 0.1733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1382 (+/- 0.0000)
- Per-trait absolute error: O 0.0900, C 0.2733, E 0.2210, A 0.0533, N 0.0533
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### commuting_support_policy:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1565 (+/- 0.0000)
- Per-trait absolute error: O 0.0567, C 0.2933, E 0.1257, A 0.0933, N 0.2133
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2500
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1817 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2000, E 0.2183, A 0.0867, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1649 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2267, E 0.1148, A 0.0800, N 0.2567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1496 (+/- 0.0000)
- Per-trait absolute error: O 0.1800, C 0.2133, E 0.1114, A 0.0133, N 0.2300
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1429
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7917
- Negotiation uniqueness: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 11.00
