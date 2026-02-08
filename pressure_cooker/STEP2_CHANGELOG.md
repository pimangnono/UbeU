# Step 2 — Session Changes & Improvements

This document covers all changes made to the Step 2 Live Interview Platform during the UX refinement and robustness iteration session.

---

## Summary of Changes

| Area | Files Changed | Key Improvement |
|------|---------------|-----------------|
| Interview UI | `interview_page.py` | Meeting room layout, speaker targeting, TTS, loading page, data panel |
| Conversation Engine | `live_engine.py` | Case study fast path, smart routing, facilitator behavior |
| API Layer | `server.py`, `models.py` | Target speaker support, timer compensation, error handling |
| Validation | `validator_agent.py` | Rubric anchors, multi-pass scoring |
| Analysis | `aggregate_results.py` (new) | Cross-participant aggregation with CSV, markdown, JSON exports |
| Navigation | `app.py`, `bfi44_page.py` | Sidebar cleanup, scroll-to-top on page transition |
| **Evidence-Based Assessment** | `turn_analyzer.py`, `assessment_builder.py`, `analysis_models.py` | Per-turn analysis with quote extraction, transparent scoring |
| **Smart Agent Workflow** | `smart_agents.py`, `discussion_orchestrator.py` | Competency-targeted challenges, phase-aware speaker selection |
| **SmartLiveEngine** | `live_engine.py` | Integrated smart agents with evidence-based analysis |

---

## 1. Speaker Targeting System

### Problem
In the original design, sending a message always triggered a multi-agent decision loop — the system manager would assess tension, check for interventions, decide the next speaker, and generate a response. This was slow (3-4 LLM calls per turn) and gave the user no control over who responds.

### Solution
Added a targeted-speaker system with two input methods:

**Radio buttons (form-based):**
- 4 options: Everyone, Jordan, Sam, Facilitator
- Wrapped in `st.form` to prevent Streamlit reruns when switching targets mid-typing
- `clear_on_submit=True` resets the form after sending

**@mention parsing:**
- Regex: `^@(jordan|sam|facilitator|everyone)\b\s*` (case-insensitive)
- Overrides radio selection, stripped from displayed message
- `@everyone` resets to normal multi-speaker mode

### Architecture
- `SubmitMessageRequest` gained `target_speaker: Optional[str]` field
- `server.py` passes it to `engine.generate_ai_turns_until_human(target_speaker=...)`
- `live_engine.py` has a targeted-speaker bypass that skips `decide_next_speaker()` entirely and generates only from the specified agent

### Files
- `pressure_cooker/step2/models.py` — Added `target_speaker` field
- `pressure_cooker/step2/server.py` — Passes target to engine
- `pressure_cooker/step2/live_engine.py` — Targeted-speaker bypass (lines 253-290)
- `pressure_cooker/step2/ui/pages/interview_page.py` — Radio buttons + @mention parsing

---

## 2. Case Study Performance Optimization

### Problem
The "Everyone" mode (no target speaker) was significantly slower than direct targeting for case study scenarios. The normal conversation loop made 3-4 sequential LLM calls per turn: tension assessment, intervention check, next speaker decision, and response generation.

### Solution
Added a **case study fast path** in `generate_ai_turns_until_human()` that:
1. Skips tension assessment (uses last known value)
2. Skips intervention check
3. Skips `decide_next_speaker()` — picks colleague directly (alternating Jordan/Sam)
4. Result: **1 LLM call per turn** instead of 3-4

### Smart Routing for Data Questions
When the user sends a message to "Everyone", the engine determines whether it's a data question or a discussion point:
- `submit_human_turn()` runs keyword matching against case study data categories
- Newly revealed categories stored in `_last_newly_revealed`
- If new data categories were matched → route to **Facilitator** (data response)
- Otherwise → route to **colleague** (discussion response)

This avoids the problem of data questions going to Jordan/Sam (who can't provide data) and prevents all generic questions from being routed to the Facilitator.

### Files
- `pressure_cooker/step2/live_engine.py` — Fast path (lines 294-346), `_last_newly_revealed` tracking

---

## 3. Facilitator Behavior Control

### Problem
The Facilitator LLM kept adding directive phrases like:
- "Let's consider how this impacts our channel choice."
- "Would you like the detailed breakdown by hospital as well?"
- "This suggests we should look at..."

This undermined the study design where the **candidate must lead the analysis**.

### Strategy
Progressive prompt strengthening across iterations:

**Iteration 1:** Added "Do NOT ask questions" to context
**Iteration 2:** Added "STRICT RULES" section with NEVER directives
**Iteration 3 (final):** Reframed the Facilitator's identity as a **"DATA CLERK, not a discussion participant"** with exhaustive banned phrase list:

```
- NEVER use directive phrases like 'Let's consider...', 'This suggests...',
  'It's worth noting...', 'This could mean...', 'Keep in mind...'
- Format: 'Here is [data category]: [numbers/facts].' — FULL STOP. Nothing after.
```

### Same approach for colleagues (Jordan/Sam)
Added case study context to both targeted and normal generation paths:
```
"Do NOT propose frameworks, structure, or analytical approaches.
Only react to what the candidate says — challenge weak reasoning,
ask for clarification, or support good points."
```

### Files
- `pressure_cooker/step2/live_engine.py` — `_build_gated_context()` strict rules, colleague case context

---

## 4. Timer Compensation System

### Problem
The 15-minute countdown timer kept ticking during LLM API wait time, which is unfair to the participant since LLM latency (5-30+ seconds per turn) is not under their control.

### Solution — Two-layer compensation

**Backend timer (engine.start_time):**
- `server.py` measures the wall-clock time of each `generate_ai_turns_until_human()` call
- After completion (or on error), shifts `engine.start_time` forward by the API wait duration
- This ensures backend time events (12-min warning, 14-min wrap-up, 15-min hard stop) exclude LLM latency
- Also compensated for `generate_opening()` during session creation

**Frontend timer (JavaScript countdown):**
- `interview_page.py` compensates `st.session_state.interview_start` by the same amount
- The JS timer is computed from `interview_start + 15*60`, so shifting it forward extends the displayed time
- When `waiting_for_response` is True, the timer shows a frozen snapshot with "paused" indicator instead of counting down
- After the response completes and page reruns, the timer resumes with the compensated end time

### Files
- `pressure_cooker/step2/server.py` — `engine.start_time += api_wait` in both success and error paths
- `pressure_cooker/step2/ui/pages/interview_page.py` — JS timer pause state, `interview_start` compensation

---

## 5. Input Locking During AI Response

### Problem
If the user typed and submitted a message while the AI was still generating a response (during the sequential reveal with `time.sleep`), the message was silently lost. Streamlit's form state gets cleared on rerun, and the blocking execution prevented the new submission from being processed.

### Solution — Two-phase message processing

**Phase 1 (submit):** User clicks Send → message saved to `st.session_state.queued_message`, `waiting_for_response = True`, then `st.rerun()`. The page re-renders with:
- Text input **disabled** with placeholder "Waiting for response..."
- Radio buttons **disabled**
- Submit button **disabled** showing "..."

**Phase 2 (process):** On the rerun, the form is visibly locked while the API call + sequential message reveal runs. After completion, `waiting_for_response = False` and `st.rerun()` re-enables the form.

This prevents message loss and makes it clear to the user that input is temporarily blocked.

### Files
- `pressure_cooker/step2/ui/pages/interview_page.py` — Two-phase form handling

---

## 6. Data Panel (Facilitator History)

### Problem
Facilitator data responses (costs, revenue, customer segments) disappeared after the next message, making it impossible to reference earlier data during analysis.

### Strategy
Added a persistent **Data Panel** beside the meeting room showing all facilitator responses:

- Two-column layout: `st.columns([3, 2])` — meeting room (left), data panel (right)
- Scrollable container with fixed max-height (350px) to prevent page expansion
- Each facilitator response displayed as a numbered card ("Data #1", "Data #2", etc.)
- **Real-time updates**: panel refreshes immediately when facilitator speaks (during sequential reveal), not just after rerun
- Newest data at the bottom with auto-scroll

### Files
- `pressure_cooker/step2/ui/pages/interview_page.py` — `_render_data_panel()` helper, two-column layout

---

## 7. Loading Page & Page Transitions

### Problem
When transitioning from BFI-44 to the interview, the user saw all components at once (questionnaire + discussion table + instruction card) without scrolling to top.

### Challenges
- `st.html()` renders in an iframe — JavaScript can't access parent DOM for scrolling
- `stc.html(height=0)` with fixed overlay was invisible (trapped in 0px iframe)
- `st.markdown(unsafe_allow_html=True)` renders in DOM but strips `<script>` tags

### Solution
Combined approach:
1. **Dark background** via `st.markdown` CSS injection (renders in DOM, not iframe)
2. **Scroll-to-top** via `stc.html(height=0)` with JS targeting multiple parent selectors
3. **Single `st.empty()` placeholder** — first shows instruction card, then replaces with sequential meeting room reveal
4. Instruction card with animated design: pulsing icon, spinning loader, "How it works" guidance
5. 4-second display time before transitioning to opening messages

### Files
- `pressure_cooker/step2/ui/pages/interview_page.py` — `_show_loading_and_reveal()`
- `pressure_cooker/step2/ui/pages/bfi44_page.py` — Scroll-to-top before rerun

---

## 8. Browser Text-to-Speech

### Solution
Web Speech API integration injected via `<script>` tags in the meeting room HTML:

- Per-speaker voice settings (pitch/rate): Jordan (lower), Sam (higher), Facilitator (slower)
- `synth.cancel()` before each new utterance prevents overlapping speech
- User's own messages skip TTS
- Toggle in timer row: `st.toggle("Sound")`
- Message display duration adjusts when TTS is enabled (~150 WPM speech vs ~200 WPM reading)

### Files
- `pressure_cooker/step2/ui/pages/interview_page.py` — `TTS_VOICE_SETTINGS`, TTS script in `_build_meeting_html()`

---

## 9. Error Handling & Resilience

### Problem
LLM API timeouts (OpenRouter) caused raw 500 Internal Server errors. The httpx client timeout was too short (60s default).

### Solution
- **Backend**: `server.py` wraps `generate_ai_turns_until_human()` in try/except, returns HTTP 503 with friendly message instead of 500
- **Frontend**: httpx timeout increased to 180s; error handler extracts structured `detail` field from response body; timer compensated even on error
- **Broad exception catching**: `except (httpx.HTTPError, httpx.TimeoutException, Exception)` covers all failure modes

### Files
- `pressure_cooker/step2/server.py` — Error handling with 503 response
- `pressure_cooker/step2/ui/pages/interview_page.py` — Improved error display, timer compensation on error

---

## 10. Sidebar Cleanup

### Problem
Streamlit auto-generated page navigation links (bfi44_page, consent_page, etc.) appeared in the sidebar.

### Solution
CSS injection in `app.py`:
```python
st.markdown(
    "<style>[data-testid='stSidebarNav'] {display:none !important;}</style>",
    unsafe_allow_html=True,
)
```

### Files
- `pressure_cooker/step2/ui/app.py`

---

## 11. Logic Validation — Rubric Anchors & Multi-Pass Scoring

### Problem
The post-session validator (Claude Haiku 4.5) used undefined 1-5 scales for analytical depth and recommendation quality, with no anchoring. Single-pass scoring meant no way to measure consistency.

### Rubric Anchors
Defined 5 explicit levels for each numeric dimension:

**Analytical Depth:**
| Score | Description |
|-------|-------------|
| 1 | No analysis — opinions without reasoning |
| 2 | Surface-level — 1 dimension, some data requests but no root cause connection |
| 3 | Moderate — 2-3 dimensions, some logical connections, significant gaps |
| 4 | Thorough — most dimensions, cross-category data connections, minor gaps |
| 5 | Exceptional — comprehensive framework, non-obvious insights, trade-offs addressed |

**Recommendation Quality:**
| Score | Description |
|-------|-------------|
| 1 | No recommendation or vague direction |
| 2 | Weak — little evidence, doesn't address core problem |
| 3 | Adequate — some data support, lacks specificity |
| 4 | Strong — specific, data-backed, considers risks |
| 5 | Excellent — prioritized, implementation steps, risks and competitive dynamics |

### Multi-Pass Scoring
- **3 independent passes** run concurrently via `asyncio.gather`
- Temperature set to 0.4 (slightly higher to surface genuine scoring variance)
- **Numeric scores**: median across passes
- **Qualitative fields** (assumptions, gaps): union across passes, deduplicated
- **Summary**: taken from the pass closest to median scores
- **Transparency**: output includes `scoring.analytical_depth_scores`, `scoring.depth_agreement` (max-min spread)

### Files
- `pressure_cooker/step2/validator_agent.py` — Full rewrite with rubric, `_aggregate_passes()`, `_run_single_pass()`

---

## 12. Aggregate Analysis Script

### Purpose
Cross-participant analysis for 30+ candidates after the study concludes.

### Outputs

| File | Description |
|------|-------------|
| `participant_summary.csv` | One row per participant — BFI-44, session stats, assessment, validation, survey |
| `all_conversations.csv` | Every turn from every session — for qualitative review |
| `aggregate_report.md` | 8-section markdown report with descriptive statistics |
| `aggregate_data.json` | Machine-readable JSON dump |

### Report Sections
1. Overview (registered, completed, scenario distribution, completion rate)
2. BFI-44 ground truth distribution
3. Session statistics (duration, turns, candidate verbosity)
4. Assessment scores (rule-based: collaboration, leadership, etc.)
5. Intent distribution (candidate turns only)
6. Logic validation with multi-pass agreement stats
7. Post-session survey results
8. Per-participant summary table

### Usage
```bash
python3 step2/evaluation/aggregate_results.py
python3 step2/evaluation/aggregate_results.py --output-dir outputs/step2/analysis
```

### Files
- `pressure_cooker/step2/evaluation/aggregate_results.py` (new)

---

## 13. Evidence-Based Assessment System

### Problem
The original assessment system lacked transparency:
- Intent classification was a single label without reasoning
- Personality inference used formula-based scoring without evidence
- Assessment scores had no audit trail showing which responses contributed to which scores
- No way to trace back why a candidate received specific competency ratings

### Solution — Per-Turn Analysis with Quote Extraction

Created a new evidence-based analysis pipeline that analyzes each candidate turn individually and extracts direct quotes as evidence.

**New Data Models (`utils/analysis_models.py`):**

| Model | Purpose |
|-------|---------|
| `TraitSignal` | Single personality trait observation with quote evidence |
| `ReasoningAssessment` | Logic quality assessment per turn |
| `IntentAnalysis` | Intent with confidence and reasoning |
| `TurnAnalysis` | Complete per-turn analysis combining all above |
| `ScoringEvidence` | Evidence item with quote, turn number, weight |
| `CompetencyScore` | Final competency score with supporting evidence |
| `EvidenceBasedAssessment` | Complete assessment with full audit trail |

**TurnAnalyzer (`pipeline/turn_analyzer.py`):**
- LLM-powered analysis of individual candidate turns
- Extracts exact quotes as evidence for each observation
- Identifies personality trait signals (Big Five) with supporting text
- Assesses reasoning quality (clarity, depth, data usage)
- Detects competency behaviors (collaboration, leadership, problem-solving, etc.)

**AssessmentBuilder (`pipeline/assessment_builder.py`):**
- Aggregates per-turn analyses into final competency scores
- Each score includes list of supporting evidence with:
  - Direct quote from candidate
  - Turn number for reference
  - Behavior type detected
  - Weight based on signal strength

### Example Evidence Trail

```json
{
  "competency_scores": {
    "problem_solving": {
      "score": 0.78,
      "evidence": [
        {
          "quote": "Let me structure this using a profitability framework",
          "turn_number": 1,
          "behavior": "used_framework",
          "weight": 0.8
        },
        {
          "quote": "The SMB segment has a 2.6x LTV:CAC ratio compared to Enterprise at 10x",
          "turn_number": 5,
          "behavior": "used_data",
          "weight": 0.9
        }
      ]
    }
  }
}
```

### Files
- `pressure_cooker/utils/analysis_models.py` — Evidence-based data models
- `pressure_cooker/pipeline/turn_analyzer.py` — Per-turn LLM analysis
- `pressure_cooker/pipeline/assessment_builder.py` — Evidence aggregation
- `pressure_cooker/pipeline/statistics.py` — Integration functions

---

## 14. Smart Agent Workflow

### Problem
The original AI agents (ProvokerAgent, MediatorAgent) had several limitations:
- **Random challenges**: Provoker generated generic challenges without strategic targeting
- **Passive mediation**: Mediator mostly validated the candidate instead of advancing discussion
- **No competency tracking**: No awareness of which competencies had been tested
- **No phase awareness**: Same behavior throughout the 15-minute session

### Solution — Strategic, Phase-Aware Agents

**DiscussionContext (`agents/discussion_orchestrator.py`):**
Shared state object that tracks:
- Current discussion phase (8 phases)
- Turns spent in each phase
- Data categories revealed
- Hypotheses stated
- Tension level
- Competency coverage

**Discussion Phases:**

| Phase | Purpose | Typical Duration |
|-------|---------|------------------|
| OPENING | Introduction, case setup | 1-2 turns |
| PROBLEM_FRAMING | Structure the problem | 2-3 turns |
| HYPOTHESIS_GENERATION | Form initial theories | 2-3 turns |
| DATA_GATHERING | Request and analyze data | 3-5 turns |
| SYNTHESIS | Connect findings | 2-3 turns |
| RECOMMENDATION | Commit to a decision | 2-3 turns |
| STRESS_TEST | Defend under pressure | 2-4 turns |
| CLOSING | Summarize conclusions | 1-2 turns |

**CompetencyCoverageTracker:**
Tracks 21 observable behaviors across 5 competency dimensions:

| Competency | Behaviors Tracked |
|------------|-------------------|
| Collaboration | acknowledged_others, built_on_ideas, resolved_conflict, sought_input |
| Leadership | set_direction, made_decisions, took_initiative, delegated_tasks |
| Problem Solving | used_data, identified_root_cause, used_framework, evaluated_alternatives, synthesized_info |
| Communication | clear_explanations, summarized, asked_clarifying_questions, adapted_style |
| Stress Management | handled_pushback, maintained_composure, adapted_approach, managed_time |

### SmartProvokerAgent (`agents/smart_agents.py`)

**Key improvements:**
- **Competency targeting**: Selects challenges based on untested competencies
- **Phase-appropriate intensity**: Gentle in opening, aggressive in stress test
- **Challenge templates**: Pre-defined provocations mapped to specific behaviors

**Intensity by Phase:**

| Phase | Intensity | Behavior |
|-------|-----------|----------|
| Opening | 0.3 | Measured, diplomatic concerns |
| Problem Framing | 0.4 | Skeptical but professional |
| Hypothesis | 0.5 | Question assumptions |
| Data Gathering | 0.5 | Demand evidence |
| Synthesis | 0.6 | Press for specifics |
| Recommendation | 0.7 | Firm challenges |
| **Stress Test** | **0.9** | Direct confrontation |
| Closing | 0.4 | Final pushback |

**Example targeted challenge for `stress_management.handled_pushback`:**
```
"That's a terrible recommendation. It ignores everything we've discussed."
```

### ActiveMediatorAgent (`agents/smart_agents.py`)

**Key improvements:**
- **Active advancement**: Prompts candidate to move through phases
- **Missing element detection**: Identifies when hypotheses, synthesis, or recommendations are missing
- **Behavior modeling**: Occasionally demonstrates good analytical behavior
- **Bridge building**: Helps candidate respond to provoker challenges

**Phase-specific roles:**

| Phase | Mediator Role |
|-------|---------------|
| Opening | Help frame the discussion |
| Hypothesis | Prompt for hypotheses if none stated |
| Data Gathering | Help connect data to hypotheses |
| Synthesis | Push for cross-category connections |
| Recommendation | Encourage commitment to a decision |
| Stress Test | Bridge between provoker and candidate |

### SmartSystemManager (`agents/smart_agents.py`)

**Strategic speaker selection:**
- Phase-aware: Favors provoker in stress test, mediator when tension is high
- Competency-driven: Routes to provoker when stress_management untested
- Pattern-aware: Prevents same speaker from dominating
- Tension assessment: LLM-based analysis of conversation dynamics

**Speaker selection logic:**
```
After candidate speaks:
├── If STRESS_TEST phase → Provoker
├── If tension > 0.7 → Mediator (de-escalate)
├── If stress_management untested → Provoker
└── Else → Alternate based on recent pattern
```

### Files
- `pressure_cooker/agents/discussion_orchestrator.py` — DiscussionContext, CompetencyCoverageTracker, phase triggers
- `pressure_cooker/agents/smart_agents.py` — SmartProvokerAgent, ActiveMediatorAgent, SmartSystemManager

---

## 15. SmartLiveEngine Integration

### Purpose
Combines the evidence-based assessment system with the smart agent workflow into a single integrated engine.

### SmartLiveEngine (`step2/live_engine.py`)

Extends `LiveEngine` with:
- Smart agent initialization (SmartProvokerAgent, ActiveMediatorAgent, SmartSystemManager)
- Shared DiscussionContext between all agents
- Competency behavior detection on each candidate turn
- Phase advancement logic
- Evidence-based analysis generation on session finalization

### Key Methods

| Method | Purpose |
|--------|---------|
| `get_discussion_phase()` | Current phase name |
| `get_phase_guidance()` | Instructions for current phase |
| `get_competency_coverage()` | Coverage stats for all 5 competencies |
| `get_targeting_info()` | Provoker's current target competency/behavior |
| `get_evidence_assessment()` | Full evidence-based assessment with quotes |

### State Persistence

SmartLiveEngine serializes additional state:
- `discussion_context`: Phase, turns in phase, tension, data revealed, hypotheses
- `competency_coverage`: Per-competency behavior observations with turn numbers and quotes

This enables session recovery with full context preserved.

### Usage

```python
from step2.live_engine import SmartLiveEngine

engine = SmartLiveEngine(
    client=llm_client,
    scenario=scenario,
    participant_name="Jin",
    case_study=case_study,
    use_smart_agents=True,  # Enable smart workflow
)

# Session runs normally...
await engine.generate_opening()
engine.submit_human_turn("Let me analyze the cost structure...")
await engine.generate_ai_turns_until_human()

# On finalization, evidence-based analysis is generated
output = await engine.finalize_session_output("P001")
# output.evidence_assessment contains full audit trail
```

### Files
- `pressure_cooker/step2/live_engine.py` — SmartLiveEngine class (lines 550-800)
- `pressure_cooker/scripts/test_smart_live_engine.py` — Integration tests

---

## Architecture Overview

```
Browser (Streamlit)                    Backend (FastAPI)
┌─────────────────────┐               ┌────────────────────────────────────────┐
│ Consent → BFI-44 →  │  HTTP/JSON    │ ParticipantManager                     │
│ Interview → Survey   │◄────────────►│ SessionManager                         │
│                      │               │                                        │
│ Meeting Room HTML    │               │ SmartLiveEngine                        │
│ Data Panel           │               │   ├─ SmartProvokerAgent (targeting)    │
│ Timer (JS countdown) │               │   ├─ ActiveMediatorAgent (advancement) │
│ Speaker Targeting    │               │   ├─ SmartSystemManager (selection)    │
│ TTS (Web Speech API) │               │   ├─ DiscussionContext (shared state)  │
│                      │               │   │    ├─ Phase tracking (8 phases)    │
│                      │               │   │    └─ CompetencyCoverageTracker    │
│                      │               │   └─ CaseStudy (data gating)           │
│                      │               │                                        │
│                      │               │ Evidence-Based Analysis                │
│                      │               │   ├─ TurnAnalyzer (per-turn LLM)       │
│                      │               │   └─ AssessmentBuilder (aggregation)   │
│                      │               │                                        │
│                      │               │ ValidatorAgent (3-pass)                │
└─────────────────────┘               └────────────────────────────────────────┘
                                              │
                                        OpenRouter API
                                       (DeepSeek V3 / Claude Haiku)
```

### Data Flow
1. Participant registers → BFI-44 scored → scenario assigned (counterbalanced)
2. Session created → SmartLiveEngine initialized → opening generated → loading page → reveal
3. Each turn:
   - Human input → competency behavior detection → phase check
   - Smart speaker selection (phase-aware, competency-driven)
   - Targeted AI response (provoker challenges untested competencies)
   - Timer compensated → sequential reveal
4. Session ends:
   - Per-turn analysis (TurnAnalyzer extracts quotes and signals)
   - Evidence aggregation (AssessmentBuilder computes scores with audit trail)
   - 3-pass logic validation (ValidatorAgent)
5. Post-session survey → all data persisted to `outputs/step2/participants/{PID}/`
6. Run `aggregate_results.py` → CSV + report + JSON for analysis

### Assessment Output Structure

```
session_output/
├── metadata (session_id, duration, total_turns)
├── turns[] (raw conversation)
├── intent_statistics (legacy)
├── assessment_mapping (legacy formula-based)
├── logical_validation (3-pass validator)
└── evidence_assessment (NEW)
    ├── turn_analyses[] (per-turn analysis)
    │   ├── intent_analysis (with reasoning)
    │   ├── trait_signals[] (quotes + Big Five)
    │   ├── reasoning_assessment
    │   └── competency_signals
    ├── competency_scores (with evidence trails)
    │   ├── collaboration {score, evidence[]}
    │   ├── leadership {score, evidence[]}
    │   ├── problem_solving {score, evidence[]}
    │   ├── communication {score, evidence[]}
    │   └── stress_management {score, evidence[]}
    └── personality_inference (Big Five with evidence)
```
