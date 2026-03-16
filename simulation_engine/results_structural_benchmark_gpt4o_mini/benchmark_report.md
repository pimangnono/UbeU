# Simulation Benchmark Report

## Suite Config
- Total runs: 120
- Conditions: engine_structural
- Script ids: australia_robodebt_10actor, australia_robodebt_3actor, australia_robodebt_5actor, boeing_737max_return_10actor, boeing_737max_return_3actor, boeing_737max_return_5actor, california_ab5_gig_classification_10actor, california_ab5_gig_classification_3actor, california_ab5_gig_classification_5actor, eu_gdpr_implementation_10actor, eu_gdpr_implementation_3actor, eu_gdpr_implementation_5actor, flint_water_crisis_10actor, flint_water_crisis_3actor, flint_water_crisis_5actor, ftx_collapse_10actor, ftx_collapse_3actor, ftx_collapse_5actor, fukushima_nuclear_restart_10actor, fukushima_nuclear_restart_3actor, fukushima_nuclear_restart_5actor, japan_intern_training_reform_10actor, japan_intern_training_reform_3actor, japan_intern_training_reform_5actor, microsoft_activision_merger_10actor, microsoft_activision_merger_3actor, microsoft_activision_merger_5actor, netflix_password_crackdown_10actor, netflix_password_crackdown_3actor, netflix_password_crackdown_5actor, nyc_congestion_pricing_10actor, nyc_congestion_pricing_3actor, nyc_congestion_pricing_5actor, peloton_demand_cliff_10actor, peloton_demand_cliff_3actor, peloton_demand_cliff_5actor, sf_homelessness_policy_10actor, sf_homelessness_policy_3actor, sf_homelessness_policy_5actor, singapore_hdb_waittime_crisis_10actor, singapore_hdb_waittime_crisis_3actor, singapore_hdb_waittime_crisis_5actor, starbucks_unionization_10actor, starbucks_unionization_3actor, starbucks_unionization_5actor, svb_bank_run_10actor, svb_bank_run_3actor, svb_bank_run_5actor, theranos_whistleblower_10actor, theranos_whistleblower_3actor, theranos_whistleblower_5actor, uk_post_office_horizon_10actor, uk_post_office_horizon_3actor, uk_post_office_horizon_5actor, wework_ipo_collapse_10actor, wework_ipo_collapse_3actor, wework_ipo_collapse_5actor, zoom_return_to_office_10actor, zoom_return_to_office_3actor, zoom_return_to_office_5actor
- Repetitions per condition: 2

## Condition Summary
### engine_structural
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0171)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1622, C 0.2230, E 0.1299, A 0.1645, N 0.1701
- Relationship inconsistency: 0.0891
- Relationship shift rate: 0.2864
- Relationship overshoot rate: 0.1837
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0867
- Clean envelope violations: 2.0867
- Structured action validity: 0.6193
- Owner resolution rate: 0.9167
- Executed action contradiction: 0.0000
- State transition coherence: 0.9167
- Action feedback utilization: 0.2750
- Action-plan alignment: 0.9667
- Planned action coverage: 0.9219
- Action family convergence: 0.7304
- Role action diversity: 0.4971
- Negotiation uniqueness: 0.2875
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1060
- Repetition rate: 0.0000
- Topic drift rate: 0.5203
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1669, 0.173]

- Phase-level quality:
  - OPENING: drift=0.1749, convergence=0.7795, diversity=0.3680
  - TENSION: drift=0.1745, convergence=0.7128, diversity=0.4597
  - NEGOTIATION: drift=0.1734, convergence=0.6794, diversity=0.4804
  - CLOSING: drift=0.1823, convergence=0.6167, diversity=0.5611

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate


## Script-Level Summary
### australia_robodebt_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1813 (+/- 0.0037)
- Clean persona drift MAE: 0.1813
- Per-trait absolute error: O 0.1690, C 0.2462, E 0.1436, A 0.2145, N 0.1331
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.2915
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1016
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1762, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1866, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1784, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1965, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1670, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1802 (+/- 0.0060)
- Clean persona drift MAE: 0.1802
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1140, A 0.2333, N 0.1300
- Relationship inconsistency: 0.2753
- Relationship shift rate: 0.3256
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5834
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.5000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1147
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0002
- Mean turns: 11.00
- Persona drift 95% CI: [0.1718, 0.1885]

- Phase-level quality:
  - OPENING: drift=0.1756, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1747, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1941, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1541 (+/- 0.0055)
- Clean persona drift MAE: 0.1541
- Per-trait absolute error: O 0.1440, C 0.2108, E 0.1063, A 0.2095, N 0.1000
- Relationship inconsistency: 0.1588
- Relationship shift rate: 0.3650
- Relationship overshoot rate: 0.4500
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
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1046
- Repetition rate: 0.0000
- Topic drift rate: 0.1071
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1465, 0.1617]

- Phase-level quality:
  - OPENING: drift=0.1552, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1492, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1285, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1900, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1585 (+/- 0.0011)
- Clean persona drift MAE: 0.1585
- Per-trait absolute error: O 0.1730, C 0.2500, E 0.1154, A 0.1538, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7417
- Role action diversity: 0.3959
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1230
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0001
- Mean turns: 22.00
- Persona drift 95% CI: [0.157, 0.16]

- Phase-level quality:
  - OPENING: drift=0.1525, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1675, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1561, convergence=0.7000, diversity=0.4166
  - CLOSING: drift=0.1605, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1626 (+/- 0.0086)
- Clean persona drift MAE: 0.1626
- Per-trait absolute error: O 0.1066, C 0.3000, E 0.0898, A 0.1633, N 0.1533
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
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
- Dialogue coherence: 0.1358
- Repetition rate: 0.0000
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1508, 0.1745]

- Phase-level quality:
  - OPENING: drift=0.1676, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1690, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1699, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1871, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### boeing_737max_return_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1677 (+/- 0.0008)
- Clean persona drift MAE: 0.1677
- Per-trait absolute error: O 0.1500, C 0.2600, E 0.0861, A 0.1605, N 0.1820
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2228
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.7084
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3214
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0909
- Repetition rate: 0.0000
- Topic drift rate: 0.2143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0004
- Mean turns: 14.00
- Persona drift 95% CI: [0.1666, 0.1688]

- Phase-level quality:
  - OPENING: drift=0.1857, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1513, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1811, convergence=0.5000, diversity=0.6250
  - CLOSING: drift=0.1800, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1593 (+/- 0.0013)
- Clean persona drift MAE: 0.1593
- Per-trait absolute error: O 0.1140, C 0.1717, E 0.1603, A 0.1502, N 0.2000
- Relationship inconsistency: 0.1893
- Relationship shift rate: 0.4232
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
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
- Dialogue coherence: 0.1176
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1574, 0.1611]

- Phase-level quality:
  - OPENING: drift=0.1558, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1703, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1604, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1542, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1434 (+/- 0.0030)
- Clean persona drift MAE: 0.1434
- Per-trait absolute error: O 0.1233, C 0.2000, E 0.0856, A 0.1350, N 0.1734
- Relationship inconsistency: 0.4745
- Relationship shift rate: 0.4184
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
- Action-plan alignment: 0.9613
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.5000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1257
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0010
- Mean turns: 11.00
- Persona drift 95% CI: [0.1392, 0.1477]

- Phase-level quality:
  - OPENING: drift=0.1540, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1530, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1551, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1832, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1493 (+/- 0.0064)
- Clean persona drift MAE: 0.1493
- Per-trait absolute error: O 0.1240, C 0.2022, E 0.1313, A 0.1470, N 0.1420
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.2385
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.4000
- Clean envelope violations: 1.4000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.4584
- Role action diversity: 0.6562
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1181
- Repetition rate: 0.0000
- Topic drift rate: 1.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0003
- Mean turns: 14.00
- Persona drift 95% CI: [0.1404, 0.1582]

- Phase-level quality:
  - OPENING: drift=0.1447, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1550, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1580, convergence=0.5000, diversity=0.6250
  - CLOSING: drift=0.1582, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### eu_gdpr_implementation_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1534 (+/- 0.0057)
- Clean persona drift MAE: 0.1534
- Per-trait absolute error: O 0.1490, C 0.2024, E 0.1003, A 0.1542, N 0.1613
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3250
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
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
- Dialogue coherence: 0.1010
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1456, 0.1613]

- Phase-level quality:
  - OPENING: drift=0.1726, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1659, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1528, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1612, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1695 (+/- 0.0089)
- Clean persona drift MAE: 0.1695
- Per-trait absolute error: O 0.2067, C 0.2334, E 0.1026, A 0.1250, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1921
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6666
- Clean envelope violations: 1.6666
- Structured action validity: 0.8750
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.5000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0011
- Mean turns: 11.00
- Persona drift 95% CI: [0.1572, 0.1818]

- Phase-level quality:
  - OPENING: drift=0.1815, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1639, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1697, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1779, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1532 (+/- 0.0008)
- Clean persona drift MAE: 0.1532
- Per-trait absolute error: O 0.2080, C 0.2000, E 0.0706, A 0.1375, N 0.1500
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2514
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7188
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0003
- Mean turns: 14.00
- Persona drift 95% CI: [0.1521, 0.1543]

- Phase-level quality:
  - OPENING: drift=0.1741, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1631, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1587, convergence=0.5000, diversity=0.6250
  - CLOSING: drift=0.1705, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1638 (+/- 0.0000)
- Clean persona drift MAE: 0.1638
- Per-trait absolute error: O 0.1900, C 0.1800, E 0.1205, A 0.1728, N 0.1556
- Relationship inconsistency: 0.0013
- Relationship shift rate: 0.2484
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9716
- Planned action coverage: 1.0000
- Action family convergence: 0.6917
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1144
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 22.00
- Persona drift 95% CI: [0.1637, 0.1638]

- Phase-level quality:
  - OPENING: drift=0.1623, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1739, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1584, convergence=0.7000, diversity=0.4166
  - CLOSING: drift=0.1797, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2125 (+/- 0.0013)
- Clean persona drift MAE: 0.2125
- Per-trait absolute error: O 0.2300, C 0.2333, E 0.1162, A 0.2434, N 0.2400
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.3018
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
- Action-plan alignment: 0.9819
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1245
- Repetition rate: 0.0000
- Topic drift rate: 0.8637
- Fallback taxonomy: n/a
- State trajectory variance: 0.0004
- Mean turns: 11.00
- Persona drift 95% CI: [0.2108, 0.2143]

- Phase-level quality:
  - OPENING: drift=0.2109, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2171, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2143, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1996, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0040)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1540, C 0.2422, E 0.1147, A 0.1630, N 0.1780
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2477
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.1483
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.2857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1649, 0.1759]

- Phase-level quality:
  - OPENING: drift=0.1784, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1718, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1855, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1510, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### ftx_collapse_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1663 (+/- 0.0050)
- Clean persona drift MAE: 0.1663
- Per-trait absolute error: O 0.2180, C 0.1981, E 0.1019, A 0.1295, N 0.1845
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3050
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1595, 0.1732]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1726, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1731, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1548, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1577 (+/- 0.0080)
- Clean persona drift MAE: 0.1577
- Per-trait absolute error: O 0.2067, C 0.1905, E 0.1580, A 0.1000, N 0.1333
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.7222
- Negotiation uniqueness: 0.1667
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1466, 0.1688]

- Phase-level quality:
  - OPENING: drift=0.1612, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1638, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1588, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1984, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2012 (+/- 0.0023)
- Clean persona drift MAE: 0.2012
- Per-trait absolute error: O 0.2240, C 0.2195, E 0.1820, A 0.2165, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2579
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8000
- Clean envelope violations: 2.8000
- Structured action validity: 0.6667
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
- Dialogue coherence: 0.0978
- Repetition rate: 0.0000
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.198, 0.2044]

- Phase-level quality:
  - OPENING: drift=0.1846, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2128, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.2028, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1888, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1712 (+/- 0.0015)
- Clean persona drift MAE: 0.1712
- Per-trait absolute error: O 0.1600, C 0.2202, E 0.1431, A 0.1402, N 0.1922
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5850
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.6250
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
- Dialogue coherence: 0.0856
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0001
- Mean turns: 22.00
- Persona drift 95% CI: [0.1691, 0.1733]

- Phase-level quality:
  - OPENING: drift=0.1567, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1932, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1697, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1946, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1620 (+/- 0.0027)
- Clean persona drift MAE: 0.1620
- Per-trait absolute error: O 0.1066, C 0.2550, E 0.0867, A 0.1416, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1400
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Dialogue coherence: 0.1099
- Repetition rate: 0.0000
- Topic drift rate: 0.0909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1583, 0.1657]

- Phase-level quality:
  - OPENING: drift=0.1603, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1657, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1748, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1800, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1634 (+/- 0.0024)
- Clean persona drift MAE: 0.1634
- Per-trait absolute error: O 0.1140, C 0.2172, E 0.1358, A 0.1180, N 0.2320
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2875
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.0741
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0886
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1601, 0.1667]

- Phase-level quality:
  - OPENING: drift=0.1734, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1850, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1621, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1680, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1603 (+/- 0.0011)
- Clean persona drift MAE: 0.1603
- Per-trait absolute error: O 0.1960, C 0.1741, E 0.1371, A 0.1431, N 0.1511
- Relationship inconsistency: 0.4190
- Relationship shift rate: 0.3655
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
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
- Dialogue coherence: 0.1023
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1587, 0.1618]

- Phase-level quality:
  - OPENING: drift=0.1446, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1870, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1578, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1646, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1928 (+/- 0.0003)
- Clean persona drift MAE: 0.1928
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.1089, A 0.1850, N 0.1934
- Relationship inconsistency: 0.3630
- Relationship shift rate: 0.6060
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1340
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0931
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1924, 0.1932]

- Phase-level quality:
  - OPENING: drift=0.1894, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.2027, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.2014, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1735, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1523 (+/- 0.0037)
- Clean persona drift MAE: 0.1523
- Per-trait absolute error: O 0.1620, C 0.2400, E 0.0814, A 0.1145, N 0.1640
- Relationship inconsistency: 0.2502
- Relationship shift rate: 0.6203
- Relationship overshoot rate: 0.4500
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
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0981
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1472, 0.1575]

- Phase-level quality:
  - OPENING: drift=0.1554, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1498, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1507, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2041, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1840 (+/- 0.0005)
- Clean persona drift MAE: 0.1840
- Per-trait absolute error: O 0.2070, C 0.1900, E 0.1590, A 0.2007, N 0.1636
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2611
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
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
- Dialogue coherence: 0.1084
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1833, 0.1848]

- Phase-level quality:
  - OPENING: drift=0.1907, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.2009, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1818, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1986, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1681 (+/- 0.0003)
- Clean persona drift MAE: 0.1681
- Per-trait absolute error: O 0.1000, C 0.2667, E 0.1170, A 0.1433, N 0.2133
- Relationship inconsistency: 0.0034
- Relationship shift rate: 0.2200
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
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1244
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1677, 0.1684]

- Phase-level quality:
  - OPENING: drift=0.1713, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1679, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1709, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1984, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1610 (+/- 0.0057)
- Clean persona drift MAE: 0.1610
- Per-trait absolute error: O 0.1740, C 0.2088, E 0.1206, A 0.1215, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2338
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0904
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1531, 0.1689]

- Phase-level quality:
  - OPENING: drift=0.1718, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1709, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1547, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2039, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1813 (+/- 0.0016)
- Clean persona drift MAE: 0.1813
- Per-trait absolute error: O 0.2530, C 0.2020, E 0.1455, A 0.1600, N 0.1458
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.3490
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.6250
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
- Dialogue coherence: 0.0919
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.179, 0.1835]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1942, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1814, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1821, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2035 (+/- 0.0074)
- Clean persona drift MAE: 0.2035
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.2155, A 0.1784, N 0.2000
- Relationship inconsistency: 0.3500
- Relationship shift rate: 0.4137
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6667
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1031
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1931, 0.2138]

- Phase-level quality:
  - OPENING: drift=0.2062, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2068, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2014, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1832, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1928 (+/- 0.0020)
- Clean persona drift MAE: 0.1928
- Per-trait absolute error: O 0.1680, C 0.2090, E 0.1795, A 0.1875, N 0.2200
- Relationship inconsistency: 0.0959
- Relationship shift rate: 0.2749
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
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1061
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.19, 0.1955]

- Phase-level quality:
  - OPENING: drift=0.2089, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1932, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1754, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1567 (+/- 0.0009)
- Clean persona drift MAE: 0.1567
- Per-trait absolute error: O 0.1500, C 0.1612, E 0.1387, A 0.1734, N 0.1600
- Relationship inconsistency: 0.0688
- Relationship shift rate: 0.3330
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9647
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0849
- Repetition rate: 0.0000
- Topic drift rate: 0.3409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 22.00
- Persona drift 95% CI: [0.1555, 0.1578]

- Phase-level quality:
  - OPENING: drift=0.1575, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1779, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1541, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1764, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1610 (+/- 0.0070)
- Clean persona drift MAE: 0.1610
- Per-trait absolute error: O 0.1100, C 0.2000, E 0.1667, A 0.1284, N 0.2000
- Relationship inconsistency: 0.2110
- Relationship shift rate: 0.3092
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
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
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1513, 0.1707]

- Phase-level quality:
  - OPENING: drift=0.1638, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1629, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1587, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1530, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### nyc_congestion_pricing_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1316 (+/- 0.0003)
- Clean persona drift MAE: 0.1316
- Per-trait absolute error: O 0.1100, C 0.2800, E 0.1133, A 0.0725, N 0.0820
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.2976
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7188
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0982
- Repetition rate: 0.0000
- Topic drift rate: 0.6428
- Fallback taxonomy: n/a
- State trajectory variance: 0.0003
- Mean turns: 14.00
- Persona drift 95% CI: [0.1312, 0.1319]

- Phase-level quality:
  - OPENING: drift=0.1440, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1316, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1512, convergence=0.5000, diversity=0.6250
  - CLOSING: drift=0.1326, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1679 (+/- 0.0016)
- Clean persona drift MAE: 0.1679
- Per-trait absolute error: O 0.1700, C 0.2600, E 0.1172, A 0.1213, N 0.1709
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2712
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9761
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1020
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0003
- Mean turns: 22.00
- Persona drift 95% CI: [0.1657, 0.1701]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1564, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1807, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1545, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### peloton_demand_cliff_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1610 (+/- 0.0137)
- Clean persona drift MAE: 0.1610
- Per-trait absolute error: O 0.1400, C 0.2333, E 0.1364, A 0.1550, N 0.1400
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2222
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
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1116
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.142, 0.18]

- Phase-level quality:
  - OPENING: drift=0.1731, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1684, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1689, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1583, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1505 (+/- 0.0098)
- Clean persona drift MAE: 0.1505
- Per-trait absolute error: O 0.1240, C 0.2082, E 0.1375, A 0.1145, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2601
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.1332
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1368, 0.1641]

- Phase-level quality:
  - OPENING: drift=0.1663, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1364, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1570, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1977, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1703 (+/- 0.0024)
- Clean persona drift MAE: 0.1703
- Per-trait absolute error: O 0.1570, C 0.2232, E 0.1241, A 0.1728, N 0.1744
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2862
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
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1043
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.167, 0.1736]

- Phase-level quality:
  - OPENING: drift=0.1750, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1724, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1883, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1557, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1440 (+/- 0.0100)
- Clean persona drift MAE: 0.1440
- Per-trait absolute error: O 0.1066, C 0.2000, E 0.0498, A 0.1567, N 0.2067
- Relationship inconsistency: 0.0075
- Relationship shift rate: 0.2141
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.1096
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1302, 0.1577]

- Phase-level quality:
  - OPENING: drift=0.1613, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1683, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1641, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1724, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1638 (+/- 0.0018)
- Clean persona drift MAE: 0.1638
- Per-trait absolute error: O 0.0840, C 0.2000, E 0.1671, A 0.1750, N 0.1930
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.2253
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
- Action-plan alignment: 0.9661
- Planned action coverage: 1.0000
- Action family convergence: 0.7084
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3928
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1084
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1613, 0.1663]

- Phase-level quality:
  - OPENING: drift=0.1721, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1800, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1732, convergence=0.5000, diversity=0.6250
  - CLOSING: drift=0.1604, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1791 (+/- 0.0028)
- Clean persona drift MAE: 0.1791
- Per-trait absolute error: O 0.1100, C 0.2400, E 0.2041, A 0.1875, N 0.1540
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3343
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.2333
- Negotiation uniqueness: 0.0513
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0932
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1752, 0.183]

- Phase-level quality:
  - OPENING: drift=0.1847, convergence=1.0000, diversity=0.2083
  - TENSION: drift=0.1849, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1769, convergence=1.0000, diversity=0.1834
  - CLOSING: drift=0.1976, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1903 (+/- 0.0110)
- Clean persona drift MAE: 0.1903
- Per-trait absolute error: O 0.1600, C 0.2667, E 0.1000, A 0.2117, N 0.2133
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1100
- Relationship overshoot rate: 0.0000
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
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0954
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1751, 0.2055]

- Phase-level quality:
  - OPENING: drift=0.1902, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1910, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1863, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0074)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1800, C 0.2800, E 0.1328, A 0.1565, N 0.1960
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.4155
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.9000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.5938
- Negotiation uniqueness: 0.3928
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0885
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0007
- Mean turns: 14.00
- Persona drift 95% CI: [0.1787, 0.1994]

- Phase-level quality:
  - OPENING: drift=0.1852, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2007, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1963, convergence=0.5000, diversity=0.6250
  - CLOSING: drift=0.2148, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1624 (+/- 0.0032)
- Clean persona drift MAE: 0.1624
- Per-trait absolute error: O 0.1740, C 0.1976, E 0.1296, A 0.1731, N 0.1378
- Relationship inconsistency: 0.1064
- Relationship shift rate: 0.3320
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5982
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9670
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1002
- Repetition rate: 0.0000
- Topic drift rate: 0.8636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0004
- Mean turns: 22.00
- Persona drift 95% CI: [0.1581, 0.1668]

- Phase-level quality:
  - OPENING: drift=0.1777, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1477, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1753, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1513, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1480 (+/- 0.0100)
- Clean persona drift MAE: 0.1480
- Per-trait absolute error: O 0.1900, C 0.1000, E 0.0832, A 0.1667, N 0.2000
- Relationship inconsistency: 0.1215
- Relationship shift rate: 0.4027
- Relationship overshoot rate: 0.4500
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
- Role action diversity: 0.3959
- Negotiation uniqueness: 0.0955
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1271
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1342, 0.1617]

- Phase-level quality:
  - OPENING: drift=0.1550, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1496, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1409, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1640, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1769 (+/- 0.0048)
- Clean persona drift MAE: 0.1769
- Per-trait absolute error: O 0.1140, C 0.2000, E 0.1328, A 0.2230, N 0.2150
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2775
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.4479
- Negotiation uniqueness: 0.0801
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1021
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1702, 0.1837]

- Phase-level quality:
  - OPENING: drift=0.1823, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1816, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1787, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.2189, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### svb_bank_run_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1547 (+/- 0.0013)
- Clean persona drift MAE: 0.1547
- Per-trait absolute error: O 0.1770, C 0.1988, E 0.1120, A 0.1267, N 0.1589
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2540
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8000
- Role action diversity: 0.3542
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0912
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1529, 0.1564]

- Phase-level quality:
  - OPENING: drift=0.1568, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1679, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1655, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1570, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1615 (+/- 0.0081)
- Clean persona drift MAE: 0.1615
- Per-trait absolute error: O 0.1767, C 0.2872, E 0.0549, A 0.1550, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1892
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
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
- Dialogue coherence: 0.1384
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1503, 0.1726]

- Phase-level quality:
  - OPENING: drift=0.1646, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1580, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1713, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### svb_bank_run_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1651 (+/- 0.0028)
- Clean persona drift MAE: 0.1651
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1127, A 0.1185, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3449
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1288
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1611, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1900, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1545, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1713, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2022, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1727 (+/- 0.0030)
- Clean persona drift MAE: 0.1727
- Per-trait absolute error: O 0.1530, C 0.2600, E 0.1409, A 0.1351, N 0.1744
- Relationship inconsistency: 0.4250
- Relationship shift rate: 0.2762
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5000
- Action family convergence: 1.0000
- Role action diversity: 0.2646
- Negotiation uniqueness: 0.0611
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1203
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1685, 0.1769]

- Phase-level quality:
  - OPENING: drift=0.1768, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1779, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1727, convergence=1.0000, diversity=0.2666
  - CLOSING: drift=0.1805, convergence=1.0000, diversity=0.2916

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1738 (+/- 0.0090)
- Clean persona drift MAE: 0.1738
- Per-trait absolute error: O 0.0867, C 0.3000, E 0.1273, A 0.1550, N 0.2000
- Relationship inconsistency: 0.0282
- Relationship shift rate: 0.2445
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
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
- Dialogue coherence: 0.1174
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1613, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1835, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1829, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1913, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1951, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1885 (+/- 0.0051)
- Clean persona drift MAE: 0.1885
- Per-trait absolute error: O 0.1660, C 0.2000, E 0.1576, A 0.2410, N 0.1780
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.3092
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8333
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0914
- Repetition rate: 0.0000
- Topic drift rate: 0.4285
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1814, 0.1956]

- Phase-level quality:
  - OPENING: drift=0.1962, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1810, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1976, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2100, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1888 (+/- 0.0018)
- Clean persona drift MAE: 0.1888
- Per-trait absolute error: O 0.1870, C 0.1800, E 0.2076, A 0.1881, N 0.1811
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3035
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0976
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1862, 0.1913]

- Phase-level quality:
  - OPENING: drift=0.1972, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1930, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1918, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1876, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### uk_post_office_horizon_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0007)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.1433, C 0.3000, E 0.1000, A 0.2567, N 0.1000
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.1621
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
- Role action diversity: 0.6111
- Negotiation uniqueness: 0.1714
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.179, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1736, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1749, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1716, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1960, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### uk_post_office_horizon_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1785 (+/- 0.0007)
- Clean persona drift MAE: 0.1785
- Per-trait absolute error: O 0.2100, C 0.2093, E 0.1276, A 0.2195, N 0.1260
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3420
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1091
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1775, 0.1795]

- Phase-level quality:
  - OPENING: drift=0.1988, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1633, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1785, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2206, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1743 (+/- 0.0054)
- Clean persona drift MAE: 0.1743
- Per-trait absolute error: O 0.2110, C 0.2102, E 0.1968, A 0.1507, N 0.1027
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1150
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.4583
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0947
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1668, 0.1817]

- Phase-level quality:
  - OPENING: drift=0.1688, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1802, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1681, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1886, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1875 (+/- 0.0152)
- Clean persona drift MAE: 0.1875
- Per-trait absolute error: O 0.1234, C 0.2000, E 0.1575, A 0.2400, N 0.2167
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2036
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1667
- Clean envelope violations: 2.1667
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1330
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1664, 0.2087]

- Phase-level quality:
  - OPENING: drift=0.1886, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1925, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1964, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2080, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1598 (+/- 0.0034)
- Clean persona drift MAE: 0.1598
- Per-trait absolute error: O 0.1240, C 0.2286, E 0.1549, A 0.1415, N 0.1500
- Relationship inconsistency: 0.2600
- Relationship shift rate: 0.3806
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1003
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1551, 0.1645]

- Phase-level quality:
  - OPENING: drift=0.1686, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1726, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1363, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1784, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1855 (+/- 0.0018)
- Clean persona drift MAE: 0.1855
- Per-trait absolute error: O 0.1930, C 0.2800, E 0.1436, A 0.1589, N 0.1518
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2616
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5714
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
- Dialogue coherence: 0.1029
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.183, 0.188]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1891, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1963, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1804, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1774 (+/- 0.0028)
- Clean persona drift MAE: 0.1774
- Per-trait absolute error: O 0.1366, C 0.2333, E 0.1605, A 0.1567, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1200
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
- Dialogue coherence: 0.1166
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1736, 0.1813]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1804, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1901, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1733, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### zoom_return_to_office_5actor:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1997 (+/- 0.0026)
- Clean persona drift MAE: 0.1997
- Per-trait absolute error: O 0.2380, C 0.2200, E 0.1792, A 0.1975, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3759
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
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1017
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1962, 0.2033]

- Phase-level quality:
  - OPENING: drift=0.2155, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1986, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2003, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Mode Summary
### exploratory:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1709 (+/- 0.0158)
- Clean persona drift MAE: 0.1709
- Per-trait absolute error: O 0.1607, C 0.2248, E 0.1302, A 0.1702, N 0.1686
- Relationship inconsistency: 0.0619
- Relationship shift rate: 0.2653
- Relationship overshoot rate: 0.1275
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1361
- Clean envelope violations: 2.1361
- Structured action validity: 0.4553
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.3500
- Action-plan alignment: 0.9689
- Planned action coverage: 0.9087
- Action family convergence: 0.7642
- Role action diversity: 0.4873
- Negotiation uniqueness: 0.2730
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1061
- Repetition rate: 0.0000
- Topic drift rate: 0.4785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1669, 0.1749]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.7478, diversity=0.3597
  - TENSION: drift=0.1746, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1754, convergence=0.6800, diversity=0.4631
  - CLOSING: drift=0.1812, convergence=0.6833, diversity=0.5097

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### guided:engine_structural
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1690 (+/- 0.0183)
- Clean persona drift MAE: 0.1690
- Per-trait absolute error: O 0.1638, C 0.2212, E 0.1297, A 0.1589, N 0.1716
- Relationship inconsistency: 0.1163
- Relationship shift rate: 0.3075
- Relationship overshoot rate: 0.2400
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0372
- Clean envelope violations: 2.0372
- Structured action validity: 0.7833
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.2000
- Action-plan alignment: 0.9645
- Planned action coverage: 0.9351
- Action family convergence: 0.6967
- Role action diversity: 0.5069
- Negotiation uniqueness: 0.3021
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1059
- Repetition rate: 0.0000
- Topic drift rate: 0.5622
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1644, 0.1737]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=0.8111, diversity=0.3764
  - TENSION: drift=0.1743, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1714, convergence=0.6789, diversity=0.4978
  - CLOSING: drift=0.1834, convergence=0.5500, diversity=0.6125

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate


## Family Summary
### algorithmic_accountability:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1802 (+/- 0.0060)
- Clean persona drift MAE: 0.1802
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1140, A 0.2333, N 0.1300
- Relationship inconsistency: 0.2753
- Relationship shift rate: 0.3256
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5834
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.5000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1147
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0002
- Mean turns: 11.00
- Persona drift 95% CI: [0.1718, 0.1885]

- Phase-level quality:
  - OPENING: drift=0.1756, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1747, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1941, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, fallback_utterance_rate, repetition_rate

### corporate_acquisition:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1710 (+/- 0.0102)
- Clean persona drift MAE: 0.1710
- Per-trait absolute error: O 0.1603, C 0.2218, E 0.1322, A 0.1552, N 0.1856
- Relationship inconsistency: 0.0011
- Relationship shift rate: 0.2383
- Relationship overshoot rate: 0.0750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2833
- Clean envelope violations: 2.2833
- Structured action validity: 0.7667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9737
- Planned action coverage: 1.0000
- Action family convergence: 0.5556
- Role action diversity: 0.5833
- Negotiation uniqueness: 0.3614
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1077
- Repetition rate: 0.0000
- Topic drift rate: 0.4794
- Fallback taxonomy: n/a
- State trajectory variance: 0.0079
- Mean turns: 15.67
- Persona drift 95% CI: [0.1629, 0.1792]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1799, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1691, convergence=0.5889, diversity=0.5556
  - CLOSING: drift=0.2003, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_crisis:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1727 (+/- 0.0144)
- Clean persona drift MAE: 0.1727
- Per-trait absolute error: O 0.1611, C 0.2259, E 0.1520, A 0.1667, N 0.1575
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2030
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1292
- Clean envelope violations: 2.1292
- Structured action validity: 0.5458
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9707
- Planned action coverage: 1.0000
- Action family convergence: 0.7333
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.2841
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1103
- Repetition rate: 0.0000
- Topic drift rate: 0.5227
- Fallback taxonomy: n/a
- State trajectory variance: 0.0072
- Mean turns: 16.50
- Persona drift 95% CI: [0.1627, 0.1827]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1744, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1785, convergence=0.6750, diversity=0.5000
  - CLOSING: drift=0.1774, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1598 (+/- 0.0034)
- Clean persona drift MAE: 0.1598
- Per-trait absolute error: O 0.1240, C 0.2286, E 0.1549, A 0.1415, N 0.1500
- Relationship inconsistency: 0.2600
- Relationship shift rate: 0.3806
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1003
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1551, 0.1645]

- Phase-level quality:
  - OPENING: drift=0.1686, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1726, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1363, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1784, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1855 (+/- 0.0018)
- Clean persona drift MAE: 0.1855
- Per-trait absolute error: O 0.1930, C 0.2800, E 0.1436, A 0.1589, N 0.1518
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2616
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5714
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
- Dialogue coherence: 0.1029
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.183, 0.188]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1891, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1963, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1804, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1505 (+/- 0.0098)
- Clean persona drift MAE: 0.1505
- Per-trait absolute error: O 0.1240, C 0.2082, E 0.1375, A 0.1145, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2601
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.1332
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1368, 0.1641]

- Phase-level quality:
  - OPENING: drift=0.1663, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1364, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1570, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1977, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1806 (+/- 0.0089)
- Clean persona drift MAE: 0.1806
- Per-trait absolute error: O 0.1595, C 0.2300, E 0.1492, A 0.1881, N 0.1762
- Relationship inconsistency: 0.2406
- Relationship shift rate: 0.2927
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3750
- Clean envelope violations: 2.3750
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9625
- Planned action coverage: 0.7500
- Action family convergence: 0.9166
- Role action diversity: 0.3510
- Negotiation uniqueness: 0.1734
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1058
- Repetition rate: 0.0000
- Topic drift rate: 0.5324
- Fallback taxonomy: n/a
- State trajectory variance: 0.0050
- Mean turns: 18.00
- Persona drift 95% CI: [0.1718, 0.1894]

- Phase-level quality:
  - OPENING: drift=0.1865, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1795, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1852, convergence=0.8334, diversity=0.3833
  - CLOSING: drift=0.1953, convergence=1.0000, diversity=0.3958

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### ethical_dilemma:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1738 (+/- 0.0090)
- Clean persona drift MAE: 0.1738
- Per-trait absolute error: O 0.0867, C 0.3000, E 0.1273, A 0.1550, N 0.2000
- Relationship inconsistency: 0.0282
- Relationship shift rate: 0.2445
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
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
- Dialogue coherence: 0.1174
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1613, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1835, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1829, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1913, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1951, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1581 (+/- 0.0067)
- Clean persona drift MAE: 0.1581
- Per-trait absolute error: O 0.1769, C 0.2430, E 0.0834, A 0.1409, N 0.1461
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2216
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0833
- Clean envelope violations: 2.0833
- Structured action validity: 0.5834
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9716
- Planned action coverage: 1.0000
- Action family convergence: 0.7125
- Role action diversity: 0.4896
- Negotiation uniqueness: 0.2954
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1148
- Repetition rate: 0.0000
- Topic drift rate: 0.4659
- Fallback taxonomy: n/a
- State trajectory variance: 0.0056
- Mean turns: 16.50
- Persona drift 95% CI: [0.1515, 0.1646]

- Phase-level quality:
  - OPENING: drift=0.1607, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1629, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1684, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1635, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1663 (+/- 0.0050)
- Clean persona drift MAE: 0.1663
- Per-trait absolute error: O 0.2180, C 0.1981, E 0.1019, A 0.1295, N 0.1845
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3050
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.1667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 1.0000
- Role action diversity: 0.1875
- Negotiation uniqueness: 0.0909
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1595, 0.1732]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1726, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1731, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1548, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1651 (+/- 0.0028)
- Clean persona drift MAE: 0.1651
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1127, A 0.1185, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3449
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.7500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1288
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1611, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1900, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1545, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1713, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.2022, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_scandal:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0225)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.2153, C 0.2050, E 0.1700, A 0.1583, N 0.1487
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1290
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.3333
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9607
- Planned action coverage: 0.6363
- Action family convergence: 0.7500
- Role action diversity: 0.6736
- Negotiation uniqueness: 0.2619
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0898
- Repetition rate: 0.0000
- Topic drift rate: 0.5893
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1574, 0.2015]

- Phase-level quality:
  - OPENING: drift=0.1729, convergence=0.3333, diversity=0.2500
  - TENSION: drift=0.1883, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1808, convergence=0.5834, diversity=0.3750
  - CLOSING: drift=0.1936, convergence=0.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1813 (+/- 0.0037)
- Clean persona drift MAE: 0.1813
- Per-trait absolute error: O 0.1690, C 0.2462, E 0.1436, A 0.2145, N 0.1331
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.2915
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1016
- Repetition rate: 0.0000
- Topic drift rate: 0.7046
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1762, 0.1863]

- Phase-level quality:
  - OPENING: drift=0.1866, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1784, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1965, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1670, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### historical_injustice:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0007)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.1433, C 0.3000, E 0.1000, A 0.2567, N 0.1000
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.1621
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
- Role action diversity: 0.6111
- Negotiation uniqueness: 0.1714
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.179, 0.181]

- Phase-level quality:
  - OPENING: drift=0.1736, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1749, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1716, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1960, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### hybrid_work_policy:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1774 (+/- 0.0028)
- Clean persona drift MAE: 0.1774
- Per-trait absolute error: O 0.1366, C 0.2333, E 0.1605, A 0.1567, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1200
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
- Dialogue coherence: 0.1166
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1736, 0.1813]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1804, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1901, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.1733, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### infrastructure_decision:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1634 (+/- 0.0024)
- Clean persona drift MAE: 0.1634
- Per-trait absolute error: O 0.1140, C 0.2172, E 0.1358, A 0.1180, N 0.2320
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2875
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.0741
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0886
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1601, 0.1667]

- Phase-level quality:
  - OPENING: drift=0.1734, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1850, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1621, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1680, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### institutional_failure:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1785 (+/- 0.0007)
- Clean persona drift MAE: 0.1785
- Per-trait absolute error: O 0.2100, C 0.2093, E 0.1276, A 0.2195, N 0.1260
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3420
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1091
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1775, 0.1795]

- Phase-level quality:
  - OPENING: drift=0.1988, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1633, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1785, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2206, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1888 (+/- 0.0018)
- Clean persona drift MAE: 0.1888
- Per-trait absolute error: O 0.1870, C 0.1800, E 0.2076, A 0.1881, N 0.1811
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3035
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0976
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1862, 0.1913]

- Phase-level quality:
  - OPENING: drift=0.1972, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1930, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1918, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1876, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_dispute:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1769 (+/- 0.0048)
- Clean persona drift MAE: 0.1769
- Per-trait absolute error: O 0.1140, C 0.2000, E 0.1328, A 0.2230, N 0.2150
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2775
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9000
- Clean envelope violations: 1.9000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.4479
- Negotiation uniqueness: 0.0801
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1021
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1702, 0.1837]

- Phase-level quality:
  - OPENING: drift=0.1823, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1816, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1787, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.2189, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_negotiation:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1480 (+/- 0.0100)
- Clean persona drift MAE: 0.1480
- Per-trait absolute error: O 0.1900, C 0.1000, E 0.0832, A 0.1667, N 0.2000
- Relationship inconsistency: 0.1215
- Relationship shift rate: 0.4027
- Relationship overshoot rate: 0.4500
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
- Role action diversity: 0.3959
- Negotiation uniqueness: 0.0955
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1271
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1342, 0.1617]

- Phase-level quality:
  - OPENING: drift=0.1550, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1496, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1409, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1640, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_policy_reform:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1603 (+/- 0.0011)
- Clean persona drift MAE: 0.1603
- Per-trait absolute error: O 0.1960, C 0.1741, E 0.1371, A 0.1431, N 0.1511
- Relationship inconsistency: 0.4190
- Relationship shift rate: 0.3655
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
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
- Dialogue coherence: 0.1023
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1587, 0.1618]

- Phase-level quality:
  - OPENING: drift=0.1446, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1870, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1578, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1646, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1523 (+/- 0.0037)
- Clean persona drift MAE: 0.1523
- Per-trait absolute error: O 0.1620, C 0.2400, E 0.0814, A 0.1145, N 0.1640
- Relationship inconsistency: 0.2502
- Relationship shift rate: 0.6203
- Relationship overshoot rate: 0.4500
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
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0981
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1472, 0.1575]

- Phase-level quality:
  - OPENING: drift=0.1554, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1498, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1507, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2041, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1624 (+/- 0.0032)
- Clean persona drift MAE: 0.1624
- Per-trait absolute error: O 0.1740, C 0.1976, E 0.1296, A 0.1731, N 0.1378
- Relationship inconsistency: 0.1064
- Relationship shift rate: 0.3320
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5982
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9670
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1002
- Repetition rate: 0.0000
- Topic drift rate: 0.8636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0004
- Mean turns: 22.00
- Persona drift 95% CI: [0.1581, 0.1668]

- Phase-level quality:
  - OPENING: drift=0.1777, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1477, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1753, convergence=0.6000, diversity=0.5000
  - CLOSING: drift=0.1513, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_rights:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1928 (+/- 0.0003)
- Clean persona drift MAE: 0.1928
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.1089, A 0.1850, N 0.1934
- Relationship inconsistency: 0.3630
- Relationship shift rate: 0.6060
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1340
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0931
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1924, 0.1932]

- Phase-level quality:
  - OPENING: drift=0.1894, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.2027, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.2014, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1735, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### platform_governance:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1924 (+/- 0.0123)
- Clean persona drift MAE: 0.1924
- Per-trait absolute error: O 0.2215, C 0.2176, E 0.1805, A 0.1692, N 0.1729
- Relationship inconsistency: 0.3815
- Relationship shift rate: 0.3814
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5583
- Clean envelope violations: 2.5583
- Structured action validity: 0.7125
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9739
- Planned action coverage: 1.0000
- Action family convergence: 0.5834
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0975
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0030
- Mean turns: 16.50
- Persona drift 95% CI: [0.1803, 0.2044]

- Phase-level quality:
  - OPENING: drift=0.1893, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.2005, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1913, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1827, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1928 (+/- 0.0020)
- Clean persona drift MAE: 0.1928
- Per-trait absolute error: O 0.1680, C 0.2090, E 0.1795, A 0.1875, N 0.2200
- Relationship inconsistency: 0.0959
- Relationship shift rate: 0.2749
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
- Action-plan alignment: 0.9643
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1061
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.19, 0.1955]

- Phase-level quality:
  - OPENING: drift=0.2089, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1932, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1754, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_failure:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1541 (+/- 0.0055)
- Clean persona drift MAE: 0.1541
- Per-trait absolute error: O 0.1440, C 0.2108, E 0.1063, A 0.2095, N 0.1000
- Relationship inconsistency: 0.1588
- Relationship shift rate: 0.3650
- Relationship overshoot rate: 0.4500
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
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1046
- Repetition rate: 0.0000
- Topic drift rate: 0.1071
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1465, 0.1617]

- Phase-level quality:
  - OPENING: drift=0.1552, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1492, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1285, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1900, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_negotiation:engine_structural
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1507 (+/- 0.0077)
- Clean persona drift MAE: 0.1507
- Per-trait absolute error: O 0.1204, C 0.1913, E 0.1258, A 0.1441, N 0.1718
- Relationship inconsistency: 0.2223
- Relationship shift rate: 0.3600
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6833
- Clean envelope violations: 1.6833
- Structured action validity: 0.8095
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1667
- Action-plan alignment: 0.9616
- Planned action coverage: 1.0000
- Action family convergence: 0.6111
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3398
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1205
- Repetition rate: 0.0000
- Topic drift rate: 0.5151
- Fallback taxonomy: n/a
- State trajectory variance: 0.0073
- Mean turns: 15.67
- Persona drift 95% CI: [0.1445, 0.1569]

- Phase-level quality:
  - OPENING: drift=0.1515, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1594, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1578, convergence=0.6667, diversity=0.4861
  - CLOSING: drift=0.1652, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### post-disaster_recovery:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1666 (+/- 0.0051)
- Clean persona drift MAE: 0.1666
- Per-trait absolute error: O 0.1333, C 0.2376, E 0.1149, A 0.1409, N 0.2061
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3625
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.6459
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9728
- Planned action coverage: 1.0000
- Action family convergence: 0.6083
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.3409
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0978
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0034
- Mean turns: 16.50
- Persona drift 95% CI: [0.1616, 0.1716]

- Phase-level quality:
  - OPENING: drift=0.1585, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1795, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1723, convergence=0.5500, diversity=0.5834
  - CLOSING: drift=0.1873, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_health_crisis:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1704 (+/- 0.0040)
- Clean persona drift MAE: 0.1704
- Per-trait absolute error: O 0.1540, C 0.2422, E 0.1147, A 0.1630, N 0.1780
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2477
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.1483
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.2857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1649, 0.1759]

- Phase-level quality:
  - OPENING: drift=0.1784, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1718, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1855, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1510, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### public_health_failure:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1881 (+/- 0.0244)
- Clean persona drift MAE: 0.1881
- Per-trait absolute error: O 0.2100, C 0.2067, E 0.1183, A 0.2081, N 0.1978
- Relationship inconsistency: 0.2072
- Relationship shift rate: 0.2751
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4833
- Clean envelope violations: 2.4833
- Structured action validity: 0.5834
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9767
- Planned action coverage: 1.0000
- Action family convergence: 0.5958
- Role action diversity: 0.5521
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1195
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0078
- Mean turns: 16.50
- Persona drift 95% CI: [0.1642, 0.2121]

- Phase-level quality:
  - OPENING: drift=0.1866, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1955, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1864, convergence=0.6000, diversity=0.5417
  - CLOSING: drift=0.1896, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_housing_crisis:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1903 (+/- 0.0110)
- Clean persona drift MAE: 0.1903
- Per-trait absolute error: O 0.1600, C 0.2667, E 0.1000, A 0.2117, N 0.2133
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1100
- Relationship overshoot rate: 0.0000
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
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5417
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0954
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1751, 0.2055]

- Phase-level quality:
  - OPENING: drift=0.1902, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1910, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1863, convergence=0.5000, diversity=0.6667
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy:engine_structural
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1598 (+/- 0.0116)
- Clean persona drift MAE: 0.1598
- Per-trait absolute error: O 0.1144, C 0.2058, E 0.1269, A 0.1582, N 0.1935
- Relationship inconsistency: 0.0565
- Relationship shift rate: 0.2587
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8375
- Clean envelope violations: 1.8375
- Structured action validity: 0.3750
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9671
- Planned action coverage: 1.0000
- Action family convergence: 0.5958
- Role action diversity: 0.5859
- Negotiation uniqueness: 0.4164
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1087
- Repetition rate: 0.0000
- Topic drift rate: 0.5666
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1517, 0.1678]

- Phase-level quality:
  - OPENING: drift=0.1681, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1709, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1711, convergence=0.5250, diversity=0.6146
  - CLOSING: drift=0.1604, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy_crisis:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1841 (+/- 0.0075)
- Clean persona drift MAE: 0.1841
- Per-trait absolute error: O 0.1450, C 0.2600, E 0.1685, A 0.1720, N 0.1750
- Relationship inconsistency: 0.0015
- Relationship shift rate: 0.3749
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.9500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9544
- Planned action coverage: 0.7046
- Action family convergence: 0.8125
- Role action diversity: 0.4135
- Negotiation uniqueness: 0.2221
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0909
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0050
- Mean turns: 18.00
- Persona drift 95% CI: [0.1767, 0.1914]

- Phase-level quality:
  - OPENING: drift=0.1850, convergence=0.8334, diversity=0.3542
  - TENSION: drift=0.1928, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.1866, convergence=0.7500, diversity=0.4042
  - CLOSING: drift=0.2062, convergence=1.0000, diversity=0.4375

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_compliance:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1613 (+/- 0.0103)
- Clean persona drift MAE: 0.1613
- Per-trait absolute error: O 0.2073, C 0.2167, E 0.0866, A 0.1313, N 0.1650
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2217
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7833
- Clean envelope violations: 1.7833
- Structured action validity: 0.9375
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9680
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6719
- Negotiation uniqueness: 0.4643
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1124
- Repetition rate: 0.0000
- Topic drift rate: 0.4919
- Fallback taxonomy: n/a
- State trajectory variance: 0.0019
- Mean turns: 12.50
- Persona drift 95% CI: [0.1512, 0.1715]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1635, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1642, convergence=0.5000, diversity=0.6459
  - CLOSING: drift=0.1742, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_crisis:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1585 (+/- 0.0011)
- Clean persona drift MAE: 0.1585
- Per-trait absolute error: O 0.1730, C 0.2500, E 0.1154, A 0.1538, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7417
- Role action diversity: 0.3959
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1230
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0001
- Mean turns: 22.00
- Persona drift 95% CI: [0.157, 0.16]

- Phase-level quality:
  - OPENING: drift=0.1525, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1675, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1561, convergence=0.7000, diversity=0.4166
  - CLOSING: drift=0.1605, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_decision:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0066)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1283, C 0.2800, E 0.0880, A 0.1619, N 0.1677
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1114
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0333
- Clean envelope violations: 2.0333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9667
- Planned action coverage: 1.0000
- Action family convergence: 0.8542
- Role action diversity: 0.4531
- Negotiation uniqueness: 0.2516
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1134
- Repetition rate: 0.0000
- Topic drift rate: 0.1526
- Fallback taxonomy: n/a
- State trajectory variance: 0.0047
- Mean turns: 12.50
- Persona drift 95% CI: [0.1587, 0.1716]

- Phase-level quality:
  - OPENING: drift=0.1767, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1601, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1755, convergence=0.7500, diversity=0.4791
  - CLOSING: drift=0.1836, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_transition:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1534 (+/- 0.0057)
- Clean persona drift MAE: 0.1534
- Per-trait absolute error: O 0.1490, C 0.2024, E 0.1003, A 0.1542, N 0.1613
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3250
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
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
- Dialogue coherence: 0.1010
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1456, 0.1613]

- Phase-level quality:
  - OPENING: drift=0.1726, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1659, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1528, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1612, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:engine_structural
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1441 (+/- 0.0126)
- Clean persona drift MAE: 0.1441
- Per-trait absolute error: O 0.1300, C 0.2206, E 0.1260, A 0.1229, N 0.1210
- Relationship inconsistency: 0.2409
- Relationship shift rate: 0.3153
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.7857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9645
- Planned action coverage: 1.0000
- Action family convergence: 0.5458
- Role action diversity: 0.5677
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0915
- Repetition rate: 0.0000
- Topic drift rate: 0.4919
- Fallback taxonomy: n/a
- State trajectory variance: 0.0045
- Mean turns: 18.00
- Persona drift 95% CI: [0.1318, 0.1564]

- Phase-level quality:
  - OPENING: drift=0.1507, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1547, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1526, convergence=0.5500, diversity=0.5625
  - CLOSING: drift=0.1545, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### workplace_policy:engine_structural
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1997 (+/- 0.0026)
- Clean persona drift MAE: 0.1997
- Per-trait absolute error: O 0.2380, C 0.2200, E 0.1792, A 0.1975, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3759
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
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1017
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1962, 0.2033]

- Phase-level quality:
  - OPENING: drift=0.2155, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1986, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2003, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Feature Attribution: What Drives Each Trait Score

### Openness (O) — Mean Error: 0.1622

| Feature | engine_structural (n=720) |
|---------|------|
| idea_count | 0.357 |
| hypothetical_count | 0.031 |
| unique_word_ratio | 0.801 |

Calibration: static

### Conscientiousness (C) — Mean Error: 0.2230

| Feature | engine_structural (n=720) |
|---------|------|
| planning_count | 1.029 |
| structure_marker_count | 0.011 |
| detail_count | 0.000 |
| goal_reference_count | 0.000 |
| correction_count | 0.000 |

Calibration: dynamic

### Extraversion (E) — Mean Error: 0.1299

| Feature | engine_structural (n=720) |
|---------|------|
| exclamation_count | 0.000 |
| question_count | 0.000 |
| word_count | 0.000 |
| filler_count | 0.000 |

Calibration: dynamic

### Agreeableness (A) — Mean Error: 0.1645

| Feature | engine_structural (n=720) |
|---------|------|
| acknowledgment_count | 0.057 |
| disagreement_count | 0.051 |
| negation_count | 1.464 |
| politeness_count | 0.000 |
| compliment_count | 0.000 |

Calibration: dynamic

### Neuroticism (N) — Mean Error: 0.1701

| Feature | engine_structural (n=720) |
|---------|------|
| hedge_count | 0.274 |
| self_doubt_count | 0.000 |
| reassurance_seeking_count | 0.001 |
| apology_count | 0.000 |
| emotional_word_count | 0.044 |

Calibration: dynamic


## Decision Driver Analysis

### engine_structural — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 6175 | sycophancy_risk | 6175 |
| TENSION | identity_consistency | 6175 | sycophancy_risk | 6175 |
| NEGOTIATION | identity_consistency | 7012 | sycophancy_risk | 7012 |
| CLOSING | identity_consistency | 3804 | sycophancy_risk | 3804 |


## Per-Archetype Trait Error

| Archetype | n | O | C | E | A | N | MAE | Top Failed Trait |
|-----------|---|---|---|---|---|---|-----|-----------------|
| Academic researcher studying crypto market failures | 2 | 0.320 | 0.211 | 0.016 | 0.094 | 0.194 | 0.167 | O |
| Activision Blizzard game studio creative lead | 2 | 0.320 | 0.085 | 0.135 | 0.014 | 0.200 | 0.151 | O |
| Activision Shareholder | 2 | 0.130 | 0.309 | 0.055 | 0.302 | 0.091 | 0.177 | C |
| Activist investor | 6 | 0.070 | 0.426 | 0.197 | 0.263 | 0.254 | 0.242 | C |
| Ad-Tech Engineer | 6 | 0.133 | 0.248 | 0.086 | 0.190 | 0.045 | 0.141 | C |
| Aerospace insurance underwriter repricing risk for the MAX fleet. | 2 | 0.070 | 0.252 | 0.051 | 0.205 | 0.080 | 0.132 | C |
| Affected mother of three | 2 | 0.120 | 0.079 | 0.136 | 0.285 | 0.104 | 0.145 | A |
| Aging local worker | 2 | 0.330 | 0.120 | 0.203 | 0.010 | 0.100 | 0.153 | O |
| Alameda Research quant who uncovered the balance sheet discrepancy | 2 | 0.420 | 0.325 | 0.149 | 0.030 | 0.100 | 0.205 | O |
| Alameda Research quantitative analyst who discovered balance sheet irregularities | 2 | 0.270 | 0.338 | 0.154 | 0.089 | 0.083 | 0.187 | C |
| Alameda quant analyst | 2 | 0.420 | 0.267 | 0.285 | 0.130 | 0.005 | 0.221 | O |
| All-Hands Moderator | 2 | 0.270 | 0.096 | 0.245 | 0.194 | 0.002 | 0.161 | O |
| Amazon Fitness lead | 2 | 0.220 | 0.293 | 0.079 | 0.103 | 0.198 | 0.179 | C |
| Apple Fitness+ product lead | 4 | 0.245 | 0.282 | 0.035 | 0.098 | 0.241 | 0.180 | C |
| Bahamas Securities Commission supervisor who approved FTX license | 2 | 0.030 | 0.071 | 0.237 | 0.193 | 0.000 | 0.106 | E |
| Bahamas regulatory officer | 2 | 0.230 | 0.129 | 0.235 | 0.176 | 0.095 | 0.173 | E |
| Bahamian financial regulatory officer who approved FTX license | 2 | 0.080 | 0.335 | 0.047 | 0.206 | 0.206 | 0.175 | C |
| Barista-Organizer working two jobs | 2 | 0.320 | 0.081 | 0.106 | 0.026 | 0.122 | 0.131 | O |
| Barista-organizer working two jobs | 2 | 0.270 | 0.081 | 0.123 | 0.046 | 0.188 | 0.142 | O |
| Barista-organizer working two jobs, recently written up for 'tardiness' after union meetings | 2 | 0.270 | 0.089 | 0.127 | 0.100 | 0.070 | 0.131 | O |
| Bootstrapped SaaS Founder | 4 | 0.245 | 0.089 | 0.163 | 0.090 | 0.102 | 0.138 | O |
| Brick-and-mortar bookstore owner (Congestion Zone) | 2 | 0.030 | 0.058 | 0.231 | 0.076 | 0.056 | 0.090 | E |
| CEO of a regional airline with 14 grounded MAX aircraft, facing significant financial losses. | 2 | 0.130 | 0.262 | 0.185 | 0.090 | 0.290 | 0.191 | N |
| CFO | 2 | 0.030 | 0.451 | 0.038 | 0.194 | 0.102 | 0.163 | C |
| CRE Lease Negotiator | 2 | 0.130 | 0.347 | 0.112 | 0.011 | 0.298 | 0.179 | C |
| CRE Lease Strategist | 2 | 0.130 | 0.378 | 0.080 | 0.319 | 0.210 | 0.223 | C |
| Cabin crew safety representative | 2 | 0.170 | 0.196 | 0.044 | 0.316 | 0.100 | 0.165 | A |
| Centrelink call center team lead | 2 | 0.070 | 0.279 | 0.104 | 0.150 | 0.005 | 0.122 | C |
| Centrelink call center worker | 2 | 0.070 | 0.369 | 0.233 | 0.101 | 0.204 | 0.195 | C |
| Centrelink call center worker processing appeals | 2 | 0.070 | 0.233 | 0.130 | 0.104 | 0.000 | 0.107 | C |
| Centrelink middle manager | 2 | 0.030 | 0.314 | 0.050 | 0.204 | 0.204 | 0.160 | C |
| Chair of the pilots' union safety committee, advocating for extensive pilot retraining. | 2 | 0.120 | 0.386 | 0.034 | 0.195 | 0.090 | 0.165 | C |
| City council president | 2 | 0.050 | 0.130 | 0.291 | 0.202 | 0.196 | 0.174 | E |
| City economic development director | 2 | 0.050 | 0.227 | 0.225 | 0.084 | 0.002 | 0.118 | C |
| City official overseeing Prop C implementation | 2 | 0.030 | 0.258 | 0.362 | 0.013 | 0.135 | 0.159 | E |
| City policymaker | 2 | 0.120 | 0.242 | 0.164 | 0.006 | 0.211 | 0.149 | C |
| Clawback-targeted foundation | 2 | 0.270 | 0.099 | 0.115 | 0.361 | 0.220 | 0.213 | A |
| Cloud Infrastructure Architect | 2 | 0.170 | 0.238 | 0.042 | 0.031 | 0.093 | 0.115 | C |
| Cloud Infrastructure Engineer at Microsoft | 4 | 0.110 | 0.292 | 0.036 | 0.144 | 0.283 | 0.173 | C |
| College student (account borrower) | 2 | 0.470 | 0.271 | 0.121 | 0.103 | 0.016 | 0.196 | O |
| Commercial Real Estate Analyst | 2 | 0.170 | 0.330 | 0.014 | 0.213 | 0.022 | 0.150 | C |
| Commercial real estate analyst | 2 | 0.120 | 0.388 | 0.137 | 0.185 | 0.362 | 0.238 | C |
| Committee member who championed $10B investment | 2 | 0.070 | 0.451 | 0.296 | 0.205 | 0.098 | 0.224 | C |
| Community Church Leader organizing relief efforts | 2 | 0.270 | 0.088 | 0.178 | 0.400 | 0.320 | 0.251 | A |
| Community Church Pastor | 2 | 0.170 | 0.017 | 0.207 | 0.415 | 0.098 | 0.181 | A |
| Community Manager (Facing Layoffs) | 2 | 0.170 | 0.041 | 0.126 | 0.410 | 0.080 | 0.165 | A |
| Community church leader | 2 | 0.270 | 0.154 | 0.221 | 0.418 | 0.296 | 0.272 | A |
| Community legal aid lawyer | 2 | 0.220 | 0.293 | 0.037 | 0.351 | 0.096 | 0.199 | A |
| Community organizer | 2 | 0.120 | 0.157 | 0.294 | 0.286 | 0.126 | 0.197 | E |
| Competing streamer's retention strategist | 2 | 0.370 | 0.150 | 0.373 | 0.195 | 0.300 | 0.278 | E |
| Competitor exchange | 2 | 0.070 | 0.429 | 0.243 | 0.320 | 0.195 | 0.251 | C |
| Congestion zone business owner | 2 | 0.050 | 0.363 | 0.033 | 0.074 | 0.010 | 0.106 | C |
| Construction CEO | 2 | 0.080 | 0.208 | 0.321 | 0.297 | 0.019 | 0.185 | E |
| Construction union leader | 6 | 0.097 | 0.193 | 0.279 | 0.177 | 0.175 | 0.184 | E |
| Consumer Privacy Advocate | 2 | 0.370 | 0.062 | 0.102 | 0.296 | 0.293 | 0.225 | O |
| Consumer rights advocate | 2 | 0.170 | 0.022 | 0.032 | 0.311 | 0.200 | 0.147 | A |
| Corporate Communications VP | 2 | 0.030 | 0.205 | 0.189 | 0.007 | 0.178 | 0.122 | C |
| Corporate communications managing public perception | 2 | 0.070 | 0.245 | 0.286 | 0.006 | 0.100 | 0.141 | E |
| Corporate labor relations specialist | 2 | 0.030 | 0.270 | 0.245 | 0.323 | 0.038 | 0.181 | A |
| Corporate real estate director locked into unfavorable lease | 2 | 0.130 | 0.229 | 0.091 | 0.094 | 0.102 | 0.129 | C |
| Creative Director at Activision | 2 | 0.370 | 0.140 | 0.181 | 0.053 | 0.187 | 0.186 | O |
| Creative Director at Activision Blizzard | 2 | 0.220 | 0.205 | 0.079 | 0.215 | 0.240 | 0.192 | N |
| Customer/Disability Advocate | 2 | 0.170 | 0.168 | 0.031 | 0.265 | 0.344 | 0.196 | N |
| DPA Enforcement Officer | 2 | 0.180 | 0.303 | 0.074 | 0.299 | 0.071 | 0.185 | C |
| Data Protection Consultant | 2 | 0.080 | 0.365 | 0.118 | 0.004 | 0.216 | 0.156 | C |
| Data Protection Officer | 4 | 0.130 | 0.375 | 0.030 | 0.104 | 0.295 | 0.187 | C |
| Deaf Software Engineer | 2 | 0.370 | 0.405 | 0.048 | 0.100 | 0.090 | 0.203 | C |
| Deaf software engineer | 2 | 0.370 | 0.377 | 0.124 | 0.094 | 0.098 | 0.213 | C |
| Deaf software engineer at Zoom | 2 | 0.220 | 0.367 | 0.058 | 0.135 | 0.120 | 0.180 | C |
| Debt collection contractor | 2 | 0.130 | 0.031 | 0.232 | 0.288 | 0.118 | 0.160 | A |
| Director of charitable foundation facing FTX donation clawback | 2 | 0.170 | 0.235 | 0.026 | 0.294 | 0.094 | 0.164 | A |
| Disability advocate customer | 2 | 0.120 | 0.070 | 0.054 | 0.384 | 0.400 | 0.206 | N |
| Disability rights advocate | 4 | 0.170 | 0.021 | 0.064 | 0.266 | 0.282 | 0.161 | N |
| Disability rights advocate for mobility-limited gig workers | 2 | 0.070 | 0.099 | 0.076 | 0.315 | 0.010 | 0.114 | A |
| Disabled Transit Riders Alliance Director | 2 | 0.170 | 0.042 | 0.023 | 0.414 | 0.089 | 0.148 | A |
| Disaster Response Vet | 2 | 0.070 | 0.400 | 0.123 | 0.292 | 0.089 | 0.195 | C |
| Disney+ retention strategist | 4 | 0.370 | 0.046 | 0.238 | 0.111 | 0.185 | 0.190 | O |
| EPA regional administrator | 2 | 0.170 | 0.208 | 0.020 | 0.004 | 0.096 | 0.099 | C |
| ER physician | 2 | 0.070 | 0.397 | 0.026 | 0.083 | 0.311 | 0.177 | C |
| ER physician treating 20+ medical emergencies per week from encampments | 2 | 0.070 | 0.386 | 0.008 | 0.075 | 0.260 | 0.160 | C |
| ER physician treating encampment-related emergencies | 2 | 0.070 | 0.375 | 0.018 | 0.094 | 0.265 | 0.164 | C |
| EU Parliament Aide | 2 | 0.100 | 0.240 | 0.078 | 0.168 | 0.193 | 0.156 | C |
| EU Policy Strategist | 2 | 0.220 | 0.333 | 0.007 | 0.004 | 0.100 | 0.133 | C |
| Elderly flat owner | 4 | 0.180 | 0.174 | 0.061 | 0.397 | 0.175 | 0.197 | A |
| Employee Resource Group Lead | 2 | 0.370 | 0.005 | 0.085 | 0.294 | 0.015 | 0.154 | O |
| Employment Lawyer | 2 | 0.130 | 0.402 | 0.018 | 0.011 | 0.202 | 0.153 | C |
| Engineering Director | 2 | 0.050 | 0.178 | 0.275 | 0.100 | 0.215 | 0.164 | E |
| Engineering Manager | 2 | 0.070 | 0.226 | 0.332 | 0.100 | 0.198 | 0.185 | E |
| Enterprise Tenant (Fortune 500 CFO) | 2 | 0.130 | 0.342 | 0.260 | 0.120 | 0.275 | 0.225 | C |
| Enterprise Tenant Representative | 2 | 0.130 | 0.294 | 0.085 | 0.100 | 0.125 | 0.147 | C |
| Environmental Justice Coalition Organizer | 2 | 0.420 | 0.058 | 0.021 | 0.202 | 0.311 | 0.203 | O |
| Esports League Organizer | 4 | 0.030 | 0.282 | 0.340 | 0.189 | 0.117 | 0.191 | E |
| European Union Aviation Safety Agency representative | 2 | 0.220 | 0.345 | 0.072 | 0.133 | 0.200 | 0.194 | C |
| Evacuee | 2 | 0.230 | 0.051 | 0.185 | 0.014 | 0.411 | 0.178 | N |
| Executive facing financial losses from grounded fleet | 2 | 0.130 | 0.241 | 0.197 | 0.106 | 0.000 | 0.135 | C |
| FAA Certification Lead | 2 | 0.080 | 0.376 | 0.084 | 0.160 | 0.020 | 0.144 | C |
| FAA advisory panel member advocating for crash victims | 2 | 0.370 | 0.120 | 0.201 | 0.016 | 0.200 | 0.181 | O |
| FDA Investigator | 2 | 0.120 | 0.437 | 0.027 | 0.215 | 0.289 | 0.217 | C |
| FDIC Field Examiner | 4 | 0.180 | 0.274 | 0.047 | 0.104 | 0.099 | 0.141 | C |
| FDIC Resolution Field Examiner | 2 | 0.130 | 0.319 | 0.041 | 0.318 | 0.000 | 0.162 | C |
| FTC Regulatory Attorney | 2 | 0.070 | 0.409 | 0.040 | 0.202 | 0.213 | 0.187 | C |
| FTC antitrust specialist | 2 | 0.130 | 0.185 | 0.021 | 0.089 | 0.100 | 0.105 | C |
| FTC regulator | 2 | 0.070 | 0.393 | 0.150 | 0.086 | 0.298 | 0.199 | C |
| FTX bankruptcy trustee overseeing asset recovery | 2 | 0.070 | 0.380 | 0.014 | 0.206 | 0.294 | 0.193 | C |
| Facing layoffs after building member relationships | 2 | 0.220 | 0.078 | 0.310 | 0.312 | 0.020 | 0.188 | A |
| Factory foreman | 2 | 0.130 | 0.074 | 0.029 | 0.016 | 0.222 | 0.094 | N |
| Fed Emergency Lending Officer | 2 | 0.130 | 0.292 | 0.041 | 0.188 | 0.199 | 0.170 | C |
| Fertility doctor | 2 | 0.170 | 0.332 | 0.029 | 0.286 | 0.203 | 0.204 | C |
| Fired Organizer (Buffalo original) | 2 | 0.420 | 0.170 | 0.327 | 0.091 | 0.222 | 0.246 | O |
| Fishing Cooperative Leader | 6 | 0.163 | 0.230 | 0.031 | 0.115 | 0.285 | 0.165 | N |
| Former FTX software engineer who built withdrawal systems | 2 | 0.370 | 0.235 | 0.126 | 0.094 | 0.006 | 0.166 | O |
| Former Plant Worker | 2 | 0.030 | 0.076 | 0.215 | 0.003 | 0.189 | 0.103 | E |
| Former executive team member | 2 | 0.170 | 0.173 | 0.399 | 0.006 | 0.202 | 0.190 | E |
| Former sub-postmaster convicted of theft | 2 | 0.130 | 0.251 | 0.088 | 0.197 | 0.403 | 0.214 | N |
| Former sub-postmaster wrongfully convicted | 4 | 0.180 | 0.212 | 0.068 | 0.216 | 0.143 | 0.164 | A |
| Formerly unhoused advocate | 2 | 0.120 | 0.121 | 0.204 | 0.205 | 0.111 | 0.152 | A |
| Formerly unhoused mentor in supportive housing | 2 | 0.070 | 0.030 | 0.144 | 0.287 | 0.140 | 0.134 | A |
| Fujitsu PR director | 2 | 0.130 | 0.124 | 0.325 | 0.198 | 0.203 | 0.196 | E |
| Fujitsu lead developer (2005-2012) | 4 | 0.370 | 0.062 | 0.108 | 0.347 | 0.101 | 0.198 | O |
| Fujitsu lead developer (Horizon team) | 2 | 0.170 | 0.403 | 0.055 | 0.302 | 0.210 | 0.228 | C |
| Game Engine Architect | 2 | 0.370 | 0.085 | 0.087 | 0.193 | 0.187 | 0.184 | O |
| Gaming Journalist | 2 | 0.370 | 0.015 | 0.145 | 0.104 | 0.087 | 0.144 | O |
| Gig platform policy lead | 2 | 0.120 | 0.450 | 0.246 | 0.196 | 0.092 | 0.221 | C |
| Gig worker advocate | 2 | 0.270 | 0.098 | 0.155 | 0.178 | 0.078 | 0.156 | O |
| Government data scientist | 2 | 0.370 | 0.393 | 0.151 | 0.121 | 0.004 | 0.208 | C |
| Government data scientist who flagged algorithm flaws | 2 | 0.370 | 0.405 | 0.034 | 0.210 | 0.100 | 0.224 | C |
| Government engineer overseeing recertification | 2 | 0.080 | 0.316 | 0.014 | 0.094 | 0.200 | 0.141 | C |
| Government labor inspector | 2 | 0.030 | 0.204 | 0.019 | 0.086 | 0.165 | 0.101 | C |
| HDB policymaker | 2 | 0.030 | 0.280 | 0.158 | 0.004 | 0.119 | 0.118 | C |
| HR Diversity Officer | 2 | 0.120 | 0.351 | 0.014 | 0.394 | 0.120 | 0.200 | A |
| Hochul Administration Representative | 2 | 0.280 | 0.032 | 0.404 | 0.024 | 0.189 | 0.186 | E |
| Homeless shelter resident | 2 | 0.050 | 0.109 | 0.063 | 0.177 | 0.089 | 0.098 | A |
| Homeowners association president | 2 | 0.230 | 0.221 | 0.063 | 0.189 | 0.211 | 0.183 | O |
| Hospital EMS coordinator | 2 | 0.030 | 0.374 | 0.120 | 0.199 | 0.098 | 0.164 | C |
| Hospital Procurement Director | 4 | 0.050 | 0.229 | 0.080 | 0.161 | 0.239 | 0.152 | N |
| Hospital procurement director who integrated Theranos devices | 2 | 0.070 | 0.254 | 0.141 | 0.082 | 0.070 | 0.124 | C |
| Immigration rights lawyer | 4 | 0.320 | 0.131 | 0.140 | 0.383 | 0.198 | 0.234 | A |
| Immigration rights lawyer pushing reform | 2 | 0.320 | 0.187 | 0.133 | 0.076 | 0.215 | 0.186 | O |
| In-house counsel managing liability exposure | 2 | 0.230 | 0.402 | 0.084 | 0.088 | 0.198 | 0.201 | C |
| Indie Game Developer | 2 | 0.320 | 0.040 | 0.051 | 0.215 | 0.109 | 0.147 | O |
| Indigenous elder affected by debt notice | 2 | 0.070 | 0.142 | 0.056 | 0.307 | 0.004 | 0.116 | A |
| Institutional investor monitoring Boeing's recovery | 2 | 0.030 | 0.180 | 0.141 | 0.223 | 0.000 | 0.115 | A |
| Insurance Underwriter | 2 | 0.050 | 0.179 | 0.035 | 0.091 | 0.195 | 0.110 | N |
| International Observer | 2 | 0.370 | 0.224 | 0.041 | 0.102 | 0.089 | 0.165 | O |
| Investigative journalist | 2 | 0.470 | 0.024 | 0.157 | 0.064 | 0.092 | 0.162 | O |
| Investigative reporter covering the recertification process | 2 | 0.470 | 0.145 | 0.135 | 0.234 | 0.000 | 0.197 | O |
| Investor who introduced others to FTX yield program | 2 | 0.030 | 0.043 | 0.109 | 0.099 | 0.294 | 0.115 | N |
| Jia Wei's fiancée | 4 | 0.050 | 0.376 | 0.187 | 0.194 | 0.168 | 0.195 | C |
| Journalist covering the FTX collapse for major financial publication | 2 | 0.470 | 0.111 | 0.106 | 0.106 | 0.194 | 0.197 | O |
| Korean Import Regulator | 2 | 0.170 | 0.300 | 0.079 | 0.020 | 0.189 | 0.152 | C |
| Lab technician at Theranos who knows the tests are unreliable | 2 | 0.120 | 0.369 | 0.193 | 0.080 | 0.290 | 0.210 | C |
| Labor advocate for laid-off staff | 2 | 0.370 | 0.042 | 0.331 | 0.201 | 0.102 | 0.209 | O |
| Labor union organizer | 4 | 0.160 | 0.184 | 0.180 | 0.083 | 0.185 | 0.158 | N |
| Labor union organizer advocating for full employment benefits | 2 | 0.170 | 0.400 | 0.178 | 0.005 | 0.260 | 0.203 | C |
| Language school operator | 2 | 0.080 | 0.274 | 0.066 | 0.088 | 0.022 | 0.106 | C |
| Language school operator profiting from training fees | 2 | 0.100 | 0.349 | 0.121 | 0.214 | 0.315 | 0.220 | C |
| Legacy Media CTO | 2 | 0.050 | 0.089 | 0.025 | 0.071 | 0.107 | 0.068 | N |
| Local Journalist Covering Labor | 2 | 0.270 | 0.030 | 0.118 | 0.157 | 0.022 | 0.120 | O |
| Local Mayor | 4 | 0.050 | 0.214 | 0.203 | 0.116 | 0.047 | 0.126 | C |
| Local Municipal Leader | 2 | 0.070 | 0.127 | 0.187 | 0.125 | 0.060 | 0.114 | E |
| Local elected official | 2 | 0.220 | 0.136 | 0.217 | 0.007 | 0.003 | 0.117 | O |
| Local journalist | 4 | 0.445 | 0.142 | 0.163 | 0.154 | 0.137 | 0.208 | O |
| Longtime customer and disability advocate worried about service consistency | 2 | 0.170 | 0.063 | 0.036 | 0.150 | 0.330 | 0.150 | N |
| Lyft driver | 2 | 0.070 | 0.022 | 0.085 | 0.106 | 0.144 | 0.085 | N |
| MP (Select Committee member) | 2 | 0.050 | 0.132 | 0.182 | 0.103 | 0.005 | 0.094 | E |
| MTA Capital Projects Director | 2 | 0.120 | 0.344 | 0.176 | 0.163 | 0.289 | 0.218 | C |
| MTA capital projects manager | 4 | 0.120 | 0.285 | 0.148 | 0.056 | 0.191 | 0.160 | C |
| Media ethics professor | 2 | 0.370 | 0.105 | 0.010 | 0.192 | 0.104 | 0.156 | O |
| Medical Journalist Investigating | 2 | 0.420 | 0.137 | 0.133 | 0.007 | 0.189 | 0.177 | O |
| Medical Researcher | 4 | 0.195 | 0.123 | 0.118 | 0.251 | 0.318 | 0.201 | N |
| Mental health counselor | 2 | 0.170 | 0.193 | 0.076 | 0.401 | 0.207 | 0.209 | A |
| Microsoft Azure gaming infrastructure engineer | 2 | 0.030 | 0.312 | 0.159 | 0.201 | 0.300 | 0.201 | C |
| Microsoft Teams Enterprise Sales Director | 2 | 0.120 | 0.066 | 0.385 | 0.217 | 0.290 | 0.216 | E |
| Microsoft Teams Sales Director | 2 | 0.270 | 0.077 | 0.325 | 0.178 | 0.002 | 0.170 | E |
| Minister for Postal Affairs | 2 | 0.070 | 0.324 | 0.162 | 0.087 | 0.219 | 0.172 | C |
| Ministry of Health official | 2 | 0.130 | 0.204 | 0.020 | 0.084 | 0.078 | 0.103 | C |
| Mt. Sinai ER Transport Coordinator | 2 | 0.030 | 0.268 | 0.062 | 0.187 | 0.089 | 0.127 | C |
| NYPD Traffic Chief | 2 | 0.130 | 0.293 | 0.031 | 0.319 | 0.189 | 0.192 | A |
| Netflix APAC content negotiator | 2 | 0.050 | 0.400 | 0.130 | 0.100 | 0.238 | 0.184 | C |
| Netflix anti-fraud engineer | 4 | 0.070 | 0.315 | 0.033 | 0.007 | 0.235 | 0.132 | C |
| Netflix customer service rep | 2 | 0.230 | 0.156 | 0.036 | 0.392 | 0.027 | 0.168 | A |
| Netflix investor relations | 2 | 0.030 | 0.405 | 0.327 | 0.197 | 0.282 | 0.248 | C |
| Netflix licensing negotiator (APAC) | 2 | 0.170 | 0.356 | 0.258 | 0.103 | 0.227 | 0.223 | C |
| Netflix regional content licensing negotiator | 2 | 0.070 | 0.408 | 0.233 | 0.072 | 0.200 | 0.197 | C |
| Nonprofit director | 2 | 0.370 | 0.246 | 0.246 | 0.294 | 0.289 | 0.289 | O |
| NordVPN product lead | 2 | 0.220 | 0.072 | 0.324 | 0.294 | 0.188 | 0.219 | E |
| NordVPN product manager | 2 | 0.270 | 0.129 | 0.294 | 0.197 | 0.282 | 0.235 | E |
| Nuclear Evacuee | 2 | 0.050 | 0.093 | 0.345 | 0.021 | 0.415 | 0.185 | N |
| Office Experience Lead | 2 | 0.070 | 0.296 | 0.161 | 0.100 | 0.198 | 0.165 | C |
| Outer-borough delivery driver | 4 | 0.130 | 0.183 | 0.083 | 0.116 | 0.094 | 0.121 | C |
| Outer-borough package delivery driver (UPS/FedEx) | 2 | 0.130 | 0.193 | 0.024 | 0.052 | 0.111 | 0.102 | C |
| Password-sharing SaaS founder | 2 | 0.370 | 0.020 | 0.243 | 0.092 | 0.182 | 0.181 | O |
| Patient who received incorrect blood test results | 2 | 0.070 | 0.277 | 0.048 | 0.302 | 0.240 | 0.187 | A |
| Patient with Incorrect Results | 2 | 0.030 | 0.161 | 0.028 | 0.209 | 0.311 | 0.148 | N |
| Patient with Misdiagnosis | 2 | 0.070 | 0.056 | 0.121 | 0.247 | 0.285 | 0.156 | N |
| Payroll Provider Account Manager | 2 | 0.030 | 0.165 | 0.174 | 0.010 | 0.199 | 0.116 | N |
| Pediatrician who identified lead poisoning in children | 2 | 0.370 | 0.332 | 0.110 | 0.202 | 0.196 | 0.242 | O |
| Pediatrician who identified lead poisoning spikes | 2 | 0.370 | 0.405 | 0.068 | 0.203 | 0.198 | 0.249 | C |
| Pediatrician who published research on spiking lead levels in children | 2 | 0.370 | 0.455 | 0.048 | 0.215 | 0.190 | 0.256 | C |
| Peloton CFO | 2 | 0.170 | 0.393 | 0.042 | 0.192 | 0.102 | 0.180 | C |
| Peloton community moderator | 2 | 0.050 | 0.166 | 0.242 | 0.208 | 0.020 | 0.137 | E |
| Peloton fitness instructor | 4 | 0.220 | 0.023 | 0.277 | 0.151 | 0.158 | 0.166 | E |
| Peloton hardware engineer | 2 | 0.370 | 0.193 | 0.052 | 0.006 | 0.098 | 0.144 | O |
| Peloton head instructor | 2 | 0.220 | 0.093 | 0.286 | 0.008 | 0.198 | 0.161 | E |
| Peloton warehouse manager | 2 | 0.030 | 0.068 | 0.033 | 0.004 | 0.215 | 0.070 | N |
| Physician Who Ordered Tests | 2 | 0.070 | 0.237 | 0.114 | 0.293 | 0.100 | 0.163 | A |
| Pilots' Union Safety Chair | 2 | 0.170 | 0.414 | 0.019 | 0.165 | 0.095 | 0.172 | C |
| Player Community Moderator | 2 | 0.120 | 0.140 | 0.251 | 0.398 | 0.331 | 0.248 | A |
| Post Office audit director | 4 | 0.230 | 0.412 | 0.142 | 0.211 | 0.196 | 0.238 | C |
| Post Office internal auditor | 2 | 0.030 | 0.336 | 0.168 | 0.133 | 0.010 | 0.135 | C |
| Post Office prosecuting lawyer | 2 | 0.130 | 0.200 | 0.162 | 0.309 | 0.003 | 0.161 | A |
| Professional gaming league organizer | 2 | 0.070 | 0.440 | 0.216 | 0.193 | 0.100 | 0.204 | C |
| Property agent | 2 | 0.120 | 0.057 | 0.329 | 0.169 | 0.026 | 0.140 | E |
| Property owner facing tenant default | 2 | 0.080 | 0.202 | 0.102 | 0.322 | 0.002 | 0.142 | A |
| Public Health Researcher | 2 | 0.270 | 0.134 | 0.171 | 0.171 | 0.085 | 0.166 | O |
| Regional Airline CEO | 2 | 0.180 | 0.211 | 0.153 | 0.109 | 0.295 | 0.189 | N |
| Regional HR Director | 2 | 0.030 | 0.230 | 0.115 | 0.296 | 0.122 | 0.159 | A |
| Remote Work Advocate | 2 | 0.470 | 0.177 | 0.068 | 0.311 | 0.298 | 0.265 | O |
| Renewables Lobbyist | 2 | 0.220 | 0.024 | 0.262 | 0.192 | 0.311 | 0.202 | N |
| Reporter investigating governance failures | 2 | 0.470 | 0.127 | 0.112 | 0.194 | 0.098 | 0.200 | O |
| Retail crypto trader who lost life savings in FTX yield program | 2 | 0.230 | 0.056 | 0.126 | 0.016 | 0.283 | 0.142 | N |
| Retail crypto trader who lost life savings in FTX's yield program | 2 | 0.170 | 0.175 | 0.088 | 0.077 | 0.300 | 0.162 | N |
| Retail crypto trader with locked savings | 2 | 0.130 | 0.174 | 0.033 | 0.095 | 0.305 | 0.147 | N |
| Risk analyst adjusting premiums for MAX operations | 2 | 0.070 | 0.269 | 0.042 | 0.201 | 0.100 | 0.136 | C |
| Rural council member | 2 | 0.050 | 0.100 | 0.215 | 0.097 | 0.197 | 0.132 | E |
| Rural factory owner | 4 | 0.230 | 0.329 | 0.102 | 0.188 | 0.086 | 0.187 | C |
| Rural factory owner dependent on program labor | 2 | 0.230 | 0.359 | 0.043 | 0.189 | 0.065 | 0.177 | C |
| SFPD liaison | 2 | 0.130 | 0.273 | 0.176 | 0.095 | 0.011 | 0.137 | C |
| SVB Board Member | 2 | 0.120 | 0.106 | 0.282 | 0.288 | 0.001 | 0.160 | A |
| SVB Commercial Banker | 4 | 0.070 | 0.379 | 0.059 | 0.100 | 0.249 | 0.171 | C |
| SVB Senior Commercial Banker | 2 | 0.030 | 0.361 | 0.041 | 0.083 | 0.200 | 0.143 | C |
| SVB Treasury Manager | 2 | 0.030 | 0.241 | 0.061 | 0.012 | 0.101 | 0.089 | C |
| SVB Treasury Risk Officer | 2 | 0.030 | 0.190 | 0.049 | 0.036 | 0.100 | 0.081 | C |
| SaaS Founder (Bootstrapped) | 2 | 0.270 | 0.138 | 0.127 | 0.071 | 0.193 | 0.160 | O |
| Safety advocate pushing for rigorous retraining | 2 | 0.120 | 0.445 | 0.021 | 0.211 | 0.100 | 0.179 | C |
| Seed-stage biotech CEO with 85 employees | 2 | 0.370 | 0.181 | 0.082 | 0.065 | 0.200 | 0.180 | O |
| Senior Centrelink manager overseeing the scheme | 2 | 0.030 | 0.333 | 0.136 | 0.310 | 0.000 | 0.162 | C |
| Senior Lab Technician at Theranos | 2 | 0.370 | 0.456 | 0.167 | 0.203 | 0.110 | 0.261 | C |
| Shift Supervisor (undecided) | 2 | 0.130 | 0.081 | 0.071 | 0.182 | 0.067 | 0.106 | A |
| Shrine Keeper | 2 | 0.230 | 0.251 | 0.186 | 0.358 | 0.089 | 0.223 | A |
| Single parent issued an incorrect $12K debt notice | 2 | 0.130 | 0.005 | 0.116 | 0.121 | 0.200 | 0.115 | N |
| Single parent sharing Netflix account with ex-spouse | 2 | 0.130 | 0.200 | 0.019 | 0.319 | 0.100 | 0.153 | A |
| Single parent sharing Netflix account with ex-spouse for children's access | 2 | 0.130 | 0.142 | 0.040 | 0.267 | 0.100 | 0.136 | A |
| Single parent sharing account with ex-spouse | 2 | 0.180 | 0.229 | 0.050 | 0.314 | 0.073 | 0.169 | A |
| Single parent with $12K incorrect debt notice | 2 | 0.130 | 0.142 | 0.086 | 0.212 | 0.293 | 0.173 | N |
| Single parent wrongly issued $12K debt notice | 2 | 0.130 | 0.261 | 0.117 | 0.170 | 0.290 | 0.194 | N |
| Single-mom DoorDash driver | 4 | 0.065 | 0.119 | 0.063 | 0.157 | 0.189 | 0.119 | N |
| Single-mom DoorDash driver needing schedule flexibility for childcare | 2 | 0.130 | 0.101 | 0.002 | 0.085 | 0.250 | 0.114 | N |
| Small Business Owner Subletter | 2 | 0.220 | 0.133 | 0.087 | 0.014 | 0.050 | 0.101 | O |
| Small business owner (congestion zone) | 2 | 0.080 | 0.191 | 0.234 | 0.125 | 0.330 | 0.192 | N |
| Small business owner (convenience store) facing 60% foot traffic decline | 2 | 0.180 | 0.262 | 0.081 | 0.087 | 0.198 | 0.162 | C |
| Small business owner (retail) | 2 | 0.130 | 0.172 | 0.098 | 0.078 | 0.011 | 0.098 | C |
| Small business owner whose storefront foot traffic dropped 60% due to nearby encampments | 2 | 0.130 | 0.186 | 0.060 | 0.035 | 0.110 | 0.104 | C |
| Small game studio founder | 2 | 0.320 | 0.022 | 0.073 | 0.111 | 0.200 | 0.145 | O |
| Small restaurant owner | 4 | 0.030 | 0.286 | 0.145 | 0.066 | 0.052 | 0.116 | C |
| Social Services Minister | 2 | 0.030 | 0.242 | 0.413 | 0.154 | 0.104 | 0.189 | E |
| Social worker at community legal center | 2 | 0.370 | 0.161 | 0.121 | 0.380 | 0.095 | 0.225 | A |
| Social worker counseling affected clients | 2 | 0.120 | 0.077 | 0.116 | 0.302 | 0.200 | 0.163 | A |
| SoftBank Investment Committee Member | 4 | 0.070 | 0.305 | 0.127 | 0.192 | 0.297 | 0.198 | C |
| South Korean recruiter | 2 | 0.170 | 0.053 | 0.369 | 0.199 | 0.100 | 0.178 | E |
| Startup CEO with frozen payroll | 2 | 0.370 | 0.159 | 0.093 | 0.073 | 0.190 | 0.177 | O |
| Startup CEO with frozen payroll funds | 2 | 0.370 | 0.063 | 0.168 | 0.092 | 0.200 | 0.179 | O |
| Startup CFO | 2 | 0.050 | 0.343 | 0.097 | 0.093 | 0.301 | 0.177 | C |
| State Budget Analyst | 2 | 0.030 | 0.206 | 0.061 | 0.104 | 0.203 | 0.121 | C |
| State Health Department Official | 2 | 0.130 | 0.278 | 0.069 | 0.004 | 0.302 | 0.157 | N |
| State budget analyst | 2 | 0.130 | 0.205 | 0.021 | 0.098 | 0.104 | 0.112 | C |
| State governor | 2 | 0.030 | 0.054 | 0.230 | 0.204 | 0.204 | 0.145 | E |
| State health director | 2 | 0.220 | 0.175 | 0.038 | 0.009 | 0.260 | 0.140 | N |
| State legislator | 2 | 0.030 | 0.322 | 0.232 | 0.008 | 0.200 | 0.158 | C |
| Store Manager (10-year veteran) | 2 | 0.070 | 0.375 | 0.116 | 0.193 | 0.200 | 0.191 | C |
| Store manager torn between corporate and staff | 2 | 0.030 | 0.191 | 0.104 | 0.177 | 0.087 | 0.118 | C |
| Store manager torn between corporate anti-union directives and loyalty to staff | 2 | 0.130 | 0.148 | 0.087 | 0.250 | 0.200 | 0.163 | A |
| Street outreach worker | 2 | 0.320 | 0.029 | 0.136 | 0.405 | 0.211 | 0.220 | A |
| Street outreach worker with deep client trust relationships | 2 | 0.070 | 0.075 | 0.231 | 0.394 | 0.227 | 0.199 | A |
| Street outreach worker with years of trust relationships among unhoused clients | 2 | 0.120 | 0.028 | 0.082 | 0.360 | 0.250 | 0.168 | A |
| Sublessor dependent on WeWork infrastructure | 2 | 0.320 | 0.171 | 0.018 | 0.002 | 0.202 | 0.143 | O |
| TEPCO Safety Engineer | 6 | 0.063 | 0.419 | 0.026 | 0.180 | 0.289 | 0.195 | C |
| Taiwanese factory line supervisor | 6 | 0.147 | 0.229 | 0.038 | 0.091 | 0.061 | 0.113 | C |
| Teams Talent Scout | 2 | 0.270 | 0.133 | 0.408 | 0.175 | 0.290 | 0.255 | E |
| Teamsters Local 814 Secretary-Treasurer | 2 | 0.070 | 0.117 | 0.157 | 0.287 | 0.089 | 0.144 | A |
| Tech Journalist | 2 | 0.470 | 0.035 | 0.096 | 0.307 | 0.001 | 0.182 | O |
| Tech executive | 2 | 0.030 | 0.421 | 0.064 | 0.195 | 0.289 | 0.200 | C |
| Tech industry lobbyist | 2 | 0.180 | 0.222 | 0.277 | 0.194 | 0.300 | 0.235 | N |
| Tech journalist investigating Robodebt | 2 | 0.470 | 0.342 | 0.102 | 0.004 | 0.096 | 0.203 | O |
| Theranos Board Member | 2 | 0.080 | 0.188 | 0.301 | 0.196 | 0.011 | 0.155 | E |
| Theranos Lab Technician | 2 | 0.220 | 0.239 | 0.168 | 0.115 | 0.022 | 0.153 | C |
| Theranos Legal Counsel | 4 | 0.180 | 0.221 | 0.140 | 0.265 | 0.163 | 0.194 | A |
| Theranos Quality Assurance Lead | 2 | 0.270 | 0.363 | 0.029 | 0.093 | 0.189 | 0.189 | C |
| Third-Party Union Buster Consultant | 2 | 0.130 | 0.305 | 0.209 | 0.302 | 0.078 | 0.205 | C |
| Trapped elderly owner | 2 | 0.280 | 0.265 | 0.121 | 0.167 | 0.220 | 0.211 | O |
| URA urban planner | 2 | 0.220 | 0.445 | 0.050 | 0.031 | 0.348 | 0.219 | C |
| US Congressional representative investigating crypto regulation | 2 | 0.170 | 0.035 | 0.294 | 0.089 | 0.194 | 0.157 | E |
| Uber executive | 2 | 0.070 | 0.373 | 0.329 | 0.100 | 0.278 | 0.230 | C |
| Uber/Lyft Driver Association Leader | 2 | 0.120 | 0.207 | 0.258 | 0.009 | 0.189 | 0.157 | E |
| Union rep for postal workers | 2 | 0.120 | 0.100 | 0.333 | 0.011 | 0.297 | 0.172 | E |
| Urban planner | 2 | 0.220 | 0.384 | 0.144 | 0.114 | 0.281 | 0.229 | C |
| VC General Partner | 4 | 0.270 | 0.043 | 0.206 | 0.176 | 0.349 | 0.209 | N |
| VC Investor (Tech Portfolio) | 2 | 0.170 | 0.038 | 0.214 | 0.199 | 0.071 | 0.138 | E |
| Victim Family Representative | 2 | 0.270 | 0.121 | 0.139 | 0.277 | 0.305 | 0.223 | N |
| Victim's daughter | 2 | 0.270 | 0.176 | 0.344 | 0.302 | 0.003 | 0.219 | E |
| Vietnamese Embassy liaison | 2 | 0.070 | 0.329 | 0.126 | 0.246 | 0.300 | 0.214 | C |
| Vietnamese technical intern (former) | 2 | 0.130 | 0.258 | 0.063 | 0.007 | 0.290 | 0.150 | N |
| Vietnamese technical intern with wage theft experience | 2 | 0.130 | 0.101 | 0.091 | 0.007 | 0.060 | 0.078 | O |
| Vietnamese trainee (wage theft victim) | 2 | 0.130 | 0.155 | 0.105 | 0.090 | 0.233 | 0.143 | N |
| Village council chair | 2 | 0.170 | 0.204 | 0.188 | 0.398 | 0.220 | 0.236 | A |
| Walgreens Partnership Manager | 4 | 0.125 | 0.214 | 0.334 | 0.063 | 0.162 | 0.179 | E |
| Warehouse logistics manager | 2 | 0.030 | 0.168 | 0.054 | 0.086 | 0.098 | 0.087 | C |
| Water Treatment Plant Operator | 2 | 0.070 | 0.305 | 0.169 | 0.090 | 0.090 | 0.145 | C |
| Water Treatment Plant Supervisor | 2 | 0.050 | 0.157 | 0.122 | 0.115 | 0.210 | 0.131 | N |
| Water treatment plant supervisor | 2 | 0.070 | 0.232 | 0.045 | 0.102 | 0.004 | 0.091 | C |
| WeWork Community Manager | 2 | 0.170 | 0.072 | 0.297 | 0.300 | 0.100 | 0.188 | A |
| WeWork Interim Legal Counsel | 2 | 0.030 | 0.249 | 0.137 | 0.100 | 0.175 | 0.138 | C |
| Xbox Platform Strategist | 2 | 0.120 | 0.209 | 0.301 | 0.091 | 0.031 | 0.150 | E |
| Young couple awaiting BTO flat | 2 | 0.170 | 0.284 | 0.069 | 0.125 | 0.350 | 0.200 | N |
| Young professional awaiting BTO flat | 2 | 0.220 | 0.249 | 0.047 | 0.079 | 0.073 | 0.134 | C |
| Young professional waiting for BTO | 2 | 0.100 | 0.259 | 0.109 | 0.021 | 0.186 | 0.135 | C |
| Zoom Engineering Manager | 2 | 0.070 | 0.267 | 0.039 | 0.118 | 0.190 | 0.137 | C |

## Scenario Difficulty vs Drift

| Scenario | Difficulty | Engine Drift | Naive Drift | Delta |
|----------|-----------|-------------|-------------|-------|
| 10actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.76 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.68 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.68 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.68 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.57 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.57 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.57 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.68 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.68 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.68 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.82 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.82 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.82 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.91 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.91 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.91 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.91 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.91 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.91 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.48 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.48 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.48 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.82 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.82 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.82 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.59 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.85 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.85 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.85 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 1.00 | 0.0000 | 0.0000 | +0.0000 |
| 10actor | 0.66 | 0.0000 | 0.0000 | +0.0000 |
| 3actor | 0.66 | 0.0000 | 0.0000 | +0.0000 |
| 5actor | 0.66 | 0.0000 | 0.0000 | +0.0000 |

## Actor Count x Condition Scaling

| Actors | Condition | n | Drift | Envelope | Convergence | Diversity | Coherence | Repetition | Topic Drift |
|--------|-----------|---|-------|----------|-------------|-----------|-----------|------------|-------------|
| 3 | engine_structural | 40 | 0.1718 | 2.0500 | 0.6937 | 0.6017 | 0.1142 | 0.0000 | 0.4727 |
| 5 | engine_structural | 40 | 0.1684 | 2.0000 | 0.6875 | 0.5417 | 0.1030 | 0.0000 | 0.5054 |
| 10 | engine_structural | 40 | 0.1696 | 2.2100 | 0.8100 | 0.3478 | 0.1009 | 0.0000 | 0.5830 |

### Drift Slope (10-actor minus 3-actor):

- engine_structural: -0.0023
