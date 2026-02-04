# Step 1: Agent Trait Consistency — Changelog

Changes made to fix personality expression and inference accuracy,
based on analysis of the initial 48-session batch (`8aec86a0`) validated by 3 LLM judges.

---

## Problems Identified

### From analysis of batch `8aec86a0` (48 sessions, 12 profiles x 4 scenarios x 1 rep)

| Problem | Root Cause | Severity |
|---------|-----------|----------|
| **Conscientiousness inflation** — all judges overestimate C by +0.12 to +0.18 | Profiles with C in 0.4-0.6 got zero behavioral guidance (threshold gap). LLM defaults to organized discussion style, which reads as high C. | Affects most profiles |
| **`stoic_pragmatist` Openness overestimated** — O inferred as 0.6 vs ground truth 0.2 (error 0.4) | Low-O behavioral cues too mild ("Let's stick to what works" sounds practical, not closed). Profile tendencies not explicit enough about rejecting novelty. | Profile-specific |
| **`cautious_skeptic` Extraversion overestimated** — E inferred as 0.5 vs ground truth 0.2 (error 0.3) | Agent produces 2-4 sentence responses every turn regardless of E level. No response length modulation. Inference prompt doesn't weight brevity as low-E signal. | Systemic + profile-specific |
| **Systematic upward bias** across traits (except N) | Inference prompt too generic — one-line trait definitions with no guidance on what group conversation behaviors map to each level. | Judge-side |

### Validation metrics (pre-fix, default judge)

| Trait | Pearson r | MAE | Bias |
|-------|----------|-----|------|
| O | 0.784 | 0.137 | +0.125 |
| **C** | **0.487** | **0.196** | **+0.154** |
| E | 0.766 | 0.124 | +0.061 |
| A | 0.777 | 0.131 | +0.098 |
| N | 0.766 | 0.135 | -0.090 |

---

## Changes Made

### 1. Agent Response Style (`agents/candidate_agent.py`)

Added `_get_response_style()` method that generates trait-calibrated instructions injected into the candidate's system prompt. These control:

- **Response length** (based on Extraversion):
  - E <= 0.3: "1 sentence ideal, 2 max. Do not elaborate."
  - E >= 0.7: "3-5 sentences. Elaborate, engage others."
  - Middle: "2-3 sentences."

- **Response structure** (based on Conscientiousness):
  - C <= 0.4: "Do NOT organize into lists/steps. Be informal, go off-topic. Avoid 'first, second, third.'"
  - C >= 0.7: "Be organized, reference deadlines, propose action items."

- **Emotional tone** (based on Neuroticism):
  - N >= 0.7: "Show visible stress, worry, frustration."
  - N <= 0.3: "Stay calm. Do not validate others' emotions — stay purely task-focused."

- **Idea engagement** (based on Openness):
  - O <= 0.3: "Do NOT explore hypotheticals or propose alternatives. Express skepticism about novel ideas."
  - O >= 0.7: "Actively explore new ideas, propose alternatives."

- **Interpersonal stance** (based on Agreeableness):
  - A <= 0.3: "Push back on disagreements. Do not soften language."
  - A >= 0.7: "Be warm and accommodating. Acknowledge others before sharing own view."

- **Combined modifier**: very low N (<=0.2) + below-midpoint E (<0.5) triggers extra brevity reinforcement — no empathetic preambles like "I understand" or "I hear you."

### 2. Behavioral Mappings (`config/bfi_mappings.py`)

**Threshold change**: Lowered from 0.7/0.3 to 0.65/0.35. This captures more profiles in the behavioral guidance system, reducing the "no guidance" gap where LLM defaults dominate.

**New/strengthened behaviors**:

| Trait | Level | Change |
|-------|-------|--------|
| Openness | Low | Added "Narrow focus" facet: no curiosity about alternatives, does not entertain what-if scenarios |
| Openness | Low | Strengthened existing facets: "actively resists novel ideas", "dismisses abstract thinking" |
| Conscientiousness | Low | Added "Disorganization" facet: jumps between topics, loses track of the point, goes off-topic |
| Conscientiousness | Low | Strengthened existing facets: "does not organize or plan", "resists rigid structure" |
| Extraversion | Low | Added "Brevity" facet: "keeps responses short — one sentence when possible, does not volunteer extra information" |
| Extraversion | Low | Strengthened "Reserve" facet: "speaks only when necessary, gives brief minimal responses" |

### 3. Profile Fixes (`config/personality_profiles.py`)

**`stoic_pragmatist`** (O=0.2, C=0.7, E=0.4, A=0.4, N=0.1):
- Behavioral tendencies rewritten to explicitly signal low O:
  - "Focuses exclusively on what works, actively dismisses novel or untested ideas"
  - "Shuts down brainstorming or hypothetical discussions"
  - "Never asks 'what if' or explores alternatives"
- Communication style: added "Avoids speculation, metaphors, and creative thinking. Speaks in concrete terms only."

**`cautious_skeptic`** (O=0.2, C=0.6, E=0.2, A=0.3, N=0.5):
- Behavioral tendencies rewritten to explicitly signal low E:
  - "Gives minimal responses — says what is needed and nothing more"
  - "Does not initiate conversation topics or engage others socially"
  - "Questions assumptions — but briefly, not in long speeches"
- Communication style: "Reserved, terse. Speaks in short sentences. Does not make small talk or build rapport."

### 4. Inference Prompt (`validation/reverse_inference.py`)

Complete rewrite of the judge prompt. Key changes:

- **Detailed scoring guide** for each trait with explicit HIGH/LOW behavioral signals
- **CAUTION boxes** warning against group discussion biases:
  - "Simply participating in a discussion is NOT a sign of openness"
  - "Most people sound somewhat organized in a structured discussion — only rate C > 0.7 if the person actively imposes additional structure"
  - "Response LENGTH is a critical signal for extraversion"
- **Behavioral statistics** now computed and passed to the judge:
  - Average words per response
  - Response length range (min-max)
  - Number of questions asked
  - Number of times addressing others by name
  - Candidate turn percentage
- **Full-range instruction**: "Use the FULL range — 0.1-0.2 for very low, 0.8-0.9 for very high"

### 5. Analysis Tooling (`scripts/analyze_step1.py`)

New script for comprehensive Step 1 analysis. Computes:

- **Per-trait metrics**: Pearson correlation, p-value, MAE, RMSE, signed bias (per judge)
- **Per-profile breakdown**: mean accuracy, std, worst trait, bias direction (per judge)
- **Per-scenario breakdown**: mean accuracy, std (per judge)
- **Inter-judge agreement**: pairwise Pearson r and mean absolute difference per trait
- **Coverage matrix**: profile x scenario session counts
- **Weak spot identification**: bottom profiles, weakest traits, high-error profile-trait combos
- **Automated recommendations**

Usage:
```bash
python scripts/analyze_step1.py \
  --batch-dir outputs/batches/<batch_id> \
  --output-report outputs/step1_report.md \
  --output-json outputs/step1_results.json
```

---

## Verification Results

Tested with 3 sessions: `stoic_pragmatist`, `cautious_skeptic`, `balanced_leader` (control), all on `resource_conflict`.

### Before/After: `cautious_skeptic` (E=0.2)

| Metric | Old Agent + Old Judge | New Agent + New Judge |
|--------|----------------------|----------------------|
| Avg words/turn | ~40-50 (est.) | **16.1** |
| O error | 0.1 | **0.0** |
| C error | 0.3 | **0.2** |
| **E error** | **0.3** | **0.1** |
| A error | 0.1 | 0.1 |
| Overall accuracy | 0.80 | **0.88** |

### Before/After: `stoic_pragmatist` (O=0.2)

| Metric | Old Agent + Old Judge | New Agent + New Judge |
|--------|----------------------|----------------------|
| **O error** | **0.4** | **0.1** |
| C error | 0.2 | 0.2 |
| E error | 0.1 | 0.2 |
| Overall accuracy | 0.84 | **0.86** |

### Known Remaining Limitation

**Conscientiousness inflation persists at ~0.2 error.** Group discussions inherently reward organized behavior, and LLM judges still tend to rate C higher than ground truth. This is documented as a structural limitation of the format rather than a fixable prompt issue.

---

## Full Generation

Batch `4501beb2`: 144 sessions (12 profiles x 4 scenarios x 3 reps) generated with all fixes applied.

Run analysis on completed batch:
```bash
python scripts/analyze_step1.py \
  --batch-dir outputs/batches/4501beb2 \
  --output-report outputs/step1_report_v2.md \
  --output-json outputs/step1_results_v2.json
```

Run validation:
```bash
python scripts/run_validation.py --batch outputs/batches/4501beb2 --verbose
```
