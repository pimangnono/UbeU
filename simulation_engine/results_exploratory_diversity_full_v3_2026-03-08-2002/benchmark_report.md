# Simulation Benchmark Report

## Suite Config
- Total runs: 4
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 1
- Clean runs: 1
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0000)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.0700, C 0.2767, E 0.1471, A 0.1100, N 0.2733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.3333
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
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1761 (+/- 0.0096)
- Clean persona drift MAE: 0.1761
- Per-trait absolute error: O 0.0878, C 0.3033, E 0.1259, A 0.1122, N 0.2511
- Relationship inconsistency: 0.0611
- Commitment contradiction: 0.1222
- Clean commitment contradiction: 0.1222
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.8889
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4167
- Role action diversity: 0.8241
- Negotiation uniqueness: 0.8889
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 11.00


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 1
- Clean runs: 1
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0000)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.0700, C 0.2767, E 0.1471, A 0.1100, N 0.2733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.3333
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
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis_response:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1761 (+/- 0.0096)
- Clean persona drift MAE: 0.1761
- Per-trait absolute error: O 0.0878, C 0.3033, E 0.1259, A 0.1122, N 0.2511
- Relationship inconsistency: 0.0611
- Commitment contradiction: 0.1222
- Clean commitment contradiction: 0.1222
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.8889
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4167
- Role action diversity: 0.8241
- Negotiation uniqueness: 0.8889
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 11.00


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 1
- Clean runs: 1
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0000)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.0700, C 0.2767, E 0.1471, A 0.1100, N 0.2733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.3333
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
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### exploratory:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1761 (+/- 0.0096)
- Clean persona drift MAE: 0.1761
- Per-trait absolute error: O 0.0878, C 0.3033, E 0.1259, A 0.1122, N 0.2511
- Relationship inconsistency: 0.0611
- Commitment contradiction: 0.1222
- Clean commitment contradiction: 0.1222
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.8889
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4167
- Role action diversity: 0.8241
- Negotiation uniqueness: 0.8889
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 11.00


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 1
- Clean runs: 1
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0000)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.0700, C 0.2767, E 0.1471, A 0.1100, N 0.2733
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.3333
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
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### brand_crisis:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1761 (+/- 0.0096)
- Clean persona drift MAE: 0.1761
- Per-trait absolute error: O 0.0878, C 0.3033, E 0.1259, A 0.1122, N 0.2511
- Relationship inconsistency: 0.0611
- Commitment contradiction: 0.1222
- Clean commitment contradiction: 0.1222
- Envelope violations: 7.0000
- Clean envelope violations: 7.0000
- Structured action validity: 0.8889
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4167
- Role action diversity: 0.8241
- Negotiation uniqueness: 0.8889
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 11.00
