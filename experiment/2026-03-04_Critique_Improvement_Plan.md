# Improvement Plan: Addressing 10 Research Design Critiques

**Date:** 2026-03-04
**Branch:** V4
**Status:** Awaiting approval

---

## Background

The V4 experiment pipeline has been fully implemented and pilot-tested (5 pilots, 4 sessions each). Results show strong behavioral differentiation (confidence 0.71-0.89) and clear profile separation (Assertive Leader: 51.6 words/turn, 0 hedges vs Passive Avoider: 26.4 words/turn, 9 hedges). However, 10 critiques identify methodological weaknesses that must be addressed before the full experiment run.

This plan categorizes each critique as **FIX** (code change required), **ACK** (document as limitation), or **FIX+ACK** (partial fix + document remainder).

---

## Critique 1: Instruction-Evaluation Phrase Leakage (FIX — Priority 1)

### Problem
The behavioral instructions in `profiles.py` use example phrases like `"what if we tried..."`, `"I'm not sure..."`, `"I disagree"` that directly overlap with the evaluator's detection phrase lists in `behavioral_features.py` (HEDGE_PHRASES, DISAGREEMENT_PHRASES, etc.). This means we're measuring **instruction-following**, not personality — the candidate parrots the prompted phrases, the evaluator detects them, and we get artificially high correlation.

### Justification
This is the single most serious methodological threat. If the candidate uses "I disagree" because the instruction literally says "Use phrases like 'I disagree'" and the evaluator counts "i disagree" in DISAGREEMENT_PHRASES, the correlation between assigned and inferred A is a trivial circular artifact. Fixing this is essential for any claim of behavioral fidelity.

**Citations:** [R1], [R2], [R13]

### Solution
Rewrite all 25 behavioral instruction blocks in `experiment/profiles.py` to describe **behavioral tendencies** without providing exact phrases. The instructions should specify *what* to do, not *how to say it*.

**Example — Low Agreeableness (current):**
```
Use phrases like 'I disagree', 'No, that won't work', 'That's the wrong approach'
```

**Example — Low Agreeableness (fixed):**
```
When you encounter ideas you find flawed, state your objections directly.
Point out specific weaknesses in proposals. Assert your own position even
when it creates tension. Prioritize being correct over being liked.
```

### Files Modified
- `experiment/profiles.py` — All 25 instruction blocks (5 levels x 5 traits)

### Verification
- After rewriting, grep for any phrase that appears in both `profiles.py` and `behavioral_features.py` phrase lists — there should be **zero overlap**
- Run `python3 -c "from experiment.profiles import BEHAVIORAL_INSTRUCTIONS; from experiment.behavioral_features import *; ..."` overlap check script

---

## Critique 2: Weak Conscientiousness Features (FIX — Priority 2)

### Problem
The C formula in `rule_based_evaluator.py` relies on `planning_count` (0.30) and `conditional_ratio` (0.25) — both detect forward-looking language but miss **backward references** (referencing earlier points), **structure markers** (numbered lists, explicit ordering), and **action items** (assigning tasks, setting deadlines). The High C instruction says "follow through on earlier points" and "hold others accountable" but there's no feature to detect either behavior.

### Justification
Conscientiousness is fundamentally about *systematic follow-through*. Our current features only capture *future-oriented planning* language, missing the behavioral core of C: tracking commitments, referencing prior agreements, and creating structured outputs. The pilot data confirms this gap — C scores show lower differentiation than E or N.

**Citations:** [R12], [R14], [R13]

### Solution
Add 3 new features to `behavioral_features.py` and update the C formula in `rule_based_evaluator.py`.

**New features:**
| Feature | Detection | Signal |
|---------|-----------|--------|
| `structure_marker_count` | Numbered items ("1.", "2."), "first...second...third", explicit lists | +C |
| `reference_back_count` | "as we discussed", "earlier you mentioned", "going back to", "we agreed" | +C |
| `action_item_count` | "who will", "by when", "let's assign", "responsible for", "deadline" | +C |

**Updated C formula:**
```
C = 0.20 * planning_count
  + 0.20 * structure_marker_count     (NEW)
  + 0.20 * conditional_ratio
  + 0.15 * reference_back_count       (NEW)
  + 0.10 * action_item_count          (NEW)
  + 0.15 * inv(emotional_word_count)
```

### Files Modified
- `experiment/behavioral_features.py` — Add 3 new fields + phrase lists + extraction logic
- `evaluation/rule_based_evaluator.py` — Update C formula weights, add calibration
- `evaluation/trait_evaluator.py` — Pass new features in evaluation prompt

### Verification
- High-C profiles (assertive_leader C=0.8, anxious_perfectionist C=0.9) should have higher structure_marker_count and reference_back_count than low-C profiles

---

## Critique 3: Feature-Instruction Mismatch (FIX — Priority 3)

### Problem
Several instructed behaviors have no corresponding detection features:
- **Openness**: Instructions say "explore hypothetical scenarios" but there's no `hypothetical_count` feature
- **Neuroticism**: Instructions say "apologetic tone" and "second-guess decisions" but there's no `apology_count` or `self_doubt_count`
- **Agreeableness**: Instructions mention "direct confrontation" patterns but `disagreement_count` doesn't capture all negation forms

### Justification
If we instruct behaviors we can't measure, those behaviors contribute nothing to the evaluation signal. This creates an asymmetry where some traits are well-instrumented (E has 7+ features) while others are weakly instrumented (N relies heavily on hedge_count alone). The feature set should cover every behavioral dimension that instructions target.

**Citations:** [R9], [R12], [R13]

### Solution
Add 5 new features targeting currently-unmeasured instructed behaviors.

**New features:**
| Feature | Phrase List | Target Trait |
|---------|------------|-------------|
| `hypothetical_count` | "what if", "imagine", "suppose", "hypothetically", "in theory" | +O |
| `apology_count` | "sorry", "I apologize", "my fault", "I shouldn't have" | +N |
| `self_doubt_count` | "I'm probably wrong", "I don't know if", "am I making sense", "this might be stupid" | +N |
| `negation_count` | "no", "not", "won't", "can't", "shouldn't", "don't" (context-aware) | -A |
| `reassurance_seeking_count` | "does that make sense?", "is that okay?", "what do you think?", "right?" | +N |

**Updated trait formulas:**
- O: Add hypothetical_count (0.15), reduce question_ratio to 0.10
- N: Add apology_count (0.10), self_doubt_count (0.10), reassurance_seeking_count (0.10), reduce hedge_count to 0.15
- A: Add negation_count as negative signal (0.10), reduce name_mention_count to 0.10

### Files Modified
- `experiment/behavioral_features.py` — Add 5 new fields + phrase lists + extraction
- `evaluation/rule_based_evaluator.py` — Update O, N, A formulas
- `evaluation/trait_evaluator.py` — Pass new features in prompt

### Verification
- High-N profiles (anxious_perfectionist N=0.9) should show elevated apology_count and self_doubt_count
- High-O profiles should show elevated hypothetical_count

---

## Critique 4: Independent Trait Interactions (FIX+ACK — Priority 5)

### Problem
Each trait instruction is generated independently, but certain combinations create contradictions:
- **High C + High N**: "Be highly organized" + "Show stress signals through hedging" = contradictory (organized people don't typically hedge)
- **Low A + High A**: Can't happen, but Low A + High E can create "aggressive leader" vs "friendly challenger" ambiguity
- **High O + Low C**: "Explore creative ideas" + "Don't create plans" = natural synergy, but the instructions don't acknowledge this

### Justification
Real human personalities have trait interactions — conscientiousness moderates how neuroticism manifests (anxious but organized vs. anxious and scattered). Ignoring interactions means some profiles produce incoherent instructions. However, modeling all interactions creates a combinatorial explosion (5! = 120 interaction pairs at 5 levels each).

**Citations:** [R10], [R11]

### Solution
Add a **cross-trait interaction paragraph** to `build_system_prompt()` in `profiles.py` for the 4 most problematic combinations:

1. **High C + High N**: "Your anxiety manifests as over-preparation and excessive checking, not as disorganization. You worry about missing details, not about lacking structure."
2. **High E + Low A**: "You are socially dominant but not warm. You speak frequently and assertively, but to advance your own agenda, not to build consensus."
3. **High O + Low C**: "You freely generate creative ideas but don't follow through with structured plans. You jump between concepts without organizing them."
4. **Low E + High A**: "You are quiet but supportive. When you do speak, it's to agree, validate, or gently mediate — not to lead or propose."

**ACK portion**: Document in the research design that full trait interaction modeling is beyond scope, and that the 4 targeted interactions address the most likely contradictions.

### Files Modified
- `experiment/profiles.py` — Add `_get_interaction_notes()` method, call from `build_system_prompt()`
- `2026-03-03_Research_Design_Refined.md` — Add limitation note about untreated interactions

### Verification
- Anxious Perfectionist (C=0.9, N=0.9) transcript should show organized-anxiety behavior, not scattered behavior
- Check that interaction notes don't contradict individual trait instructions

---

## Critique 5: Null Moderate Instructions (FIX+ACK — Priority 4)

### Problem
Moderate-level instructions (0.4-0.59) say things like "You have a balanced approach" and "neither particularly X nor Y." This gives the LLM no specific behavioral guidance, causing it to fall back to its default conversational style. Since RLHF-trained LLMs default to being helpful and agreeable, the "moderate" baseline is not truly neutral — it's biased toward high A, moderate E, and low N.

### Justification
If moderate = LLM default, then moderate profiles will all produce similar behavior regardless of which trait is moderate. This undermines RQ1 (fidelity) because the moderate band of the scale (0.4-0.6) becomes unmeasurable. The Neutral Observer (all 0.5) would be a key test case — its output should differ from Baseline A (no personality), but with current instructions it may be identical.

**Citations:** [R6], [R7], [R10]

### Solution
Rewrite all 5 moderate-level instructions to be **actively descriptive** — describing specific behavioral patterns that are clearly between high and low.

**Example — Moderate Openness (current):**
```
You have a balanced approach to new ideas. You consider creative suggestions
from others but don't strongly push for unconventional approaches yourself.
```

**Example — Moderate Openness (fixed):**
```
You engage with creative ideas when they come up but typically redirect
discussions toward practical applications. If someone suggests something
unconventional, you might say the equivalent of "interesting idea, but
how would that work in practice?" You neither champion novel approaches
nor dismiss them.
```

Note: The fixed version describes observable behaviors ("redirect toward practical applications", ask about practicality) rather than making empty statements about balance.

**ACK portion**: Document that moderate-level detection is inherently harder because the behavioral signal is weaker, and that moderate-level accuracy will likely be lower than extreme-level accuracy across all evaluation methods.

### Files Modified
- `experiment/profiles.py` — Rewrite all 5 "Moderate" instruction blocks
- `2026-03-03_Research_Design_Refined.md` — Note on moderate-level measurement difficulty

### Verification
- Run Neutral Observer (0.5, 0.5, 0.5, 0.5, 0.5) and Baseline A side by side — transcripts should show meaningfully different behavior
- Moderate-level profiles should produce features that fall between high and low extremes

---

## Critique 6: RQ3 Phase-Content Confound (ACK+analysis — Priority 8)

### Problem
The temporal decay analysis (RQ3) compares Early (introduction/exploration) vs Peak (conflict/defense) vs Late (resolution/closing) windows. But these windows differ in **both** time AND content. If personality signals change across windows, we can't distinguish temporal decay from the fact that introductions naturally elicit different behaviors than conflict phases.

### Justification
This is a fundamental confound in any sequential group discussion design. True temporal decay would require repeating the same discussion phase at different time points, which would make the conversation unrealistic. The confound is inherent to the methodology.

**Citations:** [R8], [R11]

### Solution
**ACK**: Document the confound explicitly in the research design. Add a **phase-normalized analysis** to `analysis.py` that:

1. Reports per-window results with the caveat that content and time are confounded
2. Computes a **content-adjusted delta** by comparing behavior in the same phase type across different positions (e.g., conflict phase in scenario A starts at turn 5 vs. scenario B at turn 8)
3. Acknowledges that RQ3 results should be interpreted as "phase-specific fidelity" rather than pure "temporal decay"

### Files Modified
- `experiment/analysis.py` — Add `phase_content_caveat` to RQ3 report section
- `2026-03-03_Research_Design_Refined.md` — Expand RQ3 limitations discussion

### Verification
- Report explicitly states the confound
- If cross-scenario phase comparison is possible, include it as supplementary analysis

---

## Critique 7: Weak Neuroticism Elicitation (ACK — Priority 9)

### Problem
Group discussions may not create enough pressure to elicit strong neuroticism signals. The Alex agent challenges the candidate, but these are professional disagreements, not personal attacks or high-stakes crises. High-N behaviors like apologizing, hedging under stress, and showing visible anxiety may be suppressed by the LLM's RLHF training even when instructed.

### Justification
This is partially addressed by Critique 3 (adding apology/self-doubt/reassurance-seeking features). The elicitation gap is an inherent limitation of the group discussion format — genuine anxiety requires genuine stakes, which a simulated discussion cannot provide. This parallels the Agreeableness limitation: LLMs are trained to be calm and helpful, making high-N hard to generate.

**Citations:** [R6], [R7], [R9]

### Solution
**ACK**: Document alongside the Agreeableness limitation (Appendix D) as part of the broader "RLHF bias" discussion. Note that N was the second-most affected trait after A.

The new features from Critique 3 (apology_count, self_doubt_count, reassurance_seeking_count) partially mitigate the *detection* side, even if the *generation* side remains constrained.

### Files Modified
- `2026-03-03_Research_Design_Refined.md` — Expand RLHF limitation to cover N alongside A

### Verification
- High-N profiles (anxious_perfectionist N=0.9, passive_avoider N=0.7) should show elevated apology/hedge/self-doubt counts relative to low-N profiles

---

## Critique 8: Meta-Cognitive Prompt Structure (ACK — Priority 9)

### Problem
The system prompt shows trait labels and numeric scores directly:
```
**Extraversion** (High, 0.9):
You are highly extraverted...
```
This may cause the LLM to reason *about* extraversion rather than *behave* extravertedly — a meta-cognitive effect where the model optimizes for matching the label rather than naturally expressing the behavior.

### Justification
Removing labels entirely (instruction-only, no trait names) would test whether behavior changes. However, this is an **experiment design choice**, not a bug: the prompt structure tests whether personality instructions (including labels) produce faithful behavior. A label-free condition would be a separate experiment (could be added as Baseline C in future work).

**Citations:** [R10], [R11]

### Solution
**ACK**: Document as a design choice with trade-offs. Note that:
1. Labels provide the LLM with additional context that may improve behavioral fidelity
2. Labels may also cause "trait optimization" (meta-cognitive behavior)
3. A future experiment could add Baseline C: "same behavioral instructions, no trait labels" to isolate the effect
4. Rule 2 in the prompt already prohibits mentioning trait names in output

### Files Modified
- `2026-03-03_Research_Design_Refined.md` — Add discussion of meta-cognitive prompt effects

### Verification
- N/A for code changes. Future work recommendation only.

---

## Critique 9: Profile Space Positivity Bias (FIX+ACK — Priority 6)

### Problem
The 12 profiles have a positivity bias: most have more high traits than low ones. Only 2 profiles have multiple low traits (creative_rebel: C=0.3, A=0.3; defensive_contrarian: O=0.3, A=0.2). No profile has a configuration like (O=0.3, C=0.4, E=0.2, A=0.2, N=0.8) — a "withdrawn, disagreeable, anxious, conventional" personality that would stress-test the system's ability to produce and detect multiple simultaneous low scores.

### Justification
If the system only works well for profiles with mostly high traits, it may simply be reflecting the LLM's RLHF baseline (which is naturally high-A, moderate-E, low-N). Adding a "mostly-low" profile tests whether the system can produce genuinely negative personality expressions across multiple traits simultaneously.

**Citations:** [R7], [R8], [R9]

### Solution
Add a 13th profile: **Withdrawn Critic**

```python
("withdrawn_critic", "Withdrawn Critic", "socially_challenging", 0.3, 0.4, 0.2, 0.2, 0.8)
```

This profile has 4 traits in the low/moderate-low range and 1 high (N). It tests:
- Simultaneous low E + low A (quiet AND disagreeable — rare combination)
- Low O + High N (conventional and anxious)
- Whether the generation model can produce behavior that is uniformly "negative"

**ACK portion**: Document that even with 13 profiles, the profile space is a sparse sampling of the 5-dimensional OCEAN space (0.0-1.0)^5. Full coverage would require 5^5 = 3125 profiles at 5 levels per trait.

### Files Modified
- `experiment/profiles.py` — Add 13th profile to `_PROFILE_DEFS`
- `experiment/batch_runner.py` — May need to update pilot profile selection if hardcoded
- `2026-03-03_Research_Design_Refined.md` — Update Table 3.2 and profile count references

### Verification
- Run pilot with withdrawn_critic profile
- Verify transcript shows: brief responses, direct criticism, conventional thinking, visible anxiety
- Verify inferred E < 0.3, A < 0.3 (tests whether the system can produce multiple low scores)

---

## Critique 10: Evaluator Positivity Bias (ACK+analysis — Priority 7)

### Problem
LLM evaluators trained with RLHF may systematically score high on "positive" traits (A, C, E) and low on "negative" traits (N). This is separate from the instruction-level leakage (Critique 1) — even with decontaminated instructions, the evaluator may still inflate scores due to its training bias.

### Justification
The pilot data supports this: across all 4 pilot sessions, A is consistently overestimated by +0.25-0.45. The rule-based evaluator provides a bias-free comparison, but we need an explicit analysis that quantifies the direction and magnitude of evaluator positivity bias.

**Citations:** [R1], [R2], [R3], [R4], [R5]

### Solution
Add `positivity_bias_analysis()` to `analysis.py` that:

1. Computes per-trait **signed error** (inferred - assigned) averaged across all main sessions
2. Tests whether the signed error is significantly different from 0 (one-sample t-test)
3. Compares LLM signed error vs rule-based signed error to isolate LLM-specific bias
4. Reports a "bias profile": which traits are systematically over/under-estimated

**Expected output format:**
```
| Trait | LLM Bias  | Rule-Based Bias | LLM-Specific Bias |
|-------|-----------|-----------------|-------------------|
| O     | -0.08     | -0.05           | -0.03             |
| C     | +0.05     | +0.02           | +0.03             |
| E     | -0.02     | +0.01           | -0.03             |
| A     | +0.35*    | +0.10           | +0.25*            |
| N     | -0.10     | -0.05           | -0.05             |
```

### Files Modified
- `experiment/analysis.py` — Add `positivity_bias_analysis()` function and integrate into report

### Verification
- After full experiment run, check that A and N show the largest LLM-specific bias
- Verify that rule-based evaluator shows lower bias than LLM ensemble

---

## Implementation Phases

### Phase 1: Instruction Decontamination (Critiques 1, 5)
**Files:** `experiment/profiles.py`
**Effort:** Medium — requires careful rewriting of 25 instruction blocks + 5 moderate blocks
**Depends on:** Nothing

1. Rewrite all 25 behavioral instruction blocks to remove example phrases
2. Rewrite all 5 moderate-level instructions to be actively descriptive
3. Run overlap check: zero shared phrases between profiles.py and behavioral_features.py

### Phase 2: Feature Expansion (Critiques 2, 3)
**Files:** `experiment/behavioral_features.py`, `evaluation/rule_based_evaluator.py`, `evaluation/trait_evaluator.py`
**Effort:** Medium — add 8 new features (3 for C, 5 for general)
**Depends on:** Nothing (parallel with Phase 1)

1. Add 8 new fields to BehavioralFeatures dataclass
2. Add 8 new phrase lists
3. Update extraction logic
4. Update C, O, N, A formulas in rule_based_evaluator.py
5. Update evaluation prompt in trait_evaluator.py to pass new features

### Phase 3: Cross-Trait Interactions + Profile Addition (Critiques 4, 9)
**Files:** `experiment/profiles.py`, `experiment/batch_runner.py`
**Effort:** Small
**Depends on:** Phase 1 (interaction notes complement rewritten instructions)

1. Add `_get_interaction_notes()` method to profiles.py
2. Call from `build_system_prompt()` to append interaction paragraphs
3. Add 13th profile (Withdrawn Critic) to `_PROFILE_DEFS`

### Phase 4: Pilot Re-Run
**Effort:** Small (automated, ~15 min)
**Depends on:** Phases 1-3

1. Clear old results: `rm experiment/results/session_*.json`
2. Run pilot: `python3 -m experiment.run_experiment --pilot`
3. Verify: no phrase overlap, new features populated, interaction notes in transcripts

### Phase 5: Analytical Additions (Critiques 6, 10)
**Files:** `experiment/analysis.py`
**Effort:** Small
**Depends on:** Phase 4 (needs new data format)

1. Add `positivity_bias_analysis()` function
2. Add phase-content caveat text to RQ3 report
3. Integrate both into `generate_report()` and `run_full_analysis()`

### Phase 6: Documentation Updates (Critiques 6, 7, 8)
**Files:** `2026-03-03_Research_Design_Refined.md`
**Effort:** Small
**Depends on:** All phases

1. Expand RLHF limitation section to cover N alongside A
2. Add meta-cognitive prompt structure discussion
3. Add phase-content confound discussion to RQ3
4. Update profile count (12 -> 13) and Table 3.2
5. Document cross-trait interaction approach and limitations

---

## Files Summary

**Modified files (6):**
| File | Changes | Critiques |
|------|---------|-----------|
| `experiment/profiles.py` | Rewrite 30 instruction blocks, add interaction notes, add 13th profile | 1, 4, 5, 9 |
| `experiment/behavioral_features.py` | Add 8 new features + phrase lists | 2, 3 |
| `evaluation/rule_based_evaluator.py` | Update C, O, N, A formulas with new features | 2, 3 |
| `evaluation/trait_evaluator.py` | Pass 8 new features in evaluation prompt | 2, 3 |
| `experiment/analysis.py` | Add positivity_bias_analysis(), phase-content caveat | 6, 10 |
| `2026-03-03_Research_Design_Refined.md` | Limitation discussions, profile updates | 4, 6, 7, 8, 9 |

**No new files required.**

---

## Verification Checklist

After all phases:

1. **Phrase overlap test**: Zero phrases shared between `profiles.py` instructions and `behavioral_features.py` phrase lists
2. **Feature count**: BehavioralFeatures dataclass has 30 fields (22 existing + 8 new)
3. **Profile count**: 13 profiles in EXPERIMENT_PROFILES
4. **Pilot run**: All 4 sessions complete with new features populated in JSON output
5. **Withdrawn Critic**: Produces transcript with brief, critical, anxious behavior; inferred E < 0.3, A < 0.3
6. **Interaction notes**: Anxious Perfectionist transcript shows organized-anxiety, not scattered behavior
7. **Positivity bias analysis**: Report includes per-trait signed error table
8. **Phase caveat**: RQ3 section explicitly states the content-time confound
9. **Documentation**: All ACK items reflected in the research design doc

---

## References (Citation Keys)

- **[R1]** Wang, P. et al. (2023). *Large Language Models are not Fair Evaluators*. arXiv. https://arxiv.org/abs/2305.17926
- **[R2]** Stureborg, R., Alikaniotis, D., & Suhara, Y. (2024). *Large Language Models are Inconsistent and Biased Evaluators*. arXiv. https://arxiv.org/abs/2405.01724
- **[R3]** Shi, L. et al. (2025). *Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge*. arXiv. https://arxiv.org/abs/2406.07791
- **[R4]** Verga, P. et al. (2024). *Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models*. arXiv. https://arxiv.org/abs/2404.18796
- **[R5]** Jung, J., Brahman, F., & Choi, Y. (2024). *Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement*. arXiv. https://arxiv.org/abs/2407.18370
- **[R6]** Wei, J. et al. (2024). *Simple synthetic data reduces sycophancy in large language models*. arXiv. https://arxiv.org/abs/2308.03958
- **[R7]** Salecha, A. et al. (2024). *Large language models display human-like social desirability biases in Big Five personality surveys*. PNAS Nexus, 3(12), pgae533. https://academic.oup.com/pnasnexus/article/3/12/pgae533/7919163
- **[R8]** Li, R. et al. (2025). *How Far are LLMs from Being Our Digital Twins? A Benchmark for Persona-Based Behavior Chain Simulation*. Findings of ACL 2025. https://aclanthology.org/2025.findings-acl.813/
- **[R9]** Lee, S. et al. (2025). *Do LLMs Have Distinct and Consistent Personality? TRAIT: Personality Testset designed for LLMs with Psychometrics*. Findings of NAACL 2025. https://aclanthology.org/2025.findings-naacl.469/
- **[R10]** Jiang, H. et al. (2024). *PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits*. Findings of NAACL 2024. https://aclanthology.org/2024.findings-naacl.229/
- **[R11]** Abdulhai, M. et al. (2025). *Consistently Simulating Human Personas with Multi-Turn Reinforcement Learning*. arXiv. https://arxiv.org/abs/2511.00222
- **[R12]** Mairesse, F., & Walker, M. (2007). *PERSONAGE: Personality Generation for Dialogue*. ACL 2007. https://aclanthology.org/P07-1063/
- **[R13]** Campbell, D. T., & Fiske, D. W. (1959). *Convergent and discriminant validation by the multitrait-multimethod matrix*. Psychological Bulletin, 56(2), 81-105. https://pubmed.ncbi.nlm.nih.gov/13634291/
- **[R14]** Pennebaker, J. W., & King, L. A. (1999). *Linguistic styles: language use as an individual difference*. Journal of Personality and Social Psychology, 77(6), 1296-1312. https://pubmed.ncbi.nlm.nih.gov/10626371/
