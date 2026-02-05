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

## Architecture Overview

```
Browser (Streamlit)                    Backend (FastAPI)
┌─────────────────────┐               ┌──────────────────────────┐
│ Consent → BFI-44 →  │  HTTP/JSON    │ ParticipantManager       │
│ Interview → Survey   │◄────────────►│ SessionManager           │
│                      │               │ LiveEngine               │
│ Meeting Room HTML    │               │   ├─ ProvokerAgent       │
│ Data Panel           │               │   ├─ MediatorAgent       │
│ Timer (JS countdown) │               │   ├─ SystemManagerAgent  │
│ Speaker Targeting    │               │   └─ CaseStudy (gating)  │
│ TTS (Web Speech API) │               │ ValidatorAgent (3-pass)  │
└─────────────────────┘               └──────────────────────────┘
                                              │
                                        OpenRouter API
                                       (DeepSeek V3 / Claude Haiku)
```

### Data Flow
1. Participant registers → BFI-44 scored → scenario assigned (counterbalanced)
2. Session created → opening generated → loading page → reveal
3. Each turn: human input → smart routing → AI response → timer compensated → sequential reveal
4. Session ends → intent classification → assessment mapping → 3-pass logic validation
5. Post-session survey → all data persisted to `outputs/step2/participants/{PID}/`
6. Run `aggregate_results.py` → CSV + report + JSON for analysis
