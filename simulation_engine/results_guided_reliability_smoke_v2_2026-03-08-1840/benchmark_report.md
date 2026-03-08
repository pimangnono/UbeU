# Simulation Benchmark Report

## Suite Config
- Total runs: 11
- Conditions: naive_action_baseline, engine_dialogue_only
- Script ids: new_product_launch, post_merger_integration
- Repetitions per condition: 3

## Condition Summary
### engine_dialogue_only
- Runs: 5
- Clean runs: 0
- Contaminated runs: 5
- Persona drift MAE: 0.1684 (+/- 0.0073)
- Clean persona drift MAE: 0.1684
- Per-trait absolute error: O 0.1600, C 0.4307, E 0.1254, A 0.0733, N 0.0527
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.4000
- Clean envelope violations: 5.4000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9627
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 1.0000
- Fallback taxonomy: empty_pool_fallback 1.0000
- State trajectory variance: 0.0010
- Mean turns: 11.00

### naive_action_baseline
- Runs: 6
- Clean runs: 0
- Contaminated runs: 6
- Persona drift MAE: 0.1699 (+/- 0.0075)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1550, C 0.4334, E 0.1278, A 0.0766, N 0.0567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.5000
- Clean envelope violations: 5.5000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: retry_exhausted_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Reliability Warnings
- Fallback utterance contamination detected; treat persona/fidelity deltas as non-decisive until rerun.
- engine_dialogue_only: fallback utterance rate 1.0000
- naive_action_baseline: fallback utterance rate 1.0000

## Script-Level Summary
### new_product_launch:engine_dialogue_only
- Runs: 3
- Clean runs: 0
- Contaminated runs: 3
- Persona drift MAE: 0.1624 (+/- 0.0000)
- Clean persona drift MAE: 0.1624
- Per-trait absolute error: O 0.1800, C 0.4200, E 0.1156, A 0.0600, N 0.0367
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: empty_pool_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### new_product_launch:naive_action_baseline
- Runs: 3
- Clean runs: 0
- Contaminated runs: 3
- Persona drift MAE: 0.1624 (+/- 0.0000)
- Clean persona drift MAE: 0.1624
- Per-trait absolute error: O 0.1800, C 0.4200, E 0.1156, A 0.0600, N 0.0367
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: retry_exhausted_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:engine_dialogue_only
- Runs: 2
- Clean runs: 0
- Contaminated runs: 2
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Clean persona drift MAE: 0.1773
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 1.0000
- Fallback taxonomy: empty_pool_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### post_merger_integration:naive_action_baseline
- Runs: 3
- Clean runs: 0
- Contaminated runs: 3
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Clean persona drift MAE: 0.1773
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: retry_exhausted_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Mode Summary
### guided:engine_dialogue_only
- Runs: 5
- Clean runs: 0
- Contaminated runs: 5
- Persona drift MAE: 0.1684 (+/- 0.0073)
- Clean persona drift MAE: 0.1684
- Per-trait absolute error: O 0.1600, C 0.4307, E 0.1254, A 0.0733, N 0.0527
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.4000
- Clean envelope violations: 5.4000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9627
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 1.0000
- Fallback taxonomy: empty_pool_fallback 1.0000
- State trajectory variance: 0.0010
- Mean turns: 11.00

### guided:naive_action_baseline
- Runs: 6
- Clean runs: 0
- Contaminated runs: 6
- Persona drift MAE: 0.1699 (+/- 0.0075)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1550, C 0.4334, E 0.1278, A 0.0766, N 0.0567
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.5000
- Clean envelope violations: 5.5000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: retry_exhausted_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00


## Family Summary
### integration_trust:engine_dialogue_only
- Runs: 2
- Clean runs: 0
- Contaminated runs: 2
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Clean persona drift MAE: 0.1773
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3333
- Fallback utterance rate: 1.0000
- Fallback taxonomy: empty_pool_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### integration_trust:naive_action_baseline
- Runs: 3
- Clean runs: 0
- Contaminated runs: 3
- Persona drift MAE: 0.1773 (+/- 0.0000)
- Clean persona drift MAE: 0.1773
- Per-trait absolute error: O 0.1300, C 0.4467, E 0.1400, A 0.0933, N 0.0767
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 6.0000
- Clean envelope violations: 6.0000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: retry_exhausted_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### launch_pressure:engine_dialogue_only
- Runs: 3
- Clean runs: 0
- Contaminated runs: 3
- Persona drift MAE: 0.1624 (+/- 0.0000)
- Clean persona drift MAE: 0.1624
- Per-trait absolute error: O 0.1800, C 0.4200, E 0.1156, A 0.0600, N 0.0367
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: empty_pool_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00

### launch_pressure:naive_action_baseline
- Runs: 3
- Clean runs: 0
- Contaminated runs: 3
- Persona drift MAE: 0.1624 (+/- 0.0000)
- Clean persona drift MAE: 0.1624
- Per-trait absolute error: O 0.1800, C 0.4200, E 0.1156, A 0.0600, N 0.0367
- Relationship inconsistency: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 5.0000
- Clean envelope violations: 5.0000
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
- Fallback utterance rate: 1.0000
- Fallback taxonomy: retry_exhausted_fallback 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
