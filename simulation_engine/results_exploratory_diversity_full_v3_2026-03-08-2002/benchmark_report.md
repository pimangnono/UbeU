# Simulation Benchmark Report

## Suite Config
- Total runs: 12
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: brand_crisis_response, resource_reallocation_crunch
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1723 (+/- 0.0084)
- Clean persona drift MAE: 0.1723
- Per-trait absolute error: O 0.0945, C 0.2350, E 0.1872, A 0.1000, N 0.2450
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.8333
- Clean envelope violations: 6.8333
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0014
- Mean turns: 11.00

### naive_action_baseline
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1708 (+/- 0.0115)
- Clean persona drift MAE: 0.1708
- Per-trait absolute error: O 0.0867, C 0.2983, E 0.1139, A 0.1122, N 0.2428
- Relationship inconsistency: 0.0305
- Commitment contradiction: 0.2823
- Clean commitment contradiction: 0.2823
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
- Structured action validity: 0.6945
- Owner resolution rate: 0.8333
- Executed action contradiction: 0.0000
- State transition coherence: 0.8333
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4583
- Role action diversity: 0.8148
- Negotiation uniqueness: 0.6389
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Script-Level Summary
### brand_crisis_response:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0056)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.0922, C 0.2256, E 0.1999, A 0.1122, N 0.2600
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Clean envelope violations: 7.3333
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

### resource_reallocation_crunch:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1667 (+/- 0.0068)
- Clean persona drift MAE: 0.1667
- Per-trait absolute error: O 0.0967, C 0.2444, E 0.1744, A 0.0878, N 0.2300
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.3333
- Clean envelope violations: 6.3333
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_reallocation_crunch:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1655 (+/- 0.0108)
- Clean persona drift MAE: 0.1655
- Per-trait absolute error: O 0.0856, C 0.2933, E 0.1020, A 0.1122, N 0.2344
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.4425
- Clean commitment contradiction: 0.4425
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.5000
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5000
- Role action diversity: 0.8056
- Negotiation uniqueness: 0.3889
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1723 (+/- 0.0084)
- Clean persona drift MAE: 0.1723
- Per-trait absolute error: O 0.0945, C 0.2350, E 0.1872, A 0.1000, N 0.2450
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.8333
- Clean envelope violations: 6.8333
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6875
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0014
- Mean turns: 11.00

### exploratory:naive_action_baseline
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1708 (+/- 0.0115)
- Clean persona drift MAE: 0.1708
- Per-trait absolute error: O 0.0867, C 0.2983, E 0.1139, A 0.1122, N 0.2428
- Relationship inconsistency: 0.0305
- Commitment contradiction: 0.2823
- Clean commitment contradiction: 0.2823
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
- Structured action validity: 0.6945
- Owner resolution rate: 0.8333
- Executed action contradiction: 0.0000
- State transition coherence: 0.8333
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.4583
- Role action diversity: 0.8148
- Negotiation uniqueness: 0.6389
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### brand_crisis:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0056)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.0922, C 0.2256, E 0.1999, A 0.1122, N 0.2600
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 7.3333
- Clean envelope violations: 7.3333
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

### resource_scarcity:engine_dialogue_only
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1667 (+/- 0.0068)
- Clean persona drift MAE: 0.1667
- Per-trait absolute error: O 0.0967, C 0.2444, E 0.1744, A 0.0878, N 0.2300
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.3333
- Clean envelope violations: 6.3333
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00

### resource_scarcity:naive_action_baseline
- Runs: 3
- Clean runs: 3
- Contaminated runs: 0
- Persona drift MAE: 0.1655 (+/- 0.0108)
- Clean persona drift MAE: 0.1655
- Per-trait absolute error: O 0.0856, C 0.2933, E 0.1020, A 0.1122, N 0.2344
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.4425
- Clean commitment contradiction: 0.4425
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
- Structured action validity: 0.5000
- Owner resolution rate: 0.6667
- Executed action contradiction: 0.0000
- State transition coherence: 0.6667
- Action feedback utilization: 0.6667
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.5000
- Role action diversity: 0.8056
- Negotiation uniqueness: 0.3889
- Fallback utterance rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
