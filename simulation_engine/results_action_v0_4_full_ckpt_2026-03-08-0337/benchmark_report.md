# Simulation Benchmark Report

## Suite Config
- Total runs: 5
- Conditions: naive_action_baseline, engine_dialogue_only, engine_action_v0
- Script ids: youth_employment_policy, housing_support_policy, commuting_support_policy, new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1996 (+/- 0.0043)
- Per-trait absolute error: O 0.0834, C 0.3534, E 0.2045, A 0.0733, N 0.2833
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.2045 (+/- 0.0187)
- Per-trait absolute error: O 0.1089, C 0.4400, E 0.1514, A 0.0722, N 0.2500
- Relationship inconsistency: 0.0917
- Commitment contradiction: 0.0667
- Envelope violations: 7.6667
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.1667
- Role action diversity: 0.5694
- Negotiation uniqueness: 0.5556
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### youth_employment_policy:engine_dialogue_only
- Runs: 2
- Persona drift MAE: 0.1996 (+/- 0.0043)
- Per-trait absolute error: O 0.0834, C 0.3534, E 0.2045, A 0.0733, N 0.2833
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Envelope violations: 8.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 11.00

### youth_employment_policy:naive_action_baseline
- Runs: 3
- Persona drift MAE: 0.2045 (+/- 0.0187)
- Per-trait absolute error: O 0.1089, C 0.4400, E 0.1514, A 0.0722, N 0.2500
- Relationship inconsistency: 0.0917
- Commitment contradiction: 0.0667
- Envelope violations: 7.6667
- Structured action validity: 0.6667
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.1667
- Role action diversity: 0.5694
- Negotiation uniqueness: 0.5556
- State trajectory variance: 0.0000
- Mean turns: 11.00
