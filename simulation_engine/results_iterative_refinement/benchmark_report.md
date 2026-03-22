# Simulation Benchmark Report

## Suite Config
- Total runs: 1080
- Conditions: engine_structural, naive
- Script ids: australia_robodebt_10actor, australia_robodebt_3actor, australia_robodebt_5actor, boeing_737max_return_10actor, boeing_737max_return_3actor, boeing_737max_return_5actor, california_ab5_gig_classification_10actor, california_ab5_gig_classification_3actor, california_ab5_gig_classification_5actor, eu_gdpr_implementation_10actor, eu_gdpr_implementation_3actor, eu_gdpr_implementation_5actor, flint_water_crisis_10actor, flint_water_crisis_3actor, flint_water_crisis_5actor, ftx_collapse_10actor, ftx_collapse_3actor, ftx_collapse_5actor, fukushima_nuclear_restart_10actor, fukushima_nuclear_restart_3actor, fukushima_nuclear_restart_5actor, japan_intern_training_reform_10actor, japan_intern_training_reform_3actor, japan_intern_training_reform_5actor, microsoft_activision_merger_10actor, microsoft_activision_merger_3actor, microsoft_activision_merger_5actor, netflix_password_crackdown_10actor, netflix_password_crackdown_3actor, netflix_password_crackdown_5actor, nyc_congestion_pricing_10actor, nyc_congestion_pricing_3actor, nyc_congestion_pricing_5actor, peloton_demand_cliff_10actor, peloton_demand_cliff_3actor, peloton_demand_cliff_5actor, sf_homelessness_policy_10actor, sf_homelessness_policy_3actor, sf_homelessness_policy_5actor, singapore_hdb_waittime_crisis_10actor, singapore_hdb_waittime_crisis_3actor, singapore_hdb_waittime_crisis_5actor, starbucks_unionization_10actor, starbucks_unionization_3actor, starbucks_unionization_5actor, svb_bank_run_10actor, svb_bank_run_3actor, svb_bank_run_5actor, theranos_whistleblower_10actor, theranos_whistleblower_3actor, theranos_whistleblower_5actor, uk_post_office_horizon_10actor, uk_post_office_horizon_3actor, uk_post_office_horizon_5actor, wework_ipo_collapse_10actor, wework_ipo_collapse_3actor, wework_ipo_collapse_5actor, zoom_return_to_office_10actor, zoom_return_to_office_3actor, zoom_return_to_office_5actor
- Repetitions per condition: 2

## Condition Summary
### engine_structural
- Runs: 544
- Clean runs: 544
- Contaminated runs: 0
- Persona drift MAE: 0.1685 (+/- 0.0159)
- Clean persona drift MAE: 0.1685
- Per-trait absolute error: O 0.1643, C 0.2215, E 0.1222, A 0.1643, N 0.1701
- Relationship inconsistency: 0.0724
- Relationship shift rate: 0.2204
- Relationship overshoot rate: 0.1911
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0322
- Clean envelope violations: 2.0322
- Structured action validity: 0.5868
- Owner resolution rate: 0.9338
- Executed action contradiction: 0.0000
- State transition coherence: 0.9338
- Action feedback utilization: 0.1562
- Action-plan alignment: 0.9661
- Planned action coverage: 0.9269
- Action family convergence: 0.7307
- Role action diversity: 0.4966
- Negotiation uniqueness: 0.2862
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1064
- Repetition rate: 0.0015
- Topic drift rate: 0.5202
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4082
- Commitment fulfillment rate: 0.7257
- State trajectory variance: 0.0000
- Mean turns: 3.46
- Persona drift 95% CI: [0.1671, 0.1698]

- Phase-level quality:
  - OPENING: drift=0.1717, convergence=0.7647, diversity=0.3649
  - TENSION: drift=0.1735, convergence=0.7260, diversity=0.4501
  - NEGOTIATION: drift=0.1710, convergence=0.6893, diversity=0.4480
  - CLOSING: drift=0.1793, convergence=0.5956, diversity=0.5881

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### naive
- Runs: 536
- Clean runs: 536
- Contaminated runs: 0
- Persona drift MAE: 0.1776 (+/- 0.0164)
- Clean persona drift MAE: 0.1776
- Per-trait absolute error: O 0.1827, C 0.2234, E 0.1440, A 0.1692, N 0.1685
- Relationship inconsistency: 0.0909
- Relationship shift rate: 0.2742
- Relationship overshoot rate: 0.2426
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2546
- Clean envelope violations: 2.2546
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0821
- Repetition rate: 0.0000
- Topic drift rate: 0.5627
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4020
- Commitment fulfillment rate: 0.6463
- State trajectory variance: 0.0000
- Mean turns: 3.51
- Persona drift 95% CI: [0.1762, 0.179]

- Phase-level quality:
  - OPENING: drift=0.1792, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1781, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1789, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1839, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Script-Level Summary
### australia_robodebt_10actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0007)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.1690, C 0.2400, E 0.1399, A 0.2217, N 0.1295
- Relationship inconsistency: 0.1409
- Relationship shift rate: 0.3073
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0926
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3301
- Commitment fulfillment rate: 0.6386
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1797, 0.1803]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1773, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1912, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1685, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_10actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0030)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1740, C 0.2400, E 0.1734, A 0.2294, N 0.1283
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.3119
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0634
- Repetition rate: 0.0000
- Topic drift rate: 0.7727
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3140
- Commitment fulfillment rate: 0.3636
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1875, 0.1905]

- Phase-level quality:
  - OPENING: drift=0.1933, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1876, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2006, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### australia_robodebt_3actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1761 (+/- 0.0082)
- Clean persona drift MAE: 0.1761
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.0970, A 0.2333, N 0.1266
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2725
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0792
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3005
- Commitment fulfillment rate: 0.7445
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1721, 0.1801]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1832, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1814, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1823 (+/- 0.0118)
- Clean persona drift MAE: 0.1823
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1216, A 0.2333, N 0.1333
- Relationship inconsistency: 0.0180
- Relationship shift rate: 0.2867
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3334
- Clean envelope violations: 2.3334
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0874
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2793
- Commitment fulfillment rate: 0.7291
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1765, 0.1881]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1837, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1858, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1730, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1517 (+/- 0.0068)
- Clean persona drift MAE: 0.1517
- Per-trait absolute error: O 0.1440, C 0.2042, E 0.1085, A 0.2015, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2283
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.1742
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0935
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3586
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 1.75
- Persona drift 95% CI: [0.1483, 0.155]

- Phase-level quality:
  - OPENING: drift=0.1436, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1501, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1304, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1984, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### australia_robodebt_5actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1619 (+/- 0.0054)
- Clean persona drift MAE: 0.1619
- Per-trait absolute error: O 0.1540, C 0.1998, E 0.1507, A 0.2050, N 0.1000
- Relationship inconsistency: 0.4395
- Relationship shift rate: 0.4718
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0830
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3537
- Commitment fulfillment rate: 0.8286
- State trajectory variance: 0.0000
- Mean turns: 1.75
- Persona drift 95% CI: [0.1593, 0.1645]

- Phase-level quality:
  - OPENING: drift=0.1582, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1611, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1421, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1920, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1528 (+/- 0.0005)
- Clean persona drift MAE: 0.1528
- Per-trait absolute error: O 0.1560, C 0.2500, E 0.1078, A 0.1444, N 0.1058
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0954
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4412
- Commitment fulfillment rate: 0.6778
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1526, 0.153]

- Phase-level quality:
  - OPENING: drift=0.1536, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1638, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1512, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1587, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### boeing_737max_return_10actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1585 (+/- 0.0004)
- Clean persona drift MAE: 0.1585
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1238, A 0.1396, N 0.1011
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0860
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3926
- Commitment fulfillment rate: 0.4415
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1583, 0.1587]

- Phase-level quality:
  - OPENING: drift=0.1506, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1678, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1622, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1743, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1655 (+/- 0.0002)
- Clean persona drift MAE: 0.1655
- Per-trait absolute error: O 0.1066, C 0.3000, E 0.0659, A 0.1817, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1557
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3755
- Commitment fulfillment rate: 0.6762
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1654, 0.1656]

- Phase-level quality:
  - OPENING: drift=0.1674, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1631, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1679, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1965, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1797 (+/- 0.0033)
- Clean persona drift MAE: 0.1797
- Per-trait absolute error: O 0.1167, C 0.3000, E 0.1003, A 0.2084, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1077
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4021
- Commitment fulfillment rate: 0.4857
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1781, 0.1813]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1782, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1730, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1930, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_5actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1729 (+/- 0.0101)
- Clean persona drift MAE: 0.1729
- Per-trait absolute error: O 0.1540, C 0.2600, E 0.0954, A 0.1715, N 0.1840
- Relationship inconsistency: 0.0326
- Relationship shift rate: 0.2096
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9571
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1163
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2982
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 1.75
- Persona drift 95% CI: [0.168, 0.1779]

- Phase-level quality:
  - OPENING: drift=0.1872, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1550, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1816, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1911, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### boeing_737max_return_5actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1699 (+/- 0.0033)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1340, C 0.2730, E 0.1025, A 0.1600, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1975
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0743
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3529
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 1.75
- Persona drift 95% CI: [0.1682, 0.1715]

- Phase-level quality:
  - OPENING: drift=0.2014, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1506, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1781, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1872, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_10actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1630 (+/- 0.0013)
- Clean persona drift MAE: 0.1630
- Per-trait absolute error: O 0.1220, C 0.1815, E 0.1500, A 0.1613, N 0.2000
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.2503
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1400
- Repetition rate: 0.0000
- Topic drift rate: 0.0455
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5012
- Commitment fulfillment rate: 0.4728
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1623, 0.1636]

- Phase-level quality:
  - OPENING: drift=0.1580, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1699, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1606, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1533, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_10actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1597 (+/- 0.0029)
- Clean persona drift MAE: 0.1597
- Per-trait absolute error: O 0.1140, C 0.1759, E 0.1512, A 0.1573, N 0.2000
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.4300
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0988
- Repetition rate: 0.0000
- Topic drift rate: 0.1818
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4356
- Commitment fulfillment rate: 0.5960
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1583, 0.161]

- Phase-level quality:
  - OPENING: drift=0.1573, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1653, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1618, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1628, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1629 (+/- 0.0031)
- Clean persona drift MAE: 0.1629
- Per-trait absolute error: O 0.2067, C 0.2000, E 0.1080, A 0.1333, N 0.1667
- Relationship inconsistency: 0.3453
- Relationship shift rate: 0.3055
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8333
- Clean envelope violations: 1.8333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9545
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1135
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5313
- Commitment fulfillment rate: 0.5625
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1615, 0.1644]

- Phase-level quality:
  - OPENING: drift=0.1557, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1593, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1602, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1810, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1670 (+/- 0.0001)
- Clean persona drift MAE: 0.1670
- Per-trait absolute error: O 0.2400, C 0.2000, E 0.0935, A 0.1350, N 0.1667
- Relationship inconsistency: 0.0732
- Relationship shift rate: 0.2338
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1204
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5244
- Commitment fulfillment rate: 0.5143
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1669, 0.1671]

- Phase-level quality:
  - OPENING: drift=0.1647, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1620, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1711, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1810, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_5actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1537 (+/- 0.0001)
- Clean persona drift MAE: 0.1537
- Per-trait absolute error: O 0.1480, C 0.2132, E 0.1138, A 0.1475, N 0.1460
- Relationship inconsistency: 0.0432
- Relationship shift rate: 0.2060
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1123
- Repetition rate: 0.0000
- Topic drift rate: 0.9286
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4884
- Commitment fulfillment rate: 0.5808
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1536, 0.1538]

- Phase-level quality:
  - OPENING: drift=0.1471, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1558, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1598, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1565, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_5actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1767 (+/- 0.0078)
- Clean persona drift MAE: 0.1767
- Per-trait absolute error: O 0.1620, C 0.2286, E 0.1692, A 0.1795, N 0.1440
- Relationship inconsistency: 0.0977
- Relationship shift rate: 0.3315
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0832
- Repetition rate: 0.0000
- Topic drift rate: 0.9285
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4508
- Commitment fulfillment rate: 0.8541
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1725, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1515, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1585, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1822, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1828, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1563 (+/- 0.0004)
- Clean persona drift MAE: 0.1563
- Per-trait absolute error: O 0.1560, C 0.2019, E 0.1071, A 0.1506, N 0.1663
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2195
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0983
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4092
- Commitment fulfillment rate: 0.7033
- State trajectory variance: 0.0000
- Mean turns: 3.14
- Persona drift 95% CI: [0.1562, 0.1565]

- Phase-level quality:
  - OPENING: drift=0.1711, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1649, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1561, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1672, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1693 (+/- 0.0021)
- Clean persona drift MAE: 0.1693
- Per-trait absolute error: O 0.1900, C 0.2155, E 0.1204, A 0.1578, N 0.1627
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2978
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0761
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3921
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 3.14
- Persona drift 95% CI: [0.1682, 0.1703]

- Phase-level quality:
  - OPENING: drift=0.1762, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1767, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1658, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1706, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1505 (+/- 0.0146)
- Clean persona drift MAE: 0.1505
- Per-trait absolute error: O 0.2067, C 0.1637, E 0.0869, A 0.1284, N 0.1667
- Relationship inconsistency: 0.1036
- Relationship shift rate: 0.2252
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.1666
- Clean envelope violations: 1.1666
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0979
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3083
- Commitment fulfillment rate: 0.8000
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1428, 0.1581]

- Phase-level quality:
  - OPENING: drift=0.1720, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1605, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1622, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1840, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0065)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1900, C 0.2147, E 0.1383, A 0.1133, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1930
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0838
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3429
- Commitment fulfillment rate: 0.9285
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1625, 0.1693]

- Phase-level quality:
  - OPENING: drift=0.1746, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1879, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1744, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1822, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1558 (+/- 0.0173)
- Clean persona drift MAE: 0.1558
- Per-trait absolute error: O 0.1720, C 0.2220, E 0.0857, A 0.1415, N 0.1580
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2162
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1315
- Repetition rate: 0.0000
- Topic drift rate: 0.3215
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3460
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1468, 0.1649]

- Phase-level quality:
  - OPENING: drift=0.1651, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1600, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1696, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1767, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1665 (+/- 0.0013)
- Clean persona drift MAE: 0.1665
- Per-trait absolute error: O 0.2340, C 0.2022, E 0.0923, A 0.1560, N 0.1480
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2775
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0788
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3782
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1658, 0.1672]

- Phase-level quality:
  - OPENING: drift=0.1849, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1605, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1675, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1636, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1671 (+/- 0.0010)
- Clean persona drift MAE: 0.1671
- Per-trait absolute error: O 0.1970, C 0.1800, E 0.1216, A 0.1764, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2570
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1212
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3893
- Commitment fulfillment rate: 0.7929
- State trajectory variance: 0.0000
- Mean turns: 3.14
- Persona drift 95% CI: [0.1665, 0.1676]

- Phase-level quality:
  - OPENING: drift=0.1633, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1720, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1637, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1755, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1738 (+/- 0.0029)
- Clean persona drift MAE: 0.1738
- Per-trait absolute error: O 0.2020, C 0.1834, E 0.1479, A 0.1767, N 0.1589
- Relationship inconsistency: 0.3375
- Relationship shift rate: 0.3354
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0844
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3689
- Commitment fulfillment rate: 0.7857
- State trajectory variance: 0.0000
- Mean turns: 3.14
- Persona drift 95% CI: [0.1722, 0.1753]

- Phase-level quality:
  - OPENING: drift=0.1725, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1786, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1678, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1856, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.2059 (+/- 0.0066)
- Clean persona drift MAE: 0.2059
- Per-trait absolute error: O 0.2200, C 0.2333, E 0.1232, A 0.2133, N 0.2400
- Relationship inconsistency: 0.1555
- Relationship shift rate: 0.2900
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6666
- Clean envelope violations: 2.6666
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1070
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4564
- Commitment fulfillment rate: 0.8286
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.2025, 0.2094]

- Phase-level quality:
  - OPENING: drift=0.2030, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2186, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2137, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2061, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### flint_water_crisis_3actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.2180 (+/- 0.0098)
- Clean persona drift MAE: 0.2180
- Per-trait absolute error: O 0.2367, C 0.2407, E 0.1592, A 0.2267, N 0.2267
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Clean envelope violations: 3.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0754
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4150
- Commitment fulfillment rate: 0.7750
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.2128, 0.2231]

- Phase-level quality:
  - OPENING: drift=0.2145, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2137, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2310, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2052, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:engine_structural
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0066)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1540, C 0.2400, E 0.1006, A 0.1570, N 0.1750
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.2343
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.1483
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1454
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4313
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1619, 0.1688]

- Phase-level quality:
  - OPENING: drift=0.1592, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1705, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1830, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1614, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1834 (+/- 0.0056)
- Clean persona drift MAE: 0.1834
- Per-trait absolute error: O 0.1540, C 0.2576, E 0.1419, A 0.1805, N 0.1830
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.1487
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0932
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3931
- Commitment fulfillment rate: 0.6000
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1805, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1798, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1966, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1675, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1638 (+/- 0.0019)
- Clean persona drift MAE: 0.1638
- Per-trait absolute error: O 0.1930, C 0.1972, E 0.1034, A 0.1289, N 0.1960
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0857
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5072
- Commitment fulfillment rate: 0.5960
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1627, 0.1648]

- Phase-level quality:
  - OPENING: drift=0.1740, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1626, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1705, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1632, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1711 (+/- 0.0011)
- Clean persona drift MAE: 0.1711
- Per-trait absolute error: O 0.2030, C 0.1928, E 0.1304, A 0.1283, N 0.2011
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3454
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0697
- Repetition rate: 0.0000
- Topic drift rate: 0.7272
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5136
- Commitment fulfillment rate: 0.8435
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1705, 0.1717]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1720, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1749, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1677, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1511 (+/- 0.0029)
- Clean persona drift MAE: 0.1511
- Per-trait absolute error: O 0.1900, C 0.1780, E 0.1489, A 0.1050, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.8055
- Negotiation uniqueness: 0.1834
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0801
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4738
- Commitment fulfillment rate: 0.1666
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1494, 0.1527]

- Phase-level quality:
  - OPENING: drift=0.1655, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1683, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1559, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1846, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1679 (+/- 0.0111)
- Clean persona drift MAE: 0.1679
- Per-trait absolute error: O 0.2567, C 0.1707, E 0.1787, A 0.1000, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2300
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0626
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5097
- Commitment fulfillment rate: 0.4166
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1616, 0.1742]

- Phase-level quality:
  - OPENING: drift=0.1607, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1535, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1823, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2223, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1965 (+/- 0.0077)
- Clean persona drift MAE: 0.1965
- Per-trait absolute error: O 0.1940, C 0.2349, E 0.1645, A 0.2150, N 0.1740
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1787
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0827
- Repetition rate: 0.0000
- Topic drift rate: 0.6786
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4120
- Commitment fulfillment rate: 0.7778
- State trajectory variance: 0.0000
- Mean turns: 2.33
- Persona drift 95% CI: [0.1921, 0.2009]

- Phase-level quality:
  - OPENING: drift=0.1854, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2131, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1984, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1868, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.2069 (+/- 0.0073)
- Clean persona drift MAE: 0.2069
- Per-trait absolute error: O 0.2240, C 0.2288, E 0.2055, A 0.2125, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1459
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0731
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4188
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 2.33
- Persona drift 95% CI: [0.2028, 0.2111]

- Phase-level quality:
  - OPENING: drift=0.1850, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2215, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2207, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1995, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1683 (+/- 0.0025)
- Clean persona drift MAE: 0.1683
- Per-trait absolute error: O 0.1390, C 0.2313, E 0.1386, A 0.1395, N 0.1931
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0905
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4755
- Commitment fulfillment rate: 0.8125
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1669, 0.1697]

- Phase-level quality:
  - OPENING: drift=0.1503, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1893, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1730, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1900, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0015)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.1840, C 0.2369, E 0.1406, A 0.1473, N 0.1882
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3786
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0583
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4230
- Commitment fulfillment rate: 0.4428
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1786, 0.1803]

- Phase-level quality:
  - OPENING: drift=0.1672, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2069, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1768, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1887, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_3actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1636 (+/- 0.0123)
- Clean persona drift MAE: 0.1636
- Per-trait absolute error: O 0.1333, C 0.2333, E 0.0998, A 0.1450, N 0.2067
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2591
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1325
- Repetition rate: 0.0625
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3603
- Commitment fulfillment rate: 0.9285
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1566, 0.1706]

- Phase-level quality:
  - OPENING: drift=0.1598, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1677, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1731, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1830, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### fukushima_nuclear_restart_3actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1695 (+/- 0.0039)
- Clean persona drift MAE: 0.1695
- Per-trait absolute error: O 0.1567, C 0.2333, E 0.1094, A 0.1484, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0842
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3419
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1674, 0.1717]

- Phase-level quality:
  - OPENING: drift=0.1746, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1723, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1677, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1829, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1699 (+/- 0.0026)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1420, C 0.2272, E 0.1333, A 0.1150, N 0.2320
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3541
- Negotiation uniqueness: 0.0801
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0902
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3745
- Commitment fulfillment rate: 0.7857
- State trajectory variance: 0.0000
- Mean turns: 2.33
- Persona drift 95% CI: [0.1684, 0.1714]

- Phase-level quality:
  - OPENING: drift=0.1726, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1931, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1687, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1656, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0004)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.1820, C 0.1996, E 0.1444, A 0.1265, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2900
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0801
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3600
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 2.33
- Persona drift 95% CI: [0.1743, 0.1748]

- Phase-level quality:
  - OPENING: drift=0.1838, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1931, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1748, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1679, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0060)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.2080, C 0.1674, E 0.1241, A 0.1377, N 0.1695
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2405
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0804
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3339
- Commitment fulfillment rate: 0.7663
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1579, 0.1648]

- Phase-level quality:
  - OPENING: drift=0.1453, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1784, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1628, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1709, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1710 (+/- 0.0041)
- Clean persona drift MAE: 0.1710
- Per-trait absolute error: O 0.2080, C 0.1707, E 0.1575, A 0.1560, N 0.1627
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4325
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0798
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2827
- Commitment fulfillment rate: 0.8334
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1687, 0.1733]

- Phase-level quality:
  - OPENING: drift=0.1583, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1906, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1694, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1694, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1895 (+/- 0.0055)
- Clean persona drift MAE: 0.1895
- Per-trait absolute error: O 0.2266, C 0.2333, E 0.0762, A 0.2117, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0850
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.6111
- Negotiation uniqueness: 0.1458
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1046
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.1810
- Commitment fulfillment rate: 0.9375
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1864, 0.1927]

- Phase-level quality:
  - OPENING: drift=0.1916, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1956, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1899, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1667, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### japan_intern_training_reform_3actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1904 (+/- 0.0024)
- Clean persona drift MAE: 0.1904
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.0952, A 0.2067, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4875
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0683
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2485
- Commitment fulfillment rate: 0.5834
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1889, 0.1918]

- Phase-level quality:
  - OPENING: drift=0.1935, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1938, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1976, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1776, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0029)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1920, C 0.2400, E 0.0872, A 0.1265, N 0.1800
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4238
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1008
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3734
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.1633, 0.167]

- Phase-level quality:
  - OPENING: drift=0.1664, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1446, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1562, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1639 (+/- 0.0094)
- Clean persona drift MAE: 0.1639
- Per-trait absolute error: O 0.1780, C 0.2400, E 0.1095, A 0.1260, N 0.1660
- Relationship inconsistency: 0.2430
- Relationship shift rate: 0.4229
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0992
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2923
- Commitment fulfillment rate: 0.5476
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.1581, 0.1697]

- Phase-level quality:
  - OPENING: drift=0.1800, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1537, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1523, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2043, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1845 (+/- 0.0009)
- Clean persona drift MAE: 0.1845
- Per-trait absolute error: O 0.2030, C 0.2003, E 0.1537, A 0.2006, N 0.1649
- Relationship inconsistency: 0.4953
- Relationship shift rate: 0.3374
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1013
- Repetition rate: 0.0000
- Topic drift rate: 0.3637
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4704
- Commitment fulfillment rate: 0.7462
- State trajectory variance: 0.0000
- Mean turns: 4.40
- Persona drift 95% CI: [0.1839, 0.1851]

- Phase-level quality:
  - OPENING: drift=0.1911, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1930, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1778, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.2053, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1953 (+/- 0.0048)
- Clean persona drift MAE: 0.1953
- Per-trait absolute error: O 0.2520, C 0.1928, E 0.1788, A 0.1931, N 0.1595
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2803
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0791
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4867
- Commitment fulfillment rate: 0.8000
- State trajectory variance: 0.0000
- Mean turns: 4.40
- Persona drift 95% CI: [0.1923, 0.1982]

- Phase-level quality:
  - OPENING: drift=0.1976, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1990, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1879, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2064, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0004)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.1500, C 0.2667, E 0.1092, A 0.1467, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2520
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1292
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3981
- Commitment fulfillment rate: 0.7570
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1743, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1683, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1784, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1731, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1844, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1710 (+/- 0.0027)
- Clean persona drift MAE: 0.1710
- Per-trait absolute error: O 0.1400, C 0.2667, E 0.1081, A 0.1334, N 0.2067
- Relationship inconsistency: 0.1215
- Relationship shift rate: 0.4107
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0965
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4493
- Commitment fulfillment rate: 0.7000
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1693, 0.1727]

- Phase-level quality:
  - OPENING: drift=0.1790, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1676, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1724, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1816, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1583 (+/- 0.0018)
- Clean persona drift MAE: 0.1583
- Per-trait absolute error: O 0.1800, C 0.2000, E 0.1018, A 0.1320, N 0.1780
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1031
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4758
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.1573, 0.1594]

- Phase-level quality:
  - OPENING: drift=0.1719, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1668, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1612, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1748, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0028)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.2140, C 0.2000, E 0.1275, A 0.1285, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2425
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0785
- Repetition rate: 0.0000
- Topic drift rate: 0.4285
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4895
- Commitment fulfillment rate: 0.6666
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.1683, 0.1717]

- Phase-level quality:
  - OPENING: drift=0.1817, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1646, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1614, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2097, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1785 (+/- 0.0031)
- Clean persona drift MAE: 0.1785
- Per-trait absolute error: O 0.2280, C 0.1999, E 0.1437, A 0.1663, N 0.1547
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0953
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4123
- Commitment fulfillment rate: 0.8000
- State trajectory variance: 0.0000
- Mean turns: 4.40
- Persona drift 95% CI: [0.1767, 0.1804]

- Phase-level quality:
  - OPENING: drift=0.1723, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1936, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1748, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1870, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1886 (+/- 0.0029)
- Clean persona drift MAE: 0.1886
- Per-trait absolute error: O 0.2480, C 0.1973, E 0.1773, A 0.1701, N 0.1507
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.3805
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0601
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4577
- Commitment fulfillment rate: 0.7785
- State trajectory variance: 0.0000
- Mean turns: 4.40
- Persona drift 95% CI: [0.1868, 0.1905]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2031, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1831, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1832, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1950 (+/- 0.0050)
- Clean persona drift MAE: 0.1950
- Per-trait absolute error: O 0.1667, C 0.2333, E 0.2000, A 0.2016, N 0.1733
- Relationship inconsistency: 0.0844
- Relationship shift rate: 0.2525
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1018
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4578
- Commitment fulfillment rate: 0.7000
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1919, 0.1981]

- Phase-level quality:
  - OPENING: drift=0.2034, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2056, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1950, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1711, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.2040 (+/- 0.0040)
- Clean persona drift MAE: 0.2040
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.2000, A 0.2100, N 0.1867
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1925
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6666
- Clean envelope violations: 2.6666
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0765
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4352
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.2015, 0.2065]

- Phase-level quality:
  - OPENING: drift=0.2071, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2037, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2067, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1768, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:engine_structural
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.1871 (+/- 0.0042)
- Clean persona drift MAE: 0.1871
- Per-trait absolute error: O 0.1440, C 0.2178, E 0.1932, A 0.1685, N 0.2120
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2091
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1126
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4810
- Commitment fulfillment rate: 0.8889
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.1845, 0.1897]

- Phase-level quality:
  - OPENING: drift=0.2042, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1940, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1743, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:naive
- Runs: 10
- Clean runs: 10
- Contaminated runs: 0
- Persona drift MAE: 0.2171 (+/- 0.0061)
- Clean persona drift MAE: 0.2171
- Per-trait absolute error: O 0.2020, C 0.2310, E 0.2460, A 0.1835, N 0.2230
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3237
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Clean envelope violations: 3.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4975
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.2133, 0.2209]

- Phase-level quality:
  - OPENING: drift=0.2175, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2056, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2046, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2584, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### nyc_congestion_pricing_10actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1568 (+/- 0.0002)
- Clean persona drift MAE: 0.1568
- Per-trait absolute error: O 0.1480, C 0.1672, E 0.1379, A 0.1683, N 0.1623
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.2483
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0792
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4675
- Commitment fulfillment rate: 0.5250
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1566, 0.1569]

- Phase-level quality:
  - OPENING: drift=0.1573, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1795, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1560, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1765, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1682 (+/- 0.0038)
- Clean persona drift MAE: 0.1682
- Per-trait absolute error: O 0.1740, C 0.1764, E 0.1467, A 0.1839, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2654
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0715
- Repetition rate: 0.0000
- Topic drift rate: 0.5227
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4789
- Commitment fulfillment rate: 0.3423
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1656, 0.1708]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1818, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1636, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1710, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1630 (+/- 0.0030)
- Clean persona drift MAE: 0.1630
- Per-trait absolute error: O 0.1200, C 0.2000, E 0.1667, A 0.1283, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2040
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8333
- Clean envelope violations: 1.8333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0992
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4641
- Commitment fulfillment rate: 0.9000
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1609, 0.1651]

- Phase-level quality:
  - OPENING: drift=0.1678, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1631, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1662, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1530, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1619 (+/- 0.0072)
- Clean persona drift MAE: 0.1619
- Per-trait absolute error: O 0.1000, C 0.2000, E 0.1710, A 0.1384, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1720
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6666
- Clean envelope violations: 1.6666
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0915
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4989
- Commitment fulfillment rate: 0.3333
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1569, 0.1669]

- Phase-level quality:
  - OPENING: drift=0.1623, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1744, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1623, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1520, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1435 (+/- 0.0026)
- Clean persona drift MAE: 0.1435
- Per-trait absolute error: O 0.1440, C 0.2800, E 0.1343, A 0.0730, N 0.0860
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1891
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0999
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4256
- Commitment fulfillment rate: 0.6072
- State trajectory variance: 0.0000
- Mean turns: 3.50
- Persona drift 95% CI: [0.1416, 0.1453]

- Phase-level quality:
  - OPENING: drift=0.1436, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1395, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1540, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1322, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### nyc_congestion_pricing_5actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1452 (+/- 0.0006)
- Clean persona drift MAE: 0.1452
- Per-trait absolute error: O 0.1300, C 0.2800, E 0.1411, A 0.0870, N 0.0880
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2000
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0857
- Repetition rate: 0.0000
- Topic drift rate: 0.7143
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4669
- Commitment fulfillment rate: 0.4143
- State trajectory variance: 0.0000
- Mean turns: 3.50
- Persona drift 95% CI: [0.1448, 0.1456]

- Phase-level quality:
  - OPENING: drift=0.1609, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1382, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1526, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1367, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1691 (+/- 0.0013)
- Clean persona drift MAE: 0.1691
- Per-trait absolute error: O 0.1670, C 0.2600, E 0.1215, A 0.1206, N 0.1767
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2601
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1100
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4366
- Commitment fulfillment rate: 0.9373
- State trajectory variance: 0.0001
- Mean turns: 5.50
- Persona drift 95% CI: [0.1682, 0.17]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1580, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1781, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1619, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1726 (+/- 0.0015)
- Clean persona drift MAE: 0.1726
- Per-trait absolute error: O 0.1820, C 0.2601, E 0.1253, A 0.1250, N 0.1707
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.2660
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0813
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4293
- Commitment fulfillment rate: 0.5917
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1716, 0.1736]

- Phase-level quality:
  - OPENING: drift=0.1741, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1628, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1847, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1606, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1573 (+/- 0.0079)
- Clean persona drift MAE: 0.1573
- Per-trait absolute error: O 0.0900, C 0.2480, E 0.1503, A 0.1450, N 0.1533
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2045
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6666
- Clean envelope violations: 1.6666
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0993
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4120
- Commitment fulfillment rate: 0.7571
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1518, 0.1629]

- Phase-level quality:
  - OPENING: drift=0.1708, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1729, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1720, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1496, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1828 (+/- 0.0064)
- Clean persona drift MAE: 0.1828
- Per-trait absolute error: O 0.1400, C 0.2333, E 0.1888, A 0.1784, N 0.1734
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.2600
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0815
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3879
- Commitment fulfillment rate: 0.4667
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1783, 0.1872]

- Phase-level quality:
  - OPENING: drift=0.1929, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1828, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1779, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1754, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1521 (+/- 0.0010)
- Clean persona drift MAE: 0.1521
- Per-trait absolute error: O 0.1500, C 0.2072, E 0.1217, A 0.1255, N 0.1560
- Relationship inconsistency: 0.1840
- Relationship shift rate: 0.2888
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1237
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4340
- Commitment fulfillment rate: 0.6607
- State trajectory variance: 0.0000
- Mean turns: 3.50
- Persona drift 95% CI: [0.1514, 0.1528]

- Phase-level quality:
  - OPENING: drift=0.1699, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1380, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1542, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1951, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1588 (+/- 0.0004)
- Clean persona drift MAE: 0.1588
- Per-trait absolute error: O 0.1540, C 0.2154, E 0.1492, A 0.1185, N 0.1570
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4863
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0822
- Repetition rate: 0.0000
- Topic drift rate: 0.7143
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4231
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 3.50
- Persona drift 95% CI: [0.1586, 0.1591]

- Phase-level quality:
  - OPENING: drift=0.1786, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1402, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1585, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1961, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1732 (+/- 0.0011)
- Clean persona drift MAE: 0.1732
- Per-trait absolute error: O 0.1670, C 0.2224, E 0.1216, A 0.1761, N 0.1789
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2026
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1104
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4349
- Commitment fulfillment rate: 0.8125
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1724, 0.174]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1724, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1867, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1565, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1788 (+/- 0.0042)
- Clean persona drift MAE: 0.1788
- Per-trait absolute error: O 0.1890, C 0.2205, E 0.1433, A 0.1700, N 0.1709
- Relationship inconsistency: 0.1465
- Relationship shift rate: 0.2323
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1023
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3815
- Commitment fulfillment rate: 0.6462
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1759, 0.1816]

- Phase-level quality:
  - OPENING: drift=0.1822, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1728, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1988, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1594, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1550 (+/- 0.0063)
- Clean persona drift MAE: 0.1550
- Per-trait absolute error: O 0.0834, C 0.2257, E 0.0844, A 0.1750, N 0.2067
- Relationship inconsistency: 0.0250
- Relationship shift rate: 0.2104
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1278
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4452
- Commitment fulfillment rate: 0.4500
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1506, 0.1594]

- Phase-level quality:
  - OPENING: drift=0.1738, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1683, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1674, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1656, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1783 (+/- 0.0092)
- Clean persona drift MAE: 0.1783
- Per-trait absolute error: O 0.1734, C 0.2074, E 0.1056, A 0.2016, N 0.2034
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2220
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0764
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4778
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1708, 0.1857]

- Phase-level quality:
  - OPENING: drift=0.1784, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1816, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1737, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1720, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1654 (+/- 0.0037)
- Clean persona drift MAE: 0.1654
- Per-trait absolute error: O 0.0920, C 0.2220, E 0.1600, A 0.1725, N 0.1810
- Relationship inconsistency: 0.2590
- Relationship shift rate: 0.2698
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1084
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3566
- Commitment fulfillment rate: 0.7291
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.1625, 0.1684]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1729, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1697, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1528, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### sf_homelessness_policy_5actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1797 (+/- 0.0028)
- Clean persona drift MAE: 0.1797
- Per-trait absolute error: O 0.1340, C 0.2088, E 0.1910, A 0.1805, N 0.1840
- Relationship inconsistency: 0.0187
- Relationship shift rate: 0.2121
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0956
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3879
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.1774, 0.1819]

- Phase-level quality:
  - OPENING: drift=0.1969, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1875, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1799, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1592, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1841 (+/- 0.0039)
- Clean persona drift MAE: 0.1841
- Per-trait absolute error: O 0.1130, C 0.2409, E 0.2185, A 0.2014, N 0.1471
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3073
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.3021
- Negotiation uniqueness: 0.0541
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0895
- Repetition rate: 0.0000
- Topic drift rate: 0.8409
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4068
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 7.33
- Persona drift 95% CI: [0.1811, 0.1872]

- Phase-level quality:
  - OPENING: drift=0.1798, convergence=1.0000, diversity=0.2083
  - TENSION: drift=0.1944, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1837, convergence=1.0000, diversity=0.2083
  - CLOSING: drift=0.1967, convergence=0.5000, diversity=0.1250

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1935 (+/- 0.0014)
- Clean persona drift MAE: 0.1935
- Per-trait absolute error: O 0.1530, C 0.2463, E 0.2240, A 0.1949, N 0.1489
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2207
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7500
- Clean envelope violations: 2.7500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0844
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3468
- Commitment fulfillment rate: 0.7570
- State trajectory variance: 0.0000
- Mean turns: 7.33
- Persona drift 95% CI: [0.1923, 0.1946]

- Phase-level quality:
  - OPENING: drift=0.1911, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2080, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1810, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1986, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1973 (+/- 0.0100)
- Clean persona drift MAE: 0.1973
- Per-trait absolute error: O 0.1600, C 0.2667, E 0.1000, A 0.2267, N 0.2334
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6666
- Clean envelope violations: 2.6666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4283
- Commitment fulfillment rate: 0.4667
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1893, 0.2053]

- Phase-level quality:
  - OPENING: drift=0.1910, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1987, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1844, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1996, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1922 (+/- 0.0062)
- Clean persona drift MAE: 0.1922
- Per-trait absolute error: O 0.1933, C 0.2667, E 0.1094, A 0.1983, N 0.1933
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.2860
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0772
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4395
- Commitment fulfillment rate: 0.5834
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1872, 0.1972]

- Phase-level quality:
  - OPENING: drift=0.1886, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1878, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1964, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2066, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1961 (+/- 0.0000)
- Clean persona drift MAE: 0.1961
- Per-trait absolute error: O 0.1940, C 0.2800, E 0.1557, A 0.1645, N 0.1860
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2438
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1062
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4503
- Commitment fulfillment rate: 0.7223
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.196, 0.1961]

- Phase-level quality:
  - OPENING: drift=0.1901, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2141, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1980, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2131, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### singapore_hdb_waittime_crisis_5actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.2028 (+/- 0.0009)
- Clean persona drift MAE: 0.2028
- Per-trait absolute error: O 0.1900, C 0.2800, E 0.1491, A 0.1650, N 0.2300
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3400
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0910
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4929
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.2021, 0.2035]

- Phase-level quality:
  - OPENING: drift=0.1928, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2034, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2060, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2173, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1585 (+/- 0.0048)
- Clean persona drift MAE: 0.1585
- Per-trait absolute error: O 0.1810, C 0.1795, E 0.1159, A 0.1775, N 0.1387
- Relationship inconsistency: 0.1469
- Relationship shift rate: 0.2924
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0937
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3680
- Commitment fulfillment rate: 0.7350
- State trajectory variance: 0.0000
- Mean turns: 7.33
- Persona drift 95% CI: [0.1547, 0.1623]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1462, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1709, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1590, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1602 (+/- 0.0011)
- Clean persona drift MAE: 0.1602
- Per-trait absolute error: O 0.1840, C 0.1907, E 0.1170, A 0.1855, N 0.1236
- Relationship inconsistency: 0.2590
- Relationship shift rate: 0.5685
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0601
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3812
- Commitment fulfillment rate: 0.6072
- State trajectory variance: 0.0000
- Mean turns: 7.33
- Persona drift 95% CI: [0.1593, 0.161]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1547, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1675, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1550, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_3actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1449 (+/- 0.0002)
- Clean persona drift MAE: 0.1449
- Per-trait absolute error: O 0.1633, C 0.1000, E 0.0943, A 0.1667, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3184
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.3334
- Clean envelope violations: 1.3334
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.4584
- Negotiation uniqueness: 0.1000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1132
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4334
- Commitment fulfillment rate: 0.7143
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1447, 0.1451]

- Phase-level quality:
  - OPENING: drift=0.1543, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1594, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1394, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1589, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0103)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1467, C 0.1000, E 0.1332, A 0.2233, N 0.2000
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.2908
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1667
- Clean envelope violations: 2.1667
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0873
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4264
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1524, 0.1688]

- Phase-level quality:
  - OPENING: drift=0.1658, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1600, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1512, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1690, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1872 (+/- 0.0031)
- Clean persona drift MAE: 0.1872
- Per-trait absolute error: O 0.1480, C 0.2033, E 0.1512, A 0.2275, N 0.2060
- Relationship inconsistency: 0.4336
- Relationship shift rate: 0.3128
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3438
- Negotiation uniqueness: 0.0774
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0861
- Repetition rate: 0.0000
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4406
- Commitment fulfillment rate: 0.8611
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.1847, 0.1897]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1794, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1771, convergence=1.0000, diversity=0.3750
  - CLOSING: drift=0.2307, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1893 (+/- 0.0039)
- Clean persona drift MAE: 0.1893
- Per-trait absolute error: O 0.1880, C 0.2000, E 0.1394, A 0.2160, N 0.2030
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.5316
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0712
- Repetition rate: 0.0000
- Topic drift rate: 0.8214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3874
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.1862, 0.1924]

- Phase-level quality:
  - OPENING: drift=0.1977, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1812, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1859, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2206, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1573 (+/- 0.0052)
- Clean persona drift MAE: 0.1573
- Per-trait absolute error: O 0.1720, C 0.2198, E 0.1119, A 0.1273, N 0.1556
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2230
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0991
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4416
- Commitment fulfillment rate: 0.7071
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1522, 0.1625]

- Phase-level quality:
  - OPENING: drift=0.1583, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1691, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1615, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1609, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1734 (+/- 0.0033)
- Clean persona drift MAE: 0.1734
- Per-trait absolute error: O 0.1840, C 0.2277, E 0.1487, A 0.1446, N 0.1618
- Relationship inconsistency: 0.3223
- Relationship shift rate: 0.3820
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0915
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4122
- Commitment fulfillment rate: 0.5238
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1702, 0.1765]

- Phase-level quality:
  - OPENING: drift=0.1718, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1804, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1708, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1749, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1443 (+/- 0.0029)
- Clean persona drift MAE: 0.1443
- Per-trait absolute error: O 0.1767, C 0.2450, E 0.0249, A 0.1483, N 0.1266
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1709
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6666
- Clean envelope violations: 1.6666
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1181
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3735
- Commitment fulfillment rate: 0.6945
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1415, 0.1472]

- Phase-level quality:
  - OPENING: drift=0.1545, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1659, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1547, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1626, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1688 (+/- 0.0125)
- Clean persona drift MAE: 0.1688
- Per-trait absolute error: O 0.1767, C 0.3129, E 0.0792, A 0.1417, N 0.1333
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.3170
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0929
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3702
- Commitment fulfillment rate: 0.8334
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1565, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1710, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1704, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1724, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1734, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1703 (+/- 0.0042)
- Clean persona drift MAE: 0.1703
- Per-trait absolute error: O 0.1640, C 0.2105, E 0.1331, A 0.1240, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1900
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1310
- Repetition rate: 0.0000
- Topic drift rate: 0.4285
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4111
- Commitment fulfillment rate: 0.6175
- State trajectory variance: 0.0000
- Mean turns: 7.00
- Persona drift 95% CI: [0.1662, 0.1744]

- Phase-level quality:
  - OPENING: drift=0.1973, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1541, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1734, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2092, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0052)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1409, A 0.1170, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2093
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0854
- Repetition rate: 0.0000
- Topic drift rate: 0.6428
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3630
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 7.00
- Persona drift 95% CI: [0.1653, 0.1755]

- Phase-level quality:
  - OPENING: drift=0.1895, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1532, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1801, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2085, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1646 (+/- 0.0005)
- Clean persona drift MAE: 0.1646
- Per-trait absolute error: O 0.1240, C 0.2600, E 0.1356, A 0.1316, N 0.1718
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.3476
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5000
- Action family convergence: 1.0000
- Role action diversity: 0.2437
- Negotiation uniqueness: 0.0572
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1128
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4048
- Commitment fulfillment rate: 0.5757
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1641, 0.1651]

- Phase-level quality:
  - OPENING: drift=0.1760, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1689, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1707, convergence=1.0000, diversity=0.2250
  - CLOSING: drift=0.1733, convergence=1.0000, diversity=0.2916

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1787 (+/- 0.0035)
- Clean persona drift MAE: 0.1787
- Per-trait absolute error: O 0.1780, C 0.2600, E 0.1518, A 0.1364, N 0.1669
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0702
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3832
- Commitment fulfillment rate: 0.7071
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1753, 0.182]

- Phase-level quality:
  - OPENING: drift=0.1762, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1759, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1831, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1825, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1736 (+/- 0.0055)
- Clean persona drift MAE: 0.1736
- Per-trait absolute error: O 0.1133, C 0.3000, E 0.1029, A 0.1517, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2415
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1078
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4723
- Commitment fulfillment rate: 0.5750
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1682, 0.179]

- Phase-level quality:
  - OPENING: drift=0.1884, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1860, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1837, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1888 (+/- 0.0045)
- Clean persona drift MAE: 0.1888
- Per-trait absolute error: O 0.1700, C 0.3000, E 0.0975, A 0.1767, N 0.2000
- Relationship inconsistency: 0.1465
- Relationship shift rate: 0.4175
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0767
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4191
- Commitment fulfillment rate: 0.7000
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1844, 0.1932]

- Phase-level quality:
  - OPENING: drift=0.1943, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1815, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1857, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1922, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1885 (+/- 0.0001)
- Clean persona drift MAE: 0.1885
- Per-trait absolute error: O 0.1560, C 0.2000, E 0.1573, A 0.2450, N 0.1840
- Relationship inconsistency: 0.1688
- Relationship shift rate: 0.3430
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.8333
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0935
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4095
- Commitment fulfillment rate: 0.8572
- State trajectory variance: 0.0000
- Mean turns: 7.00
- Persona drift 95% CI: [0.1883, 0.1886]

- Phase-level quality:
  - OPENING: drift=0.2041, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1809, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1998, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2100, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1953 (+/- 0.0068)
- Clean persona drift MAE: 0.1953
- Per-trait absolute error: O 0.1760, C 0.2176, E 0.1692, A 0.2360, N 0.1780
- Relationship inconsistency: 0.5860
- Relationship shift rate: 0.5013
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0755
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3652
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 7.00
- Persona drift 95% CI: [0.1886, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.2001, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1807, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2090, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2188, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1883 (+/- 0.0008)
- Clean persona drift MAE: 0.1883
- Per-trait absolute error: O 0.1790, C 0.1733, E 0.2113, A 0.1980, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2300
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.2046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4074
- Commitment fulfillment rate: 0.8572
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1875, 0.1891]

- Phase-level quality:
  - OPENING: drift=0.2007, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1946, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1888, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1876, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1934 (+/- 0.0020)
- Clean persona drift MAE: 0.1934
- Per-trait absolute error: O 0.1990, C 0.1785, E 0.2103, A 0.1990, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2000
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0736
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3948
- Commitment fulfillment rate: 0.5357
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1914, 0.1954]

- Phase-level quality:
  - OPENING: drift=0.1996, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1982, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1910, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1887, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0010)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.1333, C 0.3000, E 0.1000, A 0.2383, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.1750
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1032
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3690
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1733, 0.1753]

- Phase-level quality:
  - OPENING: drift=0.1717, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1697, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1690, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1930, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1744 (+/- 0.0057)
- Clean persona drift MAE: 0.1744
- Per-trait absolute error: O 0.1233, C 0.3000, E 0.1000, A 0.2416, N 0.1066
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1950
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0850
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3430
- Commitment fulfillment rate: 0.9166
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1665, 0.1822]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1677, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1764, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1930, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1697 (+/- 0.0045)
- Clean persona drift MAE: 0.1697
- Per-trait absolute error: O 0.2200, C 0.2039, E 0.1051, A 0.1995, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3171
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0923
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3554
- Commitment fulfillment rate: 0.6167
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1635, 0.1759]

- Phase-level quality:
  - OPENING: drift=0.1972, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1555, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1666, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2150, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1790 (+/- 0.0014)
- Clean persona drift MAE: 0.1790
- Per-trait absolute error: O 0.2140, C 0.2039, E 0.1394, A 0.2180, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3819
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0884
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3172
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.177, 0.1811]

- Phase-level quality:
  - OPENING: drift=0.1951, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1695, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1767, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2237, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0005)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.2010, C 0.2093, E 0.1962, A 0.1502, N 0.1036
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0960
- Repetition rate: 0.0416
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4248
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1714, 0.1728]

- Phase-level quality:
  - OPENING: drift=0.1634, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1837, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1663, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1913, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### wework_ipo_collapse_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1815 (+/- 0.0016)
- Clean persona drift MAE: 0.1815
- Per-trait absolute error: O 0.2180, C 0.1956, E 0.2287, A 0.1593, N 0.1063
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4135
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0711
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4148
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1793, 0.1838]

- Phase-level quality:
  - OPENING: drift=0.1850, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1831, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1752, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1874, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1860 (+/- 0.0043)
- Clean persona drift MAE: 0.1860
- Per-trait absolute error: O 0.1400, C 0.2000, E 0.1452, A 0.2217, N 0.2233
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1239
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3836
- Commitment fulfillment rate: 0.8055
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.18, 0.192]

- Phase-level quality:
  - OPENING: drift=0.1880, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1983, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1908, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2106 (+/- 0.0122)
- Clean persona drift MAE: 0.2106
- Per-trait absolute error: O 0.1567, C 0.2623, E 0.1719, A 0.2283, N 0.2333
- Relationship inconsistency: 0.0461
- Relationship shift rate: 0.2126
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1049
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4112
- Commitment fulfillment rate: 0.7143
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1936, 0.2275]

- Phase-level quality:
  - OPENING: drift=0.2039, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1950, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1976, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2150, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1488 (+/- 0.0064)
- Clean persona drift MAE: 0.1488
- Per-trait absolute error: O 0.1000, C 0.1956, E 0.1663, A 0.1305, N 0.1520
- Relationship inconsistency: 0.1146
- Relationship shift rate: 0.2778
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1187
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4374
- Commitment fulfillment rate: 0.4250
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.14, 0.1577]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1724, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1382, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1635, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1650 (+/- 0.0011)
- Clean persona drift MAE: 0.1650
- Per-trait absolute error: O 0.1640, C 0.1912, E 0.1914, A 0.1385, N 0.1400
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2036
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0864
- Repetition rate: 0.0000
- Topic drift rate: 0.6428
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4373
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1635, 0.1665]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1728, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1578, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1846 (+/- 0.0004)
- Clean persona drift MAE: 0.1846
- Per-trait absolute error: O 0.1830, C 0.2800, E 0.1442, A 0.1588, N 0.1572
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2720
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6250
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1016
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4156
- Commitment fulfillment rate: 0.9737
- State trajectory variance: 0.0001
- Mean turns: 22.00
- Persona drift 95% CI: [0.184, 0.1852]

- Phase-level quality:
  - OPENING: drift=0.1854, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1918, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1926, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1794, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1938 (+/- 0.0011)
- Clean persona drift MAE: 0.1938
- Per-trait absolute error: O 0.2180, C 0.2800, E 0.1537, A 0.1659, N 0.1513
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4088
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8000
- Clean envelope violations: 2.8000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0709
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3979
- Commitment fulfillment rate: 0.9231
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1923, 0.1953]

- Phase-level quality:
  - OPENING: drift=0.1961, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1928, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2033, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1835, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0078)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.1033, C 0.2333, E 0.1680, A 0.1700, N 0.2000
- Relationship inconsistency: 0.1405
- Relationship shift rate: 0.2475
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1061
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3487
- Commitment fulfillment rate: 0.9375
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1642, 0.1857]

- Phase-level quality:
  - OPENING: drift=0.2007, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1844, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1867, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1815, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1993 (+/- 0.0056)
- Clean persona drift MAE: 0.1993
- Per-trait absolute error: O 0.1700, C 0.2333, E 0.2299, A 0.1633, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0731
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3698
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1915, 0.2072]

- Phase-level quality:
  - OPENING: drift=0.2038, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2085, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1980, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1935, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### zoom_return_to_office_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1998 (+/- 0.0168)
- Clean persona drift MAE: 0.1998
- Per-trait absolute error: O 0.2420, C 0.2464, E 0.1785, A 0.1700, N 0.1620
- Relationship inconsistency: 0.2893
- Relationship shift rate: 0.3369
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1185
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4032
- Commitment fulfillment rate: 0.7482
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1765, 0.2231]

- Phase-level quality:
  - OPENING: drift=0.2176, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1894, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1990, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### zoom_return_to_office_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2121 (+/- 0.0022)
- Clean persona drift MAE: 0.2121
- Per-trait absolute error: O 0.2580, C 0.2354, E 0.1867, A 0.2125, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1906
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9000
- Clean envelope violations: 2.9000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0685
- Repetition rate: 0.0000
- Topic drift rate: 0.8214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3567
- Commitment fulfillment rate: 0.8375
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2091, 0.2151]

- Phase-level quality:
  - OPENING: drift=0.2160, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2019, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2105, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Mode Summary
### exploratory:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1690 (+/- 0.0149)
- Clean persona drift MAE: 0.1690
- Per-trait absolute error: O 0.1565, C 0.2245, E 0.1276, A 0.1677, N 0.1685
- Relationship inconsistency: 0.0472
- Relationship shift rate: 0.2249
- Relationship overshoot rate: 0.1725
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0356
- Clean envelope violations: 2.0356
- Structured action validity: 0.4422
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.3000
- Action-plan alignment: 0.9681
- Planned action coverage: 0.9087
- Action family convergence: 0.7675
- Role action diversity: 0.4819
- Negotiation uniqueness: 0.2714
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1056
- Repetition rate: 0.0035
- Topic drift rate: 0.4926
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4093
- Commitment fulfillment rate: 0.7175
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1652, 0.1727]

- Phase-level quality:
  - OPENING: drift=0.1749, convergence=0.7644, diversity=0.3667
  - TENSION: drift=0.1749, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1732, convergence=0.6767, diversity=0.4464
  - CLOSING: drift=0.1804, convergence=0.7167, diversity=0.5264

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### exploratory:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1803 (+/- 0.0148)
- Clean persona drift MAE: 0.1803
- Per-trait absolute error: O 0.1808, C 0.2271, E 0.1512, A 0.1742, N 0.1681
- Relationship inconsistency: 0.1272
- Relationship shift rate: 0.2757
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2689
- Clean envelope violations: 2.2689
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0812
- Repetition rate: 0.0000
- Topic drift rate: 0.5141
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3936
- Commitment fulfillment rate: 0.6626
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1765, 0.184]

- Phase-level quality:
  - OPENING: drift=0.1825, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1791, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1824, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1861, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### guided:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1706 (+/- 0.0176)
- Clean persona drift MAE: 0.1706
- Per-trait absolute error: O 0.1675, C 0.2209, E 0.1292, A 0.1628, N 0.1726
- Relationship inconsistency: 0.1128
- Relationship shift rate: 0.2324
- Relationship overshoot rate: 0.2175
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0783
- Clean envelope violations: 2.0783
- Structured action validity: 0.7227
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.1333
- Action-plan alignment: 0.9640
- Planned action coverage: 0.9351
- Action family convergence: 0.7028
- Role action diversity: 0.5065
- Negotiation uniqueness: 0.3002
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1061
- Repetition rate: 0.0000
- Topic drift rate: 0.5418
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4112
- Commitment fulfillment rate: 0.7420
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1662, 0.1751]

- Phase-level quality:
  - OPENING: drift=0.1749, convergence=0.7945, diversity=0.3681
  - TENSION: drift=0.1747, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1714, convergence=0.6867, diversity=0.4722
  - CLOSING: drift=0.1834, convergence=0.5500, diversity=0.6125

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### guided:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1788 (+/- 0.0183)
- Clean persona drift MAE: 0.1788
- Per-trait absolute error: O 0.1846, C 0.2238, E 0.1464, A 0.1683, N 0.1708
- Relationship inconsistency: 0.0631
- Relationship shift rate: 0.2870
- Relationship overshoot rate: 0.2475
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2861
- Clean envelope violations: 2.2861
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0820
- Repetition rate: 0.0000
- Topic drift rate: 0.6118
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4118
- Commitment fulfillment rate: 0.6523
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1741, 0.1834]

- Phase-level quality:
  - OPENING: drift=0.1818, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1794, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1783, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1870, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### unknown:engine_structural
- Runs: 424
- Clean runs: 424
- Contaminated runs: 0
- Persona drift MAE: 0.1681 (+/- 0.0158)
- Clean persona drift MAE: 0.1681
- Per-trait absolute error: O 0.1650, C 0.2211, E 0.1204, A 0.1640, N 0.1700
- Relationship inconsistency: 0.0703
- Relationship shift rate: 0.2180
- Relationship overshoot rate: 0.1900
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0252
- Clean envelope violations: 2.0252
- Structured action validity: 0.5881
- Owner resolution rate: 0.9387
- Executed action contradiction: 0.0000
- State transition coherence: 0.9387
- Action feedback utilization: 0.1392
- Action-plan alignment: 0.9661
- Planned action coverage: 0.9284
- Action family convergence: 0.7294
- Role action diversity: 0.4973
- Negotiation uniqueness: 0.2863
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1066
- Repetition rate: 0.0015
- Topic drift rate: 0.5211
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4076
- Commitment fulfillment rate: 0.7245
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1666, 0.1696]

- Phase-level quality:
  - OPENING: drift=0.1708, convergence=0.7605, diversity=0.3642
  - TENSION: drift=0.1731, convergence=0.7297, diversity=0.4473
  - NEGOTIATION: drift=0.1707, convergence=0.6915, diversity=0.4449
  - CLOSING: drift=0.1786, convergence=0.5849, diversity=0.5934

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### unknown:naive
- Runs: 416
- Clean runs: 416
- Contaminated runs: 0
- Persona drift MAE: 0.1770 (+/- 0.0162)
- Clean persona drift MAE: 0.1770
- Per-trait absolute error: O 0.1827, C 0.2229, E 0.1427, A 0.1686, N 0.1682
- Relationship inconsistency: 0.0897
- Relationship shift rate: 0.2721
- Relationship overshoot rate: 0.2445
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2480
- Clean envelope violations: 2.2480
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0823
- Repetition rate: 0.0000
- Topic drift rate: 0.5627
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4018
- Commitment fulfillment rate: 0.6431
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1755, 0.1786]

- Phase-level quality:
  - OPENING: drift=0.1783, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1777, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1785, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1832, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Family Summary
### algorithmic_accountability:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1761 (+/- 0.0082)
- Clean persona drift MAE: 0.1761
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.0970, A 0.2333, N 0.1266
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2725
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0792
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3005
- Commitment fulfillment rate: 0.7445
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1647, 0.1875]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1832, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1814, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### algorithmic_accountability:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1823 (+/- 0.0118)
- Clean persona drift MAE: 0.1823
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1216, A 0.2333, N 0.1333
- Relationship inconsistency: 0.0180
- Relationship shift rate: 0.2867
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3334
- Clean envelope violations: 2.3334
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0874
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2793
- Commitment fulfillment rate: 0.7291
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1659, 0.1987]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1837, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1858, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1730, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_acquisition:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1724 (+/- 0.0108)
- Clean persona drift MAE: 0.1724
- Per-trait absolute error: O 0.1777, C 0.2223, E 0.1216, A 0.1598, N 0.1810
- Relationship inconsistency: 0.1651
- Relationship shift rate: 0.2908
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2667
- Clean envelope violations: 2.2667
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9742
- Planned action coverage: 1.0000
- Action family convergence: 0.5556
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3614
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1112
- Repetition rate: 0.0000
- Topic drift rate: 0.3950
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4481
- Commitment fulfillment rate: 0.8344
- State trajectory variance: 0.0080
- Mean turns: 15.67
- Persona drift 95% CI: [0.1638, 0.1811]

- Phase-level quality:
  - OPENING: drift=0.1771, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1794, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1707, convergence=0.5889, diversity=0.5556
  - CLOSING: drift=0.1881, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_acquisition:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1787 (+/- 0.0122)
- Clean persona drift MAE: 0.1787
- Per-trait absolute error: O 0.2020, C 0.2198, E 0.1381, A 0.1517, N 0.1821
- Relationship inconsistency: 0.0405
- Relationship shift rate: 0.3112
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0847
- Repetition rate: 0.0000
- Topic drift rate: 0.5595
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4751
- Commitment fulfillment rate: 0.7222
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.169, 0.1885]

- Phase-level quality:
  - OPENING: drift=0.1861, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1770, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1739, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1992, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1711 (+/- 0.0112)
- Clean persona drift MAE: 0.1711
- Per-trait absolute error: O 0.1495, C 0.2293, E 0.1533, A 0.1593, N 0.1642
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1949
- Relationship overshoot rate: 0.0563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1167
- Clean envelope violations: 2.1167
- Structured action validity: 0.5875
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9722
- Planned action coverage: 1.0000
- Action family convergence: 0.7333
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.2841
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1073
- Repetition rate: 0.0104
- Topic drift rate: 0.5057
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4142
- Commitment fulfillment rate: 0.8125
- State trajectory variance: 0.0071
- Mean turns: 16.50
- Persona drift 95% CI: [0.1634, 0.1789]

- Phase-level quality:
  - OPENING: drift=0.1738, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1782, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1768, convergence=0.6750, diversity=0.5000
  - CLOSING: drift=0.1769, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate

### corporate_crisis:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1869 (+/- 0.0159)
- Clean persona drift MAE: 0.1869
- Per-trait absolute error: O 0.1742, C 0.2378, E 0.1787, A 0.1727, N 0.1709
- Relationship inconsistency: 0.1580
- Relationship shift rate: 0.2880
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2875
- Clean envelope violations: 2.2875
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0847
- Repetition rate: 0.0000
- Topic drift rate: 0.4716
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4108
- Commitment fulfillment rate: 0.5994
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1759, 0.1979]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1809, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1839, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1846, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1488 (+/- 0.0064)
- Clean persona drift MAE: 0.1488
- Per-trait absolute error: O 0.1000, C 0.1956, E 0.1663, A 0.1305, N 0.1520
- Relationship inconsistency: 0.1146
- Relationship shift rate: 0.2778
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1187
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4374
- Commitment fulfillment rate: 0.4250
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.14, 0.1577]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1724, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1382, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1635, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1650 (+/- 0.0011)
- Clean persona drift MAE: 0.1650
- Per-trait absolute error: O 0.1640, C 0.1912, E 0.1914, A 0.1385, N 0.1400
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2036
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0864
- Repetition rate: 0.0000
- Topic drift rate: 0.6428
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4373
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1635, 0.1665]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1728, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1578, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1846 (+/- 0.0004)
- Clean persona drift MAE: 0.1846
- Per-trait absolute error: O 0.1830, C 0.2800, E 0.1442, A 0.1588, N 0.1572
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2720
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6250
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1016
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4156
- Commitment fulfillment rate: 0.9737
- State trajectory variance: 0.0001
- Mean turns: 22.00
- Persona drift 95% CI: [0.184, 0.1852]

- Phase-level quality:
  - OPENING: drift=0.1854, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1918, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1926, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1794, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1938 (+/- 0.0011)
- Clean persona drift MAE: 0.1938
- Per-trait absolute error: O 0.2180, C 0.2800, E 0.1537, A 0.1659, N 0.1513
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4088
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8000
- Clean envelope violations: 2.8000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0709
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3979
- Commitment fulfillment rate: 0.9231
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1923, 0.1953]

- Phase-level quality:
  - OPENING: drift=0.1961, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1928, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2033, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1835, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1521 (+/- 0.0010)
- Clean persona drift MAE: 0.1521
- Per-trait absolute error: O 0.1500, C 0.2072, E 0.1217, A 0.1255, N 0.1560
- Relationship inconsistency: 0.1840
- Relationship shift rate: 0.2888
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1237
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4340
- Commitment fulfillment rate: 0.6607
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1507, 0.1535]

- Phase-level quality:
  - OPENING: drift=0.1699, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1380, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1542, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1951, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1588 (+/- 0.0004)
- Clean persona drift MAE: 0.1588
- Per-trait absolute error: O 0.1540, C 0.2154, E 0.1492, A 0.1185, N 0.1570
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4863
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0822
- Repetition rate: 0.0000
- Topic drift rate: 0.7143
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4231
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1584, 0.1593]

- Phase-level quality:
  - OPENING: drift=0.1786, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1402, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1585, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1961, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1765 (+/- 0.0119)
- Clean persona drift MAE: 0.1765
- Per-trait absolute error: O 0.1400, C 0.2300, E 0.1464, A 0.1883, N 0.1779
- Relationship inconsistency: 0.2309
- Relationship shift rate: 0.3453
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9607
- Planned action coverage: 0.7500
- Action family convergence: 0.9166
- Role action diversity: 0.3406
- Negotiation uniqueness: 0.1714
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1031
- Repetition rate: 0.0000
- Topic drift rate: 0.5049
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4072
- Commitment fulfillment rate: 0.7165
- State trajectory variance: 0.0055
- Mean turns: 18.00
- Persona drift 95% CI: [0.1648, 0.1882]

- Phase-level quality:
  - OPENING: drift=0.1900, convergence=1.0000, diversity=0.2708
  - TENSION: drift=0.1749, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1853, convergence=0.8334, diversity=0.3625
  - CLOSING: drift=0.1916, convergence=1.0000, diversity=0.3958

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1870 (+/- 0.0100)
- Clean persona drift MAE: 0.1870
- Per-trait absolute error: O 0.1770, C 0.2388, E 0.1605, A 0.1862, N 0.1724
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.3082
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4750
- Clean envelope violations: 2.4750
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0728
- Repetition rate: 0.0000
- Topic drift rate: 0.6315
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3742
- Commitment fulfillment rate: 0.6661
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1772, 0.1968]

- Phase-level quality:
  - OPENING: drift=0.1881, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1783, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1961, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2006, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1736 (+/- 0.0055)
- Clean persona drift MAE: 0.1736
- Per-trait absolute error: O 0.1133, C 0.3000, E 0.1029, A 0.1517, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2415
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1078
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4723
- Commitment fulfillment rate: 0.5750
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.166, 0.1812]

- Phase-level quality:
  - OPENING: drift=0.1884, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1860, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1837, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1888 (+/- 0.0045)
- Clean persona drift MAE: 0.1888
- Per-trait absolute error: O 0.1700, C 0.3000, E 0.0975, A 0.1767, N 0.2000
- Relationship inconsistency: 0.1465
- Relationship shift rate: 0.4175
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0767
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4191
- Commitment fulfillment rate: 0.7000
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1826, 0.195]

- Phase-level quality:
  - OPENING: drift=0.1943, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1815, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1857, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1922, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1508 (+/- 0.0078)
- Clean persona drift MAE: 0.1508
- Per-trait absolute error: O 0.1744, C 0.2324, E 0.0684, A 0.1379, N 0.1411
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1970
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9333
- Clean envelope violations: 1.9333
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7125
- Role action diversity: 0.4896
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1086
- Repetition rate: 0.0000
- Topic drift rate: 0.4659
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4075
- Commitment fulfillment rate: 0.7008
- State trajectory variance: 0.0056
- Mean turns: 16.50
- Persona drift 95% CI: [0.1432, 0.1585]

- Phase-level quality:
  - OPENING: drift=0.1564, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1675, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1581, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1618, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_contagion:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1711 (+/- 0.0094)
- Clean persona drift MAE: 0.1711
- Per-trait absolute error: O 0.1804, C 0.2703, E 0.1139, A 0.1431, N 0.1476
- Relationship inconsistency: 0.3076
- Relationship shift rate: 0.3495
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2583
- Clean envelope violations: 2.2583
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0922
- Repetition rate: 0.0000
- Topic drift rate: 0.5341
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3912
- Commitment fulfillment rate: 0.6786
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1619, 0.1802]

- Phase-level quality:
  - OPENING: drift=0.1714, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1754, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1716, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1742, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1638 (+/- 0.0019)
- Clean persona drift MAE: 0.1638
- Per-trait absolute error: O 0.1930, C 0.1972, E 0.1034, A 0.1289, N 0.1960
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0857
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5072
- Commitment fulfillment rate: 0.5960
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1612, 0.1663]

- Phase-level quality:
  - OPENING: drift=0.1740, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1626, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1705, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1632, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1711 (+/- 0.0011)
- Clean persona drift MAE: 0.1711
- Per-trait absolute error: O 0.2030, C 0.1928, E 0.1304, A 0.1283, N 0.2011
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3454
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0697
- Repetition rate: 0.0000
- Topic drift rate: 0.7272
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5136
- Commitment fulfillment rate: 0.8435
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1696, 0.1726]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1720, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1749, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1677, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1703 (+/- 0.0042)
- Clean persona drift MAE: 0.1703
- Per-trait absolute error: O 0.1640, C 0.2105, E 0.1331, A 0.1240, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1900
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1310
- Repetition rate: 0.0000
- Topic drift rate: 0.4285
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4111
- Commitment fulfillment rate: 0.6175
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1645, 0.1761]

- Phase-level quality:
  - OPENING: drift=0.1973, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1541, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1734, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2092, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0052)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1409, A 0.1170, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2093
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0854
- Repetition rate: 0.0000
- Topic drift rate: 0.6428
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3630
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1632, 0.1776]

- Phase-level quality:
  - OPENING: drift=0.1895, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1532, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1801, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2085, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_scandal:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1738 (+/- 0.0235)
- Clean persona drift MAE: 0.1738
- Per-trait absolute error: O 0.1920, C 0.2064, E 0.1567, A 0.1600, N 0.1537
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0894
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.3333
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9589
- Planned action coverage: 0.6363
- Action family convergence: 0.7500
- Role action diversity: 0.7153
- Negotiation uniqueness: 0.2702
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0814
- Repetition rate: 0.0000
- Topic drift rate: 0.6575
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4429
- Commitment fulfillment rate: 0.4722
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1508, 0.1968]

- Phase-level quality:
  - OPENING: drift=0.1755, convergence=0.3333, diversity=0.2500
  - TENSION: drift=0.1907, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1772, convergence=0.3333, diversity=0.2500
  - CLOSING: drift=0.1857, convergence=0.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_scandal:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1874 (+/- 0.0217)
- Clean persona drift MAE: 0.1874
- Per-trait absolute error: O 0.2404, C 0.1997, E 0.1921, A 0.1562, N 0.1487
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1879
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0678
- Repetition rate: 0.0000
- Topic drift rate: 0.5990
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4642
- Commitment fulfillment rate: 0.5833
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1662, 0.2087]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1875, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2015, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2109, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### generic:engine_structural
- Runs: 424
- Clean runs: 424
- Contaminated runs: 0
- Persona drift MAE: 0.1681 (+/- 0.0158)
- Clean persona drift MAE: 0.1681
- Per-trait absolute error: O 0.1650, C 0.2211, E 0.1204, A 0.1640, N 0.1700
- Relationship inconsistency: 0.0703
- Relationship shift rate: 0.2180
- Relationship overshoot rate: 0.1900
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0252
- Clean envelope violations: 2.0252
- Structured action validity: 0.5881
- Owner resolution rate: 0.9387
- Executed action contradiction: 0.0000
- State transition coherence: 0.9387
- Action feedback utilization: 0.1392
- Action-plan alignment: 0.9661
- Planned action coverage: 0.9284
- Action family convergence: 0.7294
- Role action diversity: 0.4973
- Negotiation uniqueness: 0.2863
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1066
- Repetition rate: 0.0015
- Topic drift rate: 0.5211
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4076
- Commitment fulfillment rate: 0.7245
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1666, 0.1696]

- Phase-level quality:
  - OPENING: drift=0.1708, convergence=0.7605, diversity=0.3642
  - TENSION: drift=0.1731, convergence=0.7297, diversity=0.4473
  - NEGOTIATION: drift=0.1707, convergence=0.6915, diversity=0.4449
  - CLOSING: drift=0.1786, convergence=0.5849, diversity=0.5934

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### generic:naive
- Runs: 416
- Clean runs: 416
- Contaminated runs: 0
- Persona drift MAE: 0.1770 (+/- 0.0162)
- Clean persona drift MAE: 0.1770
- Per-trait absolute error: O 0.1827, C 0.2229, E 0.1427, A 0.1686, N 0.1682
- Relationship inconsistency: 0.0897
- Relationship shift rate: 0.2721
- Relationship overshoot rate: 0.2445
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2480
- Clean envelope violations: 2.2480
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0823
- Repetition rate: 0.0000
- Topic drift rate: 0.5627
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4018
- Commitment fulfillment rate: 0.6431
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1755, 0.1786]

- Phase-level quality:
  - OPENING: drift=0.1783, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1777, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1785, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1832, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0007)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.1690, C 0.2400, E 0.1399, A 0.2217, N 0.1295
- Relationship inconsistency: 0.1409
- Relationship shift rate: 0.3073
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0926
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3301
- Commitment fulfillment rate: 0.6386
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.179, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1773, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1912, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1685, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0030)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1740, C 0.2400, E 0.1734, A 0.2294, N 0.1283
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.3119
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0634
- Repetition rate: 0.0000
- Topic drift rate: 0.7727
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3140
- Commitment fulfillment rate: 0.3636
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1848, 0.1932]

- Phase-level quality:
  - OPENING: drift=0.1933, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1876, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2006, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### historical_injustice:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0010)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.1333, C 0.3000, E 0.1000, A 0.2383, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.1750
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1032
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3690
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1729, 0.1757]

- Phase-level quality:
  - OPENING: drift=0.1717, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1697, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1690, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1930, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### historical_injustice:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1744 (+/- 0.0057)
- Clean persona drift MAE: 0.1744
- Per-trait absolute error: O 0.1233, C 0.3000, E 0.1000, A 0.2416, N 0.1066
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1950
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0850
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3430
- Commitment fulfillment rate: 0.9166
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1665, 0.1822]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1677, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1764, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1930, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0078)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.1033, C 0.2333, E 0.1680, A 0.1700, N 0.2000
- Relationship inconsistency: 0.1405
- Relationship shift rate: 0.2475
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1061
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3487
- Commitment fulfillment rate: 0.9375
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1642, 0.1857]

- Phase-level quality:
  - OPENING: drift=0.2007, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1844, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1867, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1815, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1993 (+/- 0.0056)
- Clean persona drift MAE: 0.1993
- Per-trait absolute error: O 0.1700, C 0.2333, E 0.2299, A 0.1633, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0731
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3698
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1915, 0.2072]

- Phase-level quality:
  - OPENING: drift=0.2038, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2085, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1980, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1935, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### infrastructure_decision:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1699 (+/- 0.0026)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1420, C 0.2272, E 0.1333, A 0.1150, N 0.2320
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3541
- Negotiation uniqueness: 0.0801
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0902
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3745
- Commitment fulfillment rate: 0.7857
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1663, 0.1735]

- Phase-level quality:
  - OPENING: drift=0.1726, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1931, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1687, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1656, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### infrastructure_decision:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0004)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.1820, C 0.1996, E 0.1444, A 0.1265, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2900
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0801
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3600
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1739, 0.1752]

- Phase-level quality:
  - OPENING: drift=0.1838, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1931, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1748, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1679, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1697 (+/- 0.0045)
- Clean persona drift MAE: 0.1697
- Per-trait absolute error: O 0.2200, C 0.2039, E 0.1051, A 0.1995, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3171
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0923
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3554
- Commitment fulfillment rate: 0.6167
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1635, 0.1759]

- Phase-level quality:
  - OPENING: drift=0.1972, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1555, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1666, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2150, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1790 (+/- 0.0014)
- Clean persona drift MAE: 0.1790
- Per-trait absolute error: O 0.2140, C 0.2039, E 0.1394, A 0.2180, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3819
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0884
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3172
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.177, 0.1811]

- Phase-level quality:
  - OPENING: drift=0.1951, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1695, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1767, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2237, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1883 (+/- 0.0008)
- Clean persona drift MAE: 0.1883
- Per-trait absolute error: O 0.1790, C 0.1733, E 0.2113, A 0.1980, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2300
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.2046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4074
- Commitment fulfillment rate: 0.8572
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1872, 0.1894]

- Phase-level quality:
  - OPENING: drift=0.2007, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1946, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1888, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1876, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1934 (+/- 0.0020)
- Clean persona drift MAE: 0.1934
- Per-trait absolute error: O 0.1990, C 0.1785, E 0.2103, A 0.1990, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2000
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0736
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3948
- Commitment fulfillment rate: 0.5357
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1906, 0.1962]

- Phase-level quality:
  - OPENING: drift=0.1996, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1982, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1910, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1887, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_dispute:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1872 (+/- 0.0031)
- Clean persona drift MAE: 0.1872
- Per-trait absolute error: O 0.1480, C 0.2033, E 0.1512, A 0.2275, N 0.2060
- Relationship inconsistency: 0.4336
- Relationship shift rate: 0.3128
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3438
- Negotiation uniqueness: 0.0774
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0861
- Repetition rate: 0.0000
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4406
- Commitment fulfillment rate: 0.8611
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1829, 0.1915]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1794, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1771, convergence=1.0000, diversity=0.3750
  - CLOSING: drift=0.2307, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_dispute:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1893 (+/- 0.0039)
- Clean persona drift MAE: 0.1893
- Per-trait absolute error: O 0.1880, C 0.2000, E 0.1394, A 0.2160, N 0.2030
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.5316
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0712
- Repetition rate: 0.0000
- Topic drift rate: 0.8214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3874
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1839, 0.1947]

- Phase-level quality:
  - OPENING: drift=0.1977, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1812, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1859, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2206, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_negotiation:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1449 (+/- 0.0002)
- Clean persona drift MAE: 0.1449
- Per-trait absolute error: O 0.1633, C 0.1000, E 0.0943, A 0.1667, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3184
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.3334
- Clean envelope violations: 1.3334
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.4584
- Negotiation uniqueness: 0.1000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1132
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4334
- Commitment fulfillment rate: 0.7143
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1446, 0.1452]

- Phase-level quality:
  - OPENING: drift=0.1543, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1594, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1394, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1589, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_negotiation:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0103)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1467, C 0.1000, E 0.1332, A 0.2233, N 0.2000
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.2908
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1667
- Clean envelope violations: 2.1667
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0873
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4264
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1463, 0.1749]

- Phase-level quality:
  - OPENING: drift=0.1658, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1600, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1512, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1690, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0060)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.2080, C 0.1674, E 0.1241, A 0.1377, N 0.1695
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2405
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0804
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3339
- Commitment fulfillment rate: 0.7663
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.153, 0.1697]

- Phase-level quality:
  - OPENING: drift=0.1453, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1784, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1628, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1709, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1710 (+/- 0.0041)
- Clean persona drift MAE: 0.1710
- Per-trait absolute error: O 0.2080, C 0.1707, E 0.1575, A 0.1560, N 0.1627
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4325
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0798
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2827
- Commitment fulfillment rate: 0.8334
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1653, 0.1767]

- Phase-level quality:
  - OPENING: drift=0.1583, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1906, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1694, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1694, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0029)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1920, C 0.2400, E 0.0872, A 0.1265, N 0.1800
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4238
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1008
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3734
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1611, 0.1692]

- Phase-level quality:
  - OPENING: drift=0.1664, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1446, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1562, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1639 (+/- 0.0094)
- Clean persona drift MAE: 0.1639
- Per-trait absolute error: O 0.1780, C 0.2400, E 0.1095, A 0.1260, N 0.1660
- Relationship inconsistency: 0.2430
- Relationship shift rate: 0.4229
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0992
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2923
- Commitment fulfillment rate: 0.5476
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1509, 0.1769]

- Phase-level quality:
  - OPENING: drift=0.1800, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1537, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1523, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2043, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1585 (+/- 0.0048)
- Clean persona drift MAE: 0.1585
- Per-trait absolute error: O 0.1810, C 0.1795, E 0.1159, A 0.1775, N 0.1387
- Relationship inconsistency: 0.1469
- Relationship shift rate: 0.2924
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0937
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3680
- Commitment fulfillment rate: 0.7350
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1518, 0.1652]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1462, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1709, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1590, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1602 (+/- 0.0011)
- Clean persona drift MAE: 0.1602
- Per-trait absolute error: O 0.1840, C 0.1907, E 0.1170, A 0.1855, N 0.1236
- Relationship inconsistency: 0.2590
- Relationship shift rate: 0.5685
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0601
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3812
- Commitment fulfillment rate: 0.6072
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1587, 0.1616]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1547, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1675, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1550, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_rights:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1895 (+/- 0.0055)
- Clean persona drift MAE: 0.1895
- Per-trait absolute error: O 0.2266, C 0.2333, E 0.0762, A 0.2117, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0850
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.6111
- Negotiation uniqueness: 0.1458
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1046
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.1810
- Commitment fulfillment rate: 0.9375
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1819, 0.1972]

- Phase-level quality:
  - OPENING: drift=0.1916, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1956, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1899, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1667, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_rights:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1904 (+/- 0.0024)
- Clean persona drift MAE: 0.1904
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.0952, A 0.2067, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4875
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0683
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2485
- Commitment fulfillment rate: 0.5834
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1871, 0.1936]

- Phase-level quality:
  - OPENING: drift=0.1935, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1938, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1976, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1776, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_governance:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1868 (+/- 0.0092)
- Clean persona drift MAE: 0.1868
- Per-trait absolute error: O 0.1973, C 0.2166, E 0.1719, A 0.1840, N 0.1640
- Relationship inconsistency: 0.1172
- Relationship shift rate: 0.2677
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1750
- Clean envelope violations: 2.1750
- Structured action validity: 0.6857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9716
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0986
- Repetition rate: 0.0000
- Topic drift rate: 0.5341
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4351
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0028
- Mean turns: 16.50
- Persona drift 95% CI: [0.1778, 0.1958]

- Phase-level quality:
  - OPENING: drift=0.1878, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1996, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1849, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1790, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_governance:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1963 (+/- 0.0084)
- Clean persona drift MAE: 0.1963
- Per-trait absolute error: O 0.2190, C 0.2153, E 0.1887, A 0.1900, N 0.1687
- Relationship inconsistency: 0.0281
- Relationship shift rate: 0.2865
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4833
- Clean envelope violations: 2.4833
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0683
- Repetition rate: 0.0000
- Topic drift rate: 0.6477
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4464
- Commitment fulfillment rate: 0.6393
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1881, 0.2046]

- Phase-level quality:
  - OPENING: drift=0.1938, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2034, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1949, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1800, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1871 (+/- 0.0042)
- Clean persona drift MAE: 0.1871
- Per-trait absolute error: O 0.1440, C 0.2178, E 0.1932, A 0.1685, N 0.2120
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2091
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1126
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4810
- Commitment fulfillment rate: 0.8889
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1813, 0.1929]

- Phase-level quality:
  - OPENING: drift=0.2042, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1940, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1743, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2171 (+/- 0.0061)
- Clean persona drift MAE: 0.2171
- Per-trait absolute error: O 0.2020, C 0.2310, E 0.2460, A 0.1835, N 0.2230
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3237
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Clean envelope violations: 3.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4975
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2086, 0.2256]

- Phase-level quality:
  - OPENING: drift=0.2175, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2056, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2046, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2584, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### policy_failure:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1517 (+/- 0.0068)
- Clean persona drift MAE: 0.1517
- Per-trait absolute error: O 0.1440, C 0.2042, E 0.1085, A 0.2015, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2283
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.1742
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0935
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3586
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1422, 0.1611]

- Phase-level quality:
  - OPENING: drift=0.1436, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1501, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1304, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1984, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### policy_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1619 (+/- 0.0054)
- Clean persona drift MAE: 0.1619
- Per-trait absolute error: O 0.1540, C 0.1998, E 0.1507, A 0.2050, N 0.1000
- Relationship inconsistency: 0.4395
- Relationship shift rate: 0.4718
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0830
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3537
- Commitment fulfillment rate: 0.8286
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1544, 0.1694]

- Phase-level quality:
  - OPENING: drift=0.1582, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1611, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1421, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1920, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_negotiation:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0048)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1589, C 0.1982, E 0.1239, A 0.1474, N 0.1709
- Relationship inconsistency: 0.2045
- Relationship shift rate: 0.2539
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8778
- Clean envelope violations: 1.8778
- Structured action validity: 0.6762
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9593
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5208
- Negotiation uniqueness: 0.3550
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1219
- Repetition rate: 0.0000
- Topic drift rate: 0.4914
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5070
- Commitment fulfillment rate: 0.5387
- State trajectory variance: 0.0071
- Mean turns: 15.67
- Persona drift 95% CI: [0.1561, 0.1637]

- Phase-level quality:
  - OPENING: drift=0.1536, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1617, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1602, convergence=0.7222, diversity=0.4445
  - CLOSING: drift=0.1636, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### policy_negotiation:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1678 (+/- 0.0085)
- Clean persona drift MAE: 0.1678
- Per-trait absolute error: O 0.1720, C 0.2015, E 0.1379, A 0.1573, N 0.1702
- Relationship inconsistency: 0.1546
- Relationship shift rate: 0.3317
- Relationship overshoot rate: 0.3750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9556
- Clean envelope violations: 1.9556
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1008
- Repetition rate: 0.0000
- Topic drift rate: 0.4913
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4703
- Commitment fulfillment rate: 0.6548
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.161, 0.1745]

- Phase-level quality:
  - OPENING: drift=0.1578, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1620, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1717, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1755, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### post-disaster_recovery:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0092)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1361, C 0.2323, E 0.1192, A 0.1422, N 0.1999
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1871
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2916
- Clean envelope violations: 2.2916
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9739
- Planned action coverage: 1.0000
- Action family convergence: 0.6083
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3409
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1114
- Repetition rate: 0.0312
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4178
- Commitment fulfillment rate: 0.8705
- State trajectory variance: 0.0036
- Mean turns: 16.50
- Persona drift 95% CI: [0.157, 0.1749]

- Phase-level quality:
  - OPENING: drift=0.1550, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1785, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1731, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1865, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate

### post-disaster_recovery:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0058)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.1704, C 0.2351, E 0.1250, A 0.1478, N 0.1941
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1893
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2333
- Clean envelope violations: 2.2333
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0713
- Repetition rate: 0.0000
- Topic drift rate: 0.5113
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3824
- Commitment fulfillment rate: 0.5756
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1689, 0.1801]

- Phase-level quality:
  - OPENING: drift=0.1709, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1896, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1723, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1858, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_crisis:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0066)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1540, C 0.2400, E 0.1006, A 0.1570, N 0.1750
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.2343
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.1483
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1454
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4313
- Commitment fulfillment rate: 0.8750
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1563, 0.1744]

- Phase-level quality:
  - OPENING: drift=0.1592, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1705, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1830, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1614, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### public_health_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1834 (+/- 0.0056)
- Clean persona drift MAE: 0.1834
- Per-trait absolute error: O 0.1540, C 0.2576, E 0.1419, A 0.1805, N 0.1830
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.1487
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0932
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3931
- Commitment fulfillment rate: 0.6000
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1756, 0.1912]

- Phase-level quality:
  - OPENING: drift=0.1798, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1966, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1675, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_failure:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1865 (+/- 0.0200)
- Clean persona drift MAE: 0.1865
- Per-trait absolute error: O 0.2085, C 0.2067, E 0.1224, A 0.1949, N 0.2000
- Relationship inconsistency: 0.0777
- Relationship shift rate: 0.2735
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4083
- Clean envelope violations: 2.4083
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9739
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1141
- Repetition rate: 0.0000
- Topic drift rate: 0.7614
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4229
- Commitment fulfillment rate: 0.8107
- State trajectory variance: 0.0074
- Mean turns: 16.50
- Persona drift 95% CI: [0.1669, 0.2061]

- Phase-level quality:
  - OPENING: drift=0.1832, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1953, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1887, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1908, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_health_failure:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1958 (+/- 0.0233)
- Clean persona drift MAE: 0.1958
- Per-trait absolute error: O 0.2193, C 0.2120, E 0.1535, A 0.2017, N 0.1928
- Relationship inconsistency: 0.1688
- Relationship shift rate: 0.2177
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6750
- Clean envelope violations: 2.6750
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0799
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3919
- Commitment fulfillment rate: 0.7803
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1731, 0.2186]

- Phase-level quality:
  - OPENING: drift=0.1935, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1961, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1994, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1954, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1973 (+/- 0.0100)
- Clean persona drift MAE: 0.1973
- Per-trait absolute error: O 0.1600, C 0.2667, E 0.1000, A 0.2267, N 0.2334
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6666
- Clean envelope violations: 2.6666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4283
- Commitment fulfillment rate: 0.4667
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1834, 0.2112]

- Phase-level quality:
  - OPENING: drift=0.1910, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1987, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1844, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1996, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1922 (+/- 0.0062)
- Clean persona drift MAE: 0.1922
- Per-trait absolute error: O 0.1933, C 0.2667, E 0.1094, A 0.1983, N 0.1933
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.2860
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0772
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4395
- Commitment fulfillment rate: 0.5834
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1836, 0.2008]

- Phase-level quality:
  - OPENING: drift=0.1886, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1878, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1964, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2066, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1642 (+/- 0.0076)
- Clean persona drift MAE: 0.1642
- Per-trait absolute error: O 0.1156, C 0.2175, E 0.1332, A 0.1630, N 0.1916
- Relationship inconsistency: 0.0710
- Relationship shift rate: 0.2217
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8833
- Clean envelope violations: 1.8833
- Structured action validity: 0.3750
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9667
- Planned action coverage: 1.0000
- Action family convergence: 0.6062
- Role action diversity: 0.5781
- Negotiation uniqueness: 0.4074
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1114
- Repetition rate: 0.0000
- Topic drift rate: 0.5016
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4252
- Commitment fulfillment rate: 0.7229
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1589, 0.1694]

- Phase-level quality:
  - OPENING: drift=0.1725, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1691, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1725, convergence=0.5667, diversity=0.5834
  - CLOSING: drift=0.1570, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1746 (+/- 0.0097)
- Clean persona drift MAE: 0.1746
- Per-trait absolute error: O 0.1491, C 0.2092, E 0.1527, A 0.1726, N 0.1896
- Relationship inconsistency: 0.0413
- Relationship shift rate: 0.2096
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0375
- Clean envelope violations: 2.0375
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0914
- Repetition rate: 0.0000
- Topic drift rate: 0.4659
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4365
- Commitment fulfillment rate: 0.5886
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1679, 0.1814]

- Phase-level quality:
  - OPENING: drift=0.1799, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1791, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1787, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1606, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy_crisis:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1901 (+/- 0.0065)
- Clean persona drift MAE: 0.1901
- Per-trait absolute error: O 0.1535, C 0.2604, E 0.1871, A 0.1829, N 0.1666
- Relationship inconsistency: 0.1688
- Relationship shift rate: 0.2755
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.9000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9544
- Planned action coverage: 0.7046
- Action family convergence: 0.8334
- Role action diversity: 0.4323
- Negotiation uniqueness: 0.2056
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0978
- Repetition rate: 0.0000
- Topic drift rate: 0.6347
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4285
- Commitment fulfillment rate: 0.6736
- State trajectory variance: 0.0044
- Mean turns: 18.00
- Persona drift 95% CI: [0.1837, 0.1965]

- Phase-level quality:
  - OPENING: drift=0.1850, convergence=0.8334, diversity=0.3542
  - TENSION: drift=0.2042, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.1908, convergence=0.8334, diversity=0.3542
  - CLOSING: drift=0.2049, convergence=0.7500, diversity=0.3125

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy_crisis:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1981 (+/- 0.0048)
- Clean persona drift MAE: 0.1981
- Per-trait absolute error: O 0.1715, C 0.2632, E 0.1866, A 0.1799, N 0.1895
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2803
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6250
- Clean envelope violations: 2.6250
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0877
- Repetition rate: 0.0000
- Topic drift rate: 0.6396
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4198
- Commitment fulfillment rate: 0.7118
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1934, 0.2029]

- Phase-level quality:
  - OPENING: drift=0.1920, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2057, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1935, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2079, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_compliance:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1532 (+/- 0.0162)
- Clean persona drift MAE: 0.1532
- Per-trait absolute error: O 0.1893, C 0.1928, E 0.0863, A 0.1349, N 0.1623
- Relationship inconsistency: 0.0518
- Relationship shift rate: 0.2207
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.3833
- Clean envelope violations: 1.3833
- Structured action validity: 0.7750
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9685
- Planned action coverage: 1.0000
- Action family convergence: 0.5209
- Role action diversity: 0.6562
- Negotiation uniqueness: 0.4415
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1147
- Repetition rate: 0.0000
- Topic drift rate: 0.4789
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3271
- Commitment fulfillment rate: 0.8375
- State trajectory variance: 0.0015
- Mean turns: 12.50
- Persona drift 95% CI: [0.1373, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1686, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1603, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1659, convergence=0.5834, diversity=0.5834
  - CLOSING: drift=0.1804, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_compliance:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1662 (+/- 0.0047)
- Clean persona drift MAE: 0.1662
- Per-trait absolute error: O 0.2120, C 0.2084, E 0.1153, A 0.1346, N 0.1607
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2352
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0813
- Repetition rate: 0.0000
- Topic drift rate: 0.4464
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3605
- Commitment fulfillment rate: 0.8393
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1616, 0.1708]

- Phase-level quality:
  - OPENING: drift=0.1797, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1742, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1709, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1729, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_crisis:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1528 (+/- 0.0005)
- Clean persona drift MAE: 0.1528
- Per-trait absolute error: O 0.1560, C 0.2500, E 0.1078, A 0.1444, N 0.1058
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0954
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4412
- Commitment fulfillment rate: 0.6778
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1521, 0.1535]

- Phase-level quality:
  - OPENING: drift=0.1536, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1638, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1512, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1587, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### regulatory_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1585 (+/- 0.0004)
- Clean persona drift MAE: 0.1585
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1238, A 0.1396, N 0.1011
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0860
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3926
- Commitment fulfillment rate: 0.4415
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1579, 0.1591]

- Phase-level quality:
  - OPENING: drift=0.1506, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1678, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1622, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1743, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_decision:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1692 (+/- 0.0080)
- Clean persona drift MAE: 0.1692
- Per-trait absolute error: O 0.1303, C 0.2800, E 0.0806, A 0.1766, N 0.1787
- Relationship inconsistency: 0.0163
- Relationship shift rate: 0.1048
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.6750
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9649
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.2338
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1360
- Repetition rate: 0.0000
- Topic drift rate: 0.3182
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3368
- Commitment fulfillment rate: 0.5881
- State trajectory variance: 0.0044
- Mean turns: 12.50
- Persona drift 95% CI: [0.1614, 0.1771]

- Phase-level quality:
  - OPENING: drift=0.1773, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1590, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1748, convergence=0.8334, diversity=0.4166
  - CLOSING: drift=0.1938, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_decision:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1748 (+/- 0.0059)
- Clean persona drift MAE: 0.1748
- Per-trait absolute error: O 0.1253, C 0.2865, E 0.1014, A 0.1842, N 0.1767
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0988
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0910
- Repetition rate: 0.0000
- Topic drift rate: 0.2922
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3775
- Commitment fulfillment rate: 0.5970
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.169, 0.1806]

- Phase-level quality:
  - OPENING: drift=0.1871, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1644, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1755, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1901, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1563 (+/- 0.0004)
- Clean persona drift MAE: 0.1563
- Per-trait absolute error: O 0.1560, C 0.2019, E 0.1071, A 0.1506, N 0.1663
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2195
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0983
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4092
- Commitment fulfillment rate: 0.7033
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1559, 0.1568]

- Phase-level quality:
  - OPENING: drift=0.1711, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1649, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1561, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1672, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1693 (+/- 0.0021)
- Clean persona drift MAE: 0.1693
- Per-trait absolute error: O 0.1900, C 0.2155, E 0.1204, A 0.1578, N 0.1627
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2978
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0761
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3921
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1664, 0.1721]

- Phase-level quality:
  - OPENING: drift=0.1762, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1767, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1658, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1706, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1501 (+/- 0.0069)
- Clean persona drift MAE: 0.1501
- Per-trait absolute error: O 0.1460, C 0.2236, E 0.1361, A 0.1206, N 0.1241
- Relationship inconsistency: 0.0281
- Relationship shift rate: 0.2187
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8750
- Clean envelope violations: 1.8750
- Structured action validity: 0.7571
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9651
- Planned action coverage: 1.0000
- Action family convergence: 0.5667
- Role action diversity: 0.5521
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0895
- Repetition rate: 0.0000
- Topic drift rate: 0.5114
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4466
- Commitment fulfillment rate: 0.5661
- State trajectory variance: 0.0042
- Mean turns: 18.00
- Persona drift 95% CI: [0.1433, 0.1569]

- Phase-level quality:
  - OPENING: drift=0.1505, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1595, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1550, convergence=0.6333, diversity=0.5000
  - CLOSING: drift=0.1543, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### urban_policy:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1567 (+/- 0.0118)
- Clean persona drift MAE: 0.1567
- Per-trait absolute error: O 0.1520, C 0.2282, E 0.1439, A 0.1355, N 0.1240
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2327
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0786
- Repetition rate: 0.0000
- Topic drift rate: 0.6185
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4729
- Commitment fulfillment rate: 0.3783
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1451, 0.1683]

- Phase-level quality:
  - OPENING: drift=0.1667, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1600, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1580, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1539, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1998 (+/- 0.0168)
- Clean persona drift MAE: 0.1998
- Per-trait absolute error: O 0.2420, C 0.2464, E 0.1785, A 0.1700, N 0.1620
- Relationship inconsistency: 0.2893
- Relationship shift rate: 0.3369
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1185
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4032
- Commitment fulfillment rate: 0.7482
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1765, 0.2231]

- Phase-level quality:
  - OPENING: drift=0.2176, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1894, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1990, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### workplace_policy:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2121 (+/- 0.0022)
- Clean persona drift MAE: 0.2121
- Per-trait absolute error: O 0.2580, C 0.2354, E 0.1867, A 0.2125, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1906
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9000
- Clean envelope violations: 2.9000
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
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0685
- Repetition rate: 0.0000
- Topic drift rate: 0.8214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3567
- Commitment fulfillment rate: 0.8375
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2091, 0.2151]

- Phase-level quality:
  - OPENING: drift=0.2160, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2019, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2105, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Feature Attribution: What Drives Each Trait Score

### Openness (O) — Mean Error: 0.1734

| Feature | engine_structural (n=3272) | naive (n=3248) | Delta |
|---------|------|------|------|
| idea_count | 0.386 | 0.090 | +0.296 |
| hypothetical_count | 0.031 | 0.011 | +0.020 |
| unique_word_ratio | 0.794 | 0.816 | -0.022 |

Calibration: static

### Conscientiousness (C) — Mean Error: 0.2224

| Feature | engine_structural (n=3272) | naive (n=3248) | Delta |
|---------|------|------|------|
| planning_count | 1.086 | 0.657 | +0.429 |
| structure_marker_count | 0.019 | 0.026 | -0.007 |
| detail_count | 0.000 | 0.000 | +0.000 |
| goal_reference_count | 0.000 | 0.000 | +0.000 |
| correction_count | 0.000 | 0.000 | +0.000 |

Calibration: dynamic

### Extraversion (E) — Mean Error: 0.1330

| Feature | engine_structural (n=3272) | naive (n=3248) | Delta |
|---------|------|------|------|
| exclamation_count | 0.000 | 0.000 | +0.000 |
| question_count | 0.000 | 0.000 | +0.000 |
| word_count | 0.000 | 0.000 | +0.000 |
| filler_count | 0.000 | 0.000 | +0.000 |

Calibration: dynamic

### Agreeableness (A) — Mean Error: 0.1667

| Feature | engine_structural (n=3272) | naive (n=3248) | Delta |
|---------|------|------|------|
| acknowledgment_count | 0.069 | 0.183 | -0.114 |
| disagreement_count | 0.085 | 0.056 | +0.028 |
| negation_count | 1.564 | 2.092 | -0.528 |
| politeness_count | 0.000 | 0.000 | +0.000 |
| compliment_count | 0.000 | 0.000 | +0.000 |

Calibration: dynamic

### Neuroticism (N) — Mean Error: 0.1693

| Feature | engine_structural (n=3272) | naive (n=3248) | Delta |
|---------|------|------|------|
| hedge_count | 0.267 | 0.117 | +0.150 |
| self_doubt_count | 0.000 | 0.000 | +0.000 |
| reassurance_seeking_count | 0.000 | 0.002 | -0.002 |
| apology_count | 0.000 | 0.000 | +0.000 |
| emotional_word_count | 0.062 | 0.057 | +0.005 |

Calibration: dynamic


## Decision Driver Analysis

### engine_structural — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 27188 | sycophancy_risk | 27188 |
| TENSION | identity_consistency | 27188 | sycophancy_risk | 27188 |
| NEGOTIATION | identity_consistency | 31600 | sycophancy_risk | 31600 |
| CLOSING | identity_consistency | 16792 | sycophancy_risk | 16792 |


## Per-Archetype Trait Error

| Archetype | n | O | C | E | A | N | MAE | Top Failed Trait |
|-----------|---|---|---|---|---|---|-----|-----------------|
| Academic researcher studying crypto market failures | 24 | 0.295 | 0.206 | 0.080 | 0.081 | 0.211 | 0.175 | O |
| Activision Blizzard game studio creative lead | 20 | 0.320 | 0.133 | 0.144 | 0.036 | 0.208 | 0.168 | O |
| Activision Shareholder | 20 | 0.130 | 0.280 | 0.045 | 0.293 | 0.097 | 0.169 | A |
| Activist investor | 48 | 0.067 | 0.419 | 0.150 | 0.266 | 0.260 | 0.232 | C |
| Ad-Tech Engineer | 84 | 0.123 | 0.189 | 0.107 | 0.172 | 0.055 | 0.129 | C |
| Aerospace insurance underwriter repricing risk for the MAX fleet. | 32 | 0.060 | 0.248 | 0.065 | 0.232 | 0.110 | 0.143 | C |
| Affected mother of three | 28 | 0.145 | 0.025 | 0.167 | 0.308 | 0.102 | 0.149 | A |
| Aging local worker | 24 | 0.280 | 0.091 | 0.233 | 0.010 | 0.111 | 0.145 | O |
| Alameda Research quant who uncovered the balance sheet discrepancy | 24 | 0.420 | 0.256 | 0.188 | 0.036 | 0.100 | 0.200 | O |
| Alameda Research quantitative analyst who discovered balance sheet irregularities | 24 | 0.245 | 0.394 | 0.153 | 0.091 | 0.111 | 0.199 | C |
| Alameda quant analyst | 24 | 0.445 | 0.312 | 0.307 | 0.100 | 0.018 | 0.236 | O |
| All-Hands Moderator | 4 | 0.270 | 0.131 | 0.298 | 0.209 | 0.006 | 0.183 | E |
| Amazon Fitness lead | 16 | 0.270 | 0.300 | 0.061 | 0.099 | 0.205 | 0.187 | C |
| Apple Fitness+ product lead | 32 | 0.258 | 0.292 | 0.062 | 0.094 | 0.244 | 0.190 | C |
| Bahamas Securities Commission supervisor who approved FTX license | 24 | 0.030 | 0.106 | 0.206 | 0.131 | 0.000 | 0.095 | E |
| Bahamas regulatory officer | 24 | 0.230 | 0.095 | 0.242 | 0.169 | 0.083 | 0.163 | E |
| Bahamian financial regulatory officer who approved FTX license | 24 | 0.030 | 0.276 | 0.048 | 0.188 | 0.211 | 0.151 | C |
| Barista-Organizer working two jobs | 12 | 0.345 | 0.092 | 0.067 | 0.036 | 0.108 | 0.130 | O |
| Barista-organizer working two jobs | 12 | 0.320 | 0.101 | 0.063 | 0.040 | 0.185 | 0.142 | O |
| Barista-organizer working two jobs, recently written up for 'tardiness' after union meetings | 12 | 0.245 | 0.105 | 0.117 | 0.057 | 0.093 | 0.123 | O |
| Bootstrapped SaaS Founder | 56 | 0.282 | 0.120 | 0.200 | 0.088 | 0.100 | 0.158 | O |
| Brick-and-mortar bookstore owner (Congestion Zone) | 16 | 0.050 | 0.079 | 0.287 | 0.066 | 0.019 | 0.100 | E |
| CEO of a regional airline with 14 grounded MAX aircraft, facing significant financial losses. | 32 | 0.130 | 0.303 | 0.158 | 0.110 | 0.305 | 0.201 | N |
| CFO | 4 | 0.030 | 0.392 | 0.039 | 0.202 | 0.106 | 0.154 | C |
| CRE Lease Negotiator | 4 | 0.255 | 0.410 | 0.070 | 0.003 | 0.306 | 0.209 | C |
| CRE Lease Strategist | 4 | 0.130 | 0.414 | 0.199 | 0.281 | 0.207 | 0.246 | C |
| Cabin crew safety representative | 32 | 0.145 | 0.217 | 0.032 | 0.291 | 0.106 | 0.158 | A |
| Centrelink call center team lead | 32 | 0.070 | 0.312 | 0.111 | 0.195 | 0.005 | 0.139 | C |
| Centrelink call center worker | 32 | 0.070 | 0.378 | 0.226 | 0.095 | 0.206 | 0.195 | C |
| Centrelink call center worker processing appeals | 32 | 0.070 | 0.182 | 0.092 | 0.076 | 0.000 | 0.084 | C |
| Centrelink middle manager | 32 | 0.030 | 0.372 | 0.087 | 0.205 | 0.200 | 0.179 | C |
| Chair of the pilots' union safety committee, advocating for extensive pilot retraining. | 32 | 0.145 | 0.349 | 0.026 | 0.243 | 0.105 | 0.174 | C |
| City council president | 28 | 0.070 | 0.102 | 0.309 | 0.199 | 0.198 | 0.176 | E |
| City economic development director | 4 | 0.060 | 0.174 | 0.283 | 0.107 | 0.006 | 0.126 | E |
| City official overseeing Prop C implementation | 12 | 0.055 | 0.248 | 0.383 | 0.001 | 0.106 | 0.159 | E |
| City policymaker | 16 | 0.120 | 0.315 | 0.174 | 0.010 | 0.216 | 0.167 | C |
| Clawback-targeted foundation | 24 | 0.170 | 0.130 | 0.044 | 0.384 | 0.245 | 0.195 | A |
| Cloud Infrastructure Architect | 28 | 0.245 | 0.212 | 0.046 | 0.029 | 0.089 | 0.124 | O |
| Cloud Infrastructure Engineer at Microsoft | 40 | 0.128 | 0.365 | 0.049 | 0.161 | 0.299 | 0.200 | C |
| College student (account borrower) | 20 | 0.420 | 0.270 | 0.155 | 0.111 | 0.035 | 0.198 | O |
| Commercial Real Estate Analyst | 12 | 0.170 | 0.329 | 0.016 | 0.192 | 0.014 | 0.144 | C |
| Commercial real estate analyst | 12 | 0.170 | 0.398 | 0.122 | 0.204 | 0.379 | 0.255 | C |
| Committee member who championed $10B investment | 4 | 0.070 | 0.410 | 0.294 | 0.199 | 0.094 | 0.214 | C |
| Community Church Leader organizing relief efforts | 28 | 0.245 | 0.067 | 0.255 | 0.420 | 0.307 | 0.259 | A |
| Community Church Pastor | 28 | 0.145 | 0.053 | 0.250 | 0.397 | 0.105 | 0.190 | A |
| Community Manager (Facing Layoffs) | 4 | 0.245 | 0.116 | 0.126 | 0.387 | 0.085 | 0.192 | A |
| Community church leader | 28 | 0.270 | 0.088 | 0.255 | 0.399 | 0.298 | 0.262 | A |
| Community legal aid lawyer | 32 | 0.270 | 0.269 | 0.051 | 0.398 | 0.094 | 0.216 | A |
| Community organizer | 12 | 0.245 | 0.089 | 0.342 | 0.314 | 0.091 | 0.216 | E |
| Competing streamer's retention strategist | 20 | 0.345 | 0.114 | 0.347 | 0.191 | 0.285 | 0.256 | E |
| Competitor exchange | 24 | 0.070 | 0.412 | 0.299 | 0.322 | 0.183 | 0.257 | C |
| Congestion zone business owner | 16 | 0.060 | 0.317 | 0.075 | 0.093 | 0.035 | 0.116 | C |
| Construction CEO | 12 | 0.030 | 0.207 | 0.383 | 0.306 | 0.021 | 0.189 | E |
| Construction union leader | 36 | 0.088 | 0.218 | 0.280 | 0.173 | 0.171 | 0.186 | E |
| Consumer Privacy Advocate | 28 | 0.420 | 0.079 | 0.203 | 0.289 | 0.311 | 0.261 | O |
| Consumer rights advocate | 32 | 0.145 | 0.027 | 0.032 | 0.294 | 0.209 | 0.142 | A |
| Corporate Communications VP | 12 | 0.030 | 0.201 | 0.312 | 0.009 | 0.186 | 0.148 | E |
| Corporate communications managing public perception | 32 | 0.060 | 0.174 | 0.281 | 0.017 | 0.101 | 0.127 | E |
| Corporate labor relations specialist | 12 | 0.055 | 0.184 | 0.300 | 0.301 | 0.020 | 0.172 | A |
| Corporate real estate director locked into unfavorable lease | 4 | 0.130 | 0.310 | 0.055 | 0.077 | 0.106 | 0.135 | C |
| Creative Director at Activision | 20 | 0.445 | 0.076 | 0.147 | 0.048 | 0.203 | 0.184 | O |
| Creative Director at Activision Blizzard | 20 | 0.345 | 0.077 | 0.037 | 0.208 | 0.210 | 0.175 | O |
| Customer/Disability Advocate | 12 | 0.270 | 0.084 | 0.031 | 0.278 | 0.303 | 0.193 | N |
| DPA Enforcement Officer | 28 | 0.155 | 0.375 | 0.042 | 0.249 | 0.100 | 0.184 | C |
| Data Protection Consultant | 28 | 0.055 | 0.375 | 0.065 | 0.013 | 0.200 | 0.142 | C |
| Data Protection Officer | 56 | 0.117 | 0.339 | 0.044 | 0.132 | 0.284 | 0.183 | C |
| Deaf Software Engineer | 4 | 0.370 | 0.386 | 0.073 | 0.081 | 0.092 | 0.201 | C |
| Deaf software engineer | 4 | 0.320 | 0.358 | 0.150 | 0.122 | 0.106 | 0.211 | C |
| Deaf software engineer at Zoom | 4 | 0.195 | 0.372 | 0.099 | 0.150 | 0.135 | 0.190 | C |
| Debt collection contractor | 32 | 0.130 | 0.020 | 0.234 | 0.299 | 0.094 | 0.156 | A |
| Director of charitable foundation facing FTX donation clawback | 24 | 0.170 | 0.206 | 0.040 | 0.295 | 0.128 | 0.168 | A |
| Disability advocate customer | 12 | 0.245 | 0.010 | 0.109 | 0.393 | 0.304 | 0.212 | A |
| Disability rights advocate | 60 | 0.185 | 0.042 | 0.078 | 0.308 | 0.263 | 0.175 | A |
| Disability rights advocate for mobility-limited gig workers | 30 | 0.143 | 0.071 | 0.096 | 0.299 | 0.029 | 0.128 | A |
| Disabled Transit Riders Alliance Director | 16 | 0.170 | 0.043 | 0.032 | 0.402 | 0.097 | 0.149 | A |
| Disaster Response Vet | 24 | 0.070 | 0.364 | 0.167 | 0.301 | 0.092 | 0.199 | C |
| Disney+ retention strategist | 40 | 0.295 | 0.052 | 0.220 | 0.110 | 0.207 | 0.177 | O |
| EPA regional administrator | 28 | 0.170 | 0.325 | 0.036 | 0.010 | 0.098 | 0.128 | C |
| ER physician | 16 | 0.070 | 0.415 | 0.056 | 0.101 | 0.294 | 0.187 | C |
| ER physician treating 20+ medical emergencies per week from encampments | 14 | 0.059 | 0.445 | 0.090 | 0.106 | 0.299 | 0.200 | C |
| ER physician treating encampment-related emergencies | 12 | 0.070 | 0.448 | 0.059 | 0.091 | 0.294 | 0.192 | C |
| EU Parliament Aide | 28 | 0.120 | 0.299 | 0.060 | 0.195 | 0.200 | 0.175 | C |
| EU Policy Strategist | 28 | 0.170 | 0.361 | 0.021 | 0.042 | 0.103 | 0.139 | C |
| Elderly flat owner | 24 | 0.180 | 0.211 | 0.072 | 0.402 | 0.172 | 0.207 | A |
| Employee Resource Group Lead | 4 | 0.420 | 0.063 | 0.067 | 0.297 | 0.015 | 0.172 | O |
| Employment Lawyer | 4 | 0.130 | 0.419 | 0.032 | 0.009 | 0.206 | 0.159 | C |
| Engineering Director | 4 | 0.060 | 0.228 | 0.221 | 0.097 | 0.217 | 0.165 | C |
| Engineering Manager | 4 | 0.070 | 0.210 | 0.280 | 0.105 | 0.206 | 0.174 | E |
| Enterprise Tenant (Fortune 500 CFO) | 4 | 0.130 | 0.360 | 0.262 | 0.109 | 0.293 | 0.231 | C |
| Enterprise Tenant Representative | 4 | 0.130 | 0.307 | 0.045 | 0.102 | 0.107 | 0.138 | C |
| Environmental Justice Coalition Organizer | 16 | 0.470 | 0.116 | 0.029 | 0.176 | 0.297 | 0.218 | O |
| Esports League Organizer | 40 | 0.030 | 0.345 | 0.333 | 0.187 | 0.104 | 0.200 | C |
| European Union Aviation Safety Agency representative | 32 | 0.220 | 0.326 | 0.073 | 0.103 | 0.195 | 0.183 | C |
| Evacuee | 24 | 0.230 | 0.109 | 0.215 | 0.012 | 0.397 | 0.193 | N |
| Executive facing financial losses from grounded fleet | 32 | 0.130 | 0.253 | 0.197 | 0.086 | 0.023 | 0.138 | C |
| FAA Certification Lead | 32 | 0.080 | 0.349 | 0.048 | 0.181 | 0.020 | 0.135 | C |
| FAA advisory panel member advocating for crash victims | 32 | 0.345 | 0.065 | 0.193 | 0.009 | 0.205 | 0.163 | O |
| FDA Investigator | 8 | 0.120 | 0.437 | 0.022 | 0.200 | 0.297 | 0.215 | C |
| FDIC Field Examiner | 16 | 0.180 | 0.285 | 0.083 | 0.112 | 0.098 | 0.152 | C |
| FDIC Resolution Field Examiner | 8 | 0.130 | 0.323 | 0.063 | 0.291 | 0.005 | 0.163 | C |
| FTC Regulatory Attorney | 20 | 0.070 | 0.428 | 0.105 | 0.190 | 0.208 | 0.200 | C |
| FTC antitrust specialist | 20 | 0.130 | 0.206 | 0.017 | 0.101 | 0.095 | 0.110 | C |
| FTC regulator | 16 | 0.070 | 0.403 | 0.189 | 0.082 | 0.294 | 0.208 | C |
| FTX bankruptcy trustee overseeing asset recovery | 24 | 0.070 | 0.351 | 0.031 | 0.202 | 0.289 | 0.189 | C |
| Facing layoffs after building member relationships | 4 | 0.245 | 0.065 | 0.353 | 0.293 | 0.021 | 0.196 | E |
| Factory foreman | 24 | 0.130 | 0.085 | 0.070 | 0.017 | 0.211 | 0.102 | N |
| Fed Emergency Lending Officer | 8 | 0.130 | 0.312 | 0.060 | 0.191 | 0.197 | 0.178 | C |
| Fertility doctor | 12 | 0.110 | 0.274 | 0.070 | 0.319 | 0.224 | 0.199 | A |
| Fired Organizer (Buffalo original) | 12 | 0.470 | 0.184 | 0.239 | 0.103 | 0.214 | 0.242 | O |
| Fishing Cooperative Leader | 72 | 0.147 | 0.240 | 0.043 | 0.112 | 0.270 | 0.162 | N |
| Former FTX software engineer who built withdrawal systems | 24 | 0.370 | 0.206 | 0.135 | 0.095 | 0.013 | 0.164 | O |
| Former Plant Worker | 24 | 0.055 | 0.061 | 0.172 | 0.009 | 0.203 | 0.100 | N |
| Former executive team member | 4 | 0.170 | 0.190 | 0.394 | 0.017 | 0.194 | 0.193 | E |
| Former sub-postmaster convicted of theft | 8 | 0.155 | 0.291 | 0.104 | 0.211 | 0.400 | 0.232 | N |
| Former sub-postmaster wrongfully convicted | 10 | 0.150 | 0.183 | 0.060 | 0.227 | 0.130 | 0.150 | A |
| Formerly unhoused advocate | 16 | 0.245 | 0.115 | 0.251 | 0.176 | 0.116 | 0.181 | E |
| Formerly unhoused mentor in supportive housing | 12 | 0.150 | 0.039 | 0.164 | 0.300 | 0.106 | 0.152 | A |
| Fujitsu PR director | 8 | 0.055 | 0.085 | 0.315 | 0.212 | 0.200 | 0.173 | E |
| Fujitsu lead developer (2005-2012) | 12 | 0.370 | 0.064 | 0.093 | 0.367 | 0.100 | 0.199 | O |
| Fujitsu lead developer (Horizon team) | 6 | 0.137 | 0.440 | 0.076 | 0.308 | 0.213 | 0.235 | C |
| Game Engine Architect | 20 | 0.420 | 0.116 | 0.055 | 0.216 | 0.192 | 0.200 | O |
| Gaming Journalist | 20 | 0.345 | 0.030 | 0.210 | 0.105 | 0.092 | 0.156 | O |
| Gig platform policy lead | 28 | 0.170 | 0.444 | 0.269 | 0.208 | 0.088 | 0.236 | C |
| Gig worker advocate | 32 | 0.270 | 0.103 | 0.138 | 0.228 | 0.087 | 0.165 | O |
| Government data scientist | 32 | 0.370 | 0.420 | 0.179 | 0.091 | 0.006 | 0.213 | C |
| Government data scientist who flagged algorithm flaws | 32 | 0.370 | 0.423 | 0.072 | 0.223 | 0.100 | 0.237 | C |
| Government engineer overseeing recertification | 32 | 0.055 | 0.377 | 0.026 | 0.089 | 0.195 | 0.148 | C |
| Government labor inspector | 20 | 0.080 | 0.193 | 0.036 | 0.082 | 0.193 | 0.117 | C |
| HDB policymaker | 12 | 0.060 | 0.407 | 0.186 | 0.009 | 0.087 | 0.150 | C |
| HR Diversity Officer | 4 | 0.145 | 0.322 | 0.022 | 0.403 | 0.106 | 0.200 | A |
| Hochul Administration Representative | 16 | 0.230 | 0.021 | 0.347 | 0.042 | 0.203 | 0.169 | E |
| Homeless shelter resident | 16 | 0.085 | 0.097 | 0.080 | 0.210 | 0.106 | 0.116 | A |
| Homeowners association president | 16 | 0.230 | 0.203 | 0.065 | 0.185 | 0.206 | 0.178 | O |
| Hospital EMS coordinator | 16 | 0.055 | 0.393 | 0.090 | 0.196 | 0.091 | 0.165 | C |
| Hospital Procurement Director | 16 | 0.045 | 0.298 | 0.082 | 0.149 | 0.246 | 0.164 | C |
| Hospital procurement director who integrated Theranos devices | 8 | 0.070 | 0.367 | 0.096 | 0.096 | 0.033 | 0.132 | C |
| Immigration rights lawyer | 46 | 0.357 | 0.107 | 0.138 | 0.396 | 0.196 | 0.239 | A |
| Immigration rights lawyer pushing reform | 20 | 0.345 | 0.148 | 0.205 | 0.090 | 0.180 | 0.194 | O |
| In-house counsel managing liability exposure | 4 | 0.230 | 0.410 | 0.159 | 0.107 | 0.206 | 0.222 | C |
| Indie Game Developer | 20 | 0.345 | 0.031 | 0.077 | 0.174 | 0.103 | 0.146 | O |
| Indigenous elder affected by debt notice | 32 | 0.070 | 0.096 | 0.140 | 0.306 | 0.006 | 0.124 | A |
| Institutional investor monitoring Boeing's recovery | 32 | 0.030 | 0.317 | 0.134 | 0.197 | 0.005 | 0.137 | C |
| Insurance Underwriter | 32 | 0.070 | 0.228 | 0.048 | 0.084 | 0.195 | 0.125 | C |
| International Observer | 24 | 0.320 | 0.225 | 0.054 | 0.094 | 0.103 | 0.159 | O |
| Investigative journalist | 8 | 0.470 | 0.023 | 0.180 | 0.106 | 0.100 | 0.176 | O |
| Investigative reporter covering the recertification process | 32 | 0.470 | 0.117 | 0.085 | 0.217 | 0.005 | 0.179 | O |
| Investor who introduced others to FTX yield program | 24 | 0.030 | 0.044 | 0.191 | 0.101 | 0.306 | 0.134 | N |
| Jia Wei's fiancée | 24 | 0.055 | 0.385 | 0.203 | 0.211 | 0.171 | 0.205 | C |
| Journalist covering the FTX collapse for major financial publication | 24 | 0.470 | 0.119 | 0.143 | 0.091 | 0.211 | 0.207 | O |
| Korean Import Regulator | 24 | 0.145 | 0.337 | 0.056 | 0.015 | 0.192 | 0.149 | C |
| Lab technician at Theranos who knows the tests are unreliable | 8 | 0.220 | 0.283 | 0.180 | 0.100 | 0.372 | 0.231 | N |
| Labor advocate for laid-off staff | 4 | 0.370 | 0.018 | 0.368 | 0.215 | 0.106 | 0.215 | O |
| Labor union organizer | 60 | 0.213 | 0.195 | 0.203 | 0.085 | 0.194 | 0.178 | O |
| Labor union organizer advocating for full employment benefits | 30 | 0.370 | 0.403 | 0.182 | 0.017 | 0.269 | 0.248 | C |
| Language school operator | 24 | 0.050 | 0.285 | 0.076 | 0.097 | 0.032 | 0.108 | C |
| Language school operator profiting from training fees | 20 | 0.090 | 0.355 | 0.093 | 0.227 | 0.330 | 0.219 | C |
| Legacy Media CTO | 28 | 0.050 | 0.071 | 0.013 | 0.108 | 0.111 | 0.071 | N |
| Local Journalist Covering Labor | 12 | 0.270 | 0.021 | 0.061 | 0.195 | 0.014 | 0.112 | O |
| Local Mayor | 48 | 0.120 | 0.199 | 0.192 | 0.118 | 0.016 | 0.129 | C |
| Local Municipal Leader | 24 | 0.220 | 0.151 | 0.250 | 0.106 | 0.010 | 0.147 | E |
| Local elected official | 16 | 0.245 | 0.090 | 0.260 | 0.011 | 0.009 | 0.123 | E |
| Local journalist | 52 | 0.447 | 0.130 | 0.144 | 0.152 | 0.149 | 0.204 | O |
| Longtime customer and disability advocate worried about service consistency | 12 | 0.145 | 0.039 | 0.078 | 0.191 | 0.285 | 0.148 | N |
| Lyft driver | 32 | 0.085 | 0.017 | 0.098 | 0.075 | 0.148 | 0.085 | N |
| MP (Select Committee member) | 4 | 0.060 | 0.118 | 0.164 | 0.109 | 0.000 | 0.090 | E |
| MTA Capital Projects Director | 16 | 0.145 | 0.394 | 0.177 | 0.212 | 0.297 | 0.245 | C |
| MTA capital projects manager | 32 | 0.127 | 0.336 | 0.204 | 0.061 | 0.179 | 0.181 | C |
| Media ethics professor | 20 | 0.370 | 0.105 | 0.081 | 0.208 | 0.084 | 0.170 | O |
| Medical Journalist Investigating | 8 | 0.395 | 0.137 | 0.132 | 0.019 | 0.197 | 0.176 | O |
| Medical Researcher | 56 | 0.245 | 0.139 | 0.127 | 0.245 | 0.293 | 0.210 | N |
| Mental health counselor | 32 | 0.170 | 0.159 | 0.049 | 0.403 | 0.211 | 0.199 | A |
| Microsoft Azure gaming infrastructure engineer | 20 | 0.030 | 0.209 | 0.140 | 0.210 | 0.295 | 0.177 | N |
| Microsoft Teams Enterprise Sales Director | 4 | 0.145 | 0.055 | 0.418 | 0.221 | 0.283 | 0.224 | E |
| Microsoft Teams Sales Director | 4 | 0.270 | 0.061 | 0.339 | 0.200 | 0.014 | 0.177 | E |
| Minister for Postal Affairs | 8 | 0.070 | 0.309 | 0.105 | 0.081 | 0.200 | 0.153 | C |
| Ministry of Health official | 24 | 0.080 | 0.173 | 0.017 | 0.120 | 0.112 | 0.100 | C |
| Mt. Sinai ER Transport Coordinator | 16 | 0.030 | 0.309 | 0.085 | 0.211 | 0.097 | 0.146 | C |
| NYPD Traffic Chief | 16 | 0.130 | 0.309 | 0.023 | 0.287 | 0.197 | 0.189 | C |
| Netflix APAC content negotiator | 20 | 0.060 | 0.375 | 0.205 | 0.075 | 0.200 | 0.183 | C |
| Netflix anti-fraud engineer | 40 | 0.120 | 0.317 | 0.065 | 0.016 | 0.236 | 0.151 | C |
| Netflix customer service rep | 20 | 0.180 | 0.157 | 0.058 | 0.399 | 0.044 | 0.168 | A |
| Netflix investor relations | 20 | 0.030 | 0.402 | 0.381 | 0.214 | 0.284 | 0.262 | C |
| Netflix licensing negotiator (APAC) | 20 | 0.170 | 0.393 | 0.183 | 0.101 | 0.201 | 0.209 | C |
| Netflix regional content licensing negotiator | 20 | 0.060 | 0.360 | 0.213 | 0.118 | 0.185 | 0.187 | C |
| Nonprofit director | 16 | 0.420 | 0.191 | 0.246 | 0.279 | 0.299 | 0.287 | O |
| NordVPN product lead | 20 | 0.210 | 0.111 | 0.334 | 0.291 | 0.194 | 0.228 | E |
| NordVPN product manager | 20 | 0.270 | 0.105 | 0.294 | 0.203 | 0.295 | 0.234 | N |
| Nuclear Evacuee | 24 | 0.145 | 0.083 | 0.315 | 0.013 | 0.408 | 0.193 | N |
| Office Experience Lead | 4 | 0.070 | 0.273 | 0.203 | 0.078 | 0.194 | 0.164 | C |
| Outer-borough delivery driver | 32 | 0.155 | 0.192 | 0.042 | 0.114 | 0.088 | 0.118 | C |
| Outer-borough package delivery driver (UPS/FedEx) | 16 | 0.130 | 0.172 | 0.033 | 0.062 | 0.103 | 0.100 | C |
| Password-sharing SaaS founder | 20 | 0.445 | 0.042 | 0.299 | 0.098 | 0.195 | 0.216 | O |
| Patient who received incorrect blood test results | 8 | 0.135 | 0.249 | 0.025 | 0.296 | 0.195 | 0.180 | A |
| Patient with Incorrect Results | 8 | 0.055 | 0.137 | 0.028 | 0.222 | 0.292 | 0.147 | N |
| Patient with Misdiagnosis | 8 | 0.120 | 0.039 | 0.109 | 0.299 | 0.297 | 0.173 | A |
| Payroll Provider Account Manager | 8 | 0.030 | 0.128 | 0.308 | 0.008 | 0.197 | 0.134 | E |
| Pediatrician who identified lead poisoning in children | 28 | 0.370 | 0.401 | 0.103 | 0.216 | 0.198 | 0.258 | C |
| Pediatrician who identified lead poisoning spikes | 28 | 0.370 | 0.375 | 0.074 | 0.210 | 0.193 | 0.244 | C |
| Pediatrician who published research on spiking lead levels in children | 28 | 0.370 | 0.436 | 0.062 | 0.160 | 0.193 | 0.244 | C |
| Peloton CFO | 16 | 0.170 | 0.403 | 0.020 | 0.202 | 0.106 | 0.180 | C |
| Peloton community moderator | 16 | 0.070 | 0.079 | 0.227 | 0.196 | 0.006 | 0.115 | E |
| Peloton fitness instructor | 32 | 0.258 | 0.050 | 0.356 | 0.163 | 0.153 | 0.196 | E |
| Peloton hardware engineer | 16 | 0.370 | 0.191 | 0.051 | 0.007 | 0.116 | 0.147 | O |
| Peloton head instructor | 16 | 0.220 | 0.127 | 0.328 | 0.021 | 0.222 | 0.184 | E |
| Peloton warehouse manager | 16 | 0.030 | 0.130 | 0.020 | 0.010 | 0.186 | 0.075 | N |
| Physician Who Ordered Tests | 8 | 0.060 | 0.200 | 0.092 | 0.277 | 0.097 | 0.145 | A |
| Pilots' Union Safety Chair | 32 | 0.170 | 0.411 | 0.021 | 0.182 | 0.095 | 0.176 | C |
| Player Community Moderator | 20 | 0.195 | 0.104 | 0.304 | 0.357 | 0.303 | 0.253 | A |
| Post Office audit director | 12 | 0.238 | 0.414 | 0.160 | 0.206 | 0.233 | 0.251 | C |
| Post Office internal auditor | 6 | 0.090 | 0.305 | 0.174 | 0.101 | 0.010 | 0.136 | C |
| Post Office prosecuting lawyer | 8 | 0.130 | 0.197 | 0.197 | 0.306 | 0.000 | 0.166 | A |
| Professional gaming league organizer | 20 | 0.060 | 0.405 | 0.216 | 0.199 | 0.105 | 0.197 | C |
| Property agent | 12 | 0.220 | 0.043 | 0.363 | 0.206 | 0.023 | 0.171 | E |
| Property owner facing tenant default | 4 | 0.055 | 0.235 | 0.043 | 0.279 | 0.006 | 0.124 | A |
| Public Health Researcher | 24 | 0.345 | 0.151 | 0.174 | 0.190 | 0.105 | 0.193 | O |
| Regional Airline CEO | 32 | 0.155 | 0.235 | 0.176 | 0.091 | 0.295 | 0.191 | N |
| Regional HR Director | 12 | 0.030 | 0.192 | 0.033 | 0.306 | 0.114 | 0.135 | A |
| Remote Work Advocate | 4 | 0.445 | 0.222 | 0.056 | 0.292 | 0.294 | 0.262 | O |
| Renewables Lobbyist | 24 | 0.220 | 0.035 | 0.261 | 0.204 | 0.314 | 0.207 | N |
| Reporter investigating governance failures | 4 | 0.470 | 0.098 | 0.115 | 0.224 | 0.106 | 0.203 | O |
| Retail crypto trader who lost life savings in FTX yield program | 24 | 0.155 | 0.116 | 0.094 | 0.020 | 0.306 | 0.138 | N |
| Retail crypto trader who lost life savings in FTX's yield program | 24 | 0.220 | 0.162 | 0.097 | 0.140 | 0.300 | 0.184 | N |
| Retail crypto trader with locked savings | 24 | 0.130 | 0.212 | 0.033 | 0.094 | 0.318 | 0.157 | N |
| Risk analyst adjusting premiums for MAX operations | 32 | 0.070 | 0.253 | 0.090 | 0.192 | 0.099 | 0.141 | C |
| Rural council member | 8 | 0.070 | 0.079 | 0.248 | 0.108 | 0.200 | 0.141 | E |
| Rural factory owner | 46 | 0.230 | 0.404 | 0.093 | 0.192 | 0.090 | 0.202 | C |
| Rural factory owner dependent on program labor | 20 | 0.230 | 0.269 | 0.051 | 0.193 | 0.080 | 0.165 | C |
| SFPD liaison | 16 | 0.130 | 0.278 | 0.131 | 0.093 | 0.006 | 0.128 | C |
| SVB Board Member | 8 | 0.145 | 0.203 | 0.265 | 0.302 | 0.003 | 0.184 | A |
| SVB Commercial Banker | 16 | 0.070 | 0.390 | 0.065 | 0.098 | 0.248 | 0.174 | C |
| SVB Senior Commercial Banker | 8 | 0.030 | 0.345 | 0.024 | 0.068 | 0.195 | 0.132 | C |
| SVB Treasury Manager | 8 | 0.030 | 0.191 | 0.104 | 0.013 | 0.081 | 0.084 | C |
| SVB Treasury Risk Officer | 8 | 0.030 | 0.208 | 0.106 | 0.012 | 0.100 | 0.091 | C |
| SaaS Founder (Bootstrapped) | 28 | 0.295 | 0.112 | 0.174 | 0.069 | 0.200 | 0.170 | O |
| Safety advocate pushing for rigorous retraining | 32 | 0.145 | 0.402 | 0.047 | 0.219 | 0.101 | 0.183 | C |
| Seed-stage biotech CEO with 85 employees | 8 | 0.370 | 0.168 | 0.069 | 0.076 | 0.190 | 0.175 | O |
| Senior Centrelink manager overseeing the scheme | 32 | 0.030 | 0.323 | 0.174 | 0.310 | 0.000 | 0.167 | C |
| Senior Lab Technician at Theranos | 8 | 0.320 | 0.409 | 0.205 | 0.201 | 0.104 | 0.248 | C |
| Shift Supervisor (undecided) | 12 | 0.040 | 0.080 | 0.017 | 0.194 | 0.086 | 0.084 | A |
| Shrine Keeper | 24 | 0.230 | 0.285 | 0.156 | 0.394 | 0.103 | 0.233 | A |
| Single parent issued an incorrect $12K debt notice | 32 | 0.130 | 0.023 | 0.169 | 0.112 | 0.200 | 0.127 | N |
| Single parent sharing Netflix account with ex-spouse | 20 | 0.130 | 0.230 | 0.093 | 0.287 | 0.094 | 0.167 | A |
| Single parent sharing Netflix account with ex-spouse for children's access | 20 | 0.130 | 0.226 | 0.040 | 0.309 | 0.070 | 0.155 | A |
| Single parent sharing account with ex-spouse | 20 | 0.130 | 0.178 | 0.051 | 0.322 | 0.105 | 0.157 | A |
| Single parent with $12K incorrect debt notice | 32 | 0.130 | 0.133 | 0.102 | 0.226 | 0.294 | 0.177 | N |
| Single parent wrongly issued $12K debt notice | 32 | 0.130 | 0.227 | 0.112 | 0.144 | 0.290 | 0.181 | N |
| Single-mom DoorDash driver | 60 | 0.073 | 0.153 | 0.029 | 0.180 | 0.202 | 0.128 | N |
| Single-mom DoorDash driver needing schedule flexibility for childcare | 30 | 0.153 | 0.126 | 0.025 | 0.086 | 0.201 | 0.118 | N |
| Small Business Owner Subletter | 4 | 0.270 | 0.079 | 0.187 | 0.016 | 0.007 | 0.112 | O |
| Small business owner (congestion zone) | 16 | 0.090 | 0.144 | 0.279 | 0.151 | 0.365 | 0.206 | N |
| Small business owner (convenience store) facing 60% foot traffic decline | 12 | 0.155 | 0.266 | 0.021 | 0.091 | 0.200 | 0.146 | C |
| Small business owner (retail) | 16 | 0.155 | 0.154 | 0.075 | 0.082 | 0.006 | 0.094 | O |
| Small business owner whose storefront foot traffic dropped 60% due to nearby encampments | 14 | 0.130 | 0.166 | 0.048 | 0.080 | 0.108 | 0.106 | C |
| Small game studio founder | 20 | 0.445 | 0.047 | 0.058 | 0.106 | 0.193 | 0.170 | O |
| Small restaurant owner | 60 | 0.071 | 0.288 | 0.119 | 0.061 | 0.073 | 0.122 | C |
| Social Services Minister | 32 | 0.030 | 0.220 | 0.404 | 0.197 | 0.083 | 0.187 | E |
| Social worker at community legal center | 32 | 0.370 | 0.161 | 0.105 | 0.361 | 0.095 | 0.218 | O |
| Social worker counseling affected clients | 32 | 0.145 | 0.058 | 0.141 | 0.296 | 0.200 | 0.168 | A |
| SoftBank Investment Committee Member | 8 | 0.070 | 0.302 | 0.114 | 0.175 | 0.300 | 0.192 | C |
| South Korean recruiter | 24 | 0.145 | 0.022 | 0.369 | 0.224 | 0.089 | 0.170 | E |
| Startup CEO with frozen payroll | 8 | 0.370 | 0.197 | 0.102 | 0.114 | 0.203 | 0.197 | O |
| Startup CEO with frozen payroll funds | 8 | 0.370 | 0.094 | 0.183 | 0.100 | 0.200 | 0.189 | O |
| Startup CFO | 8 | 0.060 | 0.379 | 0.078 | 0.105 | 0.303 | 0.185 | C |
| State Budget Analyst | 28 | 0.030 | 0.271 | 0.053 | 0.090 | 0.195 | 0.128 | C |
| State Health Department Official | 28 | 0.155 | 0.326 | 0.054 | 0.033 | 0.307 | 0.175 | C |
| State budget analyst | 28 | 0.130 | 0.176 | 0.059 | 0.117 | 0.102 | 0.117 | C |
| State governor | 28 | 0.030 | 0.025 | 0.207 | 0.215 | 0.202 | 0.136 | A |
| State health director | 28 | 0.270 | 0.225 | 0.105 | 0.021 | 0.291 | 0.182 | N |
| State legislator | 32 | 0.050 | 0.327 | 0.217 | 0.019 | 0.187 | 0.160 | C |
| Store Manager (10-year veteran) | 12 | 0.070 | 0.392 | 0.155 | 0.203 | 0.186 | 0.201 | C |
| Store manager torn between corporate and staff | 12 | 0.050 | 0.315 | 0.132 | 0.171 | 0.135 | 0.161 | C |
| Store manager torn between corporate anti-union directives and loyalty to staff | 12 | 0.075 | 0.156 | 0.147 | 0.336 | 0.223 | 0.187 | A |
| Street outreach worker | 16 | 0.295 | 0.032 | 0.184 | 0.399 | 0.205 | 0.223 | A |
| Street outreach worker with deep client trust relationships | 12 | 0.135 | 0.076 | 0.250 | 0.400 | 0.206 | 0.213 | A |
| Street outreach worker with years of trust relationships among unhoused clients | 14 | 0.177 | 0.042 | 0.142 | 0.373 | 0.209 | 0.189 | A |
| Sublessor dependent on WeWork infrastructure | 4 | 0.295 | 0.114 | 0.059 | 0.029 | 0.206 | 0.141 | O |
| TEPCO Safety Engineer | 72 | 0.067 | 0.397 | 0.024 | 0.190 | 0.293 | 0.194 | C |
| Taiwanese factory line supervisor | 48 | 0.130 | 0.217 | 0.054 | 0.100 | 0.069 | 0.114 | C |
| Teams Talent Scout | 4 | 0.270 | 0.114 | 0.353 | 0.200 | 0.292 | 0.246 | E |
| Teamsters Local 814 Secretary-Treasurer | 16 | 0.060 | 0.084 | 0.187 | 0.286 | 0.103 | 0.144 | A |
| Tech Journalist | 8 | 0.470 | 0.085 | 0.067 | 0.298 | 0.012 | 0.186 | O |
| Tech executive | 16 | 0.030 | 0.415 | 0.062 | 0.196 | 0.294 | 0.199 | C |
| Tech industry lobbyist | 32 | 0.105 | 0.215 | 0.301 | 0.206 | 0.276 | 0.221 | E |
| Tech journalist investigating Robodebt | 32 | 0.445 | 0.333 | 0.093 | 0.036 | 0.094 | 0.200 | O |
| Theranos Board Member | 8 | 0.030 | 0.157 | 0.331 | 0.192 | 0.003 | 0.143 | E |
| Theranos Lab Technician | 8 | 0.245 | 0.251 | 0.135 | 0.105 | 0.010 | 0.149 | C |
| Theranos Legal Counsel | 16 | 0.180 | 0.198 | 0.154 | 0.254 | 0.154 | 0.188 | A |
| Theranos Quality Assurance Lead | 8 | 0.320 | 0.400 | 0.047 | 0.100 | 0.208 | 0.215 | C |
| Third-Party Union Buster Consultant | 12 | 0.130 | 0.277 | 0.233 | 0.300 | 0.086 | 0.205 | A |
| Trapped elderly owner | 12 | 0.230 | 0.149 | 0.139 | 0.169 | 0.235 | 0.185 | N |
| URA urban planner | 12 | 0.295 | 0.449 | 0.076 | 0.019 | 0.375 | 0.243 | C |
| US Congressional representative investigating crypto regulation | 24 | 0.145 | 0.031 | 0.254 | 0.121 | 0.200 | 0.150 | E |
| Uber executive | 32 | 0.040 | 0.403 | 0.297 | 0.117 | 0.276 | 0.227 | C |
| Uber/Lyft Driver Association Leader | 16 | 0.195 | 0.191 | 0.221 | 0.019 | 0.197 | 0.165 | E |
| Union rep for postal workers | 8 | 0.145 | 0.103 | 0.316 | 0.012 | 0.300 | 0.175 | E |
| Urban planner | 12 | 0.320 | 0.383 | 0.093 | 0.120 | 0.279 | 0.239 | C |
| VC General Partner | 16 | 0.245 | 0.059 | 0.209 | 0.200 | 0.348 | 0.212 | N |
| VC Investor (Tech Portfolio) | 28 | 0.170 | 0.068 | 0.235 | 0.208 | 0.089 | 0.154 | E |
| Victim Family Representative | 32 | 0.245 | 0.109 | 0.201 | 0.291 | 0.305 | 0.230 | N |
| Victim's daughter | 8 | 0.245 | 0.191 | 0.353 | 0.305 | 0.000 | 0.219 | E |
| Vietnamese Embassy liaison | 24 | 0.245 | 0.267 | 0.120 | 0.201 | 0.312 | 0.229 | N |
| Vietnamese technical intern (former) | 22 | 0.130 | 0.225 | 0.028 | 0.039 | 0.282 | 0.141 | N |
| Vietnamese technical intern with wage theft experience | 20 | 0.180 | 0.234 | 0.106 | 0.039 | 0.083 | 0.128 | C |
| Vietnamese trainee (wage theft victim) | 24 | 0.130 | 0.206 | 0.043 | 0.106 | 0.305 | 0.158 | N |
| Village council chair | 4 | 0.170 | 0.204 | 0.195 | 0.400 | 0.200 | 0.234 | A |
| Walgreens Partnership Manager | 16 | 0.112 | 0.244 | 0.340 | 0.060 | 0.146 | 0.181 | E |
| Warehouse logistics manager | 16 | 0.030 | 0.151 | 0.074 | 0.093 | 0.094 | 0.088 | C |
| Water Treatment Plant Operator | 28 | 0.070 | 0.220 | 0.175 | 0.113 | 0.095 | 0.135 | C |
| Water Treatment Plant Supervisor | 28 | 0.070 | 0.208 | 0.107 | 0.080 | 0.200 | 0.133 | C |
| Water treatment plant supervisor | 28 | 0.070 | 0.224 | 0.048 | 0.091 | 0.002 | 0.087 | C |
| WeWork Community Manager | 4 | 0.135 | 0.015 | 0.325 | 0.289 | 0.130 | 0.179 | E |
| WeWork Interim Legal Counsel | 4 | 0.055 | 0.179 | 0.197 | 0.095 | 0.193 | 0.144 | E |
| Xbox Platform Strategist | 20 | 0.100 | 0.204 | 0.245 | 0.104 | 0.019 | 0.134 | E |
| Young couple awaiting BTO flat | 12 | 0.195 | 0.313 | 0.056 | 0.120 | 0.335 | 0.204 | N |
| Young professional awaiting BTO flat | 12 | 0.245 | 0.215 | 0.053 | 0.098 | 0.088 | 0.140 | O |
| Young professional waiting for BTO | 12 | 0.135 | 0.258 | 0.137 | 0.020 | 0.204 | 0.151 | C |
| Zoom Engineering Manager | 4 | 0.070 | 0.273 | 0.081 | 0.129 | 0.182 | 0.147 | C |

## Phase-Level Behavioral Features (Engine Condition)

| Feature | OPENING | TENSION | NEGOTIATION | CLOSING | Delta (CLOSING - OPENING) |
|---------|------|------|------|------|------|
| acknowledgment_count | 0.023 | 0.023 | 0.035 | 0.015 | -0.008 |
| apology_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| disagreement_count | 0.042 | 0.053 | 0.013 | 0.025 | -0.017 |
| emotional_word_count | 0.038 | 0.014 | 0.013 | 0.022 | -0.016 |
| hedge_count | 0.124 | 0.059 | 0.115 | 0.104 | -0.020 |
| idea_count | 0.116 | 0.107 | 0.229 | 0.102 | -0.013 |
| negation_count | 0.452 | 0.838 | 0.587 | 0.459 | +0.007 |
| reassurance_seeking_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| self_doubt_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| unique_word_ratio | 0.943 | 0.946 | 0.945 | 0.947 | +0.005 |

## Scenario Difficulty vs Drift

| Scenario | Difficulty | Engine Drift | Naive Drift | Delta |
|----------|-----------|-------------|-------------|-------|
| 10actor | 0.76 | 0.1800 | 0.1890 | -0.0090 |
| 3actor | 0.76 | 0.1761 | 0.1823 | -0.0062 |
| 5actor | 0.76 | 0.1517 | 0.1619 | -0.0102 |
| 10actor | 0.59 | 0.1528 | 0.1585 | -0.0057 |
| 3actor | 0.59 | 0.1655 | 0.1797 | -0.0142 |
| 5actor | 0.59 | 0.1729 | 0.1699 | +0.0031 |
| 10actor | 0.76 | 0.1630 | 0.1597 | +0.0033 |
| 3actor | 0.76 | 0.1629 | 0.1670 | -0.0041 |
| 5actor | 0.76 | 0.1537 | 0.1767 | -0.0230 |
| 10actor | 0.76 | 0.1563 | 0.1692 | -0.0129 |
| 3actor | 0.76 | 0.1504 | 0.1659 | -0.0155 |
| 5actor | 0.76 | 0.1559 | 0.1665 | -0.0106 |
| 10actor | 1.00 | 0.1670 | 0.1738 | -0.0067 |
| 3actor | 1.00 | 0.2059 | 0.2180 | -0.0120 |
| 5actor | 1.00 | 0.1653 | 0.1834 | -0.0181 |
| 10actor | 1.00 | 0.1637 | 0.1711 | -0.0073 |
| 3actor | 1.00 | 0.1510 | 0.1679 | -0.0169 |
| 5actor | 1.00 | 0.1965 | 0.2069 | -0.0104 |
| 10actor | 0.68 | 0.1683 | 0.1794 | -0.0111 |
| 3actor | 0.68 | 0.1636 | 0.1695 | -0.0059 |
| 5actor | 0.68 | 0.1699 | 0.1745 | -0.0047 |
| 10actor | 0.59 | 0.1613 | 0.1710 | -0.0097 |
| 3actor | 0.59 | 0.1895 | 0.1904 | -0.0008 |
| 5actor | 0.59 | 0.1651 | 0.1639 | +0.0013 |
| 10actor | 0.57 | 0.1845 | 0.1952 | -0.0107 |
| 3actor | 0.57 | 0.1745 | 0.1710 | +0.0035 |
| 5actor | 0.57 | 0.1583 | 0.1700 | -0.0117 |
| 10actor | 0.68 | 0.1785 | 0.1886 | -0.0101 |
| 3actor | 0.68 | 0.1950 | 0.2040 | -0.0090 |
| 5actor | 0.68 | 0.1871 | 0.2171 | -0.0300 |
| 10actor | 0.82 | 0.1568 | 0.1682 | -0.0114 |
| 3actor | 0.82 | 0.1630 | 0.1619 | +0.0011 |
| 5actor | 0.82 | 0.1435 | 0.1452 | -0.0017 |
| 10actor | 0.91 | 0.1691 | 0.1726 | -0.0035 |
| 3actor | 0.91 | 0.1573 | 0.1828 | -0.0254 |
| 5actor | 0.91 | 0.1521 | 0.1588 | -0.0067 |
| 10actor | 0.91 | 0.1732 | 0.1788 | -0.0055 |
| 3actor | 0.91 | 0.1550 | 0.1783 | -0.0233 |
| 5actor | 0.91 | 0.1654 | 0.1797 | -0.0142 |
| 10actor | 0.48 | 0.1842 | 0.1935 | -0.0093 |
| 3actor | 0.48 | 0.1973 | 0.1922 | +0.0051 |
| 5actor | 0.48 | 0.1960 | 0.2028 | -0.0068 |
| 10actor | 0.82 | 0.1585 | 0.1602 | -0.0017 |
| 3actor | 0.82 | 0.1449 | 0.1606 | -0.0157 |
| 5actor | 0.82 | 0.1872 | 0.1893 | -0.0021 |
| 10actor | 0.59 | 0.1573 | 0.1734 | -0.0160 |
| 3actor | 0.59 | 0.1443 | 0.1688 | -0.0244 |
| 5actor | 0.59 | 0.1703 | 0.1704 | -0.0001 |
| 10actor | 1.00 | 0.1646 | 0.1787 | -0.0141 |
| 3actor | 1.00 | 0.1736 | 0.1888 | -0.0152 |
| 5actor | 1.00 | 0.1885 | 0.1953 | -0.0069 |
| 10actor | 0.85 | 0.1883 | 0.1934 | -0.0051 |
| 3actor | 0.85 | 0.1743 | 0.1744 | -0.0000 |
| 5actor | 0.85 | 0.1697 | 0.1790 | -0.0093 |
| 10actor | 1.00 | 0.1721 | 0.1815 | -0.0094 |
| 3actor | 1.00 | 0.1860 | 0.2106 | -0.0246 |
| 5actor | 1.00 | 0.1488 | 0.1650 | -0.0161 |
| 10actor | 0.66 | 0.1846 | 0.1938 | -0.0092 |
| 3actor | 0.66 | 0.1749 | 0.1993 | -0.0244 |
| 5actor | 0.66 | 0.1998 | 0.2121 | -0.0123 |

## Influence Attribution: Who Drove Key Decisions?

### Decision Points Detected: 3822 across 544 engine runs (mean 7.03/run)

| Decision Type | Count | Mean Influence Concentration |
|---------------|-------|------------------------------|
| trait_drift_spike | 3762 | 0.441 |
| sentiment_flip | 60 | 0.360 |

### Sample Decision Traces

> **actor_2** at turn 12 (): sentiment_flip
> actor_2 sentiment toward actor_1 flipped: challenging → positive
> - actor_4: score=0.310 — 
> - actor_1: score=0.194 — 
> actor_2: actor_2 sentiment toward actor_1 flipped: challenging → positive. actor_4 (score=0.31, key signal: trait pull) actor_1 (score=0.19, key signal: trait pull)

> **actor_2** at turn 12 (): sentiment_flip
> actor_2 sentiment toward actor_4 flipped: challenging → positive
> - actor_4: score=0.310 — 
> - actor_1: score=0.194 — 
> actor_2: actor_2 sentiment toward actor_4 flipped: challenging → positive. actor_4 (score=0.31, key signal: trait pull) actor_1 (score=0.19, key signal: trait pull)

> **actor_2** at turn 12 (): sentiment_flip
> actor_2 sentiment toward actor_5 flipped: challenging → positive
> - actor_4: score=0.310 — 
> - actor_1: score=0.194 — 
> actor_2: actor_2 sentiment toward actor_5 flipped: challenging → positive. actor_4 (score=0.31, key signal: trait pull) actor_1 (score=0.19, key signal: trait pull)


## Statistical Significance: engine_structural vs naive

Bonferroni-corrected threshold: p < 0.0042 (12 comparisons)

| Metric | engine_structural (n=544) | naive (n=536) | Delta | p (Welch) | p (paired) | Cohen's d | Effect | Sig? |
|--------|----|----|----|----|----|----|----|----|
| Persona Drift MAE | 0.1685 | 0.1776 | -0.0091 | 0.0000 | 0.0000 | -0.564 | medium | Yes |
| Relationship Inconsistency | 0.0724 | 0.0909 | -0.0185 | 0.0650 | 0.3904 | -0.112 | negligible | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | 1.0000 | +0.000 | negligible | No |
| Envelope Violations | 2.0322 | 2.2546 | -0.2224 | 0.0000 | 0.0000 | -0.583 | medium | Yes |
| Action Convergence | 0.7307 | 0.0000 | +0.7307 | 0.0000 | 0.0000 | +4.614 | large | Yes |
| Role Diversity | 0.4966 | 0.0000 | +0.4966 | 0.0000 | 0.0000 | +3.993 | large | Yes |
| Dialogue Coherence | 0.1064 | 0.0821 | +0.0243 | 0.0000 | 0.0000 | +1.302 | large | Yes |
| Repetition Rate | 0.0015 | 0.0000 | +0.0015 | 0.0477 | 0.3194 | +0.160 | negligible | No |
| Topic Drift Rate | 0.5202 | 0.5627 | -0.0425 | 0.0016 | 0.0359 | -0.192 | negligible | Yes |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | 1.0000 | +0.000 | negligible | No |
| Semantic Identity Consistency | 0.4082 | 0.4020 | +0.0062 | 0.1482 | 0.3932 | +0.088 | negligible | No |
| Commitment Fulfillment Rate | 0.7257 | 0.6463 | +0.0794 | 0.0000 | 0.0020 | +0.360 | small | Yes |

### Win Rate Summary (per-script comparison)

| Metric | engine_structural wins | Total scripts |
|--------|----|----|
| Persona Drift MAE | 54/60 | 60 |
| Relationship Inconsistency | 22/60 | 60 |
| Commitment Contradiction | 0/60 | 60 |
| Envelope Violations | 45/60 | 60 |
| Action Convergence | 0/60 | 60 |
| Role Diversity | 60/60 | 60 |
| Dialogue Coherence | 58/60 | 60 |
| Repetition Rate | 0/60 | 60 |
| Topic Drift Rate | 32/60 | 60 |
| Fallback Rate | 0/60 | 60 |
| Semantic Identity Consistency | 37/60 | 60 |
| Commitment Fulfillment Rate | 39/60 | 60 |

### Per-Scenario Drift Comparison: engine_structural vs naive

| Scenario | engine_structural drift | naive drift | Delta | Winner |
|----------|----|----|----|----|
| 10actor | 0.1800 | 0.1890 | -0.0090 | engine_structural |
| 3actor | 0.1761 | 0.1823 | -0.0062 | engine_structural |
| 5actor | 0.1517 | 0.1619 | -0.0102 | engine_structural |
| 10actor | 0.1528 | 0.1585 | -0.0057 | engine_structural |
| 3actor | 0.1655 | 0.1797 | -0.0142 | engine_structural |
| 5actor | 0.1729 | 0.1699 | +0.0031 | naive |
| 10actor | 0.1630 | 0.1597 | +0.0033 | naive |
| 3actor | 0.1629 | 0.1670 | -0.0041 | engine_structural |
| 5actor | 0.1537 | 0.1767 | -0.0230 | engine_structural |
| 10actor | 0.1563 | 0.1692 | -0.0129 | engine_structural |
| 3actor | 0.1504 | 0.1659 | -0.0155 | engine_structural |
| 5actor | 0.1559 | 0.1665 | -0.0106 | engine_structural |
| 10actor | 0.1670 | 0.1738 | -0.0067 | engine_structural |
| 3actor | 0.2059 | 0.2180 | -0.0120 | engine_structural |
| 5actor | 0.1653 | 0.1834 | -0.0181 | engine_structural |
| 10actor | 0.1637 | 0.1711 | -0.0073 | engine_structural |
| 3actor | 0.1510 | 0.1679 | -0.0169 | engine_structural |
| 5actor | 0.1965 | 0.2069 | -0.0104 | engine_structural |
| 10actor | 0.1683 | 0.1794 | -0.0111 | engine_structural |
| 3actor | 0.1636 | 0.1695 | -0.0059 | engine_structural |
| 5actor | 0.1699 | 0.1745 | -0.0047 | engine_structural |
| 10actor | 0.1613 | 0.1710 | -0.0097 | engine_structural |
| 3actor | 0.1895 | 0.1904 | -0.0008 | engine_structural |
| 5actor | 0.1651 | 0.1639 | +0.0013 | naive |
| 10actor | 0.1845 | 0.1952 | -0.0107 | engine_structural |
| 3actor | 0.1745 | 0.1710 | +0.0035 | naive |
| 5actor | 0.1583 | 0.1700 | -0.0117 | engine_structural |
| 10actor | 0.1785 | 0.1886 | -0.0101 | engine_structural |
| 3actor | 0.1950 | 0.2040 | -0.0090 | engine_structural |
| 5actor | 0.1871 | 0.2171 | -0.0300 | engine_structural |
| 10actor | 0.1568 | 0.1682 | -0.0114 | engine_structural |
| 3actor | 0.1630 | 0.1619 | +0.0011 | naive |
| 5actor | 0.1435 | 0.1452 | -0.0017 | engine_structural |
| 10actor | 0.1691 | 0.1726 | -0.0035 | engine_structural |
| 3actor | 0.1573 | 0.1828 | -0.0254 | engine_structural |
| 5actor | 0.1521 | 0.1588 | -0.0067 | engine_structural |
| 10actor | 0.1732 | 0.1788 | -0.0055 | engine_structural |
| 3actor | 0.1550 | 0.1783 | -0.0233 | engine_structural |
| 5actor | 0.1654 | 0.1797 | -0.0142 | engine_structural |
| 10actor | 0.1842 | 0.1935 | -0.0093 | engine_structural |
| 3actor | 0.1973 | 0.1922 | +0.0051 | naive |
| 5actor | 0.1960 | 0.2028 | -0.0068 | engine_structural |
| 10actor | 0.1585 | 0.1602 | -0.0017 | engine_structural |
| 3actor | 0.1449 | 0.1606 | -0.0157 | engine_structural |
| 5actor | 0.1872 | 0.1893 | -0.0021 | engine_structural |
| 10actor | 0.1573 | 0.1734 | -0.0160 | engine_structural |
| 3actor | 0.1443 | 0.1688 | -0.0244 | engine_structural |
| 5actor | 0.1703 | 0.1704 | -0.0001 | engine_structural |
| 10actor | 0.1646 | 0.1787 | -0.0141 | engine_structural |
| 3actor | 0.1736 | 0.1888 | -0.0152 | engine_structural |
| 5actor | 0.1885 | 0.1953 | -0.0069 | engine_structural |
| 10actor | 0.1883 | 0.1934 | -0.0051 | engine_structural |
| 3actor | 0.1743 | 0.1744 | -0.0000 | engine_structural |
| 5actor | 0.1697 | 0.1790 | -0.0093 | engine_structural |
| 10actor | 0.1721 | 0.1815 | -0.0094 | engine_structural |
| 3actor | 0.1860 | 0.2106 | -0.0246 | engine_structural |
| 5actor | 0.1488 | 0.1650 | -0.0161 | engine_structural |
| 10actor | 0.1846 | 0.1938 | -0.0092 | engine_structural |
| 3actor | 0.1749 | 0.1993 | -0.0244 | engine_structural |
| 5actor | 0.1998 | 0.2121 | -0.0123 | engine_structural |

## Per-Trait Error: engine_structural vs naive

Bonferroni-corrected threshold: p < 0.010 (5 comparisons)

| Trait | Engine | Naive | Delta | p-value | Cohen's d | Effect | Calibration | Sig? |
|-------|--------|-------|-------|---------|-----------|--------|-------------|------|
| O | 0.1643 | 0.1827 | -0.0184 | 0.0000 | -0.472 | small | Static | Yes |
| C | 0.2215 | 0.2234 | -0.0020 | 0.3793 | -0.054 | negligible | Dynamic | No |
| E | 0.1222 | 0.1440 | -0.0219 | 0.0000 | -0.575 | medium | Dynamic | Yes |
| A | 0.1643 | 0.1692 | -0.0049 | 0.0334 | -0.130 | negligible | Dynamic | No |
| N | 0.1701 | 0.1685 | +0.0016 | 0.4456 | +0.046 | negligible | Dynamic | No |

## Actor Count x Condition Scaling

| Actors | Condition | n | Drift | Envelope | Convergence | Diversity | Coherence | Repetition | Topic Drift |
|--------|-----------|---|-------|----------|-------------|-----------|-----------|------------|-------------|
| 3 | engine_structural | 184 | 0.1704 | 1.9583 | 0.6644 | 0.6291 | 0.1099 | 0.0041 | 0.5109 |
| 3 | naive | 176 | 0.1804 | 2.2083 | 0.0000 | 0.0000 | 0.0866 | 0.0000 | 0.5232 |
| 5 | engine_structural | 176 | 0.1675 | 1.9864 | 0.7121 | 0.5189 | 0.1091 | 0.0000 | 0.5049 |
| 5 | naive | 176 | 0.1773 | 2.2352 | 0.0000 | 0.0000 | 0.0826 | 0.0000 | 0.5459 |
| 10 | engine_structural | 184 | 0.1675 | 2.1500 | 0.8147 | 0.3428 | 0.1004 | 0.0005 | 0.5442 |
| 10 | naive | 184 | 0.1751 | 2.3174 | 0.0000 | 0.0000 | 0.0774 | 0.0000 | 0.6166 |

### Drift Slope (10-actor minus 3-actor):

- engine_structural: -0.0029
- naive: -0.0053
