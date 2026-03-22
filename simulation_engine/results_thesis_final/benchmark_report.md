# Simulation Benchmark Report

## Suite Config
- Total runs: 4080
- Conditions: engine_structural, naive
- Script ids: australia_robodebt_10actor, australia_robodebt_3actor, australia_robodebt_5actor, boeing_737max_return_10actor, boeing_737max_return_3actor, boeing_737max_return_5actor, california_ab5_gig_classification_10actor, california_ab5_gig_classification_3actor, california_ab5_gig_classification_5actor, eu_gdpr_implementation_10actor, eu_gdpr_implementation_3actor, eu_gdpr_implementation_5actor, flint_water_crisis_10actor, flint_water_crisis_3actor, flint_water_crisis_5actor, ftx_collapse_10actor, ftx_collapse_3actor, ftx_collapse_5actor, fukushima_nuclear_restart_10actor, fukushima_nuclear_restart_3actor, fukushima_nuclear_restart_5actor, japan_intern_training_reform_10actor, japan_intern_training_reform_3actor, japan_intern_training_reform_5actor, microsoft_activision_merger_10actor, microsoft_activision_merger_3actor, microsoft_activision_merger_5actor, netflix_password_crackdown_10actor, netflix_password_crackdown_3actor, netflix_password_crackdown_5actor, nyc_congestion_pricing_10actor, nyc_congestion_pricing_3actor, nyc_congestion_pricing_5actor, peloton_demand_cliff_10actor, peloton_demand_cliff_3actor, peloton_demand_cliff_5actor, sf_homelessness_policy_10actor, sf_homelessness_policy_3actor, sf_homelessness_policy_5actor, singapore_hdb_waittime_crisis_10actor, singapore_hdb_waittime_crisis_3actor, singapore_hdb_waittime_crisis_5actor, starbucks_unionization_10actor, starbucks_unionization_3actor, starbucks_unionization_5actor, svb_bank_run_10actor, svb_bank_run_3actor, svb_bank_run_5actor, theranos_whistleblower_10actor, theranos_whistleblower_3actor, theranos_whistleblower_5actor, uk_post_office_horizon_10actor, uk_post_office_horizon_3actor, uk_post_office_horizon_5actor, wework_ipo_collapse_10actor, wework_ipo_collapse_3actor, wework_ipo_collapse_5actor, zoom_return_to_office_10actor, zoom_return_to_office_3actor, zoom_return_to_office_5actor
- Repetitions per condition: 4

## Condition Summary
### engine_structural
- Runs: 2056
- Clean runs: 2056
- Contaminated runs: 0
- Persona drift MAE: 0.1678 (+/- 0.0170)
- Clean persona drift MAE: 0.1678
- Per-trait absolute error: O 0.1650, C 0.2207, E 0.1203, A 0.1628, N 0.1700
- Relationship inconsistency: 0.0951
- Relationship shift rate: 0.2821
- Relationship overshoot rate: 0.2288
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0568
- Clean envelope violations: 2.0568
- Structured action validity: 0.6412
- Owner resolution rate: 0.9358
- Executed action contradiction: 0.0000
- State transition coherence: 0.9358
- Action feedback utilization: 0.2169
- Action-plan alignment: 0.9682
- Planned action coverage: 0.9277
- Action family convergence: 0.7091
- Role action diversity: 0.5103
- Negotiation uniqueness: 0.2798
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1064
- Repetition rate: 0.0024
- Topic drift rate: 0.5205
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4105
- Commitment fulfillment rate: 0.7811
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.167, 0.1685]

- Phase-level quality:
  - OPENING: drift=0.1710, convergence=0.7414, diversity=0.3570
  - TENSION: drift=0.1725, convergence=0.7228, diversity=0.4518
  - NEGOTIATION: drift=0.1711, convergence=0.6180, diversity=0.5033
  - CLOSING: drift=0.1790, convergence=0.5820, diversity=0.5829

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### naive
- Runs: 2024
- Clean runs: 2024
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0176)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.1834, C 0.2243, E 0.1438, A 0.1706, N 0.1681
- Relationship inconsistency: 0.1104
- Relationship shift rate: 0.2801
- Relationship overshoot rate: 0.1846
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2830
- Clean envelope violations: 2.2830
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
- Dialogue coherence: 0.0827
- Repetition rate: 0.0000
- Topic drift rate: 0.5413
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4018
- Commitment fulfillment rate: 0.6750
- State trajectory variance: 0.0000
- Mean turns: 1.86
- Persona drift 95% CI: [0.1773, 0.1788]

- Phase-level quality:
  - OPENING: drift=0.1787, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1789, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1782, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1832, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Script-Level Summary
### australia_robodebt_10actor:engine_structural
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1801 (+/- 0.0046)
- Clean persona drift MAE: 0.1801
- Per-trait absolute error: O 0.1715, C 0.2419, E 0.1363, A 0.2157, N 0.1351
- Relationship inconsistency: 0.0413
- Relationship shift rate: 0.3090
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2250
- Clean envelope violations: 2.2250
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0943
- Repetition rate: 0.0208
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3450
- Commitment fulfillment rate: 0.6429
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.179, 0.1812]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1778, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1936, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1704, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### australia_robodebt_10actor:naive
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1885 (+/- 0.0027)
- Clean persona drift MAE: 0.1885
- Per-trait absolute error: O 0.1740, C 0.2439, E 0.1682, A 0.2273, N 0.1295
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3323
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4250
- Clean envelope violations: 2.4250
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
- Dialogue coherence: 0.0762
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3079
- Commitment fulfillment rate: 0.7460
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1879, 0.1892]

- Phase-level quality:
  - OPENING: drift=0.1957, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1830, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1981, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1714, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:engine_structural
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1849 (+/- 0.0047)
- Clean persona drift MAE: 0.1849
- Per-trait absolute error: O 0.1983, C 0.2333, E 0.1291, A 0.2333, N 0.1300
- Relationship inconsistency: 0.1853
- Relationship shift rate: 0.2299
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1073
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3128
- Commitment fulfillment rate: 0.6792
- State trajectory variance: 0.0000
- Mean turns: 0.69
- Persona drift 95% CI: [0.1837, 0.186]

- Phase-level quality:
  - OPENING: drift=0.1785, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1807, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:naive
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1888 (+/- 0.0052)
- Clean persona drift MAE: 0.1888
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1509, A 0.2333, N 0.1366
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1806
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
- Dialogue coherence: 0.0826
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2623
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 0.69
- Persona drift 95% CI: [0.1876, 0.1901]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1903, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1867, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:engine_structural
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1447 (+/- 0.0055)
- Clean persona drift MAE: 0.1447
- Per-trait absolute error: O 0.1540, C 0.1830, E 0.0882, A 0.1925, N 0.1060
- Relationship inconsistency: 0.3660
- Relationship shift rate: 0.4764
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7500
- Clean envelope violations: 1.7500
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1955
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0976
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3791
- Commitment fulfillment rate: 0.4375
- State trajectory variance: 0.0000
- Mean turns: 0.88
- Persona drift 95% CI: [0.1433, 0.1461]

- Phase-level quality:
  - OPENING: drift=0.1447, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1428, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1300, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1902, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:naive
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0055)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1670, C 0.1932, E 0.1274, A 0.2120, N 0.1000
- Relationship inconsistency: 0.2752
- Relationship shift rate: 0.2298
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
- Dialogue coherence: 0.0776
- Repetition rate: 0.0000
- Topic drift rate: 0.1964
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3485
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 0.88
- Persona drift 95% CI: [0.1586, 0.1613]

- Phase-level quality:
  - OPENING: drift=0.1575, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1484, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1378, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1973, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:engine_structural
- Runs: 64
- Clean runs: 64
- Contaminated runs: 0
- Persona drift MAE: 0.1528 (+/- 0.0020)
- Clean persona drift MAE: 0.1528
- Per-trait absolute error: O 0.1680, C 0.2500, E 0.1034, A 0.1399, N 0.1029
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0633
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0250
- Clean envelope violations: 2.0250
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1190
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4240
- Commitment fulfillment rate: 0.6796
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1524, 0.1533]

- Phase-level quality:
  - OPENING: drift=0.1486, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1643, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1501, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1580, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:naive
- Runs: 62
- Clean runs: 62
- Contaminated runs: 0
- Persona drift MAE: 0.1568 (+/- 0.0012)
- Clean persona drift MAE: 0.1568
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1097, A 0.1467, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2242
- Clean envelope violations: 2.2242
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
- Dialogue coherence: 0.0863
- Repetition rate: 0.0000
- Topic drift rate: 0.4655
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4269
- Commitment fulfillment rate: 0.5202
- State trajectory variance: 0.0000
- Mean turns: 1.42
- Persona drift 95% CI: [0.1566, 0.1571]

- Phase-level quality:
  - OPENING: drift=0.1509, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1634, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1540, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1685, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0077)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1400, C 0.3000, E 0.0764, A 0.1667, N 0.1667
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
- Dialogue coherence: 0.1313
- Repetition rate: 0.0000
- Topic drift rate: 0.1136
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4253
- Commitment fulfillment rate: 0.6741
- State trajectory variance: 0.0000
- Mean turns: 0.73
- Persona drift 95% CI: [0.168, 0.1719]

- Phase-level quality:
  - OPENING: drift=0.1699, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1644, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1728, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1945, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1679 (+/- 0.0073)
- Clean persona drift MAE: 0.1679
- Per-trait absolute error: O 0.1150, C 0.3000, E 0.0891, A 0.1758, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5834
- Clean envelope violations: 1.5834
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
- Dialogue coherence: 0.1163
- Repetition rate: 0.0000
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4229
- Commitment fulfillment rate: 0.7291
- State trajectory variance: 0.0000
- Mean turns: 0.73
- Persona drift 95% CI: [0.1661, 0.1698]

- Phase-level quality:
  - OPENING: drift=0.1719, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1689, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1663, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1934, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### boeing_737max_return_5actor:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1744 (+/- 0.0042)
- Clean persona drift MAE: 0.1744
- Per-trait absolute error: O 0.1520, C 0.2698, E 0.0958, A 0.1723, N 0.1820
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2519
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Dialogue coherence: 0.1181
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3381
- Commitment fulfillment rate: 0.8730
- State trajectory variance: 0.0000
- Mean turns: 0.93
- Persona drift 95% CI: [0.1733, 0.1754]

- Phase-level quality:
  - OPENING: drift=0.1895, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1523, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1861, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1858, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_5actor:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1734 (+/- 0.0115)
- Clean persona drift MAE: 0.1734
- Per-trait absolute error: O 0.1370, C 0.2665, E 0.1118, A 0.1720, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2700
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
- Dialogue coherence: 0.0789
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3222
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 0.93
- Persona drift 95% CI: [0.1706, 0.1763]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1550, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1819, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1903, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_10actor:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1600 (+/- 0.0011)
- Clean persona drift MAE: 0.1600
- Per-trait absolute error: O 0.1125, C 0.1810, E 0.1528, A 0.1536, N 0.2000
- Relationship inconsistency: 0.0445
- Relationship shift rate: 0.3124
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1750
- Clean envelope violations: 2.1750
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1368
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4472
- Commitment fulfillment rate: 0.7415
- State trajectory variance: 0.0000
- Mean turns: 1.47
- Persona drift 95% CI: [0.1597, 0.1603]

- Phase-level quality:
  - OPENING: drift=0.1551, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1675, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1603, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1597, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_10actor:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1617 (+/- 0.0044)
- Clean persona drift MAE: 0.1617
- Per-trait absolute error: O 0.1160, C 0.1797, E 0.1523, A 0.1603, N 0.2000
- Relationship inconsistency: 0.4820
- Relationship shift rate: 0.4277
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
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
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.2841
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4294
- Commitment fulfillment rate: 0.6984
- State trajectory variance: 0.0000
- Mean turns: 1.47
- Persona drift 95% CI: [0.1606, 0.1628]

- Phase-level quality:
  - OPENING: drift=0.1610, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1672, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1598, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1621, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1484 (+/- 0.0076)
- Clean persona drift MAE: 0.1484
- Per-trait absolute error: O 0.1733, C 0.2037, E 0.0650, A 0.1333, N 0.1667
- Relationship inconsistency: 0.2000
- Relationship shift rate: 0.3626
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7500
- Clean envelope violations: 1.7500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1170
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4813
- Commitment fulfillment rate: 0.6801
- State trajectory variance: 0.0000
- Mean turns: 0.73
- Persona drift 95% CI: [0.1465, 0.1503]

- Phase-level quality:
  - OPENING: drift=0.1514, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1599, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1510, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1816, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:naive
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1740 (+/- 0.0052)
- Clean persona drift MAE: 0.1740
- Per-trait absolute error: O 0.1983, C 0.2092, E 0.1182, A 0.1608, N 0.1833
- Relationship inconsistency: 0.1744
- Relationship shift rate: 0.4724
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4166
- Clean envelope violations: 2.4166
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
- Dialogue coherence: 0.1135
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4956
- Commitment fulfillment rate: 0.5750
- State trajectory variance: 0.0000
- Mean turns: 0.79
- Persona drift 95% CI: [0.1726, 0.1753]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1667, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1745, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1833, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:engine_structural
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1489 (+/- 0.0071)
- Clean persona drift MAE: 0.1489
- Per-trait absolute error: O 0.1260, C 0.2000, E 0.1245, A 0.1447, N 0.1495
- Relationship inconsistency: 0.3005
- Relationship shift rate: 0.3555
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1119
- Repetition rate: 0.0000
- Topic drift rate: 0.8393
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4545
- Commitment fulfillment rate: 0.7431
- State trajectory variance: 0.0000
- Mean turns: 1.00
- Persona drift 95% CI: [0.1471, 0.1508]

- Phase-level quality:
  - OPENING: drift=0.1407, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1528, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1625, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1537, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:naive
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1619 (+/- 0.0013)
- Clean persona drift MAE: 0.1619
- Per-trait absolute error: O 0.1480, C 0.2184, E 0.1466, A 0.1512, N 0.1452
- Relationship inconsistency: 0.4495
- Relationship shift rate: 0.4055
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
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
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4197
- Commitment fulfillment rate: 0.5658
- State trajectory variance: 0.0000
- Mean turns: 1.00
- Persona drift 95% CI: [0.1615, 0.1623]

- Phase-level quality:
  - OPENING: drift=0.1490, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1565, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1769, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1471, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:engine_structural
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1627 (+/- 0.0060)
- Clean persona drift MAE: 0.1627
- Per-trait absolute error: O 0.1780, C 0.2051, E 0.1136, A 0.1527, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2911
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1156
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3620
- Commitment fulfillment rate: 0.8540
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1611, 0.1643]

- Phase-level quality:
  - OPENING: drift=0.1674, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1663, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1681, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1709, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:naive
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0039)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.1970, C 0.2090, E 0.1378, A 0.1549, N 0.1618
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4164
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0830
- Repetition rate: 0.0000
- Topic drift rate: 0.7614
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4232
- Commitment fulfillment rate: 0.7882
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1711, 0.1731]

- Phase-level quality:
  - OPENING: drift=0.1738, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1757, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1787, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1765, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:engine_structural
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1518 (+/- 0.0069)
- Clean persona drift MAE: 0.1518
- Per-trait absolute error: O 0.1650, C 0.1875, E 0.0884, A 0.1383, N 0.1800
- Relationship inconsistency: 0.1258
- Relationship shift rate: 0.2796
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1076
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3165
- Commitment fulfillment rate: 0.8958
- State trajectory variance: 0.0000
- Mean turns: 0.79
- Persona drift 95% CI: [0.1501, 0.1536]

- Phase-level quality:
  - OPENING: drift=0.1719, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1648, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1616, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1790, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:naive
- Runs: 56
- Clean runs: 56
- Contaminated runs: 0
- Persona drift MAE: 0.1683 (+/- 0.0154)
- Clean persona drift MAE: 0.1683
- Per-trait absolute error: O 0.1900, C 0.2003, E 0.1285, A 0.1525, N 0.1700
- Relationship inconsistency: 0.5300
- Relationship shift rate: 0.4215
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0833
- Clean envelope violations: 2.0833
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
- Dialogue coherence: 0.1019
- Repetition rate: 0.0000
- Topic drift rate: 0.5455
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3386
- Commitment fulfillment rate: 0.5833
- State trajectory variance: 0.0000
- Mean turns: 0.79
- Persona drift 95% CI: [0.1642, 0.1723]

- Phase-level quality:
  - OPENING: drift=0.1809, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1728, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1692, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1907, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### eu_gdpr_implementation_5actor:engine_structural
- Runs: 54
- Clean runs: 54
- Contaminated runs: 0
- Persona drift MAE: 0.1530 (+/- 0.0070)
- Clean persona drift MAE: 0.1530
- Per-trait absolute error: O 0.1816, C 0.2021, E 0.0853, A 0.1394, N 0.1566
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1962
- Relationship overshoot rate: 0.1083
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5519
- Clean envelope violations: 1.5519
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2593
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.3333
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1105
- Repetition rate: 0.0000
- Topic drift rate: 0.2883
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3741
- Commitment fulfillment rate: 0.6889
- State trajectory variance: 0.0000
- Mean turns: 1.04
- Persona drift 95% CI: [0.1511, 0.1549]

- Phase-level quality:
  - OPENING: drift=0.1707, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1560, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1575, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1831, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:naive
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.1671 (+/- 0.0056)
- Clean persona drift MAE: 0.1671
- Per-trait absolute error: O 0.2400, C 0.2016, E 0.0862, A 0.1568, N 0.1510
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2620
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0735
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3780
- Commitment fulfillment rate: 0.3958
- State trajectory variance: 0.0000
- Mean turns: 1.08
- Persona drift 95% CI: [0.1656, 0.1686]

- Phase-level quality:
  - OPENING: drift=0.1787, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1627, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1705, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1714, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:engine_structural
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0039)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1895, C 0.1850, E 0.1169, A 0.1753, N 0.1600
- Relationship inconsistency: 0.2101
- Relationship shift rate: 0.2854
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0750
- Clean envelope violations: 2.0750
- Structured action validity: 0.7500
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
- Dialogue coherence: 0.1081
- Repetition rate: 0.0000
- Topic drift rate: 0.5568
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3930
- Commitment fulfillment rate: 0.7998
- State trajectory variance: 0.0000
- Mean turns: 1.69
- Persona drift 95% CI: [0.1643, 0.1664]

- Phase-level quality:
  - OPENING: drift=0.1608, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1761, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1579, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1775, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:naive
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0018)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1995, C 0.1839, E 0.1346, A 0.1758, N 0.1583
- Relationship inconsistency: 0.0345
- Relationship shift rate: 0.3209
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0935
- Repetition rate: 0.0000
- Topic drift rate: 0.4659
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3622
- Commitment fulfillment rate: 0.7261
- State trajectory variance: 0.0000
- Mean turns: 1.69
- Persona drift 95% CI: [0.1699, 0.1709]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1813, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1603, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1831, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:engine_structural
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.2072 (+/- 0.0088)
- Clean persona drift MAE: 0.2072
- Per-trait absolute error: O 0.2033, C 0.2370, E 0.1282, A 0.2225, N 0.2450
- Relationship inconsistency: 0.1721
- Relationship shift rate: 0.2960
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5833
- Clean envelope violations: 2.5833
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1366
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3855
- Commitment fulfillment rate: 0.8393
- State trajectory variance: 0.0000
- Mean turns: 0.85
- Persona drift 95% CI: [0.2048, 0.2096]

- Phase-level quality:
  - OPENING: drift=0.2095, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2097, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2170, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2075, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:naive
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.2264 (+/- 0.0069)
- Clean persona drift MAE: 0.2264
- Per-trait absolute error: O 0.2367, C 0.2443, E 0.1565, A 0.2591, N 0.2350
- Relationship inconsistency: 0.1032
- Relationship shift rate: 0.2687
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.3333
- Clean envelope violations: 3.3333
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
- Dialogue coherence: 0.0948
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3910
- Commitment fulfillment rate: 0.8646
- State trajectory variance: 0.0000
- Mean turns: 0.85
- Persona drift 95% CI: [0.2245, 0.2283]

- Phase-level quality:
  - OPENING: drift=0.2169, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2303, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2274, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2077, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:engine_structural
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.1648 (+/- 0.0030)
- Clean persona drift MAE: 0.1648
- Per-trait absolute error: O 0.1340, C 0.2422, E 0.1029, A 0.1640, N 0.1810
- Relationship inconsistency: 0.0011
- Relationship shift rate: 0.2240
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3177
- Negotiation uniqueness: 0.1456
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1203
- Repetition rate: 0.0000
- Topic drift rate: 0.1607
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3900
- Commitment fulfillment rate: 0.8403
- State trajectory variance: 0.0000
- Mean turns: 1.08
- Persona drift 95% CI: [0.164, 0.1656]

- Phase-level quality:
  - OPENING: drift=0.1660, convergence=1.0000, diversity=0.2708
  - TENSION: drift=0.1696, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1826, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1500, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:naive
- Runs: 52
- Clean runs: 52
- Contaminated runs: 0
- Persona drift MAE: 0.1804 (+/- 0.0022)
- Clean persona drift MAE: 0.1804
- Per-trait absolute error: O 0.1540, C 0.2433, E 0.1568, A 0.1680, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2775
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
- Dialogue coherence: 0.0872
- Repetition rate: 0.0000
- Topic drift rate: 0.3215
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4092
- Commitment fulfillment rate: 0.3991
- State trajectory variance: 0.0000
- Mean turns: 1.08
- Persona drift 95% CI: [0.1799, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1835, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1948, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1613, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:engine_structural
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.1642 (+/- 0.0029)
- Clean persona drift MAE: 0.1642
- Per-trait absolute error: O 0.2070, C 0.1956, E 0.1043, A 0.1232, N 0.1906
- Relationship inconsistency: 0.0690
- Relationship shift rate: 0.3020
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0824
- Repetition rate: 0.0000
- Topic drift rate: 0.6477
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5108
- Commitment fulfillment rate: 0.9184
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1634, 0.165]

- Phase-level quality:
  - OPENING: drift=0.1734, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1647, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1700, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1600, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:naive
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.1696 (+/- 0.0043)
- Clean persona drift MAE: 0.1696
- Per-trait absolute error: O 0.2045, C 0.1975, E 0.1219, A 0.1294, N 0.1950
- Relationship inconsistency: 0.2755
- Relationship shift rate: 0.3261
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
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
- Dialogue coherence: 0.0700
- Repetition rate: 0.0000
- Topic drift rate: 0.7614
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4888
- Commitment fulfillment rate: 0.9445
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1684, 0.1709]

- Phase-level quality:
  - OPENING: drift=0.1763, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1697, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1811, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1632, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:engine_structural
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.1597 (+/- 0.0110)
- Clean persona drift MAE: 0.1597
- Per-trait absolute error: O 0.2400, C 0.1991, E 0.1259, A 0.1000, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1875
- Relationship overshoot rate: 0.2250
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
- Role action diversity: 0.7639
- Negotiation uniqueness: 0.2042
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0742
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4811
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 0.92
- Persona drift 95% CI: [0.1566, 0.1628]

- Phase-level quality:
  - OPENING: drift=0.1624, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1683, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1666, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1895, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:naive
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.1705 (+/- 0.0082)
- Clean persona drift MAE: 0.1705
- Per-trait absolute error: O 0.2567, C 0.1991, E 0.1569, A 0.1067, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Dialogue coherence: 0.0691
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4809
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 0.92
- Persona drift 95% CI: [0.1682, 0.1728]

- Phase-level quality:
  - OPENING: drift=0.1688, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1751, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1673, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1892, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:engine_structural
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.1935 (+/- 0.0067)
- Clean persona drift MAE: 0.1935
- Per-trait absolute error: O 0.2090, C 0.2123, E 0.1623, A 0.2117, N 0.1725
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3597
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0922
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3830
- Commitment fulfillment rate: 0.8369
- State trajectory variance: 0.0000
- Mean turns: 1.17
- Persona drift 95% CI: [0.1916, 0.1955]

- Phase-level quality:
  - OPENING: drift=0.1819, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2097, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1988, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1835, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:naive
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.2012 (+/- 0.0047)
- Clean persona drift MAE: 0.2012
- Per-trait absolute error: O 0.2290, C 0.2211, E 0.1636, A 0.2320, N 0.1605
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1619
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6500
- Clean envelope violations: 2.6500
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
- Dialogue coherence: 0.0612
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4026
- Commitment fulfillment rate: 0.7292
- State trajectory variance: 0.0000
- Mean turns: 1.17
- Persona drift 95% CI: [0.1999, 0.2025]

- Phase-level quality:
  - OPENING: drift=0.1913, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2165, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1983, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1986, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:engine_structural
- Runs: 48
- Clean runs: 48
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0045)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.1630, C 0.2323, E 0.1316, A 0.1396, N 0.1943
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3262
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0852
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4704
- Commitment fulfillment rate: 0.8454
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1709, 0.1734]

- Phase-level quality:
  - OPENING: drift=0.1583, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1901, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1708, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1901, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:naive
- Runs: 46
- Clean runs: 46
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0027)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.1716, C 0.2324, E 0.1497, A 0.1532, N 0.1929
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1996
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4739
- Clean envelope violations: 2.4739
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
- Dialogue coherence: 0.0669
- Repetition rate: 0.0000
- Topic drift rate: 0.6334
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4117
- Commitment fulfillment rate: 0.7832
- State trajectory variance: 0.0000
- Mean turns: 1.91
- Persona drift 95% CI: [0.1792, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1611, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1978, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1818, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1939, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_3actor:engine_structural
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1572 (+/- 0.0029)
- Clean persona drift MAE: 0.1572
- Per-trait absolute error: O 0.1050, C 0.2333, E 0.0842, A 0.1467, N 0.2167
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2242
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8333
- Clean envelope violations: 1.8333
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3395
- Commitment fulfillment rate: 0.7976
- State trajectory variance: 0.0000
- Mean turns: 1.00
- Persona drift 95% CI: [0.1563, 0.158]

- Phase-level quality:
  - OPENING: drift=0.1580, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1651, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1638, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1845, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_3actor:naive
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1757 (+/- 0.0129)
- Clean persona drift MAE: 0.1757
- Per-trait absolute error: O 0.1650, C 0.2333, E 0.1275, A 0.1492, N 0.2033
- Relationship inconsistency: 0.0011
- Relationship shift rate: 0.2177
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0774
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3438
- Commitment fulfillment rate: 0.7411
- State trajectory variance: 0.0000
- Mean turns: 1.00
- Persona drift 95% CI: [0.1719, 0.1795]

- Phase-level quality:
  - OPENING: drift=0.1698, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1786, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1811, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1942, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:engine_structural
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1758 (+/- 0.0087)
- Clean persona drift MAE: 0.1758
- Per-trait absolute error: O 0.1500, C 0.2192, E 0.1471, A 0.1275, N 0.2350
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2551
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3802
- Negotiation uniqueness: 0.0757
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0956
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3864
- Commitment fulfillment rate: 0.9286
- State trajectory variance: 0.0000
- Mean turns: 1.27
- Persona drift 95% CI: [0.1732, 0.1783]

- Phase-level quality:
  - OPENING: drift=0.1820, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1907, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1733, convergence=1.0000, diversity=0.2708
  - CLOSING: drift=0.1719, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:naive
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0063)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.1900, C 0.2054, E 0.1371, A 0.1148, N 0.2240
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.1590
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0626
- Repetition rate: 0.0000
- Topic drift rate: 0.4465
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3593
- Commitment fulfillment rate: 0.7750
- State trajectory variance: 0.0000
- Mean turns: 1.27
- Persona drift 95% CI: [0.1724, 0.1761]

- Phase-level quality:
  - OPENING: drift=0.1808, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1897, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1794, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1609, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:engine_structural
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1628 (+/- 0.0062)
- Clean persona drift MAE: 0.1628
- Per-trait absolute error: O 0.2070, C 0.1744, E 0.1220, A 0.1426, N 0.1680
- Relationship inconsistency: 0.0688
- Relationship shift rate: 0.3146
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
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
- Dialogue coherence: 0.0826
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3461
- Commitment fulfillment rate: 0.7443
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.161, 0.1647]

- Phase-level quality:
  - OPENING: drift=0.1484, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1844, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1621, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1595, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:naive
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0050)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.2140, C 0.1735, E 0.1684, A 0.1436, N 0.1613
- Relationship inconsistency: 0.1305
- Relationship shift rate: 0.4860
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2250
- Clean envelope violations: 2.2250
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
- Dialogue coherence: 0.0651
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3574
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1707, 0.1736]

- Phase-level quality:
  - OPENING: drift=0.1528, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1919, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1740, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:engine_structural
- Runs: 44
- Clean runs: 44
- Contaminated runs: 0
- Persona drift MAE: 0.1876 (+/- 0.0066)
- Clean persona drift MAE: 0.1876
- Per-trait absolute error: O 0.2350, C 0.2333, E 0.0832, A 0.1900, N 0.1967
- Relationship inconsistency: 0.1871
- Relationship shift rate: 0.3935
- Relationship overshoot rate: 0.2625
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4166
- Clean envelope violations: 2.4166
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.6632
- Negotiation uniqueness: 0.1482
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1058
- Repetition rate: 0.0312
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2468
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 1.00
- Persona drift 95% CI: [0.1857, 0.1896]

- Phase-level quality:
  - OPENING: drift=0.1921, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1925, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1949, convergence=0.7500, diversity=0.3750
  - CLOSING: drift=0.1649, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate

### japan_intern_training_reform_3actor:naive
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1892 (+/- 0.0077)
- Clean persona drift MAE: 0.1892
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.0967, A 0.1792, N 0.1933
- Relationship inconsistency: 0.1150
- Relationship shift rate: 0.3947
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5834
- Clean envelope violations: 2.5834
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
- Dialogue coherence: 0.0644
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2327
- Commitment fulfillment rate: 0.5625
- State trajectory variance: 0.0000
- Mean turns: 1.10
- Persona drift 95% CI: [0.1868, 0.1916]

- Phase-level quality:
  - OPENING: drift=0.1923, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1993, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1996, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1742, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:engine_structural
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1510 (+/- 0.0058)
- Clean persona drift MAE: 0.1510
- Per-trait absolute error: O 0.1550, C 0.2410, E 0.0626, A 0.1225, N 0.1740
- Relationship inconsistency: 0.0757
- Relationship shift rate: 0.3169
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1009
- Repetition rate: 0.0000
- Topic drift rate: 0.6607
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3680
- Commitment fulfillment rate: 0.8830
- State trajectory variance: 0.0000
- Mean turns: 1.40
- Persona drift 95% CI: [0.1492, 0.1528]

- Phase-level quality:
  - OPENING: drift=0.1596, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1431, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1471, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:naive
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1628 (+/- 0.0041)
- Clean persona drift MAE: 0.1628
- Per-trait absolute error: O 0.1820, C 0.2400, E 0.0935, A 0.1247, N 0.1740
- Relationship inconsistency: 0.2335
- Relationship shift rate: 0.5244
- Relationship overshoot rate: 0.4650
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
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
- Dialogue coherence: 0.0744
- Repetition rate: 0.0000
- Topic drift rate: 0.8392
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3417
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 1.40
- Persona drift 95% CI: [0.1616, 0.1641]

- Phase-level quality:
  - OPENING: drift=0.1733, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1471, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1534, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2030, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:engine_structural
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1796 (+/- 0.0040)
- Clean persona drift MAE: 0.1796
- Per-trait absolute error: O 0.1825, C 0.1977, E 0.1469, A 0.1987, N 0.1721
- Relationship inconsistency: 0.0675
- Relationship shift rate: 0.3347
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3750
- Clean envelope violations: 2.3750
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1082
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4844
- Commitment fulfillment rate: 0.8959
- State trajectory variance: 0.0001
- Mean turns: 2.20
- Persona drift 95% CI: [0.1783, 0.1809]

- Phase-level quality:
  - OPENING: drift=0.1857, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1974, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1760, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1986, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:naive
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1970 (+/- 0.0044)
- Clean persona drift MAE: 0.1970
- Per-trait absolute error: O 0.2510, C 0.1951, E 0.1743, A 0.2012, N 0.1632
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3238
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5250
- Clean envelope violations: 2.5250
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
- Dialogue coherence: 0.0827
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5177
- Commitment fulfillment rate: 0.8129
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1956, 0.1983]

- Phase-level quality:
  - OPENING: drift=0.1979, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2019, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1871, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2082, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:engine_structural
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0056)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.1484, C 0.2667, E 0.1145, A 0.1383, N 0.2067
- Relationship inconsistency: 0.0772
- Relationship shift rate: 0.3055
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1143
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4395
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 1.10
- Persona drift 95% CI: [0.1732, 0.1766]

- Phase-level quality:
  - OPENING: drift=0.1678, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1743, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1704, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2009, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:naive
- Runs: 40
- Clean runs: 40
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0023)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1450, C 0.2667, E 0.1286, A 0.1400, N 0.2083
- Relationship inconsistency: 0.0844
- Relationship shift rate: 0.2764
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
- Dialogue coherence: 0.0895
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4564
- Commitment fulfillment rate: 0.8929
- State trajectory variance: 0.0000
- Mean turns: 1.10
- Persona drift 95% CI: [0.177, 0.1784]

- Phase-level quality:
  - OPENING: drift=0.1818, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1793, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1734, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1820, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:engine_structural
- Runs: 38
- Clean runs: 38
- Contaminated runs: 0
- Persona drift MAE: 0.1549 (+/- 0.0087)
- Clean persona drift MAE: 0.1549
- Per-trait absolute error: O 0.1635, C 0.2127, E 0.1050, A 0.1164, N 0.1768
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0893
- Repetition rate: 0.0263
- Topic drift rate: 0.4793
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5281
- Commitment fulfillment rate: 0.9123
- State trajectory variance: 0.0000
- Mean turns: 1.47
- Persona drift 95% CI: [0.1521, 0.1576]

- Phase-level quality:
  - OPENING: drift=0.1669, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1674, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1586, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1721, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### microsoft_activision_merger_5actor:naive
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.1722 (+/- 0.0071)
- Clean persona drift MAE: 0.1722
- Per-trait absolute error: O 0.2140, C 0.2154, E 0.1276, A 0.1237, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0804
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5385
- Commitment fulfillment rate: 0.7036
- State trajectory variance: 0.0000
- Mean turns: 1.56
- Persona drift 95% CI: [0.1699, 0.1745]

- Phase-level quality:
  - OPENING: drift=0.1817, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1618, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1976, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:engine_structural
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.1741 (+/- 0.0028)
- Clean persona drift MAE: 0.1741
- Per-trait absolute error: O 0.2085, C 0.1983, E 0.1459, A 0.1686, N 0.1494
- Relationship inconsistency: 0.2512
- Relationship shift rate: 0.3573
- Relationship overshoot rate: 0.4562
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0875
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4332
- Commitment fulfillment rate: 0.9333
- State trajectory variance: 0.0000
- Mean turns: 2.44
- Persona drift 95% CI: [0.1732, 0.175]

- Phase-level quality:
  - OPENING: drift=0.1685, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1908, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1774, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1846, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:naive
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.1914 (+/- 0.0040)
- Clean persona drift MAE: 0.1914
- Per-trait absolute error: O 0.2555, C 0.2122, E 0.1592, A 0.1763, N 0.1538
- Relationship inconsistency: 0.1250
- Relationship shift rate: 0.4387
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5250
- Clean envelope violations: 2.5250
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
- Dialogue coherence: 0.0718
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4347
- Commitment fulfillment rate: 0.7262
- State trajectory variance: 0.0000
- Mean turns: 2.44
- Persona drift 95% CI: [0.1901, 0.1927]

- Phase-level quality:
  - OPENING: drift=0.1766, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2014, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1888, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1923, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:engine_structural
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.1956 (+/- 0.0022)
- Clean persona drift MAE: 0.1956
- Per-trait absolute error: O 0.1667, C 0.2333, E 0.2049, A 0.2017, N 0.1717
- Relationship inconsistency: 0.1505
- Relationship shift rate: 0.3083
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4167
- Clean envelope violations: 2.4167
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0936
- Repetition rate: 0.0000
- Topic drift rate: 0.5227
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4876
- Commitment fulfillment rate: 0.9375
- State trajectory variance: 0.0000
- Mean turns: 1.22
- Persona drift 95% CI: [0.1949, 0.1963]

- Phase-level quality:
  - OPENING: drift=0.2036, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2048, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1980, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1760, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:naive
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.2126 (+/- 0.0060)
- Clean persona drift MAE: 0.2126
- Per-trait absolute error: O 0.1950, C 0.2333, E 0.2446, A 0.2183, N 0.1717
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1410
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
- Dialogue coherence: 0.0620
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4414
- Commitment fulfillment rate: 0.3500
- State trajectory variance: 0.0000
- Mean turns: 1.22
- Persona drift 95% CI: [0.2106, 0.2145]

- Phase-level quality:
  - OPENING: drift=0.2102, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2138, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2235, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1795, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:engine_structural
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.1970 (+/- 0.0049)
- Clean persona drift MAE: 0.1970
- Per-trait absolute error: O 0.1850, C 0.2043, E 0.2014, A 0.1842, N 0.2100
- Relationship inconsistency: 0.0339
- Relationship shift rate: 0.3200
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.8333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0278
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4933
- Commitment fulfillment rate: 0.6286
- State trajectory variance: 0.0000
- Mean turns: 1.56
- Persona drift 95% CI: [0.1954, 0.1986]

- Phase-level quality:
  - OPENING: drift=0.2080, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1962, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1881, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2496, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### netflix_password_crackdown_5actor:naive
- Runs: 36
- Clean runs: 36
- Contaminated runs: 0
- Persona drift MAE: 0.2186 (+/- 0.0065)
- Clean persona drift MAE: 0.2186
- Per-trait absolute error: O 0.2020, C 0.2266, E 0.2303, A 0.2132, N 0.2210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3174
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0500
- Clean envelope violations: 3.0500
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
- Dialogue coherence: 0.0800
- Repetition rate: 0.0000
- Topic drift rate: 0.6071
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5104
- Commitment fulfillment rate: 0.6429
- State trajectory variance: 0.0000
- Mean turns: 1.56
- Persona drift 95% CI: [0.2165, 0.2207]

- Phase-level quality:
  - OPENING: drift=0.2190, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2036, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1935, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2584, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:engine_structural
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1615 (+/- 0.0015)
- Clean persona drift MAE: 0.1615
- Per-trait absolute error: O 0.1640, C 0.1610, E 0.1452, A 0.1822, N 0.1553
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3823
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0735
- Repetition rate: 0.0000
- Topic drift rate: 0.4886
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4939
- Commitment fulfillment rate: 0.7046
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.161, 0.162]

- Phase-level quality:
  - OPENING: drift=0.1571, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1833, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1568, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1784, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:naive
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0018)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.1755, C 0.1638, E 0.1876, A 0.1818, N 0.1627
- Relationship inconsistency: 0.0015
- Relationship shift rate: 0.3603
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0742
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4740
- Commitment fulfillment rate: 0.4722
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1737, 0.1749]

- Phase-level quality:
  - OPENING: drift=0.1671, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1875, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1698, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1872, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:engine_structural
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1670 (+/- 0.0101)
- Clean persona drift MAE: 0.1670
- Per-trait absolute error: O 0.1384, C 0.2000, E 0.1667, A 0.1300, N 0.2000
- Relationship inconsistency: 0.1361
- Relationship shift rate: 0.2714
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7500
- Clean envelope violations: 1.7500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0940
- Repetition rate: 0.0000
- Topic drift rate: 0.8637
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4635
- Commitment fulfillment rate: 0.7619
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1635, 0.1705]

- Phase-level quality:
  - OPENING: drift=0.1623, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1640, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1617, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1557, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:naive
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1666 (+/- 0.0110)
- Clean persona drift MAE: 0.1666
- Per-trait absolute error: O 0.1133, C 0.2000, E 0.1931, A 0.1267, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2399
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
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0780
- Repetition rate: 0.0000
- Topic drift rate: 0.8637
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4388
- Commitment fulfillment rate: 0.7375
- State trajectory variance: 0.0000
- Mean turns: 1.38
- Persona drift 95% CI: [0.1628, 0.1704]

- Phase-level quality:
  - OPENING: drift=0.1700, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1688, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1623, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1575, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:engine_structural
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1356 (+/- 0.0035)
- Clean persona drift MAE: 0.1356
- Per-trait absolute error: O 0.1170, C 0.2800, E 0.1220, A 0.0742, N 0.0850
- Relationship inconsistency: 0.1044
- Relationship shift rate: 0.2728
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.8333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.3333
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0960
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4520
- Commitment fulfillment rate: 0.6755
- State trajectory variance: 0.0000
- Mean turns: 1.75
- Persona drift 95% CI: [0.1344, 0.1369]

- Phase-level quality:
  - OPENING: drift=0.1462, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1292, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1491, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1361, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:naive
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1501 (+/- 0.0063)
- Clean persona drift MAE: 0.1501
- Per-trait absolute error: O 0.1420, C 0.2821, E 0.1516, A 0.0915, N 0.0830
- Relationship inconsistency: 0.0989
- Relationship shift rate: 0.2778
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0792
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4515
- Commitment fulfillment rate: 0.5188
- State trajectory variance: 0.0000
- Mean turns: 1.75
- Persona drift 95% CI: [0.1479, 0.1522]

- Phase-level quality:
  - OPENING: drift=0.1531, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1422, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1535, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1499, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:engine_structural
- Runs: 32
- Clean runs: 32
- Contaminated runs: 0
- Persona drift MAE: 0.1668 (+/- 0.0013)
- Clean persona drift MAE: 0.1668
- Per-trait absolute error: O 0.1660, C 0.2600, E 0.1120, A 0.1234, N 0.1729
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4735
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1157
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4683
- Commitment fulfillment rate: 0.8816
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1664, 0.1673]

- Phase-level quality:
  - OPENING: drift=0.1718, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1546, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1779, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1593, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:naive
- Runs: 30
- Clean runs: 30
- Contaminated runs: 0
- Persona drift MAE: 0.1775 (+/- 0.0037)
- Clean persona drift MAE: 0.1775
- Per-trait absolute error: O 0.1797, C 0.2600, E 0.1538, A 0.1245, N 0.1695
- Relationship inconsistency: 0.0429
- Relationship shift rate: 0.3742
- Relationship overshoot rate: 0.3300
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1733
- Clean envelope violations: 2.1733
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
- Dialogue coherence: 0.0718
- Repetition rate: 0.0000
- Topic drift rate: 0.7151
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4245
- Commitment fulfillment rate: 0.6753
- State trajectory variance: 0.0000
- Mean turns: 2.93
- Persona drift 95% CI: [0.1761, 0.1788]

- Phase-level quality:
  - OPENING: drift=0.1815, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1831, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1756, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:engine_structural
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1681 (+/- 0.0108)
- Clean persona drift MAE: 0.1681
- Per-trait absolute error: O 0.1167, C 0.2443, E 0.1568, A 0.1592, N 0.1633
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2125
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
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
- Dialogue coherence: 0.1254
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3796
- Commitment fulfillment rate: 0.6274
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1641, 0.1721]

- Phase-level quality:
  - OPENING: drift=0.1691, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1766, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1752, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1694, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:naive
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1842 (+/- 0.0058)
- Clean persona drift MAE: 0.1842
- Per-trait absolute error: O 0.1567, C 0.2571, E 0.1663, A 0.1708, N 0.1700
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1446
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4166
- Clean envelope violations: 2.4166
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
- Dialogue coherence: 0.0863
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3791
- Commitment fulfillment rate: 0.6813
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.182, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1798, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1825, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1821, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1736, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:engine_structural
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1490 (+/- 0.0011)
- Clean persona drift MAE: 0.1490
- Per-trait absolute error: O 0.1370, C 0.2073, E 0.1150, A 0.1195, N 0.1660
- Relationship inconsistency: 0.3460
- Relationship shift rate: 0.3393
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1123
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4435
- Commitment fulfillment rate: 0.8234
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1486, 0.1494]

- Phase-level quality:
  - OPENING: drift=0.1670, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1309, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1516, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1987, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:naive
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1537 (+/- 0.0033)
- Clean persona drift MAE: 0.1537
- Per-trait absolute error: O 0.1440, C 0.2085, E 0.1318, A 0.1212, N 0.1630
- Relationship inconsistency: 0.0907
- Relationship shift rate: 0.3354
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
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
- Dialogue coherence: 0.0866
- Repetition rate: 0.0000
- Topic drift rate: 0.5536
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4242
- Commitment fulfillment rate: 0.5637
- State trajectory variance: 0.0000
- Mean turns: 2.00
- Persona drift 95% CI: [0.1525, 0.1549]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1365, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1551, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2054, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:engine_structural
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1689 (+/- 0.0052)
- Clean persona drift MAE: 0.1689
- Per-trait absolute error: O 0.1440, C 0.2271, E 0.1244, A 0.1775, N 0.1717
- Relationship inconsistency: 0.1794
- Relationship shift rate: 0.3370
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
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1169
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4286
- Commitment fulfillment rate: 0.6722
- State trajectory variance: 0.0000
- Mean turns: 3.14
- Persona drift 95% CI: [0.167, 0.1709]

- Phase-level quality:
  - OPENING: drift=0.1769, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1727, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1850, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1530, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:naive
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0060)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.1865, C 0.2279, E 0.1407, A 0.1693, N 0.1722
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0990
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4101
- Commitment fulfillment rate: 0.7299
- State trajectory variance: 0.0000
- Mean turns: 3.14
- Persona drift 95% CI: [0.1771, 0.1816]

- Phase-level quality:
  - OPENING: drift=0.1795, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1808, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1964, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1584, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:engine_structural
- Runs: 28
- Clean runs: 28
- Contaminated runs: 0
- Persona drift MAE: 0.1502 (+/- 0.0067)
- Clean persona drift MAE: 0.1502
- Per-trait absolute error: O 0.1116, C 0.2000, E 0.0592, A 0.1733, N 0.2067
- Relationship inconsistency: 0.0273
- Relationship shift rate: 0.3124
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1159
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4666
- Commitment fulfillment rate: 0.6583
- State trajectory variance: 0.0000
- Mean turns: 1.57
- Persona drift 95% CI: [0.1477, 0.1527]

- Phase-level quality:
  - OPENING: drift=0.1634, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1615, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1645, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1703, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:naive
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.1778 (+/- 0.0046)
- Clean persona drift MAE: 0.1778
- Per-trait absolute error: O 0.1867, C 0.2330, E 0.0949, A 0.1808, N 0.1933
- Relationship inconsistency: 0.0311
- Relationship shift rate: 0.2328
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0800
- Repetition rate: 0.0000
- Topic drift rate: 0.2045
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4501
- Commitment fulfillment rate: 0.6250
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.1759, 0.1796]

- Phase-level quality:
  - OPENING: drift=0.1719, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1837, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1811, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1728, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:engine_structural
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.1647 (+/- 0.0080)
- Clean persona drift MAE: 0.1647
- Per-trait absolute error: O 0.0840, C 0.2099, E 0.1679, A 0.1802, N 0.1815
- Relationship inconsistency: 0.0801
- Relationship shift rate: 0.2705
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
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1162
- Repetition rate: 0.0000
- Topic drift rate: 0.4107
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3937
- Commitment fulfillment rate: 0.6786
- State trajectory variance: 0.0000
- Mean turns: 2.33
- Persona drift 95% CI: [0.1615, 0.1679]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1827, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1641, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1580, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:naive
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.1786 (+/- 0.0021)
- Clean persona drift MAE: 0.1786
- Per-trait absolute error: O 0.1240, C 0.2096, E 0.1937, A 0.1812, N 0.1845
- Relationship inconsistency: 0.0465
- Relationship shift rate: 0.2650
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0911
- Repetition rate: 0.0000
- Topic drift rate: 0.5536
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3876
- Commitment fulfillment rate: 0.8063
- State trajectory variance: 0.0000
- Mean turns: 2.33
- Persona drift 95% CI: [0.1778, 0.1795]

- Phase-level quality:
  - OPENING: drift=0.1918, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1915, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1748, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1567, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:engine_structural
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.1816 (+/- 0.0007)
- Clean persona drift MAE: 0.1816
- Per-trait absolute error: O 0.1150, C 0.2400, E 0.2092, A 0.1963, N 0.1475
- Relationship inconsistency: 0.1250
- Relationship shift rate: 0.2824
- Relationship overshoot rate: 0.2400
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2250
- Clean envelope violations: 2.2250
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.1968
- Negotiation uniqueness: 0.0471
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1110
- Repetition rate: 0.0000
- Topic drift rate: 0.8068
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3888
- Commitment fulfillment rate: 0.7229
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1813, 0.1819]

- Phase-level quality:
  - OPENING: drift=0.1836, convergence=1.0000, diversity=0.1834
  - TENSION: drift=0.1933, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1854, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1873, convergence=1.0000, diversity=0.2708

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:naive
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.1942 (+/- 0.0047)
- Clean persona drift MAE: 0.1942
- Per-trait absolute error: O 0.1490, C 0.2400, E 0.2233, A 0.2038, N 0.1549
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6500
- Clean envelope violations: 2.6500
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
- Topic drift rate: 0.8750
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3916
- Commitment fulfillment rate: 0.4782
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1923, 0.1961]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1961, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1938, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2010, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:engine_structural
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.1965 (+/- 0.0088)
- Clean persona drift MAE: 0.1965
- Per-trait absolute error: O 0.1933, C 0.2667, E 0.1000, A 0.2225, N 0.2000
- Relationship inconsistency: 0.0710
- Relationship shift rate: 0.1477
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
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
- Dialogue coherence: 0.1012
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4608
- Commitment fulfillment rate: 0.7917
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.193, 0.2]

- Phase-level quality:
  - OPENING: drift=0.1881, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1911, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1950, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2000, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:naive
- Runs: 24
- Clean runs: 24
- Contaminated runs: 0
- Persona drift MAE: 0.2066 (+/- 0.0078)
- Clean persona drift MAE: 0.2066
- Per-trait absolute error: O 0.2267, C 0.2667, E 0.1138, A 0.2592, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9167
- Clean envelope violations: 2.9167
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
- Dialogue coherence: 0.0824
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4824
- Commitment fulfillment rate: 0.7917
- State trajectory variance: 0.0000
- Mean turns: 1.83
- Persona drift 95% CI: [0.2035, 0.2097]

- Phase-level quality:
  - OPENING: drift=0.1932, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1996, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1970, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2000, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:engine_structural
- Runs: 22
- Clean runs: 22
- Contaminated runs: 0
- Persona drift MAE: 0.1919 (+/- 0.0037)
- Clean persona drift MAE: 0.1919
- Per-trait absolute error: O 0.1664, C 0.2832, E 0.1593, A 0.1600, N 0.1905
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2947
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1036
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4597
- Commitment fulfillment rate: 0.8043
- State trajectory variance: 0.0000
- Mean turns: 2.55
- Persona drift 95% CI: [0.1903, 0.1935]

- Phase-level quality:
  - OPENING: drift=0.1929, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1944, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.2017, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2241, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:naive
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.2031 (+/- 0.0031)
- Clean persona drift MAE: 0.2031
- Per-trait absolute error: O 0.1930, C 0.2800, E 0.1762, A 0.1512, N 0.2150
- Relationship inconsistency: 0.1193
- Relationship shift rate: 0.3801
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6500
- Clean envelope violations: 2.6500
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
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.5179
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4670
- Commitment fulfillment rate: 0.5643
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.2018, 0.2044]

- Phase-level quality:
  - OPENING: drift=0.2059, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2040, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2026, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2182, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:engine_structural
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0034)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.1850, C 0.1841, E 0.1386, A 0.1676, N 0.1316
- Relationship inconsistency: 0.1162
- Relationship shift rate: 0.3590
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0894
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3854
- Commitment fulfillment rate: 0.9021
- State trajectory variance: 0.0000
- Mean turns: 4.40
- Persona drift 95% CI: [0.1599, 0.1628]

- Phase-level quality:
  - OPENING: drift=0.1800, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1496, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1699, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1528, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:naive
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1646 (+/- 0.0045)
- Clean persona drift MAE: 0.1646
- Per-trait absolute error: O 0.1835, C 0.1939, E 0.1429, A 0.1764, N 0.1260
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4910
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2750
- Clean envelope violations: 2.2750
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
- Dialogue coherence: 0.0632
- Repetition rate: 0.0000
- Topic drift rate: 0.8636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3781
- Commitment fulfillment rate: 0.7222
- State trajectory variance: 0.0000
- Mean turns: 4.40
- Persona drift 95% CI: [0.1626, 0.1666]

- Phase-level quality:
  - OPENING: drift=0.1815, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1500, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1741, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1550, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:engine_structural
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1396 (+/- 0.0052)
- Clean persona drift MAE: 0.1396
- Per-trait absolute error: O 0.1417, C 0.1052, E 0.0847, A 0.1667, N 0.2000
- Relationship inconsistency: 0.3839
- Relationship shift rate: 0.3696
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.4896
- Negotiation uniqueness: 0.1045
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4516
- Commitment fulfillment rate: 0.9286
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1374, 0.1419]

- Phase-level quality:
  - OPENING: drift=0.1559, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1600, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1445, convergence=0.7500, diversity=0.2916
  - CLOSING: drift=0.1588, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:naive
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1577 (+/- 0.0146)
- Clean persona drift MAE: 0.1577
- Per-trait absolute error: O 0.1800, C 0.1128, E 0.1167, A 0.1792, N 0.2000
- Relationship inconsistency: 0.4765
- Relationship shift rate: 0.5624
- Relationship overshoot rate: 0.4625
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
- Dialogue coherence: 0.0917
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4406
- Commitment fulfillment rate: 0.8958
- State trajectory variance: 0.0000
- Mean turns: 2.20
- Persona drift 95% CI: [0.1513, 0.1641]

- Phase-level quality:
  - OPENING: drift=0.1641, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1625, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1534, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1665, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:engine_structural
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0030)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.1430, C 0.2000, E 0.1210, A 0.2155, N 0.2105
- Relationship inconsistency: 0.1998
- Relationship shift rate: 0.3845
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3507
- Negotiation uniqueness: 0.0806
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0938
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4050
- Commitment fulfillment rate: 0.8661
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.1767, 0.1793]

- Phase-level quality:
  - OPENING: drift=0.1936, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1726, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1757, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.2307, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:naive
- Runs: 20
- Clean runs: 20
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0046)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1750, C 0.2088, E 0.1279, A 0.2325, N 0.2010
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2547
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5500
- Clean envelope violations: 2.5500
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
- Dialogue coherence: 0.0797
- Repetition rate: 0.0000
- Topic drift rate: 0.8393
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4318
- Commitment fulfillment rate: 0.7000
- State trajectory variance: 0.0000
- Mean turns: 2.80
- Persona drift 95% CI: [0.187, 0.191]

- Phase-level quality:
  - OPENING: drift=0.1942, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1833, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1827, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2331, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1608 (+/- 0.0025)
- Clean persona drift MAE: 0.1608
- Per-trait absolute error: O 0.1865, C 0.2121, E 0.1161, A 0.1291, N 0.1600
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.2940
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1080
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4111
- Commitment fulfillment rate: 0.7261
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1595, 0.162]

- Phase-level quality:
  - OPENING: drift=0.1621, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1704, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1663, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1560, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1720 (+/- 0.0053)
- Clean persona drift MAE: 0.1720
- Per-trait absolute error: O 0.1840, C 0.2291, E 0.1581, A 0.1290, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3483
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0760
- Repetition rate: 0.0000
- Topic drift rate: 0.7387
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4175
- Commitment fulfillment rate: 0.5591
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1694, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1645, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1785, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1711, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1723, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1489 (+/- 0.0012)
- Clean persona drift MAE: 0.1489
- Per-trait absolute error: O 0.1683, C 0.2578, E 0.0306, A 0.1542, N 0.1333
- Relationship inconsistency: 0.0413
- Relationship shift rate: 0.2113
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1060
- Repetition rate: 0.0000
- Topic drift rate: 0.3182
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3721
- Commitment fulfillment rate: 0.6290
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1483, 0.1495]

- Phase-level quality:
  - OPENING: drift=0.1599, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1581, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1638, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1643, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1598 (+/- 0.0145)
- Clean persona drift MAE: 0.1598
- Per-trait absolute error: O 0.1767, C 0.3074, E 0.0459, A 0.1358, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1931
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
- Dialogue coherence: 0.0833
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3431
- Commitment fulfillment rate: 0.5000
- State trajectory variance: 0.0000
- Mean turns: 2.75
- Persona drift 95% CI: [0.1527, 0.1669]

- Phase-level quality:
  - OPENING: drift=0.1667, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1703, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1638, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1709, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1680 (+/- 0.0043)
- Clean persona drift MAE: 0.1680
- Per-trait absolute error: O 0.1690, C 0.2033, E 0.1326, A 0.1153, N 0.2200
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2286
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1222
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4049
- Commitment fulfillment rate: 0.7167
- State trajectory variance: 0.0000
- Mean turns: 3.50
- Persona drift 95% CI: [0.1659, 0.1701]

- Phase-level quality:
  - OPENING: drift=0.1934, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1613, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1681, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2011, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0024)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.1690, C 0.2165, E 0.1744, A 0.1170, N 0.2200
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3674
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0995
- Repetition rate: 0.0000
- Topic drift rate: 0.4107
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3645
- Commitment fulfillment rate: 0.7715
- State trajectory variance: 0.0000
- Mean turns: 3.50
- Persona drift 95% CI: [0.1782, 0.1806]

- Phase-level quality:
  - OPENING: drift=0.1973, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1636, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1821, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2013, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1711 (+/- 0.0016)
- Clean persona drift MAE: 0.1711
- Per-trait absolute error: O 0.1595, C 0.2600, E 0.1346, A 0.1323, N 0.1696
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4292
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3250
- Clean envelope violations: 2.3250
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5000
- Action family convergence: 1.0000
- Role action diversity: 0.2698
- Negotiation uniqueness: 0.0552
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1168
- Repetition rate: 0.0000
- Topic drift rate: 0.4886
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3713
- Commitment fulfillment rate: 0.8638
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1704, 0.1719]

- Phase-level quality:
  - OPENING: drift=0.1755, convergence=0.7500, diversity=0.2291
  - TENSION: drift=0.1734, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1709, convergence=1.0000, diversity=0.1834
  - CLOSING: drift=0.1761, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:naive
- Runs: 14
- Clean runs: 14
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0025)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.1730, C 0.2600, E 0.1388, A 0.1282, N 0.1717
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4627
- Relationship overshoot rate: 0.3214
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3214
- Clean envelope violations: 2.3214
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
- Topic drift rate: 0.5779
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3615
- Commitment fulfillment rate: 0.6020
- State trajectory variance: 0.0000
- Mean turns: 6.29
- Persona drift 95% CI: [0.173, 0.1756]

- Phase-level quality:
  - OPENING: drift=0.1749, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1761, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1769, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1753, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1778 (+/- 0.0073)
- Clean persona drift MAE: 0.1778
- Per-trait absolute error: O 0.1200, C 0.3000, E 0.1074, A 0.1617, N 0.2000
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.2455
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1114
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4607
- Commitment fulfillment rate: 0.8333
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1737, 0.1819]

- Phase-level quality:
  - OPENING: drift=0.1845, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1906, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1858, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1852, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1904 (+/- 0.0059)
- Clean persona drift MAE: 0.1904
- Per-trait absolute error: O 0.1416, C 0.3000, E 0.1237, A 0.1800, N 0.2067
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.3504
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0738
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4861
- Commitment fulfillment rate: 0.8375
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.187, 0.1938]

- Phase-level quality:
  - OPENING: drift=0.1961, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1923, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1840, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1935, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1916 (+/- 0.0009)
- Clean persona drift MAE: 0.1916
- Per-trait absolute error: O 0.1760, C 0.2022, E 0.1585, A 0.2412, N 0.1800
- Relationship inconsistency: 0.0399
- Relationship shift rate: 0.3469
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0867
- Repetition rate: 0.0000
- Topic drift rate: 0.5179
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3906
- Commitment fulfillment rate: 0.6151
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.1911, 0.1921]

- Phase-level quality:
  - OPENING: drift=0.2010, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1823, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1970, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2100, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1952 (+/- 0.0048)
- Clean persona drift MAE: 0.1952
- Per-trait absolute error: O 0.1810, C 0.2000, E 0.1691, A 0.2470, N 0.1790
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.6293
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6500
- Clean envelope violations: 2.6500
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
- Dialogue coherence: 0.0722
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3413
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 4.67
- Persona drift 95% CI: [0.1925, 0.1979]

- Phase-level quality:
  - OPENING: drift=0.2041, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1858, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1978, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2100, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1910 (+/- 0.0033)
- Clean persona drift MAE: 0.1910
- Per-trait absolute error: O 0.1865, C 0.1866, E 0.2097, A 0.1920, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1575
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1108
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4073
- Commitment fulfillment rate: 0.7113
- State trajectory variance: 0.0000
- Mean turns: 7.33
- Persona drift 95% CI: [0.1891, 0.1929]

- Phase-level quality:
  - OPENING: drift=0.1943, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1954, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1916, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1931, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1968 (+/- 0.0048)
- Clean persona drift MAE: 0.1968
- Per-trait absolute error: O 0.1965, C 0.1919, E 0.2184, A 0.1967, N 0.1804
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1978
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0865
- Repetition rate: 0.0000
- Topic drift rate: 0.1932
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2822
- Commitment fulfillment rate: 0.7312
- State trajectory variance: 0.0000
- Mean turns: 7.33
- Persona drift 95% CI: [0.1941, 0.1995]

- Phase-level quality:
  - OPENING: drift=0.1976, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2037, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1949, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1919, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1701 (+/- 0.0040)
- Clean persona drift MAE: 0.1701
- Per-trait absolute error: O 0.1083, C 0.3000, E 0.1028, A 0.2392, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0488
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
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.1493
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0931
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4410
- Commitment fulfillment rate: 0.6583
- State trajectory variance: 0.0000
- Mean turns: 3.67
- Persona drift 95% CI: [0.1678, 0.1724]

- Phase-level quality:
  - OPENING: drift=0.1728, convergence=0.2500, diversity=0.1250
  - TENSION: drift=0.1713, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1710, convergence=0.7500, diversity=0.2916
  - CLOSING: drift=0.1920, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0029)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1233, C 0.3000, E 0.1004, A 0.2583, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0683
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
- Dialogue coherence: 0.0741
- Repetition rate: 0.0000
- Topic drift rate: 0.3409
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3769
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1744, 0.1785]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1719, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1745, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2104, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1755 (+/- 0.0030)
- Clean persona drift MAE: 0.1755
- Per-trait absolute error: O 0.2120, C 0.2036, E 0.1200, A 0.2130, N 0.1290
- Relationship inconsistency: 0.0638
- Relationship shift rate: 0.2823
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4114
- Commitment fulfillment rate: 0.8333
- State trajectory variance: 0.0000
- Mean turns: 7.00
- Persona drift 95% CI: [0.1734, 0.1776]

- Phase-level quality:
  - OPENING: drift=0.2006, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1628, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1732, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2155, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1848 (+/- 0.0060)
- Clean persona drift MAE: 0.1848
- Per-trait absolute error: O 0.2120, C 0.2113, E 0.1522, A 0.2285, N 0.1200
- Relationship inconsistency: 0.1920
- Relationship shift rate: 0.3090
- Relationship overshoot rate: 0.2333
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
- Dialogue coherence: 0.0759
- Repetition rate: 0.0000
- Topic drift rate: 0.5893
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3771
- Commitment fulfillment rate: 0.6833
- State trajectory variance: 0.0000
- Mean turns: 7.00
- Persona drift 95% CI: [0.1806, 0.189]

- Phase-level quality:
  - OPENING: drift=0.2100, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1820, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2223, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0041)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.2045, C 0.1996, E 0.2022, A 0.1535, N 0.1004
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1883
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2750
- Clean envelope violations: 2.2750
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1050
- Repetition rate: 0.0208
- Topic drift rate: 0.3182
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4489
- Commitment fulfillment rate: 0.8141
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1692, 0.1749]

- Phase-level quality:
  - OPENING: drift=0.1647, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1829, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1643, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1878, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### wework_ipo_collapse_10actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1774 (+/- 0.0037)
- Clean persona drift MAE: 0.1774
- Per-trait absolute error: O 0.2150, C 0.2019, E 0.2212, A 0.1498, N 0.0992
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3000
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
- Dialogue coherence: 0.0677
- Repetition rate: 0.0000
- Topic drift rate: 0.3977
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4333
- Commitment fulfillment rate: 0.6731
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1749, 0.18]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1822, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1718, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1885, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1953 (+/- 0.0105)
- Clean persona drift MAE: 0.1953
- Per-trait absolute error: O 0.1367, C 0.2009, E 0.1842, A 0.2300, N 0.2250
- Relationship inconsistency: 0.0009
- Relationship shift rate: 0.2071
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1216
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3374
- Commitment fulfillment rate: 0.7940
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1881, 0.2026]

- Phase-level quality:
  - OPENING: drift=0.1886, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1993, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1999, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2122, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1950 (+/- 0.0171)
- Clean persona drift MAE: 0.1950
- Per-trait absolute error: O 0.1484, C 0.2220, E 0.1656, A 0.2175, N 0.2217
- Relationship inconsistency: 0.0721
- Relationship shift rate: 0.2843
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1011
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3644
- Commitment fulfillment rate: 0.4036
- State trajectory variance: 0.0000
- Mean turns: 5.50
- Persona drift 95% CI: [0.1831, 0.2069]

- Phase-level quality:
  - OPENING: drift=0.1907, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1957, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1941, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2188, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1573 (+/- 0.0024)
- Clean persona drift MAE: 0.1573
- Per-trait absolute error: O 0.1473, C 0.2027, E 0.1541, A 0.1333, N 0.1487
- Relationship inconsistency: 0.0999
- Relationship shift rate: 0.3184
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1667
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1273
- Repetition rate: 0.0000
- Topic drift rate: 0.4167
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4742
- Commitment fulfillment rate: 0.7795
- State trajectory variance: 0.0000
- Mean turns: 9.33
- Persona drift 95% CI: [0.1553, 0.1592]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1731, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1466, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1685, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0079)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.1590, C 0.2261, E 0.1959, A 0.1487, N 0.1430
- Relationship inconsistency: 0.5088
- Relationship shift rate: 0.3829
- Relationship overshoot rate: 0.4800
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
- Dialogue coherence: 0.0906
- Repetition rate: 0.0000
- Topic drift rate: 0.5893
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4377
- Commitment fulfillment rate: 0.6369
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1668, 0.1823]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1784, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1538, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1821, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1857 (+/- 0.0024)
- Clean persona drift MAE: 0.1857
- Per-trait absolute error: O 0.1845, C 0.2800, E 0.1442, A 0.1616, N 0.1584
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3573
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1023
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4018
- Commitment fulfillment rate: 0.8695
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1834, 0.1881]

- Phase-level quality:
  - OPENING: drift=0.1866, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1867, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1960, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1761, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1907 (+/- 0.0023)
- Clean persona drift MAE: 0.1907
- Per-trait absolute error: O 0.1985, C 0.2800, E 0.1489, A 0.1679, N 0.1582
- Relationship inconsistency: 0.1148
- Relationship shift rate: 0.3440
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
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
- Topic drift rate: 0.5341
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3883
- Commitment fulfillment rate: 0.7459
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1884, 0.193]

- Phase-level quality:
  - OPENING: drift=0.1889, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1919, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1985, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1856, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1690 (+/- 0.0072)
- Clean persona drift MAE: 0.1690
- Per-trait absolute error: O 0.1267, C 0.2333, E 0.1466, A 0.1384, N 0.2000
- Relationship inconsistency: 0.0961
- Relationship shift rate: 0.3166
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8333
- Clean envelope violations: 1.8333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1185
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3635
- Commitment fulfillment rate: 0.9226
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.162, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1911, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1834, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1862, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1769, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1937 (+/- 0.0096)
- Clean persona drift MAE: 0.1937
- Per-trait absolute error: O 0.1667, C 0.2333, E 0.2162, A 0.1525, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0425
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4166
- Clean envelope violations: 2.4166
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
- Dialogue coherence: 0.0780
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3566
- Commitment fulfillment rate: 0.8393
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1843, 0.2031]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1950, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2044, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1861, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2019 (+/- 0.0018)
- Clean persona drift MAE: 0.2019
- Per-trait absolute error: O 0.2370, C 0.2252, E 0.1831, A 0.2015, N 0.1630
- Relationship inconsistency: 0.2797
- Relationship shift rate: 0.3342
- Relationship overshoot rate: 0.3563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7500
- Clean envelope violations: 2.7500
- Structured action validity: 0.8333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1308
- Repetition rate: 0.0000
- Topic drift rate: 0.4465
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3921
- Commitment fulfillment rate: 0.9022
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2002, 0.2037]

- Phase-level quality:
  - OPENING: drift=0.2128, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2028, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1993, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2147 (+/- 0.0044)
- Clean persona drift MAE: 0.2147
- Per-trait absolute error: O 0.2600, C 0.2288, E 0.2103, A 0.2087, N 0.1660
- Relationship inconsistency: 0.2859
- Relationship shift rate: 0.4888
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0858
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3805
- Commitment fulfillment rate: 0.6567
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2104, 0.2191]

- Phase-level quality:
  - OPENING: drift=0.2213, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2039, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2063, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Mode Summary
### exploratory:engine_structural
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1705 (+/- 0.0158)
- Clean persona drift MAE: 0.1705
- Per-trait absolute error: O 0.1620, C 0.2230, E 0.1281, A 0.1693, N 0.1702
- Relationship inconsistency: 0.0765
- Relationship shift rate: 0.2794
- Relationship overshoot rate: 0.2137
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0917
- Clean envelope violations: 2.0917
- Structured action validity: 0.4894
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.2917
- Action-plan alignment: 0.9702
- Planned action coverage: 0.9087
- Action family convergence: 0.7508
- Role action diversity: 0.4938
- Negotiation uniqueness: 0.2721
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1071
- Repetition rate: 0.0014
- Topic drift rate: 0.4691
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4098
- Commitment fulfillment rate: 0.7619
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1677, 0.1734]

- Phase-level quality:
  - OPENING: drift=0.1753, convergence=0.7311, diversity=0.3514
  - TENSION: drift=0.1750, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1741, convergence=0.6183, diversity=0.4943
  - CLOSING: drift=0.1807, convergence=0.7000, diversity=0.5167

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### exploratory:naive
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1804 (+/- 0.0152)
- Clean persona drift MAE: 0.1804
- Per-trait absolute error: O 0.1798, C 0.2298, E 0.1499, A 0.1748, N 0.1679
- Relationship inconsistency: 0.0803
- Relationship shift rate: 0.2736
- Relationship overshoot rate: 0.1663
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3108
- Clean envelope violations: 2.3108
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
- Dialogue coherence: 0.0806
- Repetition rate: 0.0000
- Topic drift rate: 0.4980
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3877
- Commitment fulfillment rate: 0.6950
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1777, 0.1832]

- Phase-level quality:
  - OPENING: drift=0.1822, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1817, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1805, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1857, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### guided:engine_structural
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1690 (+/- 0.0185)
- Clean persona drift MAE: 0.1690
- Per-trait absolute error: O 0.1654, C 0.2207, E 0.1271, A 0.1607, N 0.1712
- Relationship inconsistency: 0.1100
- Relationship shift rate: 0.2891
- Relationship overshoot rate: 0.2613
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1100
- Clean envelope violations: 2.1100
- Structured action validity: 0.7771
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.2083
- Action-plan alignment: 0.9663
- Planned action coverage: 0.9351
- Action family convergence: 0.6778
- Role action diversity: 0.5247
- Negotiation uniqueness: 0.2923
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1058
- Repetition rate: 0.0029
- Topic drift rate: 0.5648
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4189
- Commitment fulfillment rate: 0.8124
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1657, 0.1723]

- Phase-level quality:
  - OPENING: drift=0.1739, convergence=0.7945, diversity=0.3672
  - TENSION: drift=0.1737, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1721, convergence=0.5867, diversity=0.5472
  - CLOSING: drift=0.1831, convergence=0.5500, diversity=0.6090

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### guided:naive
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1801 (+/- 0.0196)
- Clean persona drift MAE: 0.1801
- Per-trait absolute error: O 0.1861, C 0.2240, E 0.1504, A 0.1694, N 0.1704
- Relationship inconsistency: 0.1253
- Relationship shift rate: 0.3073
- Relationship overshoot rate: 0.2222
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3267
- Clean envelope violations: 2.3267
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
- Dialogue coherence: 0.0833
- Repetition rate: 0.0000
- Topic drift rate: 0.5856
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4190
- Commitment fulfillment rate: 0.6571
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1766, 0.1836]

- Phase-level quality:
  - OPENING: drift=0.1812, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1793, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1795, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1878, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### unknown:engine_structural
- Runs: 1816
- Clean runs: 1816
- Contaminated runs: 0
- Persona drift MAE: 0.1675 (+/- 0.0170)
- Clean persona drift MAE: 0.1675
- Per-trait absolute error: O 0.1651, C 0.2206, E 0.1193, A 0.1625, N 0.1699
- Relationship inconsistency: 0.0953
- Relationship shift rate: 0.2819
- Relationship overshoot rate: 0.2276
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0510
- Clean envelope violations: 2.0510
- Structured action validity: 0.6422
- Owner resolution rate: 0.9383
- Executed action contradiction: 0.0000
- State transition coherence: 0.9383
- Action feedback utilization: 0.2126
- Action-plan alignment: 0.9682
- Planned action coverage: 0.9285
- Action family convergence: 0.7084
- Role action diversity: 0.5104
- Negotiation uniqueness: 0.2795
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1064
- Repetition rate: 0.0024
- Topic drift rate: 0.5209
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4100
- Commitment fulfillment rate: 0.7803
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1667, 0.1683]

- Phase-level quality:
  - OPENING: drift=0.1705, convergence=0.7386, diversity=0.3567
  - TENSION: drift=0.1722, convergence=0.7241, diversity=0.4507
  - NEGOTIATION: drift=0.1708, convergence=0.6200, diversity=0.5009
  - CLOSING: drift=0.1787, convergence=0.5764, diversity=0.5856

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### unknown:naive
- Runs: 1784
- Clean runs: 1784
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0176)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1835, C 0.2240, E 0.1429, A 0.1704, N 0.1679
- Relationship inconsistency: 0.1114
- Relationship shift rate: 0.2787
- Relationship overshoot rate: 0.1833
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2782
- Clean envelope violations: 2.2782
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
- Dialogue coherence: 0.0828
- Repetition rate: 0.0000
- Topic drift rate: 0.5412
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4016
- Commitment fulfillment rate: 0.6749
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1769, 0.1785]

- Phase-level quality:
  - OPENING: drift=0.1783, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1786, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1780, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1827, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Family Summary
### algorithmic_accountability:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1849 (+/- 0.0047)
- Clean persona drift MAE: 0.1849
- Per-trait absolute error: O 0.1983, C 0.2333, E 0.1291, A 0.2333, N 0.1300
- Relationship inconsistency: 0.1853
- Relationship shift rate: 0.2299
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1073
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3128
- Commitment fulfillment rate: 0.6792
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1803, 0.1894]

- Phase-level quality:
  - OPENING: drift=0.1785, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1807, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### algorithmic_accountability:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1888 (+/- 0.0052)
- Clean persona drift MAE: 0.1888
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1509, A 0.2333, N 0.1366
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1806
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
- Dialogue coherence: 0.0826
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2623
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1837, 0.194]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1903, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1867, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_acquisition:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1699 (+/- 0.0124)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1650, C 0.2259, E 0.1222, A 0.1511, N 0.1853
- Relationship inconsistency: 0.0483
- Relationship shift rate: 0.2584
- Relationship overshoot rate: 0.1875
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2694
- Clean envelope violations: 2.2694
- Structured action validity: 0.7667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0833
- Action-plan alignment: 0.9737
- Planned action coverage: 1.0000
- Action family convergence: 0.5278
- Role action diversity: 0.6042
- Negotiation uniqueness: 0.3311
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1039
- Repetition rate: 0.0093
- Topic drift rate: 0.5016
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4841
- Commitment fulfillment rate: 0.8542
- State trajectory variance: 0.0077
- Mean turns: 15.67
- Persona drift 95% CI: [0.1628, 0.1769]

- Phase-level quality:
  - OPENING: drift=0.1734, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1797, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1684, convergence=0.4778, diversity=0.6389
  - CLOSING: drift=0.1906, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_acquisition:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1823 (+/- 0.0117)
- Clean persona drift MAE: 0.1823
- Per-trait absolute error: O 0.2033, C 0.2257, E 0.1435, A 0.1550, N 0.1839
- Relationship inconsistency: 0.0281
- Relationship shift rate: 0.2001
- Relationship overshoot rate: 0.1500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3917
- Clean envelope violations: 2.3917
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
- Topic drift rate: 0.4946
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5042
- Commitment fulfillment rate: 0.8031
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1756, 0.1889]

- Phase-level quality:
  - OPENING: drift=0.1871, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1827, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1741, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1960, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1756 (+/- 0.0140)
- Clean persona drift MAE: 0.1756
- Per-trait absolute error: O 0.1560, C 0.2262, E 0.1638, A 0.1665, N 0.1654
- Relationship inconsistency: 0.0002
- Relationship shift rate: 0.2704
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1938
- Clean envelope violations: 2.1938
- Structured action validity: 0.5875
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3750
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.7333
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.2841
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1169
- Repetition rate: 0.0052
- Topic drift rate: 0.5284
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4086
- Commitment fulfillment rate: 0.7792
- State trajectory variance: 0.0068
- Mean turns: 16.50
- Persona drift 95% CI: [0.1687, 0.1824]

- Phase-level quality:
  - OPENING: drift=0.1736, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1784, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1793, convergence=0.6750, diversity=0.5000
  - CLOSING: drift=0.1822, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_crisis:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1835 (+/- 0.0119)
- Clean persona drift MAE: 0.1835
- Per-trait absolute error: O 0.1749, C 0.2353, E 0.1765, A 0.1656, N 0.1651
- Relationship inconsistency: 0.0295
- Relationship shift rate: 0.2776
- Relationship overshoot rate: 0.1969
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3062
- Clean envelope violations: 2.3062
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
- Dialogue coherence: 0.0817
- Repetition rate: 0.0000
- Topic drift rate: 0.5227
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4004
- Commitment fulfillment rate: 0.6089
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1776, 0.1893]

- Phase-level quality:
  - OPENING: drift=0.1824, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1818, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1828, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1890, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1570 (+/- 0.0026)
- Clean persona drift MAE: 0.1570
- Per-trait absolute error: O 0.1490, C 0.2025, E 0.1531, A 0.1325, N 0.1480
- Relationship inconsistency: 0.0921
- Relationship shift rate: 0.3231
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1243
- Repetition rate: 0.0000
- Topic drift rate: 0.4465
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4789
- Commitment fulfillment rate: 0.7560
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1545, 0.1596]

- Phase-level quality:
  - OPENING: drift=0.1717, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1721, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1468, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1685, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0079)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.1590, C 0.2261, E 0.1959, A 0.1487, N 0.1430
- Relationship inconsistency: 0.5088
- Relationship shift rate: 0.3829
- Relationship overshoot rate: 0.4800
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
- Dialogue coherence: 0.0906
- Repetition rate: 0.0000
- Topic drift rate: 0.5893
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4377
- Commitment fulfillment rate: 0.6369
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1668, 0.1823]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1784, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1538, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1821, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1857 (+/- 0.0024)
- Clean persona drift MAE: 0.1857
- Per-trait absolute error: O 0.1845, C 0.2800, E 0.1442, A 0.1616, N 0.1584
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3573
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1023
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4018
- Commitment fulfillment rate: 0.8695
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1834, 0.1881]

- Phase-level quality:
  - OPENING: drift=0.1866, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1867, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1960, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1761, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1907 (+/- 0.0023)
- Clean persona drift MAE: 0.1907
- Per-trait absolute error: O 0.1985, C 0.2800, E 0.1489, A 0.1679, N 0.1582
- Relationship inconsistency: 0.1148
- Relationship shift rate: 0.3440
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
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
- Topic drift rate: 0.5341
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3883
- Commitment fulfillment rate: 0.7459
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1884, 0.193]

- Phase-level quality:
  - OPENING: drift=0.1889, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1919, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1985, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1856, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1490 (+/- 0.0011)
- Clean persona drift MAE: 0.1490
- Per-trait absolute error: O 0.1370, C 0.2073, E 0.1150, A 0.1195, N 0.1660
- Relationship inconsistency: 0.3460
- Relationship shift rate: 0.3393
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1123
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4435
- Commitment fulfillment rate: 0.8234
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1479, 0.15]

- Phase-level quality:
  - OPENING: drift=0.1670, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1309, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1516, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1987, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1537 (+/- 0.0033)
- Clean persona drift MAE: 0.1537
- Per-trait absolute error: O 0.1440, C 0.2085, E 0.1318, A 0.1212, N 0.1630
- Relationship inconsistency: 0.0907
- Relationship shift rate: 0.3354
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
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
- Dialogue coherence: 0.0866
- Repetition rate: 0.0000
- Topic drift rate: 0.5536
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4242
- Commitment fulfillment rate: 0.5637
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1505, 0.1569]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1365, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1551, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2054, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1814 (+/- 0.0103)
- Clean persona drift MAE: 0.1814
- Per-trait absolute error: O 0.1678, C 0.2311, E 0.1465, A 0.1867, N 0.1748
- Relationship inconsistency: 0.0762
- Relationship shift rate: 0.3880
- Relationship overshoot rate: 0.3937
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3625
- Clean envelope violations: 2.3625
- Structured action validity: 0.4166
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3750
- Action-plan alignment: 0.9660
- Planned action coverage: 0.7500
- Action family convergence: 0.8750
- Role action diversity: 0.3849
- Negotiation uniqueness: 0.2061
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1017
- Repetition rate: 0.0000
- Topic drift rate: 0.5032
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3810
- Commitment fulfillment rate: 0.7395
- State trajectory variance: 0.0057
- Mean turns: 18.00
- Persona drift 95% CI: [0.1742, 0.1885]

- Phase-level quality:
  - OPENING: drift=0.1883, convergence=0.8750, diversity=0.2396
  - TENSION: drift=0.1778, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1840, convergence=0.6666, diversity=0.4667
  - CLOSING: drift=0.1931, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1848 (+/- 0.0111)
- Clean persona drift MAE: 0.1848
- Per-trait absolute error: O 0.1770, C 0.2300, E 0.1540, A 0.1877, N 0.1753
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5463
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4875
- Clean envelope violations: 2.4875
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
- Dialogue coherence: 0.0778
- Repetition rate: 0.0000
- Topic drift rate: 0.6023
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3518
- Commitment fulfillment rate: 0.6696
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1771, 0.1925]

- Phase-level quality:
  - OPENING: drift=0.1895, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1812, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1874, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1925, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1778 (+/- 0.0073)
- Clean persona drift MAE: 0.1778
- Per-trait absolute error: O 0.1200, C 0.3000, E 0.1074, A 0.1617, N 0.2000
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.2455
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1114
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4607
- Commitment fulfillment rate: 0.8333
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1707, 0.185]

- Phase-level quality:
  - OPENING: drift=0.1845, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1906, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1858, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1852, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1904 (+/- 0.0059)
- Clean persona drift MAE: 0.1904
- Per-trait absolute error: O 0.1416, C 0.3000, E 0.1237, A 0.1800, N 0.2067
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.3504
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0738
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4861
- Commitment fulfillment rate: 0.8375
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1846, 0.1962]

- Phase-level quality:
  - OPENING: drift=0.1961, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1923, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1840, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1935, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1548 (+/- 0.0063)
- Clean persona drift MAE: 0.1548
- Per-trait absolute error: O 0.1774, C 0.2350, E 0.0733, A 0.1416, N 0.1467
- Relationship inconsistency: 0.1239
- Relationship shift rate: 0.2527
- Relationship overshoot rate: 0.2812
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.7084
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.6250
- Action-plan alignment: 0.9693
- Planned action coverage: 1.0000
- Action family convergence: 0.7125
- Role action diversity: 0.4896
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1070
- Repetition rate: 0.0000
- Topic drift rate: 0.5114
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3916
- Commitment fulfillment rate: 0.6775
- State trajectory variance: 0.0054
- Mean turns: 16.50
- Persona drift 95% CI: [0.1505, 0.1591]

- Phase-level quality:
  - OPENING: drift=0.1610, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1643, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1651, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1601, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_contagion:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0125)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1804, C 0.2682, E 0.1020, A 0.1324, N 0.1467
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2707
- Relationship overshoot rate: 0.0563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2833
- Clean envelope violations: 2.2833
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
- Dialogue coherence: 0.0796
- Repetition rate: 0.0000
- Topic drift rate: 0.5625
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3803
- Commitment fulfillment rate: 0.5295
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1572, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1656, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1744, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1675, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1716, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1642 (+/- 0.0029)
- Clean persona drift MAE: 0.1642
- Per-trait absolute error: O 0.2070, C 0.1956, E 0.1043, A 0.1232, N 0.1906
- Relationship inconsistency: 0.0690
- Relationship shift rate: 0.3020
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0824
- Repetition rate: 0.0000
- Topic drift rate: 0.6477
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5108
- Commitment fulfillment rate: 0.9184
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1613, 0.167]

- Phase-level quality:
  - OPENING: drift=0.1734, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1647, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1700, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1600, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1696 (+/- 0.0043)
- Clean persona drift MAE: 0.1696
- Per-trait absolute error: O 0.2045, C 0.1975, E 0.1219, A 0.1294, N 0.1950
- Relationship inconsistency: 0.2755
- Relationship shift rate: 0.3261
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
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
- Dialogue coherence: 0.0700
- Repetition rate: 0.0000
- Topic drift rate: 0.7614
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4888
- Commitment fulfillment rate: 0.9445
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1655, 0.1738]

- Phase-level quality:
  - OPENING: drift=0.1763, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1697, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1811, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1632, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1680 (+/- 0.0043)
- Clean persona drift MAE: 0.1680
- Per-trait absolute error: O 0.1690, C 0.2033, E 0.1326, A 0.1153, N 0.2200
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2286
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1222
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4049
- Commitment fulfillment rate: 0.7167
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1638, 0.1722]

- Phase-level quality:
  - OPENING: drift=0.1934, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1613, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1681, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2011, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0024)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.1690, C 0.2165, E 0.1744, A 0.1170, N 0.2200
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3674
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0995
- Repetition rate: 0.0000
- Topic drift rate: 0.4107
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3645
- Commitment fulfillment rate: 0.7715
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.177, 0.1818]

- Phase-level quality:
  - OPENING: drift=0.1973, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1636, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1821, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2013, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_scandal:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1766 (+/- 0.0192)
- Clean persona drift MAE: 0.1766
- Per-trait absolute error: O 0.2245, C 0.2057, E 0.1441, A 0.1559, N 0.1529
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2736
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.3750
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9643
- Planned action coverage: 0.6363
- Action family convergence: 0.7084
- Role action diversity: 0.7257
- Negotiation uniqueness: 0.2806
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0832
- Repetition rate: 0.0000
- Topic drift rate: 0.4935
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4321
- Commitment fulfillment rate: 0.9184
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1633, 0.1899]

- Phase-level quality:
  - OPENING: drift=0.1722, convergence=0.3333, diversity=0.2500
  - TENSION: drift=0.1890, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1827, convergence=0.1666, diversity=0.3750
  - CLOSING: drift=0.1865, convergence=0.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_scandal:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1859 (+/- 0.0167)
- Clean persona drift MAE: 0.1859
- Per-trait absolute error: O 0.2429, C 0.2101, E 0.1603, A 0.1693, N 0.1469
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0809
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
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
- Dialogue coherence: 0.0651
- Repetition rate: 0.0000
- Topic drift rate: 0.6169
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4417
- Commitment fulfillment rate: 0.7396
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1743, 0.1975]

- Phase-level quality:
  - OPENING: drift=0.1800, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1958, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1828, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1939, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### generic:engine_structural
- Runs: 1816
- Clean runs: 1816
- Contaminated runs: 0
- Persona drift MAE: 0.1675 (+/- 0.0170)
- Clean persona drift MAE: 0.1675
- Per-trait absolute error: O 0.1651, C 0.2206, E 0.1193, A 0.1625, N 0.1699
- Relationship inconsistency: 0.0953
- Relationship shift rate: 0.2819
- Relationship overshoot rate: 0.2276
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0510
- Clean envelope violations: 2.0510
- Structured action validity: 0.6422
- Owner resolution rate: 0.9383
- Executed action contradiction: 0.0000
- State transition coherence: 0.9383
- Action feedback utilization: 0.2126
- Action-plan alignment: 0.9682
- Planned action coverage: 0.9285
- Action family convergence: 0.7084
- Role action diversity: 0.5104
- Negotiation uniqueness: 0.2795
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1064
- Repetition rate: 0.0024
- Topic drift rate: 0.5209
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4100
- Commitment fulfillment rate: 0.7803
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1667, 0.1683]

- Phase-level quality:
  - OPENING: drift=0.1705, convergence=0.7386, diversity=0.3567
  - TENSION: drift=0.1722, convergence=0.7241, diversity=0.4507
  - NEGOTIATION: drift=0.1708, convergence=0.6200, diversity=0.5009
  - CLOSING: drift=0.1787, convergence=0.5764, diversity=0.5856

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### generic:naive
- Runs: 1784
- Clean runs: 1784
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0176)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1835, C 0.2240, E 0.1429, A 0.1704, N 0.1679
- Relationship inconsistency: 0.1114
- Relationship shift rate: 0.2787
- Relationship overshoot rate: 0.1833
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2782
- Clean envelope violations: 2.2782
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
- Dialogue coherence: 0.0828
- Repetition rate: 0.0000
- Topic drift rate: 0.5412
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4016
- Commitment fulfillment rate: 0.6749
- State trajectory variance: 0.0000
- Mean turns: 0.00
- Persona drift 95% CI: [0.1769, 0.1785]

- Phase-level quality:
  - OPENING: drift=0.1783, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1786, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1780, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1827, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1801 (+/- 0.0046)
- Clean persona drift MAE: 0.1801
- Per-trait absolute error: O 0.1715, C 0.2419, E 0.1363, A 0.2157, N 0.1351
- Relationship inconsistency: 0.0413
- Relationship shift rate: 0.3090
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2250
- Clean envelope violations: 2.2250
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0943
- Repetition rate: 0.0208
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3450
- Commitment fulfillment rate: 0.6429
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1757, 0.1846]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1778, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1936, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1704, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### government_algorithm_failure:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1885 (+/- 0.0027)
- Clean persona drift MAE: 0.1885
- Per-trait absolute error: O 0.1740, C 0.2439, E 0.1682, A 0.2273, N 0.1295
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3323
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4250
- Clean envelope violations: 2.4250
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
- Dialogue coherence: 0.0762
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3079
- Commitment fulfillment rate: 0.7460
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1859, 0.1912]

- Phase-level quality:
  - OPENING: drift=0.1957, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1830, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1981, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1714, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### historical_injustice:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1701 (+/- 0.0040)
- Clean persona drift MAE: 0.1701
- Per-trait absolute error: O 0.1083, C 0.3000, E 0.1028, A 0.2392, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0488
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
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.1493
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0931
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4410
- Commitment fulfillment rate: 0.6583
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1661, 0.174]

- Phase-level quality:
  - OPENING: drift=0.1728, convergence=0.2500, diversity=0.1250
  - TENSION: drift=0.1713, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1710, convergence=0.7500, diversity=0.2916
  - CLOSING: drift=0.1920, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### historical_injustice:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0029)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1233, C 0.3000, E 0.1004, A 0.2583, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0683
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
- Dialogue coherence: 0.0741
- Repetition rate: 0.0000
- Topic drift rate: 0.3409
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3769
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1736, 0.1793]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1719, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1745, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2104, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1690 (+/- 0.0072)
- Clean persona drift MAE: 0.1690
- Per-trait absolute error: O 0.1267, C 0.2333, E 0.1466, A 0.1384, N 0.2000
- Relationship inconsistency: 0.0961
- Relationship shift rate: 0.3166
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8333
- Clean envelope violations: 1.8333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1185
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3635
- Commitment fulfillment rate: 0.9226
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.162, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1911, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1834, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1862, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1769, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1937 (+/- 0.0096)
- Clean persona drift MAE: 0.1937
- Per-trait absolute error: O 0.1667, C 0.2333, E 0.2162, A 0.1525, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0425
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4166
- Clean envelope violations: 2.4166
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
- Dialogue coherence: 0.0780
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3566
- Commitment fulfillment rate: 0.8393
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1843, 0.2031]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1950, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2044, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1861, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### infrastructure_decision:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1758 (+/- 0.0087)
- Clean persona drift MAE: 0.1758
- Per-trait absolute error: O 0.1500, C 0.2192, E 0.1471, A 0.1275, N 0.2350
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2551
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3802
- Negotiation uniqueness: 0.0757
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0956
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3864
- Commitment fulfillment rate: 0.9286
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1672, 0.1843]

- Phase-level quality:
  - OPENING: drift=0.1820, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1907, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1733, convergence=1.0000, diversity=0.2708
  - CLOSING: drift=0.1719, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### infrastructure_decision:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0063)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.1900, C 0.2054, E 0.1371, A 0.1148, N 0.2240
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.1590
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0626
- Repetition rate: 0.0000
- Topic drift rate: 0.4465
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3593
- Commitment fulfillment rate: 0.7750
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1681, 0.1804]

- Phase-level quality:
  - OPENING: drift=0.1808, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1897, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1794, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1609, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1755 (+/- 0.0030)
- Clean persona drift MAE: 0.1755
- Per-trait absolute error: O 0.2120, C 0.2036, E 0.1200, A 0.2130, N 0.1290
- Relationship inconsistency: 0.0638
- Relationship shift rate: 0.2823
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4114
- Commitment fulfillment rate: 0.8333
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1726, 0.1784]

- Phase-level quality:
  - OPENING: drift=0.2006, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1628, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1732, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2155, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1848 (+/- 0.0060)
- Clean persona drift MAE: 0.1848
- Per-trait absolute error: O 0.2120, C 0.2113, E 0.1522, A 0.2285, N 0.1200
- Relationship inconsistency: 0.1920
- Relationship shift rate: 0.3090
- Relationship overshoot rate: 0.2333
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
- Dialogue coherence: 0.0759
- Repetition rate: 0.0000
- Topic drift rate: 0.5893
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3771
- Commitment fulfillment rate: 0.6833
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1789, 0.1907]

- Phase-level quality:
  - OPENING: drift=0.2100, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1820, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2223, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1910 (+/- 0.0033)
- Clean persona drift MAE: 0.1910
- Per-trait absolute error: O 0.1865, C 0.1866, E 0.2097, A 0.1920, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1575
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1108
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4073
- Commitment fulfillment rate: 0.7113
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1877, 0.1942]

- Phase-level quality:
  - OPENING: drift=0.1943, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1954, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1916, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1931, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1968 (+/- 0.0048)
- Clean persona drift MAE: 0.1968
- Per-trait absolute error: O 0.1965, C 0.1919, E 0.2184, A 0.1967, N 0.1804
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1978
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0865
- Repetition rate: 0.0000
- Topic drift rate: 0.1932
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2822
- Commitment fulfillment rate: 0.7312
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1921, 0.2014]

- Phase-level quality:
  - OPENING: drift=0.1976, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2037, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1949, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1919, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_dispute:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0030)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.1430, C 0.2000, E 0.1210, A 0.2155, N 0.2105
- Relationship inconsistency: 0.1998
- Relationship shift rate: 0.3845
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3507
- Negotiation uniqueness: 0.0806
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0938
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4050
- Commitment fulfillment rate: 0.8661
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.175, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1936, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1726, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1757, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.2307, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_dispute:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0046)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1750, C 0.2088, E 0.1279, A 0.2325, N 0.2010
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2547
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5500
- Clean envelope violations: 2.5500
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
- Dialogue coherence: 0.0797
- Repetition rate: 0.0000
- Topic drift rate: 0.8393
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4318
- Commitment fulfillment rate: 0.7000
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1845, 0.1935]

- Phase-level quality:
  - OPENING: drift=0.1942, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1833, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1827, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2331, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_negotiation:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1396 (+/- 0.0052)
- Clean persona drift MAE: 0.1396
- Per-trait absolute error: O 0.1417, C 0.1052, E 0.0847, A 0.1667, N 0.2000
- Relationship inconsistency: 0.3839
- Relationship shift rate: 0.3696
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.4896
- Negotiation uniqueness: 0.1045
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4516
- Commitment fulfillment rate: 0.9286
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1346, 0.1447]

- Phase-level quality:
  - OPENING: drift=0.1559, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1600, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1445, convergence=0.7500, diversity=0.2916
  - CLOSING: drift=0.1588, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_negotiation:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1577 (+/- 0.0146)
- Clean persona drift MAE: 0.1577
- Per-trait absolute error: O 0.1800, C 0.1128, E 0.1167, A 0.1792, N 0.2000
- Relationship inconsistency: 0.4765
- Relationship shift rate: 0.5624
- Relationship overshoot rate: 0.4625
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
- Dialogue coherence: 0.0917
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4406
- Commitment fulfillment rate: 0.8958
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1434, 0.1721]

- Phase-level quality:
  - OPENING: drift=0.1641, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1625, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1534, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1665, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1628 (+/- 0.0062)
- Clean persona drift MAE: 0.1628
- Per-trait absolute error: O 0.2070, C 0.1744, E 0.1220, A 0.1426, N 0.1680
- Relationship inconsistency: 0.0688
- Relationship shift rate: 0.3146
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
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
- Dialogue coherence: 0.0826
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3461
- Commitment fulfillment rate: 0.7443
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1567, 0.1689]

- Phase-level quality:
  - OPENING: drift=0.1484, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1844, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1621, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1595, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0050)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.2140, C 0.1735, E 0.1684, A 0.1436, N 0.1613
- Relationship inconsistency: 0.1305
- Relationship shift rate: 0.4860
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2250
- Clean envelope violations: 2.2250
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
- Dialogue coherence: 0.0651
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3574
- Commitment fulfillment rate: 0.6667
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1673, 0.177]

- Phase-level quality:
  - OPENING: drift=0.1528, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1919, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1740, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1510 (+/- 0.0058)
- Clean persona drift MAE: 0.1510
- Per-trait absolute error: O 0.1550, C 0.2410, E 0.0626, A 0.1225, N 0.1740
- Relationship inconsistency: 0.0757
- Relationship shift rate: 0.3169
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1009
- Repetition rate: 0.0000
- Topic drift rate: 0.6607
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3680
- Commitment fulfillment rate: 0.8830
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1453, 0.1567]

- Phase-level quality:
  - OPENING: drift=0.1596, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1431, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1471, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1628 (+/- 0.0041)
- Clean persona drift MAE: 0.1628
- Per-trait absolute error: O 0.1820, C 0.2400, E 0.0935, A 0.1247, N 0.1740
- Relationship inconsistency: 0.2335
- Relationship shift rate: 0.5244
- Relationship overshoot rate: 0.4650
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
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
- Dialogue coherence: 0.0744
- Repetition rate: 0.0000
- Topic drift rate: 0.8392
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3417
- Commitment fulfillment rate: 0.7084
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1589, 0.1668]

- Phase-level quality:
  - OPENING: drift=0.1733, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1471, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1534, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2030, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0034)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.1850, C 0.1841, E 0.1386, A 0.1676, N 0.1316
- Relationship inconsistency: 0.1162
- Relationship shift rate: 0.3590
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1250
- Clean envelope violations: 2.1250
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0894
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3854
- Commitment fulfillment rate: 0.9021
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.158, 0.1647]

- Phase-level quality:
  - OPENING: drift=0.1800, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1496, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1699, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1528, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1646 (+/- 0.0045)
- Clean persona drift MAE: 0.1646
- Per-trait absolute error: O 0.1835, C 0.1939, E 0.1429, A 0.1764, N 0.1260
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4910
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2750
- Clean envelope violations: 2.2750
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
- Dialogue coherence: 0.0632
- Repetition rate: 0.0000
- Topic drift rate: 0.8636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3781
- Commitment fulfillment rate: 0.7222
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1601, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1815, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1500, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1741, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1550, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_rights:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1876 (+/- 0.0066)
- Clean persona drift MAE: 0.1876
- Per-trait absolute error: O 0.2350, C 0.2333, E 0.0832, A 0.1900, N 0.1967
- Relationship inconsistency: 0.1871
- Relationship shift rate: 0.3935
- Relationship overshoot rate: 0.2625
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4166
- Clean envelope violations: 2.4166
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.6632
- Negotiation uniqueness: 0.1482
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1058
- Repetition rate: 0.0312
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2468
- Commitment fulfillment rate: 1.0000
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1811, 0.1941]

- Phase-level quality:
  - OPENING: drift=0.1921, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1925, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1949, convergence=0.7500, diversity=0.3750
  - CLOSING: drift=0.1649, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate

### labor_rights:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1892 (+/- 0.0077)
- Clean persona drift MAE: 0.1892
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.0967, A 0.1792, N 0.1933
- Relationship inconsistency: 0.1150
- Relationship shift rate: 0.3947
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5834
- Clean envelope violations: 2.5834
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
- Dialogue coherence: 0.0644
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.2327
- Commitment fulfillment rate: 0.5625
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1816, 0.1967]

- Phase-level quality:
  - OPENING: drift=0.1923, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1993, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1996, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1742, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_governance:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1849 (+/- 0.0110)
- Clean persona drift MAE: 0.1849
- Per-trait absolute error: O 0.1876, C 0.2158, E 0.1754, A 0.1852, N 0.1606
- Relationship inconsistency: 0.2008
- Relationship shift rate: 0.3328
- Relationship overshoot rate: 0.3406
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3083
- Clean envelope violations: 2.3083
- Structured action validity: 0.7571
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9728
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0906
- Repetition rate: 0.0000
- Topic drift rate: 0.6705
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4604
- Commitment fulfillment rate: 0.9354
- State trajectory variance: 0.0030
- Mean turns: 16.50
- Persona drift 95% CI: [0.1772, 0.1925]

- Phase-level quality:
  - OPENING: drift=0.1860, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1978, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1877, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1803, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_governance:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.2020 (+/- 0.0117)
- Clean persona drift MAE: 0.2020
- Per-trait absolute error: O 0.2253, C 0.2228, E 0.2019, A 0.1973, N 0.1627
- Relationship inconsistency: 0.0625
- Relationship shift rate: 0.2898
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6375
- Clean envelope violations: 2.6375
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
- Dialogue coherence: 0.0669
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4380
- Commitment fulfillment rate: 0.5381
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1938, 0.2101]

- Phase-level quality:
  - OPENING: drift=0.1934, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2076, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2061, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1859, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1970 (+/- 0.0049)
- Clean persona drift MAE: 0.1970
- Per-trait absolute error: O 0.1850, C 0.2043, E 0.2014, A 0.1842, N 0.2100
- Relationship inconsistency: 0.0339
- Relationship shift rate: 0.3200
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.8333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0278
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4933
- Commitment fulfillment rate: 0.6286
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1922, 0.2018]

- Phase-level quality:
  - OPENING: drift=0.2080, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1962, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1881, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2496, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### platform_policy_enforcement:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2186 (+/- 0.0065)
- Clean persona drift MAE: 0.2186
- Per-trait absolute error: O 0.2020, C 0.2266, E 0.2303, A 0.2132, N 0.2210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3174
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0500
- Clean envelope violations: 3.0500
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
- Dialogue coherence: 0.0800
- Repetition rate: 0.0000
- Topic drift rate: 0.6071
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.5104
- Commitment fulfillment rate: 0.6429
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2122, 0.225]

- Phase-level quality:
  - OPENING: drift=0.2190, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2036, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1935, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2584, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_failure:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1447 (+/- 0.0055)
- Clean persona drift MAE: 0.1447
- Per-trait absolute error: O 0.1540, C 0.1830, E 0.0882, A 0.1925, N 0.1060
- Relationship inconsistency: 0.3660
- Relationship shift rate: 0.4764
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7500
- Clean envelope violations: 1.7500
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1955
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0976
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3791
- Commitment fulfillment rate: 0.4375
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1393, 0.1501]

- Phase-level quality:
  - OPENING: drift=0.1447, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1428, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1300, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1902, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### policy_failure:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0055)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1670, C 0.1932, E 0.1274, A 0.2120, N 0.1000
- Relationship inconsistency: 0.2752
- Relationship shift rate: 0.2298
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
- Dialogue coherence: 0.0776
- Repetition rate: 0.0000
- Topic drift rate: 0.1964
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3485
- Commitment fulfillment rate: 0.7500
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1545, 0.1653]

- Phase-level quality:
  - OPENING: drift=0.1575, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1484, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1378, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1973, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_negotiation:engine_structural
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1524 (+/- 0.0081)
- Clean persona drift MAE: 0.1524
- Per-trait absolute error: O 0.1373, C 0.1949, E 0.1141, A 0.1439, N 0.1721
- Relationship inconsistency: 0.1817
- Relationship shift rate: 0.3435
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8083
- Clean envelope violations: 1.8083
- Structured action validity: 0.7429
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1667
- Action-plan alignment: 0.9647
- Planned action coverage: 1.0000
- Action family convergence: 0.5972
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3247
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1219
- Repetition rate: 0.0000
- Topic drift rate: 0.4995
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4610
- Commitment fulfillment rate: 0.7215
- State trajectory variance: 0.0067
- Mean turns: 15.67
- Persona drift 95% CI: [0.1479, 0.157]

- Phase-level quality:
  - OPENING: drift=0.1491, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1601, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1579, convergence=0.6111, diversity=0.5278
  - CLOSING: drift=0.1650, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### policy_negotiation:naive
- Runs: 12
- Clean runs: 12
- Contaminated runs: 0
- Persona drift MAE: 0.1658 (+/- 0.0070)
- Clean persona drift MAE: 0.1658
- Per-trait absolute error: O 0.1541, C 0.2024, E 0.1390, A 0.1575, N 0.1762
- Relationship inconsistency: 0.3686
- Relationship shift rate: 0.4352
- Relationship overshoot rate: 0.4125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1305
- Clean envelope violations: 2.1305
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
- Dialogue coherence: 0.1044
- Repetition rate: 0.0000
- Topic drift rate: 0.5395
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4482
- Commitment fulfillment rate: 0.6131
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1619, 0.1698]

- Phase-level quality:
  - OPENING: drift=0.1596, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1635, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1704, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1642, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### post-disaster_recovery:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1646 (+/- 0.0084)
- Clean persona drift MAE: 0.1646
- Per-trait absolute error: O 0.1340, C 0.2328, E 0.1079, A 0.1431, N 0.2055
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2752
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0667
- Clean envelope violations: 2.0667
- Structured action validity: 0.7084
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1250
- Action-plan alignment: 0.9728
- Planned action coverage: 1.0000
- Action family convergence: 0.6083
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0988
- Repetition rate: 0.0000
- Topic drift rate: 0.5284
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4049
- Commitment fulfillment rate: 0.8215
- State trajectory variance: 0.0036
- Mean turns: 16.50
- Persona drift 95% CI: [0.1588, 0.1705]

- Phase-level quality:
  - OPENING: drift=0.1582, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1776, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1673, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1873, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### post-disaster_recovery:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1779 (+/- 0.0096)
- Clean persona drift MAE: 0.1779
- Per-trait absolute error: O 0.1683, C 0.2329, E 0.1388, A 0.1512, N 0.1981
- Relationship inconsistency: 0.0006
- Relationship shift rate: 0.2074
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3208
- Clean envelope violations: 2.3208
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
- Dialogue coherence: 0.0721
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3778
- Commitment fulfillment rate: 0.7652
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1712, 0.1845]

- Phase-level quality:
  - OPENING: drift=0.1653, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1882, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1816, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1941, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_crisis:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1648 (+/- 0.0030)
- Clean persona drift MAE: 0.1648
- Per-trait absolute error: O 0.1340, C 0.2422, E 0.1029, A 0.1640, N 0.1810
- Relationship inconsistency: 0.0011
- Relationship shift rate: 0.2240
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3177
- Negotiation uniqueness: 0.1456
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1203
- Repetition rate: 0.0000
- Topic drift rate: 0.1607
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3900
- Commitment fulfillment rate: 0.8403
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1619, 0.1677]

- Phase-level quality:
  - OPENING: drift=0.1660, convergence=1.0000, diversity=0.2708
  - TENSION: drift=0.1696, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1826, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1500, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### public_health_crisis:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1804 (+/- 0.0022)
- Clean persona drift MAE: 0.1804
- Per-trait absolute error: O 0.1540, C 0.2433, E 0.1568, A 0.1680, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2775
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
- Dialogue coherence: 0.0872
- Repetition rate: 0.0000
- Topic drift rate: 0.3215
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4092
- Commitment fulfillment rate: 0.3991
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1783, 0.1826]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1835, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1948, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1613, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_failure:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1863 (+/- 0.0220)
- Clean persona drift MAE: 0.1863
- Per-trait absolute error: O 0.1964, C 0.2110, E 0.1225, A 0.1989, N 0.2025
- Relationship inconsistency: 0.1911
- Relationship shift rate: 0.2907
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3292
- Clean envelope violations: 2.3292
- Structured action validity: 0.7084
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1250
- Action-plan alignment: 0.9739
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1224
- Repetition rate: 0.0000
- Topic drift rate: 0.6080
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3892
- Commitment fulfillment rate: 0.8195
- State trajectory variance: 0.0074
- Mean turns: 16.50
- Persona drift 95% CI: [0.171, 0.2015]

- Phase-level quality:
  - OPENING: drift=0.1851, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1929, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1875, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1925, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_health_failure:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1984 (+/- 0.0284)
- Clean persona drift MAE: 0.1984
- Per-trait absolute error: O 0.2181, C 0.2141, E 0.1455, A 0.2175, N 0.1967
- Relationship inconsistency: 0.0689
- Relationship shift rate: 0.2948
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7916
- Clean envelope violations: 2.7916
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
- Dialogue coherence: 0.0941
- Repetition rate: 0.0000
- Topic drift rate: 0.5625
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3766
- Commitment fulfillment rate: 0.7954
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1787, 0.2181]

- Phase-level quality:
  - OPENING: drift=0.1929, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2058, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1938, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1954, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1965 (+/- 0.0088)
- Clean persona drift MAE: 0.1965
- Per-trait absolute error: O 0.1933, C 0.2667, E 0.1000, A 0.2225, N 0.2000
- Relationship inconsistency: 0.0710
- Relationship shift rate: 0.1477
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
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
- Dialogue coherence: 0.1012
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4608
- Commitment fulfillment rate: 0.7917
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1879, 0.2051]

- Phase-level quality:
  - OPENING: drift=0.1881, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1911, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1950, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2000, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2066 (+/- 0.0078)
- Clean persona drift MAE: 0.2066
- Per-trait absolute error: O 0.2267, C 0.2667, E 0.1138, A 0.2592, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9167
- Clean envelope violations: 2.9167
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
- Dialogue coherence: 0.0824
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4824
- Commitment fulfillment rate: 0.7917
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1989, 0.2143]

- Phase-level quality:
  - OPENING: drift=0.1932, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1996, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1970, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2000, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy:engine_structural
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1627 (+/- 0.0107)
- Clean persona drift MAE: 0.1627
- Per-trait absolute error: O 0.1195, C 0.2093, E 0.1295, A 0.1653, N 0.1900
- Relationship inconsistency: 0.1057
- Relationship shift rate: 0.2978
- Relationship overshoot rate: 0.2812
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9167
- Clean envelope violations: 1.9167
- Structured action validity: 0.4167
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.1875
- Action-plan alignment: 0.9722
- Planned action coverage: 1.0000
- Action family convergence: 0.5854
- Role action diversity: 0.5938
- Negotiation uniqueness: 0.4026
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1108
- Repetition rate: 0.0000
- Topic drift rate: 0.5174
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4381
- Commitment fulfillment rate: 0.6928
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1575, 0.1679]

- Phase-level quality:
  - OPENING: drift=0.1701, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1702, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1688, convergence=0.4833, diversity=0.6459
  - CLOSING: drift=0.1593, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy:naive
- Runs: 16
- Clean runs: 16
- Contaminated runs: 0
- Persona drift MAE: 0.1756 (+/- 0.0085)
- Clean persona drift MAE: 0.1756
- Per-trait absolute error: O 0.1526, C 0.2176, E 0.1556, A 0.1645, N 0.1875
- Relationship inconsistency: 0.0194
- Relationship shift rate: 0.2552
- Relationship overshoot rate: 0.0844
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9875
- Clean envelope violations: 1.9875
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
- Dialogue coherence: 0.0870
- Repetition rate: 0.0000
- Topic drift rate: 0.5191
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4217
- Commitment fulfillment rate: 0.7247
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1714, 0.1798]

- Phase-level quality:
  - OPENING: drift=0.1783, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1812, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1787, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1613, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy_crisis:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1867 (+/- 0.0057)
- Clean persona drift MAE: 0.1867
- Per-trait absolute error: O 0.1410, C 0.2615, E 0.1841, A 0.1781, N 0.1688
- Relationship inconsistency: 0.0625
- Relationship shift rate: 0.2881
- Relationship overshoot rate: 0.2325
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3625
- Clean envelope violations: 2.3625
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1250
- Action-plan alignment: 0.9526
- Planned action coverage: 0.7046
- Action family convergence: 0.7916
- Role action diversity: 0.4109
- Negotiation uniqueness: 0.2378
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1069
- Repetition rate: 0.0000
- Topic drift rate: 0.6177
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4238
- Commitment fulfillment rate: 0.7583
- State trajectory variance: 0.0044
- Mean turns: 18.00
- Persona drift 95% CI: [0.1827, 0.1906]

- Phase-level quality:
  - OPENING: drift=0.1884, convergence=0.8334, diversity=0.3417
  - TENSION: drift=0.1938, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.1935, convergence=0.6666, diversity=0.4583
  - CLOSING: drift=0.2055, convergence=1.0000, diversity=0.3854

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy_crisis:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1987 (+/- 0.0059)
- Clean persona drift MAE: 0.1987
- Per-trait absolute error: O 0.1710, C 0.2600, E 0.1998, A 0.1775, N 0.1850
- Relationship inconsistency: 0.0596
- Relationship shift rate: 0.2901
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6500
- Clean envelope violations: 2.6500
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
- Dialogue coherence: 0.0900
- Repetition rate: 0.0000
- Topic drift rate: 0.6964
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4293
- Commitment fulfillment rate: 0.5212
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1945, 0.2028]

- Phase-level quality:
  - OPENING: drift=0.1991, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2000, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1982, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2096, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_compliance:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1525 (+/- 0.0070)
- Clean persona drift MAE: 0.1525
- Per-trait absolute error: O 0.1735, C 0.1948, E 0.0870, A 0.1387, N 0.1685
- Relationship inconsistency: 0.0629
- Relationship shift rate: 0.2396
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6083
- Clean envelope violations: 1.6083
- Structured action validity: 0.9000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9721
- Planned action coverage: 1.0000
- Action family convergence: 0.4791
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4415
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1091
- Repetition rate: 0.0000
- Topic drift rate: 0.4724
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3452
- Commitment fulfillment rate: 0.7979
- State trajectory variance: 0.0017
- Mean turns: 12.50
- Persona drift 95% CI: [0.1477, 0.1574]

- Phase-level quality:
  - OPENING: drift=0.1713, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1605, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1596, convergence=0.4166, diversity=0.7084
  - CLOSING: drift=0.1811, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_compliance:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1677 (+/- 0.0116)
- Clean persona drift MAE: 0.1677
- Per-trait absolute error: O 0.2150, C 0.2010, E 0.1074, A 0.1546, N 0.1605
- Relationship inconsistency: 0.2650
- Relationship shift rate: 0.3417
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1167
- Clean envelope violations: 2.1167
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
- Topic drift rate: 0.4335
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3583
- Commitment fulfillment rate: 0.4896
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1597, 0.1757]

- Phase-level quality:
  - OPENING: drift=0.1798, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1678, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1699, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1810, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_crisis:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1528 (+/- 0.0020)
- Clean persona drift MAE: 0.1528
- Per-trait absolute error: O 0.1680, C 0.2500, E 0.1034, A 0.1399, N 0.1029
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0633
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0250
- Clean envelope violations: 2.0250
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1190
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4240
- Commitment fulfillment rate: 0.6796
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1509, 0.1548]

- Phase-level quality:
  - OPENING: drift=0.1486, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1643, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1501, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1580, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_crisis:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1569 (+/- 0.0012)
- Clean persona drift MAE: 0.1569
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1100, A 0.1465, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2250
- Clean envelope violations: 2.2250
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
- Dialogue coherence: 0.0862
- Repetition rate: 0.0000
- Topic drift rate: 0.4659
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4270
- Commitment fulfillment rate: 0.5208
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1557, 0.158]

- Phase-level quality:
  - OPENING: drift=0.1510, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1633, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1540, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1686, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_decision:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1722 (+/- 0.0066)
- Clean persona drift MAE: 0.1722
- Per-trait absolute error: O 0.1460, C 0.2849, E 0.0861, A 0.1695, N 0.1744
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1260
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9685
- Planned action coverage: 1.0000
- Action family convergence: 0.8334
- Role action diversity: 0.4688
- Negotiation uniqueness: 0.2694
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1247
- Repetition rate: 0.0000
- Topic drift rate: 0.2175
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3817
- Commitment fulfillment rate: 0.7736
- State trajectory variance: 0.0042
- Mean turns: 12.50
- Persona drift 95% CI: [0.1676, 0.1767]

- Phase-level quality:
  - OPENING: drift=0.1797, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1584, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1794, convergence=0.6666, diversity=0.5416
  - CLOSING: drift=0.1901, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_decision:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1707 (+/- 0.0100)
- Clean persona drift MAE: 0.1707
- Per-trait absolute error: O 0.1260, C 0.2833, E 0.1004, A 0.1739, N 0.1700
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9167
- Clean envelope violations: 1.9167
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
- Dialogue coherence: 0.0976
- Repetition rate: 0.0000
- Topic drift rate: 0.2062
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3726
- Commitment fulfillment rate: 0.6979
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1638, 0.1776]

- Phase-level quality:
  - OPENING: drift=0.1830, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1620, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1741, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1918, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1627 (+/- 0.0060)
- Clean persona drift MAE: 0.1627
- Per-trait absolute error: O 0.1780, C 0.2051, E 0.1136, A 0.1527, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2911
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1156
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3620
- Commitment fulfillment rate: 0.8540
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1568, 0.1686]

- Phase-level quality:
  - OPENING: drift=0.1674, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1663, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1681, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1709, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0039)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.1970, C 0.2090, E 0.1378, A 0.1549, N 0.1618
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4164
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0830
- Repetition rate: 0.0000
- Topic drift rate: 0.7614
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4232
- Commitment fulfillment rate: 0.7882
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1683, 0.1759]

- Phase-level quality:
  - OPENING: drift=0.1738, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1757, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1787, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1765, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1486 (+/- 0.0132)
- Clean persona drift MAE: 0.1486
- Per-trait absolute error: O 0.1405, C 0.2205, E 0.1336, A 0.1282, N 0.1202
- Relationship inconsistency: 0.1554
- Relationship shift rate: 0.3276
- Relationship overshoot rate: 0.2812
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.7024
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9693
- Planned action coverage: 1.0000
- Action family convergence: 0.5250
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0847
- Repetition rate: 0.0000
- Topic drift rate: 0.5479
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4729
- Commitment fulfillment rate: 0.6900
- State trajectory variance: 0.0043
- Mean turns: 18.00
- Persona drift 95% CI: [0.1394, 0.1577]

- Phase-level quality:
  - OPENING: drift=0.1516, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1563, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1529, convergence=0.4667, diversity=0.6250
  - CLOSING: drift=0.1573, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### urban_policy:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1622 (+/- 0.0130)
- Clean persona drift MAE: 0.1622
- Per-trait absolute error: O 0.1588, C 0.2230, E 0.1696, A 0.1366, N 0.1228
- Relationship inconsistency: 0.0502
- Relationship shift rate: 0.3190
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
- Dialogue coherence: 0.0767
- Repetition rate: 0.0000
- Topic drift rate: 0.5373
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.4627
- Commitment fulfillment rate: 0.4955
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1532, 0.1711]

- Phase-level quality:
  - OPENING: drift=0.1601, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1648, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1616, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1686, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2019 (+/- 0.0018)
- Clean persona drift MAE: 0.2019
- Per-trait absolute error: O 0.2370, C 0.2252, E 0.1831, A 0.2015, N 0.1630
- Relationship inconsistency: 0.2797
- Relationship shift rate: 0.3342
- Relationship overshoot rate: 0.3563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7500
- Clean envelope violations: 2.7500
- Structured action validity: 0.8333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1308
- Repetition rate: 0.0000
- Topic drift rate: 0.4465
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3921
- Commitment fulfillment rate: 0.9022
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2002, 0.2037]

- Phase-level quality:
  - OPENING: drift=0.2128, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2028, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1993, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2147 (+/- 0.0044)
- Clean persona drift MAE: 0.2147
- Per-trait absolute error: O 0.2600, C 0.2288, E 0.2103, A 0.2087, N 0.1660
- Relationship inconsistency: 0.2859
- Relationship shift rate: 0.4888
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0858
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- Semantic identity consistency: 0.3805
- Commitment fulfillment rate: 0.6567
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2104, 0.2191]

- Phase-level quality:
  - OPENING: drift=0.2213, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2039, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2063, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Feature Attribution: What Drives Each Trait Score

### Openness (O) — Mean Error: 0.1741

| Feature | engine_structural (n=12424) | naive (n=12256) | Delta |
|---------|------|------|------|
| idea_count | 0.370 | 0.101 | +0.269 |
| hypothetical_count | 0.029 | 0.015 | +0.013 |
| unique_word_ratio | 0.798 | 0.816 | -0.018 |

Calibration: static

### Conscientiousness (C) — Mean Error: 0.2225

| Feature | engine_structural (n=12424) | naive (n=12256) | Delta |
|---------|------|------|------|
| planning_count | 0.990 | 0.725 | +0.265 |
| structure_marker_count | 0.009 | 0.022 | -0.013 |
| detail_count | 0.000 | 0.000 | +0.000 |
| goal_reference_count | 0.000 | 0.000 | +0.000 |
| correction_count | 0.000 | 0.000 | +0.000 |

Calibration: dynamic

### Extraversion (E) — Mean Error: 0.1319

| Feature | engine_structural (n=12424) | naive (n=12256) | Delta |
|---------|------|------|------|
| exclamation_count | 0.000 | 0.000 | +0.000 |
| question_count | 0.000 | 0.000 | +0.000 |
| word_count | 0.000 | 0.000 | +0.000 |
| filler_count | 0.000 | 0.000 | +0.000 |

Calibration: dynamic

### Agreeableness (A) — Mean Error: 0.1667

| Feature | engine_structural (n=12424) | naive (n=12256) | Delta |
|---------|------|------|------|
| acknowledgment_count | 0.061 | 0.194 | -0.133 |
| disagreement_count | 0.083 | 0.061 | +0.023 |
| negation_count | 1.453 | 2.043 | -0.589 |
| politeness_count | 0.000 | 0.000 | +0.000 |
| compliment_count | 0.000 | 0.000 | +0.000 |

Calibration: dynamic

### Neuroticism (N) — Mean Error: 0.1690

| Feature | engine_structural (n=12424) | naive (n=12256) | Delta |
|---------|------|------|------|
| hedge_count | 0.286 | 0.126 | +0.160 |
| self_doubt_count | 0.000 | 0.000 | -0.000 |
| reassurance_seeking_count | 0.000 | 0.001 | -0.001 |
| apology_count | 0.002 | 0.002 | -0.000 |
| emotional_word_count | 0.055 | 0.037 | +0.018 |

Calibration: dynamic


## Decision Driver Analysis

### engine_structural — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 185904 | sycophancy_risk | 185904 |
| TENSION | identity_consistency | 185904 | sycophancy_risk | 185904 |
| NEGOTIATION | identity_consistency | 216000 | sycophancy_risk | 216000 |
| CLOSING | identity_consistency | 114888 | sycophancy_risk | 114888 |


## Per-Archetype Trait Error

| Archetype | n | O | C | E | A | N | MAE | Top Failed Trait |
|-----------|---|---|---|---|---|---|-----|-----------------|
| Academic researcher studying crypto market failures | 96 | 0.358 | 0.194 | 0.023 | 0.093 | 0.196 | 0.173 | O |
| Activision Blizzard game studio creative lead | 74 | 0.319 | 0.120 | 0.140 | 0.025 | 0.205 | 0.162 | O |
| Activision Shareholder | 80 | 0.130 | 0.300 | 0.081 | 0.298 | 0.111 | 0.184 | C |
| Activist investor | 174 | 0.067 | 0.425 | 0.176 | 0.268 | 0.263 | 0.240 | C |
| Ad-Tech Engineer | 330 | 0.141 | 0.212 | 0.101 | 0.188 | 0.046 | 0.138 | C |
| Aerospace insurance underwriter repricing risk for the MAX fleet. | 120 | 0.070 | 0.261 | 0.070 | 0.199 | 0.095 | 0.139 | C |
| Affected mother of three | 104 | 0.158 | 0.036 | 0.125 | 0.318 | 0.102 | 0.148 | A |
| Aging local worker | 88 | 0.255 | 0.111 | 0.251 | 0.019 | 0.109 | 0.149 | O |
| Alameda Research quant who uncovered the balance sheet discrepancy | 96 | 0.457 | 0.256 | 0.174 | 0.041 | 0.095 | 0.205 | O |
| Alameda Research quantitative analyst who discovered balance sheet irregularities | 96 | 0.257 | 0.365 | 0.144 | 0.088 | 0.110 | 0.193 | C |
| Alameda quant analyst | 96 | 0.445 | 0.274 | 0.229 | 0.103 | 0.013 | 0.213 | O |
| All-Hands Moderator | 8 | 0.245 | 0.111 | 0.227 | 0.201 | 0.012 | 0.159 | O |
| Amazon Fitness lead | 62 | 0.257 | 0.322 | 0.064 | 0.105 | 0.196 | 0.189 | C |
| Apple Fitness+ product lead | 118 | 0.236 | 0.276 | 0.064 | 0.096 | 0.247 | 0.184 | C |
| Bahamas Securities Commission supervisor who approved FTX license | 96 | 0.055 | 0.143 | 0.205 | 0.184 | 0.002 | 0.118 | E |
| Bahamas regulatory officer | 96 | 0.255 | 0.107 | 0.210 | 0.188 | 0.091 | 0.170 | O |
| Bahamian financial regulatory officer who approved FTX license | 96 | 0.055 | 0.311 | 0.028 | 0.176 | 0.204 | 0.155 | C |
| Barista-Organizer working two jobs | 40 | 0.357 | 0.069 | 0.204 | 0.029 | 0.091 | 0.150 | O |
| Barista-organizer working two jobs | 40 | 0.307 | 0.095 | 0.047 | 0.028 | 0.186 | 0.133 | O |
| Barista-organizer working two jobs, recently written up for 'tardiness' after union meetings | 40 | 0.270 | 0.118 | 0.082 | 0.032 | 0.094 | 0.119 | O |
| Bootstrapped SaaS Founder | 218 | 0.243 | 0.131 | 0.181 | 0.115 | 0.117 | 0.157 | O |
| Brick-and-mortar bookstore owner (Congestion Zone) | 64 | 0.050 | 0.071 | 0.260 | 0.097 | 0.041 | 0.104 | E |
| CEO of a regional airline with 14 grounded MAX aircraft, facing significant financial losses. | 120 | 0.168 | 0.255 | 0.162 | 0.108 | 0.298 | 0.198 | N |
| CFO | 8 | 0.030 | 0.410 | 0.047 | 0.196 | 0.112 | 0.159 | C |
| CRE Lease Negotiator | 8 | 0.205 | 0.424 | 0.095 | 0.020 | 0.316 | 0.212 | C |
| CRE Lease Strategist | 8 | 0.130 | 0.389 | 0.183 | 0.301 | 0.204 | 0.241 | C |
| Cabin crew safety representative | 126 | 0.157 | 0.204 | 0.016 | 0.293 | 0.104 | 0.155 | A |
| Centrelink call center team lead | 128 | 0.070 | 0.383 | 0.144 | 0.189 | 0.008 | 0.159 | C |
| Centrelink call center worker | 128 | 0.070 | 0.401 | 0.252 | 0.090 | 0.190 | 0.200 | C |
| Centrelink call center worker processing appeals | 128 | 0.065 | 0.191 | 0.108 | 0.100 | 0.004 | 0.094 | C |
| Centrelink middle manager | 128 | 0.030 | 0.369 | 0.058 | 0.201 | 0.207 | 0.173 | C |
| Chair of the pilots' union safety committee, advocating for extensive pilot retraining. | 120 | 0.145 | 0.384 | 0.016 | 0.207 | 0.097 | 0.170 | C |
| City council president | 104 | 0.070 | 0.102 | 0.286 | 0.206 | 0.197 | 0.172 | E |
| City economic development director | 16 | 0.050 | 0.206 | 0.286 | 0.103 | 0.004 | 0.130 | E |
| City official overseeing Prop C implementation | 48 | 0.043 | 0.192 | 0.399 | 0.011 | 0.110 | 0.151 | E |
| City policymaker | 56 | 0.152 | 0.308 | 0.204 | 0.018 | 0.210 | 0.178 | C |
| Clawback-targeted foundation | 96 | 0.195 | 0.092 | 0.089 | 0.402 | 0.238 | 0.203 | A |
| Cloud Infrastructure Architect | 112 | 0.245 | 0.175 | 0.022 | 0.021 | 0.092 | 0.111 | O |
| Cloud Infrastructure Engineer at Microsoft | 160 | 0.105 | 0.355 | 0.060 | 0.162 | 0.298 | 0.196 | C |
| College student (account borrower) | 72 | 0.457 | 0.279 | 0.153 | 0.102 | 0.035 | 0.205 | O |
| Commercial Real Estate Analyst | 40 | 0.170 | 0.299 | 0.057 | 0.196 | 0.012 | 0.147 | C |
| Commercial real estate analyst | 40 | 0.157 | 0.422 | 0.107 | 0.209 | 0.383 | 0.256 | C |
| Committee member who championed $10B investment | 16 | 0.070 | 0.412 | 0.272 | 0.209 | 0.097 | 0.212 | C |
| Community Church Leader organizing relief efforts | 104 | 0.232 | 0.083 | 0.246 | 0.396 | 0.316 | 0.255 | A |
| Community Church Pastor | 104 | 0.145 | 0.024 | 0.265 | 0.419 | 0.104 | 0.191 | A |
| Community Manager (Facing Layoffs) | 16 | 0.233 | 0.057 | 0.173 | 0.386 | 0.070 | 0.184 | A |
| Community church leader | 104 | 0.245 | 0.116 | 0.217 | 0.400 | 0.303 | 0.256 | A |
| Community legal aid lawyer | 128 | 0.245 | 0.266 | 0.071 | 0.383 | 0.099 | 0.213 | A |
| Community organizer | 48 | 0.207 | 0.121 | 0.343 | 0.318 | 0.098 | 0.218 | E |
| Competing streamer's retention strategist | 72 | 0.320 | 0.100 | 0.378 | 0.198 | 0.283 | 0.256 | E |
| Competitor exchange | 96 | 0.070 | 0.449 | 0.248 | 0.314 | 0.185 | 0.253 | C |
| Congestion zone business owner | 64 | 0.072 | 0.324 | 0.086 | 0.102 | 0.014 | 0.120 | C |
| Construction CEO | 48 | 0.030 | 0.214 | 0.323 | 0.310 | 0.019 | 0.179 | E |
| Construction union leader | 138 | 0.065 | 0.218 | 0.291 | 0.191 | 0.153 | 0.184 | E |
| Consumer Privacy Advocate | 112 | 0.445 | 0.085 | 0.184 | 0.290 | 0.297 | 0.260 | O |
| Consumer rights advocate | 120 | 0.158 | 0.029 | 0.038 | 0.295 | 0.188 | 0.141 | A |
| Corporate Communications VP | 40 | 0.030 | 0.212 | 0.287 | 0.013 | 0.188 | 0.146 | E |
| Corporate communications managing public perception | 126 | 0.070 | 0.211 | 0.255 | 0.012 | 0.098 | 0.129 | E |
| Corporate labor relations specialist | 40 | 0.030 | 0.202 | 0.336 | 0.300 | 0.018 | 0.177 | E |
| Corporate real estate director locked into unfavorable lease | 16 | 0.130 | 0.281 | 0.067 | 0.078 | 0.103 | 0.132 | C |
| Creative Director at Activision | 80 | 0.432 | 0.070 | 0.189 | 0.030 | 0.214 | 0.187 | O |
| Creative Director at Activision Blizzard | 80 | 0.345 | 0.122 | 0.040 | 0.194 | 0.230 | 0.186 | O |
| Customer/Disability Advocate | 40 | 0.245 | 0.095 | 0.067 | 0.279 | 0.321 | 0.201 | N |
| DPA Enforcement Officer | 112 | 0.130 | 0.393 | 0.056 | 0.259 | 0.092 | 0.186 | C |
| Data Protection Consultant | 112 | 0.105 | 0.358 | 0.084 | 0.005 | 0.208 | 0.152 | C |
| Data Protection Officer | 218 | 0.104 | 0.334 | 0.038 | 0.139 | 0.290 | 0.181 | C |
| Deaf Software Engineer | 8 | 0.358 | 0.373 | 0.092 | 0.113 | 0.090 | 0.205 | C |
| Deaf software engineer | 8 | 0.345 | 0.405 | 0.118 | 0.115 | 0.105 | 0.218 | C |
| Deaf software engineer at Zoom | 8 | 0.220 | 0.395 | 0.085 | 0.118 | 0.097 | 0.183 | C |
| Debt collection contractor | 128 | 0.130 | 0.024 | 0.214 | 0.298 | 0.107 | 0.155 | A |
| Director of charitable foundation facing FTX donation clawback | 96 | 0.127 | 0.234 | 0.038 | 0.289 | 0.129 | 0.164 | A |
| Disability advocate customer | 40 | 0.245 | 0.031 | 0.063 | 0.377 | 0.321 | 0.207 | A |
| Disability rights advocate | 232 | 0.158 | 0.042 | 0.076 | 0.289 | 0.276 | 0.168 | A |
| Disability rights advocate for mobility-limited gig workers | 116 | 0.144 | 0.073 | 0.067 | 0.251 | 0.022 | 0.111 | A |
| Disabled Transit Riders Alliance Director | 64 | 0.170 | 0.034 | 0.044 | 0.404 | 0.092 | 0.149 | A |
| Disaster Response Vet | 94 | 0.070 | 0.359 | 0.131 | 0.295 | 0.094 | 0.190 | C |
| Disney+ retention strategist | 144 | 0.332 | 0.061 | 0.221 | 0.134 | 0.210 | 0.192 | O |
| EPA regional administrator | 104 | 0.158 | 0.296 | 0.033 | 0.009 | 0.097 | 0.119 | C |
| ER physician | 56 | 0.070 | 0.414 | 0.048 | 0.097 | 0.302 | 0.186 | C |
| ER physician treating 20+ medical emergencies per week from encampments | 52 | 0.065 | 0.421 | 0.064 | 0.081 | 0.284 | 0.183 | C |
| ER physician treating encampment-related emergencies | 48 | 0.070 | 0.415 | 0.035 | 0.097 | 0.296 | 0.183 | C |
| EU Parliament Aide | 112 | 0.115 | 0.284 | 0.093 | 0.176 | 0.197 | 0.173 | C |
| EU Policy Strategist | 106 | 0.218 | 0.296 | 0.042 | 0.028 | 0.076 | 0.132 | C |
| Elderly flat owner | 90 | 0.189 | 0.145 | 0.079 | 0.398 | 0.181 | 0.198 | A |
| Employee Resource Group Lead | 8 | 0.432 | 0.037 | 0.114 | 0.299 | 0.011 | 0.179 | O |
| Employment Lawyer | 8 | 0.130 | 0.411 | 0.033 | 0.008 | 0.212 | 0.159 | C |
| Engineering Director | 8 | 0.065 | 0.199 | 0.203 | 0.098 | 0.215 | 0.156 | N |
| Engineering Manager | 8 | 0.065 | 0.185 | 0.317 | 0.093 | 0.211 | 0.174 | E |
| Enterprise Tenant (Fortune 500 CFO) | 16 | 0.130 | 0.394 | 0.239 | 0.103 | 0.285 | 0.230 | C |
| Enterprise Tenant Representative | 10 | 0.130 | 0.318 | 0.064 | 0.102 | 0.107 | 0.144 | C |
| Environmental Justice Coalition Organizer | 64 | 0.457 | 0.083 | 0.029 | 0.204 | 0.292 | 0.213 | O |
| Esports League Organizer | 160 | 0.030 | 0.339 | 0.343 | 0.188 | 0.111 | 0.202 | E |
| European Union Aviation Safety Agency representative | 126 | 0.270 | 0.323 | 0.102 | 0.104 | 0.204 | 0.201 | C |
| Evacuee | 94 | 0.256 | 0.110 | 0.223 | 0.013 | 0.406 | 0.201 | N |
| Executive facing financial losses from grounded fleet | 126 | 0.130 | 0.253 | 0.214 | 0.096 | 0.002 | 0.139 | C |
| FAA Certification Lead | 120 | 0.055 | 0.355 | 0.037 | 0.185 | 0.001 | 0.127 | C |
| FAA advisory panel member advocating for crash victims | 126 | 0.370 | 0.066 | 0.183 | 0.013 | 0.202 | 0.167 | O |
| FDA Investigator | 30 | 0.157 | 0.400 | 0.020 | 0.197 | 0.297 | 0.214 | C |
| FDIC Field Examiner | 64 | 0.180 | 0.278 | 0.076 | 0.108 | 0.100 | 0.148 | C |
| FDIC Resolution Field Examiner | 32 | 0.130 | 0.312 | 0.052 | 0.286 | 0.000 | 0.156 | C |
| FTC Regulatory Attorney | 80 | 0.070 | 0.412 | 0.064 | 0.189 | 0.211 | 0.189 | C |
| FTC antitrust specialist | 74 | 0.130 | 0.235 | 0.036 | 0.092 | 0.095 | 0.118 | C |
| FTC regulator | 62 | 0.065 | 0.415 | 0.159 | 0.092 | 0.296 | 0.205 | C |
| FTX bankruptcy trustee overseeing asset recovery | 96 | 0.065 | 0.359 | 0.056 | 0.176 | 0.296 | 0.190 | C |
| Facing layoffs after building member relationships | 16 | 0.270 | 0.059 | 0.387 | 0.304 | 0.007 | 0.205 | E |
| Factory foreman | 88 | 0.130 | 0.089 | 0.064 | 0.021 | 0.207 | 0.102 | N |
| Fed Emergency Lending Officer | 32 | 0.130 | 0.293 | 0.060 | 0.193 | 0.200 | 0.175 | C |
| Fertility doctor | 48 | 0.157 | 0.321 | 0.087 | 0.306 | 0.198 | 0.214 | C |
| Fired Organizer (Buffalo original) | 40 | 0.470 | 0.201 | 0.251 | 0.085 | 0.212 | 0.244 | O |
| Fishing Cooperative Leader | 270 | 0.146 | 0.198 | 0.034 | 0.114 | 0.275 | 0.153 | N |
| Former FTX software engineer who built withdrawal systems | 96 | 0.370 | 0.189 | 0.176 | 0.106 | 0.010 | 0.170 | O |
| Former Plant Worker | 94 | 0.043 | 0.062 | 0.197 | 0.022 | 0.194 | 0.104 | E |
| Former executive team member | 16 | 0.170 | 0.176 | 0.356 | 0.019 | 0.192 | 0.183 | E |
| Former sub-postmaster convicted of theft | 24 | 0.130 | 0.291 | 0.117 | 0.232 | 0.400 | 0.234 | N |
| Former sub-postmaster wrongfully convicted | 36 | 0.130 | 0.223 | 0.055 | 0.225 | 0.146 | 0.156 | A |
| Formerly unhoused advocate | 56 | 0.207 | 0.107 | 0.222 | 0.197 | 0.107 | 0.168 | E |
| Formerly unhoused mentor in supportive housing | 48 | 0.130 | 0.034 | 0.118 | 0.299 | 0.102 | 0.137 | A |
| Fujitsu PR director | 24 | 0.067 | 0.118 | 0.302 | 0.207 | 0.200 | 0.179 | E |
| Fujitsu lead developer (2005-2012) | 40 | 0.403 | 0.078 | 0.096 | 0.354 | 0.101 | 0.206 | O |
| Fujitsu lead developer (Horizon team) | 20 | 0.155 | 0.344 | 0.085 | 0.326 | 0.200 | 0.222 | C |
| Game Engine Architect | 80 | 0.407 | 0.105 | 0.069 | 0.200 | 0.189 | 0.194 | O |
| Gaming Journalist | 80 | 0.333 | 0.033 | 0.139 | 0.110 | 0.100 | 0.143 | O |
| Gig platform policy lead | 112 | 0.145 | 0.450 | 0.301 | 0.200 | 0.078 | 0.235 | C |
| Gig worker advocate | 120 | 0.270 | 0.109 | 0.114 | 0.194 | 0.088 | 0.155 | O |
| Government data scientist | 128 | 0.370 | 0.421 | 0.155 | 0.103 | 0.007 | 0.211 | C |
| Government data scientist who flagged algorithm flaws | 128 | 0.345 | 0.391 | 0.034 | 0.193 | 0.096 | 0.212 | C |
| Government engineer overseeing recertification | 126 | 0.030 | 0.395 | 0.030 | 0.097 | 0.198 | 0.150 | C |
| Government labor inspector | 80 | 0.042 | 0.234 | 0.050 | 0.096 | 0.187 | 0.122 | C |
| HDB policymaker | 48 | 0.055 | 0.394 | 0.202 | 0.014 | 0.102 | 0.153 | C |
| HR Diversity Officer | 8 | 0.133 | 0.311 | 0.038 | 0.392 | 0.111 | 0.197 | A |
| Hochul Administration Representative | 64 | 0.255 | 0.016 | 0.406 | 0.017 | 0.186 | 0.176 | E |
| Homeless shelter resident | 56 | 0.062 | 0.103 | 0.060 | 0.201 | 0.090 | 0.103 | A |
| Homeowners association president | 56 | 0.243 | 0.214 | 0.068 | 0.186 | 0.209 | 0.184 | O |
| Hospital EMS coordinator | 64 | 0.030 | 0.383 | 0.149 | 0.205 | 0.096 | 0.173 | C |
| Hospital Procurement Director | 54 | 0.052 | 0.298 | 0.076 | 0.142 | 0.242 | 0.162 | C |
| Hospital procurement director who integrated Theranos devices | 24 | 0.065 | 0.310 | 0.123 | 0.106 | 0.036 | 0.128 | C |
| Immigration rights lawyer | 172 | 0.344 | 0.095 | 0.142 | 0.382 | 0.198 | 0.232 | A |
| Immigration rights lawyer pushing reform | 80 | 0.333 | 0.055 | 0.137 | 0.095 | 0.187 | 0.161 | O |
| In-house counsel managing liability exposure | 16 | 0.230 | 0.412 | 0.135 | 0.096 | 0.197 | 0.214 | C |
| Indie Game Developer | 80 | 0.320 | 0.027 | 0.051 | 0.185 | 0.106 | 0.138 | O |
| Indigenous elder affected by debt notice | 128 | 0.070 | 0.127 | 0.115 | 0.309 | 0.007 | 0.126 | A |
| Institutional investor monitoring Boeing's recovery | 126 | 0.043 | 0.302 | 0.105 | 0.198 | 0.005 | 0.130 | C |
| Insurance Underwriter | 120 | 0.060 | 0.230 | 0.049 | 0.096 | 0.199 | 0.127 | C |
| International Observer | 94 | 0.357 | 0.229 | 0.066 | 0.090 | 0.117 | 0.172 | O |
| Investigative journalist | 24 | 0.445 | 0.041 | 0.147 | 0.086 | 0.100 | 0.164 | O |
| Investigative reporter covering the recertification process | 126 | 0.457 | 0.095 | 0.105 | 0.214 | 0.002 | 0.175 | O |
| Investor who introduced others to FTX yield program | 96 | 0.042 | 0.037 | 0.152 | 0.088 | 0.285 | 0.121 | N |
| Jia Wei's fiancée | 90 | 0.050 | 0.409 | 0.212 | 0.210 | 0.178 | 0.212 | C |
| Journalist covering the FTX collapse for major financial publication | 96 | 0.470 | 0.120 | 0.150 | 0.101 | 0.201 | 0.208 | O |
| Korean Import Regulator | 94 | 0.157 | 0.342 | 0.077 | 0.014 | 0.194 | 0.157 | C |
| Lab technician at Theranos who knows the tests are unreliable | 24 | 0.207 | 0.338 | 0.161 | 0.101 | 0.348 | 0.231 | N |
| Labor advocate for laid-off staff | 16 | 0.370 | 0.040 | 0.379 | 0.190 | 0.103 | 0.216 | E |
| Labor union organizer | 232 | 0.185 | 0.193 | 0.180 | 0.093 | 0.184 | 0.167 | C |
| Labor union organizer advocating for full employment benefits | 116 | 0.319 | 0.359 | 0.180 | 0.042 | 0.282 | 0.236 | C |
| Language school operator | 88 | 0.075 | 0.321 | 0.055 | 0.102 | 0.050 | 0.121 | C |
| Language school operator profiting from training fees | 80 | 0.070 | 0.368 | 0.077 | 0.213 | 0.331 | 0.212 | C |
| Legacy Media CTO | 112 | 0.078 | 0.093 | 0.039 | 0.086 | 0.108 | 0.081 | N |
| Local Journalist Covering Labor | 40 | 0.270 | 0.030 | 0.085 | 0.178 | 0.012 | 0.115 | O |
| Local Mayor | 182 | 0.128 | 0.233 | 0.191 | 0.107 | 0.033 | 0.139 | C |
| Local Municipal Leader | 88 | 0.195 | 0.147 | 0.248 | 0.134 | 0.030 | 0.151 | E |
| Local elected official | 64 | 0.245 | 0.088 | 0.204 | 0.019 | 0.004 | 0.112 | O |
| Local journalist | 192 | 0.464 | 0.118 | 0.170 | 0.154 | 0.139 | 0.209 | O |
| Longtime customer and disability advocate worried about service consistency | 40 | 0.157 | 0.043 | 0.052 | 0.207 | 0.309 | 0.154 | N |
| Lyft driver | 120 | 0.085 | 0.020 | 0.143 | 0.079 | 0.129 | 0.091 | E |
| MP (Select Committee member) | 16 | 0.060 | 0.134 | 0.166 | 0.118 | 0.004 | 0.096 | E |
| MTA Capital Projects Director | 64 | 0.157 | 0.404 | 0.230 | 0.207 | 0.292 | 0.258 | C |
| MTA capital projects manager | 128 | 0.136 | 0.332 | 0.195 | 0.057 | 0.185 | 0.181 | C |
| Media ethics professor | 72 | 0.345 | 0.109 | 0.041 | 0.208 | 0.095 | 0.160 | O |
| Medical Journalist Investigating | 30 | 0.443 | 0.120 | 0.089 | 0.012 | 0.200 | 0.173 | O |
| Medical Researcher | 218 | 0.242 | 0.126 | 0.149 | 0.237 | 0.307 | 0.212 | N |
| Mental health counselor | 128 | 0.170 | 0.184 | 0.034 | 0.385 | 0.204 | 0.196 | A |
| Microsoft Azure gaming infrastructure engineer | 74 | 0.042 | 0.300 | 0.134 | 0.193 | 0.295 | 0.193 | C |
| Microsoft Teams Enterprise Sales Director | 8 | 0.170 | 0.045 | 0.347 | 0.225 | 0.305 | 0.218 | E |
| Microsoft Teams Sales Director | 8 | 0.258 | 0.075 | 0.346 | 0.215 | 0.018 | 0.182 | E |
| Minister for Postal Affairs | 24 | 0.070 | 0.324 | 0.140 | 0.097 | 0.200 | 0.166 | C |
| Ministry of Health official | 88 | 0.093 | 0.212 | 0.040 | 0.096 | 0.116 | 0.111 | C |
| Mt. Sinai ER Transport Coordinator | 64 | 0.055 | 0.250 | 0.103 | 0.196 | 0.103 | 0.141 | C |
| NYPD Traffic Chief | 64 | 0.130 | 0.299 | 0.099 | 0.297 | 0.192 | 0.203 | C |
| Netflix APAC content negotiator | 72 | 0.065 | 0.382 | 0.204 | 0.089 | 0.199 | 0.188 | C |
| Netflix anti-fraud engineer | 144 | 0.109 | 0.307 | 0.052 | 0.019 | 0.238 | 0.145 | C |
| Netflix customer service rep | 72 | 0.193 | 0.209 | 0.098 | 0.415 | 0.028 | 0.188 | A |
| Netflix investor relations | 72 | 0.030 | 0.397 | 0.350 | 0.208 | 0.284 | 0.254 | C |
| Netflix licensing negotiator (APAC) | 72 | 0.133 | 0.366 | 0.214 | 0.097 | 0.201 | 0.202 | C |
| Netflix regional content licensing negotiator | 72 | 0.067 | 0.383 | 0.254 | 0.117 | 0.175 | 0.199 | C |
| Nonprofit director | 56 | 0.357 | 0.188 | 0.234 | 0.282 | 0.296 | 0.272 | O |
| NordVPN product lead | 72 | 0.257 | 0.089 | 0.335 | 0.309 | 0.186 | 0.235 | E |
| NordVPN product manager | 72 | 0.257 | 0.121 | 0.277 | 0.188 | 0.295 | 0.228 | N |
| Nuclear Evacuee | 88 | 0.182 | 0.081 | 0.325 | 0.018 | 0.415 | 0.204 | N |
| Office Experience Lead | 8 | 0.060 | 0.287 | 0.173 | 0.096 | 0.188 | 0.161 | C |
| Outer-borough delivery driver | 128 | 0.149 | 0.208 | 0.063 | 0.097 | 0.090 | 0.121 | C |
| Outer-borough package delivery driver (UPS/FedEx) | 64 | 0.143 | 0.193 | 0.038 | 0.078 | 0.108 | 0.112 | C |
| Password-sharing SaaS founder | 72 | 0.395 | 0.032 | 0.290 | 0.128 | 0.184 | 0.206 | O |
| Patient who received incorrect blood test results | 24 | 0.120 | 0.252 | 0.063 | 0.305 | 0.226 | 0.193 | A |
| Patient with Incorrect Results | 30 | 0.057 | 0.133 | 0.037 | 0.207 | 0.297 | 0.146 | N |
| Patient with Misdiagnosis | 24 | 0.145 | 0.021 | 0.136 | 0.288 | 0.297 | 0.178 | N |
| Payroll Provider Account Manager | 32 | 0.043 | 0.130 | 0.243 | 0.011 | 0.200 | 0.125 | E |
| Pediatrician who identified lead poisoning in children | 104 | 0.370 | 0.391 | 0.138 | 0.200 | 0.200 | 0.260 | C |
| Pediatrician who identified lead poisoning spikes | 104 | 0.345 | 0.412 | 0.085 | 0.194 | 0.197 | 0.247 | C |
| Pediatrician who published research on spiking lead levels in children | 104 | 0.357 | 0.403 | 0.064 | 0.215 | 0.194 | 0.247 | C |
| Peloton CFO | 62 | 0.170 | 0.397 | 0.048 | 0.196 | 0.099 | 0.182 | C |
| Peloton community moderator | 62 | 0.070 | 0.130 | 0.274 | 0.204 | 0.008 | 0.137 | E |
| Peloton fitness instructor | 112 | 0.268 | 0.049 | 0.311 | 0.161 | 0.165 | 0.191 | E |
| Peloton hardware engineer | 62 | 0.370 | 0.173 | 0.072 | 0.010 | 0.098 | 0.145 | O |
| Peloton head instructor | 62 | 0.233 | 0.099 | 0.325 | 0.020 | 0.220 | 0.179 | E |
| Peloton warehouse manager | 56 | 0.030 | 0.100 | 0.023 | 0.019 | 0.208 | 0.076 | N |
| Physician Who Ordered Tests | 30 | 0.065 | 0.194 | 0.120 | 0.294 | 0.097 | 0.154 | A |
| Pilots' Union Safety Chair | 120 | 0.170 | 0.406 | 0.048 | 0.181 | 0.105 | 0.182 | C |
| Player Community Moderator | 80 | 0.207 | 0.100 | 0.264 | 0.400 | 0.306 | 0.255 | A |
| Post Office audit director | 40 | 0.230 | 0.417 | 0.184 | 0.200 | 0.218 | 0.250 | C |
| Post Office internal auditor | 20 | 0.058 | 0.348 | 0.184 | 0.095 | 0.000 | 0.137 | C |
| Post Office prosecuting lawyer | 24 | 0.130 | 0.200 | 0.139 | 0.301 | 0.000 | 0.154 | A |
| Professional gaming league organizer | 74 | 0.070 | 0.379 | 0.213 | 0.187 | 0.105 | 0.191 | C |
| Property agent | 48 | 0.220 | 0.034 | 0.384 | 0.206 | 0.020 | 0.173 | E |
| Property owner facing tenant default | 16 | 0.030 | 0.212 | 0.072 | 0.295 | 0.003 | 0.122 | A |
| Public Health Researcher | 88 | 0.333 | 0.136 | 0.170 | 0.189 | 0.091 | 0.184 | O |
| Regional Airline CEO | 120 | 0.168 | 0.264 | 0.167 | 0.117 | 0.299 | 0.203 | N |
| Regional HR Director | 40 | 0.030 | 0.204 | 0.048 | 0.289 | 0.107 | 0.136 | A |
| Remote Work Advocate | 8 | 0.445 | 0.181 | 0.072 | 0.311 | 0.299 | 0.262 | O |
| Renewables Lobbyist | 94 | 0.219 | 0.037 | 0.296 | 0.204 | 0.306 | 0.212 | N |
| Reporter investigating governance failures | 16 | 0.470 | 0.116 | 0.117 | 0.202 | 0.097 | 0.201 | O |
| Retail crypto trader who lost life savings in FTX yield program | 96 | 0.155 | 0.115 | 0.092 | 0.016 | 0.304 | 0.137 | N |
| Retail crypto trader who lost life savings in FTX's yield program | 96 | 0.232 | 0.199 | 0.045 | 0.086 | 0.303 | 0.173 | N |
| Retail crypto trader with locked savings | 96 | 0.130 | 0.162 | 0.039 | 0.103 | 0.306 | 0.148 | N |
| Risk analyst adjusting premiums for MAX operations | 126 | 0.070 | 0.238 | 0.034 | 0.195 | 0.102 | 0.128 | C |
| Rural council member | 24 | 0.070 | 0.118 | 0.280 | 0.109 | 0.200 | 0.155 | E |
| Rural factory owner | 172 | 0.230 | 0.372 | 0.089 | 0.191 | 0.092 | 0.195 | C |
| Rural factory owner dependent on program labor | 80 | 0.243 | 0.318 | 0.064 | 0.201 | 0.081 | 0.181 | C |
| SFPD liaison | 56 | 0.130 | 0.288 | 0.165 | 0.095 | 0.007 | 0.137 | C |
| SVB Board Member | 32 | 0.170 | 0.205 | 0.246 | 0.293 | 0.000 | 0.183 | A |
| SVB Commercial Banker | 64 | 0.070 | 0.399 | 0.085 | 0.086 | 0.250 | 0.178 | C |
| SVB Senior Commercial Banker | 32 | 0.030 | 0.362 | 0.015 | 0.073 | 0.200 | 0.136 | C |
| SVB Treasury Manager | 32 | 0.030 | 0.199 | 0.096 | 0.012 | 0.100 | 0.087 | C |
| SVB Treasury Risk Officer | 32 | 0.030 | 0.239 | 0.131 | 0.015 | 0.100 | 0.103 | C |
| SaaS Founder (Bootstrapped) | 112 | 0.345 | 0.127 | 0.193 | 0.095 | 0.192 | 0.190 | O |
| Safety advocate pushing for rigorous retraining | 126 | 0.132 | 0.413 | 0.021 | 0.210 | 0.098 | 0.175 | C |
| Seed-stage biotech CEO with 85 employees | 32 | 0.357 | 0.174 | 0.047 | 0.076 | 0.200 | 0.171 | O |
| Senior Centrelink manager overseeing the scheme | 128 | 0.042 | 0.310 | 0.146 | 0.313 | 0.004 | 0.163 | A |
| Senior Lab Technician at Theranos | 24 | 0.357 | 0.409 | 0.169 | 0.210 | 0.101 | 0.249 | C |
| Shift Supervisor (undecided) | 40 | 0.070 | 0.112 | 0.051 | 0.166 | 0.067 | 0.093 | A |
| Shrine Keeper | 94 | 0.230 | 0.310 | 0.133 | 0.396 | 0.106 | 0.235 | A |
| Single parent issued an incorrect $12K debt notice | 128 | 0.180 | 0.029 | 0.119 | 0.118 | 0.199 | 0.129 | N |
| Single parent sharing Netflix account with ex-spouse | 72 | 0.143 | 0.218 | 0.067 | 0.338 | 0.089 | 0.171 | A |
| Single parent sharing Netflix account with ex-spouse for children's access | 72 | 0.155 | 0.216 | 0.042 | 0.315 | 0.057 | 0.157 | A |
| Single parent sharing account with ex-spouse | 72 | 0.130 | 0.191 | 0.028 | 0.331 | 0.101 | 0.156 | A |
| Single parent with $12K incorrect debt notice | 128 | 0.143 | 0.115 | 0.085 | 0.228 | 0.300 | 0.174 | N |
| Single parent wrongly issued $12K debt notice | 128 | 0.155 | 0.210 | 0.116 | 0.146 | 0.298 | 0.185 | N |
| Single-mom DoorDash driver | 232 | 0.096 | 0.155 | 0.028 | 0.175 | 0.206 | 0.132 | N |
| Single-mom DoorDash driver needing schedule flexibility for childcare | 116 | 0.093 | 0.187 | 0.025 | 0.147 | 0.220 | 0.134 | N |
| Small Business Owner Subletter | 10 | 0.320 | 0.114 | 0.141 | 0.015 | 0.015 | 0.121 | O |
| Small business owner (congestion zone) | 64 | 0.108 | 0.128 | 0.267 | 0.166 | 0.355 | 0.205 | N |
| Small business owner (convenience store) facing 60% foot traffic decline | 48 | 0.142 | 0.279 | 0.068 | 0.093 | 0.198 | 0.156 | C |
| Small business owner (retail) | 56 | 0.130 | 0.196 | 0.110 | 0.075 | 0.006 | 0.103 | C |
| Small business owner whose storefront foot traffic dropped 60% due to nearby encampments | 52 | 0.182 | 0.170 | 0.034 | 0.065 | 0.101 | 0.110 | O |
| Small game studio founder | 74 | 0.379 | 0.035 | 0.057 | 0.103 | 0.191 | 0.153 | O |
| Small restaurant owner | 232 | 0.064 | 0.257 | 0.106 | 0.049 | 0.067 | 0.109 | C |
| Social Services Minister | 128 | 0.030 | 0.209 | 0.387 | 0.195 | 0.101 | 0.184 | E |
| Social worker at community legal center | 128 | 0.357 | 0.106 | 0.160 | 0.365 | 0.095 | 0.217 | A |
| Social worker counseling affected clients | 128 | 0.170 | 0.020 | 0.132 | 0.287 | 0.212 | 0.164 | A |
| SoftBank Investment Committee Member | 26 | 0.067 | 0.263 | 0.133 | 0.185 | 0.304 | 0.190 | N |
| South Korean recruiter | 88 | 0.157 | 0.023 | 0.386 | 0.204 | 0.093 | 0.173 | E |
| Startup CEO with frozen payroll | 32 | 0.370 | 0.219 | 0.117 | 0.076 | 0.200 | 0.196 | O |
| Startup CEO with frozen payroll funds | 32 | 0.357 | 0.103 | 0.240 | 0.093 | 0.200 | 0.199 | O |
| Startup CFO | 32 | 0.070 | 0.361 | 0.136 | 0.097 | 0.300 | 0.193 | C |
| State Budget Analyst | 104 | 0.030 | 0.183 | 0.041 | 0.109 | 0.196 | 0.112 | N |
| State Health Department Official | 104 | 0.130 | 0.310 | 0.078 | 0.007 | 0.303 | 0.166 | C |
| State budget analyst | 104 | 0.130 | 0.210 | 0.076 | 0.100 | 0.102 | 0.124 | C |
| State governor | 104 | 0.030 | 0.050 | 0.193 | 0.204 | 0.202 | 0.136 | A |
| State health director | 104 | 0.245 | 0.223 | 0.059 | 0.017 | 0.286 | 0.166 | N |
| State legislator | 120 | 0.055 | 0.317 | 0.218 | 0.015 | 0.216 | 0.164 | C |
| Store Manager (10-year veteran) | 40 | 0.070 | 0.354 | 0.161 | 0.191 | 0.191 | 0.193 | C |
| Store manager torn between corporate and staff | 40 | 0.055 | 0.272 | 0.068 | 0.206 | 0.121 | 0.145 | C |
| Store manager torn between corporate anti-union directives and loyalty to staff | 40 | 0.055 | 0.166 | 0.167 | 0.279 | 0.198 | 0.173 | A |
| Street outreach worker | 56 | 0.270 | 0.049 | 0.143 | 0.389 | 0.202 | 0.210 | A |
| Street outreach worker with deep client trust relationships | 48 | 0.135 | 0.129 | 0.283 | 0.403 | 0.209 | 0.232 | A |
| Street outreach worker with years of trust relationships among unhoused clients | 52 | 0.192 | 0.054 | 0.130 | 0.384 | 0.217 | 0.195 | A |
| Sublessor dependent on WeWork infrastructure | 16 | 0.308 | 0.094 | 0.045 | 0.021 | 0.196 | 0.133 | O |
| TEPCO Safety Engineer | 270 | 0.063 | 0.405 | 0.029 | 0.193 | 0.288 | 0.196 | C |
| Taiwanese factory line supervisor | 174 | 0.134 | 0.228 | 0.043 | 0.095 | 0.071 | 0.114 | C |
| Teams Talent Scout | 8 | 0.258 | 0.137 | 0.392 | 0.215 | 0.302 | 0.261 | E |
| Teamsters Local 814 Secretary-Treasurer | 64 | 0.060 | 0.081 | 0.216 | 0.309 | 0.092 | 0.152 | A |
| Tech Journalist | 32 | 0.470 | 0.066 | 0.083 | 0.311 | 0.000 | 0.186 | O |
| Tech executive | 56 | 0.030 | 0.408 | 0.072 | 0.195 | 0.291 | 0.199 | C |
| Tech industry lobbyist | 120 | 0.042 | 0.217 | 0.300 | 0.202 | 0.277 | 0.208 | E |
| Tech journalist investigating Robodebt | 128 | 0.470 | 0.315 | 0.153 | 0.022 | 0.102 | 0.212 | O |
| Theranos Board Member | 30 | 0.057 | 0.214 | 0.323 | 0.200 | 0.003 | 0.159 | E |
| Theranos Lab Technician | 30 | 0.257 | 0.276 | 0.131 | 0.098 | 0.009 | 0.154 | C |
| Theranos Legal Counsel | 54 | 0.174 | 0.209 | 0.165 | 0.235 | 0.168 | 0.190 | A |
| Theranos Quality Assurance Lead | 30 | 0.333 | 0.363 | 0.030 | 0.097 | 0.197 | 0.204 | C |
| Third-Party Union Buster Consultant | 40 | 0.130 | 0.316 | 0.198 | 0.292 | 0.088 | 0.205 | C |
| Trapped elderly owner | 48 | 0.318 | 0.164 | 0.139 | 0.211 | 0.227 | 0.212 | O |
| URA urban planner | 42 | 0.282 | 0.432 | 0.085 | 0.011 | 0.372 | 0.236 | C |
| US Congressional representative investigating crypto regulation | 96 | 0.157 | 0.041 | 0.273 | 0.129 | 0.193 | 0.159 | E |
| Uber executive | 120 | 0.065 | 0.417 | 0.310 | 0.116 | 0.299 | 0.241 | C |
| Uber/Lyft Driver Association Leader | 64 | 0.220 | 0.195 | 0.239 | 0.010 | 0.192 | 0.171 | E |
| Union rep for postal workers | 24 | 0.170 | 0.094 | 0.324 | 0.023 | 0.300 | 0.182 | E |
| Urban planner | 48 | 0.307 | 0.389 | 0.117 | 0.115 | 0.292 | 0.244 | C |
| VC General Partner | 64 | 0.264 | 0.043 | 0.232 | 0.191 | 0.350 | 0.216 | N |
| VC Investor (Tech Portfolio) | 112 | 0.170 | 0.033 | 0.265 | 0.206 | 0.097 | 0.154 | E |
| Victim Family Representative | 120 | 0.270 | 0.086 | 0.217 | 0.282 | 0.301 | 0.231 | N |
| Victim's daughter | 24 | 0.245 | 0.194 | 0.364 | 0.279 | 0.003 | 0.217 | E |
| Vietnamese Embassy liaison | 88 | 0.232 | 0.303 | 0.095 | 0.194 | 0.293 | 0.224 | C |
| Vietnamese technical intern (former) | 84 | 0.130 | 0.215 | 0.039 | 0.017 | 0.293 | 0.139 | N |
| Vietnamese technical intern with wage theft experience | 80 | 0.155 | 0.227 | 0.063 | 0.013 | 0.085 | 0.109 | C |
| Vietnamese trainee (wage theft victim) | 88 | 0.143 | 0.207 | 0.042 | 0.098 | 0.304 | 0.159 | N |
| Village council chair | 16 | 0.170 | 0.191 | 0.228 | 0.408 | 0.215 | 0.243 | A |
| Walgreens Partnership Manager | 54 | 0.108 | 0.250 | 0.330 | 0.054 | 0.148 | 0.178 | E |
| Warehouse logistics manager | 62 | 0.043 | 0.147 | 0.053 | 0.092 | 0.096 | 0.086 | C |
| Water Treatment Plant Operator | 104 | 0.070 | 0.285 | 0.180 | 0.101 | 0.102 | 0.148 | C |
| Water Treatment Plant Supervisor | 104 | 0.070 | 0.235 | 0.117 | 0.111 | 0.210 | 0.149 | C |
| Water treatment plant supervisor | 104 | 0.070 | 0.224 | 0.058 | 0.093 | 0.002 | 0.090 | C |
| WeWork Community Manager | 10 | 0.200 | 0.037 | 0.306 | 0.303 | 0.135 | 0.196 | E |
| WeWork Interim Legal Counsel | 10 | 0.040 | 0.203 | 0.177 | 0.089 | 0.187 | 0.139 | C |
| Xbox Platform Strategist | 80 | 0.093 | 0.206 | 0.270 | 0.109 | 0.016 | 0.139 | E |
| Young couple awaiting BTO flat | 48 | 0.270 | 0.313 | 0.046 | 0.132 | 0.298 | 0.212 | C |
| Young professional awaiting BTO flat | 42 | 0.191 | 0.245 | 0.031 | 0.077 | 0.066 | 0.122 | C |
| Young professional waiting for BTO | 48 | 0.120 | 0.224 | 0.089 | 0.028 | 0.197 | 0.131 | C |
| Zoom Engineering Manager | 8 | 0.050 | 0.260 | 0.112 | 0.093 | 0.197 | 0.143 | C |

## Phase-Level Behavioral Features (Engine Condition)

| Feature | OPENING | TENSION | NEGOTIATION | CLOSING | Delta (CLOSING - OPENING) |
|---------|------|------|------|------|------|
| acknowledgment_count | 0.024 | 0.034 | 0.014 | 0.018 | -0.006 |
| apology_count | 0.000 | 0.001 | 0.002 | 0.000 | +0.000 |
| disagreement_count | 0.027 | 0.040 | 0.036 | 0.019 | -0.008 |
| emotional_word_count | 0.035 | 0.009 | 0.010 | 0.028 | -0.007 |
| hedge_count | 0.132 | 0.041 | 0.143 | 0.125 | -0.008 |
| idea_count | 0.125 | 0.086 | 0.221 | 0.118 | -0.007 |
| negation_count | 0.442 | 0.784 | 0.504 | 0.501 | +0.059 |
| reassurance_seeking_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| self_doubt_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| unique_word_ratio | 0.943 | 0.948 | 0.946 | 0.950 | +0.008 |

## Scenario Difficulty vs Drift

| Scenario | Difficulty | Engine Drift | Naive Drift | Delta |
|----------|-----------|-------------|-------------|-------|
| 10actor | 0.76 | 0.1801 | 0.1886 | -0.0084 |
| 3actor | 0.76 | 0.1849 | 0.1889 | -0.0040 |
| 5actor | 0.76 | 0.1447 | 0.1599 | -0.0152 |
| 10actor | 0.59 | 0.1529 | 0.1568 | -0.0040 |
| 3actor | 0.59 | 0.1700 | 0.1679 | +0.0020 |
| 5actor | 0.59 | 0.1744 | 0.1735 | +0.0009 |
| 10actor | 0.76 | 0.1600 | 0.1617 | -0.0017 |
| 3actor | 0.76 | 0.1484 | 0.1740 | -0.0256 |
| 5actor | 0.76 | 0.1489 | 0.1619 | -0.0130 |
| 10actor | 0.76 | 0.1627 | 0.1721 | -0.0094 |
| 3actor | 0.76 | 0.1518 | 0.1683 | -0.0164 |
| 5actor | 0.76 | 0.1530 | 0.1671 | -0.0141 |
| 10actor | 1.00 | 0.1653 | 0.1704 | -0.0051 |
| 3actor | 1.00 | 0.2072 | 0.2264 | -0.0192 |
| 5actor | 1.00 | 0.1648 | 0.1804 | -0.0156 |
| 10actor | 1.00 | 0.1642 | 0.1697 | -0.0055 |
| 3actor | 1.00 | 0.1597 | 0.1705 | -0.0108 |
| 5actor | 1.00 | 0.1935 | 0.2012 | -0.0077 |
| 10actor | 0.68 | 0.1721 | 0.1800 | -0.0078 |
| 3actor | 0.68 | 0.1572 | 0.1757 | -0.0185 |
| 5actor | 0.68 | 0.1757 | 0.1743 | +0.0015 |
| 10actor | 0.59 | 0.1628 | 0.1721 | -0.0093 |
| 3actor | 0.59 | 0.1876 | 0.1892 | -0.0015 |
| 5actor | 0.59 | 0.1510 | 0.1629 | -0.0118 |
| 10actor | 0.57 | 0.1796 | 0.1970 | -0.0174 |
| 3actor | 0.57 | 0.1749 | 0.1777 | -0.0028 |
| 5actor | 0.57 | 0.1549 | 0.1722 | -0.0173 |
| 10actor | 0.68 | 0.1741 | 0.1914 | -0.0173 |
| 3actor | 0.68 | 0.1956 | 0.2126 | -0.0169 |
| 5actor | 0.68 | 0.1970 | 0.2186 | -0.0216 |
| 10actor | 0.82 | 0.1615 | 0.1743 | -0.0128 |
| 3actor | 0.82 | 0.1670 | 0.1666 | +0.0003 |
| 5actor | 0.82 | 0.1357 | 0.1500 | -0.0144 |
| 10actor | 0.91 | 0.1668 | 0.1775 | -0.0106 |
| 3actor | 0.91 | 0.1681 | 0.1842 | -0.0161 |
| 5actor | 0.91 | 0.1490 | 0.1537 | -0.0048 |
| 10actor | 0.91 | 0.1690 | 0.1793 | -0.0104 |
| 3actor | 0.91 | 0.1502 | 0.1778 | -0.0276 |
| 5actor | 0.91 | 0.1647 | 0.1786 | -0.0139 |
| 10actor | 0.48 | 0.1816 | 0.1942 | -0.0126 |
| 3actor | 0.48 | 0.1965 | 0.2066 | -0.0101 |
| 5actor | 0.48 | 0.1919 | 0.2031 | -0.0112 |
| 10actor | 0.82 | 0.1614 | 0.1646 | -0.0032 |
| 3actor | 0.82 | 0.1396 | 0.1577 | -0.0181 |
| 5actor | 0.82 | 0.1780 | 0.1890 | -0.0110 |
| 10actor | 0.59 | 0.1608 | 0.1720 | -0.0113 |
| 3actor | 0.59 | 0.1489 | 0.1598 | -0.0109 |
| 5actor | 0.59 | 0.1680 | 0.1794 | -0.0114 |
| 10actor | 1.00 | 0.1712 | 0.1743 | -0.0032 |
| 3actor | 1.00 | 0.1778 | 0.1904 | -0.0126 |
| 5actor | 1.00 | 0.1916 | 0.1952 | -0.0036 |
| 10actor | 0.85 | 0.1910 | 0.1968 | -0.0058 |
| 3actor | 0.85 | 0.1701 | 0.1764 | -0.0063 |
| 5actor | 0.85 | 0.1755 | 0.1848 | -0.0093 |
| 10actor | 1.00 | 0.1720 | 0.1774 | -0.0054 |
| 3actor | 1.00 | 0.1954 | 0.1950 | +0.0004 |
| 5actor | 1.00 | 0.1573 | 0.1745 | -0.0173 |
| 10actor | 0.66 | 0.1857 | 0.1907 | -0.0049 |
| 3actor | 0.66 | 0.1690 | 0.1937 | -0.0247 |
| 5actor | 0.66 | 0.2020 | 0.2147 | -0.0128 |

## Influence Attribution: Who Drove Key Decisions?

### Decision Points Detected: 14381 across 2056 engine runs (mean 6.99/run)

| Decision Type | Count | Mean Influence Concentration |
|---------------|-------|------------------------------|
| trait_drift_spike | 14171 | 0.444 |
| sentiment_flip | 210 | 0.455 |

### Sample Decision Traces

> **actor_1** at turn 11 (TENSION): trait_drift_spike
> actor_1 drift spike -0.102 (→0.135)
> - actor_8: score=0.405 — 
> - actor_9: score=0.324 — 
> actor_1: actor_1 drift spike -0.102 (→0.135). actor_8 (score=0.40, key signal: trait pull) actor_9 (score=0.32, key signal: trait pull)

> **actor_1** at turn 11 (TENSION): trait_drift_spike
> actor_1 drift spike -0.102 (→0.135)
> - actor_8: score=0.405 — 
> - actor_9: score=0.324 — 
> actor_1: actor_1 drift spike -0.102 (→0.135). actor_8 (score=0.40, key signal: trait pull) actor_9 (score=0.32, key signal: trait pull)

> **actor_1** at turn 11 (TENSION): trait_drift_spike
> actor_1 drift spike -0.102 (→0.135)
> - actor_8: score=0.405 — 
> - actor_9: score=0.324 — 
> actor_1: actor_1 drift spike -0.102 (→0.135). actor_8 (score=0.40, key signal: trait pull) actor_9 (score=0.32, key signal: trait pull)


## Statistical Significance: engine_structural vs naive

Bonferroni-corrected threshold: p < 0.0042 (12 comparisons)

| Metric | engine_structural (n=2056) | naive (n=2024) | Delta | p (Welch) | p (paired) | Cohen's d | Effect | Sig? |
|--------|----|----|----|----|----|----|----|----|
| Persona Drift MAE | 0.1678 | 0.1780 | -0.0103 | 0.0000 | 0.0000 | -0.594 | medium | Yes |
| Relationship Inconsistency | 0.0951 | 0.1104 | -0.0153 | 0.0236 | 0.7361 | -0.071 | negligible | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | 1.0000 | +0.000 | negligible | No |
| Envelope Violations | 2.0568 | 2.2830 | -0.2262 | 0.0000 | 0.0013 | -0.603 | medium | Yes |
| Action Convergence | 0.7091 | 0.0000 | +0.7091 | 0.0000 | 0.0000 | +4.188 | large | Yes |
| Role Diversity | 0.5103 | 0.0000 | +0.5103 | 0.0000 | 0.0000 | +3.879 | large | Yes |
| Dialogue Coherence | 0.1064 | 0.0827 | +0.0238 | 0.0000 | 0.0000 | +1.335 | large | Yes |
| Repetition Rate | 0.0024 | 0.0000 | +0.0024 | 0.0000 | 0.0825 | +0.213 | small | Yes |
| Topic Drift Rate | 0.5205 | 0.5413 | -0.0208 | 0.0028 | 0.4195 | -0.094 | negligible | Yes |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | 1.0000 | +0.000 | negligible | No |
| Semantic Identity Consistency | 0.4105 | 0.4018 | +0.0087 | 0.0001 | 0.0149 | +0.127 | negligible | Yes |
| Commitment Fulfillment Rate | 0.7811 | 0.6750 | +0.1061 | 0.0000 | 0.0000 | +0.487 | small | Yes |

### Win Rate Summary (per-script comparison)

| Metric | engine_structural wins | Total scripts |
|--------|----|----|
| Persona Drift MAE | 55/60 | 60 |
| Relationship Inconsistency | 22/60 | 60 |
| Commitment Contradiction | 0/60 | 60 |
| Envelope Violations | 51/60 | 60 |
| Action Convergence | 0/60 | 60 |
| Role Diversity | 60/60 | 60 |
| Dialogue Coherence | 59/60 | 60 |
| Repetition Rate | 0/60 | 60 |
| Topic Drift Rate | 37/60 | 60 |
| Fallback Rate | 0/60 | 60 |
| Semantic Identity Consistency | 38/60 | 60 |
| Commitment Fulfillment Rate | 44/60 | 60 |

### Per-Scenario Drift Comparison: engine_structural vs naive

| Scenario | engine_structural drift | naive drift | Delta | Winner |
|----------|----|----|----|----|
| 10actor | 0.1801 | 0.1886 | -0.0084 | engine_structural |
| 3actor | 0.1849 | 0.1889 | -0.0040 | engine_structural |
| 5actor | 0.1447 | 0.1599 | -0.0152 | engine_structural |
| 10actor | 0.1529 | 0.1568 | -0.0040 | engine_structural |
| 3actor | 0.1700 | 0.1679 | +0.0020 | naive |
| 5actor | 0.1744 | 0.1735 | +0.0009 | naive |
| 10actor | 0.1600 | 0.1617 | -0.0017 | engine_structural |
| 3actor | 0.1484 | 0.1740 | -0.0256 | engine_structural |
| 5actor | 0.1489 | 0.1619 | -0.0130 | engine_structural |
| 10actor | 0.1627 | 0.1721 | -0.0094 | engine_structural |
| 3actor | 0.1518 | 0.1683 | -0.0164 | engine_structural |
| 5actor | 0.1530 | 0.1671 | -0.0141 | engine_structural |
| 10actor | 0.1653 | 0.1704 | -0.0051 | engine_structural |
| 3actor | 0.2072 | 0.2264 | -0.0192 | engine_structural |
| 5actor | 0.1648 | 0.1804 | -0.0156 | engine_structural |
| 10actor | 0.1642 | 0.1697 | -0.0055 | engine_structural |
| 3actor | 0.1597 | 0.1705 | -0.0108 | engine_structural |
| 5actor | 0.1935 | 0.2012 | -0.0077 | engine_structural |
| 10actor | 0.1721 | 0.1800 | -0.0078 | engine_structural |
| 3actor | 0.1572 | 0.1757 | -0.0185 | engine_structural |
| 5actor | 0.1757 | 0.1743 | +0.0015 | naive |
| 10actor | 0.1628 | 0.1721 | -0.0093 | engine_structural |
| 3actor | 0.1876 | 0.1892 | -0.0015 | engine_structural |
| 5actor | 0.1510 | 0.1629 | -0.0118 | engine_structural |
| 10actor | 0.1796 | 0.1970 | -0.0174 | engine_structural |
| 3actor | 0.1749 | 0.1777 | -0.0028 | engine_structural |
| 5actor | 0.1549 | 0.1722 | -0.0173 | engine_structural |
| 10actor | 0.1741 | 0.1914 | -0.0173 | engine_structural |
| 3actor | 0.1956 | 0.2126 | -0.0169 | engine_structural |
| 5actor | 0.1970 | 0.2186 | -0.0216 | engine_structural |
| 10actor | 0.1615 | 0.1743 | -0.0128 | engine_structural |
| 3actor | 0.1670 | 0.1666 | +0.0003 | naive |
| 5actor | 0.1357 | 0.1500 | -0.0144 | engine_structural |
| 10actor | 0.1668 | 0.1775 | -0.0106 | engine_structural |
| 3actor | 0.1681 | 0.1842 | -0.0161 | engine_structural |
| 5actor | 0.1490 | 0.1537 | -0.0048 | engine_structural |
| 10actor | 0.1690 | 0.1793 | -0.0104 | engine_structural |
| 3actor | 0.1502 | 0.1778 | -0.0276 | engine_structural |
| 5actor | 0.1647 | 0.1786 | -0.0139 | engine_structural |
| 10actor | 0.1816 | 0.1942 | -0.0126 | engine_structural |
| 3actor | 0.1965 | 0.2066 | -0.0101 | engine_structural |
| 5actor | 0.1919 | 0.2031 | -0.0112 | engine_structural |
| 10actor | 0.1614 | 0.1646 | -0.0032 | engine_structural |
| 3actor | 0.1396 | 0.1577 | -0.0181 | engine_structural |
| 5actor | 0.1780 | 0.1890 | -0.0110 | engine_structural |
| 10actor | 0.1608 | 0.1720 | -0.0113 | engine_structural |
| 3actor | 0.1489 | 0.1598 | -0.0109 | engine_structural |
| 5actor | 0.1680 | 0.1794 | -0.0114 | engine_structural |
| 10actor | 0.1712 | 0.1743 | -0.0032 | engine_structural |
| 3actor | 0.1778 | 0.1904 | -0.0126 | engine_structural |
| 5actor | 0.1916 | 0.1952 | -0.0036 | engine_structural |
| 10actor | 0.1910 | 0.1968 | -0.0058 | engine_structural |
| 3actor | 0.1701 | 0.1764 | -0.0063 | engine_structural |
| 5actor | 0.1755 | 0.1848 | -0.0093 | engine_structural |
| 10actor | 0.1720 | 0.1774 | -0.0054 | engine_structural |
| 3actor | 0.1954 | 0.1950 | +0.0004 | naive |
| 5actor | 0.1573 | 0.1745 | -0.0173 | engine_structural |
| 10actor | 0.1857 | 0.1907 | -0.0049 | engine_structural |
| 3actor | 0.1690 | 0.1937 | -0.0247 | engine_structural |
| 5actor | 0.2020 | 0.2147 | -0.0128 | engine_structural |

## Per-Trait Error: engine_structural vs naive

Bonferroni-corrected threshold: p < 0.010 (5 comparisons)

| Trait | Engine | Naive | Delta | p-value | Cohen's d | Effect | Calibration | Sig? |
|-------|--------|-------|-------|---------|-----------|--------|-------------|------|
| O | 0.1650 | 0.1834 | -0.0184 | 0.0000 | -0.469 | small | Static | Yes |
| C | 0.2207 | 0.2243 | -0.0036 | 0.0154 | -0.101 | negligible | Dynamic | No |
| E | 0.1203 | 0.1438 | -0.0235 | 0.0000 | -0.611 | medium | Dynamic | Yes |
| A | 0.1628 | 0.1706 | -0.0079 | 0.0000 | -0.200 | negligible | Dynamic | Yes |
| N | 0.1700 | 0.1681 | +0.0019 | 0.1842 | +0.055 | negligible | Dynamic | No |

## Actor Count x Condition Scaling

| Actors | Condition | n | Drift | Envelope | Convergence | Diversity | Coherence | Repetition | Topic Drift |
|--------|-----------|---|-------|----------|-------------|-----------|-----------|------------|-------------|
| 3 | engine_structural | 688 | 0.1710 | 2.0087 | 0.6570 | 0.6364 | 0.1105 | 0.0020 | 0.5165 |
| 3 | naive | 672 | 0.1827 | 2.3001 | 0.0000 | 0.0000 | 0.0877 | 0.0000 | 0.5161 |
| 5 | engine_structural | 664 | 0.1646 | 2.0021 | 0.6504 | 0.5608 | 0.1049 | 0.0030 | 0.4506 |
| 5 | naive | 656 | 0.1756 | 2.2220 | 0.0000 | 0.0000 | 0.0791 | 0.0000 | 0.5084 |
| 10 | engine_structural | 704 | 0.1675 | 2.1554 | 0.8155 | 0.3394 | 0.1038 | 0.0021 | 0.5902 |
| 10 | naive | 696 | 0.1758 | 2.3241 | 0.0000 | 0.0000 | 0.0812 | 0.0000 | 0.5965 |

### Drift Slope (10-actor minus 3-actor):

- engine_structural: -0.0035
- naive: -0.0069
