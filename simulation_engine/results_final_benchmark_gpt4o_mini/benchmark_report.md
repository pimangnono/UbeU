# Simulation Benchmark Report

## Suite Config
- Total runs: 360
- Conditions: engine_dialogue_only, naive, naive_informed
- Script ids: australia_robodebt_10actor, australia_robodebt_3actor, australia_robodebt_5actor, boeing_737max_return_10actor, boeing_737max_return_3actor, boeing_737max_return_5actor, california_ab5_gig_classification_10actor, california_ab5_gig_classification_3actor, california_ab5_gig_classification_5actor, eu_gdpr_implementation_10actor, eu_gdpr_implementation_3actor, eu_gdpr_implementation_5actor, flint_water_crisis_10actor, flint_water_crisis_3actor, flint_water_crisis_5actor, ftx_collapse_10actor, ftx_collapse_3actor, ftx_collapse_5actor, fukushima_nuclear_restart_10actor, fukushima_nuclear_restart_3actor, fukushima_nuclear_restart_5actor, japan_intern_training_reform_10actor, japan_intern_training_reform_3actor, japan_intern_training_reform_5actor, microsoft_activision_merger_10actor, microsoft_activision_merger_3actor, microsoft_activision_merger_5actor, netflix_password_crackdown_10actor, netflix_password_crackdown_3actor, netflix_password_crackdown_5actor, nyc_congestion_pricing_10actor, nyc_congestion_pricing_3actor, nyc_congestion_pricing_5actor, peloton_demand_cliff_10actor, peloton_demand_cliff_3actor, peloton_demand_cliff_5actor, sf_homelessness_policy_10actor, sf_homelessness_policy_3actor, sf_homelessness_policy_5actor, singapore_hdb_waittime_crisis_10actor, singapore_hdb_waittime_crisis_3actor, singapore_hdb_waittime_crisis_5actor, starbucks_unionization_10actor, starbucks_unionization_3actor, starbucks_unionization_5actor, svb_bank_run_10actor, svb_bank_run_3actor, svb_bank_run_5actor, theranos_whistleblower_10actor, theranos_whistleblower_3actor, theranos_whistleblower_5actor, uk_post_office_horizon_10actor, uk_post_office_horizon_3actor, uk_post_office_horizon_5actor, wework_ipo_collapse_10actor, wework_ipo_collapse_3actor, wework_ipo_collapse_5actor, zoom_return_to_office_10actor, zoom_return_to_office_3actor, zoom_return_to_office_5actor
- Repetitions per condition: 2

## Condition Summary
### engine_dialogue_only
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1691 (+/- 0.0170)
- Clean persona drift MAE: 0.1691
- Per-trait absolute error: O 0.1546, C 0.2185, E 0.1385, A 0.1646, N 0.1692
- Relationship inconsistency: 0.1124
- Relationship shift rate: 0.2756
- Relationship overshoot rate: 0.2454
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0469
- Clean envelope violations: 2.0469
- Structured action validity: 0.6290
- Owner resolution rate: 0.9167
- Executed action contradiction: 0.0000
- State transition coherence: 0.9167
- Action feedback utilization: 0.3833
- Action-plan alignment: 0.9687
- Planned action coverage: 0.9211
- Action family convergence: 0.7218
- Role action diversity: 0.4999
- Negotiation uniqueness: 0.2797
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2352
- Repetition rate: 0.0278
- Topic drift rate: 0.3881
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.166, 0.1721]

- Phase-level quality:
  - OPENING: drift=0.1760, convergence=0.7628, diversity=0.3589
  - TENSION: drift=0.1739, convergence=0.7128, diversity=0.4597
  - NEGOTIATION: drift=0.1733, convergence=0.6367, diversity=0.5024
  - CLOSING: drift=0.1818, convergence=0.6500, diversity=0.5757

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### naive
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1802 (+/- 0.0167)
- Clean persona drift MAE: 0.1802
- Per-trait absolute error: O 0.1838, C 0.2267, E 0.1504, A 0.1692, N 0.1708
- Relationship inconsistency: 0.1697
- Relationship shift rate: 0.3477
- Relationship overshoot rate: 0.3346
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3353
- Clean envelope violations: 2.3353
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
- Dialogue coherence: 0.2029
- Repetition rate: 0.0139
- Topic drift rate: 0.3321
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1772, 0.1832]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1785, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1801, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1859, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### naive_informed
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1735 (+/- 0.0160)
- Clean persona drift MAE: 0.1735
- Per-trait absolute error: O 0.1750, C 0.2213, E 0.1388, A 0.1632, N 0.1692
- Relationship inconsistency: 0.1190
- Relationship shift rate: 0.2780
- Relationship overshoot rate: 0.2356
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1575
- Clean envelope violations: 2.1575
- Structured action validity: 0.6290
- Owner resolution rate: 0.9167
- Executed action contradiction: 0.0000
- State transition coherence: 0.9167
- Action feedback utilization: 0.3750
- Action-plan alignment: 0.9686
- Planned action coverage: 0.9219
- Action family convergence: 0.7218
- Role action diversity: 0.5017
- Negotiation uniqueness: 0.2836
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2069
- Repetition rate: 0.0104
- Topic drift rate: 0.3620
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1706, 0.1764]

- Phase-level quality:
  - OPENING: drift=0.1777, convergence=0.7545, diversity=0.3558
  - TENSION: drift=0.1764, convergence=0.7128, diversity=0.4597
  - NEGOTIATION: drift=0.1755, convergence=0.6200, diversity=0.4953
  - CLOSING: drift=0.1828, convergence=0.5917, diversity=0.5486

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate


## Script-Level Summary
### australia_robodebt_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1809 (+/- 0.0000)
- Clean persona drift MAE: 0.1809
- Per-trait absolute error: O 0.1570, C 0.2409, E 0.1431, A 0.2271, N 0.1366
- Relationship inconsistency: 0.2500
- Relationship shift rate: 0.3704
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1989
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1809, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1883, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1784, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1921, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1658, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0043)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1740, C 0.2471, E 0.1651, A 0.2245, N 0.1345
- Relationship inconsistency: 0.2251
- Relationship shift rate: 0.4196
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1896
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.183, 0.1951]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1817, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2009, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1683, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1839 (+/- 0.0022)
- Clean persona drift MAE: 0.1839
- Per-trait absolute error: O 0.1790, C 0.2416, E 0.1487, A 0.2239, N 0.1265
- Relationship inconsistency: 0.3470
- Relationship shift rate: 0.3641
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1970
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1809, 0.1869]

- Phase-level quality:
  - OPENING: drift=0.1897, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1795, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1993, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1686, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1733 (+/- 0.0062)
- Clean persona drift MAE: 0.1733
- Per-trait absolute error: O 0.1400, C 0.2333, E 0.1298, A 0.2333, N 0.1300
- Relationship inconsistency: 0.4970
- Relationship shift rate: 0.4562
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2177
- Repetition rate: 0.1875
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1647, 0.1818]

- Phase-level quality:
  - OPENING: drift=0.1771, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1822, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1840, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### australia_robodebt_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1856 (+/- 0.0035)
- Clean persona drift MAE: 0.1856
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1477, A 0.2333, N 0.1234
- Relationship inconsistency: 0.0435
- Relationship shift rate: 0.4707
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
- Dialogue coherence: 0.1819
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1807, 0.1905]

- Phase-level quality:
  - OPENING: drift=0.1917, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1860, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1843, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1840 (+/- 0.0028)
- Clean persona drift MAE: 0.1840
- Per-trait absolute error: O 0.1734, C 0.2333, E 0.1467, A 0.2333, N 0.1333
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.5316
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1773
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1801, 0.1879]

- Phase-level quality:
  - OPENING: drift=0.1867, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1845, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1369 (+/- 0.0005)
- Clean persona drift MAE: 0.1369
- Per-trait absolute error: O 0.1300, C 0.1811, E 0.0827, A 0.1815, N 0.1090
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4275
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.1909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1870
- Repetition rate: 0.0000
- Topic drift rate: 0.0357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1362, 0.1376]

- Phase-level quality:
  - OPENING: drift=0.1479, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1375, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1234, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1790, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1536 (+/- 0.0020)
- Clean persona drift MAE: 0.1536
- Per-trait absolute error: O 0.1740, C 0.2086, E 0.0887, A 0.1925, N 0.1040
- Relationship inconsistency: 0.4845
- Relationship shift rate: 0.4475
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
- Dialogue coherence: 0.1918
- Repetition rate: 0.0000
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1508, 0.1564]

- Phase-level quality:
  - OPENING: drift=0.1483, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1411, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1365, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1891, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### australia_robodebt_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1494 (+/- 0.0010)
- Clean persona drift MAE: 0.1494
- Per-trait absolute error: O 0.1640, C 0.1800, E 0.0913, A 0.2030, N 0.1090
- Relationship inconsistency: 0.3893
- Relationship shift rate: 0.3770
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.1909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1828
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1481, 0.1508]

- Phase-level quality:
  - OPENING: drift=0.1498, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1404, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1291, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1990, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### boeing_737max_return_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1591 (+/- 0.0032)
- Clean persona drift MAE: 0.1591
- Per-trait absolute error: O 0.1790, C 0.2500, E 0.1137, A 0.1456, N 0.1071
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
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
- Dialogue coherence: 0.2272
- Repetition rate: 0.0416
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1547, 0.1634]

- Phase-level quality:
  - OPENING: drift=0.1574, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1638, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1552, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1599, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### boeing_737max_return_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1621 (+/- 0.0016)
- Clean persona drift MAE: 0.1621
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1285, A 0.1516, N 0.1022
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
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
- Dialogue coherence: 0.2001
- Repetition rate: 0.0416
- Topic drift rate: 0.1819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1599, 0.1643]

- Phase-level quality:
  - OPENING: drift=0.1580, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1558, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1653, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### boeing_737max_return_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1547 (+/- 0.0036)
- Clean persona drift MAE: 0.1547
- Per-trait absolute error: O 0.1730, C 0.2500, E 0.1130, A 0.1375, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.7143
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
- Dialogue coherence: 0.2336
- Repetition rate: 0.0416
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1497, 0.1597]

- Phase-level quality:
  - OPENING: drift=0.1516, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1607, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1523, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1634, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### boeing_737max_return_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1744 (+/- 0.0006)
- Clean persona drift MAE: 0.1744
- Per-trait absolute error: O 0.1366, C 0.3000, E 0.1007, A 0.1683, N 0.1666
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.6000
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
- Dialogue coherence: 0.2979
- Repetition rate: 0.0625
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1735, 0.1754]

- Phase-level quality:
  - OPENING: drift=0.1691, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1742, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1705, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1900, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### boeing_737max_return_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1861 (+/- 0.0007)
- Clean persona drift MAE: 0.1861
- Per-trait absolute error: O 0.1567, C 0.3000, E 0.1021, A 0.1983, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
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
- Dialogue coherence: 0.2104
- Repetition rate: 0.0625
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1851, 0.1871]

- Phase-level quality:
  - OPENING: drift=0.1760, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1717, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1842, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2014, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### boeing_737max_return_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0123)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.1400, C 0.3000, E 0.0872, A 0.1700, N 0.1800
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
- Dialogue coherence: 0.2343
- Repetition rate: 0.0625
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1583, 0.1926]

- Phase-level quality:
  - OPENING: drift=0.1698, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1676, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1720, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1911, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### boeing_737max_return_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1651 (+/- 0.0038)
- Clean persona drift MAE: 0.1651
- Per-trait absolute error: O 0.1200, C 0.2600, E 0.0905, A 0.1715, N 0.1840
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2517
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.16, 0.1703]

- Phase-level quality:
  - OPENING: drift=0.1790, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1545, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1804, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1780, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1705 (+/- 0.0077)
- Clean persona drift MAE: 0.1705
- Per-trait absolute error: O 0.1440, C 0.2600, E 0.0968, A 0.1840, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1925
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2284
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1598, 0.1812]

- Phase-level quality:
  - OPENING: drift=0.1834, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1595, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1817, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1790, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### boeing_737max_return_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1724 (+/- 0.0041)
- Clean persona drift MAE: 0.1724
- Per-trait absolute error: O 0.1360, C 0.2600, E 0.1051, A 0.1810, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1163
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
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2169
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1667, 0.1781]

- Phase-level quality:
  - OPENING: drift=0.1870, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1592, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1807, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1870, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1550 (+/- 0.0000)
- Clean persona drift MAE: 0.1550
- Per-trait absolute error: O 0.1020, C 0.1652, E 0.1517, A 0.1557, N 0.2000
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.1295
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Dialogue coherence: 0.2757
- Repetition rate: 0.0000
- Topic drift rate: 0.0455
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1549, 0.155]

- Phase-level quality:
  - OPENING: drift=0.1578, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1623, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1543, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1511, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1660 (+/- 0.0011)
- Clean persona drift MAE: 0.1660
- Per-trait absolute error: O 0.1420, C 0.1815, E 0.1541, A 0.1523, N 0.2000
- Relationship inconsistency: 0.6380
- Relationship shift rate: 0.4844
- Relationship overshoot rate: 0.4688
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
- Dialogue coherence: 0.2274
- Repetition rate: 0.0000
- Topic drift rate: 0.0227
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1645, 0.1675]

- Phase-level quality:
  - OPENING: drift=0.1588, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1636, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1658, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1583, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1607 (+/- 0.0007)
- Clean persona drift MAE: 0.1607
- Per-trait absolute error: O 0.1320, C 0.1741, E 0.1500, A 0.1476, N 0.2000
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.3276
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Dialogue coherence: 0.2319
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1597, 0.1617]

- Phase-level quality:
  - OPENING: drift=0.1593, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1639, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1633, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1549, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1371 (+/- 0.0033)
- Clean persona drift MAE: 0.1371
- Per-trait absolute error: O 0.0900, C 0.2000, E 0.0884, A 0.1333, N 0.1734
- Relationship inconsistency: 0.4403
- Relationship shift rate: 0.4211
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2239
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1325, 0.1416]

- Phase-level quality:
  - OPENING: drift=0.1486, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1708, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1464, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1894, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1640 (+/- 0.0007)
- Clean persona drift MAE: 0.1640
- Per-trait absolute error: O 0.2067, C 0.2000, E 0.1001, A 0.1333, N 0.1800
- Relationship inconsistency: 0.5945
- Relationship shift rate: 0.4220
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2165
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.163, 0.165]

- Phase-level quality:
  - OPENING: drift=0.1623, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1600, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1638, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1811, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1667 (+/- 0.0029)
- Clean persona drift MAE: 0.1667
- Per-trait absolute error: O 0.2233, C 0.2000, E 0.1032, A 0.1333, N 0.1734
- Relationship inconsistency: 0.2755
- Relationship shift rate: 0.4200
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2314
- Repetition rate: 0.0625
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1627, 0.1706]

- Phase-level quality:
  - OPENING: drift=0.1557, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1608, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1709, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1800, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### california_ab5_gig_classification_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1538 (+/- 0.0036)
- Clean persona drift MAE: 0.1538
- Per-trait absolute error: O 0.1280, C 0.2018, E 0.1280, A 0.1555, N 0.1560
- Relationship inconsistency: 0.4710
- Relationship shift rate: 0.4076
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1982
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1488, 0.1588]

- Phase-level quality:
  - OPENING: drift=0.1438, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1497, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1662, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1392, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1677 (+/- 0.0018)
- Clean persona drift MAE: 0.1677
- Per-trait absolute error: O 0.1820, C 0.2020, E 0.1500, A 0.1505, N 0.1540
- Relationship inconsistency: 0.0390
- Relationship shift rate: 0.3287
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
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
- Dialogue coherence: 0.2011
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1652, 0.1702]

- Phase-level quality:
  - OPENING: drift=0.1537, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1571, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1768, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1628, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1567 (+/- 0.0019)
- Clean persona drift MAE: 0.1567
- Per-trait absolute error: O 0.1520, C 0.2220, E 0.1293, A 0.1340, N 0.1460
- Relationship inconsistency: 0.2545
- Relationship shift rate: 0.3720
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2164
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1539, 0.1594]

- Phase-level quality:
  - OPENING: drift=0.1457, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1567, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1613, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1394, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0030)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.1590, C 0.2059, E 0.1200, A 0.1569, N 0.1644
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2381
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.157, 0.1655]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1658, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1584, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1723, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0013)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1730, C 0.2124, E 0.1195, A 0.1636, N 0.1578
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4605
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2018
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1634, 0.167]

- Phase-level quality:
  - OPENING: drift=0.1768, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1752, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1637, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1668, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1732 (+/- 0.0020)
- Clean persona drift MAE: 0.1732
- Per-trait absolute error: O 0.1920, C 0.2105, E 0.1255, A 0.1761, N 0.1618
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4175
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Dialogue coherence: 0.2172
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1704, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1805, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1799, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1655, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1742, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1432 (+/- 0.0023)
- Clean persona drift MAE: 0.1432
- Per-trait absolute error: O 0.1167, C 0.1425, E 0.1522, A 0.1384, N 0.1667
- Relationship inconsistency: 0.0761
- Relationship shift rate: 0.2706
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2402
- Repetition rate: 0.0625
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1401, 0.1464]

- Phase-level quality:
  - OPENING: drift=0.1641, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1679, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1708, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1816, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### eu_gdpr_implementation_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1701 (+/- 0.0096)
- Clean persona drift MAE: 0.1701
- Per-trait absolute error: O 0.2233, C 0.1835, E 0.1305, A 0.1433, N 0.1700
- Relationship inconsistency: 0.5375
- Relationship shift rate: 0.5350
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1982
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1569, 0.1834]

- Phase-level quality:
  - OPENING: drift=0.1645, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1848, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1765, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1885, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1643 (+/- 0.0012)
- Clean persona drift MAE: 0.1643
- Per-trait absolute error: O 0.2067, C 0.2003, E 0.1361, A 0.1116, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4408
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2016
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1626, 0.166]

- Phase-level quality:
  - OPENING: drift=0.1736, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1839, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1687, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1828, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### eu_gdpr_implementation_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1564 (+/- 0.0067)
- Clean persona drift MAE: 0.1564
- Per-trait absolute error: O 0.2080, C 0.2011, E 0.1038, A 0.1230, N 0.1460
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2759
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.3333
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2867
- Repetition rate: 0.0000
- Topic drift rate: 0.1071
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1471, 0.1657]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1587, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1698, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1876, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1745 (+/- 0.0035)
- Clean persona drift MAE: 0.1745
- Per-trait absolute error: O 0.2520, C 0.2009, E 0.1195, A 0.1480, N 0.1520
- Relationship inconsistency: 0.3875
- Relationship shift rate: 0.3567
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
- Dialogue coherence: 0.2107
- Repetition rate: 0.0000
- Topic drift rate: 0.0357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1696, 0.1794]

- Phase-level quality:
  - OPENING: drift=0.1791, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1669, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1762, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1974, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1671 (+/- 0.0016)
- Clean persona drift MAE: 0.1671
- Per-trait absolute error: O 0.2520, C 0.2039, E 0.1068, A 0.1330, N 0.1400
- Relationship inconsistency: 0.2930
- Relationship shift rate: 0.3705
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.3333
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2227
- Repetition rate: 0.0000
- Topic drift rate: 0.0357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1649, 0.1693]

- Phase-level quality:
  - OPENING: drift=0.1738, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1662, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1671, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1721, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0032)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1960, C 0.1891, E 0.1323, A 0.1742, N 0.1600
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.3377
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2692
- Repetition rate: 0.0416
- Topic drift rate: 0.3409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.166, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1644, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1729, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1678, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1825, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### flint_water_crisis_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1714 (+/- 0.0047)
- Clean persona drift MAE: 0.1714
- Per-trait absolute error: O 0.2000, C 0.1901, E 0.1451, A 0.1615, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3298
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
- Dialogue coherence: 0.2310
- Repetition rate: 0.0000
- Topic drift rate: 0.1364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1649, 0.1778]

- Phase-level quality:
  - OPENING: drift=0.1611, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1857, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1610, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1872, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### flint_water_crisis_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1643 (+/- 0.0006)
- Clean persona drift MAE: 0.1643
- Per-trait absolute error: O 0.1780, C 0.1815, E 0.1238, A 0.1738, N 0.1644
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3325
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2385
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1635, 0.1651]

- Phase-level quality:
  - OPENING: drift=0.1640, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1767, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1565, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1773, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### flint_water_crisis_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1973 (+/- 0.0053)
- Clean persona drift MAE: 0.1973
- Per-trait absolute error: O 0.1300, C 0.2333, E 0.1431, A 0.2334, N 0.2467
- Relationship inconsistency: 0.1155
- Relationship shift rate: 0.2922
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2750
- Repetition rate: 0.1250
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.19, 0.2046]

- Phase-level quality:
  - OPENING: drift=0.2102, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2028, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2114, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2130, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2307 (+/- 0.0090)
- Clean persona drift MAE: 0.2307
- Per-trait absolute error: O 0.2200, C 0.2333, E 0.1836, A 0.2833, N 0.2333
- Relationship inconsistency: 0.1711
- Relationship shift rate: 0.3296
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.5000
- Clean envelope violations: 3.5000
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
- Dialogue coherence: 0.2101
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2182, 0.2432]

- Phase-level quality:
  - OPENING: drift=0.2303, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2125, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2356, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2188, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2084 (+/- 0.0023)
- Clean persona drift MAE: 0.2084
- Per-trait absolute error: O 0.1800, C 0.2333, E 0.1422, A 0.2534, N 0.2333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2325
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2036
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2053, 0.2116]

- Phase-level quality:
  - OPENING: drift=0.2133, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2096, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2235, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1929, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1819 (+/- 0.0060)
- Clean persona drift MAE: 0.1819
- Per-trait absolute error: O 0.1700, C 0.2505, E 0.1284, A 0.1745, N 0.1860
- Relationship inconsistency: 0.0699
- Relationship shift rate: 0.3422
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2421
- Repetition rate: 0.0000
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1736, 0.1902]

- Phase-level quality:
  - OPENING: drift=0.1704, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1726, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1927, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1594, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1797 (+/- 0.0134)
- Clean persona drift MAE: 0.1797
- Per-trait absolute error: O 0.1800, C 0.2510, E 0.1280, A 0.1475, N 0.1920
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2573
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
- Dialogue coherence: 0.2064
- Repetition rate: 0.0000
- Topic drift rate: 0.0357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1611, 0.1983]

- Phase-level quality:
  - OPENING: drift=0.1701, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1662, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2009, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1680, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1691 (+/- 0.0020)
- Clean persona drift MAE: 0.1691
- Per-trait absolute error: O 0.1540, C 0.2499, E 0.1116, A 0.1500, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2425
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2147
- Repetition rate: 0.0556
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1663, 0.172]

- Phase-level quality:
  - OPENING: drift=0.1732, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1620, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1885, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1593, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### ftx_collapse_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1620 (+/- 0.0019)
- Clean persona drift MAE: 0.1620
- Per-trait absolute error: O 0.1710, C 0.2097, E 0.1085, A 0.1303, N 0.1904
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1375
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9738
- Planned action coverage: 0.9546
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2365
- Repetition rate: 0.0000
- Topic drift rate: 0.3637
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1594, 0.1646]

- Phase-level quality:
  - OPENING: drift=0.1693, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1638, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1758, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1540, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1706 (+/- 0.0015)
- Clean persona drift MAE: 0.1706
- Per-trait absolute error: O 0.2010, C 0.2073, E 0.1239, A 0.1289, N 0.1922
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3109
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
- Dialogue coherence: 0.2143
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1685, 0.1728]

- Phase-level quality:
  - OPENING: drift=0.1740, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1653, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1808, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1623, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1681 (+/- 0.0045)
- Clean persona drift MAE: 0.1681
- Per-trait absolute error: O 0.1930, C 0.2085, E 0.1213, A 0.1361, N 0.1820
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2712
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2024
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1618, 0.1745]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1713, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1750, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1593, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1648 (+/- 0.0035)
- Clean persona drift MAE: 0.1648
- Per-trait absolute error: O 0.2233, C 0.2092, E 0.1584, A 0.1000, N 0.1333
- Relationship inconsistency: 0.3015
- Relationship shift rate: 0.5390
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.1340
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1962
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1601, 0.1696]

- Phase-level quality:
  - OPENING: drift=0.1661, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1761, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1572, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1900, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1941 (+/- 0.0089)
- Clean persona drift MAE: 0.1941
- Per-trait absolute error: O 0.2900, C 0.2678, E 0.1797, A 0.1000, N 0.1333
- Relationship inconsistency: 0.4125
- Relationship shift rate: 0.4547
- Relationship overshoot rate: 0.5250
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
- Dialogue coherence: 0.1910
- Repetition rate: 0.0000
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1819, 0.2064]

- Phase-level quality:
  - OPENING: drift=0.1648, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1620, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1768, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2097, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### ftx_collapse_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1590 (+/- 0.0119)
- Clean persona drift MAE: 0.1590
- Per-trait absolute error: O 0.2233, C 0.1706, E 0.1613, A 0.1066, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2925
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.3889
- Negotiation uniqueness: 0.2381
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1966
- Repetition rate: 0.0000
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1425, 0.1755]

- Phase-level quality:
  - OPENING: drift=0.1657, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1607, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1699, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1860, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1816 (+/- 0.0033)
- Clean persona drift MAE: 0.1816
- Per-trait absolute error: O 0.1640, C 0.1807, E 0.1790, A 0.2125, N 0.1720
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2396
- Repetition rate: 0.0556
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.177, 0.1862]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1975, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1979, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1800, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### ftx_collapse_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1987 (+/- 0.0001)
- Clean persona drift MAE: 0.1987
- Per-trait absolute error: O 0.2340, C 0.1912, E 0.1869, A 0.2175, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.2120
- Repetition rate: 0.1111
- Topic drift rate: 0.2858
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1987, 0.1988]

- Phase-level quality:
  - OPENING: drift=0.1789, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2114, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1992, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1916, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### ftx_collapse_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1991 (+/- 0.0005)
- Clean persona drift MAE: 0.1991
- Per-trait absolute error: O 0.2340, C 0.2156, E 0.1851, A 0.2005, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2024
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1983, 0.1998]

- Phase-level quality:
  - OPENING: drift=0.1881, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2127, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1940, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1955, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1688 (+/- 0.0007)
- Clean persona drift MAE: 0.1688
- Per-trait absolute error: O 0.1340, C 0.2322, E 0.1502, A 0.1336, N 0.1940
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1325
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2310
- Repetition rate: 0.0833
- Topic drift rate: 0.8637
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1678, 0.1698]

- Phase-level quality:
  - OPENING: drift=0.1668, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1871, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1628, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1886, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### fukushima_nuclear_restart_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1774 (+/- 0.0005)
- Clean persona drift MAE: 0.1774
- Per-trait absolute error: O 0.1640, C 0.2288, E 0.1643, A 0.1428, N 0.1873
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1638
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
- Dialogue coherence: 0.2137
- Repetition rate: 0.0416
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1768, 0.1781]

- Phase-level quality:
  - OPENING: drift=0.1641, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1985, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1922, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### fukushima_nuclear_restart_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1739 (+/- 0.0005)
- Clean persona drift MAE: 0.1739
- Per-trait absolute error: O 0.1640, C 0.2208, E 0.1503, A 0.1429, N 0.1913
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5500
- Clean envelope violations: 2.5500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1955
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1731, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1565, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1998, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1698, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1903, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1625 (+/- 0.0112)
- Clean persona drift MAE: 0.1625
- Per-trait absolute error: O 0.1666, C 0.2333, E 0.1140, A 0.1050, N 0.1934
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1667
- Clean envelope violations: 2.1667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2605
- Repetition rate: 0.0625
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.147, 0.178]

- Phase-level quality:
  - OPENING: drift=0.1661, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1665, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1694, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1720, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### fukushima_nuclear_restart_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1836 (+/- 0.0089)
- Clean persona drift MAE: 0.1836
- Per-trait absolute error: O 0.1734, C 0.2513, E 0.1232, A 0.1700, N 0.2000
- Relationship inconsistency: 0.4375
- Relationship shift rate: 0.4334
- Relationship overshoot rate: 0.2850
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
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
- Dialogue coherence: 0.2368
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1713, 0.1959]

- Phase-level quality:
  - OPENING: drift=0.1822, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1782, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1655, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1850, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### fukushima_nuclear_restart_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1568 (+/- 0.0013)
- Clean persona drift MAE: 0.1568
- Per-trait absolute error: O 0.1400, C 0.2333, E 0.1019, A 0.1083, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1175
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2202
- Repetition rate: 0.0000
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.155, 0.1585]

- Phase-level quality:
  - OPENING: drift=0.1664, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1604, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1636, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1870, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0008)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1700, C 0.1958, E 0.1517, A 0.1225, N 0.2100
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1116
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.0714
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2309
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1689, 0.1711]

- Phase-level quality:
  - OPENING: drift=0.1708, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1911, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1674, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1794, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1860 (+/- 0.0008)
- Clean persona drift MAE: 0.1860
- Per-trait absolute error: O 0.1900, C 0.2112, E 0.1744, A 0.1340, N 0.2200
- Relationship inconsistency: 0.0225
- Relationship shift rate: 0.2755
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.2018
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1849, 0.187]

- Phase-level quality:
  - OPENING: drift=0.1806, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1849, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1797, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1749, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1851 (+/- 0.0050)
- Clean persona drift MAE: 0.1851
- Per-trait absolute error: O 0.2020, C 0.2310, E 0.1585, A 0.1110, N 0.2230
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.2041
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.0769
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2030
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1782, 0.192]

- Phase-level quality:
  - OPENING: drift=0.1806, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1921, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1770, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1871, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### japan_intern_training_reform_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1558 (+/- 0.0035)
- Clean persona drift MAE: 0.1558
- Per-trait absolute error: O 0.1660, C 0.1724, E 0.1289, A 0.1481, N 0.1636
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3960
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2737
- Repetition rate: 0.0833
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1509, 0.1607]

- Phase-level quality:
  - OPENING: drift=0.1553, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1732, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1564, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1568, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### japan_intern_training_reform_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1682 (+/- 0.0013)
- Clean persona drift MAE: 0.1682
- Per-trait absolute error: O 0.2150, C 0.1710, E 0.1488, A 0.1461, N 0.1600
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4969
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
- Dialogue coherence: 0.1733
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1664, 0.17]

- Phase-level quality:
  - OPENING: drift=0.1564, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1882, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1660, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1643, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1610 (+/- 0.0035)
- Clean persona drift MAE: 0.1610
- Per-trait absolute error: O 0.2000, C 0.1711, E 0.1304, A 0.1418, N 0.1618
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3753
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2083
- Repetition rate: 0.0416
- Topic drift rate: 0.8181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1561, 0.1659]

- Phase-level quality:
  - OPENING: drift=0.1483, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1807, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1651, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1629, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### japan_intern_training_reform_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1911 (+/- 0.0039)
- Clean persona drift MAE: 0.1911
- Per-trait absolute error: O 0.2100, C 0.2400, E 0.0905, A 0.2217, N 0.1933
- Relationship inconsistency: 0.3518
- Relationship shift rate: 0.4718
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.1056
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2155
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1857, 0.1965]

- Phase-level quality:
  - OPENING: drift=0.1910, convergence=0.5000, diversity=0.1666
  - TENSION: drift=0.1976, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1900, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1774, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2000 (+/- 0.0015)
- Clean persona drift MAE: 0.2000
- Per-trait absolute error: O 0.2600, C 0.2333, E 0.1169, A 0.1834, N 0.2067
- Relationship inconsistency: 0.2720
- Relationship shift rate: 0.4587
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
- Dialogue coherence: 0.2006
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1979, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.2019, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2009, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2011, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1620, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### japan_intern_training_reform_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1904 (+/- 0.0009)
- Clean persona drift MAE: 0.1904
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.0917, A 0.1834, N 0.2000
- Relationship inconsistency: 0.6350
- Relationship shift rate: 0.5804
- Relationship overshoot rate: 0.4929
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.7222
- Negotiation uniqueness: 0.1667
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1955
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1892, 0.1915]

- Phase-level quality:
  - OPENING: drift=0.1954, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1954, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1880, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1696, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### japan_intern_training_reform_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1523 (+/- 0.0029)
- Clean persona drift MAE: 0.1523
- Per-trait absolute error: O 0.1580, C 0.2400, E 0.0701, A 0.1075, N 0.1860
- Relationship inconsistency: 0.1136
- Relationship shift rate: 0.3334
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
- Dialogue coherence: 0.2301
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1483, 0.1563]

- Phase-level quality:
  - OPENING: drift=0.1640, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1395, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1462, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1533 (+/- 0.0005)
- Clean persona drift MAE: 0.1533
- Per-trait absolute error: O 0.1580, C 0.2508, E 0.0706, A 0.1070, N 0.1800
- Relationship inconsistency: 0.5510
- Relationship shift rate: 0.4419
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
- Dialogue coherence: 0.2009
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1526, 0.154]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1417, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1468, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2040, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### japan_intern_training_reform_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1501 (+/- 0.0024)
- Clean persona drift MAE: 0.1501
- Per-trait absolute error: O 0.1620, C 0.2400, E 0.0666, A 0.0980, N 0.1840
- Relationship inconsistency: 0.2778
- Relationship shift rate: 0.3683
- Relationship overshoot rate: 0.4750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
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
- Dialogue coherence: 0.1984
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1468, 0.1534]

- Phase-level quality:
  - OPENING: drift=0.1649, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1447, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1437, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1913 (+/- 0.0013)
- Clean persona drift MAE: 0.1913
- Per-trait absolute error: O 0.2130, C 0.1954, E 0.1770, A 0.2031, N 0.1680
- Relationship inconsistency: 0.1170
- Relationship shift rate: 0.4145
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2651
- Repetition rate: 0.0000
- Topic drift rate: 0.2954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0002
- Mean turns: 22.00
- Persona drift 95% CI: [0.1895, 0.1931]

- Phase-level quality:
  - OPENING: drift=0.1915, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.2029, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1842, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.2068, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1985 (+/- 0.0016)
- Clean persona drift MAE: 0.1985
- Per-trait absolute error: O 0.2520, C 0.1949, E 0.1789, A 0.2025, N 0.1640
- Relationship inconsistency: 0.3110
- Relationship shift rate: 0.4136
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
- Dialogue coherence: 0.2169
- Repetition rate: 0.0000
- Topic drift rate: 0.1819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1963, 0.2006]

- Phase-level quality:
  - OPENING: drift=0.1964, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2051, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1904, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2096, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1901 (+/- 0.0009)
- Clean persona drift MAE: 0.1901
- Per-trait absolute error: O 0.2350, C 0.1934, E 0.1618, A 0.1989, N 0.1618
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2092
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2168
- Repetition rate: 0.0000
- Topic drift rate: 0.3182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1888, 0.1915]

- Phase-level quality:
  - OPENING: drift=0.1961, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.2006, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1786, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.2104, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1651 (+/- 0.0068)
- Clean persona drift MAE: 0.1651
- Per-trait absolute error: O 0.1433, C 0.2667, E 0.0956, A 0.1333, N 0.1866
- Relationship inconsistency: 0.5882
- Relationship shift rate: 0.4702
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2459
- Repetition rate: 0.0625
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1557, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1782, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1675, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1706, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### microsoft_activision_merger_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1722 (+/- 0.0003)
- Clean persona drift MAE: 0.1722
- Per-trait absolute error: O 0.1233, C 0.2667, E 0.1079, A 0.1533, N 0.2100
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.3583
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
- Dialogue coherence: 0.2225
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1719, 0.1726]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1733, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1686, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1885, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1752 (+/- 0.0017)
- Clean persona drift MAE: 0.1752
- Per-trait absolute error: O 0.1433, C 0.2667, E 0.1190, A 0.1500, N 0.1966
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.1071
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2113
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1729, 0.1774]

- Phase-level quality:
  - OPENING: drift=0.1782, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1779, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1773, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1814, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### microsoft_activision_merger_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1634 (+/- 0.0051)
- Clean persona drift MAE: 0.1634
- Per-trait absolute error: O 0.2100, C 0.2121, E 0.1074, A 0.1185, N 0.1690
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2700
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2330
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1563, 0.1705]

- Phase-level quality:
  - OPENING: drift=0.1809, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1651, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1496, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1827, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1661 (+/- 0.0025)
- Clean persona drift MAE: 0.1661
- Per-trait absolute error: O 0.1940, C 0.2044, E 0.1315, A 0.1165, N 0.1840
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2479
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
- Dialogue coherence: 0.1974
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1626, 0.1696]

- Phase-level quality:
  - OPENING: drift=0.1867, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1673, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1592, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1906, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1563 (+/- 0.0013)
- Clean persona drift MAE: 0.1563
- Per-trait absolute error: O 0.1940, C 0.2088, E 0.1058, A 0.0990, N 0.1740
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1998
- Repetition rate: 0.0000
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1545, 0.1581]

- Phase-level quality:
  - OPENING: drift=0.1670, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1623, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1517, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1935, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1748 (+/- 0.0006)
- Clean persona drift MAE: 0.1748
- Per-trait absolute error: O 0.2180, C 0.1912, E 0.1555, A 0.1589, N 0.1500
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3295
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.2198
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.174, 0.1755]

- Phase-level quality:
  - OPENING: drift=0.1714, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1920, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1755, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1861, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1858 (+/- 0.0004)
- Clean persona drift MAE: 0.1858
- Per-trait absolute error: O 0.2430, C 0.2019, E 0.1675, A 0.1598, N 0.1569
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3488
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1740
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1852, 0.1864]

- Phase-level quality:
  - OPENING: drift=0.1787, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1905, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1844, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1890, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1808 (+/- 0.0016)
- Clean persona drift MAE: 0.1808
- Per-trait absolute error: O 0.2330, C 0.1966, E 0.1573, A 0.1660, N 0.1509
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.2387
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.7143
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2110
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1785, 0.183]

- Phase-level quality:
  - OPENING: drift=0.1785, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1901, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1828, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1851, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2052 (+/- 0.0045)
- Clean persona drift MAE: 0.2052
- Per-trait absolute error: O 0.1734, C 0.2333, E 0.2030, A 0.2033, N 0.2134
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3035
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3334
- Clean envelope violations: 2.3334
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1946
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1989, 0.2116]

- Phase-level quality:
  - OPENING: drift=0.2093, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2067, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2061, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1758, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2095 (+/- 0.0008)
- Clean persona drift MAE: 0.2095
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.2142, A 0.2034, N 0.2067
- Relationship inconsistency: 0.3875
- Relationship shift rate: 0.4550
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1470
- Repetition rate: 0.0000
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2084, 0.2106]

- Phase-level quality:
  - OPENING: drift=0.2072, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2090, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2136, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1966 (+/- 0.0014)
- Clean persona drift MAE: 0.1966
- Per-trait absolute error: O 0.1567, C 0.2333, E 0.2000, A 0.1834, N 0.2100
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2710
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1884
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1948, 0.1985]

- Phase-level quality:
  - OPENING: drift=0.2027, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2033, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2048, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1749, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1934 (+/- 0.0016)
- Clean persona drift MAE: 0.1934
- Per-trait absolute error: O 0.1480, C 0.2205, E 0.1981, A 0.1785, N 0.2220
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.1175
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8000
- Clean envelope violations: 2.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2050
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1912, 0.1956]

- Phase-level quality:
  - OPENING: drift=0.2129, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1960, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1802, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2036 (+/- 0.0010)
- Clean persona drift MAE: 0.2036
- Per-trait absolute error: O 0.2020, C 0.2088, E 0.2120, A 0.1820, N 0.2130
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2660
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1705
- Repetition rate: 0.0000
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2022, 0.205]

- Phase-level quality:
  - OPENING: drift=0.2132, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1930, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1898, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2408, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2031 (+/- 0.0010)
- Clean persona drift MAE: 0.2031
- Per-trait absolute error: O 0.1820, C 0.2148, E 0.1923, A 0.1985, N 0.2280
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2863
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2073
- Repetition rate: 0.0000
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2018, 0.2045]

- Phase-level quality:
  - OPENING: drift=0.2126, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1941, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1830, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1625 (+/- 0.0005)
- Clean persona drift MAE: 0.1625
- Per-trait absolute error: O 0.1590, C 0.1441, E 0.1708, A 0.1794, N 0.1592
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3010
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Dialogue coherence: 0.1956
- Repetition rate: 0.0000
- Topic drift rate: 0.2046
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1618, 0.1632]

- Phase-level quality:
  - OPENING: drift=0.1648, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1820, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1623, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1718, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0008)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.1690, C 0.1798, E 0.1849, A 0.1798, N 0.1613
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.6481
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
- Dialogue coherence: 0.1847
- Repetition rate: 0.0000
- Topic drift rate: 0.1137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1739, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1633, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1875, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1741, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1803, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1720 (+/- 0.0016)
- Clean persona drift MAE: 0.1720
- Per-trait absolute error: O 0.1740, C 0.1698, E 0.1759, A 0.1834, N 0.1569
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.3093
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Dialogue coherence: 0.1914
- Repetition rate: 0.0416
- Topic drift rate: 0.1137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1698, 0.1742]

- Phase-level quality:
  - OPENING: drift=0.1656, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1827, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1712, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1781, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### nyc_congestion_pricing_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1532 (+/- 0.0039)
- Clean persona drift MAE: 0.1532
- Per-trait absolute error: O 0.1000, C 0.2000, E 0.1729, A 0.0934, N 0.2000
- Relationship inconsistency: 0.1688
- Relationship shift rate: 0.2856
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1975
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1478, 0.1586]

- Phase-level quality:
  - OPENING: drift=0.1540, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1630, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1681, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1495, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0053)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.1233, C 0.2000, E 0.1667, A 0.1167, N 0.2000
- Relationship inconsistency: 0.1340
- Relationship shift rate: 0.3060
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
- Dialogue coherence: 0.1860
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1539, 0.1688]

- Phase-level quality:
  - OPENING: drift=0.1684, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1623, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1630, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1500, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### nyc_congestion_pricing_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1590 (+/- 0.0030)
- Clean persona drift MAE: 0.1590
- Per-trait absolute error: O 0.1000, C 0.2000, E 0.1667, A 0.1283, N 0.2000
- Relationship inconsistency: 0.2295
- Relationship shift rate: 0.2942
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.3333
- Clean envelope violations: 1.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1835
- Repetition rate: 0.0625
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1548, 0.1632]

- Phase-level quality:
  - OPENING: drift=0.1661, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1607, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1630, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1510, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### nyc_congestion_pricing_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1368 (+/- 0.0020)
- Clean persona drift MAE: 0.1368
- Per-trait absolute error: O 0.1060, C 0.2800, E 0.1169, A 0.0990, N 0.0820
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2787
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.3333
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2229
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.134, 0.1396]

- Phase-level quality:
  - OPENING: drift=0.1386, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1335, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1448, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1342, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1442 (+/- 0.0010)
- Clean persona drift MAE: 0.1442
- Per-trait absolute error: O 0.1340, C 0.2800, E 0.1247, A 0.1010, N 0.0810
- Relationship inconsistency: 0.2340
- Relationship shift rate: 0.3399
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1946
- Repetition rate: 0.0000
- Topic drift rate: 0.1071
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1428, 0.1455]

- Phase-level quality:
  - OPENING: drift=0.1422, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1289, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1537, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1291, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1470 (+/- 0.0031)
- Clean persona drift MAE: 0.1470
- Per-trait absolute error: O 0.1440, C 0.2800, E 0.1286, A 0.0985, N 0.0840
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2733
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.4000
- Clean envelope violations: 1.4000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.3333
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2208
- Repetition rate: 0.0556
- Topic drift rate: 0.2143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1427, 0.1513]

- Phase-level quality:
  - OPENING: drift=0.1424, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1341, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1568, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1373, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### peloton_demand_cliff_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1643 (+/- 0.0053)
- Clean persona drift MAE: 0.1643
- Per-trait absolute error: O 0.1250, C 0.2600, E 0.1425, A 0.1240, N 0.1703
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2056
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2471
- Repetition rate: 0.0833
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1569, 0.1718]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1548, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1794, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1612, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### peloton_demand_cliff_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1766 (+/- 0.0030)
- Clean persona drift MAE: 0.1766
- Per-trait absolute error: O 0.1730, C 0.2600, E 0.1527, A 0.1250, N 0.1723
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1817
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
- Dialogue coherence: 0.2122
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1724, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1805, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1673, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1783, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1704, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1686 (+/- 0.0018)
- Clean persona drift MAE: 0.1686
- Per-trait absolute error: O 0.1530, C 0.2613, E 0.1371, A 0.1180, N 0.1736
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2025
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2120
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1661, 0.1711]

- Phase-level quality:
  - OPENING: drift=0.1778, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1631, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1738, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1706, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### peloton_demand_cliff_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1643 (+/- 0.0077)
- Clean persona drift MAE: 0.1643
- Per-trait absolute error: O 0.1167, C 0.2333, E 0.1732, A 0.1583, N 0.1400
- Relationship inconsistency: 0.1874
- Relationship shift rate: 0.3370
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.3333
- Clean envelope violations: 1.3333
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
- Dialogue coherence: 0.2525
- Repetition rate: 0.0625
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1536, 0.175]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1743, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1766, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1724, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### peloton_demand_cliff_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1832 (+/- 0.0010)
- Clean persona drift MAE: 0.1832
- Per-trait absolute error: O 0.1500, C 0.2626, E 0.1963, A 0.1266, N 0.1800
- Relationship inconsistency: 0.2236
- Relationship shift rate: 0.3830
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
- Dialogue coherence: 0.2050
- Repetition rate: 0.0625
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1818, 0.1845]

- Phase-level quality:
  - OPENING: drift=0.1835, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1842, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1886, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1790, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### peloton_demand_cliff_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0075)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1433, C 0.2333, E 0.1689, A 0.1667, N 0.1400
- Relationship inconsistency: 0.1600
- Relationship shift rate: 0.4300
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Dialogue coherence: 0.1872
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.16, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1783, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1769, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1709, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1718, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1487 (+/- 0.0040)
- Clean persona drift MAE: 0.1487
- Per-trait absolute error: O 0.1020, C 0.2000, E 0.1432, A 0.1305, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2583
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Dialogue coherence: 0.2282
- Repetition rate: 0.0556
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1431, 0.1544]

- Phase-level quality:
  - OPENING: drift=0.1797, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1304, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1569, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1955, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### peloton_demand_cliff_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1569 (+/- 0.0064)
- Clean persona drift MAE: 0.1569
- Per-trait absolute error: O 0.1540, C 0.2011, E 0.1513, A 0.1130, N 0.1650
- Relationship inconsistency: 0.0225
- Relationship shift rate: 0.3720
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
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
- Dialogue coherence: 0.2219
- Repetition rate: 0.1111
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.148, 0.1658]

- Phase-level quality:
  - OPENING: drift=0.1760, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1360, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1573, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1940, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### peloton_demand_cliff_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1577 (+/- 0.0012)
- Clean persona drift MAE: 0.1577
- Per-trait absolute error: O 0.1540, C 0.2061, E 0.1417, A 0.1210, N 0.1660
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3100
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Dialogue coherence: 0.1983
- Repetition rate: 0.0000
- Topic drift rate: 0.5714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.156, 0.1594]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1413, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1575, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1946, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### sf_homelessness_policy_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1717 (+/- 0.0019)
- Clean persona drift MAE: 0.1717
- Per-trait absolute error: O 0.1580, C 0.2155, E 0.1307, A 0.1884, N 0.1660
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2800
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
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2176
- Repetition rate: 0.0000
- Topic drift rate: 0.3409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1691, 0.1743]

- Phase-level quality:
  - OPENING: drift=0.1763, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1727, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1914, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1508, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1787 (+/- 0.0013)
- Clean persona drift MAE: 0.1787
- Per-trait absolute error: O 0.1820, C 0.2132, E 0.1481, A 0.1761, N 0.1740
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4579
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
- Dialogue coherence: 0.2070
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1768, 0.1805]

- Phase-level quality:
  - OPENING: drift=0.1835, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1762, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1973, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1519, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1766 (+/- 0.0009)
- Clean persona drift MAE: 0.1766
- Per-trait absolute error: O 0.1850, C 0.2152, E 0.1318, A 0.1815, N 0.1696
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3538
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
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1973
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1754, 0.1778]

- Phase-level quality:
  - OPENING: drift=0.1834, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1753, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1915, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1522, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### sf_homelessness_policy_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1617 (+/- 0.0130)
- Clean persona drift MAE: 0.1617
- Per-trait absolute error: O 0.1600, C 0.2238, E 0.0598, A 0.1917, N 0.1733
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2047
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.6667
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
- Dialogue coherence: 0.2584
- Repetition rate: 0.0625
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1437, 0.1797]

- Phase-level quality:
  - OPENING: drift=0.1756, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1630, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1623, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1766, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### sf_homelessness_policy_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1821 (+/- 0.0002)
- Clean persona drift MAE: 0.1821
- Per-trait absolute error: O 0.1734, C 0.2129, E 0.1176, A 0.2000, N 0.2067
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3594
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
- Dialogue coherence: 0.1996
- Repetition rate: 0.0000
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1818, 0.1824]

- Phase-level quality:
  - OPENING: drift=0.1928, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1803, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1817, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1714, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0006)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1433, C 0.2000, E 0.0794, A 0.1800, N 0.1966
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.3100
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2023
- Repetition rate: 0.0000
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1591, 0.1607]

- Phase-level quality:
  - OPENING: drift=0.1769, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1710, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1677, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1713, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0091)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.0860, C 0.2000, E 0.1778, A 0.1710, N 0.1920
- Relationship inconsistency: 0.0653
- Relationship shift rate: 0.3036
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
- Dialogue coherence: 0.2068
- Repetition rate: 0.0000
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1527, 0.178]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1833, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1693, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1608, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1723 (+/- 0.0006)
- Clean persona drift MAE: 0.1723
- Per-trait absolute error: O 0.1040, C 0.2000, E 0.2020, A 0.1755, N 0.1800
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.3501
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
- Dialogue coherence: 0.1678
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1713, 0.1732]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1881, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1719, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1783, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1752 (+/- 0.0040)
- Clean persona drift MAE: 0.1752
- Per-trait absolute error: O 0.1060, C 0.2066, E 0.1920, A 0.1895, N 0.1820
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4883
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
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1905
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1697, 0.1807]

- Phase-level quality:
  - OPENING: drift=0.1865, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1862, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1758, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1723, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0008)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1580, C 0.2400, E 0.1995, A 0.1945, N 0.1535
- Relationship inconsistency: 0.0795
- Relationship shift rate: 0.3174
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.2271
- Negotiation uniqueness: 0.0528
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2341
- Repetition rate: 0.0000
- Topic drift rate: 0.5455
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.188, 0.1901]

- Phase-level quality:
  - OPENING: drift=0.1845, convergence=1.0000, diversity=0.2666
  - TENSION: drift=0.1898, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1878, convergence=1.0000, diversity=0.1834
  - CLOSING: drift=0.1969, convergence=1.0000, diversity=0.2916

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### singapore_hdb_waittime_crisis_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1883 (+/- 0.0030)
- Clean persona drift MAE: 0.1883
- Per-trait absolute error: O 0.1580, C 0.2400, E 0.1951, A 0.1958, N 0.1522
- Relationship inconsistency: 0.3319
- Relationship shift rate: 0.4394
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
- Dialogue coherence: 0.2158
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1842, 0.1923]

- Phase-level quality:
  - OPENING: drift=0.1799, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1955, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1860, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1886, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1860 (+/- 0.0005)
- Clean persona drift MAE: 0.1860
- Per-trait absolute error: O 0.1580, C 0.2400, E 0.1812, A 0.1976, N 0.1535
- Relationship inconsistency: 0.1633
- Relationship shift rate: 0.3838
- Relationship overshoot rate: 0.4950
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.3208
- Negotiation uniqueness: 0.0590
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2091
- Repetition rate: 0.0416
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1853, 0.1868]

- Phase-level quality:
  - OPENING: drift=0.1769, convergence=1.0000, diversity=0.2250
  - TENSION: drift=0.1870, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1845, convergence=1.0000, diversity=0.2250
  - CLOSING: drift=0.1976, convergence=0.5000, diversity=0.1666

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, topic_drift_rate

### singapore_hdb_waittime_crisis_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1823 (+/- 0.0003)
- Clean persona drift MAE: 0.1823
- Per-trait absolute error: O 0.1933, C 0.2667, E 0.1000, A 0.1850, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1750
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2283
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1819, 0.1827]

- Phase-level quality:
  - OPENING: drift=0.1824, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1916, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1910, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1884 (+/- 0.0064)
- Clean persona drift MAE: 0.1884
- Per-trait absolute error: O 0.1767, C 0.2667, E 0.1001, A 0.2316, N 0.1667
- Relationship inconsistency: 0.1420
- Relationship shift rate: 0.2188
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8334
- Clean envelope violations: 2.8334
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
- Dialogue coherence: 0.1744
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1795, 0.1972]

- Phase-level quality:
  - OPENING: drift=0.1909, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1880, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1880, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2092, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1829 (+/- 0.0016)
- Clean persona drift MAE: 0.1829
- Per-trait absolute error: O 0.1767, C 0.2667, E 0.1013, A 0.2034, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3334
- Clean envelope violations: 2.3334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1945
- Repetition rate: 0.0625
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1807, 0.1851]

- Phase-level quality:
  - OPENING: drift=0.1886, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1992, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1820, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2044, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### singapore_hdb_waittime_crisis_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1899 (+/- 0.0019)
- Clean persona drift MAE: 0.1899
- Per-trait absolute error: O 0.1800, C 0.2800, E 0.1245, A 0.1760, N 0.1890
- Relationship inconsistency: 0.2610
- Relationship shift rate: 0.3316
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2164
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1873, 0.1925]

- Phase-level quality:
  - OPENING: drift=0.1931, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1900, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1973, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2039, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2016 (+/- 0.0033)
- Clean persona drift MAE: 0.2016
- Per-trait absolute error: O 0.2060, C 0.2800, E 0.1257, A 0.1805, N 0.2160
- Relationship inconsistency: 0.4875
- Relationship shift rate: 0.4139
- Relationship overshoot rate: 0.5250
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
- Dialogue coherence: 0.1978
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.197, 0.2062]

- Phase-level quality:
  - OPENING: drift=0.1938, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1978, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2055, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2098, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### singapore_hdb_waittime_crisis_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1949 (+/- 0.0023)
- Clean persona drift MAE: 0.1949
- Per-trait absolute error: O 0.2160, C 0.2800, E 0.1171, A 0.1515, N 0.2100
- Relationship inconsistency: 0.1834
- Relationship shift rate: 0.3856
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1848
- Repetition rate: 0.0000
- Topic drift rate: 0.2858
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1917, 0.1981]

- Phase-level quality:
  - OPENING: drift=0.1905, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1862, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.2028, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2039, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1543 (+/- 0.0041)
- Clean persona drift MAE: 0.1543
- Per-trait absolute error: O 0.1550, C 0.1780, E 0.1328, A 0.1704, N 0.1356
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2787
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.2333
- Repetition rate: 0.0000
- Topic drift rate: 0.8409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1487, 0.16]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1495, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1602, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1500, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1615 (+/- 0.0004)
- Clean persona drift MAE: 0.1615
- Per-trait absolute error: O 0.1840, C 0.1812, E 0.1383, A 0.1753, N 0.1289
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
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
- Dialogue coherence: 0.1778
- Repetition rate: 0.0416
- Topic drift rate: 0.8409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1609, 0.1621]

- Phase-level quality:
  - OPENING: drift=0.1817, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1525, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1745, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1523, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### starbucks_unionization_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1590 (+/- 0.0009)
- Clean persona drift MAE: 0.1590
- Per-trait absolute error: O 0.1810, C 0.1824, E 0.1308, A 0.1785, N 0.1222
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1450
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Dialogue coherence: 0.2427
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1578, 0.1602]

- Phase-level quality:
  - OPENING: drift=0.1802, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1498, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1639, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1568, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1453 (+/- 0.0052)
- Clean persona drift MAE: 0.1453
- Per-trait absolute error: O 0.1400, C 0.1000, E 0.1197, A 0.1667, N 0.2000
- Relationship inconsistency: 0.4165
- Relationship shift rate: 0.4245
- Relationship overshoot rate: 0.2750
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
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.1111
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1916
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1381, 0.1525]

- Phase-level quality:
  - OPENING: drift=0.1593, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1624, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1461, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1620, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0024)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1867, C 0.1147, E 0.1349, A 0.1667, N 0.2000
- Relationship inconsistency: 0.3775
- Relationship shift rate: 0.3448
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1990
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1573, 0.1639]

- Phase-level quality:
  - OPENING: drift=0.1592, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1644, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1568, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1654, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1496 (+/- 0.0007)
- Clean persona drift MAE: 0.1496
- Per-trait absolute error: O 0.1533, C 0.1074, E 0.1207, A 0.1667, N 0.2000
- Relationship inconsistency: 0.3166
- Relationship shift rate: 0.3710
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.5486
- Negotiation uniqueness: 0.1270
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1933
- Repetition rate: 0.0000
- Topic drift rate: 0.5455
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1486, 0.1506]

- Phase-level quality:
  - OPENING: drift=0.1547, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1619, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1522, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1640, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0010)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.1340, C 0.2000, E 0.1197, A 0.2285, N 0.2080
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.3791
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.0955
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2187
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1766, 0.1794]

- Phase-level quality:
  - OPENING: drift=0.1841, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1744, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1774, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.2251, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1876 (+/- 0.0067)
- Clean persona drift MAE: 0.1876
- Per-trait absolute error: O 0.1820, C 0.2022, E 0.1198, A 0.2320, N 0.2020
- Relationship inconsistency: 0.2028
- Relationship shift rate: 0.3573
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1839
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1783, 0.1969]

- Phase-level quality:
  - OPENING: drift=0.1914, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1794, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1829, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2334, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1891 (+/- 0.0001)
- Clean persona drift MAE: 0.1891
- Per-trait absolute error: O 0.1880, C 0.2044, E 0.1262, A 0.2250, N 0.2020
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4187
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.2916
- Negotiation uniqueness: 0.0917
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2247
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1891, 0.1892]

- Phase-level quality:
  - OPENING: drift=0.1971, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1778, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1863, convergence=1.0000, diversity=0.3750
  - CLOSING: drift=0.2212, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1603 (+/- 0.0091)
- Clean persona drift MAE: 0.1603
- Per-trait absolute error: O 0.1460, C 0.2050, E 0.1505, A 0.1322, N 0.1680
- Relationship inconsistency: 0.0599
- Relationship shift rate: 0.2593
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2447
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1478, 0.1729]

- Phase-level quality:
  - OPENING: drift=0.1704, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1666, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1655, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1633, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1778 (+/- 0.0001)
- Clean persona drift MAE: 0.1778
- Per-trait absolute error: O 0.1820, C 0.2247, E 0.1891, A 0.1331, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1750
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
- Dialogue coherence: 0.2302
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1777, 0.1778]

- Phase-level quality:
  - OPENING: drift=0.1784, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1782, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1769, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1694 (+/- 0.0064)
- Clean persona drift MAE: 0.1694
- Per-trait absolute error: O 0.1820, C 0.2029, E 0.1692, A 0.1323, N 0.1607
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2289
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1605, 0.1783]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1715, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1736, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1639, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1551 (+/- 0.0112)
- Clean persona drift MAE: 0.1551
- Per-trait absolute error: O 0.1767, C 0.2505, E 0.0782, A 0.1234, N 0.1467
- Relationship inconsistency: 0.0585
- Relationship shift rate: 0.2720
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2785
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1396, 0.1706]

- Phase-level quality:
  - OPENING: drift=0.1552, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1759, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1614, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1689, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1691 (+/- 0.0169)
- Clean persona drift MAE: 0.1691
- Per-trait absolute error: O 0.1600, C 0.3055, E 0.0969, A 0.1366, N 0.1467
- Relationship inconsistency: 0.5000
- Relationship shift rate: 0.4559
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2443
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1457, 0.1926]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1616, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1780, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1744, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1536 (+/- 0.0127)
- Clean persona drift MAE: 0.1536
- Per-trait absolute error: O 0.1600, C 0.2615, E 0.0699, A 0.1367, N 0.1400
- Relationship inconsistency: 0.1465
- Relationship shift rate: 0.2100
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2006
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.136, 0.1712]

- Phase-level quality:
  - OPENING: drift=0.1635, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1663, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1708, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1584, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### svb_bank_run_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0075)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1660, C 0.2059, E 0.1593, A 0.1210, N 0.2300
- Relationship inconsistency: 0.0120
- Relationship shift rate: 0.2882
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.7500
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
- Dialogue coherence: 0.2732
- Repetition rate: 0.1111
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.166, 0.1868]

- Phase-level quality:
  - OPENING: drift=0.1885, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1584, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1741, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2094, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### svb_bank_run_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1855 (+/- 0.0059)
- Clean persona drift MAE: 0.1855
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1986, A 0.1345, N 0.2200
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.3806
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
- Dialogue coherence: 0.2389
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1772, 0.1937]

- Phase-level quality:
  - OPENING: drift=0.1943, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1645, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1890, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2143, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1740 (+/- 0.0008)
- Clean persona drift MAE: 0.1740
- Per-trait absolute error: O 0.1640, C 0.2000, E 0.1815, A 0.1045, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2144
- Repetition rate: 0.0556
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1729, 0.1751]

- Phase-level quality:
  - OPENING: drift=0.1941, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1571, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1772, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### theranos_whistleblower_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1680 (+/- 0.0065)
- Clean persona drift MAE: 0.1680
- Per-trait absolute error: O 0.1530, C 0.2600, E 0.1278, A 0.1313, N 0.1678
- Relationship inconsistency: 0.0780
- Relationship shift rate: 0.4090
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5000
- Action family convergence: 1.0000
- Role action diversity: 0.3271
- Negotiation uniqueness: 0.0620
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2381
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.159, 0.177]

- Phase-level quality:
  - OPENING: drift=0.1685, convergence=0.5000, diversity=0.1000
  - TENSION: drift=0.1683, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1744, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.1653, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1736 (+/- 0.0024)
- Clean persona drift MAE: 0.1736
- Per-trait absolute error: O 0.1630, C 0.2600, E 0.1470, A 0.1316, N 0.1664
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.5362
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
- Dialogue coherence: 0.2225
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1703, 0.1769]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1739, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1750, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1820, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1695 (+/- 0.0023)
- Clean persona drift MAE: 0.1695
- Per-trait absolute error: O 0.1580, C 0.2600, E 0.1307, A 0.1293, N 0.1696
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5773
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
- Role action diversity: 0.2112
- Negotiation uniqueness: 0.0596
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2151
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1663, 0.1727]

- Phase-level quality:
  - OPENING: drift=0.1740, convergence=0.5000, diversity=0.1250
  - TENSION: drift=0.1753, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1712, convergence=1.0000, diversity=0.2000
  - CLOSING: drift=0.1702, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1772 (+/- 0.0018)
- Clean persona drift MAE: 0.1772
- Per-trait absolute error: O 0.1300, C 0.3000, E 0.1074, A 0.1483, N 0.2000
- Relationship inconsistency: 0.4393
- Relationship shift rate: 0.4936
- Relationship overshoot rate: 0.5000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
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
- Dialogue coherence: 0.2595
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1747, 0.1796]

- Phase-level quality:
  - OPENING: drift=0.1795, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1847, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1809, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1879, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0065)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1567, C 0.3000, E 0.0917, A 0.1400, N 0.2000
- Relationship inconsistency: 0.4842
- Relationship shift rate: 0.6583
- Relationship overshoot rate: 0.5000
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
- Dialogue coherence: 0.1732
- Repetition rate: 0.0000
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1687, 0.1866]

- Phase-level quality:
  - OPENING: drift=0.1810, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1940, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1774, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1891, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1805 (+/- 0.0010)
- Clean persona drift MAE: 0.1805
- Per-trait absolute error: O 0.1367, C 0.3000, E 0.1109, A 0.1550, N 0.2000
- Relationship inconsistency: 0.5745
- Relationship shift rate: 0.6158
- Relationship overshoot rate: 0.5250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
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
- Dialogue coherence: 0.1903
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1791, 0.1819]

- Phase-level quality:
  - OPENING: drift=0.1872, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1860, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1866, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1921, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2037 (+/- 0.0056)
- Clean persona drift MAE: 0.2037
- Per-trait absolute error: O 0.2360, C 0.2000, E 0.1771, A 0.2355, N 0.1700
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2961
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8000
- Clean envelope violations: 2.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2221
- Repetition rate: 0.1667
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1959, 0.2115]

- Phase-level quality:
  - OPENING: drift=0.2054, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1895, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.2066, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2110, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### theranos_whistleblower_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2053 (+/- 0.0018)
- Clean persona drift MAE: 0.2053
- Per-trait absolute error: O 0.1960, C 0.2152, E 0.1885, A 0.2470, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
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
- Dialogue coherence: 0.1546
- Repetition rate: 0.1111
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2028, 0.2078]

- Phase-level quality:
  - OPENING: drift=0.2107, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1949, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1994, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2144, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### theranos_whistleblower_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1993 (+/- 0.0005)
- Clean persona drift MAE: 0.1993
- Per-trait absolute error: O 0.1860, C 0.2193, E 0.1805, A 0.2350, N 0.1760
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4300
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9000
- Clean envelope violations: 2.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1864
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1987, 0.2]

- Phase-level quality:
  - OPENING: drift=0.2037, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1930, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1966, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2144, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1846 (+/- 0.0012)
- Clean persona drift MAE: 0.1846
- Per-trait absolute error: O 0.1750, C 0.1714, E 0.2063, A 0.1924, N 0.1778
- Relationship inconsistency: 0.1406
- Relationship shift rate: 0.3263
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2160
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1829, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1925, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1853, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1913, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1901, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1947 (+/- 0.0036)
- Clean persona drift MAE: 0.1947
- Per-trait absolute error: O 0.1990, C 0.1823, E 0.2092, A 0.2002, N 0.1829
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4850
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1808
- Repetition rate: 0.0000
- Topic drift rate: 0.1137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1897, 0.1997]

- Phase-level quality:
  - OPENING: drift=0.1932, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1998, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1927, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1951, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1930 (+/- 0.0014)
- Clean persona drift MAE: 0.1930
- Per-trait absolute error: O 0.1940, C 0.1914, E 0.2051, A 0.1931, N 0.1811
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2940
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1729
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1909, 0.195]

- Phase-level quality:
  - OPENING: drift=0.1951, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1956, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1920, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1958, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### uk_post_office_horizon_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0001)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.0767, C 0.3000, E 0.1091, A 0.2334, N 0.1066
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.1625
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2150
- Repetition rate: 0.0625
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1649, 0.1654]

- Phase-level quality:
  - OPENING: drift=0.1750, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1752, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1733, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1869, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate

### uk_post_office_horizon_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1767 (+/- 0.0018)
- Clean persona drift MAE: 0.1767
- Per-trait absolute error: O 0.1066, C 0.3140, E 0.1013, A 0.2616, N 0.1000
- Relationship inconsistency: 0.0360
- Relationship shift rate: 0.1075
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
- Dialogue coherence: 0.2168
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1742, 0.1792]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1740, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1722, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1915, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1649 (+/- 0.0024)
- Clean persona drift MAE: 0.1649
- Per-trait absolute error: O 0.1000, C 0.3000, E 0.1000, A 0.2250, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.6389
- Negotiation uniqueness: 0.2083
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2064
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1617, 0.1682]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1701, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1720, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1810, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1660 (+/- 0.0001)
- Clean persona drift MAE: 0.1660
- Per-trait absolute error: O 0.1660, C 0.2055, E 0.1310, A 0.2165, N 0.1110
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.3169
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2178
- Repetition rate: 0.0556
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1659, 0.1661]

- Phase-level quality:
  - OPENING: drift=0.1948, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1578, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1677, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2200, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### uk_post_office_horizon_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1819 (+/- 0.0029)
- Clean persona drift MAE: 0.1819
- Per-trait absolute error: O 0.1960, C 0.2094, E 0.1523, A 0.2255, N 0.1260
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3087
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
- Dialogue coherence: 0.1895
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1779, 0.1858]

- Phase-level quality:
  - OPENING: drift=0.2012, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1686, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1797, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2150, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1782 (+/- 0.0010)
- Clean persona drift MAE: 0.1782
- Per-trait absolute error: O 0.2140, C 0.2027, E 0.1331, A 0.2215, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1895
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1768, 0.1797]

- Phase-level quality:
  - OPENING: drift=0.1998, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1631, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1729, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2235, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1713 (+/- 0.0016)
- Clean persona drift MAE: 0.1713
- Per-trait absolute error: O 0.2080, C 0.1866, E 0.2094, A 0.1548, N 0.0974
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1366
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.2000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2470
- Repetition rate: 0.0416
- Topic drift rate: 0.2954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.169, 0.1735]

- Phase-level quality:
  - OPENING: drift=0.1678, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1827, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1654, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1896, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### wework_ipo_collapse_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0004)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.2170, C 0.2022, E 0.2208, A 0.1587, N 0.1016
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2139
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
- Dialogue coherence: 0.2162
- Repetition rate: 0.0000
- Topic drift rate: 0.2046
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1794, 0.1807]

- Phase-level quality:
  - OPENING: drift=0.1759, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1875, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1703, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1902, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0012)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.2210, C 0.1907, E 0.2102, A 0.1545, N 0.1007
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.2000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2016
- Repetition rate: 0.0416
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1737, 0.1771]

- Phase-level quality:
  - OPENING: drift=0.1698, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1843, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1671, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1870, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### wework_ipo_collapse_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1807 (+/- 0.0040)
- Clean persona drift MAE: 0.1807
- Per-trait absolute error: O 0.1233, C 0.2000, E 0.1504, A 0.2167, N 0.2133
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2633
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2579
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1751, 0.1864]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1860, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1876, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2110, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1949 (+/- 0.0009)
- Clean persona drift MAE: 0.1949
- Per-trait absolute error: O 0.1400, C 0.2147, E 0.1763, A 0.2100, N 0.2333
- Relationship inconsistency: 0.1613
- Relationship shift rate: 0.3507
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
- Dialogue coherence: 0.2575
- Repetition rate: 0.2500
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1937, 0.196]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2016, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1975, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2254, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### wework_ipo_collapse_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0050)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1333, C 0.2000, E 0.1232, A 0.1916, N 0.2333
- Relationship inconsistency: 0.4215
- Relationship shift rate: 0.4000
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2151
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1694, 0.1833]

- Phase-level quality:
  - OPENING: drift=0.1892, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1947, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2175, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1569 (+/- 0.0017)
- Clean persona drift MAE: 0.1569
- Per-trait absolute error: O 0.1460, C 0.1839, E 0.1706, A 0.1350, N 0.1490
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1650
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2405
- Repetition rate: 0.0556
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1545, 0.1593]

- Phase-level quality:
  - OPENING: drift=0.1778, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1774, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1424, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1669, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### wework_ipo_collapse_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1736 (+/- 0.0008)
- Clean persona drift MAE: 0.1736
- Per-trait absolute error: O 0.1740, C 0.2132, E 0.1908, A 0.1445, N 0.1460
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1640
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
- Dialogue coherence: 0.2188
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1726, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1733, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1710, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1631, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1696, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1547 (+/- 0.0055)
- Clean persona drift MAE: 0.1547
- Per-trait absolute error: O 0.1340, C 0.1641, E 0.1762, A 0.1445, N 0.1550
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2809
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2280
- Repetition rate: 0.0000
- Topic drift rate: 0.2858
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1472, 0.1623]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1754, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1446, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1587, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1844 (+/- 0.0004)
- Clean persona drift MAE: 0.1844
- Per-trait absolute error: O 0.1620, C 0.2800, E 0.1535, A 0.1674, N 0.1589
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.4163
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.8667
- Role action diversity: 0.2917
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2549
- Repetition rate: 0.0416
- Topic drift rate: 0.2954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1837, 0.185]

- Phase-level quality:
  - OPENING: drift=0.1908, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1870, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1924, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1855, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### zoom_return_to_office_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1919 (+/- 0.0013)
- Clean persona drift MAE: 0.1919
- Per-trait absolute error: O 0.1930, C 0.2800, E 0.1669, A 0.1650, N 0.1544
- Relationship inconsistency: 0.0710
- Relationship shift rate: 0.4308
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1941
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1901, 0.1937]

- Phase-level quality:
  - OPENING: drift=0.1873, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1988, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1968, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1835, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1891 (+/- 0.0011)
- Clean persona drift MAE: 0.1891
- Per-trait absolute error: O 0.1880, C 0.2800, E 0.1630, A 0.1620, N 0.1527
- Relationship inconsistency: 0.3625
- Relationship shift rate: 0.4035
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.8667
- Role action diversity: 0.2917
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2361
- Repetition rate: 0.0000
- Topic drift rate: 0.1364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1876, 0.1906]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1979, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1941, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1818, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0086)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.0667, C 0.2333, E 0.1954, A 0.1650, N 0.2000
- Relationship inconsistency: 0.1006
- Relationship shift rate: 0.2596
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2502
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1602, 0.184]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1840, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2084, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1915, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1916 (+/- 0.0049)
- Clean persona drift MAE: 0.1916
- Per-trait absolute error: O 0.1700, C 0.2773, E 0.1592, A 0.1517, N 0.2000
- Relationship inconsistency: 0.0780
- Relationship shift rate: 0.2488
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
- Dialogue coherence: 0.2207
- Repetition rate: 0.0000
- Topic drift rate: 0.1818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1848, 0.1984]

- Phase-level quality:
  - OPENING: drift=0.1905, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2011, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2016, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1925, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1731 (+/- 0.0045)
- Clean persona drift MAE: 0.1731
- Per-trait absolute error: O 0.1533, C 0.2407, E 0.1385, A 0.1333, N 0.2000
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.2027
- Relationship overshoot rate: 0.0000
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
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2167
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.167, 0.1793]

- Phase-level quality:
  - OPENING: drift=0.1767, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1945, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2044, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1805, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2066 (+/- 0.0029)
- Clean persona drift MAE: 0.2066
- Per-trait absolute error: O 0.2380, C 0.2200, E 0.2051, A 0.1975, N 0.1720
- Relationship inconsistency: 0.0630
- Relationship shift rate: 0.2335
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2399
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2025, 0.2106]

- Phase-level quality:
  - OPENING: drift=0.2120, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2010, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2025, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2450, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2147 (+/- 0.0063)
- Clean persona drift MAE: 0.2147
- Per-trait absolute error: O 0.2620, C 0.2354, E 0.2150, A 0.2010, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3970
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2111
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.206, 0.2234]

- Phase-level quality:
  - OPENING: drift=0.2126, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2089, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2163, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2147 (+/- 0.0014)
- Clean persona drift MAE: 0.2147
- Per-trait absolute error: O 0.2580, C 0.2354, E 0.2127, A 0.1990, N 0.1680
- Relationship inconsistency: 0.0360
- Relationship shift rate: 0.3191
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2016
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2126, 0.2167]

- Phase-level quality:
  - OPENING: drift=0.2179, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2048, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2142, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1697 (+/- 0.0142)
- Clean persona drift MAE: 0.1697
- Per-trait absolute error: O 0.1534, C 0.2197, E 0.1409, A 0.1677, N 0.1670
- Relationship inconsistency: 0.0895
- Relationship shift rate: 0.2654
- Relationship overshoot rate: 0.2492
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0567
- Clean envelope violations: 2.0567
- Structured action validity: 0.4622
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.4333
- Action-plan alignment: 0.9707
- Planned action coverage: 0.9071
- Action family convergence: 0.7597
- Role action diversity: 0.4762
- Negotiation uniqueness: 0.2661
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2369
- Repetition rate: 0.0437
- Topic drift rate: 0.3832
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1661, 0.1733]

- Phase-level quality:
  - OPENING: drift=0.1768, convergence=0.7145, diversity=0.3422
  - TENSION: drift=0.1738, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1743, convergence=0.6789, diversity=0.4792
  - CLOSING: drift=0.1807, convergence=0.7500, diversity=0.5417

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### exploratory:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1820 (+/- 0.0152)
- Clean persona drift MAE: 0.1820
- Per-trait absolute error: O 0.1797, C 0.2304, E 0.1580, A 0.1725, N 0.1695
- Relationship inconsistency: 0.1388
- Relationship shift rate: 0.3323
- Relationship overshoot rate: 0.3062
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3511
- Clean envelope violations: 2.3511
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
- Dialogue coherence: 0.2079
- Repetition rate: 0.0229
- Topic drift rate: 0.3509
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1782, 0.1859]

- Phase-level quality:
  - OPENING: drift=0.1822, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1790, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1814, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1867, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### exploratory:naive_informed
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1733 (+/- 0.0147)
- Clean persona drift MAE: 0.1733
- Per-trait absolute error: O 0.1684, C 0.2205, E 0.1428, A 0.1674, N 0.1673
- Relationship inconsistency: 0.0949
- Relationship shift rate: 0.2713
- Relationship overshoot rate: 0.2125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2122
- Clean envelope violations: 2.2122
- Structured action validity: 0.4622
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.5667
- Action-plan alignment: 0.9707
- Planned action coverage: 0.9087
- Action family convergence: 0.7597
- Role action diversity: 0.4774
- Negotiation uniqueness: 0.2712
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2024
- Repetition rate: 0.0051
- Topic drift rate: 0.3755
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1696, 0.177]

- Phase-level quality:
  - OPENING: drift=0.1793, convergence=0.7145, diversity=0.3430
  - TENSION: drift=0.1766, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1760, convergence=0.6456, diversity=0.4650
  - CLOSING: drift=0.1824, convergence=0.7000, diversity=0.5167

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### guided:engine_dialogue_only
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1684 (+/- 0.0193)
- Clean persona drift MAE: 0.1684
- Per-trait absolute error: O 0.1557, C 0.2173, E 0.1362, A 0.1615, N 0.1714
- Relationship inconsistency: 0.1353
- Relationship shift rate: 0.2858
- Relationship overshoot rate: 0.2417
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0372
- Clean envelope violations: 2.0372
- Structured action validity: 0.7957
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9666
- Planned action coverage: 0.9351
- Action family convergence: 0.6839
- Role action diversity: 0.5235
- Negotiation uniqueness: 0.2933
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2335
- Repetition rate: 0.0118
- Topic drift rate: 0.3931
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1635, 0.1733]

- Phase-level quality:
  - OPENING: drift=0.1752, convergence=0.8111, diversity=0.3755
  - TENSION: drift=0.1739, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1723, convergence=0.5944, diversity=0.5256
  - CLOSING: drift=0.1829, convergence=0.5500, diversity=0.6097

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### guided:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1783 (+/- 0.0178)
- Clean persona drift MAE: 0.1783
- Per-trait absolute error: O 0.1880, C 0.2231, E 0.1427, A 0.1659, N 0.1720
- Relationship inconsistency: 0.2007
- Relationship shift rate: 0.3631
- Relationship overshoot rate: 0.3631
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3194
- Clean envelope violations: 2.3194
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
- Dialogue coherence: 0.1979
- Repetition rate: 0.0049
- Topic drift rate: 0.3133
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1738, 0.1828]

- Phase-level quality:
  - OPENING: drift=0.1785, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1780, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1788, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1851, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### guided:naive_informed
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1737 (+/- 0.0172)
- Clean persona drift MAE: 0.1737
- Per-trait absolute error: O 0.1816, C 0.2222, E 0.1348, A 0.1590, N 0.1710
- Relationship inconsistency: 0.1431
- Relationship shift rate: 0.2847
- Relationship overshoot rate: 0.2588
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1028
- Clean envelope violations: 2.1028
- Structured action validity: 0.7957
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.1833
- Action-plan alignment: 0.9666
- Planned action coverage: 0.9351
- Action family convergence: 0.6839
- Role action diversity: 0.5260
- Negotiation uniqueness: 0.2960
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2114
- Repetition rate: 0.0157
- Topic drift rate: 0.3485
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1694, 0.1781]

- Phase-level quality:
  - OPENING: drift=0.1761, convergence=0.7945, diversity=0.3686
  - TENSION: drift=0.1762, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1751, convergence=0.5944, diversity=0.5256
  - CLOSING: drift=0.1832, convergence=0.4833, diversity=0.5806

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate


## Family Summary
### algorithmic_accountability:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1733 (+/- 0.0062)
- Clean persona drift MAE: 0.1733
- Per-trait absolute error: O 0.1400, C 0.2333, E 0.1298, A 0.2333, N 0.1300
- Relationship inconsistency: 0.4970
- Relationship shift rate: 0.4562
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2177
- Repetition rate: 0.1875
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1647, 0.1818]

- Phase-level quality:
  - OPENING: drift=0.1771, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1822, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1840, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### algorithmic_accountability:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1856 (+/- 0.0035)
- Clean persona drift MAE: 0.1856
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1477, A 0.2333, N 0.1234
- Relationship inconsistency: 0.0435
- Relationship shift rate: 0.4707
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
- Dialogue coherence: 0.1819
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1807, 0.1905]

- Phase-level quality:
  - OPENING: drift=0.1917, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1860, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1843, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### algorithmic_accountability:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1840 (+/- 0.0028)
- Clean persona drift MAE: 0.1840
- Per-trait absolute error: O 0.1734, C 0.2333, E 0.1467, A 0.2333, N 0.1333
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.5316
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1773
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1801, 0.1879]

- Phase-level quality:
  - OPENING: drift=0.1867, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1845, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_acquisition:engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1733 (+/- 0.0137)
- Clean persona drift MAE: 0.1733
- Per-trait absolute error: O 0.1888, C 0.2247, E 0.1267, A 0.1516, N 0.1745
- Relationship inconsistency: 0.2351
- Relationship shift rate: 0.3849
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.7667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9783
- Planned action coverage: 1.0000
- Action family convergence: 0.5278
- Role action diversity: 0.6042
- Negotiation uniqueness: 0.3311
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2480
- Repetition rate: 0.0208
- Topic drift rate: 0.3095
- Fallback taxonomy: n/a
- State trajectory variance: 0.0079
- Mean turns: 15.67
- Persona drift 95% CI: [0.1623, 0.1842]

- Phase-level quality:
  - OPENING: drift=0.1835, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1785, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1681, convergence=0.4778, diversity=0.6389
  - CLOSING: drift=0.1882, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_acquisition:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1789 (+/- 0.0141)
- Clean persona drift MAE: 0.1789
- Per-trait absolute error: O 0.1898, C 0.2220, E 0.1394, A 0.1574, N 0.1860
- Relationship inconsistency: 0.1067
- Relationship shift rate: 0.3399
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4111
- Clean envelope violations: 2.4111
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
- Dialogue coherence: 0.2123
- Repetition rate: 0.0000
- Topic drift rate: 0.2262
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1676, 0.1902]

- Phase-level quality:
  - OPENING: drift=0.1854, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1819, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1727, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1963, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_acquisition:naive_informed
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1739 (+/- 0.0139)
- Clean persona drift MAE: 0.1739
- Per-trait absolute error: O 0.1908, C 0.2230, E 0.1288, A 0.1493, N 0.1775
- Relationship inconsistency: 0.0010
- Relationship shift rate: 0.1504
- Relationship overshoot rate: 0.0750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.7667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9783
- Planned action coverage: 1.0000
- Action family convergence: 0.5278
- Role action diversity: 0.6042
- Negotiation uniqueness: 0.3311
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2093
- Repetition rate: 0.0000
- Topic drift rate: 0.2208
- Fallback taxonomy: n/a
- State trajectory variance: 0.0077
- Mean turns: 15.67
- Persona drift 95% CI: [0.1627, 0.185]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1803, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1692, convergence=0.4778, diversity=0.6389
  - CLOSING: drift=0.1951, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_crisis:engine_dialogue_only
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1702 (+/- 0.0085)
- Clean persona drift MAE: 0.1702
- Per-trait absolute error: O 0.1432, C 0.2200, E 0.1689, A 0.1635, N 0.1552
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.2356
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9166
- Clean envelope violations: 1.9166
- Structured action validity: 0.4083
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3750
- Action-plan alignment: 0.9704
- Planned action coverage: 1.0000
- Action family convergence: 0.7584
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2511
- Repetition rate: 0.0469
- Topic drift rate: 0.5227
- Fallback taxonomy: n/a
- State trajectory variance: 0.0072
- Mean turns: 16.50
- Persona drift 95% CI: [0.1643, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1780, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1744, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1773, convergence=0.7750, diversity=0.4167
  - CLOSING: drift=0.1835, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_crisis:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1837 (+/- 0.0071)
- Clean persona drift MAE: 0.1837
- Per-trait absolute error: O 0.1700, C 0.2349, E 0.1865, A 0.1551, N 0.1718
- Relationship inconsistency: 0.1650
- Relationship shift rate: 0.2823
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.2227
- Repetition rate: 0.0781
- Topic drift rate: 0.5227
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1788, 0.1886]

- Phase-level quality:
  - OPENING: drift=0.1831, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1851, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1837, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1913, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### corporate_crisis:naive_informed
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1727 (+/- 0.0057)
- Clean persona drift MAE: 0.1727
- Per-trait absolute error: O 0.1627, C 0.2213, E 0.1598, A 0.1577, N 0.1619
- Relationship inconsistency: 0.1454
- Relationship shift rate: 0.2581
- Relationship overshoot rate: 0.2812
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1667
- Clean envelope violations: 2.1667
- Structured action validity: 0.4083
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3750
- Action-plan alignment: 0.9704
- Planned action coverage: 1.0000
- Action family convergence: 0.7584
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2040
- Repetition rate: 0.0104
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0072
- Mean turns: 16.50
- Persona drift 95% CI: [0.1688, 0.1766]

- Phase-level quality:
  - OPENING: drift=0.1787, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1798, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1747, convergence=0.7750, diversity=0.4167
  - CLOSING: drift=0.1867, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_crisis_management:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1569 (+/- 0.0017)
- Clean persona drift MAE: 0.1569
- Per-trait absolute error: O 0.1460, C 0.1839, E 0.1706, A 0.1350, N 0.1490
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1650
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2405
- Repetition rate: 0.0556
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1545, 0.1593]

- Phase-level quality:
  - OPENING: drift=0.1778, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1774, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1424, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1669, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### corporate_crisis_management:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1736 (+/- 0.0008)
- Clean persona drift MAE: 0.1736
- Per-trait absolute error: O 0.1740, C 0.2132, E 0.1908, A 0.1445, N 0.1460
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1640
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
- Dialogue coherence: 0.2188
- Repetition rate: 0.0000
- Topic drift rate: 0.1786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1726, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1733, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1710, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1631, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1696, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1547 (+/- 0.0055)
- Clean persona drift MAE: 0.1547
- Per-trait absolute error: O 0.1340, C 0.1641, E 0.1762, A 0.1445, N 0.1550
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2809
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2280
- Repetition rate: 0.0000
- Topic drift rate: 0.2858
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1472, 0.1623]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1754, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1446, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1587, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1844 (+/- 0.0004)
- Clean persona drift MAE: 0.1844
- Per-trait absolute error: O 0.1620, C 0.2800, E 0.1535, A 0.1674, N 0.1589
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.4163
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.8667
- Role action diversity: 0.2917
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2549
- Repetition rate: 0.0416
- Topic drift rate: 0.2954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1837, 0.185]

- Phase-level quality:
  - OPENING: drift=0.1908, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1870, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1924, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1855, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### corporate_policy_change:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1919 (+/- 0.0013)
- Clean persona drift MAE: 0.1919
- Per-trait absolute error: O 0.1930, C 0.2800, E 0.1669, A 0.1650, N 0.1544
- Relationship inconsistency: 0.0710
- Relationship shift rate: 0.4308
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1941
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1901, 0.1937]

- Phase-level quality:
  - OPENING: drift=0.1873, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1988, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1968, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1835, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1891 (+/- 0.0011)
- Clean persona drift MAE: 0.1891
- Per-trait absolute error: O 0.1880, C 0.2800, E 0.1630, A 0.1620, N 0.1527
- Relationship inconsistency: 0.3625
- Relationship shift rate: 0.4035
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.8667
- Role action diversity: 0.2917
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2361
- Repetition rate: 0.0000
- Topic drift rate: 0.1364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1876, 0.1906]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1979, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1941, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1818, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1487 (+/- 0.0040)
- Clean persona drift MAE: 0.1487
- Per-trait absolute error: O 0.1020, C 0.2000, E 0.1432, A 0.1305, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2583
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Dialogue coherence: 0.2282
- Repetition rate: 0.0556
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1431, 0.1544]

- Phase-level quality:
  - OPENING: drift=0.1797, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1304, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1569, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1955, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### corporate_turnaround:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1569 (+/- 0.0064)
- Clean persona drift MAE: 0.1569
- Per-trait absolute error: O 0.1540, C 0.2011, E 0.1513, A 0.1130, N 0.1650
- Relationship inconsistency: 0.0225
- Relationship shift rate: 0.3720
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
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
- Dialogue coherence: 0.2219
- Repetition rate: 0.1111
- Topic drift rate: 0.6429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.148, 0.1658]

- Phase-level quality:
  - OPENING: drift=0.1760, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1360, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1573, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1940, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### corporate_turnaround:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1577 (+/- 0.0012)
- Clean persona drift MAE: 0.1577
- Per-trait absolute error: O 0.1540, C 0.2061, E 0.1417, A 0.1210, N 0.1660
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3100
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
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
- Dialogue coherence: 0.1983
- Repetition rate: 0.0000
- Topic drift rate: 0.5714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.156, 0.1594]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1413, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1575, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1946, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### corporate_whistleblowing:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1859 (+/- 0.0189)
- Clean persona drift MAE: 0.1859
- Per-trait absolute error: O 0.1945, C 0.2300, E 0.1525, A 0.1834, N 0.1689
- Relationship inconsistency: 0.0390
- Relationship shift rate: 0.3525
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.6666
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9625
- Planned action coverage: 0.7500
- Action family convergence: 0.8750
- Role action diversity: 0.4135
- Negotiation uniqueness: 0.2095
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2301
- Repetition rate: 0.0833
- Topic drift rate: 0.5698
- Fallback taxonomy: n/a
- State trajectory variance: 0.0057
- Mean turns: 18.00
- Persona drift 95% CI: [0.1674, 0.2043]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=0.7500, diversity=0.1750
  - TENSION: drift=0.1789, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1905, convergence=0.6666, diversity=0.5208
  - CLOSING: drift=0.1882, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_whistleblowing:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1895 (+/- 0.0160)
- Clean persona drift MAE: 0.1895
- Per-trait absolute error: O 0.1795, C 0.2376, E 0.1677, A 0.1893, N 0.1732
- Relationship inconsistency: 0.0690
- Relationship shift rate: 0.3356
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1885
- Repetition rate: 0.0556
- Topic drift rate: 0.4659
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1738, 0.2051]

- Phase-level quality:
  - OPENING: drift=0.1931, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1844, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1872, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1982, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### corporate_whistleblowing:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1844 (+/- 0.0150)
- Clean persona drift MAE: 0.1844
- Per-trait absolute error: O 0.1720, C 0.2396, E 0.1556, A 0.1822, N 0.1728
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5036
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
- Structured action validity: 0.6666
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9625
- Planned action coverage: 0.7500
- Action family convergence: 0.8750
- Role action diversity: 0.3556
- Negotiation uniqueness: 0.2084
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2008
- Repetition rate: 0.0000
- Topic drift rate: 0.5617
- Fallback taxonomy: n/a
- State trajectory variance: 0.0057
- Mean turns: 18.00
- Persona drift 95% CI: [0.1697, 0.1991]

- Phase-level quality:
  - OPENING: drift=0.1889, convergence=0.7500, diversity=0.1875
  - TENSION: drift=0.1841, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1839, convergence=0.6666, diversity=0.4750
  - CLOSING: drift=0.1923, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### ethical_dilemma:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1772 (+/- 0.0018)
- Clean persona drift MAE: 0.1772
- Per-trait absolute error: O 0.1300, C 0.3000, E 0.1074, A 0.1483, N 0.2000
- Relationship inconsistency: 0.4393
- Relationship shift rate: 0.4936
- Relationship overshoot rate: 0.5000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
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
- Dialogue coherence: 0.2595
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1747, 0.1796]

- Phase-level quality:
  - OPENING: drift=0.1795, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1847, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1809, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1879, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0065)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1567, C 0.3000, E 0.0917, A 0.1400, N 0.2000
- Relationship inconsistency: 0.4842
- Relationship shift rate: 0.6583
- Relationship overshoot rate: 0.5000
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
- Dialogue coherence: 0.1732
- Repetition rate: 0.0000
- Topic drift rate: 0.0454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1687, 0.1866]

- Phase-level quality:
  - OPENING: drift=0.1810, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1940, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1774, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1891, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1805 (+/- 0.0010)
- Clean persona drift MAE: 0.1805
- Per-trait absolute error: O 0.1367, C 0.3000, E 0.1109, A 0.1550, N 0.2000
- Relationship inconsistency: 0.5745
- Relationship shift rate: 0.6158
- Relationship overshoot rate: 0.5250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
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
- Dialogue coherence: 0.1903
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1791, 0.1819]

- Phase-level quality:
  - OPENING: drift=0.1872, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1860, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1866, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1921, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1577 (+/- 0.0105)
- Clean persona drift MAE: 0.1577
- Per-trait absolute error: O 0.1613, C 0.2278, E 0.1143, A 0.1278, N 0.1573
- Relationship inconsistency: 0.0592
- Relationship shift rate: 0.2656
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0417
- Clean envelope violations: 2.0417
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7125
- Role action diversity: 0.4896
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2616
- Repetition rate: 0.0000
- Topic drift rate: 0.7387
- Fallback taxonomy: n/a
- State trajectory variance: 0.0054
- Mean turns: 16.50
- Persona drift 95% CI: [0.1474, 0.168]

- Phase-level quality:
  - OPENING: drift=0.1628, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1712, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1635, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1661, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_contagion:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1734 (+/- 0.0127)
- Clean persona drift MAE: 0.1734
- Per-trait absolute error: O 0.1710, C 0.2651, E 0.1430, A 0.1348, N 0.1533
- Relationship inconsistency: 0.2500
- Relationship shift rate: 0.3154
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2083
- Clean envelope violations: 2.2083
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
- Dialogue coherence: 0.2372
- Repetition rate: 0.0000
- Topic drift rate: 0.6136
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.161, 0.1859]

- Phase-level quality:
  - OPENING: drift=0.1758, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1674, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1781, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1756, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1615 (+/- 0.0128)
- Clean persona drift MAE: 0.1615
- Per-trait absolute error: O 0.1710, C 0.2322, E 0.1196, A 0.1345, N 0.1503
- Relationship inconsistency: 0.0732
- Relationship shift rate: 0.1050
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.8000
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
- Dialogue coherence: 0.2148
- Repetition rate: 0.0000
- Topic drift rate: 0.6250
- Fallback taxonomy: n/a
- State trajectory variance: 0.0054
- Mean turns: 16.50
- Persona drift 95% CI: [0.149, 0.174]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1689, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1722, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1612, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1620 (+/- 0.0019)
- Clean persona drift MAE: 0.1620
- Per-trait absolute error: O 0.1710, C 0.2097, E 0.1085, A 0.1303, N 0.1904
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1375
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9738
- Planned action coverage: 0.9546
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2365
- Repetition rate: 0.0000
- Topic drift rate: 0.3637
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1594, 0.1646]

- Phase-level quality:
  - OPENING: drift=0.1693, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1638, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1758, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1540, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1706 (+/- 0.0015)
- Clean persona drift MAE: 0.1706
- Per-trait absolute error: O 0.2010, C 0.2073, E 0.1239, A 0.1289, N 0.1922
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3109
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
- Dialogue coherence: 0.2143
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1685, 0.1728]

- Phase-level quality:
  - OPENING: drift=0.1740, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1653, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1808, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1623, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1681 (+/- 0.0045)
- Clean persona drift MAE: 0.1681
- Per-trait absolute error: O 0.1930, C 0.2085, E 0.1213, A 0.1361, N 0.1820
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2712
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2024
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1618, 0.1745]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1713, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1750, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1593, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0075)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1660, C 0.2059, E 0.1593, A 0.1210, N 0.2300
- Relationship inconsistency: 0.0120
- Relationship shift rate: 0.2882
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.7500
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
- Dialogue coherence: 0.2732
- Repetition rate: 0.1111
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.166, 0.1868]

- Phase-level quality:
  - OPENING: drift=0.1885, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1584, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1741, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2094, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### financial_crisis_management:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1855 (+/- 0.0059)
- Clean persona drift MAE: 0.1855
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1986, A 0.1345, N 0.2200
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.3806
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
- Dialogue coherence: 0.2389
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1772, 0.1937]

- Phase-level quality:
  - OPENING: drift=0.1943, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1645, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1890, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2143, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1740 (+/- 0.0008)
- Clean persona drift MAE: 0.1740
- Per-trait absolute error: O 0.1640, C 0.2000, E 0.1815, A 0.1045, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2144
- Repetition rate: 0.0556
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1729, 0.1751]

- Phase-level quality:
  - OPENING: drift=0.1941, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1571, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1772, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### financial_scandal:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1732 (+/- 0.0090)
- Clean persona drift MAE: 0.1732
- Per-trait absolute error: O 0.1936, C 0.1950, E 0.1687, A 0.1562, N 0.1527
- Relationship inconsistency: 0.1507
- Relationship shift rate: 0.2695
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5000
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9607
- Planned action coverage: 0.6363
- Action family convergence: 0.7084
- Role action diversity: 0.5521
- Negotiation uniqueness: 0.2455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2179
- Repetition rate: 0.0278
- Topic drift rate: 0.3182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1644, 0.1821]

- Phase-level quality:
  - OPENING: drift=0.1709, convergence=0.3333, diversity=0.2500
  - TENSION: drift=0.1868, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1775, convergence=0.6666, diversity=0.5833
  - CLOSING: drift=0.1850, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### financial_scandal:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1965 (+/- 0.0067)
- Clean persona drift MAE: 0.1965
- Per-trait absolute error: O 0.2620, C 0.2295, E 0.1832, A 0.1588, N 0.1487
- Relationship inconsistency: 0.2062
- Relationship shift rate: 0.2274
- Relationship overshoot rate: 0.3750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5667
- Clean envelope violations: 2.5667
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
- Dialogue coherence: 0.2015
- Repetition rate: 0.0556
- Topic drift rate: 0.1883
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1899, 0.203]

- Phase-level quality:
  - OPENING: drift=0.1719, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1867, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1880, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2006, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### financial_scandal:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1790 (+/- 0.0217)
- Clean persona drift MAE: 0.1790
- Per-trait absolute error: O 0.2287, C 0.1931, E 0.1732, A 0.1536, N 0.1467
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1462
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.5000
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9607
- Planned action coverage: 0.6363
- Action family convergence: 0.7084
- Role action diversity: 0.5382
- Negotiation uniqueness: 0.2976
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1995
- Repetition rate: 0.0000
- Topic drift rate: 0.2776
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1577, 0.2003]

- Phase-level quality:
  - OPENING: drift=0.1769, convergence=0.3333, diversity=0.2500
  - TENSION: drift=0.1867, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1819, convergence=0.4166, diversity=0.5000
  - CLOSING: drift=0.1908, convergence=0.2500, diversity=0.6250

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1809 (+/- 0.0000)
- Clean persona drift MAE: 0.1809
- Per-trait absolute error: O 0.1570, C 0.2409, E 0.1431, A 0.2271, N 0.1366
- Relationship inconsistency: 0.2500
- Relationship shift rate: 0.3704
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1989
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1809, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1883, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1784, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1921, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1658, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0043)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1740, C 0.2471, E 0.1651, A 0.2245, N 0.1345
- Relationship inconsistency: 0.2251
- Relationship shift rate: 0.4196
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1896
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.183, 0.1951]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1817, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2009, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1683, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1839 (+/- 0.0022)
- Clean persona drift MAE: 0.1839
- Per-trait absolute error: O 0.1790, C 0.2416, E 0.1487, A 0.2239, N 0.1265
- Relationship inconsistency: 0.3470
- Relationship shift rate: 0.3641
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1970
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1809, 0.1869]

- Phase-level quality:
  - OPENING: drift=0.1897, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1795, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1993, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1686, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### historical_injustice:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0001)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.0767, C 0.3000, E 0.1091, A 0.2334, N 0.1066
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.1625
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2150
- Repetition rate: 0.0625
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1649, 0.1654]

- Phase-level quality:
  - OPENING: drift=0.1750, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1752, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1733, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1869, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate

### historical_injustice:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1767 (+/- 0.0018)
- Clean persona drift MAE: 0.1767
- Per-trait absolute error: O 0.1066, C 0.3140, E 0.1013, A 0.2616, N 0.1000
- Relationship inconsistency: 0.0360
- Relationship shift rate: 0.1075
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
- Dialogue coherence: 0.2168
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1742, 0.1792]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1740, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1722, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1915, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### historical_injustice:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1649 (+/- 0.0024)
- Clean persona drift MAE: 0.1649
- Per-trait absolute error: O 0.1000, C 0.3000, E 0.1000, A 0.2250, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.6389
- Negotiation uniqueness: 0.2083
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2064
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1617, 0.1682]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1701, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1720, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1810, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1721 (+/- 0.0086)
- Clean persona drift MAE: 0.1721
- Per-trait absolute error: O 0.0667, C 0.2333, E 0.1954, A 0.1650, N 0.2000
- Relationship inconsistency: 0.1006
- Relationship shift rate: 0.2596
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6667
- Clean envelope violations: 1.6667
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2502
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1602, 0.184]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1840, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2084, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1915, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1916 (+/- 0.0049)
- Clean persona drift MAE: 0.1916
- Per-trait absolute error: O 0.1700, C 0.2773, E 0.1592, A 0.1517, N 0.2000
- Relationship inconsistency: 0.0780
- Relationship shift rate: 0.2488
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
- Dialogue coherence: 0.2207
- Repetition rate: 0.0000
- Topic drift rate: 0.1818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1848, 0.1984]

- Phase-level quality:
  - OPENING: drift=0.1905, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2011, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2016, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1925, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1731 (+/- 0.0045)
- Clean persona drift MAE: 0.1731
- Per-trait absolute error: O 0.1533, C 0.2407, E 0.1385, A 0.1333, N 0.2000
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.2027
- Relationship overshoot rate: 0.0000
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
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2167
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.167, 0.1793]

- Phase-level quality:
  - OPENING: drift=0.1767, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1945, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2044, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1805, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### infrastructure_decision:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0008)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1700, C 0.1958, E 0.1517, A 0.1225, N 0.2100
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1116
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.0714
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2309
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1689, 0.1711]

- Phase-level quality:
  - OPENING: drift=0.1708, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1911, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1674, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1794, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### infrastructure_decision:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1860 (+/- 0.0008)
- Clean persona drift MAE: 0.1860
- Per-trait absolute error: O 0.1900, C 0.2112, E 0.1744, A 0.1340, N 0.2200
- Relationship inconsistency: 0.0225
- Relationship shift rate: 0.2755
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.2018
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1849, 0.187]

- Phase-level quality:
  - OPENING: drift=0.1806, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1849, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1797, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1749, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### infrastructure_decision:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1851 (+/- 0.0050)
- Clean persona drift MAE: 0.1851
- Per-trait absolute error: O 0.2020, C 0.2310, E 0.1585, A 0.1110, N 0.2230
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.2041
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.0769
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2030
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1782, 0.192]

- Phase-level quality:
  - OPENING: drift=0.1806, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1921, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1770, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1871, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### institutional_failure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1660 (+/- 0.0001)
- Clean persona drift MAE: 0.1660
- Per-trait absolute error: O 0.1660, C 0.2055, E 0.1310, A 0.2165, N 0.1110
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.3169
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2178
- Repetition rate: 0.0556
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1659, 0.1661]

- Phase-level quality:
  - OPENING: drift=0.1948, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1578, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1677, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2200, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### institutional_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1819 (+/- 0.0029)
- Clean persona drift MAE: 0.1819
- Per-trait absolute error: O 0.1960, C 0.2094, E 0.1523, A 0.2255, N 0.1260
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3087
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
- Dialogue coherence: 0.1895
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1779, 0.1858]

- Phase-level quality:
  - OPENING: drift=0.2012, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1686, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1797, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2150, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1782 (+/- 0.0010)
- Clean persona drift MAE: 0.1782
- Per-trait absolute error: O 0.2140, C 0.2027, E 0.1331, A 0.2215, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1895
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1768, 0.1797]

- Phase-level quality:
  - OPENING: drift=0.1998, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1631, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1729, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2235, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1846 (+/- 0.0012)
- Clean persona drift MAE: 0.1846
- Per-trait absolute error: O 0.1750, C 0.1714, E 0.2063, A 0.1924, N 0.1778
- Relationship inconsistency: 0.1406
- Relationship shift rate: 0.3263
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2160
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1829, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1925, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1853, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1913, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1901, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1947 (+/- 0.0036)
- Clean persona drift MAE: 0.1947
- Per-trait absolute error: O 0.1990, C 0.1823, E 0.2092, A 0.2002, N 0.1829
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4850
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1808
- Repetition rate: 0.0000
- Topic drift rate: 0.1137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1897, 0.1997]

- Phase-level quality:
  - OPENING: drift=0.1932, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1998, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1927, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1951, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1930 (+/- 0.0014)
- Clean persona drift MAE: 0.1930
- Per-trait absolute error: O 0.1940, C 0.1914, E 0.2051, A 0.1931, N 0.1811
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2940
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9795
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1729
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1909, 0.195]

- Phase-level quality:
  - OPENING: drift=0.1951, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1956, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1920, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1958, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_dispute:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1780 (+/- 0.0010)
- Clean persona drift MAE: 0.1780
- Per-trait absolute error: O 0.1340, C 0.2000, E 0.1197, A 0.2285, N 0.2080
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.3791
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.0955
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2187
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1766, 0.1794]

- Phase-level quality:
  - OPENING: drift=0.1841, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1744, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1774, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.2251, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_dispute:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1876 (+/- 0.0067)
- Clean persona drift MAE: 0.1876
- Per-trait absolute error: O 0.1820, C 0.2022, E 0.1198, A 0.2320, N 0.2020
- Relationship inconsistency: 0.2028
- Relationship shift rate: 0.3573
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1839
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1783, 0.1969]

- Phase-level quality:
  - OPENING: drift=0.1914, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1794, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1829, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2334, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_dispute:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1891 (+/- 0.0001)
- Clean persona drift MAE: 0.1891
- Per-trait absolute error: O 0.1880, C 0.2044, E 0.1262, A 0.2250, N 0.2020
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4187
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6000
- Clean envelope violations: 2.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.2916
- Negotiation uniqueness: 0.0917
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2247
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1891, 0.1892]

- Phase-level quality:
  - OPENING: drift=0.1971, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1778, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1863, convergence=1.0000, diversity=0.3750
  - CLOSING: drift=0.2212, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_negotiation:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1453 (+/- 0.0052)
- Clean persona drift MAE: 0.1453
- Per-trait absolute error: O 0.1400, C 0.1000, E 0.1197, A 0.1667, N 0.2000
- Relationship inconsistency: 0.4165
- Relationship shift rate: 0.4245
- Relationship overshoot rate: 0.2750
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
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.1111
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1916
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1381, 0.1525]

- Phase-level quality:
  - OPENING: drift=0.1593, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1624, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1461, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1620, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_negotiation:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0024)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1867, C 0.1147, E 0.1349, A 0.1667, N 0.2000
- Relationship inconsistency: 0.3775
- Relationship shift rate: 0.3448
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.1990
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1573, 0.1639]

- Phase-level quality:
  - OPENING: drift=0.1592, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1644, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1568, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1654, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_negotiation:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1496 (+/- 0.0007)
- Clean persona drift MAE: 0.1496
- Per-trait absolute error: O 0.1533, C 0.1074, E 0.1207, A 0.1667, N 0.2000
- Relationship inconsistency: 0.3166
- Relationship shift rate: 0.3710
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.5486
- Negotiation uniqueness: 0.1270
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1933
- Repetition rate: 0.0000
- Topic drift rate: 0.5455
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1486, 0.1506]

- Phase-level quality:
  - OPENING: drift=0.1547, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1619, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1522, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1640, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_policy_reform:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1558 (+/- 0.0035)
- Clean persona drift MAE: 0.1558
- Per-trait absolute error: O 0.1660, C 0.1724, E 0.1289, A 0.1481, N 0.1636
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3960
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2737
- Repetition rate: 0.0833
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1509, 0.1607]

- Phase-level quality:
  - OPENING: drift=0.1553, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1732, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1564, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1568, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### labor_policy_reform:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1682 (+/- 0.0013)
- Clean persona drift MAE: 0.1682
- Per-trait absolute error: O 0.2150, C 0.1710, E 0.1488, A 0.1461, N 0.1600
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.4969
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
- Dialogue coherence: 0.1733
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1664, 0.17]

- Phase-level quality:
  - OPENING: drift=0.1564, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1882, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1660, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1643, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1610 (+/- 0.0035)
- Clean persona drift MAE: 0.1610
- Per-trait absolute error: O 0.2000, C 0.1711, E 0.1304, A 0.1418, N 0.1618
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3753
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2083
- Repetition rate: 0.0416
- Topic drift rate: 0.8181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1561, 0.1659]

- Phase-level quality:
  - OPENING: drift=0.1483, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1807, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1651, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1629, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### labor_reform:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1523 (+/- 0.0029)
- Clean persona drift MAE: 0.1523
- Per-trait absolute error: O 0.1580, C 0.2400, E 0.0701, A 0.1075, N 0.1860
- Relationship inconsistency: 0.1136
- Relationship shift rate: 0.3334
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
- Dialogue coherence: 0.2301
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1483, 0.1563]

- Phase-level quality:
  - OPENING: drift=0.1640, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1395, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1462, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1533 (+/- 0.0005)
- Clean persona drift MAE: 0.1533
- Per-trait absolute error: O 0.1580, C 0.2508, E 0.0706, A 0.1070, N 0.1800
- Relationship inconsistency: 0.5510
- Relationship shift rate: 0.4419
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
- Dialogue coherence: 0.2009
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1526, 0.154]

- Phase-level quality:
  - OPENING: drift=0.1689, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1417, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1468, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2040, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_reform:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1501 (+/- 0.0024)
- Clean persona drift MAE: 0.1501
- Per-trait absolute error: O 0.1620, C 0.2400, E 0.0666, A 0.0980, N 0.1840
- Relationship inconsistency: 0.2778
- Relationship shift rate: 0.3683
- Relationship overshoot rate: 0.4750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
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
- Dialogue coherence: 0.1984
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1468, 0.1534]

- Phase-level quality:
  - OPENING: drift=0.1649, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1447, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1437, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1543 (+/- 0.0041)
- Clean persona drift MAE: 0.1543
- Per-trait absolute error: O 0.1550, C 0.1780, E 0.1328, A 0.1704, N 0.1356
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2787
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.2333
- Repetition rate: 0.0000
- Topic drift rate: 0.8409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1487, 0.16]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1495, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1602, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1500, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1615 (+/- 0.0004)
- Clean persona drift MAE: 0.1615
- Per-trait absolute error: O 0.1840, C 0.1812, E 0.1383, A 0.1753, N 0.1289
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
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
- Dialogue coherence: 0.1778
- Repetition rate: 0.0416
- Topic drift rate: 0.8409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1609, 0.1621]

- Phase-level quality:
  - OPENING: drift=0.1817, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1525, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1745, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1523, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### labor_relations:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1590 (+/- 0.0009)
- Clean persona drift MAE: 0.1590
- Per-trait absolute error: O 0.1810, C 0.1824, E 0.1308, A 0.1785, N 0.1222
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1450
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
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
- Dialogue coherence: 0.2427
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1578, 0.1602]

- Phase-level quality:
  - OPENING: drift=0.1802, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1498, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1639, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1568, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_rights:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1911 (+/- 0.0039)
- Clean persona drift MAE: 0.1911
- Per-trait absolute error: O 0.2100, C 0.2400, E 0.0905, A 0.2217, N 0.1933
- Relationship inconsistency: 0.3518
- Relationship shift rate: 0.4718
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.1056
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2155
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1857, 0.1965]

- Phase-level quality:
  - OPENING: drift=0.1910, convergence=0.5000, diversity=0.1666
  - TENSION: drift=0.1976, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1900, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1774, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_rights:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2000 (+/- 0.0015)
- Clean persona drift MAE: 0.2000
- Per-trait absolute error: O 0.2600, C 0.2333, E 0.1169, A 0.1834, N 0.2067
- Relationship inconsistency: 0.2720
- Relationship shift rate: 0.4587
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
- Dialogue coherence: 0.2006
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1979, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.2019, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2009, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2011, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1620, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_rights:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1904 (+/- 0.0009)
- Clean persona drift MAE: 0.1904
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.0917, A 0.1834, N 0.2000
- Relationship inconsistency: 0.6350
- Relationship shift rate: 0.5804
- Relationship overshoot rate: 0.4929
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.7222
- Negotiation uniqueness: 0.1667
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1955
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1892, 0.1915]

- Phase-level quality:
  - OPENING: drift=0.1954, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1954, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1880, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1696, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### platform_governance:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1900 (+/- 0.0156)
- Clean persona drift MAE: 0.1900
- Per-trait absolute error: O 0.1957, C 0.2122, E 0.1792, A 0.1811, N 0.1817
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.3165
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2667
- Clean envelope violations: 2.2667
- Structured action validity: 0.7571
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2072
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- State trajectory variance: 0.0031
- Mean turns: 16.50
- Persona drift 95% CI: [0.1747, 0.2053]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1993, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1908, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1809, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_governance:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1976 (+/- 0.0119)
- Clean persona drift MAE: 0.1976
- Per-trait absolute error: O 0.2165, C 0.2176, E 0.1909, A 0.1816, N 0.1818
- Relationship inconsistency: 0.1938
- Relationship shift rate: 0.4019
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5583
- Clean envelope violations: 2.5583
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
- Dialogue coherence: 0.1605
- Repetition rate: 0.0000
- Topic drift rate: 0.3523
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.186, 0.2093]

- Phase-level quality:
  - OPENING: drift=0.1929, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1998, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1990, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1795, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_governance:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1887 (+/- 0.0081)
- Clean persona drift MAE: 0.1887
- Per-trait absolute error: O 0.1948, C 0.2150, E 0.1786, A 0.1747, N 0.1804
- Relationship inconsistency: 0.1688
- Relationship shift rate: 0.2549
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3167
- Clean envelope violations: 2.3167
- Structured action validity: 0.7571
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1997
- Repetition rate: 0.0000
- Topic drift rate: 0.4886
- Fallback taxonomy: n/a
- State trajectory variance: 0.0031
- Mean turns: 16.50
- Persona drift 95% CI: [0.1808, 0.1966]

- Phase-level quality:
  - OPENING: drift=0.1906, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1967, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1938, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1800, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1934 (+/- 0.0016)
- Clean persona drift MAE: 0.1934
- Per-trait absolute error: O 0.1480, C 0.2205, E 0.1981, A 0.1785, N 0.2220
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.1175
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8000
- Clean envelope violations: 2.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2050
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1912, 0.1956]

- Phase-level quality:
  - OPENING: drift=0.2129, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1960, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1802, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2036 (+/- 0.0010)
- Clean persona drift MAE: 0.2036
- Per-trait absolute error: O 0.2020, C 0.2088, E 0.2120, A 0.1820, N 0.2130
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2660
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1705
- Repetition rate: 0.0000
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2022, 0.205]

- Phase-level quality:
  - OPENING: drift=0.2132, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1930, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1898, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2408, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2031 (+/- 0.0010)
- Clean persona drift MAE: 0.2031
- Per-trait absolute error: O 0.1820, C 0.2148, E 0.1923, A 0.1985, N 0.2280
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.2863
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2073
- Repetition rate: 0.0000
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2018, 0.2045]

- Phase-level quality:
  - OPENING: drift=0.2126, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1941, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1830, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_failure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1369 (+/- 0.0005)
- Clean persona drift MAE: 0.1369
- Per-trait absolute error: O 0.1300, C 0.1811, E 0.0827, A 0.1815, N 0.1090
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4275
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.1909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1870
- Repetition rate: 0.0000
- Topic drift rate: 0.0357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1362, 0.1376]

- Phase-level quality:
  - OPENING: drift=0.1479, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1375, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1234, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1790, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### policy_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1536 (+/- 0.0020)
- Clean persona drift MAE: 0.1536
- Per-trait absolute error: O 0.1740, C 0.2086, E 0.0887, A 0.1925, N 0.1040
- Relationship inconsistency: 0.4845
- Relationship shift rate: 0.4475
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
- Dialogue coherence: 0.1918
- Repetition rate: 0.0000
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1508, 0.1564]

- Phase-level quality:
  - OPENING: drift=0.1483, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1411, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1365, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1891, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### policy_failure:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1494 (+/- 0.0010)
- Clean persona drift MAE: 0.1494
- Per-trait absolute error: O 0.1640, C 0.1800, E 0.0913, A 0.2030, N 0.1090
- Relationship inconsistency: 0.3893
- Relationship shift rate: 0.3770
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.1909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1828
- Repetition rate: 0.0000
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1481, 0.1508]

- Phase-level quality:
  - OPENING: drift=0.1498, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1404, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1291, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1990, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### policy_negotiation:engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1486 (+/- 0.0086)
- Clean persona drift MAE: 0.1486
- Per-trait absolute error: O 0.1067, C 0.1890, E 0.1227, A 0.1482, N 0.1764
- Relationship inconsistency: 0.3068
- Relationship shift rate: 0.3194
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.8095
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.3333
- Action-plan alignment: 0.9635
- Planned action coverage: 1.0000
- Action family convergence: 0.5972
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3247
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2326
- Repetition rate: 0.0000
- Topic drift rate: 0.3561
- Fallback taxonomy: n/a
- State trajectory variance: 0.0069
- Mean turns: 15.67
- Persona drift 95% CI: [0.1417, 0.1555]

- Phase-level quality:
  - OPENING: drift=0.1500, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1610, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1556, convergence=0.6111, diversity=0.5278
  - CLOSING: drift=0.1599, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### policy_negotiation:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0020)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1769, C 0.1945, E 0.1347, A 0.1454, N 0.1780
- Relationship inconsistency: 0.4238
- Relationship shift rate: 0.4117
- Relationship overshoot rate: 0.4562
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0722
- Clean envelope violations: 2.0722
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
- Dialogue coherence: 0.2150
- Repetition rate: 0.0000
- Topic drift rate: 0.3604
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1643, 0.1675]

- Phase-level quality:
  - OPENING: drift=0.1583, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1603, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1688, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1674, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_negotiation:naive_informed
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0046)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.1691, C 0.1987, E 0.1275, A 0.1383, N 0.1731
- Relationship inconsistency: 0.3143
- Relationship shift rate: 0.3732
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8056
- Clean envelope violations: 1.8056
- Structured action validity: 0.8095
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9635
- Planned action coverage: 1.0000
- Action family convergence: 0.5972
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3247
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2266
- Repetition rate: 0.0208
- Topic drift rate: 0.2922
- Fallback taxonomy: n/a
- State trajectory variance: 0.0069
- Mean turns: 15.67
- Persona drift 95% CI: [0.1577, 0.165]

- Phase-level quality:
  - OPENING: drift=0.1536, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1605, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1651, convergence=0.6111, diversity=0.5278
  - CLOSING: drift=0.1581, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate

### post-disaster_recovery:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1656 (+/- 0.0085)
- Clean persona drift MAE: 0.1656
- Per-trait absolute error: O 0.1503, C 0.2328, E 0.1321, A 0.1193, N 0.1937
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0663
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2084
- Clean envelope violations: 2.2084
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9784
- Planned action coverage: 1.0000
- Action family convergence: 0.6083
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2457
- Repetition rate: 0.0729
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0030
- Mean turns: 16.50
- Persona drift 95% CI: [0.1573, 0.174]

- Phase-level quality:
  - OPENING: drift=0.1664, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1768, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1661, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1803, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate

### post-disaster_recovery:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1805 (+/- 0.0070)
- Clean persona drift MAE: 0.1805
- Per-trait absolute error: O 0.1687, C 0.2400, E 0.1437, A 0.1564, N 0.1936
- Relationship inconsistency: 0.2188
- Relationship shift rate: 0.2985
- Relationship overshoot rate: 0.2550
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5084
- Clean envelope violations: 2.5084
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
- Dialogue coherence: 0.2253
- Repetition rate: 0.0208
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1737, 0.1874]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1883, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1693, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1886, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### post-disaster_recovery:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0086)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1520, C 0.2270, E 0.1261, A 0.1256, N 0.1957
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1263
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2750
- Clean envelope violations: 2.2750
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9784
- Planned action coverage: 1.0000
- Action family convergence: 0.6083
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2078
- Repetition rate: 0.0000
- Topic drift rate: 0.4432
- Fallback taxonomy: n/a
- State trajectory variance: 0.0030
- Mean turns: 16.50
- Persona drift 95% CI: [0.1569, 0.1737]

- Phase-level quality:
  - OPENING: drift=0.1615, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1802, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1667, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1886, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_health_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1819 (+/- 0.0060)
- Clean persona drift MAE: 0.1819
- Per-trait absolute error: O 0.1700, C 0.2505, E 0.1284, A 0.1745, N 0.1860
- Relationship inconsistency: 0.0699
- Relationship shift rate: 0.3422
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2421
- Repetition rate: 0.0000
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1736, 0.1902]

- Phase-level quality:
  - OPENING: drift=0.1704, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1726, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1927, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1594, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1797 (+/- 0.0134)
- Clean persona drift MAE: 0.1797
- Per-trait absolute error: O 0.1800, C 0.2510, E 0.1280, A 0.1475, N 0.1920
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2573
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
- Dialogue coherence: 0.2064
- Repetition rate: 0.0000
- Topic drift rate: 0.0357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1611, 0.1983]

- Phase-level quality:
  - OPENING: drift=0.1701, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1662, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2009, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1680, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_crisis:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1691 (+/- 0.0020)
- Clean persona drift MAE: 0.1691
- Per-trait absolute error: O 0.1540, C 0.2499, E 0.1116, A 0.1500, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2425
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2147
- Repetition rate: 0.0556
- Topic drift rate: 0.0714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1663, 0.172]

- Phase-level quality:
  - OPENING: drift=0.1732, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1620, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1885, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1593, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### public_health_failure:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1838 (+/- 0.0142)
- Clean persona drift MAE: 0.1838
- Per-trait absolute error: O 0.1630, C 0.2112, E 0.1377, A 0.2038, N 0.2034
- Relationship inconsistency: 0.1997
- Relationship shift rate: 0.3149
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2666
- Clean envelope violations: 2.2666
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9784
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2721
- Repetition rate: 0.0833
- Topic drift rate: 0.5114
- Fallback taxonomy: n/a
- State trajectory variance: 0.0075
- Mean turns: 16.50
- Persona drift 95% CI: [0.1699, 0.1977]

- Phase-level quality:
  - OPENING: drift=0.1873, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1878, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1896, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1977, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate

### public_health_failure:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2010 (+/- 0.0305)
- Clean persona drift MAE: 0.2010
- Per-trait absolute error: O 0.2100, C 0.2117, E 0.1643, A 0.2224, N 0.1966
- Relationship inconsistency: 0.0856
- Relationship shift rate: 0.3297
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8750
- Clean envelope violations: 2.8750
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
- Dialogue coherence: 0.2205
- Repetition rate: 0.0000
- Topic drift rate: 0.3637
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1711, 0.2309]

- Phase-level quality:
  - OPENING: drift=0.1957, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1991, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1983, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2030, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_failure:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1864 (+/- 0.0221)
- Clean persona drift MAE: 0.1864
- Per-trait absolute error: O 0.1790, C 0.2074, E 0.1330, A 0.2136, N 0.1989
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2825
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4083
- Clean envelope violations: 2.4083
- Structured action validity: 0.6333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9784
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2210
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0075
- Mean turns: 16.50
- Persona drift 95% CI: [0.1647, 0.2081]

- Phase-level quality:
  - OPENING: drift=0.1887, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1931, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1900, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1851, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_housing_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1823 (+/- 0.0003)
- Clean persona drift MAE: 0.1823
- Per-trait absolute error: O 0.1933, C 0.2667, E 0.1000, A 0.1850, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1750
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2283
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1819, 0.1827]

- Phase-level quality:
  - OPENING: drift=0.1824, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1916, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1910, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2050, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1884 (+/- 0.0064)
- Clean persona drift MAE: 0.1884
- Per-trait absolute error: O 0.1767, C 0.2667, E 0.1001, A 0.2316, N 0.1667
- Relationship inconsistency: 0.1420
- Relationship shift rate: 0.2188
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8334
- Clean envelope violations: 2.8334
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
- Dialogue coherence: 0.1744
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1795, 0.1972]

- Phase-level quality:
  - OPENING: drift=0.1909, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1880, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1880, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2092, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1829 (+/- 0.0016)
- Clean persona drift MAE: 0.1829
- Per-trait absolute error: O 0.1767, C 0.2667, E 0.1013, A 0.2034, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3334
- Clean envelope violations: 2.3334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1945
- Repetition rate: 0.0625
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1807, 0.1851]

- Phase-level quality:
  - OPENING: drift=0.1886, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1992, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1820, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2044, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### public_policy:engine_dialogue_only
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1630 (+/- 0.0106)
- Clean persona drift MAE: 0.1630
- Per-trait absolute error: O 0.1260, C 0.2098, E 0.1353, A 0.1611, N 0.1828
- Relationship inconsistency: 0.0596
- Relationship shift rate: 0.2685
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8167
- Clean envelope violations: 1.8167
- Structured action validity: 0.4167
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.1250
- Action-plan alignment: 0.9761
- Planned action coverage: 1.0000
- Action family convergence: 0.5854
- Role action diversity: 0.5938
- Negotiation uniqueness: 0.4026
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2201
- Repetition rate: 0.0156
- Topic drift rate: 0.1713
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1556, 0.1703]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1705, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1727, convergence=0.4833, diversity=0.6459
  - CLOSING: drift=0.1594, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### public_policy:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1736 (+/- 0.0084)
- Clean persona drift MAE: 0.1736
- Per-trait absolute error: O 0.1457, C 0.2065, E 0.1586, A 0.1671, N 0.1902
- Relationship inconsistency: 0.0920
- Relationship shift rate: 0.3684
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1901
- Repetition rate: 0.0000
- Topic drift rate: 0.2565
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1678, 0.1794]

- Phase-level quality:
  - OPENING: drift=0.1835, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1767, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1785, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1629, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy:naive_informed
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1677 (+/- 0.0086)
- Clean persona drift MAE: 0.1677
- Per-trait absolute error: O 0.1336, C 0.2054, E 0.1425, A 0.1698, N 0.1870
- Relationship inconsistency: 0.1324
- Relationship shift rate: 0.3616
- Relationship overshoot rate: 0.2812
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8875
- Clean envelope violations: 1.8875
- Structured action validity: 0.4167
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9761
- Planned action coverage: 1.0000
- Action family convergence: 0.5854
- Role action diversity: 0.5938
- Negotiation uniqueness: 0.4026
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1934
- Repetition rate: 0.0156
- Topic drift rate: 0.1380
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1617, 0.1737]

- Phase-level quality:
  - OPENING: drift=0.1782, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1733, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1745, convergence=0.4833, diversity=0.6459
  - CLOSING: drift=0.1617, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### public_policy_crisis:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1895 (+/- 0.0015)
- Clean persona drift MAE: 0.1895
- Per-trait absolute error: O 0.1690, C 0.2600, E 0.1620, A 0.1852, N 0.1713
- Relationship inconsistency: 0.1703
- Relationship shift rate: 0.3245
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9562
- Planned action coverage: 0.7046
- Action family convergence: 0.7916
- Role action diversity: 0.4260
- Negotiation uniqueness: 0.2407
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2253
- Repetition rate: 0.0000
- Topic drift rate: 0.3977
- Fallback taxonomy: n/a
- State trajectory variance: 0.0047
- Mean turns: 18.00
- Persona drift 95% CI: [0.188, 0.191]

- Phase-level quality:
  - OPENING: drift=0.1888, convergence=0.8334, diversity=0.3833
  - TENSION: drift=0.1899, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.1925, convergence=0.6666, diversity=0.4667
  - CLOSING: drift=0.2004, convergence=1.0000, diversity=0.3958

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy_crisis:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1949 (+/- 0.0074)
- Clean persona drift MAE: 0.1949
- Per-trait absolute error: O 0.1820, C 0.2600, E 0.1604, A 0.1881, N 0.1841
- Relationship inconsistency: 0.4097
- Relationship shift rate: 0.4266
- Relationship overshoot rate: 0.4875
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
- Dialogue coherence: 0.2068
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1877, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1966, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1958, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1992, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy_crisis:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1905 (+/- 0.0047)
- Clean persona drift MAE: 0.1905
- Per-trait absolute error: O 0.1870, C 0.2600, E 0.1492, A 0.1745, N 0.1818
- Relationship inconsistency: 0.1733
- Relationship shift rate: 0.3847
- Relationship overshoot rate: 0.4725
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2750
- Clean envelope violations: 2.2750
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9562
- Planned action coverage: 0.7046
- Action family convergence: 0.7916
- Role action diversity: 0.4729
- Negotiation uniqueness: 0.2438
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1970
- Repetition rate: 0.0208
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0047
- Mean turns: 18.00
- Persona drift 95% CI: [0.1858, 0.1951]

- Phase-level quality:
  - OPENING: drift=0.1837, convergence=0.8334, diversity=0.3625
  - TENSION: drift=0.1866, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.1937, convergence=0.6666, diversity=0.4875
  - CLOSING: drift=0.2008, convergence=0.7500, diversity=0.3333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### regulatory_compliance:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1498 (+/- 0.0083)
- Clean persona drift MAE: 0.1498
- Per-trait absolute error: O 0.1623, C 0.1718, E 0.1280, A 0.1307, N 0.1563
- Relationship inconsistency: 0.0381
- Relationship shift rate: 0.2732
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7334
- Clean envelope violations: 1.7334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9698
- Planned action coverage: 1.0000
- Action family convergence: 0.4791
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4415
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2634
- Repetition rate: 0.0312
- Topic drift rate: 0.3490
- Fallback taxonomy: n/a
- State trajectory variance: 0.0017
- Mean turns: 12.50
- Persona drift 95% CI: [0.1417, 0.1579]

- Phase-level quality:
  - OPENING: drift=0.1693, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1633, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1703, convergence=0.4166, diversity=0.7084
  - CLOSING: drift=0.1846, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### regulatory_compliance:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1723 (+/- 0.0075)
- Clean persona drift MAE: 0.1723
- Per-trait absolute error: O 0.2377, C 0.1922, E 0.1250, A 0.1457, N 0.1610
- Relationship inconsistency: 0.4625
- Relationship shift rate: 0.4459
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1833
- Clean envelope violations: 2.1833
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
- Dialogue coherence: 0.2044
- Repetition rate: 0.0000
- Topic drift rate: 0.1542
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.165, 0.1797]

- Phase-level quality:
  - OPENING: drift=0.1718, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1758, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1764, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1929, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_compliance:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1657 (+/- 0.0020)
- Clean persona drift MAE: 0.1657
- Per-trait absolute error: O 0.2293, C 0.2021, E 0.1214, A 0.1223, N 0.1533
- Relationship inconsistency: 0.1465
- Relationship shift rate: 0.4057
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7833
- Clean envelope violations: 1.7833
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9698
- Planned action coverage: 1.0000
- Action family convergence: 0.4791
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4415
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2121
- Repetition rate: 0.0000
- Topic drift rate: 0.1996
- Fallback taxonomy: n/a
- State trajectory variance: 0.0017
- Mean turns: 12.50
- Persona drift 95% CI: [0.1637, 0.1677]

- Phase-level quality:
  - OPENING: drift=0.1737, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1751, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1679, convergence=0.4166, diversity=0.7084
  - CLOSING: drift=0.1774, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1591 (+/- 0.0032)
- Clean persona drift MAE: 0.1591
- Per-trait absolute error: O 0.1790, C 0.2500, E 0.1137, A 0.1456, N 0.1071
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
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
- Dialogue coherence: 0.2272
- Repetition rate: 0.0416
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1547, 0.1634]

- Phase-level quality:
  - OPENING: drift=0.1574, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1638, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1552, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1599, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### regulatory_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1621 (+/- 0.0016)
- Clean persona drift MAE: 0.1621
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1285, A 0.1516, N 0.1022
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
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
- Dialogue coherence: 0.2001
- Repetition rate: 0.0416
- Topic drift rate: 0.1819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1599, 0.1643]

- Phase-level quality:
  - OPENING: drift=0.1580, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1558, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1653, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### regulatory_crisis:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1547 (+/- 0.0036)
- Clean persona drift MAE: 0.1547
- Per-trait absolute error: O 0.1730, C 0.2500, E 0.1130, A 0.1375, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.7143
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
- Dialogue coherence: 0.2336
- Repetition rate: 0.0416
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1497, 0.1597]

- Phase-level quality:
  - OPENING: drift=0.1516, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1607, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1523, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1634, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### regulatory_decision:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1698 (+/- 0.0054)
- Clean persona drift MAE: 0.1698
- Per-trait absolute error: O 0.1283, C 0.2800, E 0.0956, A 0.1699, N 0.1753
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9685
- Planned action coverage: 1.0000
- Action family convergence: 0.8334
- Role action diversity: 0.4688
- Negotiation uniqueness: 0.2694
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2748
- Repetition rate: 0.0312
- Topic drift rate: 0.0893
- Fallback taxonomy: n/a
- State trajectory variance: 0.0042
- Mean turns: 12.50
- Persona drift 95% CI: [0.1645, 0.1751]

- Phase-level quality:
  - OPENING: drift=0.1741, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1643, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1755, convergence=0.6666, diversity=0.5416
  - CLOSING: drift=0.1840, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate

### regulatory_decision:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1783 (+/- 0.0095)
- Clean persona drift MAE: 0.1783
- Per-trait absolute error: O 0.1504, C 0.2800, E 0.0994, A 0.1911, N 0.1707
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0963
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5333
- Clean envelope violations: 2.5333
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
- Dialogue coherence: 0.2195
- Repetition rate: 0.0312
- Topic drift rate: 0.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.169, 0.1876]

- Phase-level quality:
  - OPENING: drift=0.1797, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1656, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1830, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1902, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### regulatory_decision:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1739 (+/- 0.0093)
- Clean persona drift MAE: 0.1739
- Per-trait absolute error: O 0.1380, C 0.2800, E 0.0962, A 0.1755, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0581
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
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
- Dialogue coherence: 0.2256
- Repetition rate: 0.0312
- Topic drift rate: 0.0227
- Fallback taxonomy: n/a
- State trajectory variance: 0.0042
- Mean turns: 12.50
- Persona drift 95% CI: [0.1648, 0.1831]

- Phase-level quality:
  - OPENING: drift=0.1784, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1633, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1764, convergence=0.6666, diversity=0.5416
  - CLOSING: drift=0.1890, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate

### regulatory_transition:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0030)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.1590, C 0.2059, E 0.1200, A 0.1569, N 0.1644
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2830
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
- Structured action validity: 0.4286
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2381
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.157, 0.1655]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1658, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1584, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1723, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0013)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1730, C 0.2124, E 0.1195, A 0.1636, N 0.1578
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4605
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2018
- Repetition rate: 0.0000
- Topic drift rate: 0.3863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1634, 0.167]

- Phase-level quality:
  - OPENING: drift=0.1768, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1752, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1637, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1668, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1732 (+/- 0.0020)
- Clean persona drift MAE: 0.1732
- Per-trait absolute error: O 0.1920, C 0.2105, E 0.1255, A 0.1761, N 0.1618
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4175
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
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
- Dialogue coherence: 0.2172
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1704, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1805, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1799, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1655, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1742, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1497 (+/- 0.0129)
- Clean persona drift MAE: 0.1497
- Per-trait absolute error: O 0.1325, C 0.2121, E 0.1439, A 0.1392, N 0.1206
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2898
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.8572
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9669
- Planned action coverage: 1.0000
- Action family convergence: 0.5250
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2093
- Repetition rate: 0.0000
- Topic drift rate: 0.1916
- Fallback taxonomy: n/a
- State trajectory variance: 0.0042
- Mean turns: 18.00
- Persona drift 95% CI: [0.137, 0.1623]

- Phase-level quality:
  - OPENING: drift=0.1517, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1577, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1535, convergence=0.4667, diversity=0.6250
  - CLOSING: drift=0.1530, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### urban_policy:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1595 (+/- 0.0154)
- Clean persona drift MAE: 0.1595
- Per-trait absolute error: O 0.1515, C 0.2299, E 0.1548, A 0.1404, N 0.1212
- Relationship inconsistency: 0.1733
- Relationship shift rate: 0.4940
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
- Dialogue coherence: 0.1897
- Repetition rate: 0.0000
- Topic drift rate: 0.1104
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1444, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1528, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1582, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1639, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1547, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1595 (+/- 0.0127)
- Clean persona drift MAE: 0.1595
- Per-trait absolute error: O 0.1590, C 0.2249, E 0.1523, A 0.1409, N 0.1205
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2913
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8250
- Clean envelope violations: 1.8250
- Structured action validity: 0.8572
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9669
- Planned action coverage: 1.0000
- Action family convergence: 0.5250
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2061
- Repetition rate: 0.0486
- Topic drift rate: 0.1640
- Fallback taxonomy: n/a
- State trajectory variance: 0.0042
- Mean turns: 18.00
- Persona drift 95% CI: [0.147, 0.172]

- Phase-level quality:
  - OPENING: drift=0.1540, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1583, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1640, convergence=0.4667, diversity=0.6250
  - CLOSING: drift=0.1577, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### workplace_policy:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2066 (+/- 0.0029)
- Clean persona drift MAE: 0.2066
- Per-trait absolute error: O 0.2380, C 0.2200, E 0.2051, A 0.1975, N 0.1720
- Relationship inconsistency: 0.0630
- Relationship shift rate: 0.2335
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2399
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2025, 0.2106]

- Phase-level quality:
  - OPENING: drift=0.2120, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2010, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2025, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2450, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2147 (+/- 0.0063)
- Clean persona drift MAE: 0.2147
- Per-trait absolute error: O 0.2620, C 0.2354, E 0.2150, A 0.2010, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3970
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.2111
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.206, 0.2234]

- Phase-level quality:
  - OPENING: drift=0.2126, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2089, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2163, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2147 (+/- 0.0014)
- Clean persona drift MAE: 0.2147
- Per-trait absolute error: O 0.2580, C 0.2354, E 0.2127, A 0.1990, N 0.1680
- Relationship inconsistency: 0.0360
- Relationship shift rate: 0.3191
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.2016
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2126, 0.2167]

- Phase-level quality:
  - OPENING: drift=0.2179, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2048, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2142, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Feature Attribution: What Drives Each Trait Score

### Openness (O) — Mean Error: 0.1711

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| idea_count | 0.694 | 0.151 | 0.197 |
| hypothetical_count | 0.000 | 0.000 | 0.001 |
| unique_word_ratio | 0.642 | 0.672 | 0.670 |

Calibration: static

### Conscientiousness (C) — Mean Error: 0.2222

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| planning_count | 2.121 | 1.374 | 1.688 |
| structure_marker_count | 0.007 | 0.006 | 0.007 |
| detail_count | 0.000 | 0.000 | 0.000 |
| goal_reference_count | 0.000 | 0.000 | 0.000 |
| correction_count | 0.000 | 0.000 | 0.000 |

Calibration: dynamic

### Extraversion (E) — Mean Error: 0.1426

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| exclamation_count | 0.000 | 0.000 | 0.000 |
| question_count | 0.000 | 0.000 | 0.000 |
| word_count | 0.000 | 0.000 | 0.000 |
| filler_count | 0.000 | 0.000 | 0.000 |

Calibration: dynamic

### Agreeableness (A) — Mean Error: 0.1657

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| acknowledgment_count | 0.163 | 0.188 | 0.128 |
| disagreement_count | 0.258 | 0.212 | 0.163 |
| negation_count | 0.906 | 0.947 | 1.244 |
| politeness_count | 0.000 | 0.000 | 0.000 |
| compliment_count | 0.000 | 0.000 | 0.000 |

Calibration: dynamic

### Neuroticism (N) — Mean Error: 0.1697

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| hedge_count | 0.443 | 0.138 | 0.176 |
| self_doubt_count | 0.000 | 0.000 | 0.000 |
| reassurance_seeking_count | 0.000 | 0.000 | 0.000 |
| apology_count | 0.001 | 0.001 | 0.000 |
| emotional_word_count | 0.056 | 0.067 | 0.086 |

Calibration: dynamic


## Engine Advantage Decomposition

| Stage | Drift MAE | Delta from Previous | % of Total Improvement |
|-------|-----------|--------------------|-----------------------|
| Naive (baseline) | 0.1802 | — | — |
| + Multi-candidate pool (naive_informed) | 0.1735 | -0.0067 | 60% |
| + Controller intelligence (engine) | 0.1691 | -0.0044 | 40% |
| **Total improvement** | | **-0.0111** | **100%** |

Interpretation: 60% of the engine's drift advantage comes from having multiple candidates;
40% comes from the controller's scoring intelligence.

## Decision Driver Analysis

### engine_dialogue_only — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 260988 | sycophancy_risk | 260988 |
| TENSION | identity_consistency | 260988 | sycophancy_risk | 260988 |
| NEGOTIATION | identity_consistency | 302880 | sycophancy_risk | 302880 |
| CLOSING | identity_consistency | 161088 | sycophancy_risk | 161088 |

### naive_informed — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 254248 | sycophancy_risk | 254248 |
| TENSION | identity_consistency | 254248 | sycophancy_risk | 254248 |
| NEGOTIATION | identity_consistency | 295100 | sycophancy_risk | 295100 |
| CLOSING | identity_consistency | 156968 | sycophancy_risk | 156968 |


## Per-Archetype Trait Error

| Archetype | n | O | C | E | A | N | MAE | Top Failed Trait |
|-----------|---|---|---|---|---|---|-----|-----------------|
| Academic researcher studying crypto market failures | 6 | 0.270 | 0.224 | 0.045 | 0.101 | 0.183 | 0.165 | O |
| Activision Blizzard game studio creative lead | 6 | 0.337 | 0.110 | 0.096 | 0.015 | 0.199 | 0.151 | O |
| Activision Shareholder | 6 | 0.130 | 0.256 | 0.016 | 0.317 | 0.108 | 0.165 | A |
| Activist investor | 18 | 0.061 | 0.393 | 0.156 | 0.254 | 0.258 | 0.224 | C |
| Ad-Tech Engineer | 18 | 0.137 | 0.215 | 0.121 | 0.181 | 0.054 | 0.141 | C |
| Aerospace insurance underwriter repricing risk for the MAX fleet. | 6 | 0.057 | 0.302 | 0.089 | 0.209 | 0.110 | 0.153 | C |
| Affected mother of three | 6 | 0.153 | 0.034 | 0.201 | 0.314 | 0.101 | 0.161 | A |
| Aging local worker | 6 | 0.247 | 0.073 | 0.203 | 0.010 | 0.102 | 0.127 | O |
| Alameda Research quant who uncovered the balance sheet discrepancy | 6 | 0.387 | 0.276 | 0.250 | 0.042 | 0.097 | 0.210 | O |
| Alameda Research quantitative analyst who discovered balance sheet irregularities | 6 | 0.203 | 0.406 | 0.171 | 0.093 | 0.102 | 0.195 | C |
| Alameda quant analyst | 6 | 0.387 | 0.274 | 0.309 | 0.049 | 0.007 | 0.205 | O |
| All-Hands Moderator | 6 | 0.187 | 0.076 | 0.264 | 0.190 | 0.011 | 0.145 | E |
| Amazon Fitness lead | 6 | 0.237 | 0.276 | 0.086 | 0.088 | 0.203 | 0.178 | C |
| Apple Fitness+ product lead | 12 | 0.233 | 0.291 | 0.058 | 0.106 | 0.252 | 0.188 | C |
| Bahamas Securities Commission supervisor who approved FTX license | 6 | 0.097 | 0.148 | 0.122 | 0.168 | 0.017 | 0.110 | A |
| Bahamas regulatory officer | 6 | 0.280 | 0.136 | 0.176 | 0.188 | 0.093 | 0.175 | O |
| Bahamian financial regulatory officer who approved FTX license | 6 | 0.063 | 0.320 | 0.021 | 0.190 | 0.217 | 0.162 | C |
| Barista-Organizer working two jobs | 6 | 0.337 | 0.080 | 0.211 | 0.011 | 0.093 | 0.146 | O |
| Barista-organizer working two jobs | 6 | 0.320 | 0.043 | 0.142 | 0.015 | 0.190 | 0.142 | O |
| Barista-organizer working two jobs, recently written up for 'tardiness' after union meetings | 6 | 0.270 | 0.079 | 0.155 | 0.038 | 0.088 | 0.126 | O |
| Bootstrapped SaaS Founder | 12 | 0.275 | 0.074 | 0.228 | 0.089 | 0.103 | 0.154 | O |
| Brick-and-mortar bookstore owner (Congestion Zone) | 6 | 0.070 | 0.051 | 0.334 | 0.093 | 0.013 | 0.112 | E |
| CEO of a regional airline with 14 grounded MAX aircraft, facing significant financial losses. | 6 | 0.263 | 0.281 | 0.175 | 0.109 | 0.290 | 0.224 | N |
| CFO | 6 | 0.030 | 0.374 | 0.020 | 0.205 | 0.111 | 0.148 | C |
| CRE Lease Negotiator | 6 | 0.130 | 0.418 | 0.104 | 0.024 | 0.304 | 0.196 | C |
| CRE Lease Strategist | 6 | 0.163 | 0.398 | 0.110 | 0.277 | 0.212 | 0.232 | C |
| Cabin crew safety representative | 6 | 0.137 | 0.184 | 0.025 | 0.285 | 0.111 | 0.148 | A |
| Centrelink call center team lead | 6 | 0.070 | 0.370 | 0.162 | 0.203 | 0.007 | 0.162 | C |
| Centrelink call center worker | 6 | 0.063 | 0.345 | 0.272 | 0.116 | 0.196 | 0.198 | C |
| Centrelink call center worker processing appeals | 6 | 0.063 | 0.205 | 0.106 | 0.107 | 0.020 | 0.100 | C |
| Centrelink middle manager | 6 | 0.030 | 0.369 | 0.032 | 0.209 | 0.207 | 0.169 | C |
| Chair of the pilots' union safety committee, advocating for extensive pilot retraining. | 6 | 0.113 | 0.318 | 0.026 | 0.218 | 0.120 | 0.159 | C |
| City council president | 6 | 0.080 | 0.122 | 0.277 | 0.188 | 0.199 | 0.173 | E |
| City economic development director | 6 | 0.067 | 0.204 | 0.264 | 0.103 | 0.013 | 0.130 | E |
| City official overseeing Prop C implementation | 6 | 0.047 | 0.222 | 0.366 | 0.016 | 0.102 | 0.150 | E |
| City policymaker | 6 | 0.097 | 0.358 | 0.191 | 0.012 | 0.192 | 0.170 | C |
| Clawback-targeted foundation | 6 | 0.187 | 0.057 | 0.082 | 0.426 | 0.227 | 0.196 | A |
| Cloud Infrastructure Architect | 6 | 0.220 | 0.133 | 0.021 | 0.016 | 0.089 | 0.096 | O |
| Cloud Infrastructure Engineer at Microsoft | 12 | 0.115 | 0.338 | 0.069 | 0.169 | 0.298 | 0.198 | C |
| College student (account borrower) | 6 | 0.420 | 0.264 | 0.201 | 0.093 | 0.024 | 0.201 | O |
| Commercial Real Estate Analyst | 6 | 0.120 | 0.345 | 0.070 | 0.211 | 0.033 | 0.156 | C |
| Commercial real estate analyst | 6 | 0.097 | 0.384 | 0.032 | 0.218 | 0.407 | 0.228 | N |
| Committee member who championed $10B investment | 6 | 0.063 | 0.386 | 0.227 | 0.206 | 0.093 | 0.195 | C |
| Community Church Leader organizing relief efforts | 6 | 0.220 | 0.098 | 0.251 | 0.462 | 0.313 | 0.269 | A |
| Community Church Pastor | 6 | 0.103 | 0.055 | 0.297 | 0.397 | 0.112 | 0.193 | A |
| Community Manager (Facing Layoffs) | 6 | 0.170 | 0.061 | 0.201 | 0.359 | 0.080 | 0.174 | A |
| Community church leader | 6 | 0.253 | 0.143 | 0.248 | 0.388 | 0.306 | 0.268 | A |
| Community legal aid lawyer | 6 | 0.253 | 0.320 | 0.084 | 0.395 | 0.104 | 0.231 | A |
| Community organizer | 6 | 0.253 | 0.114 | 0.344 | 0.315 | 0.092 | 0.224 | E |
| Competing streamer's retention strategist | 6 | 0.320 | 0.117 | 0.377 | 0.183 | 0.325 | 0.264 | E |
| Competitor exchange | 6 | 0.070 | 0.365 | 0.290 | 0.299 | 0.193 | 0.243 | C |
| Congestion zone business owner | 6 | 0.063 | 0.295 | 0.058 | 0.142 | 0.011 | 0.114 | C |
| Construction CEO | 6 | 0.030 | 0.138 | 0.309 | 0.298 | 0.007 | 0.156 | E |
| Construction union leader | 18 | 0.091 | 0.216 | 0.268 | 0.187 | 0.167 | 0.186 | E |
| Consumer Privacy Advocate | 6 | 0.420 | 0.094 | 0.176 | 0.323 | 0.296 | 0.262 | O |
| Consumer rights advocate | 6 | 0.170 | 0.051 | 0.020 | 0.304 | 0.177 | 0.144 | A |
| Corporate Communications VP | 6 | 0.047 | 0.178 | 0.304 | 0.015 | 0.181 | 0.145 | E |
| Corporate communications managing public perception | 6 | 0.073 | 0.200 | 0.294 | 0.013 | 0.096 | 0.135 | E |
| Corporate labor relations specialist | 6 | 0.097 | 0.276 | 0.288 | 0.303 | 0.018 | 0.197 | A |
| Corporate real estate director locked into unfavorable lease | 6 | 0.130 | 0.273 | 0.044 | 0.095 | 0.092 | 0.127 | C |
| Creative Director at Activision | 6 | 0.470 | 0.082 | 0.213 | 0.015 | 0.211 | 0.198 | O |
| Creative Director at Activision Blizzard | 6 | 0.320 | 0.121 | 0.016 | 0.217 | 0.193 | 0.173 | O |
| Customer/Disability Advocate | 6 | 0.220 | 0.050 | 0.035 | 0.280 | 0.315 | 0.180 | N |
| DPA Enforcement Officer | 6 | 0.147 | 0.331 | 0.022 | 0.305 | 0.096 | 0.180 | C |
| Data Protection Consultant | 6 | 0.063 | 0.437 | 0.088 | 0.015 | 0.192 | 0.159 | C |
| Data Protection Officer | 12 | 0.097 | 0.331 | 0.051 | 0.114 | 0.283 | 0.175 | C |
| Deaf Software Engineer | 6 | 0.353 | 0.366 | 0.127 | 0.117 | 0.122 | 0.217 | C |
| Deaf software engineer | 6 | 0.353 | 0.355 | 0.149 | 0.095 | 0.104 | 0.211 | C |
| Deaf software engineer at Zoom | 6 | 0.213 | 0.348 | 0.047 | 0.125 | 0.107 | 0.168 | C |
| Debt collection contractor | 6 | 0.147 | 0.053 | 0.188 | 0.286 | 0.093 | 0.153 | A |
| Director of charitable foundation facing FTX donation clawback | 6 | 0.153 | 0.261 | 0.022 | 0.290 | 0.098 | 0.165 | A |
| Disability advocate customer | 6 | 0.270 | 0.032 | 0.056 | 0.403 | 0.282 | 0.208 | A |
| Disability rights advocate | 12 | 0.212 | 0.043 | 0.089 | 0.282 | 0.278 | 0.181 | A |
| Disability rights advocate for mobility-limited gig workers | 6 | 0.137 | 0.052 | 0.083 | 0.278 | 0.020 | 0.114 | A |
| Disabled Transit Riders Alliance Director | 6 | 0.170 | 0.045 | 0.024 | 0.397 | 0.103 | 0.148 | A |
| Disaster Response Vet | 6 | 0.063 | 0.348 | 0.089 | 0.305 | 0.096 | 0.180 | C |
| Disney+ retention strategist | 12 | 0.328 | 0.038 | 0.251 | 0.106 | 0.216 | 0.188 | O |
| EPA regional administrator | 6 | 0.113 | 0.316 | 0.022 | 0.019 | 0.099 | 0.114 | C |
| ER physician | 6 | 0.043 | 0.427 | 0.081 | 0.086 | 0.314 | 0.190 | C |
| ER physician treating 20+ medical emergencies per week from encampments | 6 | 0.077 | 0.487 | 0.076 | 0.104 | 0.277 | 0.204 | C |
| ER physician treating encampment-related emergencies | 6 | 0.050 | 0.338 | 0.073 | 0.062 | 0.290 | 0.162 | C |
| EU Parliament Aide | 6 | 0.113 | 0.251 | 0.106 | 0.193 | 0.189 | 0.170 | C |
| EU Policy Strategist | 6 | 0.237 | 0.400 | 0.032 | 0.028 | 0.097 | 0.159 | C |
| Elderly flat owner | 12 | 0.230 | 0.214 | 0.050 | 0.402 | 0.165 | 0.212 | A |
| Employee Resource Group Lead | 6 | 0.437 | 0.063 | 0.138 | 0.281 | 0.007 | 0.185 | O |
| Employment Lawyer | 6 | 0.130 | 0.386 | 0.097 | 0.011 | 0.204 | 0.165 | C |
| Engineering Director | 6 | 0.073 | 0.209 | 0.268 | 0.098 | 0.188 | 0.167 | E |
| Engineering Manager | 6 | 0.057 | 0.226 | 0.333 | 0.127 | 0.204 | 0.189 | E |
| Enterprise Tenant (Fortune 500 CFO) | 6 | 0.163 | 0.372 | 0.174 | 0.126 | 0.290 | 0.225 | C |
| Enterprise Tenant Representative | 6 | 0.163 | 0.235 | 0.026 | 0.107 | 0.123 | 0.131 | C |
| Environmental Justice Coalition Organizer | 6 | 0.437 | 0.117 | 0.051 | 0.198 | 0.296 | 0.219 | O |
| Esports League Organizer | 12 | 0.038 | 0.338 | 0.310 | 0.187 | 0.100 | 0.195 | C |
| European Union Aviation Safety Agency representative | 6 | 0.187 | 0.317 | 0.108 | 0.100 | 0.196 | 0.182 | C |
| Evacuee | 6 | 0.230 | 0.081 | 0.211 | 0.009 | 0.386 | 0.183 | N |
| Executive facing financial losses from grounded fleet | 6 | 0.197 | 0.274 | 0.208 | 0.122 | 0.004 | 0.161 | C |
| FAA Certification Lead | 6 | 0.097 | 0.331 | 0.041 | 0.177 | 0.005 | 0.130 | C |
| FAA advisory panel member advocating for crash victims | 6 | 0.370 | 0.143 | 0.192 | 0.013 | 0.204 | 0.184 | O |
| FDA Investigator | 6 | 0.113 | 0.364 | 0.012 | 0.195 | 0.282 | 0.193 | C |
| FDIC Field Examiner | 12 | 0.213 | 0.302 | 0.106 | 0.111 | 0.092 | 0.165 | C |
| FDIC Resolution Field Examiner | 6 | 0.163 | 0.369 | 0.118 | 0.270 | 0.013 | 0.187 | C |
| FTC Regulatory Attorney | 6 | 0.050 | 0.427 | 0.090 | 0.189 | 0.208 | 0.193 | C |
| FTC antitrust specialist | 6 | 0.130 | 0.210 | 0.024 | 0.078 | 0.091 | 0.107 | C |
| FTC regulator | 6 | 0.073 | 0.416 | 0.217 | 0.109 | 0.289 | 0.221 | C |
| FTX bankruptcy trustee overseeing asset recovery | 6 | 0.057 | 0.374 | 0.080 | 0.218 | 0.287 | 0.203 | C |
| Facing layoffs after building member relationships | 6 | 0.253 | 0.073 | 0.421 | 0.309 | 0.009 | 0.213 | E |
| Factory foreman | 6 | 0.130 | 0.115 | 0.065 | 0.014 | 0.202 | 0.105 | N |
| Fed Emergency Lending Officer | 6 | 0.147 | 0.295 | 0.096 | 0.192 | 0.192 | 0.185 | C |
| Fertility doctor | 6 | 0.170 | 0.248 | 0.109 | 0.296 | 0.199 | 0.205 | A |
| Fired Organizer (Buffalo original) | 6 | 0.453 | 0.174 | 0.264 | 0.076 | 0.211 | 0.235 | O |
| Fishing Cooperative Leader | 18 | 0.152 | 0.228 | 0.022 | 0.093 | 0.266 | 0.152 | N |
| Former FTX software engineer who built withdrawal systems | 6 | 0.320 | 0.190 | 0.179 | 0.095 | 0.029 | 0.163 | O |
| Former Plant Worker | 6 | 0.047 | 0.144 | 0.192 | 0.023 | 0.218 | 0.125 | N |
| Former executive team member | 6 | 0.153 | 0.178 | 0.405 | 0.018 | 0.185 | 0.188 | E |
| Former sub-postmaster convicted of theft | 6 | 0.130 | 0.290 | 0.083 | 0.216 | 0.397 | 0.223 | N |
| Former sub-postmaster wrongfully convicted | 12 | 0.130 | 0.186 | 0.054 | 0.210 | 0.152 | 0.146 | A |
| Formerly unhoused advocate | 6 | 0.220 | 0.128 | 0.253 | 0.212 | 0.100 | 0.182 | E |
| Formerly unhoused mentor in supportive housing | 6 | 0.080 | 0.052 | 0.179 | 0.320 | 0.115 | 0.149 | A |
| Fujitsu PR director | 6 | 0.030 | 0.097 | 0.290 | 0.199 | 0.194 | 0.162 | E |
| Fujitsu lead developer (2005-2012) | 12 | 0.378 | 0.066 | 0.101 | 0.339 | 0.097 | 0.196 | O |
| Fujitsu lead developer (Horizon team) | 6 | 0.103 | 0.385 | 0.073 | 0.325 | 0.189 | 0.215 | C |
| Game Engine Architect | 6 | 0.437 | 0.127 | 0.117 | 0.204 | 0.192 | 0.215 | O |
| Gaming Journalist | 6 | 0.353 | 0.022 | 0.164 | 0.107 | 0.107 | 0.151 | O |
| Gig platform policy lead | 6 | 0.113 | 0.426 | 0.270 | 0.213 | 0.100 | 0.225 | C |
| Gig worker advocate | 6 | 0.270 | 0.084 | 0.081 | 0.204 | 0.077 | 0.143 | O |
| Government data scientist | 6 | 0.337 | 0.400 | 0.157 | 0.121 | 0.011 | 0.205 | C |
| Government data scientist who flagged algorithm flaws | 6 | 0.337 | 0.334 | 0.018 | 0.195 | 0.089 | 0.195 | O |
| Government engineer overseeing recertification | 6 | 0.097 | 0.400 | 0.017 | 0.116 | 0.196 | 0.165 | C |
| Government labor inspector | 6 | 0.030 | 0.220 | 0.019 | 0.060 | 0.200 | 0.106 | C |
| HDB policymaker | 6 | 0.070 | 0.397 | 0.180 | 0.017 | 0.108 | 0.155 | C |
| HR Diversity Officer | 6 | 0.153 | 0.341 | 0.043 | 0.392 | 0.089 | 0.204 | A |
| Hochul Administration Representative | 6 | 0.247 | 0.042 | 0.400 | 0.016 | 0.197 | 0.180 | E |
| Homeless shelter resident | 6 | 0.063 | 0.063 | 0.070 | 0.195 | 0.086 | 0.095 | A |
| Homeowners association president | 6 | 0.230 | 0.107 | 0.033 | 0.205 | 0.200 | 0.155 | O |
| Hospital EMS coordinator | 6 | 0.063 | 0.306 | 0.098 | 0.192 | 0.098 | 0.152 | C |
| Hospital Procurement Director | 12 | 0.093 | 0.267 | 0.057 | 0.155 | 0.242 | 0.163 | C |
| Hospital procurement director who integrated Theranos devices | 6 | 0.050 | 0.334 | 0.102 | 0.072 | 0.023 | 0.116 | C |
| Immigration rights lawyer | 12 | 0.320 | 0.105 | 0.167 | 0.393 | 0.199 | 0.237 | A |
| Immigration rights lawyer pushing reform | 6 | 0.337 | 0.099 | 0.180 | 0.059 | 0.192 | 0.173 | O |
| In-house counsel managing liability exposure | 6 | 0.247 | 0.386 | 0.160 | 0.123 | 0.193 | 0.222 | C |
| Indie Game Developer | 6 | 0.270 | 0.046 | 0.106 | 0.204 | 0.118 | 0.149 | O |
| Indigenous elder affected by debt notice | 6 | 0.070 | 0.155 | 0.108 | 0.327 | 0.011 | 0.134 | A |
| Institutional investor monitoring Boeing's recovery | 6 | 0.047 | 0.270 | 0.122 | 0.193 | 0.004 | 0.127 | C |
| Insurance Underwriter | 6 | 0.050 | 0.231 | 0.065 | 0.120 | 0.203 | 0.134 | C |
| International Observer | 6 | 0.303 | 0.260 | 0.018 | 0.080 | 0.096 | 0.151 | O |
| Investigative journalist | 6 | 0.437 | 0.030 | 0.159 | 0.106 | 0.097 | 0.166 | O |
| Investigative reporter covering the recertification process | 6 | 0.453 | 0.133 | 0.112 | 0.200 | 0.013 | 0.182 | O |
| Investor who introduced others to FTX yield program | 6 | 0.063 | 0.077 | 0.182 | 0.099 | 0.276 | 0.139 | N |
| Jia Wei's fiancée | 12 | 0.053 | 0.358 | 0.156 | 0.191 | 0.179 | 0.188 | C |
| Journalist covering the FTX collapse for major financial publication | 6 | 0.453 | 0.099 | 0.168 | 0.112 | 0.198 | 0.206 | O |
| Korean Import Regulator | 6 | 0.130 | 0.301 | 0.098 | 0.018 | 0.192 | 0.148 | C |
| Lab technician at Theranos who knows the tests are unreliable | 6 | 0.203 | 0.305 | 0.172 | 0.073 | 0.373 | 0.226 | N |
| Labor advocate for laid-off staff | 6 | 0.370 | 0.045 | 0.353 | 0.203 | 0.107 | 0.216 | O |
| Labor union organizer | 12 | 0.205 | 0.168 | 0.207 | 0.073 | 0.197 | 0.170 | E |
| Labor union organizer advocating for full employment benefits | 6 | 0.303 | 0.395 | 0.184 | 0.043 | 0.323 | 0.250 | C |
| Language school operator | 6 | 0.080 | 0.325 | 0.086 | 0.116 | 0.002 | 0.122 | C |
| Language school operator profiting from training fees | 6 | 0.053 | 0.377 | 0.079 | 0.180 | 0.308 | 0.199 | C |
| Legacy Media CTO | 6 | 0.063 | 0.122 | 0.014 | 0.099 | 0.104 | 0.081 | C |
| Local Journalist Covering Labor | 6 | 0.253 | 0.049 | 0.079 | 0.187 | 0.019 | 0.117 | O |
| Local Mayor | 12 | 0.112 | 0.226 | 0.253 | 0.103 | 0.012 | 0.141 | E |
| Local Municipal Leader | 6 | 0.203 | 0.137 | 0.255 | 0.088 | 0.003 | 0.138 | E |
| Local elected official | 6 | 0.237 | 0.150 | 0.253 | 0.035 | 0.011 | 0.137 | E |
| Local journalist | 12 | 0.445 | 0.123 | 0.167 | 0.144 | 0.159 | 0.208 | O |
| Longtime customer and disability advocate worried about service consistency | 6 | 0.153 | 0.061 | 0.088 | 0.170 | 0.318 | 0.158 | N |
| Lyft driver | 6 | 0.137 | 0.022 | 0.210 | 0.089 | 0.129 | 0.117 | E |
| MP (Select Committee member) | 6 | 0.057 | 0.109 | 0.146 | 0.113 | 0.010 | 0.087 | E |
| MTA Capital Projects Director | 6 | 0.137 | 0.363 | 0.207 | 0.198 | 0.296 | 0.240 | C |
| MTA capital projects manager | 12 | 0.133 | 0.317 | 0.183 | 0.060 | 0.177 | 0.174 | C |
| Media ethics professor | 6 | 0.353 | 0.079 | 0.043 | 0.208 | 0.082 | 0.153 | O |
| Medical Journalist Investigating | 6 | 0.420 | 0.141 | 0.165 | 0.017 | 0.197 | 0.188 | O |
| Medical Researcher | 12 | 0.295 | 0.154 | 0.144 | 0.245 | 0.274 | 0.222 | O |
| Mental health counselor | 6 | 0.170 | 0.220 | 0.013 | 0.380 | 0.211 | 0.199 | A |
| Microsoft Azure gaming infrastructure engineer | 6 | 0.097 | 0.306 | 0.174 | 0.186 | 0.299 | 0.212 | C |
| Microsoft Teams Enterprise Sales Director | 6 | 0.120 | 0.051 | 0.335 | 0.220 | 0.307 | 0.207 | E |
| Microsoft Teams Sales Director | 6 | 0.253 | 0.141 | 0.387 | 0.171 | 0.035 | 0.197 | E |
| Minister for Postal Affairs | 6 | 0.070 | 0.256 | 0.116 | 0.102 | 0.203 | 0.149 | C |
| Ministry of Health official | 6 | 0.063 | 0.243 | 0.023 | 0.106 | 0.105 | 0.108 | C |
| Mt. Sinai ER Transport Coordinator | 6 | 0.030 | 0.293 | 0.156 | 0.202 | 0.103 | 0.157 | C |
| NYPD Traffic Chief | 6 | 0.130 | 0.261 | 0.104 | 0.313 | 0.196 | 0.201 | A |
| Netflix APAC content negotiator | 6 | 0.063 | 0.414 | 0.190 | 0.112 | 0.214 | 0.199 | C |
| Netflix anti-fraud engineer | 12 | 0.103 | 0.322 | 0.076 | 0.018 | 0.239 | 0.152 | C |
| Netflix customer service rep | 6 | 0.130 | 0.222 | 0.096 | 0.395 | 0.018 | 0.172 | A |
| Netflix investor relations | 6 | 0.047 | 0.375 | 0.295 | 0.205 | 0.289 | 0.242 | C |
| Netflix licensing negotiator (APAC) | 6 | 0.137 | 0.373 | 0.206 | 0.107 | 0.204 | 0.205 | C |
| Netflix regional content licensing negotiator | 6 | 0.070 | 0.390 | 0.217 | 0.112 | 0.190 | 0.196 | C |
| Nonprofit director | 6 | 0.420 | 0.262 | 0.289 | 0.299 | 0.292 | 0.313 | O |
| NordVPN product lead | 6 | 0.220 | 0.084 | 0.305 | 0.287 | 0.206 | 0.220 | E |
| NordVPN product manager | 6 | 0.253 | 0.110 | 0.310 | 0.197 | 0.308 | 0.236 | E |
| Nuclear Evacuee | 6 | 0.270 | 0.082 | 0.305 | 0.019 | 0.397 | 0.215 | N |
| Office Experience Lead | 6 | 0.063 | 0.304 | 0.182 | 0.119 | 0.196 | 0.173 | C |
| Outer-borough delivery driver | 12 | 0.130 | 0.187 | 0.031 | 0.094 | 0.089 | 0.106 | C |
| Outer-borough package delivery driver (UPS/FedEx) | 6 | 0.130 | 0.208 | 0.044 | 0.070 | 0.097 | 0.110 | C |
| Password-sharing SaaS founder | 6 | 0.453 | 0.035 | 0.265 | 0.086 | 0.182 | 0.204 | O |
| Patient who received incorrect blood test results | 6 | 0.170 | 0.261 | 0.036 | 0.298 | 0.203 | 0.194 | A |
| Patient with Incorrect Results | 6 | 0.030 | 0.137 | 0.032 | 0.193 | 0.270 | 0.132 | N |
| Patient with Misdiagnosis | 6 | 0.170 | 0.086 | 0.213 | 0.269 | 0.285 | 0.205 | N |
| Payroll Provider Account Manager | 6 | 0.030 | 0.111 | 0.246 | 0.018 | 0.207 | 0.123 | E |
| Pediatrician who identified lead poisoning in children | 6 | 0.353 | 0.339 | 0.126 | 0.199 | 0.199 | 0.243 | O |
| Pediatrician who identified lead poisoning spikes | 6 | 0.337 | 0.376 | 0.063 | 0.166 | 0.203 | 0.229 | C |
| Pediatrician who published research on spiking lead levels in children | 6 | 0.237 | 0.350 | 0.084 | 0.172 | 0.193 | 0.207 | C |
| Peloton CFO | 6 | 0.080 | 0.363 | 0.026 | 0.199 | 0.104 | 0.154 | C |
| Peloton community moderator | 6 | 0.050 | 0.135 | 0.258 | 0.218 | 0.027 | 0.137 | E |
| Peloton fitness instructor | 12 | 0.262 | 0.055 | 0.396 | 0.144 | 0.147 | 0.201 | E |
| Peloton hardware engineer | 6 | 0.270 | 0.233 | 0.093 | 0.017 | 0.096 | 0.142 | O |
| Peloton head instructor | 6 | 0.213 | 0.100 | 0.413 | 0.019 | 0.203 | 0.190 | E |
| Peloton warehouse manager | 6 | 0.047 | 0.147 | 0.026 | 0.020 | 0.208 | 0.090 | N |
| Physician Who Ordered Tests | 6 | 0.057 | 0.202 | 0.084 | 0.291 | 0.101 | 0.147 | A |
| Pilots' Union Safety Chair | 6 | 0.153 | 0.332 | 0.014 | 0.205 | 0.095 | 0.160 | C |
| Player Community Moderator | 6 | 0.270 | 0.109 | 0.270 | 0.391 | 0.292 | 0.266 | A |
| Post Office audit director | 12 | 0.255 | 0.428 | 0.124 | 0.196 | 0.192 | 0.239 | C |
| Post Office internal auditor | 6 | 0.050 | 0.387 | 0.207 | 0.085 | 0.016 | 0.149 | C |
| Post Office prosecuting lawyer | 6 | 0.163 | 0.233 | 0.119 | 0.311 | 0.009 | 0.167 | A |
| Professional gaming league organizer | 6 | 0.063 | 0.367 | 0.176 | 0.151 | 0.109 | 0.173 | C |
| Property agent | 6 | 0.270 | 0.067 | 0.388 | 0.189 | 0.011 | 0.185 | E |
| Property owner facing tenant default | 6 | 0.030 | 0.185 | 0.036 | 0.293 | 0.007 | 0.110 | A |
| Public Health Researcher | 6 | 0.370 | 0.116 | 0.213 | 0.187 | 0.094 | 0.196 | O |
| Regional Airline CEO | 6 | 0.163 | 0.319 | 0.187 | 0.136 | 0.295 | 0.220 | C |
| Regional HR Director | 6 | 0.030 | 0.208 | 0.027 | 0.289 | 0.111 | 0.133 | A |
| Remote Work Advocate | 6 | 0.453 | 0.180 | 0.033 | 0.314 | 0.296 | 0.255 | O |
| Renewables Lobbyist | 6 | 0.220 | 0.061 | 0.353 | 0.162 | 0.299 | 0.219 | E |
| Reporter investigating governance failures | 6 | 0.470 | 0.130 | 0.116 | 0.204 | 0.097 | 0.204 | O |
| Retail crypto trader who lost life savings in FTX yield program | 6 | 0.130 | 0.081 | 0.049 | 0.024 | 0.294 | 0.116 | N |
| Retail crypto trader who lost life savings in FTX's yield program | 6 | 0.253 | 0.224 | 0.128 | 0.098 | 0.287 | 0.198 | N |
| Retail crypto trader with locked savings | 6 | 0.130 | 0.147 | 0.061 | 0.088 | 0.307 | 0.147 | N |
| Risk analyst adjusting premiums for MAX operations | 6 | 0.070 | 0.247 | 0.071 | 0.187 | 0.104 | 0.136 | C |
| Rural council member | 6 | 0.063 | 0.075 | 0.303 | 0.116 | 0.195 | 0.151 | E |
| Rural factory owner | 12 | 0.247 | 0.374 | 0.068 | 0.200 | 0.099 | 0.198 | C |
| Rural factory owner dependent on program labor | 6 | 0.247 | 0.380 | 0.017 | 0.198 | 0.108 | 0.190 | C |
| SFPD liaison | 6 | 0.130 | 0.256 | 0.116 | 0.099 | 0.008 | 0.122 | C |
| SVB Board Member | 6 | 0.137 | 0.209 | 0.311 | 0.294 | 0.010 | 0.192 | E |
| SVB Commercial Banker | 12 | 0.062 | 0.351 | 0.088 | 0.088 | 0.248 | 0.167 | C |
| SVB Senior Commercial Banker | 6 | 0.030 | 0.290 | 0.025 | 0.049 | 0.217 | 0.122 | C |
| SVB Treasury Manager | 6 | 0.030 | 0.209 | 0.166 | 0.014 | 0.097 | 0.103 | C |
| SVB Treasury Risk Officer | 6 | 0.063 | 0.235 | 0.175 | 0.037 | 0.108 | 0.124 | C |
| SaaS Founder (Bootstrapped) | 6 | 0.337 | 0.047 | 0.216 | 0.103 | 0.196 | 0.180 | O |
| Safety advocate pushing for rigorous retraining | 6 | 0.137 | 0.331 | 0.035 | 0.218 | 0.104 | 0.165 | C |
| Seed-stage biotech CEO with 85 employees | 6 | 0.303 | 0.159 | 0.102 | 0.078 | 0.203 | 0.169 | O |
| Senior Centrelink manager overseeing the scheme | 6 | 0.113 | 0.341 | 0.072 | 0.278 | 0.011 | 0.163 | C |
| Senior Lab Technician at Theranos | 6 | 0.337 | 0.367 | 0.199 | 0.198 | 0.097 | 0.240 | C |
| Shift Supervisor (undecided) | 6 | 0.070 | 0.129 | 0.039 | 0.187 | 0.033 | 0.092 | A |
| Shrine Keeper | 6 | 0.230 | 0.354 | 0.197 | 0.401 | 0.108 | 0.258 | A |
| Single parent issued an incorrect $12K debt notice | 6 | 0.130 | 0.038 | 0.055 | 0.111 | 0.207 | 0.108 | N |
| Single parent sharing Netflix account with ex-spouse | 6 | 0.130 | 0.207 | 0.013 | 0.302 | 0.102 | 0.151 | A |
| Single parent sharing Netflix account with ex-spouse for children's access | 6 | 0.130 | 0.193 | 0.024 | 0.295 | 0.115 | 0.151 | A |
| Single parent sharing account with ex-spouse | 6 | 0.130 | 0.157 | 0.026 | 0.304 | 0.092 | 0.142 | A |
| Single parent with $12K incorrect debt notice | 6 | 0.130 | 0.058 | 0.096 | 0.203 | 0.277 | 0.153 | N |
| Single parent wrongly issued $12K debt notice | 6 | 0.130 | 0.203 | 0.100 | 0.115 | 0.287 | 0.167 | N |
| Single-mom DoorDash driver | 12 | 0.100 | 0.129 | 0.020 | 0.158 | 0.178 | 0.117 | N |
| Single-mom DoorDash driver needing schedule flexibility for childcare | 6 | 0.080 | 0.153 | 0.024 | 0.080 | 0.183 | 0.104 | N |
| Small Business Owner Subletter | 6 | 0.287 | 0.066 | 0.165 | 0.017 | 0.038 | 0.115 | O |
| Small business owner (congestion zone) | 6 | 0.073 | 0.238 | 0.284 | 0.161 | 0.360 | 0.223 | N |
| Small business owner (convenience store) facing 60% foot traffic decline | 6 | 0.130 | 0.277 | 0.055 | 0.084 | 0.210 | 0.151 | C |
| Small business owner (retail) | 6 | 0.130 | 0.144 | 0.122 | 0.088 | 0.011 | 0.099 | C |
| Small business owner whose storefront foot traffic dropped 60% due to nearby encampments | 6 | 0.147 | 0.117 | 0.023 | 0.086 | 0.088 | 0.092 | O |
| Small game studio founder | 6 | 0.370 | 0.050 | 0.106 | 0.126 | 0.180 | 0.166 | O |
| Small restaurant owner | 12 | 0.075 | 0.288 | 0.110 | 0.056 | 0.094 | 0.124 | C |
| Social Services Minister | 6 | 0.047 | 0.226 | 0.417 | 0.207 | 0.111 | 0.201 | E |
| Social worker at community legal center | 6 | 0.303 | 0.127 | 0.162 | 0.383 | 0.093 | 0.214 | A |
| Social worker counseling affected clients | 6 | 0.137 | 0.033 | 0.187 | 0.270 | 0.210 | 0.167 | A |
| SoftBank Investment Committee Member | 12 | 0.068 | 0.261 | 0.102 | 0.164 | 0.295 | 0.178 | N |
| South Korean recruiter | 6 | 0.130 | 0.031 | 0.400 | 0.183 | 0.098 | 0.168 | E |
| Startup CEO with frozen payroll | 6 | 0.337 | 0.193 | 0.108 | 0.089 | 0.200 | 0.185 | O |
| Startup CEO with frozen payroll funds | 6 | 0.270 | 0.071 | 0.195 | 0.078 | 0.200 | 0.163 | O |
| Startup CFO | 6 | 0.067 | 0.324 | 0.105 | 0.104 | 0.308 | 0.181 | C |
| State Budget Analyst | 6 | 0.097 | 0.203 | 0.025 | 0.069 | 0.205 | 0.120 | N |
| State Health Department Official | 6 | 0.213 | 0.312 | 0.050 | 0.035 | 0.305 | 0.183 | C |
| State budget analyst | 6 | 0.163 | 0.224 | 0.033 | 0.098 | 0.101 | 0.124 | C |
| State governor | 6 | 0.063 | 0.071 | 0.191 | 0.190 | 0.201 | 0.143 | N |
| State health director | 6 | 0.220 | 0.188 | 0.082 | 0.017 | 0.301 | 0.162 | N |
| State legislator | 6 | 0.057 | 0.309 | 0.188 | 0.013 | 0.177 | 0.149 | C |
| Store Manager (10-year veteran) | 6 | 0.057 | 0.341 | 0.128 | 0.193 | 0.189 | 0.182 | C |
| Store manager torn between corporate and staff | 6 | 0.057 | 0.275 | 0.092 | 0.203 | 0.123 | 0.150 | C |
| Store manager torn between corporate anti-union directives and loyalty to staff | 6 | 0.057 | 0.182 | 0.132 | 0.293 | 0.193 | 0.171 | A |
| Street outreach worker | 6 | 0.353 | 0.030 | 0.191 | 0.417 | 0.196 | 0.238 | A |
| Street outreach worker with deep client trust relationships | 6 | 0.187 | 0.122 | 0.280 | 0.412 | 0.207 | 0.242 | A |
| Street outreach worker with years of trust relationships among unhoused clients | 6 | 0.253 | 0.033 | 0.158 | 0.382 | 0.212 | 0.208 | A |
| Sublessor dependent on WeWork infrastructure | 6 | 0.370 | 0.072 | 0.109 | 0.006 | 0.203 | 0.152 | O |
| TEPCO Safety Engineer | 18 | 0.070 | 0.344 | 0.064 | 0.205 | 0.293 | 0.195 | C |
| Taiwanese factory line supervisor | 18 | 0.136 | 0.205 | 0.066 | 0.088 | 0.071 | 0.113 | C |
| Teams Talent Scout | 6 | 0.237 | 0.116 | 0.411 | 0.223 | 0.305 | 0.258 | E |
| Teamsters Local 814 Secretary-Treasurer | 6 | 0.070 | 0.106 | 0.162 | 0.300 | 0.096 | 0.147 | A |
| Tech Journalist | 6 | 0.403 | 0.059 | 0.172 | 0.282 | 0.027 | 0.189 | O |
| Tech executive | 6 | 0.063 | 0.370 | 0.020 | 0.207 | 0.300 | 0.192 | C |
| Tech industry lobbyist | 6 | 0.030 | 0.200 | 0.288 | 0.202 | 0.300 | 0.204 | N |
| Tech journalist investigating Robodebt | 6 | 0.453 | 0.287 | 0.156 | 0.008 | 0.104 | 0.202 | O |
| Theranos Board Member | 6 | 0.063 | 0.139 | 0.280 | 0.190 | 0.017 | 0.138 | E |
| Theranos Lab Technician | 6 | 0.220 | 0.300 | 0.157 | 0.097 | 0.028 | 0.160 | C |
| Theranos Legal Counsel | 12 | 0.205 | 0.259 | 0.153 | 0.254 | 0.144 | 0.203 | C |
| Theranos Quality Assurance Lead | 6 | 0.320 | 0.412 | 0.024 | 0.100 | 0.204 | 0.212 | C |
| Third-Party Union Buster Consultant | 6 | 0.147 | 0.253 | 0.184 | 0.300 | 0.104 | 0.197 | A |
| Trapped elderly owner | 6 | 0.230 | 0.160 | 0.077 | 0.160 | 0.187 | 0.163 | O |
| URA urban planner | 6 | 0.303 | 0.427 | 0.026 | 0.019 | 0.382 | 0.231 | C |
| US Congressional representative investigating crypto regulation | 6 | 0.170 | 0.053 | 0.264 | 0.095 | 0.198 | 0.156 | E |
| Uber executive | 6 | 0.063 | 0.431 | 0.289 | 0.091 | 0.307 | 0.236 | C |
| Uber/Lyft Driver Association Leader | 6 | 0.253 | 0.160 | 0.290 | 0.022 | 0.196 | 0.184 | E |
| Union rep for postal workers | 6 | 0.147 | 0.130 | 0.379 | 0.009 | 0.303 | 0.193 | E |
| Urban planner | 6 | 0.337 | 0.432 | 0.071 | 0.124 | 0.307 | 0.254 | C |
| VC General Partner | 12 | 0.253 | 0.053 | 0.317 | 0.209 | 0.358 | 0.238 | N |
| VC Investor (Tech Portfolio) | 6 | 0.137 | 0.055 | 0.300 | 0.201 | 0.107 | 0.160 | E |
| Victim Family Representative | 6 | 0.203 | 0.087 | 0.181 | 0.257 | 0.288 | 0.203 | N |
| Victim's daughter | 6 | 0.253 | 0.199 | 0.365 | 0.298 | 0.014 | 0.226 | E |
| Vietnamese Embassy liaison | 6 | 0.170 | 0.268 | 0.063 | 0.198 | 0.298 | 0.199 | N |
| Vietnamese technical intern (former) | 6 | 0.147 | 0.184 | 0.050 | 0.021 | 0.300 | 0.140 | N |
| Vietnamese technical intern with wage theft experience | 6 | 0.130 | 0.142 | 0.050 | 0.024 | 0.108 | 0.091 | C |
| Vietnamese trainee (wage theft victim) | 6 | 0.130 | 0.182 | 0.047 | 0.115 | 0.302 | 0.155 | N |
| Village council chair | 6 | 0.107 | 0.207 | 0.274 | 0.408 | 0.200 | 0.239 | A |
| Walgreens Partnership Manager | 12 | 0.142 | 0.228 | 0.339 | 0.068 | 0.151 | 0.185 | E |
| Warehouse logistics manager | 6 | 0.047 | 0.190 | 0.014 | 0.085 | 0.096 | 0.086 | C |
| Water Treatment Plant Operator | 6 | 0.090 | 0.306 | 0.178 | 0.120 | 0.105 | 0.160 | C |
| Water Treatment Plant Supervisor | 6 | 0.073 | 0.252 | 0.134 | 0.135 | 0.207 | 0.160 | C |
| Water treatment plant supervisor | 6 | 0.043 | 0.231 | 0.075 | 0.091 | 0.001 | 0.088 | C |
| WeWork Community Manager | 6 | 0.187 | 0.051 | 0.377 | 0.295 | 0.110 | 0.204 | E |
| WeWork Interim Legal Counsel | 6 | 0.047 | 0.243 | 0.198 | 0.093 | 0.198 | 0.156 | C |
| Xbox Platform Strategist | 6 | 0.137 | 0.203 | 0.296 | 0.096 | 0.014 | 0.149 | E |
| Young couple awaiting BTO flat | 6 | 0.253 | 0.339 | 0.031 | 0.107 | 0.277 | 0.201 | C |
| Young professional awaiting BTO flat | 6 | 0.203 | 0.256 | 0.035 | 0.128 | 0.090 | 0.142 | C |
| Young professional waiting for BTO | 6 | 0.170 | 0.232 | 0.046 | 0.025 | 0.208 | 0.136 | C |
| Zoom Engineering Manager | 6 | 0.057 | 0.352 | 0.111 | 0.105 | 0.187 | 0.162 | C |

## Phase-Level Behavioral Features (Engine Condition)

| Feature | OPENING | TENSION | NEGOTIATION | CLOSING | Delta (CLOSING - OPENING) |
|---------|------|------|------|------|------|
| acknowledgment_count | 0.053 | 0.028 | 0.088 | 0.148 | +0.094 |
| apology_count | 0.002 | 0.000 | 0.000 | 0.000 | -0.002 |
| disagreement_count | 0.108 | 0.022 | 0.158 | 0.138 | +0.029 |
| emotional_word_count | 0.045 | 0.003 | 0.009 | 0.023 | -0.022 |
| hedge_count | 0.237 | 0.044 | 0.271 | 0.110 | -0.126 |
| idea_count | 0.188 | 0.278 | 0.376 | 0.181 | -0.006 |
| negation_count | 0.267 | 0.542 | 0.262 | 0.277 | +0.010 |
| reassurance_seeking_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| self_doubt_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| unique_word_ratio | 0.860 | 0.826 | 0.837 | 0.839 | -0.021 |

## Scenario Difficulty vs Drift

| Scenario | Difficulty | Engine Drift | Naive Drift | Delta |
|----------|-----------|-------------|-------------|-------|
| 10actor | 0.76 | 0.1809 | 0.1865 | -0.0055 |
| 3actor | 0.76 | 0.1733 | 0.1848 | -0.0115 |
| 5actor | 0.76 | 0.1369 | 0.1515 | -0.0146 |
| 10actor | 0.59 | 0.1591 | 0.1584 | +0.0007 |
| 3actor | 0.59 | 0.1744 | 0.1808 | -0.0063 |
| 5actor | 0.59 | 0.1651 | 0.1714 | -0.0063 |
| 10actor | 0.76 | 0.1550 | 0.1633 | -0.0084 |
| 3actor | 0.76 | 0.1371 | 0.1653 | -0.0283 |
| 5actor | 0.76 | 0.1538 | 0.1622 | -0.0084 |
| 10actor | 0.76 | 0.1613 | 0.1692 | -0.0080 |
| 3actor | 0.76 | 0.1432 | 0.1672 | -0.0240 |
| 5actor | 0.76 | 0.1564 | 0.1708 | -0.0144 |
| 10actor | 1.00 | 0.1704 | 0.1678 | +0.0025 |
| 3actor | 1.00 | 0.1973 | 0.2196 | -0.0223 |
| 5actor | 1.00 | 0.1819 | 0.1744 | +0.0075 |
| 10actor | 1.00 | 0.1620 | 0.1694 | -0.0074 |
| 3actor | 1.00 | 0.1648 | 0.1766 | -0.0117 |
| 5actor | 1.00 | 0.1816 | 0.1989 | -0.0173 |
| 10actor | 0.68 | 0.1688 | 0.1757 | -0.0068 |
| 3actor | 0.68 | 0.1625 | 0.1702 | -0.0077 |
| 5actor | 0.68 | 0.1700 | 0.1855 | -0.0155 |
| 10actor | 0.59 | 0.1558 | 0.1646 | -0.0088 |
| 3actor | 0.59 | 0.1911 | 0.1952 | -0.0041 |
| 5actor | 0.59 | 0.1523 | 0.1517 | +0.0006 |
| 10actor | 0.57 | 0.1913 | 0.1943 | -0.0030 |
| 3actor | 0.57 | 0.1651 | 0.1737 | -0.0086 |
| 5actor | 0.57 | 0.1634 | 0.1612 | +0.0022 |
| 10actor | 0.68 | 0.1748 | 0.1833 | -0.0085 |
| 3actor | 0.68 | 0.2052 | 0.2031 | +0.0022 |
| 5actor | 0.68 | 0.1934 | 0.2034 | -0.0100 |
| 10actor | 0.82 | 0.1625 | 0.1735 | -0.0110 |
| 3actor | 0.82 | 0.1532 | 0.1602 | -0.0070 |
| 5actor | 0.82 | 0.1368 | 0.1456 | -0.0088 |
| 10actor | 0.91 | 0.1643 | 0.1726 | -0.0083 |
| 3actor | 0.91 | 0.1643 | 0.1768 | -0.0125 |
| 5actor | 0.91 | 0.1487 | 0.1573 | -0.0086 |
| 10actor | 0.91 | 0.1717 | 0.1776 | -0.0059 |
| 3actor | 0.91 | 0.1617 | 0.1710 | -0.0093 |
| 5actor | 0.91 | 0.1653 | 0.1737 | -0.0084 |
| 10actor | 0.48 | 0.1890 | 0.1872 | +0.0019 |
| 3actor | 0.48 | 0.1823 | 0.1856 | -0.0033 |
| 5actor | 0.48 | 0.1899 | 0.1982 | -0.0083 |
| 10actor | 0.82 | 0.1543 | 0.1603 | -0.0059 |
| 3actor | 0.82 | 0.1453 | 0.1551 | -0.0098 |
| 5actor | 0.82 | 0.1780 | 0.1884 | -0.0104 |
| 10actor | 0.59 | 0.1603 | 0.1736 | -0.0132 |
| 3actor | 0.59 | 0.1551 | 0.1614 | -0.0063 |
| 5actor | 0.59 | 0.1764 | 0.1797 | -0.0033 |
| 10actor | 1.00 | 0.1680 | 0.1715 | -0.0035 |
| 3actor | 1.00 | 0.1772 | 0.1791 | -0.0019 |
| 5actor | 1.00 | 0.2037 | 0.2023 | +0.0014 |
| 10actor | 0.85 | 0.1846 | 0.1938 | -0.0092 |
| 3actor | 0.85 | 0.1652 | 0.1708 | -0.0057 |
| 5actor | 0.85 | 0.1660 | 0.1801 | -0.0141 |
| 10actor | 1.00 | 0.1713 | 0.1777 | -0.0065 |
| 3actor | 1.00 | 0.1807 | 0.1856 | -0.0049 |
| 5actor | 1.00 | 0.1569 | 0.1642 | -0.0073 |
| 10actor | 0.66 | 0.1844 | 0.1905 | -0.0061 |
| 3actor | 0.66 | 0.1721 | 0.1824 | -0.0103 |
| 5actor | 0.66 | 0.2066 | 0.2147 | -0.0081 |

## Influence Attribution: Who Drove Key Decisions?

### Decision Points Detected: 874 across 120 engine runs (mean 7.28/run)

| Decision Type | Count | Mean Influence Concentration |
|---------------|-------|------------------------------|
| trait_drift_spike | 837 | 0.415 |
| sentiment_flip | 37 | 0.479 |

### Sample Decision Traces

> **actor_1** at turn 11 (TENSION): trait_drift_spike
> actor_1 drift spike -0.179 (→0.203)
> - actor_10: score=0.379 — 
> - actor_9: score=0.300 — 
> actor_1: actor_1 drift spike -0.179 (→0.203). actor_10 (score=0.38, key signal: trait pull) actor_9 (score=0.30, key signal: trait pull)

> **actor_1** at turn 7 (NEGOTIATION): trait_drift_spike
> actor_1 drift spike -0.050 (→0.106)
> - actor_2: score=0.371 — 
> - actor_3: score=0.287 — 
> actor_1: actor_1 drift spike -0.050 (→0.106). actor_2 (score=0.37, key signal: trait pull) actor_3 (score=0.29, key signal: trait pull)

> **actor_1** at turn 7 (): sentiment_flip
> actor_1 sentiment toward actor_3 flipped: positive → challenging
> - actor_2: score=0.359 — 
> - actor_3: score=0.258 — 
> actor_1: actor_1 sentiment toward actor_3 flipped: positive → challenging. actor_2 (score=0.36, key signal: trait pull) actor_3 (score=0.26, key signal: trait pull)


## Statistical Significance: engine_dialogue_only vs naive

| Metric | engine_dialogue_only (n=120) | naive (n=120) | Delta | p-value | Cohen's d | Sig? |
|--------|----|----|----|----|----|----|
| Persona Drift MAE | 0.1691 | 0.1802 | -0.0111 | 0.0000 | -0.658 | Yes |
| Relationship Inconsistency | 0.1124 | 0.1697 | -0.0573 | 0.0442 | -0.260 | Yes |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |
| Envelope Violations | 2.0469 | 2.3353 | -0.2883 | 0.0000 | -0.796 | Yes |
| Action Convergence | 0.7218 | 0.0000 | +0.7218 | 0.0000 | +4.578 | Yes |
| Role Diversity | 0.4999 | 0.0000 | +0.4999 | 0.0000 | +4.205 | Yes |
| Dialogue Coherence | 0.2352 | 0.2029 | +0.0323 | 0.0000 | +1.153 | Yes |
| Repetition Rate | 0.0278 | 0.0139 | +0.0139 | 0.0635 | +0.240 | No |
| Topic Drift Rate | 0.3881 | 0.3321 | +0.0561 | 0.0860 | +0.222 | No |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |

## Per-Trait Error: engine_dialogue_only vs naive

| Trait | Engine | Naive | Delta | p-value | Calibration |
|-------|--------|-------|-------|---------|-------------|
| O | 0.1546 | 0.1838 | -0.0293 | 0.0000 | Static |
| C | 0.2185 | 0.2267 | -0.0082 | 0.1137 | Dynamic |
| E | 0.1385 | 0.1504 | -0.0118 | 0.0155 | Dynamic |
| A | 0.1646 | 0.1692 | -0.0046 | 0.3951 | Dynamic |
| N | 0.1692 | 0.1708 | -0.0016 | 0.7156 | Dynamic |

## Statistical Significance: engine_dialogue_only vs naive_informed

| Metric | engine_dialogue_only (n=120) | naive_informed (n=120) | Delta | p-value | Cohen's d | Sig? |
|--------|----|----|----|----|----|----|
| Persona Drift MAE | 0.1691 | 0.1735 | -0.0044 | 0.0382 | -0.268 | Yes |
| Relationship Inconsistency | 0.1124 | 0.1190 | -0.0066 | 0.8030 | -0.032 | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |
| Envelope Violations | 2.0469 | 2.1575 | -0.1106 | 0.0213 | -0.297 | Yes |
| Action Convergence | 0.7218 | 0.7218 | +0.0000 | 1.0000 | +0.000 | No |
| Role Diversity | 0.4999 | 0.5017 | -0.0018 | 0.9334 | -0.011 | No |
| Dialogue Coherence | 0.2352 | 0.2069 | +0.0283 | 0.0000 | +1.089 | Yes |
| Repetition Rate | 0.0278 | 0.0104 | +0.0174 | 0.0040 | +0.372 | Yes |
| Topic Drift Rate | 0.3881 | 0.3620 | +0.0261 | 0.4275 | +0.102 | No |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |

## Per-Trait Error: engine_dialogue_only vs naive_informed

| Trait | Engine | Naive | Delta | p-value | Calibration |
|-------|--------|-------|-------|---------|-------------|
| O | 0.1546 | 0.1750 | -0.0204 | 0.0001 | Static |
| C | 0.2185 | 0.2213 | -0.0028 | 0.5777 | Dynamic |
| E | 0.1385 | 0.1388 | -0.0003 | 0.9531 | Dynamic |
| A | 0.1646 | 0.1632 | +0.0014 | 0.7904 | Dynamic |
| N | 0.1692 | 0.1692 | -0.0000 | 0.9947 | Dynamic |

## Statistical Significance: naive_informed vs naive

| Metric | naive_informed (n=120) | naive (n=120) | Delta | p-value | Cohen's d | Sig? |
|--------|----|----|----|----|----|----|
| Persona Drift MAE | 0.1735 | 0.1802 | -0.0067 | 0.0016 | -0.408 | Yes |
| Relationship Inconsistency | 0.1190 | 0.1697 | -0.0507 | 0.0815 | -0.225 | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |
| Envelope Violations | 2.1575 | 2.3353 | -0.1778 | 0.0002 | -0.477 | Yes |
| Action Convergence | 0.7218 | 0.0000 | +0.7218 | 0.0000 | +4.578 | Yes |
| Role Diversity | 0.5017 | 0.0000 | +0.5017 | 0.0000 | +4.155 | Yes |
| Dialogue Coherence | 0.2069 | 0.2029 | +0.0040 | 0.1834 | +0.172 | No |
| Repetition Rate | 0.0104 | 0.0139 | -0.0035 | 0.5663 | -0.074 | No |
| Topic Drift Rate | 0.3620 | 0.3321 | +0.0299 | 0.3695 | +0.116 | No |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |

## Per-Trait Error: naive_informed vs naive

| Trait | Engine | Naive | Delta | p-value | Calibration |
|-------|--------|-------|-------|---------|-------------|
| O | 0.1750 | 0.1838 | -0.0089 | 0.0685 | Static |
| C | 0.2213 | 0.2267 | -0.0054 | 0.2846 | Dynamic |
| E | 0.1388 | 0.1504 | -0.0116 | 0.0161 | Dynamic |
| A | 0.1632 | 0.1692 | -0.0060 | 0.2703 | Dynamic |
| N | 0.1692 | 0.1708 | -0.0016 | 0.7247 | Dynamic |

## Actor Count x Condition Scaling

| Actors | Condition | n | Drift | Envelope | Convergence | Diversity | Coherence | Repetition | Topic Drift |
|--------|-----------|---|-------|----------|-------------|-----------|-----------|------------|-------------|
| 3 | engine_dialogue_only | 40 | 0.1686 | 1.9083 | 0.6937 | 0.5906 | 0.2378 | 0.0375 | 0.3568 |
| 3 | naive | 40 | 0.1841 | 2.3583 | 0.0000 | 0.0000 | 0.2046 | 0.0187 | 0.2818 |
| 3 | naive_informed | 40 | 0.1724 | 2.0250 | 0.6937 | 0.6045 | 0.2025 | 0.0125 | 0.3136 |
| 5 | engine_dialogue_only | 40 | 0.1692 | 2.0950 | 0.6542 | 0.5646 | 0.2296 | 0.0250 | 0.3429 |
| 5 | naive | 40 | 0.1789 | 2.3050 | 0.0000 | 0.0000 | 0.2000 | 0.0167 | 0.3179 |
| 5 | naive_informed | 40 | 0.1747 | 2.1600 | 0.6542 | 0.5573 | 0.2052 | 0.0083 | 0.3304 |
| 10 | engine_dialogue_only | 40 | 0.1695 | 2.1375 | 0.8175 | 0.3444 | 0.2382 | 0.0208 | 0.4648 |
| 10 | naive | 40 | 0.1776 | 2.3425 | 0.0000 | 0.0000 | 0.2042 | 0.0062 | 0.3966 |
| 10 | naive_informed | 40 | 0.1735 | 2.2875 | 0.8175 | 0.3433 | 0.2130 | 0.0104 | 0.4420 |

### Drift Slope (10-actor minus 3-actor):

- engine_dialogue_only: +0.0009
- naive: -0.0065
- naive_informed: +0.0011
