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
- Persona drift MAE: 0.1700 (+/- 0.0173)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1637, C 0.2208, E 0.1291, A 0.1652, N 0.1712
- Relationship inconsistency: 0.0914
- Relationship shift rate: 0.2931
- Relationship overshoot rate: 0.2192
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0731
- Clean envelope violations: 2.0731
- Structured action validity: 0.5921
- Owner resolution rate: 0.9167
- Executed action contradiction: 0.0000
- State transition coherence: 0.9167
- Action feedback utilization: 0.2583
- Action-plan alignment: 0.9680
- Planned action coverage: 0.9219
- Action family convergence: 0.7197
- Role action diversity: 0.5031
- Negotiation uniqueness: 0.2873
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1057
- Repetition rate: 0.0021
- Topic drift rate: 0.5080
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1669, 0.1731]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.7878, diversity=0.3743
  - TENSION: drift=0.1742, convergence=0.7128, diversity=0.4597
  - NEGOTIATION: drift=0.1733, convergence=0.6200, diversity=0.4961
  - CLOSING: drift=0.1816, convergence=0.6250, diversity=0.5646

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### naive
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1793 (+/- 0.0181)
- Clean persona drift MAE: 0.1793
- Per-trait absolute error: O 0.1829, C 0.2255, E 0.1483, A 0.1712, N 0.1686
- Relationship inconsistency: 0.0882
- Relationship shift rate: 0.3232
- Relationship overshoot rate: 0.2288
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2586
- Clean envelope violations: 2.2586
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0807
- Repetition rate: 0.0000
- Topic drift rate: 0.5450
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.176, 0.1825]

- Phase-level quality:
  - OPENING: drift=0.1819, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1795, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1797, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1858, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### naive_informed
- Runs: 120
- Clean runs: 120
- Contaminated runs: 0
- Persona drift MAE: 0.1725 (+/- 0.0159)
- Clean persona drift MAE: 0.1725
- Per-trait absolute error: O 0.1722, C 0.2232, E 0.1312, A 0.1660, N 0.1699
- Relationship inconsistency: 0.1132
- Relationship shift rate: 0.3105
- Relationship overshoot rate: 0.2282
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1561
- Clean envelope violations: 2.1561
- Structured action validity: 0.5921
- Owner resolution rate: 0.9167
- Executed action contradiction: 0.0000
- State transition coherence: 0.9167
- Action feedback utilization: 0.2667
- Action-plan alignment: 0.9679
- Planned action coverage: 0.9219
- Action family convergence: 0.7197
- Role action diversity: 0.4971
- Negotiation uniqueness: 0.2871
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0931
- Repetition rate: 0.0044
- Topic drift rate: 0.5380
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1697, 0.1754]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.7711, diversity=0.3660
  - TENSION: drift=0.1751, convergence=0.7128, diversity=0.4597
  - NEGOTIATION: drift=0.1750, convergence=0.6450, diversity=0.5072
  - CLOSING: drift=0.1823, convergence=0.6250, diversity=0.5674

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate


## Script-Level Summary
### australia_robodebt_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1790 (+/- 0.0006)
- Clean persona drift MAE: 0.1790
- Per-trait absolute error: O 0.1790, C 0.2414, E 0.1328, A 0.2147, N 0.1274
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3267
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0995
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1783, 0.1798]

- Phase-level quality:
  - OPENING: drift=0.1842, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1760, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1966, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1700, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1905 (+/- 0.0061)
- Clean persona drift MAE: 0.1905
- Per-trait absolute error: O 0.1740, C 0.2472, E 0.1636, A 0.2354, N 0.1322
- Relationship inconsistency: 0.4500
- Relationship shift rate: 0.4285
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
- Dialogue coherence: 0.0650
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.182, 0.199]

- Phase-level quality:
  - OPENING: drift=0.1914, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1904, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2081, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1677, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1826 (+/- 0.0006)
- Clean persona drift MAE: 0.1826
- Per-trait absolute error: O 0.1740, C 0.2400, E 0.1432, A 0.2233, N 0.1327
- Relationship inconsistency: 0.1032
- Relationship shift rate: 0.2711
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0783
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1817, 0.1836]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1821, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1938, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1694, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1856 (+/- 0.0014)
- Clean persona drift MAE: 0.1856
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1247, A 0.2333, N 0.1467
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2800
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
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1035
- Repetition rate: 0.0625
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1838, 0.1875]

- Phase-level quality:
  - OPENING: drift=0.1843, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1820, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### australia_robodebt_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0041)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1686, A 0.2333, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2200
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0717
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1833, 0.1947]

- Phase-level quality:
  - OPENING: drift=0.1841, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1927, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2031, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1804 (+/- 0.0025)
- Clean persona drift MAE: 0.1804
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1122, A 0.2333, N 0.1333
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.3709
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0854
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1769, 0.184]

- Phase-level quality:
  - OPENING: drift=0.1771, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1839, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1885, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1522 (+/- 0.0019)
- Clean persona drift MAE: 0.1522
- Per-trait absolute error: O 0.1640, C 0.1866, E 0.1164, A 0.1990, N 0.0950
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4071
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
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.1742
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0944
- Repetition rate: 0.0000
- Topic drift rate: 0.2143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1496, 0.1547]

- Phase-level quality:
  - OPENING: drift=0.1510, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1470, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1318, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1970, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### australia_robodebt_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1478 (+/- 0.0050)
- Clean persona drift MAE: 0.1478
- Per-trait absolute error: O 0.1500, C 0.1976, E 0.1015, A 0.1900, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3667
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
- Dialogue coherence: 0.0603
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1409, 0.1547]

- Phase-level quality:
  - OPENING: drift=0.1577, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1439, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1311, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2025, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### australia_robodebt_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1487 (+/- 0.0021)
- Clean persona drift MAE: 0.1487
- Per-trait absolute error: O 0.1540, C 0.1866, E 0.1116, A 0.1995, N 0.0920
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4905
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.2000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0839
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1458, 0.1517]

- Phase-level quality:
  - OPENING: drift=0.1520, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1471, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1324, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1960, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1579 (+/- 0.0019)
- Clean persona drift MAE: 0.1579
- Per-trait absolute error: O 0.1830, C 0.2500, E 0.1141, A 0.1450, N 0.0978
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
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1074
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1552, 0.1607]

- Phase-level quality:
  - OPENING: drift=0.1498, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1638, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1592, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1644, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1616 (+/- 0.0026)
- Clean persona drift MAE: 0.1616
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1260, A 0.1512, N 0.1029
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
- Dialogue coherence: 0.0955
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.158, 0.1652]

- Phase-level quality:
  - OPENING: drift=0.1567, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1707, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1542, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1631, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1555 (+/- 0.0020)
- Clean persona drift MAE: 0.1555
- Per-trait absolute error: O 0.1830, C 0.2500, E 0.0993, A 0.1449, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
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
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1100
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1527, 0.1582]

- Phase-level quality:
  - OPENING: drift=0.1488, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1608, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1543, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1638, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1639 (+/- 0.0037)
- Clean persona drift MAE: 0.1639
- Per-trait absolute error: O 0.1167, C 0.3000, E 0.0832, A 0.1533, N 0.1667
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
- Dialogue coherence: 0.1226
- Repetition rate: 0.0625
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1588, 0.1691]

- Phase-level quality:
  - OPENING: drift=0.1638, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1693, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1688, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1938, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### boeing_737max_return_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1701 (+/- 0.0003)
- Clean persona drift MAE: 0.1701
- Per-trait absolute error: O 0.1233, C 0.3000, E 0.1057, A 0.1517, N 0.1700
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
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0860
- Repetition rate: 0.0000
- Topic drift rate: 0.1363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1698, 0.1705]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1815, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1946, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1727 (+/- 0.0071)
- Clean persona drift MAE: 0.1727
- Per-trait absolute error: O 0.1400, C 0.3000, E 0.0789, A 0.1784, N 0.1667
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
- Dialogue coherence: 0.1154
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.163, 0.1825]

- Phase-level quality:
  - OPENING: drift=0.1691, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1690, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1698, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1890, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1744 (+/- 0.0035)
- Clean persona drift MAE: 0.1744
- Per-trait absolute error: O 0.1500, C 0.2620, E 0.1003, A 0.1775, N 0.1820
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2190
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1046
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1695, 0.1793]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1563, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1855, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1810, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0005)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1300, C 0.2600, E 0.0948, A 0.1610, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2713
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
- Dialogue coherence: 0.0690
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1645, 0.1659]

- Phase-level quality:
  - OPENING: drift=0.1834, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1573, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1739, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1810, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### boeing_737max_return_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1724 (+/- 0.0015)
- Clean persona drift MAE: 0.1724
- Per-trait absolute error: O 0.1440, C 0.2600, E 0.0906, A 0.1835, N 0.1840
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2907
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0985
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1703, 0.1745]

- Phase-level quality:
  - OPENING: drift=0.1910, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1589, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1733, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1880, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1601 (+/- 0.0012)
- Clean persona drift MAE: 0.1601
- Per-trait absolute error: O 0.1130, C 0.1733, E 0.1538, A 0.1602, N 0.2000
- Relationship inconsistency: 0.1467
- Relationship shift rate: 0.2958
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Dialogue coherence: 0.1456
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1584, 0.1618]

- Phase-level quality:
  - OPENING: drift=0.1545, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1673, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1637, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1518, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### california_ab5_gig_classification_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1696 (+/- 0.0010)
- Clean persona drift MAE: 0.1696
- Per-trait absolute error: O 0.1250, C 0.1978, E 0.1568, A 0.1686, N 0.2000
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.3156
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
- Dialogue coherence: 0.1291
- Repetition rate: 0.0000
- Topic drift rate: 0.2046
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1682, 0.1711]

- Phase-level quality:
  - OPENING: drift=0.1637, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1773, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1662, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1638, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1605 (+/- 0.0007)
- Clean persona drift MAE: 0.1605
- Per-trait absolute error: O 0.1180, C 0.1869, E 0.1525, A 0.1452, N 0.2000
- Relationship inconsistency: 0.3790
- Relationship shift rate: 0.3661
- Relationship overshoot rate: 0.4929
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
- Dialogue coherence: 0.1230
- Repetition rate: 0.0416
- Topic drift rate: 0.2954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1596, 0.1615]

- Phase-level quality:
  - OPENING: drift=0.1589, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1689, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1610, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1547, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### california_ab5_gig_classification_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1520 (+/- 0.0015)
- Clean persona drift MAE: 0.1520
- Per-trait absolute error: O 0.1734, C 0.2000, E 0.0862, A 0.1333, N 0.1667
- Relationship inconsistency: 0.4152
- Relationship shift rate: 0.3913
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
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1305
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1499, 0.154]

- Phase-level quality:
  - OPENING: drift=0.1551, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1532, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1507, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1836, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1656 (+/- 0.0008)
- Clean persona drift MAE: 0.1656
- Per-trait absolute error: O 0.2067, C 0.2147, E 0.1017, A 0.1383, N 0.1667
- Relationship inconsistency: 0.2798
- Relationship shift rate: 0.4017
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
- Dialogue coherence: 0.1116
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1645, 0.1667]

- Phase-level quality:
  - OPENING: drift=0.1644, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1627, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1622, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1842, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1555 (+/- 0.0008)
- Clean persona drift MAE: 0.1555
- Per-trait absolute error: O 0.1567, C 0.2000, E 0.0857, A 0.1416, N 0.1933
- Relationship inconsistency: 0.5000
- Relationship shift rate: 0.3160
- Relationship overshoot rate: 0.3000
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
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1437
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1544, 0.1565]

- Phase-level quality:
  - OPENING: drift=0.1504, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1565, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1646, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1821, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1459 (+/- 0.0033)
- Clean persona drift MAE: 0.1459
- Per-trait absolute error: O 0.1180, C 0.2000, E 0.1257, A 0.1380, N 0.1480
- Relationship inconsistency: 0.0011
- Relationship shift rate: 0.2452
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 0.8000
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
- Dialogue coherence: 0.1162
- Repetition rate: 0.0000
- Topic drift rate: 0.9643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1413, 0.1505]

- Phase-level quality:
  - OPENING: drift=0.1419, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1525, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1586, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1565, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1644 (+/- 0.0021)
- Clean persona drift MAE: 0.1644
- Per-trait absolute error: O 0.1720, C 0.2022, E 0.1775, A 0.1235, N 0.1470
- Relationship inconsistency: 0.6380
- Relationship shift rate: 0.4311
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.0792
- Repetition rate: 0.0000
- Topic drift rate: 0.9643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1615, 0.1674]

- Phase-level quality:
  - OPENING: drift=0.1528, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1537, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1768, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1646, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### california_ab5_gig_classification_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1513 (+/- 0.0006)
- Clean persona drift MAE: 0.1513
- Per-trait absolute error: O 0.1180, C 0.2110, E 0.1387, A 0.1460, N 0.1430
- Relationship inconsistency: 0.4495
- Relationship shift rate: 0.3354
- Relationship overshoot rate: 0.4500
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
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1149
- Repetition rate: 0.0000
- Topic drift rate: 1.0000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1506, 0.1521]

- Phase-level quality:
  - OPENING: drift=0.1441, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1530, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1663, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1517, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### eu_gdpr_implementation_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0006)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1750, C 0.2069, E 0.1015, A 0.1525, N 0.1671
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3456
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Dialogue coherence: 0.1068
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1598, 0.1614]

- Phase-level quality:
  - OPENING: drift=0.1657, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1647, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1665, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1749, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1768 (+/- 0.0029)
- Clean persona drift MAE: 0.1768
- Per-trait absolute error: O 0.2030, C 0.2212, E 0.1478, A 0.1494, N 0.1627
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3050
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
- Dialogue coherence: 0.0561
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1728, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1808, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1742, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1758, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1732, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0023)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1760, C 0.2109, E 0.1136, A 0.1453, N 0.1571
- Relationship inconsistency: 0.0460
- Relationship shift rate: 0.3166
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
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
- Dialogue coherence: 0.1142
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1574, 0.1638]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1704, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1578, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1699, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1563 (+/- 0.0009)
- Clean persona drift MAE: 0.1563
- Per-trait absolute error: O 0.1900, C 0.1926, E 0.1190, A 0.1067, N 0.1734
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2260
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1188
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1552, 0.1575]

- Phase-level quality:
  - OPENING: drift=0.1646, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1778, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1612, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1913, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1594 (+/- 0.0014)
- Clean persona drift MAE: 0.1594
- Per-trait absolute error: O 0.1734, C 0.2095, E 0.0941, A 0.1533, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2640
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
- Dialogue coherence: 0.0766
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1575, 0.1613]

- Phase-level quality:
  - OPENING: drift=0.1796, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1634, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1743, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1790, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1517 (+/- 0.0047)
- Clean persona drift MAE: 0.1517
- Per-trait absolute error: O 0.1567, C 0.2040, E 0.1177, A 0.1133, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2575
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.3333
- Clean envelope violations: 1.3333
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0811
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1452, 0.1581]

- Phase-level quality:
  - OPENING: drift=0.1847, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1614, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1617, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1834, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### eu_gdpr_implementation_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1589 (+/- 0.0019)
- Clean persona drift MAE: 0.1589
- Per-trait absolute error: O 0.1780, C 0.2148, E 0.0930, A 0.1565, N 0.1520
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2522
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1179
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1563, 0.1615]

- Phase-level quality:
  - OPENING: drift=0.1790, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1611, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1580, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1819, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1661 (+/- 0.0048)
- Clean persona drift MAE: 0.1661
- Per-trait absolute error: O 0.2280, C 0.2132, E 0.1037, A 0.1475, N 0.1380
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2596
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
- Dialogue coherence: 0.0964
- Repetition rate: 0.0000
- Topic drift rate: 0.2857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1594, 0.1728]

- Phase-level quality:
  - OPENING: drift=0.1809, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1666, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1670, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1645, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### eu_gdpr_implementation_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1517 (+/- 0.0067)
- Clean persona drift MAE: 0.1517
- Per-trait absolute error: O 0.1480, C 0.2121, E 0.0923, A 0.1420, N 0.1640
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3754
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0910
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1424, 0.161]

- Phase-level quality:
  - OPENING: drift=0.1765, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1551, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1608, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1678, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### flint_water_crisis_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1646 (+/- 0.0003)
- Clean persona drift MAE: 0.1646
- Per-trait absolute error: O 0.1970, C 0.1800, E 0.1119, A 0.1738, N 0.1600
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3112
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1175
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1642, 0.1649]

- Phase-level quality:
  - OPENING: drift=0.1604, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1740, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1587, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1760, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### flint_water_crisis_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1699 (+/- 0.0014)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.2020, C 0.1882, E 0.1237, A 0.1758, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2969
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
- Dialogue coherence: 0.0965
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1679, 0.172]

- Phase-level quality:
  - OPENING: drift=0.1656, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1783, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1621, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1808, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1666 (+/- 0.0013)
- Clean persona drift MAE: 0.1666
- Per-trait absolute error: O 0.2020, C 0.1800, E 0.1126, A 0.1785, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3100
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0968
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1648, 0.1684]

- Phase-level quality:
  - OPENING: drift=0.1638, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1751, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1573, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1777, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2047 (+/- 0.0006)
- Clean persona drift MAE: 0.2047
- Per-trait absolute error: O 0.1633, C 0.2333, E 0.1286, A 0.2350, N 0.2633
- Relationship inconsistency: 0.3717
- Relationship shift rate: 0.4082
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1177
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.204, 0.2055]

- Phase-level quality:
  - OPENING: drift=0.2124, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2128, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2248, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1959, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### flint_water_crisis_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2293 (+/- 0.0092)
- Clean persona drift MAE: 0.2293
- Per-trait absolute error: O 0.2367, C 0.2333, E 0.1697, A 0.2733, N 0.2333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.3334
- Clean envelope violations: 3.3334
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
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
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2165, 0.2421]

- Phase-level quality:
  - OPENING: drift=0.2175, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2338, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2278, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2014, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2058 (+/- 0.0022)
- Clean persona drift MAE: 0.2058
- Per-trait absolute error: O 0.2133, C 0.2333, E 0.1306, A 0.2183, N 0.2333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2750
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8334
- Clean envelope violations: 2.8334
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0971
- Repetition rate: 0.0000
- Topic drift rate: 0.9546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2028, 0.2088]

- Phase-level quality:
  - OPENING: drift=0.2155, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2186, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2129, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1855, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1674 (+/- 0.0018)
- Clean persona drift MAE: 0.1674
- Per-trait absolute error: O 0.1540, C 0.2466, E 0.0998, A 0.1570, N 0.1800
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.2431
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
- Role action diversity: 0.3438
- Negotiation uniqueness: 0.1548
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1128
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.165, 0.1699]

- Phase-level quality:
  - OPENING: drift=0.1666, convergence=1.0000, diversity=0.3750
  - TENSION: drift=0.1731, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1830, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1544, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1783 (+/- 0.0033)
- Clean persona drift MAE: 0.1783
- Per-trait absolute error: O 0.1540, C 0.2400, E 0.1374, A 0.1740, N 0.1860
- Relationship inconsistency: 0.1616
- Relationship shift rate: 0.4143
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
- Dialogue coherence: 0.0733
- Repetition rate: 0.0000
- Topic drift rate: 0.2143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1737, 0.1829]

- Phase-level quality:
  - OPENING: drift=0.1796, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1714, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1890, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1617, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### flint_water_crisis_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1658 (+/- 0.0014)
- Clean persona drift MAE: 0.1658
- Per-trait absolute error: O 0.1440, C 0.2422, E 0.1005, A 0.1620, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2563
- Relationship overshoot rate: 0.2250
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
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.1483
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0918
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1639, 0.1676]

- Phase-level quality:
  - OPENING: drift=0.1756, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1735, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1782, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1544, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0002)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1930, C 0.2054, E 0.1029, A 0.1322, N 0.1925
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3086
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
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
- Dialogue coherence: 0.0855
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1649, 0.1655]

- Phase-level quality:
  - OPENING: drift=0.1758, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1625, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1686, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1569, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0004)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.2130, C 0.1976, E 0.1324, A 0.1389, N 0.1922
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3330
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
- Dialogue coherence: 0.0757
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1744, 0.1753]

- Phase-level quality:
  - OPENING: drift=0.1739, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1774, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1795, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1646, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1676 (+/- 0.0010)
- Clean persona drift MAE: 0.1676
- Per-trait absolute error: O 0.2180, C 0.1958, E 0.1047, A 0.1283, N 0.1911
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2742
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
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
- Dialogue coherence: 0.0867
- Repetition rate: 0.0416
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1662, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1721, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1693, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1659, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1636, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### ftx_collapse_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1515 (+/- 0.0054)
- Clean persona drift MAE: 0.1515
- Per-trait absolute error: O 0.1733, C 0.2000, E 0.1511, A 0.1000, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.1875
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0902
- Repetition rate: 0.0000
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.144, 0.159]

- Phase-level quality:
  - OPENING: drift=0.1636, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1673, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1603, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1790, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1735 (+/- 0.0088)
- Clean persona drift MAE: 0.1735
- Per-trait absolute error: O 0.2567, C 0.1835, E 0.1775, A 0.1167, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2325
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
- Dialogue coherence: 0.0615
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1613, 0.1857]

- Phase-level quality:
  - OPENING: drift=0.1639, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1867, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1561, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2025, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0008)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.2400, C 0.2074, E 0.1227, A 0.1000, N 0.1333
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
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1834
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0617
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1596, 0.1617]

- Phase-level quality:
  - OPENING: drift=0.1621, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1671, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1648, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1935, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1834 (+/- 0.0062)
- Clean persona drift MAE: 0.1834
- Per-trait absolute error: O 0.1600, C 0.2062, E 0.1721, A 0.2085, N 0.1700
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
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1161
- Repetition rate: 0.0000
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1748, 0.1919]

- Phase-level quality:
  - OPENING: drift=0.1787, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1998, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.2002, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1790, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1994 (+/- 0.0003)
- Clean persona drift MAE: 0.1994
- Per-trait absolute error: O 0.2340, C 0.2222, E 0.1612, A 0.2195, N 0.1600
- Relationship inconsistency: 0.4500
- Relationship shift rate: 0.6972
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
- Dialogue coherence: 0.0771
- Repetition rate: 0.0000
- Topic drift rate: 0.4285
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.199, 0.1998]

- Phase-level quality:
  - OPENING: drift=0.1946, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2133, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1867, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1955, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ftx_collapse_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2000 (+/- 0.0026)
- Clean persona drift MAE: 0.2000
- Per-trait absolute error: O 0.2340, C 0.2112, E 0.1729, A 0.2175, N 0.1640
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2950
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9000
- Clean envelope violations: 2.9000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0896
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1963, 0.2036]

- Phase-level quality:
  - OPENING: drift=0.1844, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.2109, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.2072, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1866, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1686 (+/- 0.0003)
- Clean persona drift MAE: 0.1686
- Per-trait absolute error: O 0.1590, C 0.2175, E 0.1359, A 0.1367, N 0.1940
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3488
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.4000
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
- Dialogue coherence: 0.0791
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1683, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1533, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1928, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1662, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1884, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1792 (+/- 0.0008)
- Clean persona drift MAE: 0.1792
- Per-trait absolute error: O 0.1690, C 0.2401, E 0.1457, A 0.1475, N 0.1935
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4285
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
- Dialogue coherence: 0.0566
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1781, 0.1802]

- Phase-level quality:
  - OPENING: drift=0.1624, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1901, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1750, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1922, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1770 (+/- 0.0003)
- Clean persona drift MAE: 0.1770
- Per-trait absolute error: O 0.1690, C 0.2329, E 0.1447, A 0.1438, N 0.1945
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2500
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0713
- Repetition rate: 0.0000
- Topic drift rate: 0.7273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1766, 0.1774]

- Phase-level quality:
  - OPENING: drift=0.1588, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1954, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1748, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1935, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### fukushima_nuclear_restart_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1600 (+/- 0.0058)
- Clean persona drift MAE: 0.1600
- Per-trait absolute error: O 0.1233, C 0.2333, E 0.0931, A 0.1300, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3975
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6666
- Clean envelope violations: 1.6666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1085
- Repetition rate: 0.0000
- Topic drift rate: 0.1818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.152, 0.168]

- Phase-level quality:
  - OPENING: drift=0.1653, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1658, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1595, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1820, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### fukushima_nuclear_restart_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1645 (+/- 0.0020)
- Clean persona drift MAE: 0.1645
- Per-trait absolute error: O 0.1567, C 0.2333, E 0.0856, A 0.1467, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0975
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
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1617, 0.1673]

- Phase-level quality:
  - OPENING: drift=0.1649, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1653, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1653, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1901, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1646 (+/- 0.0010)
- Clean persona drift MAE: 0.1646
- Per-trait absolute error: O 0.1267, C 0.2333, E 0.1048, A 0.1384, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0885
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1632, 0.166]

- Phase-level quality:
  - OPENING: drift=0.1602, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1682, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1676, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1909, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0092)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1200, C 0.2156, E 0.1431, A 0.1190, N 0.2280
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2772
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.0839
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1523, 0.178]

- Phase-level quality:
  - OPENING: drift=0.1695, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1885, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1704, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1692, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1877 (+/- 0.0059)
- Clean persona drift MAE: 0.1877
- Per-trait absolute error: O 0.2120, C 0.2084, E 0.1500, A 0.1400, N 0.2280
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3500
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
- Dialogue coherence: 0.0619
- Repetition rate: 0.0000
- Topic drift rate: 0.3215
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1795, 0.1959]

- Phase-level quality:
  - OPENING: drift=0.1840, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1998, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1836, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1703, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### fukushima_nuclear_restart_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1715 (+/- 0.0004)
- Clean persona drift MAE: 0.1715
- Per-trait absolute error: O 0.1580, C 0.2162, E 0.1351, A 0.1245, N 0.2240
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2513
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.0741
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0785
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1709, 0.1722]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1857, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1701, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.1831, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### japan_intern_training_reform_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0004)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1910, C 0.1727, E 0.1290, A 0.1442, N 0.1627
- Relationship inconsistency: 0.2753
- Relationship shift rate: 0.3993
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
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
- Dialogue coherence: 0.0802
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1593, 0.1606]

- Phase-level quality:
  - OPENING: drift=0.1498, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1794, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1633, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1578, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1678 (+/- 0.0050)
- Clean persona drift MAE: 0.1678
- Per-trait absolute error: O 0.2100, C 0.1672, E 0.1484, A 0.1568, N 0.1565
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.5267
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
- Dialogue coherence: 0.0760
- Repetition rate: 0.0000
- Topic drift rate: 0.7727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1608, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1570, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1852, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1692, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1624, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0019)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.2080, C 0.1716, E 0.1380, A 0.1496, N 0.1587
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.4438
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Dialogue coherence: 0.0877
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1624, 0.1679]

- Phase-level quality:
  - OPENING: drift=0.1493, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1835, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1625, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1637, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1853 (+/- 0.0080)
- Clean persona drift MAE: 0.1853
- Per-trait absolute error: O 0.2266, C 0.2333, E 0.0697, A 0.2034, N 0.1934
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4550
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
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.7222
- Negotiation uniqueness: 0.1667
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1742, 0.1964]

- Phase-level quality:
  - OPENING: drift=0.1923, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1884, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1914, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1721, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1862 (+/- 0.0105)
- Clean persona drift MAE: 0.1862
- Per-trait absolute error: O 0.2266, C 0.2333, E 0.0728, A 0.2250, N 0.1734
- Relationship inconsistency: 0.2610
- Relationship shift rate: 0.3950
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
- Dialogue coherence: 0.0684
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1716, 0.2008]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1941, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1820, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1725, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1956 (+/- 0.0023)
- Clean persona drift MAE: 0.1956
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.1047, A 0.1966, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4500
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.5972
- Negotiation uniqueness: 0.1458
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0625
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1925, 0.1988]

- Phase-level quality:
  - OPENING: drift=0.1953, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1940, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.2054, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1650, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate

### japan_intern_training_reform_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1542 (+/- 0.0062)
- Clean persona drift MAE: 0.1542
- Per-trait absolute error: O 0.1780, C 0.2400, E 0.0825, A 0.1005, N 0.1700
- Relationship inconsistency: 0.5620
- Relationship shift rate: 0.4889
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1456, 0.1628]

- Phase-level quality:
  - OPENING: drift=0.1666, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1460, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1542, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2020, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1679 (+/- 0.0100)
- Clean persona drift MAE: 0.1679
- Per-trait absolute error: O 0.1780, C 0.2400, E 0.1008, A 0.1370, N 0.1840
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.5857
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
- Dialogue coherence: 0.0893
- Repetition rate: 0.0000
- Topic drift rate: 0.6786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1542, 0.1817]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1536, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1637, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2020, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### japan_intern_training_reform_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1565 (+/- 0.0008)
- Clean persona drift MAE: 0.1565
- Per-trait absolute error: O 0.1820, C 0.2400, E 0.0614, A 0.1195, N 0.1800
- Relationship inconsistency: 0.3720
- Relationship shift rate: 0.5325
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0940
- Repetition rate: 0.0000
- Topic drift rate: 0.7143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1555, 0.1576]

- Phase-level quality:
  - OPENING: drift=0.1699, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1432, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1547, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1970, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1813 (+/- 0.0019)
- Clean persona drift MAE: 0.1813
- Per-trait absolute error: O 0.1830, C 0.2022, E 0.1472, A 0.2034, N 0.1707
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3301
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0938
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1787, 0.1838]

- Phase-level quality:
  - OPENING: drift=0.1875, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1933, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1740, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.2061, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1946 (+/- 0.0015)
- Clean persona drift MAE: 0.1946
- Per-trait absolute error: O 0.2420, C 0.2086, E 0.1589, A 0.1991, N 0.1643
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2965
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.0669
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1925, 0.1966]

- Phase-level quality:
  - OPENING: drift=0.1968, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2017, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1845, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2082, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1847 (+/- 0.0017)
- Clean persona drift MAE: 0.1847
- Per-trait absolute error: O 0.2200, C 0.1900, E 0.1565, A 0.1935, N 0.1636
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3153
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0893
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1823, 0.1871]

- Phase-level quality:
  - OPENING: drift=0.1918, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1943, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1762, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.2051, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1729 (+/- 0.0010)
- Clean persona drift MAE: 0.1729
- Per-trait absolute error: O 0.1567, C 0.2667, E 0.1096, A 0.1317, N 0.2000
- Relationship inconsistency: 0.1436
- Relationship shift rate: 0.2848
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1348
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1716, 0.1743]

- Phase-level quality:
  - OPENING: drift=0.1704, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1683, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1744, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1953, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### microsoft_activision_merger_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1748 (+/- 0.0077)
- Clean persona drift MAE: 0.1748
- Per-trait absolute error: O 0.1567, C 0.2667, E 0.1270, A 0.1333, N 0.1900
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2400
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
- Dialogue coherence: 0.0812
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.164, 0.1855]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1731, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1807, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1872, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1729 (+/- 0.0033)
- Clean persona drift MAE: 0.1729
- Per-trait absolute error: O 0.1400, C 0.2667, E 0.0978, A 0.1400, N 0.2200
- Relationship inconsistency: 0.4500
- Relationship shift rate: 0.3940
- Relationship overshoot rate: 0.4500
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
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1147
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1682, 0.1775]

- Phase-level quality:
  - OPENING: drift=0.1711, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1673, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1849, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1761, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1532 (+/- 0.0018)
- Clean persona drift MAE: 0.1532
- Per-trait absolute error: O 0.1800, C 0.2000, E 0.0917, A 0.1140, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2925
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0857
- Repetition rate: 0.0000
- Topic drift rate: 0.4642
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1507, 0.1556]

- Phase-level quality:
  - OPENING: drift=0.1722, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1603, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1498, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1786, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1634 (+/- 0.0064)
- Clean persona drift MAE: 0.1634
- Per-trait absolute error: O 0.2040, C 0.2198, E 0.1007, A 0.1155, N 0.1770
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2725
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0713
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1545, 0.1723]

- Phase-level quality:
  - OPENING: drift=0.1777, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1579, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1632, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1978, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### microsoft_activision_merger_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1521 (+/- 0.0016)
- Clean persona drift MAE: 0.1521
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.0981, A 0.1140, N 0.1740
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0631
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1498, 0.1543]

- Phase-level quality:
  - OPENING: drift=0.1643, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1668, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1570, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1802, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### netflix_password_crackdown_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1796 (+/- 0.0018)
- Clean persona drift MAE: 0.1796
- Per-trait absolute error: O 0.2210, C 0.2049, E 0.1507, A 0.1673, N 0.1540
- Relationship inconsistency: 0.2840
- Relationship shift rate: 0.3045
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.5714
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
- Dialogue coherence: 0.1095
- Repetition rate: 0.0000
- Topic drift rate: 0.8636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1771, 0.1821]

- Phase-level quality:
  - OPENING: drift=0.1760, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1923, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1812, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1789, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### netflix_password_crackdown_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1842 (+/- 0.0060)
- Clean persona drift MAE: 0.1842
- Per-trait absolute error: O 0.2480, C 0.2079, E 0.1603, A 0.1569, N 0.1483
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3434
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
- Dialogue coherence: 0.0597
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.176, 0.1925]

- Phase-level quality:
  - OPENING: drift=0.1766, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1934, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1884, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1920, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0026)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.2230, C 0.2010, E 0.1482, A 0.1612, N 0.1552
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2466
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3500
- Clean envelope violations: 2.3500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0902
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1741, 0.1813]

- Phase-level quality:
  - OPENING: drift=0.1712, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1896, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1758, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1907, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2185 (+/- 0.0071)
- Clean persona drift MAE: 0.2185
- Per-trait absolute error: O 0.2167, C 0.2333, E 0.2006, A 0.2450, N 0.1966
- Relationship inconsistency: 0.0008
- Relationship shift rate: 0.1896
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8334
- Clean envelope violations: 2.8334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0811
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2087, 0.2283]

- Phase-level quality:
  - OPENING: drift=0.2056, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2179, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2065, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1734, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2113 (+/- 0.0008)
- Clean persona drift MAE: 0.2113
- Per-trait absolute error: O 0.2100, C 0.2333, E 0.2298, A 0.1833, N 0.2000
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
- Dialogue coherence: 0.0738
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2102, 0.2124]

- Phase-level quality:
  - OPENING: drift=0.2022, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2103, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2036, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1976, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2016 (+/- 0.0004)
- Clean persona drift MAE: 0.2016
- Per-trait absolute error: O 0.2167, C 0.2333, E 0.2000, A 0.2016, N 0.1567
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1882
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7500
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0671
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2012, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.2063, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.2053, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1961, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1734, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1906 (+/- 0.0004)
- Clean persona drift MAE: 0.1906
- Per-trait absolute error: O 0.1880, C 0.2068, E 0.1830, A 0.1735, N 0.2020
- Relationship inconsistency: 0.2000
- Relationship shift rate: 0.4334
- Relationship overshoot rate: 0.5250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0948
- Repetition rate: 0.0000
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.19, 0.1913]

- Phase-level quality:
  - OPENING: drift=0.2111, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1948, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1785, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2452, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2165 (+/- 0.0015)
- Clean persona drift MAE: 0.2165
- Per-trait absolute error: O 0.1920, C 0.2156, E 0.2586, A 0.1950, N 0.2210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3136
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
- Dialogue coherence: 0.0706
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2143, 0.2186]

- Phase-level quality:
  - OPENING: drift=0.2273, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2036, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1910, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### netflix_password_crackdown_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2014 (+/- 0.0020)
- Clean persona drift MAE: 0.2014
- Per-trait absolute error: O 0.2080, C 0.2090, E 0.1892, A 0.1795, N 0.2210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2289
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Clean envelope violations: 3.0000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0834
- Repetition rate: 0.0556
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1986, 0.2042]

- Phase-level quality:
  - OPENING: drift=0.2135, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1940, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1849, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2452, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### nyc_congestion_pricing_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1644 (+/- 0.0031)
- Clean persona drift MAE: 0.1644
- Per-trait absolute error: O 0.1690, C 0.1701, E 0.1408, A 0.1846, N 0.1573
- Relationship inconsistency: 0.0563
- Relationship shift rate: 0.3982
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0921
- Repetition rate: 0.0000
- Topic drift rate: 0.1591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1601, 0.1687]

- Phase-level quality:
  - OPENING: drift=0.1603, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1780, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1619, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1804, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1672 (+/- 0.0019)
- Clean persona drift MAE: 0.1672
- Per-trait absolute error: O 0.1770, C 0.1686, E 0.1595, A 0.1709, N 0.1598
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3750
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
- Dialogue coherence: 0.0831
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1646, 0.1698]

- Phase-level quality:
  - OPENING: drift=0.1659, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1752, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1682, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1797, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### nyc_congestion_pricing_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1673 (+/- 0.0000)
- Clean persona drift MAE: 0.1673
- Per-trait absolute error: O 0.1700, C 0.1744, E 0.1533, A 0.1800, N 0.1592
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4275
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0846
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1673, 0.1674]

- Phase-level quality:
  - OPENING: drift=0.1625, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1797, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1613, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1802, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1657 (+/- 0.0029)
- Clean persona drift MAE: 0.1657
- Per-trait absolute error: O 0.1366, C 0.2000, E 0.1666, A 0.1250, N 0.2000
- Relationship inconsistency: 0.2295
- Relationship shift rate: 0.2783
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9773
- Planned action coverage: 1.0000
- Action family convergence: 0.1250
- Role action diversity: 0.9167
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0965
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1616, 0.1697]

- Phase-level quality:
  - OPENING: drift=0.1647, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1687, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1663, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1520, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1683 (+/- 0.0129)
- Clean persona drift MAE: 0.1683
- Per-trait absolute error: O 0.1167, C 0.2000, E 0.2063, A 0.1183, N 0.2000
- Relationship inconsistency: 0.0710
- Relationship shift rate: 0.3114
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
- Dialogue coherence: 0.1105
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1504, 0.1862]

- Phase-level quality:
  - OPENING: drift=0.1870, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1704, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1699, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1516, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0093)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1333, C 0.2000, E 0.1667, A 0.1267, N 0.2000
- Relationship inconsistency: 0.3072
- Relationship shift rate: 0.3510
- Relationship overshoot rate: 0.5250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.1250
- Role action diversity: 0.9167
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0748
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1524, 0.1783]

- Phase-level quality:
  - OPENING: drift=0.1643, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1613, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1618, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1530, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1396 (+/- 0.0025)
- Clean persona drift MAE: 0.1396
- Per-trait absolute error: O 0.1240, C 0.2800, E 0.1243, A 0.0840, N 0.0860
- Relationship inconsistency: 0.2750
- Relationship shift rate: 0.4125
- Relationship overshoot rate: 0.2250
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
- Action family convergence: 0.4167
- Role action diversity: 0.6875
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0932
- Repetition rate: 0.0000
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1361, 0.1432]

- Phase-level quality:
  - OPENING: drift=0.1432, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1327, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1487, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1432, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1401 (+/- 0.0027)
- Clean persona drift MAE: 0.1401
- Per-trait absolute error: O 0.1060, C 0.2820, E 0.1309, A 0.0925, N 0.0890
- Relationship inconsistency: 0.3235
- Relationship shift rate: 0.3025
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
- Dialogue coherence: 0.0696
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1364, 0.1438]

- Phase-level quality:
  - OPENING: drift=0.1600, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1331, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1492, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1341, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### nyc_congestion_pricing_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1377 (+/- 0.0000)
- Clean persona drift MAE: 0.1377
- Per-trait absolute error: O 0.1240, C 0.2800, E 0.1285, A 0.0740, N 0.0820
- Relationship inconsistency: 0.0916
- Relationship shift rate: 0.2734
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7000
- Clean envelope violations: 1.7000
- Structured action validity: 1.0000
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
- Dialogue coherence: 0.0762
- Repetition rate: 0.0000
- Topic drift rate: 0.5714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1377, 0.1377]

- Phase-level quality:
  - OPENING: drift=0.1467, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1394, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1513, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1278, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: persona_drift_mae, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### peloton_demand_cliff_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1659 (+/- 0.0021)
- Clean persona drift MAE: 0.1659
- Per-trait absolute error: O 0.1700, C 0.2600, E 0.1094, A 0.1197, N 0.1707
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4275
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1154
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1631, 0.1688]

- Phase-level quality:
  - OPENING: drift=0.1718, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1499, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1817, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1646, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0034)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.1820, C 0.2600, E 0.1406, A 0.1200, N 0.1722
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3100
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
- Dialogue coherence: 0.0807
- Repetition rate: 0.0000
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1702, 0.1797]

- Phase-level quality:
  - OPENING: drift=0.1794, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1646, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1823, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1716, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1705 (+/- 0.0001)
- Clean persona drift MAE: 0.1705
- Per-trait absolute error: O 0.1700, C 0.2600, E 0.1242, A 0.1270, N 0.1714
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2735
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0908
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1703, 0.1708]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1545, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1794, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1662, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1714 (+/- 0.0025)
- Clean persona drift MAE: 0.1714
- Per-trait absolute error: O 0.1400, C 0.2480, E 0.1521, A 0.1367, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2385
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3334
- Clean envelope violations: 2.3334
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
- Dialogue coherence: 0.0945
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.168, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1694, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1754, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1809, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1734, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1915 (+/- 0.0108)
- Clean persona drift MAE: 0.1915
- Per-trait absolute error: O 0.1400, C 0.2517, E 0.2009, A 0.1916, N 0.1734
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.3261
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
- Dialogue coherence: 0.1004
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1765, 0.2065]

- Phase-level quality:
  - OPENING: drift=0.1784, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1981, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1965, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1699, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1734 (+/- 0.0030)
- Clean persona drift MAE: 0.1734
- Per-trait absolute error: O 0.1233, C 0.2681, E 0.1418, A 0.1667, N 0.1667
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2379
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.1127
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1691, 0.1776]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1708, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1809, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1668, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### peloton_demand_cliff_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1469 (+/- 0.0000)
- Clean persona drift MAE: 0.1469
- Per-trait absolute error: O 0.1240, C 0.2000, E 0.1183, A 0.1250, N 0.1670
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3203
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Dialogue coherence: 0.1137
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1468, 0.1469]

- Phase-level quality:
  - OPENING: drift=0.1659, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1306, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1462, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1956, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### peloton_demand_cliff_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1623 (+/- 0.0059)
- Clean persona drift MAE: 0.1623
- Per-trait absolute error: O 0.1540, C 0.2044, E 0.1654, A 0.1340, N 0.1540
- Relationship inconsistency: 0.0180
- Relationship shift rate: 0.2487
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0942
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1541, 0.1706]

- Phase-level quality:
  - OPENING: drift=0.1841, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1428, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1613, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1978, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### peloton_demand_cliff_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1492 (+/- 0.0007)
- Clean persona drift MAE: 0.1492
- Per-trait absolute error: O 0.1340, C 0.2044, E 0.1182, A 0.1215, N 0.1680
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3540
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.0965
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1482, 0.1502]

- Phase-level quality:
  - OPENING: drift=0.1676, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1321, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1515, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1940, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1726 (+/- 0.0018)
- Clean persona drift MAE: 0.1726
- Per-trait absolute error: O 0.1570, C 0.2258, E 0.1212, A 0.1800, N 0.1786
- Relationship inconsistency: 0.1313
- Relationship shift rate: 0.2871
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
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8500
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1196
- Repetition rate: 0.0000
- Topic drift rate: 0.5454
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1701, 0.175]

- Phase-level quality:
  - OPENING: drift=0.1788, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1752, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1843, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1527, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1832 (+/- 0.0028)
- Clean persona drift MAE: 0.1832
- Per-trait absolute error: O 0.1940, C 0.2390, E 0.1371, A 0.1739, N 0.1722
- Relationship inconsistency: 0.0360
- Relationship shift rate: 0.2660
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0997
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1793, 0.1872]

- Phase-level quality:
  - OPENING: drift=0.1829, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1797, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1911, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1582, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1733 (+/- 0.0015)
- Clean persona drift MAE: 0.1733
- Per-trait absolute error: O 0.1690, C 0.2298, E 0.1202, A 0.1772, N 0.1700
- Relationship inconsistency: 0.1375
- Relationship shift rate: 0.2818
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
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8500
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1712, 0.1754]

- Phase-level quality:
  - OPENING: drift=0.1794, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1727, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1857, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1604, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1522 (+/- 0.0014)
- Clean persona drift MAE: 0.1522
- Per-trait absolute error: O 0.1233, C 0.2000, E 0.0675, A 0.1700, N 0.2000
- Relationship inconsistency: 0.0015
- Relationship shift rate: 0.2056
- Relationship overshoot rate: 0.0000
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
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1111
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1503, 0.1541]

- Phase-level quality:
  - OPENING: drift=0.1706, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1627, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1631, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1680, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0093)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1667, C 0.2183, E 0.0814, A 0.1733, N 0.1867
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2298
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
- Dialogue coherence: 0.0930
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1524, 0.1782]

- Phase-level quality:
  - OPENING: drift=0.1861, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1687, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1787, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1670, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1569 (+/- 0.0019)
- Clean persona drift MAE: 0.1569
- Per-trait absolute error: O 0.1233, C 0.2000, E 0.0746, A 0.1800, N 0.2067
- Relationship inconsistency: 0.0282
- Relationship shift rate: 0.2449
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6666
- Clean envelope violations: 1.6666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1169
- Repetition rate: 0.0000
- Topic drift rate: 0.1818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1543, 0.1595]

- Phase-level quality:
  - OPENING: drift=0.1737, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1703, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1661, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1700, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1661 (+/- 0.0071)
- Clean persona drift MAE: 0.1661
- Per-trait absolute error: O 0.0900, C 0.2000, E 0.1746, A 0.1760, N 0.1900
- Relationship inconsistency: 0.1807
- Relationship shift rate: 0.2865
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
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1176
- Repetition rate: 0.0000
- Topic drift rate: 0.4642
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1563, 0.1759]

- Phase-level quality:
  - OPENING: drift=0.1745, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1860, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1750, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1496, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1781 (+/- 0.0031)
- Clean persona drift MAE: 0.1781
- Per-trait absolute error: O 0.1440, C 0.2242, E 0.1658, A 0.1725, N 0.1840
- Relationship inconsistency: 0.0750
- Relationship shift rate: 0.2750
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
- Dialogue coherence: 0.0980
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1738, 0.1824]

- Phase-level quality:
  - OPENING: drift=0.1848, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1804, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1839, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1729, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### sf_homelessness_policy_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1633 (+/- 0.0038)
- Clean persona drift MAE: 0.1633
- Per-trait absolute error: O 0.0800, C 0.2088, E 0.1648, A 0.1790, N 0.1840
- Relationship inconsistency: 0.2481
- Relationship shift rate: 0.3515
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
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1026
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.158, 0.1686]

- Phase-level quality:
  - OPENING: drift=0.1804, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1773, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1687, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1490, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1830 (+/- 0.0021)
- Clean persona drift MAE: 0.1830
- Per-trait absolute error: O 0.1310, C 0.2400, E 0.1971, A 0.1922, N 0.1542
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2966
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.2500
- Negotiation uniqueness: 0.0572
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0845
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.18, 0.1859]

- Phase-level quality:
  - OPENING: drift=0.1868, convergence=1.0000, diversity=0.2083
  - TENSION: drift=0.1946, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1765, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1935, convergence=1.0000, diversity=0.2916

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1958 (+/- 0.0028)
- Clean persona drift MAE: 0.1958
- Per-trait absolute error: O 0.1590, C 0.2437, E 0.2264, A 0.1931, N 0.1567
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3255
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
- Dialogue coherence: 0.0972
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1919, 0.1997]

- Phase-level quality:
  - OPENING: drift=0.1985, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1916, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1912, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1990, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1893 (+/- 0.0005)
- Clean persona drift MAE: 0.1893
- Per-trait absolute error: O 0.1480, C 0.2400, E 0.2142, A 0.1951, N 0.1489
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2570
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5500
- Clean envelope violations: 2.5500
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9444
- Planned action coverage: 0.4091
- Action family convergence: 1.0000
- Role action diversity: 0.3166
- Negotiation uniqueness: 0.0572
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1065
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1885, 0.19]

- Phase-level quality:
  - OPENING: drift=0.1873, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1864, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1928, convergence=1.0000, diversity=0.2250
  - CLOSING: drift=0.2006, convergence=0.5000, diversity=0.1250

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2016 (+/- 0.0004)
- Clean persona drift MAE: 0.2016
- Per-trait absolute error: O 0.2100, C 0.2667, E 0.1000, A 0.2183, N 0.2133
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.0867
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
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1073
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2012, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.2016, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1874, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1924, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1997 (+/- 0.0029)
- Clean persona drift MAE: 0.1997
- Per-trait absolute error: O 0.2100, C 0.2667, E 0.1091, A 0.2333, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.0674
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1958, 0.2037]

- Phase-level quality:
  - OPENING: drift=0.2045, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1910, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1940, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2027, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1933 (+/- 0.0000)
- Clean persona drift MAE: 0.1933
- Per-trait absolute error: O 0.1767, C 0.2667, E 0.1000, A 0.2233, N 0.2000
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.1867
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
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0958
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1933, 0.1934]

- Phase-level quality:
  - OPENING: drift=0.1908, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1951, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1950, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1950, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1911 (+/- 0.0019)
- Clean persona drift MAE: 0.1911
- Per-trait absolute error: O 0.1800, C 0.2800, E 0.1515, A 0.1550, N 0.1890
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.2643
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
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1019
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1885, 0.1937]

- Phase-level quality:
  - OPENING: drift=0.1897, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1952, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.2060, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2085, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2079 (+/- 0.0010)
- Clean persona drift MAE: 0.2079
- Per-trait absolute error: O 0.2000, C 0.2800, E 0.1702, A 0.1735, N 0.2160
- Relationship inconsistency: 0.2907
- Relationship shift rate: 0.3968
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.0932
- Repetition rate: 0.0000
- Topic drift rate: 0.4642
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2065, 0.2094]

- Phase-level quality:
  - OPENING: drift=0.2058, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1981, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2093, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2168, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### singapore_hdb_waittime_crisis_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1949 (+/- 0.0001)
- Clean persona drift MAE: 0.1949
- Per-trait absolute error: O 0.1840, C 0.2800, E 0.1721, A 0.1440, N 0.1940
- Relationship inconsistency: 0.0180
- Relationship shift rate: 0.2304
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4000
- Clean envelope violations: 2.4000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0930
- Repetition rate: 0.0000
- Topic drift rate: 0.5714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1946, 0.1951]

- Phase-level quality:
  - OPENING: drift=0.1898, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1925, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.2113, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2228, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1560 (+/- 0.0070)
- Clean persona drift MAE: 0.1560
- Per-trait absolute error: O 0.1740, C 0.1744, E 0.1202, A 0.1789, N 0.1325
- Relationship inconsistency: 0.0936
- Relationship shift rate: 0.3277
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0968
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1463, 0.1657]

- Phase-level quality:
  - OPENING: drift=0.1752, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1502, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1620, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1551, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1670 (+/- 0.0003)
- Clean persona drift MAE: 0.1670
- Per-trait absolute error: O 0.1860, C 0.1973, E 0.1447, A 0.1772, N 0.1298
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.4765
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
- Dialogue coherence: 0.0703
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1666, 0.1674]

- Phase-level quality:
  - OPENING: drift=0.1786, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1567, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1723, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1556, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0000)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1960, C 0.1986, E 0.1263, A 0.1741, N 0.1316
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.6420
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0635
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1653, 0.1653]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1515, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1716, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1557, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: persona_drift_mae, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1343 (+/- 0.0066)
- Clean persona drift MAE: 0.1343
- Per-trait absolute error: O 0.0966, C 0.1000, E 0.1033, A 0.1717, N 0.2000
- Relationship inconsistency: 0.0015
- Relationship shift rate: 0.4437
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
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.5486
- Negotiation uniqueness: 0.1270
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1096
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1252, 0.1434]

- Phase-level quality:
  - OPENING: drift=0.1610, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1579, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1454, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1540, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1588 (+/- 0.0137)
- Clean persona drift MAE: 0.1588
- Per-trait absolute error: O 0.1567, C 0.1000, E 0.1688, A 0.1683, N 0.2000
- Relationship inconsistency: 0.1605
- Relationship shift rate: 0.2830
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
- Dialogue coherence: 0.0870
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1397, 0.1778]

- Phase-level quality:
  - OPENING: drift=0.1623, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1683, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1664, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1640, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### starbucks_unionization_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1532 (+/- 0.0045)
- Clean persona drift MAE: 0.1532
- Per-trait absolute error: O 0.1734, C 0.1000, E 0.1213, A 0.1717, N 0.2000
- Relationship inconsistency: 0.5370
- Relationship shift rate: 0.4676
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
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.4028
- Negotiation uniqueness: 0.1125
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1250
- Repetition rate: 0.0000
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1469, 0.1596]

- Phase-level quality:
  - OPENING: drift=0.1559, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1537, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1583, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1640, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1872 (+/- 0.0000)
- Clean persona drift MAE: 0.1872
- Per-trait absolute error: O 0.1680, C 0.2000, E 0.1450, A 0.2145, N 0.2090
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2556
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.0741
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1044
- Repetition rate: 0.0000
- Topic drift rate: 0.8215
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1872, 0.1873]

- Phase-level quality:
  - OPENING: drift=0.1907, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1806, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1829, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.2215, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1859 (+/- 0.0042)
- Clean persona drift MAE: 0.1859
- Per-trait absolute error: O 0.1780, C 0.2066, E 0.1260, A 0.2180, N 0.2010
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.4693
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
- Dialogue coherence: 0.0777
- Repetition rate: 0.0000
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1801, 0.1917]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1786, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1823, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2371, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### starbucks_unionization_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1825 (+/- 0.0037)
- Clean persona drift MAE: 0.1825
- Per-trait absolute error: O 0.1840, C 0.2000, E 0.1130, A 0.2055, N 0.2100
- Relationship inconsistency: 0.0653
- Relationship shift rate: 0.3388
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3958
- Negotiation uniqueness: 0.0801
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0888
- Repetition rate: 0.0000
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1774, 0.1876]

- Phase-level quality:
  - OPENING: drift=0.1970, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1681, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1815, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.2284, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1595 (+/- 0.0005)
- Clean persona drift MAE: 0.1595
- Per-trait absolute error: O 0.1840, C 0.2021, E 0.1227, A 0.1289, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3096
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8500
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0970
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1589, 0.1602]

- Phase-level quality:
  - OPENING: drift=0.1619, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1681, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1652, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1562, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1649 (+/- 0.0036)
- Clean persona drift MAE: 0.1649
- Per-trait absolute error: O 0.1840, C 0.2210, E 0.1270, A 0.1325, N 0.1600
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.3654
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
- Dialogue coherence: 0.0943
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1599, 0.1699]

- Phase-level quality:
  - OPENING: drift=0.1592, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1777, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1683, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1547, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0047)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1790, C 0.2007, E 0.1285, A 0.1295, N 0.1618
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2632
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.8500
- Role action diversity: 0.3125
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0924
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1534, 0.1664]

- Phase-level quality:
  - OPENING: drift=0.1543, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1705, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1679, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1561, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1482 (+/- 0.0016)
- Clean persona drift MAE: 0.1482
- Per-trait absolute error: O 0.1767, C 0.2450, E 0.0359, A 0.1500, N 0.1333
- Relationship inconsistency: 0.2815
- Relationship shift rate: 0.3648
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
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1268
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.146, 0.1504]

- Phase-level quality:
  - OPENING: drift=0.1605, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1577, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1662, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1645, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1588 (+/- 0.0071)
- Clean persona drift MAE: 0.1588
- Per-trait absolute error: O 0.1767, C 0.2688, E 0.0585, A 0.1567, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3745
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
- Dialogue coherence: 0.0977
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.149, 0.1686]

- Phase-level quality:
  - OPENING: drift=0.1629, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1614, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1725, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1557, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1683 (+/- 0.0045)
- Clean persona drift MAE: 0.1683
- Per-trait absolute error: O 0.1767, C 0.2926, E 0.0802, A 0.1583, N 0.1333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2325
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
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.7083
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0890
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1619, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1601, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1765, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1699, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1774, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1675 (+/- 0.0052)
- Clean persona drift MAE: 0.1675
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1282, A 0.1155, N 0.2200
- Relationship inconsistency: 0.0675
- Relationship shift rate: 0.2341
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1249
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1604, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1884, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1558, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1715, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2045, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0053)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1740, C 0.2042, E 0.1516, A 0.1325, N 0.2200
- Relationship inconsistency: 0.0795
- Relationship shift rate: 0.3385
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
- Dialogue coherence: 0.0893
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1692, 0.1837]

- Phase-level quality:
  - OPENING: drift=0.1992, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1641, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1753, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2031, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### svb_bank_run_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0024)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1700, C 0.2000, E 0.1456, A 0.1145, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2460
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0995
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1667, 0.1733]

- Phase-level quality:
  - OPENING: drift=0.1983, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1533, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1759, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1990, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1720 (+/- 0.0004)
- Clean persona drift MAE: 0.1720
- Per-trait absolute error: O 0.1640, C 0.2600, E 0.1386, A 0.1349, N 0.1629
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3793
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5000
- Action family convergence: 1.0000
- Role action diversity: 0.2750
- Negotiation uniqueness: 0.0606
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1142
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1716, 0.1725]

- Phase-level quality:
  - OPENING: drift=0.1715, convergence=1.0000, diversity=0.3750
  - TENSION: drift=0.1743, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1738, convergence=1.0000, diversity=0.2250
  - CLOSING: drift=0.1725, convergence=1.0000, diversity=0.3333

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1754 (+/- 0.0004)
- Clean persona drift MAE: 0.1754
- Per-trait absolute error: O 0.1680, C 0.2600, E 0.1345, A 0.1445, N 0.1700
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5488
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
- Dialogue coherence: 0.0756
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1748, 0.176]

- Phase-level quality:
  - OPENING: drift=0.1737, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1795, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1734, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1736, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1810 (+/- 0.0001)
- Clean persona drift MAE: 0.1810
- Per-trait absolute error: O 0.1880, C 0.2600, E 0.1499, A 0.1385, N 0.1691
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.6953
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.5000
- Action family convergence: 1.0000
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.0697
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0974
- Repetition rate: 0.0000
- Topic drift rate: 0.4318
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1808, 0.1813]

- Phase-level quality:
  - OPENING: drift=0.1752, convergence=0.5000, diversity=0.1666
  - TENSION: drift=0.1813, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1839, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1733, convergence=1.0000, diversity=0.4166

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1820 (+/- 0.0104)
- Clean persona drift MAE: 0.1820
- Per-trait absolute error: O 0.1200, C 0.3000, E 0.1249, A 0.1650, N 0.2000
- Relationship inconsistency: 0.1376
- Relationship shift rate: 0.2502
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1093
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1676, 0.1964]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1893, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1847, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1966, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1931 (+/- 0.0049)
- Clean persona drift MAE: 0.1931
- Per-trait absolute error: O 0.1533, C 0.3000, E 0.1338, A 0.1783, N 0.2000
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3175
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
- Dialogue coherence: 0.0596
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1863, 0.1999]

- Phase-level quality:
  - OPENING: drift=0.1962, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1992, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1844, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2077, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1788 (+/- 0.0026)
- Clean persona drift MAE: 0.1788
- Per-trait absolute error: O 0.1033, C 0.3000, E 0.1323, A 0.1583, N 0.2000
- Relationship inconsistency: 0.2981
- Relationship shift rate: 0.3599
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.0875
- Repetition rate: 0.0000
- Topic drift rate: 0.2272
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1752, 0.1824]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1880, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1815, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1949, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1885 (+/- 0.0019)
- Clean persona drift MAE: 0.1885
- Per-trait absolute error: O 0.1760, C 0.2022, E 0.1453, A 0.2390, N 0.1800
- Relationship inconsistency: 0.3214
- Relationship shift rate: 0.3931
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.8333
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0798
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1859, 0.1911]

- Phase-level quality:
  - OPENING: drift=0.2021, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1802, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1933, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2100, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1987 (+/- 0.0013)
- Clean persona drift MAE: 0.1987
- Per-trait absolute error: O 0.1860, C 0.2000, E 0.1754, A 0.2520, N 0.1800
- Relationship inconsistency: 0.1310
- Relationship shift rate: 0.6326
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
- Dialogue coherence: 0.0655
- Repetition rate: 0.0000
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1969, 0.2005]

- Phase-level quality:
  - OPENING: drift=0.2000, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1845, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2047, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2100, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### theranos_whistleblower_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1895 (+/- 0.0024)
- Clean persona drift MAE: 0.1895
- Per-trait absolute error: O 0.1860, C 0.2000, E 0.1397, A 0.2455, N 0.1760
- Relationship inconsistency: 0.5350
- Relationship shift rate: 0.6633
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.8333
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0650
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1861, 0.1928]

- Phase-level quality:
  - OPENING: drift=0.1982, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1840, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1958, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2100, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1947 (+/- 0.0016)
- Clean persona drift MAE: 0.1947
- Per-trait absolute error: O 0.1940, C 0.1888, E 0.2090, A 0.2017, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0897
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1925, 0.1969]

- Phase-level quality:
  - OPENING: drift=0.1976, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1974, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1920, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1884, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1969 (+/- 0.0050)
- Clean persona drift MAE: 0.1969
- Per-trait absolute error: O 0.1990, C 0.1873, E 0.2230, A 0.1965, N 0.1789
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4118
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
- Dialogue coherence: 0.0747
- Repetition rate: 0.0000
- Topic drift rate: 0.1819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.19, 0.2038]

- Phase-level quality:
  - OPENING: drift=0.1907, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2075, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1939, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2038, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1927 (+/- 0.0028)
- Clean persona drift MAE: 0.1927
- Per-trait absolute error: O 0.2020, C 0.1815, E 0.2054, A 0.1946, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3980
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0966
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1888, 0.1966]

- Phase-level quality:
  - OPENING: drift=0.1999, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1947, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1906, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1880, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1687 (+/- 0.0026)
- Clean persona drift MAE: 0.1687
- Per-trait absolute error: O 0.1167, C 0.3000, E 0.1000, A 0.2267, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1333
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1017
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.165, 0.1723]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1703, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1680, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1910, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1706 (+/- 0.0053)
- Clean persona drift MAE: 0.1706
- Per-trait absolute error: O 0.1167, C 0.3000, E 0.1000, A 0.2367, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Dialogue coherence: 0.0614
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1632, 0.1781]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1747, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2047, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0023)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1400, C 0.3000, E 0.1000, A 0.2483, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1340
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0925
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1744, 0.1809]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=1.0000, diversity=0.5000
  - TENSION: drift=0.1707, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1764, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1910, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1729 (+/- 0.0016)
- Clean persona drift MAE: 0.1729
- Per-trait absolute error: O 0.2060, C 0.2016, E 0.1262, A 0.2110, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2913
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1021
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1707, 0.1752]

- Phase-level quality:
  - OPENING: drift=0.1991, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1605, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1740, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2170, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1850 (+/- 0.0063)
- Clean persona drift MAE: 0.1850
- Per-trait absolute error: O 0.2140, C 0.2000, E 0.1507, A 0.2445, N 0.1160
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4800
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
- Dialogue coherence: 0.0708
- Repetition rate: 0.0000
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1762, 0.1939]

- Phase-level quality:
  - OPENING: drift=0.2016, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1718, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1791, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2220, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### uk_post_office_horizon_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0013)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.2140, C 0.2042, E 0.1299, A 0.2280, N 0.1210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3597
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0980
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1777, 0.1812]

- Phase-level quality:
  - OPENING: drift=0.2026, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1661, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1728, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2335, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1751 (+/- 0.0031)
- Clean persona drift MAE: 0.1751
- Per-trait absolute error: O 0.1990, C 0.2188, E 0.2004, A 0.1523, N 0.1048
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4075
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
- Structured action validity: 0.4000
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
- Dialogue coherence: 0.1070
- Repetition rate: 0.0000
- Topic drift rate: 0.3409
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1708, 0.1794]

- Phase-level quality:
  - OPENING: drift=0.1699, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1850, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1618, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1940, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0021)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.2130, C 0.1959, E 0.2213, A 0.1520, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3109
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
- Dialogue coherence: 0.0793
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1735, 0.1794]

- Phase-level quality:
  - OPENING: drift=0.1775, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1811, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1709, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1876, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1714 (+/- 0.0023)
- Clean persona drift MAE: 0.1714
- Per-trait absolute error: O 0.2180, C 0.1826, E 0.2009, A 0.1545, N 0.1013
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9705
- Planned action coverage: 1.0000
- Action family convergence: 0.7167
- Role action diversity: 0.4167
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0964
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1683, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1644, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1838, convergence=0.6000, diversity=0.5000
  - NEGOTIATION: drift=0.1639, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1932, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1765 (+/- 0.0046)
- Clean persona drift MAE: 0.1765
- Per-trait absolute error: O 0.1000, C 0.2000, E 0.1211, A 0.2450, N 0.2167
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2459
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
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7917
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1270
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1702, 0.1829]

- Phase-level quality:
  - OPENING: drift=0.1843, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1850, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.2110, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1941 (+/- 0.0033)
- Clean persona drift MAE: 0.1941
- Per-trait absolute error: O 0.1567, C 0.2074, E 0.1350, A 0.2384, N 0.2333
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2050
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
- Dialogue coherence: 0.1014
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1895, 0.1987]

- Phase-level quality:
  - OPENING: drift=0.1876, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2040, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1863, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2110, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1958 (+/- 0.0023)
- Clean persona drift MAE: 0.1958
- Per-trait absolute error: O 0.1567, C 0.2110, E 0.1426, A 0.2450, N 0.2233
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.2586
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.3750
- Role action diversity: 0.7917
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1205
- Repetition rate: 0.0625
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1926, 0.1989]

- Phase-level quality:
  - OPENING: drift=0.1891, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.2004, convergence=0.0000, diversity=1.0000
  - NEGOTIATION: drift=0.1918, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.2123, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### wework_ipo_collapse_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1521 (+/- 0.0055)
- Clean persona drift MAE: 0.1521
- Per-trait absolute error: O 0.1100, C 0.1934, E 0.1536, A 0.1495, N 0.1540
- Relationship inconsistency: 0.0247
- Relationship shift rate: 0.2431
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.4000
- Clean envelope violations: 1.4000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1235
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1445, 0.1597]

- Phase-level quality:
  - OPENING: drift=0.1695, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1735, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1351, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1650, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1693 (+/- 0.0038)
- Clean persona drift MAE: 0.1693
- Per-trait absolute error: O 0.1840, C 0.2088, E 0.1906, A 0.1190, N 0.1440
- Relationship inconsistency: 0.2430
- Relationship shift rate: 0.4548
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
- Dialogue coherence: 0.0794
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.164, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1726, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1771, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1626, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### wework_ipo_collapse_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0010)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1540, C 0.2066, E 0.1657, A 0.1385, N 0.1380
- Relationship inconsistency: 0.2375
- Relationship shift rate: 0.4868
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0709
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1592, 0.162]

- Phase-level quality:
  - OPENING: drift=0.1711, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1723, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1484, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1638, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1860 (+/- 0.0024)
- Clean persona drift MAE: 0.1860
- Per-trait absolute error: O 0.1840, C 0.2800, E 0.1441, A 0.1649, N 0.1575
- Relationship inconsistency: 0.3250
- Relationship shift rate: 0.3435
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1038
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1827, 0.1894]

- Phase-level quality:
  - OPENING: drift=0.1883, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1880, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1935, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1845, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1902 (+/- 0.0032)
- Clean persona drift MAE: 0.1902
- Per-trait absolute error: O 0.2090, C 0.2830, E 0.1389, A 0.1611, N 0.1589
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4244
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1858, 0.1946]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1913, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1959, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1769, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_10actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1870 (+/- 0.0013)
- Clean persona drift MAE: 0.1870
- Per-trait absolute error: O 0.1860, C 0.2802, E 0.1543, A 0.1587, N 0.1558
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4444
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0910
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1853, 0.1888]

- Phase-level quality:
  - OPENING: drift=0.1860, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1930, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1960, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1810, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1753 (+/- 0.0026)
- Clean persona drift MAE: 0.1753
- Per-trait absolute error: O 0.1467, C 0.2333, E 0.1532, A 0.1434, N 0.2000
- Relationship inconsistency: 0.3791
- Relationship shift rate: 0.3567
- Relationship overshoot rate: 0.2500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1001
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1717, 0.1789]

- Phase-level quality:
  - OPENING: drift=0.1839, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1885, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2005, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1760, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### zoom_return_to_office_3actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2036 (+/- 0.0197)
- Clean persona drift MAE: 0.2036
- Per-trait absolute error: O 0.1633, C 0.2407, E 0.2341, A 0.1800, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2882
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
- Dialogue coherence: 0.0846
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1763, 0.231]

- Phase-level quality:
  - OPENING: drift=0.2039, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1975, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2140, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2030, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_3actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1741 (+/- 0.0015)
- Clean persona drift MAE: 0.1741
- Per-trait absolute error: O 0.1467, C 0.2480, E 0.1410, A 0.1350, N 0.2000
- Relationship inconsistency: 0.3513
- Relationship shift rate: 0.4371
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0958
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1721, 0.1762]

- Phase-level quality:
  - OPENING: drift=0.1761, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1920, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1944, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1793, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2094 (+/- 0.0025)
- Clean persona drift MAE: 0.2094
- Per-trait absolute error: O 0.2620, C 0.2200, E 0.1995, A 0.2060, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5072
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1171
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2059, 0.213]

- Phase-level quality:
  - OPENING: drift=0.2200, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1996, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2111, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2075 (+/- 0.0047)
- Clean persona drift MAE: 0.2075
- Per-trait absolute error: O 0.2520, C 0.2222, E 0.2054, A 0.1980, N 0.1600
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4227
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
- Dialogue coherence: 0.0789
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.201, 0.214]

- Phase-level quality:
  - OPENING: drift=0.2147, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2031, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2041, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### zoom_return_to_office_5actor:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1980 (+/- 0.0011)
- Clean persona drift MAE: 0.1980
- Per-trait absolute error: O 0.2420, C 0.2222, E 0.1600, A 0.2035, N 0.1620
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.3884
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9000
- Clean envelope violations: 2.9000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1964, 0.1995]

- Phase-level quality:
  - OPENING: drift=0.2093, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2020, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1925, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Mode Summary
### exploratory:engine_dialogue_only
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1693 (+/- 0.0141)
- Clean persona drift MAE: 0.1693
- Per-trait absolute error: O 0.1567, C 0.2215, E 0.1287, A 0.1689, N 0.1709
- Relationship inconsistency: 0.0651
- Relationship shift rate: 0.2821
- Relationship overshoot rate: 0.2100
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0600
- Clean envelope violations: 2.0600
- Structured action validity: 0.4361
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.2667
- Action-plan alignment: 0.9700
- Planned action coverage: 0.9087
- Action family convergence: 0.7558
- Role action diversity: 0.4843
- Negotiation uniqueness: 0.2793
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1066
- Repetition rate: 0.0021
- Topic drift rate: 0.4729
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1658, 0.1729]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.7811, diversity=0.3805
  - TENSION: drift=0.1742, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1735, convergence=0.6467, diversity=0.4769
  - CLOSING: drift=0.1798, convergence=0.7167, diversity=0.5278

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### exploratory:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1800 (+/- 0.0163)
- Clean persona drift MAE: 0.1800
- Per-trait absolute error: O 0.1818, C 0.2259, E 0.1470, A 0.1780, N 0.1672
- Relationship inconsistency: 0.0798
- Relationship shift rate: 0.3320
- Relationship overshoot rate: 0.2175
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2444
- Clean envelope violations: 2.2444
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0795
- Repetition rate: 0.0000
- Topic drift rate: 0.4988
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1758, 0.1841]

- Phase-level quality:
  - OPENING: drift=0.1811, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1817, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1803, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1849, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### exploratory:naive_informed
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1734 (+/- 0.0137)
- Clean persona drift MAE: 0.1734
- Per-trait absolute error: O 0.1703, C 0.2241, E 0.1320, A 0.1724, N 0.1683
- Relationship inconsistency: 0.0692
- Relationship shift rate: 0.3042
- Relationship overshoot rate: 0.1950
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1550
- Clean envelope violations: 2.1550
- Structured action validity: 0.4361
- Owner resolution rate: 0.8667
- Executed action contradiction: 0.0000
- State transition coherence: 0.8667
- Action feedback utilization: 0.4000
- Action-plan alignment: 0.9700
- Planned action coverage: 0.9087
- Action family convergence: 0.7558
- Role action diversity: 0.4766
- Negotiation uniqueness: 0.2798
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0910
- Repetition rate: 0.0035
- Topic drift rate: 0.4860
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.17, 0.1769]

- Phase-level quality:
  - OPENING: drift=0.1771, convergence=0.7478, diversity=0.3625
  - TENSION: drift=0.1765, convergence=0.7456, diversity=0.4361
  - NEGOTIATION: drift=0.1755, convergence=0.6800, diversity=0.4930
  - CLOSING: drift=0.1821, convergence=0.7000, diversity=0.5222

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### guided:engine_dialogue_only
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1706 (+/- 0.0200)
- Clean persona drift MAE: 0.1706
- Per-trait absolute error: O 0.1707, C 0.2201, E 0.1295, A 0.1615, N 0.1714
- Relationship inconsistency: 0.1178
- Relationship shift rate: 0.3041
- Relationship overshoot rate: 0.2283
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0861
- Clean envelope violations: 2.0861
- Structured action validity: 0.7481
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9660
- Planned action coverage: 0.9351
- Action family convergence: 0.6836
- Role action diversity: 0.5219
- Negotiation uniqueness: 0.2953
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1048
- Repetition rate: 0.0021
- Topic drift rate: 0.5431
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1656, 0.1757]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.7945, diversity=0.3681
  - TENSION: drift=0.1743, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1731, convergence=0.5933, diversity=0.5153
  - CLOSING: drift=0.1834, convergence=0.5333, diversity=0.6014

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### guided:naive
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1786 (+/- 0.0197)
- Clean persona drift MAE: 0.1786
- Per-trait absolute error: O 0.1840, C 0.2251, E 0.1495, A 0.1644, N 0.1700
- Relationship inconsistency: 0.0966
- Relationship shift rate: 0.3144
- Relationship overshoot rate: 0.2400
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2728
- Clean envelope violations: 2.2728
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
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
- Topic drift rate: 0.5912
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1736, 0.1836]

- Phase-level quality:
  - OPENING: drift=0.1827, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1773, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1792, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1867, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### guided:naive_informed
- Runs: 60
- Clean runs: 60
- Contaminated runs: 0
- Persona drift MAE: 0.1716 (+/- 0.0178)
- Clean persona drift MAE: 0.1716
- Per-trait absolute error: O 0.1740, C 0.2223, E 0.1305, A 0.1596, N 0.1716
- Relationship inconsistency: 0.1573
- Relationship shift rate: 0.3167
- Relationship overshoot rate: 0.2614
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1572
- Clean envelope violations: 2.1572
- Structured action validity: 0.7481
- Owner resolution rate: 0.9667
- Executed action contradiction: 0.0000
- State transition coherence: 0.9667
- Action feedback utilization: 0.1333
- Action-plan alignment: 0.9659
- Planned action coverage: 0.9351
- Action family convergence: 0.6836
- Role action diversity: 0.5175
- Negotiation uniqueness: 0.2944
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0952
- Repetition rate: 0.0053
- Topic drift rate: 0.5899
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1671, 0.1761]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.7945, diversity=0.3694
  - TENSION: drift=0.1736, convergence=0.6800, diversity=0.4833
  - NEGOTIATION: drift=0.1745, convergence=0.6100, diversity=0.5214
  - CLOSING: drift=0.1825, convergence=0.5500, diversity=0.6125

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate


## Family Summary
### algorithmic_accountability:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1856 (+/- 0.0014)
- Clean persona drift MAE: 0.1856
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1247, A 0.2333, N 0.1467
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2800
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
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1035
- Repetition rate: 0.0625
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1838, 0.1875]

- Phase-level quality:
  - OPENING: drift=0.1843, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1870, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1820, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### algorithmic_accountability:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1890 (+/- 0.0041)
- Clean persona drift MAE: 0.1890
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1686, A 0.2333, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2200
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0717
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1833, 0.1947]

- Phase-level quality:
  - OPENING: drift=0.1841, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1927, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2031, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### algorithmic_accountability:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1804 (+/- 0.0025)
- Clean persona drift MAE: 0.1804
- Per-trait absolute error: O 0.1900, C 0.2333, E 0.1122, A 0.2333, N 0.1333
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.3709
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8334
- Clean envelope violations: 1.8334
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.2500
- Role action diversity: 0.8333
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0854
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1769, 0.184]

- Phase-level quality:
  - OPENING: drift=0.1771, convergence=0.5000, diversity=0.6667
  - TENSION: drift=0.1839, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1885, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1700, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_acquisition:engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1691 (+/- 0.0119)
- Clean persona drift MAE: 0.1691
- Per-trait absolute error: O 0.1732, C 0.2230, E 0.1162, A 0.1497, N 0.1836
- Relationship inconsistency: 0.0479
- Relationship shift rate: 0.3025
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1889
- Clean envelope violations: 2.1889
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9749
- Planned action coverage: 1.0000
- Action family convergence: 0.5306
- Role action diversity: 0.5972
- Negotiation uniqueness: 0.3376
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1047
- Repetition rate: 0.0000
- Topic drift rate: 0.4502
- Fallback taxonomy: n/a
- State trajectory variance: 0.0079
- Mean turns: 15.67
- Persona drift 95% CI: [0.1596, 0.1786]

- Phase-level quality:
  - OPENING: drift=0.1767, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1740, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1661, convergence=0.4889, diversity=0.6111
  - CLOSING: drift=0.1933, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_acquisition:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1776 (+/- 0.0141)
- Clean persona drift MAE: 0.1776
- Per-trait absolute error: O 0.2009, C 0.2317, E 0.1289, A 0.1493, N 0.1771
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2697
- Relationship overshoot rate: 0.1500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1389
- Clean envelope violations: 2.1389
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0732
- Repetition rate: 0.0000
- Topic drift rate: 0.5931
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1662, 0.1889]

- Phase-level quality:
  - OPENING: drift=0.1842, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1776, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1762, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1978, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_acquisition:naive_informed
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1699 (+/- 0.0137)
- Clean persona drift MAE: 0.1699
- Per-trait absolute error: O 0.1780, C 0.2189, E 0.1175, A 0.1492, N 0.1859
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.2364
- Relationship overshoot rate: 0.3000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1111
- Clean envelope violations: 2.1111
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9749
- Planned action coverage: 1.0000
- Action family convergence: 0.5306
- Role action diversity: 0.5972
- Negotiation uniqueness: 0.3376
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0891
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0079
- Mean turns: 15.67
- Persona drift 95% CI: [0.1589, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1757, convergence=0.8222, diversity=0.3889
  - TENSION: drift=0.1761, convergence=0.5889, diversity=0.5556
  - NEGOTIATION: drift=0.1727, convergence=0.4889, diversity=0.6111
  - CLOSING: drift=0.1871, convergence=0.2222, diversity=0.8333

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_crisis:engine_dialogue_only
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1722 (+/- 0.0052)
- Clean persona drift MAE: 0.1722
- Per-trait absolute error: O 0.1522, C 0.2317, E 0.1457, A 0.1634, N 0.1680
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3298
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2167
- Clean envelope violations: 2.2167
- Structured action validity: 0.5333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1250
- Action-plan alignment: 0.9716
- Planned action coverage: 1.0000
- Action family convergence: 0.7271
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.2841
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1110
- Repetition rate: 0.0000
- Topic drift rate: 0.5455
- Fallback taxonomy: n/a
- State trajectory variance: 0.0071
- Mean turns: 16.50
- Persona drift 95% CI: [0.1686, 0.1758]

- Phase-level quality:
  - OPENING: drift=0.1738, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1744, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1773, convergence=0.6500, diversity=0.5000
  - CLOSING: drift=0.1857, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_crisis:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1842 (+/- 0.0105)
- Clean persona drift MAE: 0.1842
- Per-trait absolute error: O 0.1729, C 0.2287, E 0.1744, A 0.1755, N 0.1697
- Relationship inconsistency: 0.0281
- Relationship shift rate: 0.2880
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1458
- Clean envelope violations: 2.1458
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0905
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.177, 0.1915]

- Phase-level quality:
  - OPENING: drift=0.1807, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1869, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1840, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1850, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis:naive_informed
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1778 (+/- 0.0107)
- Clean persona drift MAE: 0.1778
- Per-trait absolute error: O 0.1670, C 0.2304, E 0.1524, A 0.1733, N 0.1657
- Relationship inconsistency: 0.0281
- Relationship shift rate: 0.1925
- Relationship overshoot rate: 0.0563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1875
- Clean envelope violations: 2.1875
- Structured action validity: 0.5333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9716
- Planned action coverage: 1.0000
- Action family convergence: 0.7271
- Role action diversity: 0.4792
- Negotiation uniqueness: 0.2841
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1051
- Repetition rate: 0.0156
- Topic drift rate: 0.5568
- Fallback taxonomy: n/a
- State trajectory variance: 0.0071
- Mean turns: 16.50
- Persona drift 95% CI: [0.1704, 0.1852]

- Phase-level quality:
  - OPENING: drift=0.1756, convergence=0.8250, diversity=0.3750
  - TENSION: drift=0.1774, convergence=0.6000, diversity=0.5416
  - NEGOTIATION: drift=0.1790, convergence=0.6500, diversity=0.5000
  - CLOSING: drift=0.1846, convergence=0.8334, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### corporate_crisis_management:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1521 (+/- 0.0055)
- Clean persona drift MAE: 0.1521
- Per-trait absolute error: O 0.1100, C 0.1934, E 0.1536, A 0.1495, N 0.1540
- Relationship inconsistency: 0.0247
- Relationship shift rate: 0.2431
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.4000
- Clean envelope violations: 1.4000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1235
- Repetition rate: 0.0000
- Topic drift rate: 0.3929
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1445, 0.1597]

- Phase-level quality:
  - OPENING: drift=0.1695, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1735, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1351, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1650, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1693 (+/- 0.0038)
- Clean persona drift MAE: 0.1693
- Per-trait absolute error: O 0.1840, C 0.2088, E 0.1906, A 0.1190, N 0.1440
- Relationship inconsistency: 0.2430
- Relationship shift rate: 0.4548
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
- Dialogue coherence: 0.0794
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.164, 0.1746]

- Phase-level quality:
  - OPENING: drift=0.1726, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1771, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1626, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1750, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_crisis_management:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0010)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1540, C 0.2066, E 0.1657, A 0.1385, N 0.1380
- Relationship inconsistency: 0.2375
- Relationship shift rate: 0.4868
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9714
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.4286
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0709
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1592, 0.162]

- Phase-level quality:
  - OPENING: drift=0.1711, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1723, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1484, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1638, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1860 (+/- 0.0024)
- Clean persona drift MAE: 0.1860
- Per-trait absolute error: O 0.1840, C 0.2800, E 0.1441, A 0.1649, N 0.1575
- Relationship inconsistency: 0.3250
- Relationship shift rate: 0.3435
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1038
- Repetition rate: 0.0000
- Topic drift rate: 0.4773
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1827, 0.1894]

- Phase-level quality:
  - OPENING: drift=0.1883, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1880, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1935, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1845, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1902 (+/- 0.0032)
- Clean persona drift MAE: 0.1902
- Per-trait absolute error: O 0.2090, C 0.2830, E 0.1389, A 0.1611, N 0.1589
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4244
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.0819
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1858, 0.1946]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1913, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1959, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1769, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_policy_change:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1870 (+/- 0.0013)
- Clean persona drift MAE: 0.1870
- Per-trait absolute error: O 0.1860, C 0.2802, E 0.1543, A 0.1587, N 0.1558
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4444
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4500
- Clean envelope violations: 2.4500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9682
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0910
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1853, 0.1888]

- Phase-level quality:
  - OPENING: drift=0.1860, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1930, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1960, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1810, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_turnaround:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1469 (+/- 0.0000)
- Clean persona drift MAE: 0.1469
- Per-trait absolute error: O 0.1240, C 0.2000, E 0.1183, A 0.1250, N 0.1670
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3203
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
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
- Dialogue coherence: 0.1137
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1468, 0.1469]

- Phase-level quality:
  - OPENING: drift=0.1659, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1306, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1462, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1956, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### corporate_turnaround:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1623 (+/- 0.0059)
- Clean persona drift MAE: 0.1623
- Per-trait absolute error: O 0.1540, C 0.2044, E 0.1654, A 0.1340, N 0.1540
- Relationship inconsistency: 0.0180
- Relationship shift rate: 0.2487
- Relationship overshoot rate: 0.0000
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
- Dialogue coherence: 0.0942
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1541, 0.1706]

- Phase-level quality:
  - OPENING: drift=0.1841, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1428, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1613, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1978, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### corporate_turnaround:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1492 (+/- 0.0007)
- Clean persona drift MAE: 0.1492
- Per-trait absolute error: O 0.1340, C 0.2044, E 0.1182, A 0.1215, N 0.1680
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3540
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.0965
- Repetition rate: 0.0000
- Topic drift rate: 0.3571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1482, 0.1502]

- Phase-level quality:
  - OPENING: drift=0.1676, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1321, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1515, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1940, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1803 (+/- 0.0083)
- Clean persona drift MAE: 0.1803
- Per-trait absolute error: O 0.1700, C 0.2311, E 0.1420, A 0.1870, N 0.1714
- Relationship inconsistency: 0.1607
- Relationship shift rate: 0.3862
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3750
- Clean envelope violations: 2.3750
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9643
- Planned action coverage: 0.7500
- Action family convergence: 0.9166
- Role action diversity: 0.3563
- Negotiation uniqueness: 0.2089
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0970
- Repetition rate: 0.0000
- Topic drift rate: 0.4010
- Fallback taxonomy: n/a
- State trajectory variance: 0.0057
- Mean turns: 18.00
- Persona drift 95% CI: [0.1721, 0.1884]

- Phase-level quality:
  - OPENING: drift=0.1868, convergence=1.0000, diversity=0.3125
  - TENSION: drift=0.1772, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1835, convergence=0.8334, diversity=0.3625
  - CLOSING: drift=0.1913, convergence=1.0000, diversity=0.4166

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1870 (+/- 0.0117)
- Clean persona drift MAE: 0.1870
- Per-trait absolute error: O 0.1770, C 0.2300, E 0.1549, A 0.1982, N 0.1750
- Relationship inconsistency: 0.0655
- Relationship shift rate: 0.5907
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
- Dialogue coherence: 0.0706
- Repetition rate: 0.0000
- Topic drift rate: 0.5698
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1756, 0.1985]

- Phase-level quality:
  - OPENING: drift=0.1868, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1820, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1891, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1918, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### corporate_whistleblowing:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1852 (+/- 0.0045)
- Clean persona drift MAE: 0.1852
- Per-trait absolute error: O 0.1870, C 0.2300, E 0.1448, A 0.1920, N 0.1725
- Relationship inconsistency: 0.2675
- Relationship shift rate: 0.6793
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9643
- Planned action coverage: 0.7500
- Action family convergence: 0.9166
- Role action diversity: 0.4062
- Negotiation uniqueness: 0.2134
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0812
- Repetition rate: 0.0000
- Topic drift rate: 0.4838
- Fallback taxonomy: n/a
- State trajectory variance: 0.0057
- Mean turns: 18.00
- Persona drift 95% CI: [0.1808, 0.1897]

- Phase-level quality:
  - OPENING: drift=0.1867, convergence=0.7500, diversity=0.2083
  - TENSION: drift=0.1826, convergence=0.8334, diversity=0.3333
  - NEGOTIATION: drift=0.1898, convergence=0.8334, diversity=0.3750
  - CLOSING: drift=0.1916, convergence=1.0000, diversity=0.4583

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### ethical_dilemma:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1820 (+/- 0.0104)
- Clean persona drift MAE: 0.1820
- Per-trait absolute error: O 0.1200, C 0.3000, E 0.1249, A 0.1650, N 0.2000
- Relationship inconsistency: 0.1376
- Relationship shift rate: 0.2502
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.1093
- Repetition rate: 0.0000
- Topic drift rate: 0.4546
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1676, 0.1964]

- Phase-level quality:
  - OPENING: drift=0.1890, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1893, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1847, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1966, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1931 (+/- 0.0049)
- Clean persona drift MAE: 0.1931
- Per-trait absolute error: O 0.1533, C 0.3000, E 0.1338, A 0.1783, N 0.2000
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3175
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
- Dialogue coherence: 0.0596
- Repetition rate: 0.0000
- Topic drift rate: 0.2273
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1863, 0.1999]

- Phase-level quality:
  - OPENING: drift=0.1962, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1992, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1844, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2077, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### ethical_dilemma:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1788 (+/- 0.0026)
- Clean persona drift MAE: 0.1788
- Per-trait absolute error: O 0.1033, C 0.3000, E 0.1323, A 0.1583, N 0.2000
- Relationship inconsistency: 0.2981
- Relationship shift rate: 0.3599
- Relationship overshoot rate: 0.4500
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
- Dialogue coherence: 0.0875
- Repetition rate: 0.0000
- Topic drift rate: 0.2272
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1752, 0.1824]

- Phase-level quality:
  - OPENING: drift=0.1904, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1880, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1815, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.1949, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1539 (+/- 0.0058)
- Clean persona drift MAE: 0.1539
- Per-trait absolute error: O 0.1804, C 0.2236, E 0.0793, A 0.1394, N 0.1467
- Relationship inconsistency: 0.1407
- Relationship shift rate: 0.3372
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0750
- Clean envelope violations: 2.0750
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9738
- Planned action coverage: 1.0000
- Action family convergence: 0.6750
- Role action diversity: 0.5104
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1119
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0056
- Mean turns: 16.50
- Persona drift 95% CI: [0.1482, 0.1596]

- Phase-level quality:
  - OPENING: drift=0.1612, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1629, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1657, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1604, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_contagion:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1618 (+/- 0.0064)
- Clean persona drift MAE: 0.1618
- Per-trait absolute error: O 0.1804, C 0.2449, E 0.0928, A 0.1446, N 0.1467
- Relationship inconsistency: 0.2065
- Relationship shift rate: 0.3700
- Relationship overshoot rate: 0.3375
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
- Dialogue coherence: 0.0960
- Repetition rate: 0.0000
- Topic drift rate: 0.6705
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1556, 0.1681]

- Phase-level quality:
  - OPENING: drift=0.1610, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1696, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1704, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1552, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_contagion:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1641 (+/- 0.0062)
- Clean persona drift MAE: 0.1641
- Per-trait absolute error: O 0.1779, C 0.2467, E 0.1044, A 0.1439, N 0.1476
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2479
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1833
- Clean envelope violations: 2.1833
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.7500
- Action-plan alignment: 0.9738
- Planned action coverage: 1.0000
- Action family convergence: 0.6750
- Role action diversity: 0.5104
- Negotiation uniqueness: 0.3181
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.5113
- Fallback taxonomy: n/a
- State trajectory variance: 0.0056
- Mean turns: 16.50
- Persona drift 95% CI: [0.158, 0.1702]

- Phase-level quality:
  - OPENING: drift=0.1572, convergence=0.6500, diversity=0.5000
  - TENSION: drift=0.1735, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1689, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1668, convergence=1.0000, diversity=0.3750

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0002)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1930, C 0.2054, E 0.1029, A 0.1322, N 0.1925
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.3086
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9500
- Clean envelope violations: 1.9500
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
- Dialogue coherence: 0.0855
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1649, 0.1655]

- Phase-level quality:
  - OPENING: drift=0.1758, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1625, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1686, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1569, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1749 (+/- 0.0004)
- Clean persona drift MAE: 0.1749
- Per-trait absolute error: O 0.2130, C 0.1976, E 0.1324, A 0.1389, N 0.1922
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3330
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
- Dialogue coherence: 0.0757
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1744, 0.1753]

- Phase-level quality:
  - OPENING: drift=0.1739, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1774, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1795, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1646, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_aftermath:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1676 (+/- 0.0010)
- Clean persona drift MAE: 0.1676
- Per-trait absolute error: O 0.2180, C 0.1958, E 0.1047, A 0.1283, N 0.1911
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2742
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
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
- Dialogue coherence: 0.0867
- Repetition rate: 0.0416
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1662, 0.169]

- Phase-level quality:
  - OPENING: drift=0.1721, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1693, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1659, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1636, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, topic_drift_rate

### financial_crisis_management:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1675 (+/- 0.0052)
- Clean persona drift MAE: 0.1675
- Per-trait absolute error: O 0.1740, C 0.2000, E 0.1282, A 0.1155, N 0.2200
- Relationship inconsistency: 0.0675
- Relationship shift rate: 0.2341
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1249
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1604, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1884, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1558, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1715, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2045, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1764 (+/- 0.0053)
- Clean persona drift MAE: 0.1764
- Per-trait absolute error: O 0.1740, C 0.2042, E 0.1516, A 0.1325, N 0.2200
- Relationship inconsistency: 0.0795
- Relationship shift rate: 0.3385
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
- Dialogue coherence: 0.0893
- Repetition rate: 0.0000
- Topic drift rate: 0.6072
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1692, 0.1837]

- Phase-level quality:
  - OPENING: drift=0.1992, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1641, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1753, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2031, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_crisis_management:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1700 (+/- 0.0024)
- Clean persona drift MAE: 0.1700
- Per-trait absolute error: O 0.1700, C 0.2000, E 0.1456, A 0.1145, N 0.2200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2460
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9821
- Planned action coverage: 1.0000
- Action family convergence: 0.7500
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0995
- Repetition rate: 0.0000
- Topic drift rate: 0.3928
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1667, 0.1733]

- Phase-level quality:
  - OPENING: drift=0.1983, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1533, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1759, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1990, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_scandal:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1674 (+/- 0.0169)
- Clean persona drift MAE: 0.1674
- Per-trait absolute error: O 0.1666, C 0.2031, E 0.1616, A 0.1542, N 0.1517
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0675
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0167
- Clean envelope violations: 2.0167
- Structured action validity: 0.2500
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9607
- Planned action coverage: 0.6363
- Action family convergence: 0.7500
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2366
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1031
- Repetition rate: 0.0000
- Topic drift rate: 0.6802
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1508, 0.184]

- Phase-level quality:
  - OPENING: drift=0.1711, convergence=0.5834, diversity=0.3750
  - TENSION: drift=0.1836, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1803, convergence=0.5834, diversity=0.3750
  - CLOSING: drift=0.1790, convergence=0.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### financial_scandal:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1865 (+/- 0.0144)
- Clean persona drift MAE: 0.1865
- Per-trait absolute error: O 0.2454, C 0.2029, E 0.1694, A 0.1681, N 0.1467
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4649
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
- Dialogue coherence: 0.0693
- Repetition rate: 0.0000
- Topic drift rate: 0.5098
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1724, 0.2005]

- Phase-level quality:
  - OPENING: drift=0.1793, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2000, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1714, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1990, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### financial_scandal:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1803 (+/- 0.0197)
- Clean persona drift MAE: 0.1803
- Per-trait absolute error: O 0.2370, C 0.2093, E 0.1478, A 0.1588, N 0.1487
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1475
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2833
- Clean envelope violations: 2.2833
- Structured action validity: 0.2500
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9607
- Planned action coverage: 0.6363
- Action family convergence: 0.7500
- Role action diversity: 0.5695
- Negotiation uniqueness: 0.2345
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0756
- Repetition rate: 0.0000
- Topic drift rate: 0.5406
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1609, 0.1997]

- Phase-level quality:
  - OPENING: drift=0.1733, convergence=0.3333, diversity=0.2500
  - TENSION: drift=0.1890, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1860, convergence=0.8334, diversity=0.5000
  - CLOSING: drift=0.1900, convergence=0.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1790 (+/- 0.0006)
- Clean persona drift MAE: 0.1790
- Per-trait absolute error: O 0.1790, C 0.2414, E 0.1328, A 0.2147, N 0.1274
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3267
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2500
- Clean envelope violations: 2.2500
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0995
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1783, 0.1798]

- Phase-level quality:
  - OPENING: drift=0.1842, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1760, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1966, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1700, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1905 (+/- 0.0061)
- Clean persona drift MAE: 0.1905
- Per-trait absolute error: O 0.1740, C 0.2472, E 0.1636, A 0.2354, N 0.1322
- Relationship inconsistency: 0.4500
- Relationship shift rate: 0.4285
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
- Dialogue coherence: 0.0650
- Repetition rate: 0.0000
- Topic drift rate: 0.6818
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.182, 0.199]

- Phase-level quality:
  - OPENING: drift=0.1914, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1904, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2081, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1677, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### government_algorithm_failure:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1826 (+/- 0.0006)
- Clean persona drift MAE: 0.1826
- Per-trait absolute error: O 0.1740, C 0.2400, E 0.1432, A 0.2233, N 0.1327
- Relationship inconsistency: 0.1032
- Relationship shift rate: 0.2711
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.4000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2727
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0783
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1817, 0.1836]

- Phase-level quality:
  - OPENING: drift=0.1869, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1821, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1938, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1694, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### historical_injustice:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1687 (+/- 0.0026)
- Clean persona drift MAE: 0.1687
- Per-trait absolute error: O 0.1167, C 0.3000, E 0.1000, A 0.2267, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3333
- Clean envelope violations: 2.3333
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1333
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1017
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.165, 0.1723]

- Phase-level quality:
  - OPENING: drift=0.1716, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1703, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1680, convergence=0.5000, diversity=0.1666
  - CLOSING: drift=0.1910, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### historical_injustice:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1706 (+/- 0.0053)
- Clean persona drift MAE: 0.1706
- Per-trait absolute error: O 0.1167, C 0.3000, E 0.1000, A 0.2367, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
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
- Dialogue coherence: 0.0614
- Repetition rate: 0.0000
- Topic drift rate: 0.3636
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1632, 0.1781]

- Phase-level quality:
  - OPENING: drift=0.1764, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1668, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1747, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2047, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### historical_injustice:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1777 (+/- 0.0023)
- Clean persona drift MAE: 0.1777
- Per-trait absolute error: O 0.1400, C 0.3000, E 0.1000, A 0.2483, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.2727
- Action family convergence: 1.0000
- Role action diversity: 0.5139
- Negotiation uniqueness: 0.1340
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0925
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1744, 0.1809]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=1.0000, diversity=0.5000
  - TENSION: drift=0.1707, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1764, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1910, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1753 (+/- 0.0026)
- Clean persona drift MAE: 0.1753
- Per-trait absolute error: O 0.1467, C 0.2333, E 0.1532, A 0.1434, N 0.2000
- Relationship inconsistency: 0.3791
- Relationship shift rate: 0.3567
- Relationship overshoot rate: 0.2500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1001
- Repetition rate: 0.0000
- Topic drift rate: 0.4545
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1717, 0.1789]

- Phase-level quality:
  - OPENING: drift=0.1839, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1885, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.2005, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1760, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### hybrid_work_policy:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2036 (+/- 0.0197)
- Clean persona drift MAE: 0.2036
- Per-trait absolute error: O 0.1633, C 0.2407, E 0.2341, A 0.1800, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2882
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
- Dialogue coherence: 0.0846
- Repetition rate: 0.0000
- Topic drift rate: 0.2727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1763, 0.231]

- Phase-level quality:
  - OPENING: drift=0.2039, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1975, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2140, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2030, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### hybrid_work_policy:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1741 (+/- 0.0015)
- Clean persona drift MAE: 0.1741
- Per-trait absolute error: O 0.1467, C 0.2480, E 0.1410, A 0.1350, N 0.2000
- Relationship inconsistency: 0.3513
- Relationship shift rate: 0.4371
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1666
- Clean envelope violations: 2.1666
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9818
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.4545
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0958
- Repetition rate: 0.0000
- Topic drift rate: 0.4091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1721, 0.1762]

- Phase-level quality:
  - OPENING: drift=0.1761, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1920, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1944, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1793, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### infrastructure_decision:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0092)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.1200, C 0.2156, E 0.1431, A 0.1190, N 0.2280
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2772
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.4166
- Negotiation uniqueness: 0.0839
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0989
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1523, 0.178]

- Phase-level quality:
  - OPENING: drift=0.1695, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1885, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1704, convergence=1.0000, diversity=0.4166
  - CLOSING: drift=0.1692, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### infrastructure_decision:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1877 (+/- 0.0059)
- Clean persona drift MAE: 0.1877
- Per-trait absolute error: O 0.2120, C 0.2084, E 0.1500, A 0.1400, N 0.2280
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3500
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
- Dialogue coherence: 0.0619
- Repetition rate: 0.0000
- Topic drift rate: 0.3215
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1795, 0.1959]

- Phase-level quality:
  - OPENING: drift=0.1840, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1998, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1836, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1703, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### infrastructure_decision:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1715 (+/- 0.0004)
- Clean persona drift MAE: 0.1715
- Per-trait absolute error: O 0.1580, C 0.2162, E 0.1351, A 0.1245, N 0.2240
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2513
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
- Structured action validity: 0.5000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9500
- Planned action coverage: 0.7857
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.0741
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0785
- Repetition rate: 0.0000
- Topic drift rate: 0.4286
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1709, 0.1722]

- Phase-level quality:
  - OPENING: drift=0.1779, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1857, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1701, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.1831, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### institutional_failure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1729 (+/- 0.0016)
- Clean persona drift MAE: 0.1729
- Per-trait absolute error: O 0.2060, C 0.2016, E 0.1262, A 0.2110, N 0.1200
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2913
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1021
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1707, 0.1752]

- Phase-level quality:
  - OPENING: drift=0.1991, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1605, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1740, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2170, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1850 (+/- 0.0063)
- Clean persona drift MAE: 0.1850
- Per-trait absolute error: O 0.2140, C 0.2000, E 0.1507, A 0.2445, N 0.1160
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4800
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
- Dialogue coherence: 0.0708
- Repetition rate: 0.0000
- Topic drift rate: 0.5715
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1762, 0.1939]

- Phase-level quality:
  - OPENING: drift=0.2016, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1718, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1791, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2220, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_failure:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1794 (+/- 0.0013)
- Clean persona drift MAE: 0.1794
- Per-trait absolute error: O 0.2140, C 0.2042, E 0.1299, A 0.2280, N 0.1210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3597
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.6667
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0980
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1777, 0.1812]

- Phase-level quality:
  - OPENING: drift=0.2026, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1661, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1728, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2335, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1947 (+/- 0.0016)
- Clean persona drift MAE: 0.1947
- Per-trait absolute error: O 0.1940, C 0.1888, E 0.2090, A 0.2017, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1350
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7000
- Clean envelope violations: 2.7000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0897
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1925, 0.1969]

- Phase-level quality:
  - OPENING: drift=0.1976, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1974, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1920, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1884, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1969 (+/- 0.0050)
- Clean persona drift MAE: 0.1969
- Per-trait absolute error: O 0.1990, C 0.1873, E 0.2230, A 0.1965, N 0.1789
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4118
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
- Dialogue coherence: 0.0747
- Repetition rate: 0.0000
- Topic drift rate: 0.1819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.19, 0.2038]

- Phase-level quality:
  - OPENING: drift=0.1907, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2075, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1939, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2038, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### institutional_harm:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1927 (+/- 0.0028)
- Clean persona drift MAE: 0.1927
- Per-trait absolute error: O 0.2020, C 0.1815, E 0.2054, A 0.1946, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3980
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5000
- Clean envelope violations: 2.5000
- Structured action validity: 0.3333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9727
- Planned action coverage: 1.0000
- Action family convergence: 0.8167
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0966
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1888, 0.1966]

- Phase-level quality:
  - OPENING: drift=0.1999, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1947, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1906, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1880, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_dispute:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1872 (+/- 0.0000)
- Clean persona drift MAE: 0.1872
- Per-trait absolute error: O 0.1680, C 0.2000, E 0.1450, A 0.2145, N 0.2090
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2556
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.0741
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1044
- Repetition rate: 0.0000
- Topic drift rate: 0.8215
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1872, 0.1873]

- Phase-level quality:
  - OPENING: drift=0.1907, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1806, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1829, convergence=1.0000, diversity=0.2916
  - CLOSING: drift=0.2215, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_dispute:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1859 (+/- 0.0042)
- Clean persona drift MAE: 0.1859
- Per-trait absolute error: O 0.1780, C 0.2066, E 0.1260, A 0.2180, N 0.2010
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.4693
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
- Dialogue coherence: 0.0777
- Repetition rate: 0.0000
- Topic drift rate: 0.8571
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1801, 0.1917]

- Phase-level quality:
  - OPENING: drift=0.1924, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1786, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1823, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2371, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_dispute:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1825 (+/- 0.0037)
- Clean persona drift MAE: 0.1825
- Per-trait absolute error: O 0.1840, C 0.2000, E 0.1130, A 0.2055, N 0.2100
- Relationship inconsistency: 0.0653
- Relationship shift rate: 0.3388
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.6429
- Action family convergence: 1.0000
- Role action diversity: 0.3958
- Negotiation uniqueness: 0.0801
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0888
- Repetition rate: 0.0000
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1774, 0.1876]

- Phase-level quality:
  - OPENING: drift=0.1970, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1681, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1815, convergence=1.0000, diversity=0.3333
  - CLOSING: drift=0.2284, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_negotiation:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1343 (+/- 0.0066)
- Clean persona drift MAE: 0.1343
- Per-trait absolute error: O 0.0966, C 0.1000, E 0.1033, A 0.1717, N 0.2000
- Relationship inconsistency: 0.0015
- Relationship shift rate: 0.4437
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
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.5486
- Negotiation uniqueness: 0.1270
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1096
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1252, 0.1434]

- Phase-level quality:
  - OPENING: drift=0.1610, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1579, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1454, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1540, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_negotiation:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1588 (+/- 0.0137)
- Clean persona drift MAE: 0.1588
- Per-trait absolute error: O 0.1567, C 0.1000, E 0.1688, A 0.1683, N 0.2000
- Relationship inconsistency: 0.1605
- Relationship shift rate: 0.2830
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
- Dialogue coherence: 0.0870
- Repetition rate: 0.0000
- Topic drift rate: 0.6364
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1397, 0.1778]

- Phase-level quality:
  - OPENING: drift=0.1623, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1683, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1664, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1640, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_negotiation:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1532 (+/- 0.0045)
- Clean persona drift MAE: 0.1532
- Per-trait absolute error: O 0.1734, C 0.1000, E 0.1213, A 0.1717, N 0.2000
- Relationship inconsistency: 0.5370
- Relationship shift rate: 0.4676
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
- Planned action coverage: 0.5455
- Action family convergence: 1.0000
- Role action diversity: 0.4028
- Negotiation uniqueness: 0.1125
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1250
- Repetition rate: 0.0000
- Topic drift rate: 0.6819
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1469, 0.1596]

- Phase-level quality:
  - OPENING: drift=0.1559, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1537, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1583, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1640, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### labor_policy_reform:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1599 (+/- 0.0004)
- Clean persona drift MAE: 0.1599
- Per-trait absolute error: O 0.1910, C 0.1727, E 0.1290, A 0.1442, N 0.1627
- Relationship inconsistency: 0.2753
- Relationship shift rate: 0.3993
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8500
- Clean envelope violations: 1.8500
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
- Dialogue coherence: 0.0802
- Repetition rate: 0.0000
- Topic drift rate: 0.8182
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1593, 0.1606]

- Phase-level quality:
  - OPENING: drift=0.1498, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1794, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1633, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1578, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1678 (+/- 0.0050)
- Clean persona drift MAE: 0.1678
- Per-trait absolute error: O 0.2100, C 0.1672, E 0.1484, A 0.1568, N 0.1565
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.5267
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
- Dialogue coherence: 0.0760
- Repetition rate: 0.0000
- Topic drift rate: 0.7727
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1608, 0.1747]

- Phase-level quality:
  - OPENING: drift=0.1570, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1852, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1692, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1624, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_policy_reform:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1652 (+/- 0.0019)
- Clean persona drift MAE: 0.1652
- Per-trait absolute error: O 0.2080, C 0.1716, E 0.1380, A 0.1496, N 0.1587
- Relationship inconsistency: 0.1500
- Relationship shift rate: 0.4438
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2000
- Clean envelope violations: 2.2000
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
- Dialogue coherence: 0.0877
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1624, 0.1679]

- Phase-level quality:
  - OPENING: drift=0.1493, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1835, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1625, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1637, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1542 (+/- 0.0062)
- Clean persona drift MAE: 0.1542
- Per-trait absolute error: O 0.1780, C 0.2400, E 0.0825, A 0.1005, N 0.1700
- Relationship inconsistency: 0.5620
- Relationship shift rate: 0.4889
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.6000
- Clean envelope violations: 1.6000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.7857
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1456, 0.1628]

- Phase-level quality:
  - OPENING: drift=0.1666, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1460, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1542, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2020, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1679 (+/- 0.0100)
- Clean persona drift MAE: 0.1679
- Per-trait absolute error: O 0.1780, C 0.2400, E 0.1008, A 0.1370, N 0.1840
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.5857
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
- Dialogue coherence: 0.0893
- Repetition rate: 0.0000
- Topic drift rate: 0.6786
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1542, 0.1817]

- Phase-level quality:
  - OPENING: drift=0.1730, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1536, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1637, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2020, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_reform:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1565 (+/- 0.0008)
- Clean persona drift MAE: 0.1565
- Per-trait absolute error: O 0.1820, C 0.2400, E 0.0614, A 0.1195, N 0.1800
- Relationship inconsistency: 0.3720
- Relationship shift rate: 0.5325
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8000
- Clean envelope violations: 1.8000
- Structured action validity: 1.0000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3571
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0940
- Repetition rate: 0.0000
- Topic drift rate: 0.7143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1555, 0.1576]

- Phase-level quality:
  - OPENING: drift=0.1699, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1432, convergence=0.3333, diversity=0.7500
  - NEGOTIATION: drift=0.1547, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.1970, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1560 (+/- 0.0070)
- Clean persona drift MAE: 0.1560
- Per-trait absolute error: O 0.1740, C 0.1744, E 0.1202, A 0.1789, N 0.1325
- Relationship inconsistency: 0.0936
- Relationship shift rate: 0.3277
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1000
- Clean envelope violations: 2.1000
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0968
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1463, 0.1657]

- Phase-level quality:
  - OPENING: drift=0.1752, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1502, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1620, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1551, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_relations:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1670 (+/- 0.0003)
- Clean persona drift MAE: 0.1670
- Per-trait absolute error: O 0.1860, C 0.1973, E 0.1447, A 0.1772, N 0.1298
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.4765
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
- Dialogue coherence: 0.0703
- Repetition rate: 0.0000
- Topic drift rate: 0.9091
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1666, 0.1674]

- Phase-level quality:
  - OPENING: drift=0.1786, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1567, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1723, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1556, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate, topic_drift_rate

### labor_relations:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1653 (+/- 0.0000)
- Clean persona drift MAE: 0.1653
- Per-trait absolute error: O 0.1960, C 0.1986, E 0.1263, A 0.1741, N 0.1316
- Relationship inconsistency: 0.1380
- Relationship shift rate: 0.6420
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
- Structured action validity: 0.5714
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9636
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.1818
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0635
- Repetition rate: 0.0000
- Topic drift rate: 0.8863
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1653, 0.1653]

- Phase-level quality:
  - OPENING: drift=0.1754, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1515, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1716, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1557, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: persona_drift_mae, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_rights:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1853 (+/- 0.0080)
- Clean persona drift MAE: 0.1853
- Per-trait absolute error: O 0.2266, C 0.2333, E 0.0697, A 0.2034, N 0.1934
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4550
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
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.7222
- Negotiation uniqueness: 0.1667
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0907
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1742, 0.1964]

- Phase-level quality:
  - OPENING: drift=0.1923, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1884, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.1914, convergence=0.5000, diversity=0.2500
  - CLOSING: drift=0.1721, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_rights:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1862 (+/- 0.0105)
- Clean persona drift MAE: 0.1862
- Per-trait absolute error: O 0.2266, C 0.2333, E 0.0728, A 0.2250, N 0.1734
- Relationship inconsistency: 0.2610
- Relationship shift rate: 0.3950
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
- Dialogue coherence: 0.0684
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1716, 0.2008]

- Phase-level quality:
  - OPENING: drift=0.1940, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1941, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1820, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1725, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### labor_rights:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1956 (+/- 0.0023)
- Clean persona drift MAE: 0.1956
- Per-trait absolute error: O 0.2433, C 0.2333, E 0.1047, A 0.1966, N 0.2000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4500
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
- Action-plan alignment: 0.9500
- Planned action coverage: 0.4545
- Action family convergence: 1.0000
- Role action diversity: 0.5972
- Negotiation uniqueness: 0.1458
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0819
- Repetition rate: 0.0625
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1925, 0.1988]

- Phase-level quality:
  - OPENING: drift=0.1953, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1940, convergence=1.0000, diversity=0.3333
  - NEGOTIATION: drift=0.2054, convergence=1.0000, diversity=0.5000
  - CLOSING: drift=0.1650, convergence=0.5000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, fallback_utterance_rate

### platform_governance:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1991 (+/- 0.0201)
- Clean persona drift MAE: 0.1991
- Per-trait absolute error: O 0.2188, C 0.2191, E 0.1757, A 0.2062, N 0.1753
- Relationship inconsistency: 0.1424
- Relationship shift rate: 0.2471
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.6667
- Clean envelope violations: 2.6667
- Structured action validity: 0.7857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9738
- Planned action coverage: 1.0000
- Action family convergence: 0.5458
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0953
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0032
- Mean turns: 16.50
- Persona drift 95% CI: [0.1793, 0.2188]

- Phase-level quality:
  - OPENING: drift=0.1908, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.2051, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1938, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1761, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_governance:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1978 (+/- 0.0142)
- Clean persona drift MAE: 0.1978
- Per-trait absolute error: O 0.2290, C 0.2206, E 0.1951, A 0.1701, N 0.1742
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2392
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0668
- Repetition rate: 0.0000
- Topic drift rate: 0.6477
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1839, 0.2117]

- Phase-level quality:
  - OPENING: drift=0.1894, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2018, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1960, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1948, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_governance:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1897 (+/- 0.0121)
- Clean persona drift MAE: 0.1897
- Per-trait absolute error: O 0.2198, C 0.2172, E 0.1741, A 0.1814, N 0.1559
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2174
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5084
- Clean envelope violations: 2.5084
- Structured action validity: 0.7857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9738
- Planned action coverage: 1.0000
- Action family convergence: 0.5458
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0787
- Repetition rate: 0.0000
- Topic drift rate: 0.6932
- Fallback taxonomy: n/a
- State trajectory variance: 0.0032
- Mean turns: 16.50
- Persona drift 95% CI: [0.1778, 0.2016]

- Phase-level quality:
  - OPENING: drift=0.1888, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1975, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1860, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1820, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1906 (+/- 0.0004)
- Clean persona drift MAE: 0.1906
- Per-trait absolute error: O 0.1880, C 0.2068, E 0.1830, A 0.1735, N 0.2020
- Relationship inconsistency: 0.2000
- Relationship shift rate: 0.4334
- Relationship overshoot rate: 0.5250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 1.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0948
- Repetition rate: 0.0000
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.19, 0.1913]

- Phase-level quality:
  - OPENING: drift=0.2111, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1948, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1785, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2452, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2165 (+/- 0.0015)
- Clean persona drift MAE: 0.2165
- Per-trait absolute error: O 0.1920, C 0.2156, E 0.2586, A 0.1950, N 0.2210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3136
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
- Dialogue coherence: 0.0706
- Repetition rate: 0.0000
- Topic drift rate: 0.7500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2143, 0.2186]

- Phase-level quality:
  - OPENING: drift=0.2273, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2036, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1910, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2540, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### platform_policy_enforcement:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2014 (+/- 0.0020)
- Clean persona drift MAE: 0.2014
- Per-trait absolute error: O 0.2080, C 0.2090, E 0.1892, A 0.1795, N 0.2210
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2289
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 3.0000
- Clean envelope violations: 3.0000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9679
- Planned action coverage: 1.0000
- Action family convergence: 0.5000
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0834
- Repetition rate: 0.0556
- Topic drift rate: 0.6785
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1986, 0.2042]

- Phase-level quality:
  - OPENING: drift=0.2135, convergence=0.6667, diversity=0.5000
  - TENSION: drift=0.1940, convergence=0.6667, diversity=0.5000
  - NEGOTIATION: drift=0.1849, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2452, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate

### policy_failure:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1522 (+/- 0.0019)
- Clean persona drift MAE: 0.1522
- Per-trait absolute error: O 0.1640, C 0.1866, E 0.1164, A 0.1990, N 0.0950
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4071
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
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.1742
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0944
- Repetition rate: 0.0000
- Topic drift rate: 0.2143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1496, 0.1547]

- Phase-level quality:
  - OPENING: drift=0.1510, convergence=0.5000, diversity=0.2500
  - TENSION: drift=0.1470, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1318, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1970, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate, topic_drift_rate

### policy_failure:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1478 (+/- 0.0050)
- Clean persona drift MAE: 0.1478
- Per-trait absolute error: O 0.1500, C 0.1976, E 0.1015, A 0.1900, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3667
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
- Dialogue coherence: 0.0603
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1409, 0.1547]

- Phase-level quality:
  - OPENING: drift=0.1577, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1439, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1311, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2025, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_failure:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1487 (+/- 0.0021)
- Clean persona drift MAE: 0.1487
- Per-trait absolute error: O 0.1540, C 0.1866, E 0.1116, A 0.1995, N 0.0920
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.4905
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5000
- Clean envelope violations: 1.5000
- Structured action validity: 0.2500
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9800
- Planned action coverage: 0.7143
- Action family convergence: 1.0000
- Role action diversity: 0.3333
- Negotiation uniqueness: 0.2000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0839
- Repetition rate: 0.0000
- Topic drift rate: 0.1429
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1458, 0.1517]

- Phase-level quality:
  - OPENING: drift=0.1520, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1471, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1324, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1960, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_negotiation:engine_dialogue_only
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1527 (+/- 0.0062)
- Clean persona drift MAE: 0.1527
- Per-trait absolute error: O 0.1348, C 0.1911, E 0.1219, A 0.1438, N 0.1716
- Relationship inconsistency: 0.1877
- Relationship shift rate: 0.3108
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7556
- Clean envelope violations: 1.7556
- Structured action validity: 0.7429
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.1667
- Action-plan alignment: 0.9623
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.5486
- Negotiation uniqueness: 0.3312
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1307
- Repetition rate: 0.0000
- Topic drift rate: 0.5032
- Fallback taxonomy: n/a
- State trajectory variance: 0.0074
- Mean turns: 15.67
- Persona drift 95% CI: [0.1477, 0.1576]

- Phase-level quality:
  - OPENING: drift=0.1505, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1577, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1577, convergence=0.5556, diversity=0.5556
  - CLOSING: drift=0.1640, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### policy_negotiation:naive
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1666 (+/- 0.0027)
- Clean persona drift MAE: 0.1666
- Per-trait absolute error: O 0.1679, C 0.2049, E 0.1453, A 0.1435, N 0.1712
- Relationship inconsistency: 0.3090
- Relationship shift rate: 0.3828
- Relationship overshoot rate: 0.3750
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0333
- Clean envelope violations: 2.0333
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1067
- Repetition rate: 0.0000
- Topic drift rate: 0.5714
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 15.67
- Persona drift 95% CI: [0.1644, 0.1687]

- Phase-level quality:
  - OPENING: drift=0.1603, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1646, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1684, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1709, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### policy_negotiation:naive_informed
- Runs: 6
- Clean runs: 6
- Contaminated runs: 0
- Persona drift MAE: 0.1558 (+/- 0.0038)
- Clean persona drift MAE: 0.1558
- Per-trait absolute error: O 0.1309, C 0.1993, E 0.1257, A 0.1443, N 0.1788
- Relationship inconsistency: 0.4428
- Relationship shift rate: 0.3392
- Relationship overshoot rate: 0.4143
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.8722
- Clean envelope violations: 1.8722
- Structured action validity: 0.7429
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9623
- Planned action coverage: 1.0000
- Action family convergence: 0.5833
- Role action diversity: 0.5486
- Negotiation uniqueness: 0.3312
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1272
- Repetition rate: 0.0139
- Topic drift rate: 0.5985
- Fallback taxonomy: n/a
- State trajectory variance: 0.0074
- Mean turns: 15.67
- Persona drift 95% CI: [0.1527, 0.1588]

- Phase-level quality:
  - OPENING: drift=0.1511, convergence=0.7222, diversity=0.4445
  - TENSION: drift=0.1595, convergence=0.7222, diversity=0.4445
  - NEGOTIATION: drift=0.1640, convergence=0.5556, diversity=0.5556
  - CLOSING: drift=0.1629, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate

### post-disaster_recovery:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1643 (+/- 0.0060)
- Clean persona drift MAE: 0.1643
- Per-trait absolute error: O 0.1411, C 0.2254, E 0.1145, A 0.1334, N 0.2070
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3731
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9333
- Clean envelope violations: 1.9333
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5709
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3409
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0938
- Repetition rate: 0.0000
- Topic drift rate: 0.4204
- Fallback taxonomy: n/a
- State trajectory variance: 0.0036
- Mean turns: 16.50
- Persona drift 95% CI: [0.1585, 0.1702]

- Phase-level quality:
  - OPENING: drift=0.1593, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1793, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1628, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1852, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### post-disaster_recovery:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1718 (+/- 0.0075)
- Clean persona drift MAE: 0.1718
- Per-trait absolute error: O 0.1628, C 0.2367, E 0.1156, A 0.1471, N 0.1968
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2630
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
- Dialogue coherence: 0.0704
- Repetition rate: 0.0000
- Topic drift rate: 0.5114
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1645, 0.1792]

- Phase-level quality:
  - OPENING: drift=0.1637, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1777, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1702, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1911, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### post-disaster_recovery:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1708 (+/- 0.0062)
- Clean persona drift MAE: 0.1708
- Per-trait absolute error: O 0.1478, C 0.2331, E 0.1248, A 0.1411, N 0.2072
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2450
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0917
- Clean envelope violations: 2.0917
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9750
- Planned action coverage: 1.0000
- Action family convergence: 0.5709
- Role action diversity: 0.5625
- Negotiation uniqueness: 0.3409
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0799
- Repetition rate: 0.0000
- Topic drift rate: 0.5455
- Fallback taxonomy: n/a
- State trajectory variance: 0.0036
- Mean turns: 16.50
- Persona drift 95% CI: [0.1647, 0.1769]

- Phase-level quality:
  - OPENING: drift=0.1595, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1818, convergence=0.6500, diversity=0.5000
  - NEGOTIATION: drift=0.1712, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1922, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_health_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1674 (+/- 0.0018)
- Clean persona drift MAE: 0.1674
- Per-trait absolute error: O 0.1540, C 0.2466, E 0.0998, A 0.1570, N 0.1800
- Relationship inconsistency: 0.0030
- Relationship shift rate: 0.2431
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
- Role action diversity: 0.3438
- Negotiation uniqueness: 0.1548
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1128
- Repetition rate: 0.0000
- Topic drift rate: 0.2500
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.165, 0.1699]

- Phase-level quality:
  - OPENING: drift=0.1666, convergence=1.0000, diversity=0.3750
  - TENSION: drift=0.1731, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1830, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1544, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, fallback_utterance_rate, repetition_rate

### public_health_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1783 (+/- 0.0033)
- Clean persona drift MAE: 0.1783
- Per-trait absolute error: O 0.1540, C 0.2400, E 0.1374, A 0.1740, N 0.1860
- Relationship inconsistency: 0.1616
- Relationship shift rate: 0.4143
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
- Dialogue coherence: 0.0733
- Repetition rate: 0.0000
- Topic drift rate: 0.2143
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1737, 0.1829]

- Phase-level quality:
  - OPENING: drift=0.1796, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1714, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1890, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1617, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_crisis:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1658 (+/- 0.0014)
- Clean persona drift MAE: 0.1658
- Per-trait absolute error: O 0.1440, C 0.2422, E 0.1005, A 0.1620, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2563
- Relationship overshoot rate: 0.2250
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
- Role action diversity: 0.3229
- Negotiation uniqueness: 0.1483
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0918
- Repetition rate: 0.0000
- Topic drift rate: 0.3214
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1639, 0.1676]

- Phase-level quality:
  - OPENING: drift=0.1756, convergence=1.0000, diversity=0.2916
  - TENSION: drift=0.1735, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1782, convergence=1.0000, diversity=0.2500
  - CLOSING: drift=0.1544, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, fallback_utterance_rate, repetition_rate

### public_health_failure:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1847 (+/- 0.0201)
- Clean persona drift MAE: 0.1847
- Per-trait absolute error: O 0.1802, C 0.2067, E 0.1202, A 0.2044, N 0.2117
- Relationship inconsistency: 0.2891
- Relationship shift rate: 0.3597
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2916
- Clean envelope violations: 2.2916
- Structured action validity: 0.5333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.2500
- Action-plan alignment: 0.9762
- Planned action coverage: 1.0000
- Action family convergence: 0.5458
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1176
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0076
- Mean turns: 16.50
- Persona drift 95% CI: [0.1649, 0.2044]

- Phase-level quality:
  - OPENING: drift=0.1864, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1935, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1918, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1860, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_health_failure:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1996 (+/- 0.0304)
- Clean persona drift MAE: 0.1996
- Per-trait absolute error: O 0.2193, C 0.2107, E 0.1467, A 0.2245, N 0.1966
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1485
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.8167
- Clean envelope violations: 2.8167
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
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
- Topic drift rate: 0.5568
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 16.50
- Persona drift 95% CI: [0.1698, 0.2294]

- Phase-level quality:
  - OPENING: drift=0.1915, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2060, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1949, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1911, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_health_failure:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1862 (+/- 0.0197)
- Clean persona drift MAE: 0.1862
- Per-trait absolute error: O 0.2077, C 0.2067, E 0.1216, A 0.1984, N 0.1966
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2925
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.5917
- Clean envelope violations: 2.5917
- Structured action validity: 0.5333
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9762
- Planned action coverage: 1.0000
- Action family convergence: 0.5458
- Role action diversity: 0.5834
- Negotiation uniqueness: 0.3636
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0970
- Repetition rate: 0.0000
- Topic drift rate: 0.7954
- Fallback taxonomy: n/a
- State trajectory variance: 0.0076
- Mean turns: 16.50
- Persona drift 95% CI: [0.1669, 0.2055]

- Phase-level quality:
  - OPENING: drift=0.1896, convergence=0.9000, diversity=0.3333
  - TENSION: drift=0.1968, convergence=0.5500, diversity=0.5834
  - NEGOTIATION: drift=0.1851, convergence=0.4000, diversity=0.6666
  - CLOSING: drift=0.1816, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_housing_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2016 (+/- 0.0004)
- Clean persona drift MAE: 0.2016
- Per-trait absolute error: O 0.2100, C 0.2667, E 0.1000, A 0.2183, N 0.2133
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.0867
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
- Action-plan alignment: 0.9591
- Planned action coverage: 1.0000
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1073
- Repetition rate: 0.0000
- Topic drift rate: 0.3181
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.2012, 0.2021]

- Phase-level quality:
  - OPENING: drift=0.2016, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1874, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1924, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.2040, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1997 (+/- 0.0029)
- Clean persona drift MAE: 0.1997
- Per-trait absolute error: O 0.2100, C 0.2667, E 0.1091, A 0.2333, N 0.1800
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.2250
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
- Dialogue coherence: 0.0674
- Repetition rate: 0.0000
- Topic drift rate: 0.5909
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1958, 0.2037]

- Phase-level quality:
  - OPENING: drift=0.2045, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1910, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1940, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2027, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_housing_crisis:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1933 (+/- 0.0000)
- Clean persona drift MAE: 0.1933
- Per-trait absolute error: O 0.1767, C 0.2667, E 0.1000, A 0.2233, N 0.2000
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.1867
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
- Action family convergence: 0.6250
- Role action diversity: 0.6250
- Negotiation uniqueness: 0.5455
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0958
- Repetition rate: 0.0000
- Topic drift rate: 0.7728
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 11.00
- Persona drift 95% CI: [0.1933, 0.1934]

- Phase-level quality:
  - OPENING: drift=0.1908, convergence=1.0000, diversity=0.3333
  - TENSION: drift=0.1951, convergence=0.5000, diversity=0.6667
  - NEGOTIATION: drift=0.1950, convergence=0.0000, diversity=1.0000
  - CLOSING: drift=0.1950, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy:engine_dialogue_only
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1641 (+/- 0.0084)
- Clean persona drift MAE: 0.1641
- Per-trait absolute error: O 0.1267, C 0.2065, E 0.1325, A 0.1628, N 0.1922
- Relationship inconsistency: 0.1358
- Relationship shift rate: 0.2644
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9625
- Clean envelope violations: 1.9625
- Structured action validity: 0.5000
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9712
- Planned action coverage: 1.0000
- Action family convergence: 0.5563
- Role action diversity: 0.6094
- Negotiation uniqueness: 0.4367
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1112
- Repetition rate: 0.0000
- Topic drift rate: 0.5024
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1583, 0.17]

- Phase-level quality:
  - OPENING: drift=0.1721, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1731, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1722, convergence=0.3667, diversity=0.7083
  - CLOSING: drift=0.1556, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy:naive
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1737 (+/- 0.0110)
- Clean persona drift MAE: 0.1737
- Per-trait absolute error: O 0.1553, C 0.2204, E 0.1477, A 0.1595, N 0.1857
- Relationship inconsistency: 0.0455
- Relationship shift rate: 0.2705
- Relationship overshoot rate: 0.1688
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1083
- Clean envelope violations: 2.1083
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1003
- Repetition rate: 0.0000
- Topic drift rate: 0.4854
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1661, 0.1813]

- Phase-level quality:
  - OPENING: drift=0.1852, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1748, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1809, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1624, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy:naive_informed
- Runs: 8
- Clean runs: 8
- Contaminated runs: 0
- Persona drift MAE: 0.1647 (+/- 0.0078)
- Clean persona drift MAE: 0.1647
- Per-trait absolute error: O 0.1264, C 0.2096, E 0.1316, A 0.1657, N 0.1902
- Relationship inconsistency: 0.1802
- Relationship shift rate: 0.3073
- Relationship overshoot rate: 0.3563
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9292
- Clean envelope violations: 1.9292
- Structured action validity: 0.5000
- Owner resolution rate: 0.5000
- Executed action contradiction: 0.0000
- State transition coherence: 0.5000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9701
- Planned action coverage: 1.0000
- Action family convergence: 0.5563
- Role action diversity: 0.6094
- Negotiation uniqueness: 0.4367
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0977
- Repetition rate: 0.0000
- Topic drift rate: 0.4984
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.50
- Persona drift 95% CI: [0.1593, 0.1701]

- Phase-level quality:
  - OPENING: drift=0.1744, convergence=0.6167, diversity=0.5417
  - TENSION: drift=0.1704, convergence=0.4917, diversity=0.6250
  - NEGOTIATION: drift=0.1706, convergence=0.3667, diversity=0.7083
  - CLOSING: drift=0.1581, convergence=0.7500, diversity=0.5625

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy_crisis:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1870 (+/- 0.0046)
- Clean persona drift MAE: 0.1870
- Per-trait absolute error: O 0.1555, C 0.2600, E 0.1743, A 0.1736, N 0.1716
- Relationship inconsistency: 0.0585
- Relationship shift rate: 0.2805
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.2750
- Clean envelope violations: 2.2750
- Structured action validity: 0.9000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9579
- Planned action coverage: 0.7046
- Action family convergence: 0.8334
- Role action diversity: 0.4062
- Negotiation uniqueness: 0.2429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0932
- Repetition rate: 0.0000
- Topic drift rate: 0.6932
- Fallback taxonomy: n/a
- State trajectory variance: 0.0053
- Mean turns: 18.00
- Persona drift 95% CI: [0.1826, 0.1915]

- Phase-level quality:
  - OPENING: drift=0.1883, convergence=0.8334, diversity=0.3542
  - TENSION: drift=0.1949, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.1913, convergence=0.8334, diversity=0.4166
  - CLOSING: drift=0.2010, convergence=1.0000, diversity=0.3958

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### public_policy_crisis:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.2019 (+/- 0.0064)
- Clean persona drift MAE: 0.2019
- Per-trait absolute error: O 0.1795, C 0.2619, E 0.1983, A 0.1833, N 0.1863
- Relationship inconsistency: 0.1453
- Relationship shift rate: 0.3611
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.7250
- Clean envelope violations: 2.7250
- Structured action validity: 0.0000
- Owner resolution rate: 0.0000
- Executed action contradiction: 0.0000
- State transition coherence: 0.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.0000
- Planned action coverage: 0.0000
- Action family convergence: 0.0000
- Role action diversity: 0.0000
- Negotiation uniqueness: 0.0000
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0952
- Repetition rate: 0.0000
- Topic drift rate: 0.6753
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1956, 0.2082]

- Phase-level quality:
  - OPENING: drift=0.2021, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1949, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2002, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2079, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### public_policy_crisis:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1920 (+/- 0.0028)
- Clean persona drift MAE: 0.1920
- Per-trait absolute error: O 0.1660, C 0.2600, E 0.1932, A 0.1695, N 0.1714
- Relationship inconsistency: 0.0090
- Relationship shift rate: 0.2437
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.4750
- Clean envelope violations: 2.4750
- Structured action validity: 0.9000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9579
- Planned action coverage: 0.7046
- Action family convergence: 0.8334
- Role action diversity: 0.4396
- Negotiation uniqueness: 0.2429
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0997
- Repetition rate: 0.0000
- Topic drift rate: 0.6948
- Fallback taxonomy: n/a
- State trajectory variance: 0.0053
- Mean turns: 18.00
- Persona drift 95% CI: [0.1893, 0.1948]

- Phase-level quality:
  - OPENING: drift=0.1885, convergence=0.8334, diversity=0.3750
  - TENSION: drift=0.1895, convergence=0.6666, diversity=0.4583
  - NEGOTIATION: drift=0.2021, convergence=0.8334, diversity=0.3625
  - CLOSING: drift=0.2117, convergence=0.7500, diversity=0.3125

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_compliance:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1576 (+/- 0.0019)
- Clean persona drift MAE: 0.1576
- Per-trait absolute error: O 0.1840, C 0.2037, E 0.1060, A 0.1316, N 0.1627
- Relationship inconsistency: 0.0022
- Relationship shift rate: 0.2391
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9833
- Clean envelope violations: 1.9833
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9726
- Planned action coverage: 1.0000
- Action family convergence: 0.4584
- Role action diversity: 0.6979
- Negotiation uniqueness: 0.4513
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1184
- Repetition rate: 0.0000
- Topic drift rate: 0.3652
- Fallback taxonomy: n/a
- State trajectory variance: 0.0016
- Mean turns: 12.50
- Persona drift 95% CI: [0.1557, 0.1595]

- Phase-level quality:
  - OPENING: drift=0.1718, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1694, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1596, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1866, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_compliance:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1628 (+/- 0.0049)
- Clean persona drift MAE: 0.1628
- Per-trait absolute error: O 0.2007, C 0.2113, E 0.0989, A 0.1504, N 0.1523
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.2618
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0866
- Repetition rate: 0.0000
- Topic drift rate: 0.4610
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.158, 0.1675]

- Phase-level quality:
  - OPENING: drift=0.1802, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1651, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1706, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1717, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_compliance:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1517 (+/- 0.0058)
- Clean persona drift MAE: 0.1517
- Per-trait absolute error: O 0.1523, C 0.2081, E 0.1050, A 0.1277, N 0.1653
- Relationship inconsistency: 0.1125
- Relationship shift rate: 0.3165
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.5167
- Clean envelope violations: 1.5167
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9726
- Planned action coverage: 1.0000
- Action family convergence: 0.4584
- Role action diversity: 0.6979
- Negotiation uniqueness: 0.4513
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0861
- Repetition rate: 0.0000
- Topic drift rate: 0.5779
- Fallback taxonomy: n/a
- State trajectory variance: 0.0016
- Mean turns: 12.50
- Persona drift 95% CI: [0.146, 0.1573]

- Phase-level quality:
  - OPENING: drift=0.1806, convergence=0.5834, diversity=0.5834
  - TENSION: drift=0.1582, convergence=0.4166, diversity=0.7084
  - NEGOTIATION: drift=0.1613, convergence=0.3333, diversity=0.7500
  - CLOSING: drift=0.1756, convergence=0.5000, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_crisis:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1579 (+/- 0.0019)
- Clean persona drift MAE: 0.1579
- Per-trait absolute error: O 0.1830, C 0.2500, E 0.1141, A 0.1450, N 0.0978
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
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9659
- Planned action coverage: 1.0000
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1074
- Repetition rate: 0.0000
- Topic drift rate: 0.5682
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1552, 0.1607]

- Phase-level quality:
  - OPENING: drift=0.1498, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1638, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1592, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1644, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_crisis:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1616 (+/- 0.0026)
- Clean persona drift MAE: 0.1616
- Per-trait absolute error: O 0.1780, C 0.2500, E 0.1260, A 0.1512, N 0.1029
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
- Dialogue coherence: 0.0955
- Repetition rate: 0.0000
- Topic drift rate: 0.5000
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.158, 0.1652]

- Phase-level quality:
  - OPENING: drift=0.1567, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1707, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1542, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1631, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_crisis:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1555 (+/- 0.0020)
- Clean persona drift MAE: 0.1555
- Per-trait absolute error: O 0.1830, C 0.2500, E 0.0993, A 0.1449, N 0.1000
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.0000
- Relationship overshoot rate: 0.0000
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
- Action family convergence: 0.7667
- Role action diversity: 0.3750
- Negotiation uniqueness: 0.2273
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1100
- Repetition rate: 0.0000
- Topic drift rate: 0.5228
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1527, 0.1582]

- Phase-level quality:
  - OPENING: drift=0.1488, convergence=0.8000, diversity=0.3333
  - TENSION: drift=0.1608, convergence=0.8000, diversity=0.3333
  - NEGOTIATION: drift=0.1543, convergence=0.8000, diversity=0.3333
  - CLOSING: drift=0.1638, convergence=0.6667, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, relationship_shift_rate, relationship_overshoot_rate, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_decision:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1692 (+/- 0.0064)
- Clean persona drift MAE: 0.1692
- Per-trait absolute error: O 0.1333, C 0.2810, E 0.0918, A 0.1654, N 0.1744
- Relationship inconsistency: 0.0045
- Relationship shift rate: 0.1095
- Relationship overshoot rate: 0.0000
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1500
- Clean envelope violations: 2.1500
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9667
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.2338
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1136
- Repetition rate: 0.0312
- Topic drift rate: 0.2467
- Fallback taxonomy: n/a
- State trajectory variance: 0.0046
- Mean turns: 12.50
- Persona drift 95% CI: [0.1629, 0.1754]

- Phase-level quality:
  - OPENING: drift=0.1781, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1628, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1772, convergence=0.8334, diversity=0.4166
  - CLOSING: drift=0.1874, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, fallback_utterance_rate

### regulatory_decision:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1677 (+/- 0.0025)
- Clean persona drift MAE: 0.1677
- Per-trait absolute error: O 0.1267, C 0.2800, E 0.1003, A 0.1563, N 0.1750
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1357
- Relationship overshoot rate: 0.1125
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
- Dialogue coherence: 0.0775
- Repetition rate: 0.0000
- Topic drift rate: 0.1932
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 12.50
- Persona drift 95% CI: [0.1652, 0.1701]

- Phase-level quality:
  - OPENING: drift=0.1782, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1620, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1777, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1878, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_decision:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1726 (+/- 0.0051)
- Clean persona drift MAE: 0.1726
- Per-trait absolute error: O 0.1420, C 0.2800, E 0.0847, A 0.1809, N 0.1754
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.1453
- Relationship overshoot rate: 0.1125
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.1333
- Clean envelope violations: 2.1333
- Structured action validity: 0.7000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9667
- Planned action coverage: 1.0000
- Action family convergence: 0.8750
- Role action diversity: 0.4375
- Negotiation uniqueness: 0.2338
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1069
- Repetition rate: 0.0000
- Topic drift rate: 0.2743
- Fallback taxonomy: n/a
- State trajectory variance: 0.0046
- Mean turns: 12.50
- Persona drift 95% CI: [0.1676, 0.1776]

- Phase-level quality:
  - OPENING: drift=0.1801, convergence=0.8334, diversity=0.4166
  - TENSION: drift=0.1640, convergence=0.8334, diversity=0.4166
  - NEGOTIATION: drift=0.1715, convergence=0.8334, diversity=0.4166
  - CLOSING: drift=0.1885, convergence=1.0000, diversity=0.5000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, fallback_utterance_rate, repetition_rate

### regulatory_transition:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0006)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1750, C 0.2069, E 0.1015, A 0.1525, N 0.1671
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3456
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0000
- Clean envelope violations: 2.0000
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
- Dialogue coherence: 0.1068
- Repetition rate: 0.0000
- Topic drift rate: 0.6363
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1598, 0.1614]

- Phase-level quality:
  - OPENING: drift=0.1657, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1647, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1665, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1749, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_inconsistency, relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1768 (+/- 0.0029)
- Clean persona drift MAE: 0.1768
- Per-trait absolute error: O 0.2030, C 0.2212, E 0.1478, A 0.1494, N 0.1627
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.3050
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
- Dialogue coherence: 0.0561
- Repetition rate: 0.0000
- Topic drift rate: 0.6591
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1728, 0.1808]

- Phase-level quality:
  - OPENING: drift=0.1808, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1742, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1758, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1732, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, envelope_violations, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### regulatory_transition:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1606 (+/- 0.0023)
- Clean persona drift MAE: 0.1606
- Per-trait absolute error: O 0.1760, C 0.2109, E 0.1136, A 0.1453, N 0.1571
- Relationship inconsistency: 0.0460
- Relationship shift rate: 0.3166
- Relationship overshoot rate: 0.4500
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.0500
- Clean envelope violations: 2.0500
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
- Dialogue coherence: 0.1142
- Repetition rate: 0.0000
- Topic drift rate: 0.6137
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 22.00
- Persona drift 95% CI: [0.1574, 0.1638]

- Phase-level quality:
  - OPENING: drift=0.1724, convergence=1.0000, diversity=0.1667
  - TENSION: drift=0.1704, convergence=1.0000, diversity=0.1667
  - NEGOTIATION: drift=0.1578, convergence=1.0000, diversity=0.1667
  - CLOSING: drift=0.1699, convergence=1.0000, diversity=0.2500

- Zero-variance metrics: relationship_overshoot_rate, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:engine_dialogue_only
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1520 (+/- 0.0127)
- Clean persona drift MAE: 0.1520
- Per-trait absolute error: O 0.1465, C 0.2251, E 0.1326, A 0.1343, N 0.1217
- Relationship inconsistency: 0.1656
- Relationship shift rate: 0.4053
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.7500
- Clean envelope violations: 1.7500
- Structured action validity: 0.7857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9640
- Planned action coverage: 1.0000
- Action family convergence: 0.5917
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0927
- Repetition rate: 0.0000
- Topic drift rate: 0.3653
- Fallback taxonomy: n/a
- State trajectory variance: 0.0048
- Mean turns: 18.00
- Persona drift 95% CI: [0.1396, 0.1645]

- Phase-level quality:
  - OPENING: drift=0.1517, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1553, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1553, convergence=0.7333, diversity=0.4166
  - CLOSING: drift=0.1618, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### urban_policy:naive
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1537 (+/- 0.0137)
- Clean persona drift MAE: 0.1537
- Per-trait absolute error: O 0.1415, C 0.2253, E 0.1452, A 0.1317, N 0.1244
- Relationship inconsistency: 0.1618
- Relationship shift rate: 0.3387
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
- Dialogue coherence: 0.0764
- Repetition rate: 0.0000
- Topic drift rate: 0.5990
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 18.00
- Persona drift 95% CI: [0.1402, 0.1671]

- Phase-level quality:
  - OPENING: drift=0.1630, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.1542, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.1587, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.1569, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### urban_policy:naive_informed
- Runs: 4
- Clean runs: 4
- Contaminated runs: 0
- Persona drift MAE: 0.1525 (+/- 0.0148)
- Clean persona drift MAE: 0.1525
- Per-trait absolute error: O 0.1470, C 0.2272, E 0.1409, A 0.1270, N 0.1206
- Relationship inconsistency: 0.0458
- Relationship shift rate: 0.3505
- Relationship overshoot rate: 0.3375
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 1.9750
- Clean envelope violations: 1.9750
- Structured action validity: 0.7857
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.0000
- Action-plan alignment: 0.9640
- Planned action coverage: 1.0000
- Action family convergence: 0.5917
- Role action diversity: 0.5312
- Negotiation uniqueness: 0.3279
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0804
- Repetition rate: 0.0000
- Topic drift rate: 0.4220
- Fallback taxonomy: n/a
- State trajectory variance: 0.0048
- Mean turns: 18.00
- Persona drift 95% CI: [0.138, 0.1671]

- Phase-level quality:
  - OPENING: drift=0.1546, convergence=0.7333, diversity=0.4166
  - TENSION: drift=0.1595, convergence=0.5666, diversity=0.5416
  - NEGOTIATION: drift=0.1563, convergence=0.7333, diversity=0.4166
  - CLOSING: drift=0.1540, convergence=0.3333, diversity=0.7500

- Zero-variance metrics: commitment_contradiction, fallback_utterance_rate, repetition_rate

### workplace_policy:engine_dialogue_only
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2094 (+/- 0.0025)
- Clean persona drift MAE: 0.2094
- Per-trait absolute error: O 0.2620, C 0.2200, E 0.1995, A 0.2060, N 0.1600
- Relationship inconsistency: 0.0000
- Relationship shift rate: 0.5072
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.3000
- Clean envelope violations: 2.3000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.1171
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.2059, 0.213]

- Phase-level quality:
  - OPENING: drift=0.2200, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.1996, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.2111, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: relationship_inconsistency, commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:naive
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.2075 (+/- 0.0047)
- Clean persona drift MAE: 0.2075
- Per-trait absolute error: O 0.2520, C 0.2222, E 0.2054, A 0.1980, N 0.1600
- Relationship inconsistency: 0.2250
- Relationship shift rate: 0.4227
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
- Dialogue coherence: 0.0789
- Repetition rate: 0.0000
- Topic drift rate: 0.4643
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.201, 0.214]

- Phase-level quality:
  - OPENING: drift=0.2147, convergence=0.0000, diversity=0.0000
  - TENSION: drift=0.2031, convergence=0.0000, diversity=0.0000
  - NEGOTIATION: drift=0.2041, convergence=0.0000, diversity=0.0000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=0.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate

### workplace_policy:naive_informed
- Runs: 2
- Clean runs: 2
- Contaminated runs: 0
- Persona drift MAE: 0.1980 (+/- 0.0011)
- Clean persona drift MAE: 0.1980
- Per-trait absolute error: O 0.2420, C 0.2222, E 0.1600, A 0.2035, N 0.1620
- Relationship inconsistency: 0.4130
- Relationship shift rate: 0.3884
- Relationship overshoot rate: 0.2250
- Commitment contradiction: 0.0000
- Clean commitment contradiction: 0.0000
- Envelope violations: 2.9000
- Clean envelope violations: 2.9000
- Structured action validity: 0.8000
- Owner resolution rate: 1.0000
- Executed action contradiction: 0.0000
- State transition coherence: 1.0000
- Action feedback utilization: 0.5000
- Action-plan alignment: 0.9786
- Planned action coverage: 1.0000
- Action family convergence: 0.6667
- Role action diversity: 0.5000
- Negotiation uniqueness: 0.2857
- Fallback utterance rate: 0.0000
- Dialogue coherence: 0.0963
- Repetition rate: 0.0000
- Topic drift rate: 0.5357
- Fallback taxonomy: n/a
- State trajectory variance: 0.0000
- Mean turns: 14.00
- Persona drift 95% CI: [0.1964, 0.1995]

- Phase-level quality:
  - OPENING: drift=0.2093, convergence=1.0000, diversity=0.2500
  - TENSION: drift=0.2020, convergence=1.0000, diversity=0.2500
  - NEGOTIATION: drift=0.1925, convergence=0.6667, diversity=0.5000
  - CLOSING: drift=0.2400, convergence=0.0000, diversity=1.0000

- Zero-variance metrics: commitment_contradiction, action_family_convergence, role_action_diversity, negotiation_uniqueness, fallback_utterance_rate, repetition_rate


## Feature Attribution: What Drives Each Trait Score

### Openness (O) — Mean Error: 0.1729

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| idea_count | 0.332 | 0.115 | 0.222 |
| hypothetical_count | 0.036 | 0.015 | 0.031 |
| unique_word_ratio | 0.799 | 0.815 | 0.818 |

Calibration: static

### Conscientiousness (C) — Mean Error: 0.2232

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| planning_count | 1.078 | 0.719 | 0.887 |
| structure_marker_count | 0.010 | 0.031 | 0.007 |
| detail_count | 0.000 | 0.000 | 0.000 |
| goal_reference_count | 0.000 | 0.000 | 0.000 |
| correction_count | 0.000 | 0.000 | 0.000 |

Calibration: dynamic

### Extraversion (E) — Mean Error: 0.1362

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| exclamation_count | 0.000 | 0.000 | 0.000 |
| question_count | 0.000 | 0.000 | 0.000 |
| word_count | 0.000 | 0.000 | 0.000 |
| filler_count | 0.000 | 0.000 | 0.000 |

Calibration: dynamic

### Agreeableness (A) — Mean Error: 0.1674

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| acknowledgment_count | 0.046 | 0.176 | 0.075 |
| disagreement_count | 0.074 | 0.044 | 0.058 |
| negation_count | 1.522 | 2.103 | 1.571 |
| politeness_count | 0.000 | 0.000 | 0.000 |
| compliment_count | 0.000 | 0.000 | 0.000 |

Calibration: dynamic

### Neuroticism (N) — Mean Error: 0.1699

| Feature | engine_dialogue_only (n=720) | naive (n=720) | naive_informed (n=720) |
|---------|------|------|------|
| hedge_count | 0.267 | 0.128 | 0.182 |
| self_doubt_count | 0.000 | 0.000 | 0.000 |
| reassurance_seeking_count | 0.001 | 0.001 | 0.000 |
| apology_count | 0.001 | 0.003 | 0.001 |
| emotional_word_count | 0.067 | 0.046 | 0.049 |

Calibration: dynamic


## Engine Advantage Decomposition

| Stage | Drift MAE | Delta from Previous | % of Total Improvement |
|-------|-----------|--------------------|-----------------------|
| Naive (baseline) | 0.1793 | — | — |
| + Multi-candidate pool (naive_informed) | 0.1725 | -0.0068 | 73% |
| + Controller intelligence (engine) | 0.1700 | -0.0025 | 27% |
| **Total improvement** | | **-0.0093** | **100%** |

Interpretation: 73% of the engine's drift advantage comes from having multiple candidates;
27% comes from the controller's scoring intelligence.

## Decision Driver Analysis

### engine_dialogue_only — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 170984 | sycophancy_risk | 170984 |
| TENSION | identity_consistency | 170984 | sycophancy_risk | 170984 |
| NEGOTIATION | identity_consistency | 193304 | sycophancy_risk | 193304 |
| CLOSING | identity_consistency | 105388 | sycophancy_risk | 105388 |

### naive_informed — What Drives Candidate Selection

| Phase | Top Positive Driver | Count | Top Negative Driver | Count |
|-------|-------------------|-------|-------------------|-------|
| OPENING | identity_consistency | 166818 | sycophancy_risk | 166818 |
| TENSION | identity_consistency | 166818 | sycophancy_risk | 166818 |
| NEGOTIATION | identity_consistency | 189136 | sycophancy_risk | 189136 |
| CLOSING | identity_consistency | 102984 | sycophancy_risk | 102984 |


## Per-Archetype Trait Error

| Archetype | n | O | C | E | A | N | MAE | Top Failed Trait |
|-----------|---|---|---|---|---|---|-----|-----------------|
| Academic researcher studying crypto market failures | 6 | 0.337 | 0.210 | 0.030 | 0.105 | 0.193 | 0.175 | O |
| Activision Blizzard game studio creative lead | 6 | 0.337 | 0.126 | 0.105 | 0.020 | 0.197 | 0.157 | O |
| Activision Shareholder | 6 | 0.130 | 0.310 | 0.052 | 0.301 | 0.110 | 0.180 | C |
| Activist investor | 18 | 0.070 | 0.429 | 0.177 | 0.270 | 0.256 | 0.240 | C |
| Ad-Tech Engineer | 18 | 0.124 | 0.223 | 0.103 | 0.175 | 0.046 | 0.134 | C |
| Aerospace insurance underwriter repricing risk for the MAX fleet. | 6 | 0.063 | 0.258 | 0.066 | 0.193 | 0.102 | 0.136 | C |
| Affected mother of three | 6 | 0.153 | 0.040 | 0.120 | 0.309 | 0.100 | 0.145 | A |
| Aging local worker | 6 | 0.247 | 0.087 | 0.227 | 0.017 | 0.116 | 0.139 | O |
| Alameda Research quant who uncovered the balance sheet discrepancy | 6 | 0.437 | 0.294 | 0.187 | 0.036 | 0.093 | 0.209 | O |
| Alameda Research quantitative analyst who discovered balance sheet irregularities | 6 | 0.253 | 0.386 | 0.153 | 0.081 | 0.100 | 0.194 | C |
| Alameda quant analyst | 6 | 0.420 | 0.232 | 0.269 | 0.089 | 0.007 | 0.203 | O |
| All-Hands Moderator | 6 | 0.270 | 0.046 | 0.309 | 0.200 | 0.011 | 0.167 | E |
| Amazon Fitness lead | 6 | 0.237 | 0.306 | 0.050 | 0.102 | 0.197 | 0.178 | C |
| Apple Fitness+ product lead | 12 | 0.253 | 0.252 | 0.065 | 0.102 | 0.244 | 0.183 | O |
| Bahamas Securities Commission supervisor who approved FTX license | 6 | 0.030 | 0.102 | 0.214 | 0.167 | 0.003 | 0.103 | E |
| Bahamas regulatory officer | 6 | 0.230 | 0.117 | 0.191 | 0.190 | 0.092 | 0.164 | O |
| Bahamian financial regulatory officer who approved FTX license | 6 | 0.030 | 0.316 | 0.065 | 0.203 | 0.207 | 0.164 | C |
| Barista-Organizer working two jobs | 6 | 0.370 | 0.055 | 0.163 | 0.060 | 0.086 | 0.147 | O |
| Barista-organizer working two jobs | 6 | 0.370 | 0.067 | 0.140 | 0.036 | 0.176 | 0.158 | O |
| Barista-organizer working two jobs, recently written up for 'tardiness' after union meetings | 6 | 0.253 | 0.077 | 0.144 | 0.037 | 0.066 | 0.115 | O |
| Bootstrapped SaaS Founder | 12 | 0.228 | 0.129 | 0.214 | 0.095 | 0.106 | 0.154 | O |
| Brick-and-mortar bookstore owner (Congestion Zone) | 6 | 0.050 | 0.084 | 0.268 | 0.081 | 0.026 | 0.102 | E |
| CEO of a regional airline with 14 grounded MAX aircraft, facing significant financial losses. | 6 | 0.147 | 0.248 | 0.159 | 0.098 | 0.298 | 0.190 | N |
| CFO | 6 | 0.030 | 0.446 | 0.040 | 0.199 | 0.111 | 0.165 | C |
| CRE Lease Negotiator | 6 | 0.180 | 0.446 | 0.122 | 0.014 | 0.304 | 0.213 | C |
| CRE Lease Strategist | 6 | 0.130 | 0.417 | 0.129 | 0.292 | 0.202 | 0.234 | C |
| Cabin crew safety representative | 6 | 0.170 | 0.208 | 0.064 | 0.304 | 0.098 | 0.169 | A |
| Centrelink call center team lead | 6 | 0.070 | 0.350 | 0.128 | 0.180 | 0.010 | 0.148 | C |
| Centrelink call center worker | 6 | 0.070 | 0.392 | 0.257 | 0.092 | 0.196 | 0.201 | C |
| Centrelink call center worker processing appeals | 6 | 0.063 | 0.183 | 0.106 | 0.093 | 0.008 | 0.091 | C |
| Centrelink middle manager | 6 | 0.030 | 0.384 | 0.078 | 0.199 | 0.196 | 0.177 | C |
| Chair of the pilots' union safety committee, advocating for extensive pilot retraining. | 6 | 0.170 | 0.395 | 0.042 | 0.192 | 0.103 | 0.180 | C |
| City council president | 6 | 0.070 | 0.073 | 0.274 | 0.200 | 0.200 | 0.163 | E |
| City economic development director | 6 | 0.063 | 0.175 | 0.290 | 0.098 | 0.003 | 0.126 | E |
| City official overseeing Prop C implementation | 6 | 0.047 | 0.226 | 0.373 | 0.016 | 0.107 | 0.154 | E |
| City policymaker | 6 | 0.120 | 0.289 | 0.202 | 0.011 | 0.204 | 0.165 | C |
| Clawback-targeted foundation | 6 | 0.187 | 0.083 | 0.078 | 0.399 | 0.225 | 0.194 | A |
| Cloud Infrastructure Architect | 6 | 0.220 | 0.204 | 0.036 | 0.014 | 0.093 | 0.114 | O |
| Cloud Infrastructure Engineer at Microsoft | 12 | 0.120 | 0.328 | 0.052 | 0.161 | 0.303 | 0.193 | C |
| College student (account borrower) | 6 | 0.437 | 0.305 | 0.149 | 0.103 | 0.031 | 0.205 | O |
| Commercial Real Estate Analyst | 6 | 0.170 | 0.329 | 0.024 | 0.183 | 0.014 | 0.144 | C |
| Commercial real estate analyst | 6 | 0.170 | 0.422 | 0.095 | 0.165 | 0.384 | 0.247 | C |
| Committee member who championed $10B investment | 6 | 0.063 | 0.403 | 0.230 | 0.198 | 0.097 | 0.198 | C |
| Community Church Leader organizing relief efforts | 6 | 0.220 | 0.048 | 0.219 | 0.399 | 0.335 | 0.244 | A |
| Community Church Pastor | 6 | 0.153 | 0.031 | 0.215 | 0.407 | 0.098 | 0.181 | A |
| Community Manager (Facing Layoffs) | 6 | 0.220 | 0.042 | 0.171 | 0.414 | 0.083 | 0.186 | A |
| Community church leader | 6 | 0.270 | 0.132 | 0.231 | 0.400 | 0.300 | 0.267 | A |
| Community legal aid lawyer | 6 | 0.270 | 0.284 | 0.051 | 0.401 | 0.104 | 0.222 | A |
| Community organizer | 6 | 0.220 | 0.120 | 0.308 | 0.298 | 0.112 | 0.212 | E |
| Competing streamer's retention strategist | 6 | 0.370 | 0.101 | 0.383 | 0.218 | 0.298 | 0.274 | E |
| Competitor exchange | 6 | 0.063 | 0.435 | 0.272 | 0.303 | 0.192 | 0.253 | C |
| Congestion zone business owner | 6 | 0.063 | 0.276 | 0.062 | 0.092 | 0.029 | 0.105 | C |
| Construction CEO | 6 | 0.030 | 0.237 | 0.344 | 0.296 | 0.010 | 0.183 | E |
| Construction union leader | 18 | 0.108 | 0.224 | 0.287 | 0.187 | 0.172 | 0.196 | E |
| Consumer Privacy Advocate | 6 | 0.437 | 0.110 | 0.144 | 0.289 | 0.300 | 0.256 | O |
| Consumer rights advocate | 6 | 0.170 | 0.035 | 0.037 | 0.289 | 0.183 | 0.143 | A |
| Corporate Communications VP | 6 | 0.047 | 0.204 | 0.284 | 0.022 | 0.193 | 0.150 | E |
| Corporate communications managing public perception | 6 | 0.070 | 0.241 | 0.286 | 0.018 | 0.098 | 0.143 | E |
| Corporate labor relations specialist | 6 | 0.030 | 0.222 | 0.298 | 0.300 | 0.026 | 0.175 | A |
| Corporate real estate director locked into unfavorable lease | 6 | 0.130 | 0.283 | 0.053 | 0.079 | 0.103 | 0.130 | C |
| Creative Director at Activision | 6 | 0.420 | 0.093 | 0.191 | 0.012 | 0.209 | 0.185 | O |
| Creative Director at Activision Blizzard | 6 | 0.337 | 0.101 | 0.033 | 0.196 | 0.200 | 0.173 | O |
| Customer/Disability Advocate | 6 | 0.253 | 0.079 | 0.020 | 0.254 | 0.312 | 0.184 | N |
| DPA Enforcement Officer | 6 | 0.147 | 0.394 | 0.044 | 0.236 | 0.086 | 0.181 | C |
| Data Protection Consultant | 6 | 0.097 | 0.378 | 0.096 | 0.013 | 0.223 | 0.161 | C |
| Data Protection Officer | 12 | 0.097 | 0.343 | 0.016 | 0.135 | 0.293 | 0.177 | C |
| Deaf Software Engineer | 6 | 0.353 | 0.387 | 0.075 | 0.102 | 0.098 | 0.203 | C |
| Deaf software engineer | 6 | 0.370 | 0.389 | 0.103 | 0.103 | 0.089 | 0.211 | C |
| Deaf software engineer at Zoom | 6 | 0.237 | 0.379 | 0.071 | 0.129 | 0.103 | 0.184 | C |
| Debt collection contractor | 6 | 0.130 | 0.021 | 0.242 | 0.288 | 0.096 | 0.155 | A |
| Director of charitable foundation facing FTX donation clawback | 6 | 0.153 | 0.243 | 0.023 | 0.295 | 0.123 | 0.167 | A |
| Disability advocate customer | 6 | 0.237 | 0.033 | 0.054 | 0.388 | 0.322 | 0.207 | A |
| Disability rights advocate | 12 | 0.162 | 0.043 | 0.104 | 0.275 | 0.273 | 0.171 | A |
| Disability rights advocate for mobility-limited gig workers | 6 | 0.170 | 0.102 | 0.068 | 0.274 | 0.027 | 0.128 | A |
| Disabled Transit Riders Alliance Director | 6 | 0.170 | 0.035 | 0.055 | 0.402 | 0.094 | 0.151 | A |
| Disaster Response Vet | 6 | 0.070 | 0.386 | 0.122 | 0.297 | 0.094 | 0.194 | C |
| Disney+ retention strategist | 12 | 0.362 | 0.041 | 0.238 | 0.110 | 0.211 | 0.192 | O |
| EPA regional administrator | 6 | 0.170 | 0.283 | 0.025 | 0.006 | 0.100 | 0.117 | C |
| ER physician | 6 | 0.070 | 0.422 | 0.015 | 0.091 | 0.300 | 0.179 | C |
| ER physician treating 20+ medical emergencies per week from encampments | 6 | 0.063 | 0.420 | 0.053 | 0.073 | 0.293 | 0.181 | C |
| ER physician treating encampment-related emergencies | 6 | 0.070 | 0.399 | 0.039 | 0.102 | 0.293 | 0.180 | C |
| EU Parliament Aide | 6 | 0.137 | 0.304 | 0.093 | 0.176 | 0.208 | 0.184 | C |
| EU Policy Strategist | 6 | 0.170 | 0.333 | 0.050 | 0.020 | 0.090 | 0.132 | C |
| Elderly flat owner | 12 | 0.197 | 0.183 | 0.089 | 0.398 | 0.173 | 0.208 | A |
| Employee Resource Group Lead | 6 | 0.437 | 0.024 | 0.152 | 0.304 | 0.007 | 0.185 | O |
| Employment Lawyer | 6 | 0.130 | 0.413 | 0.022 | 0.004 | 0.211 | 0.156 | C |
| Engineering Director | 6 | 0.070 | 0.153 | 0.183 | 0.115 | 0.198 | 0.144 | N |
| Engineering Manager | 6 | 0.057 | 0.203 | 0.310 | 0.095 | 0.219 | 0.177 | E |
| Enterprise Tenant (Fortune 500 CFO) | 6 | 0.130 | 0.347 | 0.178 | 0.111 | 0.287 | 0.210 | C |
| Enterprise Tenant Representative | 6 | 0.147 | 0.309 | 0.065 | 0.094 | 0.107 | 0.144 | C |
| Environmental Justice Coalition Organizer | 6 | 0.470 | 0.084 | 0.051 | 0.198 | 0.294 | 0.220 | O |
| Esports League Organizer | 12 | 0.038 | 0.381 | 0.339 | 0.177 | 0.107 | 0.209 | C |
| European Union Aviation Safety Agency representative | 6 | 0.270 | 0.324 | 0.072 | 0.096 | 0.202 | 0.193 | C |
| Evacuee | 6 | 0.247 | 0.096 | 0.206 | 0.006 | 0.406 | 0.192 | N |
| Executive facing financial losses from grounded fleet | 6 | 0.130 | 0.267 | 0.211 | 0.094 | 0.002 | 0.141 | C |
| FAA Certification Lead | 6 | 0.097 | 0.321 | 0.056 | 0.176 | 0.020 | 0.134 | C |
| FAA advisory panel member advocating for crash victims | 6 | 0.370 | 0.075 | 0.172 | 0.020 | 0.194 | 0.166 | O |
| FDA Investigator | 6 | 0.153 | 0.436 | 0.021 | 0.195 | 0.299 | 0.221 | C |
| FDIC Field Examiner | 12 | 0.180 | 0.299 | 0.077 | 0.106 | 0.100 | 0.152 | C |
| FDIC Resolution Field Examiner | 6 | 0.130 | 0.322 | 0.063 | 0.292 | 0.000 | 0.161 | C |
| FTC Regulatory Attorney | 6 | 0.063 | 0.391 | 0.055 | 0.207 | 0.210 | 0.185 | C |
| FTC antitrust specialist | 6 | 0.130 | 0.207 | 0.025 | 0.088 | 0.097 | 0.110 | C |
| FTC regulator | 6 | 0.070 | 0.447 | 0.158 | 0.091 | 0.297 | 0.213 | C |
| FTX bankruptcy trustee overseeing asset recovery | 6 | 0.070 | 0.351 | 0.033 | 0.208 | 0.293 | 0.191 | C |
| Facing layoffs after building member relationships | 6 | 0.220 | 0.083 | 0.359 | 0.311 | 0.019 | 0.198 | E |
| Factory foreman | 6 | 0.130 | 0.080 | 0.054 | 0.018 | 0.209 | 0.098 | N |
| Fed Emergency Lending Officer | 6 | 0.130 | 0.306 | 0.063 | 0.200 | 0.199 | 0.180 | C |
| Fertility doctor | 6 | 0.170 | 0.304 | 0.074 | 0.292 | 0.190 | 0.206 | C |
| Fired Organizer (Buffalo original) | 6 | 0.437 | 0.204 | 0.223 | 0.094 | 0.214 | 0.234 | O |
| Fishing Cooperative Leader | 18 | 0.152 | 0.192 | 0.033 | 0.111 | 0.278 | 0.153 | N |
| Former FTX software engineer who built withdrawal systems | 6 | 0.370 | 0.218 | 0.163 | 0.090 | 0.008 | 0.170 | O |
| Former Plant Worker | 6 | 0.030 | 0.061 | 0.149 | 0.010 | 0.194 | 0.089 | N |
| Former executive team member | 6 | 0.170 | 0.156 | 0.427 | 0.029 | 0.203 | 0.197 | E |
| Former sub-postmaster convicted of theft | 6 | 0.130 | 0.289 | 0.106 | 0.213 | 0.397 | 0.227 | N |
| Former sub-postmaster wrongfully convicted | 12 | 0.147 | 0.234 | 0.070 | 0.209 | 0.147 | 0.161 | C |
| Formerly unhoused advocate | 6 | 0.220 | 0.122 | 0.208 | 0.211 | 0.096 | 0.171 | O |
| Formerly unhoused mentor in supportive housing | 6 | 0.107 | 0.044 | 0.149 | 0.290 | 0.109 | 0.140 | A |
| Fujitsu PR director | 6 | 0.063 | 0.109 | 0.365 | 0.200 | 0.200 | 0.188 | E |
| Fujitsu lead developer (2005-2012) | 12 | 0.420 | 0.060 | 0.110 | 0.354 | 0.099 | 0.209 | O |
| Fujitsu lead developer (Horizon team) | 6 | 0.153 | 0.366 | 0.054 | 0.279 | 0.200 | 0.211 | C |
| Game Engine Architect | 6 | 0.387 | 0.118 | 0.049 | 0.203 | 0.190 | 0.189 | O |
| Gaming Journalist | 6 | 0.337 | 0.055 | 0.166 | 0.090 | 0.101 | 0.150 | O |
| Gig platform policy lead | 6 | 0.120 | 0.437 | 0.279 | 0.194 | 0.083 | 0.223 | C |
| Gig worker advocate | 6 | 0.270 | 0.117 | 0.137 | 0.198 | 0.076 | 0.160 | O |
| Government data scientist | 6 | 0.370 | 0.417 | 0.124 | 0.123 | 0.004 | 0.207 | C |
| Government data scientist who flagged algorithm flaws | 6 | 0.370 | 0.402 | 0.039 | 0.210 | 0.092 | 0.223 | C |
| Government engineer overseeing recertification | 6 | 0.063 | 0.331 | 0.059 | 0.096 | 0.198 | 0.149 | C |
| Government labor inspector | 6 | 0.113 | 0.233 | 0.026 | 0.088 | 0.209 | 0.134 | C |
| HDB policymaker | 6 | 0.057 | 0.367 | 0.196 | 0.013 | 0.110 | 0.149 | C |
| HR Diversity Officer | 6 | 0.107 | 0.311 | 0.050 | 0.394 | 0.119 | 0.196 | A |
| Hochul Administration Representative | 6 | 0.247 | 0.037 | 0.371 | 0.025 | 0.187 | 0.173 | E |
| Homeless shelter resident | 6 | 0.080 | 0.121 | 0.069 | 0.206 | 0.093 | 0.114 | A |
| Homeowners association president | 6 | 0.280 | 0.214 | 0.060 | 0.204 | 0.207 | 0.193 | O |
| Hospital EMS coordinator | 6 | 0.030 | 0.408 | 0.149 | 0.211 | 0.097 | 0.179 | C |
| Hospital Procurement Director | 12 | 0.047 | 0.247 | 0.067 | 0.152 | 0.247 | 0.152 | N |
| Hospital procurement director who integrated Theranos devices | 6 | 0.070 | 0.337 | 0.142 | 0.101 | 0.023 | 0.135 | C |
| Immigration rights lawyer | 12 | 0.320 | 0.100 | 0.135 | 0.390 | 0.195 | 0.228 | A |
| Immigration rights lawyer pushing reform | 6 | 0.337 | 0.097 | 0.162 | 0.110 | 0.176 | 0.176 | O |
| In-house counsel managing liability exposure | 6 | 0.230 | 0.362 | 0.128 | 0.104 | 0.197 | 0.204 | C |
| Indie Game Developer | 6 | 0.337 | 0.022 | 0.047 | 0.206 | 0.109 | 0.144 | O |
| Indigenous elder affected by debt notice | 6 | 0.070 | 0.117 | 0.071 | 0.299 | 0.004 | 0.112 | A |
| Institutional investor monitoring Boeing's recovery | 6 | 0.030 | 0.298 | 0.096 | 0.205 | 0.002 | 0.126 | C |
| Insurance Underwriter | 6 | 0.057 | 0.230 | 0.041 | 0.109 | 0.195 | 0.126 | C |
| International Observer | 6 | 0.370 | 0.259 | 0.038 | 0.085 | 0.109 | 0.172 | O |
| Investigative journalist | 6 | 0.470 | 0.043 | 0.181 | 0.107 | 0.100 | 0.180 | O |
| Investigative reporter covering the recertification process | 6 | 0.470 | 0.124 | 0.097 | 0.202 | 0.008 | 0.180 | O |
| Investor who introduced others to FTX yield program | 6 | 0.047 | 0.037 | 0.156 | 0.094 | 0.292 | 0.125 | N |
| Jia Wei's fiancée | 12 | 0.068 | 0.402 | 0.207 | 0.211 | 0.168 | 0.211 | C |
| Journalist covering the FTX collapse for major financial publication | 6 | 0.453 | 0.096 | 0.113 | 0.101 | 0.193 | 0.191 | O |
| Korean Import Regulator | 6 | 0.153 | 0.334 | 0.065 | 0.016 | 0.194 | 0.153 | C |
| Lab technician at Theranos who knows the tests are unreliable | 6 | 0.220 | 0.327 | 0.175 | 0.109 | 0.393 | 0.245 | N |
| Labor advocate for laid-off staff | 6 | 0.370 | 0.061 | 0.373 | 0.200 | 0.103 | 0.222 | E |
| Labor union organizer | 12 | 0.203 | 0.190 | 0.211 | 0.074 | 0.179 | 0.171 | E |
| Labor union organizer advocating for full employment benefits | 6 | 0.287 | 0.391 | 0.177 | 0.030 | 0.280 | 0.233 | C |
| Language school operator | 6 | 0.067 | 0.292 | 0.090 | 0.108 | 0.037 | 0.119 | C |
| Language school operator profiting from training fees | 6 | 0.053 | 0.390 | 0.102 | 0.195 | 0.334 | 0.215 | C |
| Legacy Media CTO | 6 | 0.063 | 0.096 | 0.024 | 0.099 | 0.100 | 0.076 | N |
| Local Journalist Covering Labor | 6 | 0.270 | 0.022 | 0.093 | 0.196 | 0.014 | 0.119 | O |
| Local Mayor | 12 | 0.125 | 0.226 | 0.206 | 0.108 | 0.031 | 0.139 | C |
| Local Municipal Leader | 6 | 0.203 | 0.156 | 0.207 | 0.125 | 0.030 | 0.144 | E |
| Local elected official | 6 | 0.237 | 0.111 | 0.233 | 0.027 | 0.011 | 0.124 | O |
| Local journalist | 12 | 0.462 | 0.119 | 0.159 | 0.166 | 0.142 | 0.210 | O |
| Longtime customer and disability advocate worried about service consistency | 6 | 0.137 | 0.010 | 0.097 | 0.223 | 0.316 | 0.156 | N |
| Lyft driver | 6 | 0.120 | 0.022 | 0.084 | 0.103 | 0.161 | 0.098 | N |
| MP (Select Committee member) | 6 | 0.057 | 0.111 | 0.166 | 0.121 | 0.003 | 0.092 | E |
| MTA Capital Projects Director | 6 | 0.170 | 0.406 | 0.208 | 0.198 | 0.294 | 0.255 | C |
| MTA capital projects manager | 12 | 0.122 | 0.345 | 0.198 | 0.050 | 0.180 | 0.179 | C |
| Media ethics professor | 6 | 0.353 | 0.095 | 0.031 | 0.193 | 0.088 | 0.152 | O |
| Medical Journalist Investigating | 6 | 0.453 | 0.162 | 0.180 | 0.026 | 0.203 | 0.205 | O |
| Medical Researcher | 12 | 0.262 | 0.134 | 0.144 | 0.243 | 0.282 | 0.213 | N |
| Mental health counselor | 6 | 0.170 | 0.184 | 0.042 | 0.397 | 0.207 | 0.200 | A |
| Microsoft Azure gaming infrastructure engineer | 6 | 0.047 | 0.271 | 0.123 | 0.185 | 0.298 | 0.185 | N |
| Microsoft Teams Enterprise Sales Director | 6 | 0.170 | 0.050 | 0.351 | 0.223 | 0.303 | 0.220 | E |
| Microsoft Teams Sales Director | 6 | 0.270 | 0.080 | 0.339 | 0.206 | 0.019 | 0.183 | E |
| Minister for Postal Affairs | 6 | 0.070 | 0.318 | 0.152 | 0.109 | 0.200 | 0.170 | C |
| Ministry of Health official | 6 | 0.047 | 0.225 | 0.031 | 0.096 | 0.106 | 0.101 | C |
| Mt. Sinai ER Transport Coordinator | 6 | 0.030 | 0.265 | 0.077 | 0.192 | 0.094 | 0.132 | C |
| NYPD Traffic Chief | 6 | 0.130 | 0.283 | 0.040 | 0.298 | 0.194 | 0.189 | A |
| Netflix APAC content negotiator | 6 | 0.057 | 0.387 | 0.197 | 0.102 | 0.197 | 0.188 | C |
| Netflix anti-fraud engineer | 12 | 0.112 | 0.309 | 0.060 | 0.008 | 0.236 | 0.145 | C |
| Netflix customer service rep | 6 | 0.163 | 0.186 | 0.083 | 0.393 | 0.025 | 0.170 | A |
| Netflix investor relations | 6 | 0.030 | 0.378 | 0.321 | 0.199 | 0.288 | 0.243 | C |
| Netflix licensing negotiator (APAC) | 6 | 0.130 | 0.395 | 0.197 | 0.105 | 0.188 | 0.203 | C |
| Netflix regional content licensing negotiator | 6 | 0.127 | 0.357 | 0.214 | 0.098 | 0.178 | 0.195 | C |
| Nonprofit director | 6 | 0.353 | 0.189 | 0.218 | 0.284 | 0.300 | 0.269 | O |
| NordVPN product lead | 6 | 0.253 | 0.076 | 0.330 | 0.295 | 0.205 | 0.232 | E |
| NordVPN product manager | 6 | 0.237 | 0.127 | 0.294 | 0.188 | 0.296 | 0.228 | N |
| Nuclear Evacuee | 6 | 0.137 | 0.084 | 0.355 | 0.020 | 0.408 | 0.201 | N |
| Office Experience Lead | 6 | 0.080 | 0.297 | 0.120 | 0.098 | 0.204 | 0.160 | C |
| Outer-borough delivery driver | 12 | 0.155 | 0.185 | 0.040 | 0.101 | 0.088 | 0.114 | C |
| Outer-borough package delivery driver (UPS/FedEx) | 6 | 0.163 | 0.208 | 0.034 | 0.058 | 0.106 | 0.114 | C |
| Password-sharing SaaS founder | 6 | 0.403 | 0.024 | 0.303 | 0.097 | 0.196 | 0.205 | O |
| Patient who received incorrect blood test results | 6 | 0.087 | 0.236 | 0.074 | 0.292 | 0.183 | 0.174 | A |
| Patient with Incorrect Results | 6 | 0.080 | 0.136 | 0.040 | 0.202 | 0.279 | 0.147 | N |
| Patient with Misdiagnosis | 6 | 0.153 | 0.029 | 0.126 | 0.297 | 0.302 | 0.181 | N |
| Payroll Provider Account Manager | 6 | 0.030 | 0.086 | 0.221 | 0.013 | 0.199 | 0.110 | E |
| Pediatrician who identified lead poisoning in children | 6 | 0.370 | 0.391 | 0.111 | 0.200 | 0.200 | 0.254 | C |
| Pediatrician who identified lead poisoning spikes | 6 | 0.370 | 0.407 | 0.077 | 0.202 | 0.207 | 0.253 | C |
| Pediatrician who published research on spiking lead levels in children | 6 | 0.337 | 0.420 | 0.064 | 0.214 | 0.180 | 0.243 | C |
| Peloton CFO | 6 | 0.170 | 0.404 | 0.038 | 0.191 | 0.103 | 0.181 | C |
| Peloton community moderator | 6 | 0.057 | 0.098 | 0.236 | 0.204 | 0.003 | 0.120 | E |
| Peloton fitness instructor | 12 | 0.253 | 0.042 | 0.324 | 0.151 | 0.175 | 0.189 | E |
| Peloton hardware engineer | 6 | 0.353 | 0.190 | 0.067 | 0.005 | 0.112 | 0.145 | O |
| Peloton head instructor | 6 | 0.253 | 0.082 | 0.353 | 0.026 | 0.208 | 0.184 | E |
| Peloton warehouse manager | 6 | 0.030 | 0.140 | 0.034 | 0.017 | 0.201 | 0.085 | N |
| Physician Who Ordered Tests | 6 | 0.063 | 0.209 | 0.122 | 0.309 | 0.096 | 0.160 | A |
| Pilots' Union Safety Chair | 6 | 0.137 | 0.411 | 0.032 | 0.185 | 0.095 | 0.172 | C |
| Player Community Moderator | 6 | 0.203 | 0.093 | 0.256 | 0.395 | 0.305 | 0.251 | A |
| Post Office audit director | 12 | 0.238 | 0.430 | 0.154 | 0.197 | 0.198 | 0.243 | C |
| Post Office internal auditor | 6 | 0.057 | 0.357 | 0.180 | 0.127 | 0.000 | 0.144 | C |
| Post Office prosecuting lawyer | 6 | 0.147 | 0.177 | 0.118 | 0.296 | 0.000 | 0.148 | A |
| Professional gaming league organizer | 6 | 0.063 | 0.389 | 0.196 | 0.183 | 0.102 | 0.187 | C |
| Property agent | 6 | 0.220 | 0.045 | 0.362 | 0.193 | 0.013 | 0.166 | E |
| Property owner facing tenant default | 6 | 0.047 | 0.260 | 0.053 | 0.304 | 0.003 | 0.133 | A |
| Public Health Researcher | 6 | 0.353 | 0.121 | 0.165 | 0.198 | 0.092 | 0.186 | O |
| Regional Airline CEO | 6 | 0.147 | 0.275 | 0.163 | 0.107 | 0.295 | 0.197 | N |
| Regional HR Director | 6 | 0.030 | 0.204 | 0.088 | 0.281 | 0.114 | 0.144 | A |
| Remote Work Advocate | 6 | 0.437 | 0.180 | 0.042 | 0.303 | 0.289 | 0.250 | O |
| Renewables Lobbyist | 6 | 0.203 | 0.052 | 0.309 | 0.217 | 0.309 | 0.218 | E |
| Reporter investigating governance failures | 6 | 0.470 | 0.111 | 0.108 | 0.187 | 0.097 | 0.195 | O |
| Retail crypto trader who lost life savings in FTX yield program | 6 | 0.197 | 0.102 | 0.113 | 0.032 | 0.307 | 0.150 | N |
| Retail crypto trader who lost life savings in FTX's yield program | 6 | 0.203 | 0.195 | 0.050 | 0.114 | 0.303 | 0.173 | N |
| Retail crypto trader with locked savings | 6 | 0.147 | 0.199 | 0.033 | 0.095 | 0.308 | 0.156 | N |
| Risk analyst adjusting premiums for MAX operations | 6 | 0.070 | 0.232 | 0.046 | 0.215 | 0.102 | 0.133 | C |
| Rural council member | 6 | 0.063 | 0.123 | 0.266 | 0.111 | 0.200 | 0.153 | E |
| Rural factory owner | 12 | 0.230 | 0.391 | 0.090 | 0.204 | 0.088 | 0.201 | C |
| Rural factory owner dependent on program labor | 6 | 0.247 | 0.269 | 0.060 | 0.185 | 0.076 | 0.167 | C |
| SFPD liaison | 6 | 0.130 | 0.305 | 0.141 | 0.087 | 0.011 | 0.135 | C |
| SVB Board Member | 6 | 0.153 | 0.206 | 0.255 | 0.289 | 0.001 | 0.181 | A |
| SVB Commercial Banker | 12 | 0.067 | 0.375 | 0.073 | 0.102 | 0.250 | 0.173 | C |
| SVB Senior Commercial Banker | 6 | 0.030 | 0.331 | 0.032 | 0.083 | 0.200 | 0.135 | C |
| SVB Treasury Manager | 6 | 0.030 | 0.173 | 0.097 | 0.004 | 0.101 | 0.081 | C |
| SVB Treasury Risk Officer | 6 | 0.030 | 0.181 | 0.098 | 0.015 | 0.100 | 0.085 | C |
| SaaS Founder (Bootstrapped) | 6 | 0.320 | 0.062 | 0.211 | 0.086 | 0.197 | 0.175 | O |
| Safety advocate pushing for rigorous retraining | 6 | 0.170 | 0.400 | 0.028 | 0.219 | 0.098 | 0.183 | C |
| Seed-stage biotech CEO with 85 employees | 6 | 0.370 | 0.153 | 0.080 | 0.090 | 0.200 | 0.179 | O |
| Senior Centrelink manager overseeing the scheme | 6 | 0.030 | 0.311 | 0.139 | 0.287 | 0.008 | 0.155 | C |
| Senior Lab Technician at Theranos | 6 | 0.370 | 0.425 | 0.154 | 0.214 | 0.093 | 0.251 | C |
| Shift Supervisor (undecided) | 6 | 0.077 | 0.112 | 0.060 | 0.176 | 0.082 | 0.102 | A |
| Shrine Keeper | 6 | 0.230 | 0.235 | 0.179 | 0.398 | 0.106 | 0.229 | A |
| Single parent issued an incorrect $12K debt notice | 6 | 0.147 | 0.022 | 0.124 | 0.092 | 0.174 | 0.112 | N |
| Single parent sharing Netflix account with ex-spouse | 6 | 0.147 | 0.206 | 0.053 | 0.307 | 0.087 | 0.160 | A |
| Single parent sharing Netflix account with ex-spouse for children's access | 6 | 0.147 | 0.242 | 0.033 | 0.315 | 0.077 | 0.163 | A |
| Single parent sharing account with ex-spouse | 6 | 0.130 | 0.219 | 0.028 | 0.312 | 0.102 | 0.158 | A |
| Single parent with $12K incorrect debt notice | 6 | 0.147 | 0.117 | 0.114 | 0.220 | 0.300 | 0.179 | N |
| Single parent wrongly issued $12K debt notice | 6 | 0.130 | 0.244 | 0.125 | 0.133 | 0.290 | 0.184 | N |
| Single-mom DoorDash driver | 12 | 0.068 | 0.145 | 0.026 | 0.168 | 0.205 | 0.123 | N |
| Single-mom DoorDash driver needing schedule flexibility for childcare | 6 | 0.080 | 0.122 | 0.029 | 0.109 | 0.220 | 0.112 | N |
| Small Business Owner Subletter | 6 | 0.287 | 0.100 | 0.135 | 0.012 | 0.021 | 0.111 | O |
| Small business owner (congestion zone) | 6 | 0.093 | 0.149 | 0.258 | 0.155 | 0.357 | 0.202 | N |
| Small business owner (convenience store) facing 60% foot traffic decline | 6 | 0.130 | 0.260 | 0.031 | 0.085 | 0.207 | 0.143 | C |
| Small business owner (retail) | 6 | 0.130 | 0.197 | 0.129 | 0.092 | 0.021 | 0.114 | C |
| Small business owner whose storefront foot traffic dropped 60% due to nearby encampments | 6 | 0.147 | 0.184 | 0.045 | 0.062 | 0.097 | 0.107 | C |
| Small game studio founder | 6 | 0.353 | 0.040 | 0.036 | 0.096 | 0.190 | 0.143 | O |
| Small restaurant owner | 12 | 0.068 | 0.271 | 0.094 | 0.057 | 0.077 | 0.113 | C |
| Social Services Minister | 6 | 0.030 | 0.225 | 0.398 | 0.188 | 0.104 | 0.189 | E |
| Social worker at community legal center | 6 | 0.370 | 0.105 | 0.153 | 0.388 | 0.100 | 0.223 | A |
| Social worker counseling affected clients | 6 | 0.170 | 0.033 | 0.142 | 0.298 | 0.197 | 0.168 | A |
| SoftBank Investment Committee Member | 12 | 0.063 | 0.284 | 0.095 | 0.195 | 0.298 | 0.187 | N |
| South Korean recruiter | 6 | 0.170 | 0.035 | 0.353 | 0.204 | 0.091 | 0.171 | E |
| Startup CEO with frozen payroll | 6 | 0.370 | 0.170 | 0.111 | 0.085 | 0.201 | 0.187 | O |
| Startup CEO with frozen payroll funds | 6 | 0.370 | 0.108 | 0.218 | 0.102 | 0.200 | 0.200 | O |
| Startup CFO | 6 | 0.070 | 0.347 | 0.098 | 0.094 | 0.301 | 0.182 | C |
| State Budget Analyst | 6 | 0.030 | 0.217 | 0.041 | 0.089 | 0.202 | 0.116 | C |
| State Health Department Official | 6 | 0.130 | 0.307 | 0.078 | 0.023 | 0.302 | 0.168 | C |
| State budget analyst | 6 | 0.130 | 0.197 | 0.058 | 0.102 | 0.100 | 0.117 | C |
| State governor | 6 | 0.030 | 0.043 | 0.187 | 0.215 | 0.200 | 0.135 | A |
| State health director | 6 | 0.270 | 0.207 | 0.019 | 0.023 | 0.300 | 0.164 | N |
| State legislator | 6 | 0.050 | 0.327 | 0.224 | 0.015 | 0.198 | 0.163 | C |
| Store Manager (10-year veteran) | 6 | 0.070 | 0.394 | 0.144 | 0.193 | 0.193 | 0.199 | C |
| Store manager torn between corporate and staff | 6 | 0.077 | 0.265 | 0.052 | 0.175 | 0.126 | 0.139 | C |
| Store manager torn between corporate anti-union directives and loyalty to staff | 6 | 0.037 | 0.213 | 0.152 | 0.253 | 0.218 | 0.175 | A |
| Street outreach worker | 6 | 0.320 | 0.043 | 0.149 | 0.393 | 0.207 | 0.222 | A |
| Street outreach worker with deep client trust relationships | 6 | 0.170 | 0.126 | 0.250 | 0.386 | 0.213 | 0.229 | A |
| Street outreach worker with years of trust relationships among unhoused clients | 6 | 0.203 | 0.014 | 0.126 | 0.388 | 0.203 | 0.187 | A |
| Sublessor dependent on WeWork infrastructure | 6 | 0.337 | 0.097 | 0.054 | 0.019 | 0.196 | 0.140 | O |
| TEPCO Safety Engineer | 18 | 0.059 | 0.419 | 0.037 | 0.187 | 0.292 | 0.199 | C |
| Taiwanese factory line supervisor | 18 | 0.130 | 0.222 | 0.043 | 0.102 | 0.075 | 0.114 | C |
| Teams Talent Scout | 6 | 0.270 | 0.126 | 0.403 | 0.200 | 0.298 | 0.259 | E |
| Teamsters Local 814 Secretary-Treasurer | 6 | 0.070 | 0.100 | 0.149 | 0.315 | 0.094 | 0.146 | A |
| Tech Journalist | 6 | 0.470 | 0.070 | 0.103 | 0.298 | 0.007 | 0.189 | O |
| Tech executive | 6 | 0.030 | 0.414 | 0.072 | 0.192 | 0.296 | 0.201 | C |
| Tech industry lobbyist | 6 | 0.063 | 0.225 | 0.339 | 0.211 | 0.283 | 0.224 | E |
| Tech journalist investigating Robodebt | 6 | 0.470 | 0.290 | 0.088 | 0.038 | 0.096 | 0.197 | O |
| Theranos Board Member | 6 | 0.047 | 0.179 | 0.309 | 0.211 | 0.004 | 0.150 | E |
| Theranos Lab Technician | 6 | 0.253 | 0.273 | 0.138 | 0.121 | 0.010 | 0.159 | C |
| Theranos Legal Counsel | 12 | 0.180 | 0.211 | 0.146 | 0.261 | 0.149 | 0.189 | A |
| Theranos Quality Assurance Lead | 6 | 0.370 | 0.405 | 0.027 | 0.098 | 0.196 | 0.219 | C |
| Third-Party Union Buster Consultant | 6 | 0.130 | 0.296 | 0.203 | 0.309 | 0.090 | 0.205 | A |
| Trapped elderly owner | 6 | 0.247 | 0.123 | 0.110 | 0.188 | 0.217 | 0.177 | O |
| URA urban planner | 6 | 0.287 | 0.403 | 0.112 | 0.009 | 0.376 | 0.237 | C |
| US Congressional representative investigating crypto regulation | 6 | 0.170 | 0.038 | 0.286 | 0.123 | 0.204 | 0.164 | E |
| Uber executive | 6 | 0.070 | 0.419 | 0.309 | 0.102 | 0.276 | 0.235 | C |
| Uber/Lyft Driver Association Leader | 6 | 0.220 | 0.209 | 0.258 | 0.018 | 0.202 | 0.181 | E |
| Union rep for postal workers | 6 | 0.170 | 0.082 | 0.311 | 0.030 | 0.300 | 0.179 | E |
| Urban planner | 6 | 0.337 | 0.378 | 0.128 | 0.115 | 0.290 | 0.250 | C |
| VC General Partner | 12 | 0.270 | 0.046 | 0.202 | 0.196 | 0.350 | 0.213 | N |
| VC Investor (Tech Portfolio) | 6 | 0.153 | 0.040 | 0.265 | 0.204 | 0.093 | 0.151 | E |
| Victim Family Representative | 6 | 0.270 | 0.067 | 0.185 | 0.293 | 0.305 | 0.224 | N |
| Victim's daughter | 6 | 0.253 | 0.191 | 0.324 | 0.313 | 0.000 | 0.216 | E |
| Vietnamese Embassy liaison | 6 | 0.253 | 0.301 | 0.103 | 0.226 | 0.299 | 0.236 | C |
| Vietnamese technical intern (former) | 6 | 0.130 | 0.211 | 0.024 | 0.025 | 0.283 | 0.135 | N |
| Vietnamese technical intern with wage theft experience | 6 | 0.147 | 0.211 | 0.057 | 0.017 | 0.095 | 0.105 | C |
| Vietnamese trainee (wage theft victim) | 6 | 0.130 | 0.166 | 0.060 | 0.122 | 0.268 | 0.149 | N |
| Village council chair | 6 | 0.170 | 0.158 | 0.210 | 0.400 | 0.201 | 0.228 | A |
| Walgreens Partnership Manager | 12 | 0.125 | 0.217 | 0.317 | 0.061 | 0.147 | 0.173 | E |
| Warehouse logistics manager | 6 | 0.047 | 0.174 | 0.037 | 0.093 | 0.097 | 0.089 | C |
| Water Treatment Plant Operator | 6 | 0.070 | 0.252 | 0.152 | 0.100 | 0.102 | 0.135 | C |
| Water Treatment Plant Supervisor | 6 | 0.057 | 0.232 | 0.145 | 0.113 | 0.215 | 0.152 | C |
| Water treatment plant supervisor | 6 | 0.070 | 0.250 | 0.058 | 0.098 | 0.000 | 0.095 | C |
| WeWork Community Manager | 6 | 0.203 | 0.042 | 0.342 | 0.265 | 0.122 | 0.195 | E |
| WeWork Interim Legal Counsel | 6 | 0.047 | 0.225 | 0.167 | 0.121 | 0.184 | 0.149 | C |
| Xbox Platform Strategist | 6 | 0.073 | 0.201 | 0.246 | 0.107 | 0.016 | 0.129 | E |
| Young couple awaiting BTO flat | 6 | 0.203 | 0.354 | 0.046 | 0.115 | 0.327 | 0.209 | C |
| Young professional awaiting BTO flat | 6 | 0.203 | 0.205 | 0.038 | 0.082 | 0.080 | 0.122 | C |
| Young professional waiting for BTO | 6 | 0.170 | 0.235 | 0.086 | 0.016 | 0.203 | 0.142 | C |
| Zoom Engineering Manager | 6 | 0.050 | 0.293 | 0.106 | 0.106 | 0.193 | 0.150 | C |

## Phase-Level Behavioral Features (Engine Condition)

| Feature | OPENING | TENSION | NEGOTIATION | CLOSING | Delta (CLOSING - OPENING) |
|---------|------|------|------|------|------|
| acknowledgment_count | 0.012 | 0.025 | 0.022 | 0.021 | +0.009 |
| apology_count | 0.000 | 0.000 | 0.002 | 0.000 | +0.000 |
| disagreement_count | 0.037 | 0.035 | 0.026 | 0.015 | -0.023 |
| emotional_word_count | 0.058 | 0.006 | 0.013 | 0.015 | -0.043 |
| hedge_count | 0.149 | 0.060 | 0.124 | 0.067 | -0.083 |
| idea_count | 0.108 | 0.096 | 0.197 | 0.098 | -0.010 |
| negation_count | 0.456 | 0.838 | 0.517 | 0.465 | +0.009 |
| reassurance_seeking_count | 0.000 | 0.000 | 0.001 | 0.000 | +0.000 |
| self_doubt_count | 0.000 | 0.000 | 0.000 | 0.000 | +0.000 |
| unique_word_ratio | 0.944 | 0.951 | 0.949 | 0.950 | +0.006 |

## Scenario Difficulty vs Drift

| Scenario | Difficulty | Engine Drift | Naive Drift | Delta |
|----------|-----------|-------------|-------------|-------|
| 10actor | 0.76 | 0.1790 | 0.1866 | -0.0075 |
| 3actor | 0.76 | 0.1856 | 0.1847 | +0.0009 |
| 5actor | 0.76 | 0.1522 | 0.1483 | +0.0039 |
| 10actor | 0.59 | 0.1579 | 0.1585 | -0.0006 |
| 3actor | 0.59 | 0.1639 | 0.1714 | -0.0075 |
| 5actor | 0.59 | 0.1744 | 0.1688 | +0.0056 |
| 10actor | 0.76 | 0.1601 | 0.1651 | -0.0050 |
| 3actor | 0.76 | 0.1520 | 0.1605 | -0.0086 |
| 5actor | 0.76 | 0.1459 | 0.1579 | -0.0120 |
| 10actor | 0.76 | 0.1606 | 0.1687 | -0.0081 |
| 3actor | 0.76 | 0.1563 | 0.1555 | +0.0008 |
| 5actor | 0.76 | 0.1589 | 0.1589 | +0.0000 |
| 10actor | 1.00 | 0.1646 | 0.1683 | -0.0037 |
| 3actor | 1.00 | 0.2047 | 0.2175 | -0.0128 |
| 5actor | 1.00 | 0.1674 | 0.1720 | -0.0046 |
| 10actor | 1.00 | 0.1652 | 0.1712 | -0.0060 |
| 3actor | 1.00 | 0.1515 | 0.1671 | -0.0156 |
| 5actor | 1.00 | 0.1834 | 0.1997 | -0.0163 |
| 10actor | 0.68 | 0.1686 | 0.1781 | -0.0094 |
| 3actor | 0.68 | 0.1600 | 0.1646 | -0.0045 |
| 5actor | 0.68 | 0.1652 | 0.1796 | -0.0145 |
| 10actor | 0.59 | 0.1599 | 0.1665 | -0.0065 |
| 3actor | 0.59 | 0.1853 | 0.1909 | -0.0056 |
| 5actor | 0.59 | 0.1542 | 0.1623 | -0.0081 |
| 10actor | 0.57 | 0.1813 | 0.1896 | -0.0084 |
| 3actor | 0.57 | 0.1729 | 0.1738 | -0.0009 |
| 5actor | 0.57 | 0.1532 | 0.1577 | -0.0046 |
| 10actor | 0.68 | 0.1796 | 0.1810 | -0.0014 |
| 3actor | 0.68 | 0.2185 | 0.2065 | +0.0120 |
| 5actor | 0.68 | 0.1906 | 0.2089 | -0.0183 |
| 10actor | 0.82 | 0.1644 | 0.1673 | -0.0029 |
| 3actor | 0.82 | 0.1657 | 0.1668 | -0.0012 |
| 5actor | 0.82 | 0.1396 | 0.1389 | +0.0008 |
| 10actor | 0.91 | 0.1659 | 0.1727 | -0.0068 |
| 3actor | 0.91 | 0.1714 | 0.1824 | -0.0111 |
| 5actor | 0.91 | 0.1469 | 0.1558 | -0.0089 |
| 10actor | 0.91 | 0.1726 | 0.1783 | -0.0057 |
| 3actor | 0.91 | 0.1522 | 0.1611 | -0.0089 |
| 5actor | 0.91 | 0.1661 | 0.1707 | -0.0046 |
| 10actor | 0.48 | 0.1830 | 0.1925 | -0.0096 |
| 3actor | 0.48 | 0.2016 | 0.1966 | +0.0051 |
| 5actor | 0.48 | 0.1911 | 0.2014 | -0.0103 |
| 10actor | 0.82 | 0.1560 | 0.1661 | -0.0101 |
| 3actor | 0.82 | 0.1343 | 0.1560 | -0.0217 |
| 5actor | 0.82 | 0.1872 | 0.1842 | +0.0030 |
| 10actor | 0.59 | 0.1595 | 0.1624 | -0.0028 |
| 3actor | 0.59 | 0.1482 | 0.1635 | -0.0153 |
| 5actor | 0.59 | 0.1675 | 0.1732 | -0.0057 |
| 10actor | 1.00 | 0.1720 | 0.1782 | -0.0062 |
| 3actor | 1.00 | 0.1820 | 0.1860 | -0.0040 |
| 5actor | 1.00 | 0.1885 | 0.1941 | -0.0056 |
| 10actor | 0.85 | 0.1947 | 0.1948 | -0.0001 |
| 3actor | 0.85 | 0.1687 | 0.1741 | -0.0055 |
| 5actor | 0.85 | 0.1729 | 0.1822 | -0.0093 |
| 10actor | 1.00 | 0.1751 | 0.1739 | +0.0011 |
| 3actor | 1.00 | 0.1765 | 0.1949 | -0.0184 |
| 5actor | 1.00 | 0.1521 | 0.1649 | -0.0128 |
| 10actor | 0.66 | 0.1860 | 0.1886 | -0.0026 |
| 3actor | 0.66 | 0.1753 | 0.1889 | -0.0136 |
| 5actor | 0.66 | 0.2094 | 0.2027 | +0.0067 |

## Influence Attribution: Who Drove Key Decisions?

### Decision Points Detected: 841 across 120 engine runs (mean 7.01/run)

| Decision Type | Count | Mean Influence Concentration |
|---------------|-------|------------------------------|
| trait_drift_spike | 826 | 0.448 |
| sentiment_flip | 15 | 0.377 |

### Sample Decision Traces

> **actor_3** at turn 13 (): sentiment_flip
> actor_3 sentiment toward actor_1 flipped: positive → negative
> - actor_2: score=0.372 — 
> - actor_1: score=0.289 — 
> actor_3: actor_3 sentiment toward actor_1 flipped: positive → negative. actor_2 (score=0.37, key signal: trait pull) actor_1 (score=0.29, key signal: trait pull)

> **actor_3** at turn 13 (): sentiment_flip
> actor_3 sentiment toward actor_2 flipped: positive → negative
> - actor_2: score=0.372 — 
> - actor_1: score=0.289 — 
> actor_3: actor_3 sentiment toward actor_2 flipped: positive → negative. actor_2 (score=0.37, key signal: trait pull) actor_1 (score=0.29, key signal: trait pull)

> **actor_2** at turn 8 (): sentiment_flip
> actor_2 sentiment toward actor_1 flipped: negative → positive
> - actor_1: score=0.359 — 
> - actor_3: score=0.133 — 
> actor_2: actor_2 sentiment toward actor_1 flipped: negative → positive. actor_1 (score=0.36, key signal: trait pull) actor_3 (score=0.13, key signal: trait pull)


## Statistical Significance: engine_dialogue_only vs naive

| Metric | engine_dialogue_only (n=120) | naive (n=120) | Delta | p-value | Cohen's d | Sig? |
|--------|----|----|----|----|----|----|
| Persona Drift MAE | 0.1700 | 0.1793 | -0.0093 | 0.0001 | -0.522 | Yes |
| Relationship Inconsistency | 0.0914 | 0.0882 | +0.0032 | 0.8958 | +0.017 | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |
| Envelope Violations | 2.0731 | 2.2586 | -0.1856 | 0.0001 | -0.519 | Yes |
| Action Convergence | 0.7197 | 0.0000 | +0.7197 | 0.0000 | +4.202 | Yes |
| Role Diversity | 0.5031 | 0.0000 | +0.5031 | 0.0000 | +3.813 | Yes |
| Dialogue Coherence | 0.1057 | 0.0807 | +0.0250 | 0.0000 | +1.446 | Yes |
| Repetition Rate | 0.0021 | 0.0000 | +0.0021 | 0.1564 | +0.183 | No |
| Topic Drift Rate | 0.5080 | 0.5450 | -0.0370 | 0.1845 | -0.171 | No |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |

## Per-Trait Error: engine_dialogue_only vs naive

| Trait | Engine | Naive | Delta | p-value | Calibration |
|-------|--------|-------|-------|---------|-------------|
| O | 0.1637 | 0.1829 | -0.0192 | 0.0001 | Static |
| C | 0.2208 | 0.2255 | -0.0046 | 0.3300 | Dynamic |
| E | 0.1291 | 0.1483 | -0.0191 | 0.0004 | Dynamic |
| A | 0.1652 | 0.1712 | -0.0060 | 0.2593 | Dynamic |
| N | 0.1712 | 0.1686 | +0.0026 | 0.5689 | Dynamic |

## Statistical Significance: engine_dialogue_only vs naive_informed

| Metric | engine_dialogue_only (n=120) | naive_informed (n=120) | Delta | p-value | Cohen's d | Sig? |
|--------|----|----|----|----|----|----|
| Persona Drift MAE | 0.1700 | 0.1725 | -0.0025 | 0.2437 | -0.151 | No |
| Relationship Inconsistency | 0.0914 | 0.1132 | -0.0218 | 0.4001 | -0.109 | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |
| Envelope Violations | 2.0731 | 2.1561 | -0.0831 | 0.0843 | -0.223 | No |
| Action Convergence | 0.7197 | 0.7197 | +0.0000 | 1.0000 | +0.000 | No |
| Role Diversity | 0.5031 | 0.4971 | +0.0060 | 0.8008 | +0.033 | No |
| Dialogue Coherence | 0.1057 | 0.0931 | +0.0126 | 0.0000 | +0.691 | Yes |
| Repetition Rate | 0.0021 | 0.0044 | -0.0023 | 0.3453 | -0.122 | No |
| Topic Drift Rate | 0.5080 | 0.5380 | -0.0300 | 0.2909 | -0.136 | No |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |

## Per-Trait Error: engine_dialogue_only vs naive_informed

| Trait | Engine | Naive | Delta | p-value | Calibration |
|-------|--------|-------|-------|---------|-------------|
| O | 0.1637 | 0.1722 | -0.0085 | 0.0844 | Static |
| C | 0.2208 | 0.2232 | -0.0024 | 0.6227 | Dynamic |
| E | 0.1291 | 0.1312 | -0.0021 | 0.6457 | Dynamic |
| A | 0.1652 | 0.1660 | -0.0008 | 0.8762 | Dynamic |
| N | 0.1712 | 0.1699 | +0.0012 | 0.7877 | Dynamic |

## Statistical Significance: naive_informed vs naive

| Metric | naive_informed (n=120) | naive (n=120) | Delta | p-value | Cohen's d | Sig? |
|--------|----|----|----|----|----|----|
| Persona Drift MAE | 0.1725 | 0.1793 | -0.0068 | 0.0022 | -0.396 | Yes |
| Relationship Inconsistency | 0.1132 | 0.0882 | +0.0250 | 0.3238 | +0.127 | No |
| Commitment Contradiction | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |
| Envelope Violations | 2.1561 | 2.2586 | -0.1025 | 0.0383 | -0.268 | Yes |
| Action Convergence | 0.7197 | 0.0000 | +0.7197 | 0.0000 | +4.202 | Yes |
| Role Diversity | 0.4971 | 0.0000 | +0.4971 | 0.0000 | +3.840 | Yes |
| Dialogue Coherence | 0.0931 | 0.0807 | +0.0124 | 0.0000 | +0.680 | Yes |
| Repetition Rate | 0.0044 | 0.0000 | +0.0044 | 0.0256 | +0.289 | Yes |
| Topic Drift Rate | 0.5380 | 0.5450 | -0.0070 | 0.8035 | -0.032 | No |
| Fallback Rate | 0.0000 | 0.0000 | +0.0000 | 1.0000 | +0.000 | No |

## Per-Trait Error: naive_informed vs naive

| Trait | Engine | Naive | Delta | p-value | Calibration |
|-------|--------|-------|-------|---------|-------------|
| O | 0.1722 | 0.1829 | -0.0107 | 0.0269 | Static |
| C | 0.2232 | 0.2255 | -0.0022 | 0.6415 | Dynamic |
| E | 0.1312 | 0.1483 | -0.0170 | 0.0013 | Dynamic |
| A | 0.1660 | 0.1712 | -0.0052 | 0.3230 | Dynamic |
| N | 0.1699 | 0.1686 | +0.0013 | 0.7688 | Dynamic |

## Actor Count x Condition Scaling

| Actors | Condition | n | Drift | Envelope | Convergence | Diversity | Coherence | Repetition | Topic Drift |
|--------|-----------|---|-------|----------|-------------|-----------|-----------|------------|-------------|
| 3 | engine_dialogue_only | 40 | 0.1713 | 2.0667 | 0.6125 | 0.6642 | 0.1091 | 0.0063 | 0.4591 |
| 3 | naive | 40 | 0.1814 | 2.2333 | 0.0000 | 0.0000 | 0.0832 | 0.0000 | 0.5273 |
| 3 | naive_informed | 40 | 0.1749 | 2.0583 | 0.6125 | 0.6451 | 0.0974 | 0.0063 | 0.5455 |
| 5 | engine_dialogue_only | 40 | 0.1683 | 1.9650 | 0.7042 | 0.5229 | 0.1058 | 0.0000 | 0.5036 |
| 5 | naive | 40 | 0.1784 | 2.2050 | 0.0000 | 0.0000 | 0.0783 | 0.0000 | 0.5089 |
| 5 | naive_informed | 40 | 0.1698 | 2.1250 | 0.7042 | 0.5156 | 0.0888 | 0.0028 | 0.5071 |
| 10 | engine_dialogue_only | 40 | 0.1703 | 2.1875 | 0.8425 | 0.3221 | 0.1022 | 0.0000 | 0.5614 |
| 10 | naive | 40 | 0.1781 | 2.3375 | 0.0000 | 0.0000 | 0.0807 | 0.0000 | 0.5989 |
| 10 | naive_informed | 40 | 0.1728 | 2.2850 | 0.8425 | 0.3304 | 0.0932 | 0.0042 | 0.5614 |

### Drift Slope (10-actor minus 3-actor):

- engine_dialogue_only: -0.0010
- naive: -0.0033
- naive_informed: -0.0021
