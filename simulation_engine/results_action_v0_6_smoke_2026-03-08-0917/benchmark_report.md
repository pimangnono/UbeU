# Simulation Benchmark Report

## Suite Config
- Total runs: 6
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: commuting_support_policy, new_product_launch
- Repetitions per condition: 1

## Condition Summary
### engine_action_v0
- Runs: 2
- Persona drift MAE: 0.1741 (+/- 0.0023)
- Per-trait absolute error: O 0.1250, C 0.3066, E 0.2040, A 0.0667, N 0.1683
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 6.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9568
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5208
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0006
- Mean turns: 11.00

### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1447 (+/- 0.0273)
- Per-trait absolute error: O 0.0716, C 0.2666, E 0.1500, A 0.0733, N 0.1616
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 4.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9568
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5208
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0006
- Mean turns: 11.00

### naive_action_baseline
- Runs: 2
- Persona drift MAE: 0.1649 (+/- 0.0127)
- Per-trait absolute error: O 0.1084, C 0.3467, E 0.1283, A 0.0466, N 0.1950
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.1429
- Envelope violations: 6.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.8334
- Role action diversity: 0.7430
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0005
- Mean turns: 11.00


## Controlled Engine vs Baseline
- Persona drift delta (`controlled - baseline`): +0.0092
- Per-trait error delta: O +0.0166, C -0.0401, E +0.0757, A +0.0201, N -0.0267
- Relationship inconsistency delta: +0.0000
- Commitment contradiction delta: -0.1429
- Structured action validity delta: +0.0000
- Executed action contradiction delta: +0.0000
- Action-plan alignment delta: +0.9568
- Action family convergence delta: -0.0834
- Role action diversity delta: -0.2222
- Negotiation uniqueness delta: -0.6667
- State trajectory variance delta: +0.0001

## Action Engine vs Dialogue-Only
- Persona drift delta (`controlled - baseline`): +0.0294
- Per-trait error delta: O +0.0534, C +0.0400, E +0.0540, A -0.0066, N +0.0067
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
- Persona drift MAE: 0.1764 (+/- 0.0000)
- Per-trait absolute error: O 0.1033, C 0.3533, E 0.2453, A 0.0600, N 0.1200
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
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

### commuting_support_policy:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1174 (+/- 0.0000)
- Per-trait absolute error: O 0.0633, C 0.1933, E 0.1702, A 0.0800, N 0.0800
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 2.0000
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
- Runs: 1
- Persona drift MAE: 0.1523 (+/- 0.0000)
- Per-trait absolute error: O 0.0700, C 0.3267, E 0.1317, A 0.0600, N 0.1733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 1.0000
- Role action diversity: 0.7778
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_action_v0
- Runs: 1
- Persona drift MAE: 0.1719 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.2600, E 0.1627, A 0.0733, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:engine_dialogue_only
- Runs: 1
- Persona drift MAE: 0.1720 (+/- 0.0000)
- Per-trait absolute error: O 0.0800, C 0.3400, E 0.1299, A 0.0667, N 0.2433
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 1
- Persona drift MAE: 0.1776 (+/- 0.0000)
- Per-trait absolute error: O 0.1467, C 0.3667, E 0.1248, A 0.0333, N 0.2167
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.2857
- Envelope violations: 7.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.6667
- Role action diversity: 0.7083
- Negotiation uniqueness: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
