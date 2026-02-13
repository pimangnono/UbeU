# UbeU V4 Implementation Plan

**Objective:** Validate AI-inferred personality traits against BFI-44 self-report for FYP research.

**Last Updated:** 2026-02-13 (Rev 5: + React frontend phase, API-first design)

---

## New User Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ADMIN SIDE (HR Manager)                       │
├─────────────────────────────────────────────────────────────────────┤
│  1. Receive candidate application (external - job role known)       │
│  2. Register test session in admin dashboard                        │
│     - Assign userId (e.g., P001)                                    │
│     - Assign job role                                               │
│     - Select interview mode (case/group/both)                       │
│     - Select scenario template                                      │
│  3. Share userId with candidate                                     │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      CANDIDATE SIDE (User)                          │
├─────────────────────────────────────────────────────────────────────┤
│  1. Sign in with userId (no registration needed)                    │
│  2. Consent form                                                    │
│  3. BFI-44 questionnaire                                            │
│  4. Group discussion (mode pre-configured by HR)                    │
│  5. View personal report (OCEAN + CCS skills)                       │
│  6. Post-survey (includes report accuracy questions)                │
│  7. Completion screen                                               │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      HR DASHBOARD (Post-Session)                    │
├─────────────────────────────────────────────────────────────────────┤
│  - View all candidate reports                                       │
│  - Compare BFI-44 (self-report) vs AI-inferred traits               │
│  - Export data for FYP analysis                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## System Architecture

```
Phase 0-7 (Dev/Testing):        Phase 8 (Production):
┌──────────────┐                ┌──────────────┐
│  Streamlit   │                │    React     │
│  (Prototype) │                │  (Frontend)  │
└──────┬───────┘                └──────┬───────┘
       │                               │
       │  Both talk to same API        │
       ▼                               ▼
┌─────────────────────────────────────────────┐
│              FastAPI (Backend)               │
│  REST endpoints + WebSocket (chat stream)   │
└──────────┬──────────────────┬───────────────┘
           │                  │
    ┌──────▼───────┐   ┌──────▼───────┐
    │  OpenRouter   │   │   Supabase   │
    │  (LLM API)   │   │  (Postgres)  │
    └──────────────┘   └──────────────┘
```

**Key:** FastAPI is designed API-first from Phase 0. Streamlit is the rapid prototype
during development. React replaces it in Phase 8 without any backend changes.

---

## Supabase Database Schema

Replaces all JSON file storage (`outputs/participants/`, `outputs/sessions/`).
Supabase Auth replaces custom admin password and session tokens.

### Tables

```sql
-- Participants (replaces ParticipantManager JSON files)
CREATE TABLE participants (
    id TEXT PRIMARY KEY,                    -- P001, P002, ...
    name TEXT NOT NULL,
    email TEXT,
    job_role TEXT,
    status TEXT DEFAULT 'pending',          -- pending, in_progress, completed
    condition TEXT,                          -- case_first, group_first
    interview_mode TEXT DEFAULT 'group',    -- case, group, both
    scenario_id TEXT DEFAULT 'product_team',
    consent_given BOOLEAN DEFAULT FALSE,
    consent_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

-- BFI-44 responses and scores
CREATE TABLE bfi44_results (
    participant_id TEXT PRIMARY KEY REFERENCES participants(id),
    raw_responses JSONB NOT NULL,           -- {1: 4, 2: 2, ...}
    scores JSONB NOT NULL,                  -- {O: 0.72, C: 0.65, ...}
    duration_seconds INTEGER,
    submitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- Session transcripts (conversation turns)
CREATE TABLE sessions (
    id TEXT PRIMARY KEY,                    -- UUID
    participant_id TEXT REFERENCES participants(id),
    mode TEXT NOT NULL,                     -- case_study, group_discussion
    scenario_id TEXT,
    status TEXT DEFAULT 'active',           -- active, ended
    started_at TIMESTAMPTZ DEFAULT NOW(),
    ended_at TIMESTAMPTZ,
    duration_seconds INTEGER
);

CREATE TABLE turns (
    id SERIAL PRIMARY KEY,
    session_id TEXT REFERENCES sessions(id),
    turn_number INTEGER NOT NULL,
    speaker_name TEXT NOT NULL,             -- Candidate, Alex, Jordan, Riley
    speaker_role TEXT NOT NULL,             -- candidate, alex, jordan, riley
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- AI personality assessment results
CREATE TABLE assessments (
    id SERIAL PRIMARY KEY,
    participant_id TEXT REFERENCES participants(id),
    session_id TEXT REFERENCES sessions(id),
    mode TEXT NOT NULL,                     -- case_study, group_discussion

    -- Ensemble scores (median of 3 models)
    scores JSONB,                           -- {O: 0.68, C: 0.71, ...}
    confidence JSONB,                       -- {O: 0.85, C: 0.78, ...}

    -- Per-model breakdown
    deepseek_scores JSONB,
    gemini_scores JSONB,
    grok_scores JSONB,

    -- Evidence and metadata
    evidence JSONB,                         -- [{trait, quote, turn, direction, strength}]
    strengths TEXT[],
    development_areas TEXT[],
    behavioral_summary TEXT,

    -- Quality flags
    quality_flags JSONB DEFAULT '{}',       -- {insufficient_turns: true, ...}
    parse_errors INTEGER DEFAULT 0,

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Behavioral statistics per session
CREATE TABLE session_stats (
    session_id TEXT PRIMARY KEY REFERENCES sessions(id),
    total_turns INTEGER,
    candidate_turns INTEGER,
    candidate_word_count INTEGER,
    avg_words_per_turn REAL,
    times_addressed_others INTEGER,
    times_asked_questions INTEGER,
    times_disagreed INTEGER,
    times_acknowledged INTEGER,
    times_proposed_ideas INTEGER,
    trait_coverage JSONB                    -- {O: 0.6, C: 0.3, ...}
);

-- Post-survey responses
CREATE TABLE surveys (
    participant_id TEXT PRIMARY KEY REFERENCES participants(id),
    -- Report accuracy
    personality_accuracy INTEGER,           -- 1-5
    skills_accuracy INTEGER,                -- 1-5
    most_accurate_trait TEXT,
    least_accurate_trait TEXT,
    -- Reflection
    ai_realism INTEGER,                     -- 1-5
    natural_behavior INTEGER,               -- 1-5
    scripted_moments TEXT,                   -- open text
    -- Legacy fields
    group_naturalness INTEGER,
    group_engagement INTEGER,
    overall_recommendation INTEGER,
    open_feedback TEXT,
    submitted_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Row Level Security (RLS)

```sql
-- Admin can read/write everything
-- Candidates can only read/write their own data
ALTER TABLE participants ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Admin full access" ON participants
    FOR ALL USING (auth.role() = 'authenticated');

CREATE POLICY "Candidate reads own" ON participants
    FOR SELECT USING (id = current_setting('app.current_participant_id'));
```

### What Supabase Replaces

| Old (JSON files) | New (Supabase) | Benefit |
|---|---|---|
| `outputs/participants/P001/record.json` | `participants` + `bfi44_results` tables | Atomic writes, no race conditions |
| `server/participant_manager.py` file CRUD | `supabase-py` client calls | Concurrent access safe |
| In-memory session store | `sessions` + `turns` tables | Survives server restart |
| Hardcoded admin password | Supabase Auth | Proper auth with JWT |
| Custom session tokens | Supabase Auth JWT | Industry-standard tokens |
| Sequential ID with file lock | `nextval()` or app-level sequence | Atomic ID generation |

### Environment Variables

```env
# Supabase
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGci...
SUPABASE_SERVICE_KEY=eyJhbGci...    # Server-side only (full access)

# OpenRouter (LLM)
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Models
LLM_AGENT_MODEL=deepseek/deepseek-chat-v3-0324
ENSEMBLE_MODEL_1=deepseek/deepseek-chat-v3-0324
ENSEMBLE_MODEL_2=google/gemini-2.5-flash
ENSEMBLE_MODEL_3=x-ai/grok-4.1-fast
```

---

## Existing Backend (Must Integrate With)

All phases integrate with existing components — no parallel systems.

```
server/
├── server.py              ← FastAPI app (refactor to use Supabase)
├── models.py              ← Pydantic models (keep, extend)
├── participant_manager.py ← REPLACE internals with Supabase client
├── session_manager.py     ← REPLACE in-memory store with Supabase
├── bfi44.py               ← Keep (scoring logic stays server-side)
└── pdf_export.py          ← Keep (reads from Supabase instead)

agents/
├── base_agent.py          ← Extend with A2A task handling
├── group_agents.py        ← Refactor to A2A-compliant
└── trait_selector.py      ← Upgrade to LLM-based

engines/
├── base_engine.py         ← Keep (session lifecycle, timer)
├── case_engine.py         ← Keep (Mode 1)
└── group_engine.py        ← Thin wrapper around A2A Moderator

evaluation/
├── logic_evaluator.py     ← Keep (Mode 1)
└── trait_evaluator.py     ← Upgrade to real 3-model ensemble

clients/
└── llm_client.py          ← Add multi-model support + retry
```

---

## A2A Multi-Agent Architecture

### Overview

Hybrid A2A: central **Moderator Agent** orchestrates turn-taking and trait
coverage, while each **Participant Agent** is an independent A2A agent with
its own personality, memory, and LLM call.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     HYBRID A2A ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────┘

                    ┌───────────────────────┐
                    │   MODERATOR AGENT     │
                    │   ─────────────────   │
                    │   - TraitTracker      │
                    │   - Turn selector     │
                    │   - Trait gap analysis │
                    │   - Conversation state │
                    └───────────┬───────────┘
                                │
                    A2A Task Dispatch
                    (who speaks + goal)
                                │
            ┌───────────────────┼───────────────────┐
            ▼                   ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │  ALEX AGENT  │   │ JORDAN AGENT │   │  RILEY AGENT │
    │  ──────────  │   │  ──────────  │   │  ──────────  │
    │  Assertive   │   │  Supportive  │   │  Skeptical   │
    │  Challenging │   │  Collaborative│   │  Detail-ori. │
    │              │   │              │   │              │
    │  Own prompt  │   │  Own prompt  │   │  Own prompt  │
    │  Own memory  │   │  Own memory  │   │  Own memory  │
    │  Own Agent   │   │  Own Agent   │   │  Own Agent   │
    │  Card        │   │  Card        │   │  Card        │
    └──────────────┘   └──────────────┘   └──────────────┘

    To add Agent 4, 5: Deploy new Agent Card + register with Moderator
```

### Migration: GroupEngine → A2A Moderator

```
BEFORE (V3):
  GroupEngine.generate_ai_response()
    → TraitElicitationSelector.select_next_speaker()
    → agents[speaker].generate_response()       ← single centralized call
    → return turns

AFTER (V4 A2A):
  GroupEngine.generate_ai_response()
    → Moderator.select_and_dispatch()            ← A2A task dispatch
      → TraitTracker.analyze_gaps()              ← LLM-based
      → send A2A Task to agent
      → agent generates independently            ← own LLM call, own context
      → return A2A Task result
    → persist turn to Supabase                   ← crash recovery
    → return turns

GroupEngine = thin wrapper. Session lifecycle, timer, stats remain.
```

### Agent Cards (A2A Standard)

```json
{
  "name": "alex",
  "description": "Assertive, challenging team member who tests ideas directly",
  "url": "http://localhost:8001/a2a",
  "capabilities": { "streaming": true, "pushNotifications": false },
  "skills": [
    { "id": "probe_neuroticism", "name": "Stress Testing" },
    { "id": "probe_extraversion", "name": "Assertion Challenge" }
  ]
}
```

### Agents and Trait Coverage

| Agent | Personality | Best For Probing | Style |
|-------|-------------|------------------|-------|
| Alex | Assertive, challenging | N (stress), E (assertion) | Direct confrontation |
| Jordan | Supportive, collaborative | A (cooperation), O (ideas) | Build on ideas, invite |
| Riley | Skeptical, detail-oriented | C (planning), O (unconventional) | Question assumptions |

### Scaling to 5 Agents (Future)

Add: Agent Card JSON + agent prompt file + registry entry. No architectural changes.

| Agent | Personality | Would Cover |
|-------|-------------|-------------|
| Sam | Diplomatic, process-focused | C (organization), A (mediation) |
| Casey | Energetic, spontaneous | E (social energy), O (brainstorming) |

---

## True Multi-Model Ensemble

### Models (via OpenRouter)

| Model | ID | Role |
|-------|----|------|
| DeepSeek V3 | `deepseek/deepseek-chat-v3-0324` | Judge 1 |
| Gemini 2.5 Flash | `google/gemini-2.5-flash` | Judge 2 |
| Grok 4.1 Fast | `x-ai/grok-4.1-fast` | Judge 3 |

### Why True Multi-Model

Old "ensemble" = same model 3x at different temperatures. That's sampling
variation, not consensus. True multi-model gives genuine architectural
diversity, valid ICC, and per-model accuracy for thesis.

### Flow

```
1. Format transcript + behavioral stats (from Supabase)
2. Send SAME prompt to all 3 models in parallel
3. Each evaluates 5 OCEAN traits → scores + evidence
4. Aggregate per trait:
   - Score = median of 3
   - Confidence = 1.0 - (max - min)
   - Evidence = union (deduplicated)
5. Store per-model scores in assessments table
6. Flag low-agreement traits (range > 0.3)
```

---

## Security Fixes

| ID | Issue | Fix |
|----|-------|-----|
| S1 | Hardcoded admin password | Supabase Auth (email/password login) |
| S2 | No API authentication | Supabase JWT tokens validated per request |
| S3 | CORS wildcard `*` | Restrict to `CORS_ORIGINS` env var |
| S4 | Prompt injection via user input | Sanitize messages before LLM prompt |
| S5 | Race condition in ID generation | Supabase atomic sequence / `SELECT FOR UPDATE` |
| S6 | Silent eval parse failure | Log errors, `confidence=0.0`, `parse_error=True` |

---

## Statistical Analysis Methods

### Convergent Validity (BFI-44 vs AI-Inferred)

| Method | Purpose |
|--------|---------|
| Pearson r per trait | Linear correlation with p-value |
| ICC(2,1) per trait | Absolute agreement |
| Paired t-test per trait | Systematic bias detection |
| Cohen's d | Effect size |
| MAE per trait | Error magnitude |
| Bland-Altman plots | Visual agreement |

### Score Standardization

BFI-44 (Likert 1-5) normalized to 0-1: `(score - 1) / 4`

### Inter-Model Agreement

| Method | Purpose |
|--------|---------|
| ICC(2,3) across 3 models | Judge agreement |
| Krippendorff's alpha | Ordinal agreement |
| Per-trait model spread | Hardest traits to judge |

### Data Quality Gates

```python
QUALITY_THRESHOLDS = {
    "min_candidate_turns": 8,
    "min_avg_words_per_turn": 15,
    "min_trait_coverage_confidence": 0.3,
    "max_parse_errors": 1,
}
```

Flagged sessions excluded from primary analysis. Both filtered and unfiltered
results reported in thesis (transparency).

### Export Format

```csv
participant_id,bfi_O,bfi_C,bfi_E,bfi_A,bfi_N,ai_O,ai_C,ai_E,ai_A,ai_N,conf_O,conf_C,conf_E,conf_A,conf_N,quality_flag
P001,0.68,0.75,0.82,0.60,0.35,0.72,0.70,0.78,0.65,0.30,0.85,0.78,0.90,0.72,0.68,
```

### Dependencies

```
supabase>=2.0.0     # Supabase Python client
scipy>=1.11.0       # pearsonr, ttest_rel
pingouin>=0.5.3     # ICC
matplotlib>=3.8.0   # Bland-Altman plots
```

---

## Implementation Phases

### Phase 0: Supabase Setup (Target: Feb 14)
**Status:** Not Started

#### Tasks:
- [ ] Create Supabase project (free tier)
- [ ] Create database tables (schema above)
- [ ] Set up Supabase Auth (admin user)
- [ ] Configure Row Level Security policies
- [ ] Create `server/supabase_client.py` — shared Supabase client
- [ ] Refactor `server/participant_manager.py` — replace JSON file ops with Supabase queries
- [ ] Refactor `server/session_manager.py` — persist sessions to Supabase instead of in-memory
- [ ] Update `server/server.py` — init Supabase client on startup, add JWT auth middleware
- [ ] Add Supabase env vars to `.env`
- [ ] Remove all demo mode code:
  - Remove `demo_mode` flag from session state in `ui/app.py`
  - Remove `DEMO_RESPONSES` and mock generators in `ui/pages/group_discussion_page.py`
  - Remove demo checkbox from `ui/pages/consent_page.py`
  - Remove `DEMO_CANDIDATES` from `ui/pages/admin_dashboard.py`
- [ ] Delete `outputs/participants/` and `outputs/sessions/` (data moves to Supabase)
- [ ] Verify existing BFI-44 scoring in `server/bfi44.py` works standalone
- [ ] **API-first design:** All endpoints return clean JSON (no Streamlit-specific formats). This ensures React can consume the same API in Phase 8 without backend changes.

#### Files to create/modify:
- Create `server/supabase_client.py`
- Refactor `server/participant_manager.py`
- Refactor `server/session_manager.py`
- Modify `server/server.py` — Supabase init + auth
- Modify `ui/app.py` — remove demo_mode
- Modify `ui/pages/group_discussion_page.py` — remove demo code
- Modify `ui/pages/consent_page.py` — remove demo checkbox
- Modify `ui/pages/admin_dashboard.py` — remove DEMO_CANDIDATES

---

### Phase 1: Admin Session Management (Target: Feb 15-16)
**Status:** Not Started

#### Tasks:
- [ ] Add session pre-registration endpoint
  - `POST /admin/session` — insert into `participants` table
  - Input: candidate name, email (optional), job role, mode, scenario
  - Auto-generate userId (P001, P002...) via Supabase sequence
  - Protected by Supabase Auth (admin JWT)

- [ ] Update admin dashboard UI
  - Login via Supabase Auth (email/password)
  - Session registration form (name, job role, mode, scenario)
  - Session list view queried from `participants` table
  - Status: Pending / In Progress / Completed
  - Quick actions: View report, export data

- [ ] Remove mode toggles from candidate-facing sidebar
  - Mode pre-configured by admin in `participants` table
  - Candidate cannot change modes

- [ ] Security: CORS restriction (S3)
  - `CORS_ORIGINS` env var, default `localhost:8501`

#### Files to modify:
- `server/server.py` — Add `/admin/session`, CORS config
- `ui/pages/admin_dashboard.py` — Supabase Auth login, session registration + list
- `ui/app.py` — Remove mode toggles from sidebar

---

### Phase 2: UserId-Based Sign-In + Input Security (Target: Feb 16-17)
**Status:** Not Started

#### Tasks:
- [ ] Replace registration form with userId sign-in
  - Input: userId only (e.g., P001)
  - Query `participants` table — validate exists + status is `pending`
  - Load pre-configured mode, scenario, job role from DB

- [ ] Session state management
  - Update `participants.status` to `in_progress` on sign-in
  - Prevent re-entry for `completed` sessions
  - Handle invalid/nonexistent userIds

- [ ] Input sanitization (S4)
  - Sanitize candidate messages before LLM prompts
  - Block common injection patterns, truncate to max length

#### Files to modify:
- `ui/pages/consent_page.py` — UserId sign-in querying Supabase
- `server/server.py` — Add userId validation endpoint
- Create `server/sanitizer.py` — Input sanitization

---

### Phase 3: A2A Agent Infrastructure + Real Ensemble (Target: Feb 17-20)
**Status:** Not Started

Refactors agent architecture to A2A and upgrades evaluation to true
multi-model ensemble. All interactions go through live LLM calls.

#### Migration strategy:
`engines/group_engine.py` stays as session wrapper (timer, stats, phases).
Internals delegate to A2A Moderator. Turns persisted to Supabase per-turn.

#### Tasks:
- [ ] Create A2A base classes (extend `agents/base_agent.py`)
  - `A2AAgent` with A2A task handling
  - Agent Card definitions (JSON)

- [ ] Implement Moderator Agent
  - Turn order management
  - A2A Task dispatch to participant agents
  - Round-robin initially (adaptive in Phase 4)

- [ ] Migrate 3 Participant Agents to A2A
  - Refactor Alex, Jordan, Riley from `group_agents.py`
  - Keep existing personalities/prompts (proven)
  - Each receives context via A2A Task, generates independently

- [ ] Agent Registry
  - Config file (JSON), discovered by Moderator
  - Add agent = Agent Card + prompt + register

- [ ] Refactor GroupEngine
  - `generate_ai_response()` delegates to Moderator
  - Each turn persisted to `turns` table in Supabase (crash recovery)
  - Session lifecycle, timer, stats remain in GroupEngine

- [ ] Upgrade to true multi-model ensemble
  - Extend `clients/llm_client.py` with `ENSEMBLE_MODELS`
  - Refactor `evaluation/trait_evaluator.py`:
    - Send same prompt to DeepSeek, Gemini, Grok in parallel
    - Aggregate: median score, confidence = 1.0 - range
    - Store per-model scores in `assessments` table
  - Fix S6: log parse errors, confidence=0.0, parse_error flag

- [ ] Error handling and retry
  - LLM retry with exponential backoff (max 3 attempts)
  - If one ensemble model fails, use remaining 2
  - Session state in Supabase — survives server restart

#### A2A Message Schema:

```json
// Moderator → Agent
{
  "task_id": "turn_005_alex",
  "task_type": "respond_in_discussion",
  "input": {
    "conversation_history": [...],
    "your_role": "assertive_challenger",
    "goal": "continue_discussion",
    "scenario_context": "Product team budget discussion"
  }
}

// Agent → Moderator
{
  "task_id": "turn_005_alex",
  "status": "completed",
  "output": {
    "response_text": "I think we're overcomplicating this...",
    "internal_notes": {
      "intent": "challenge_proposal",
      "candidate_trait_observed": null
    }
  }
}
```

#### Files to create/modify:
- Modify `agents/base_agent.py` — A2A task handling
- Create `agents/moderator.py` — A2A Moderator
- Refactor `agents/group_agents.py` — A2A-compliant
- Create `agents/agent_cards/` — Agent Card JSONs
- Create `agents/registry.py` — Agent discovery
- Modify `engines/group_engine.py` — Thin wrapper, Supabase turn persistence
- Modify `clients/llm_client.py` — Multi-model + retry
- Modify `evaluation/trait_evaluator.py` — 3-model ensemble + error logging

---

### Phase 4: Adaptive AI Behavior + Quality Gates (Target: Feb 20-22)
**Status:** Not Started

Moderator becomes intelligent about which agent to dispatch and why.

#### Tasks:
- [ ] Upgrade TraitTracker to LLM-based analysis
  - Replace keyword matching with LLM call after each candidate turn
  - "What OCEAN traits did this response demonstrate? Score 0-1."
  - Uses DeepSeek (fast/cheap) for real-time analysis
  - Keyword matching as fallback if LLM call fails

- [ ] Adaptive turn selection in Moderator
  - Trait gaps → best agent selection
  - Missing N? → Alex. Missing A? → Jordan. Missing C? → Riley.
  - Rotation logic to prevent domination

- [ ] Trait elicitation goals in A2A Tasks
  - `elicitation_goal` in task dispatch
  - Agent incorporates naturally (hint, not script)

- [ ] Session quality gates (real-time)
  - Track: candidate turns, avg words, trait coverage
  - If quality low near session end, agents prompt more directly
  - Quality flags stored in `assessments.quality_flags`

- [ ] Trait elicitation strategies:

  | Trait | Primary Agent | Strategy |
  |-------|--------------|----------|
  | Openness | Jordan / Riley | Propose unconventional solution |
  | Conscientiousness | Riley | Ask about planning, deadlines |
  | Extraversion | Alex | Create silence / direct challenge |
  | Agreeableness | Jordan | Create disagreement |
  | Neuroticism | Alex | Apply mild pressure |

#### Files to create/modify:
- Refactor `agents/trait_selector.py` — LLM-based + keyword fallback
- Modify `agents/moderator.py` — Adaptive dispatch + quality gate
- Modify `agents/group_agents.py` — Handle elicitation goals

---

### Phase 5: Dual-View Report (Target: Feb 22-23)
**Status:** Not Started

#### Tasks:
- [ ] Candidate report view
  - OCEAN trait scores (0-100%)
  - Top 3 CCS skills
  - Key evidence quotes (positive framing)

- [ ] HR manager report view (admin dashboard)
  - Full OCEAN scores with confidence
  - All CCS skills with evidence
  - BFI-44 vs AI-inferred comparison chart
  - Per-model ensemble breakdown (from `assessments` table)
  - Conversation transcript (from `turns` table)
  - Session quality flags
  - Survey responses (from `surveys` table)

- [ ] Report data fetched from Supabase:
  ```sql
  SELECT p.*, b.scores AS bfi44, a.scores AS ai_scores,
         a.deepseek_scores, a.gemini_scores, a.grok_scores,
         a.quality_flags, a.evidence
  FROM participants p
  JOIN bfi44_results b ON b.participant_id = p.id
  JOIN assessments a ON a.participant_id = p.id
  WHERE p.id = 'P001';
  ```

#### Files to modify:
- `ui/pages/results_page.py` — Candidate report
- `ui/pages/admin_dashboard.py` — HR report with ensemble detail
- Create `ui/components/report_card.py` — Reusable components

---

### Phase 6: Enhanced Post-Survey (Target: Feb 23-24)
**Status:** Not Started

#### Tasks:
- [ ] Report accuracy questions:
  - "The personality assessment accurately reflects who I am" (1-5)
  - "The skills assessment matches my self-perception" (1-5)
  - "Which trait felt most/least accurate?" (dropdown)

- [ ] Reflection questions:
  - "Did the AI teammates feel realistic?" (1-5)
  - "Did you behave naturally during the discussion?" (1-5)
  - "Any moments that felt scripted or artificial?" (open text)

- [ ] Survey saved to `surveys` table in Supabase
- [ ] Update `participants.status` to `completed` on submit

#### Files to modify:
- `ui/pages/survey_page.py` — Accuracy + reflection questions
- `server/models.py` — Update PostSessionSurvey model
- `server/server.py` — Survey endpoint writes to Supabase

---

### Phase 7: Data Export & Statistical Analysis (Target: Feb 24-26)
**Status:** Not Started

#### Tasks:
- [ ] Export functionality in admin dashboard
  - CSV: SQL query → pandas → CSV download
    ```sql
    SELECT p.id, b.scores, a.scores, a.confidence, a.quality_flags
    FROM participants p
    JOIN bfi44_results b ON ...
    JOIN assessments a ON ...
    WHERE p.status = 'completed';
    ```
  - JSON: Full session data with transcript
  - PDF: Individual reports (existing `pdf_export.py`)

- [ ] Statistical analysis module
  - Pearson r per trait with p-values
  - ICC(2,1) per trait
  - Paired t-test per trait (systematic bias)
  - Cohen's d effect size
  - Bland-Altman plots
  - Inter-model ICC(2,3) for ensemble agreement
  - Aggregate summary table for thesis

- [ ] Score standardization
  - BFI-44: `(raw - 1) / 4` → 0-1
  - Verify reverse-scored items in `server/bfi44.py`

- [ ] Quality-filtered analysis
  - Run stats on full AND quality-filtered datasets
  - Report both in thesis

#### Files to create/modify:
- Create `analysis/statistics.py` — Statistical computations
- Create `analysis/plots.py` — Bland-Altman, scatter, radar
- Create `ui/services/export_service.py` — CSV/JSON/PDF export
- Modify `ui/pages/admin_dashboard.py` — Export buttons + stats display

---

### Phase 8: React Frontend (Target: Feb 27 - Mar 2)
**Status:** Not Started

Replaces Streamlit with a professional React frontend. Zero backend changes
needed — React consumes the same FastAPI endpoints Streamlit used.

#### Why React over Streamlit:
| Aspect | Streamlit | React |
|--------|-----------|-------|
| Chat UX | Basic, page reruns on every interaction | Real-time WebSocket, typing indicators, smooth scroll |
| Animations | None | Framer Motion transitions, loading states |
| Mobile | Poor | Responsive by default (Tailwind) |
| Professional feel | Looks like a data dashboard | Looks like a product |
| State management | Session state (fragile) | React state + context (robust) |
| FYP demo impression | "It's a prototype" | "It's a platform" |

#### Tech Stack:
- **React 18** + TypeScript
- **Tailwind CSS** — utility-first styling, fast iteration
- **Framer Motion** — smooth page transitions, chat animations
- **Supabase JS client** — auth + realtime subscriptions
- **WebSocket** — real-time chat streaming from FastAPI

#### Tasks:
- [ ] Project setup
  - `npx create-react-app frontend --template typescript`
  - Install: `tailwindcss`, `framer-motion`, `@supabase/supabase-js`, `react-router-dom`
  - Configure proxy to FastAPI (`http://localhost:8000`)

- [ ] Auth & routing
  - Supabase Auth (same as admin, but candidate role)
  - Routes: `/login`, `/consent`, `/questionnaire`, `/discussion`, `/report`, `/survey`, `/complete`
  - Admin routes: `/admin/login`, `/admin/dashboard`, `/admin/report/:id`
  - Protected routes with auth guards

- [ ] Candidate pages
  - **Login page** — userId input, clean minimal design
  - **Consent page** — scrollable consent text, checkbox + submit
  - **BFI-44 page** — Likert scale with progress bar, keyboard navigation
  - **Group Discussion page** (critical):
    - WebSocket connection to FastAPI for real-time chat
    - Agent avatars with distinct colors
    - Typing indicator ("Alex is typing...")
    - Phase progression indicator
    - Message bubbles with timestamps
    - Auto-scroll with "new messages" button
  - **Results page** — OCEAN radar chart, skill badges, evidence cards
  - **Survey page** — Likert scales + text areas
  - **Completion page** — thank you screen

- [ ] Admin pages
  - **Admin login** — Supabase Auth email/password
  - **Dashboard** — session list table with filters, status badges
  - **Session registration** — form with candidate info, mode, scenario
  - **Report view** — full report with BFI-44 comparison, ensemble breakdown
  - **Export** — CSV/JSON download buttons

- [ ] WebSocket endpoint in FastAPI
  - `ws://localhost:8000/ws/discussion/{session_id}`
  - Server pushes: agent responses, typing events, phase changes
  - Client sends: candidate messages
  - Fallback to polling if WebSocket fails

- [ ] Remove Streamlit
  - Delete `ui/` directory
  - Update `README.md` with React setup instructions
  - Update deployment docs

#### Files to create:
```
frontend/                          # NEW React app
├── src/
│   ├── App.tsx                    # Router + auth provider
│   ├── api/
│   │   ├── client.ts              # Axios/fetch wrapper for FastAPI
│   │   └── supabase.ts            # Supabase client
│   ├── pages/
│   │   ├── LoginPage.tsx
│   │   ├── ConsentPage.tsx
│   │   ├── BFI44Page.tsx
│   │   ├── DiscussionPage.tsx     # WebSocket chat
│   │   ├── ResultsPage.tsx
│   │   ├── SurveyPage.tsx
│   │   └── admin/
│   │       ├── AdminLogin.tsx
│   │       ├── Dashboard.tsx
│   │       └── ReportView.tsx
│   ├── components/
│   │   ├── ChatBubble.tsx
│   │   ├── TypingIndicator.tsx
│   │   ├── OceanRadar.tsx         # Radar chart
│   │   ├── SkillBadge.tsx
│   │   ├── LikertScale.tsx
│   │   └── ProgressTracker.tsx
│   └── styles/
│       └── tailwind.css
├── package.json
├── tsconfig.json
└── tailwind.config.js

server/
└── server.py                      # Add WebSocket endpoint
```

#### Files to modify:
- `server/server.py` — Add WebSocket endpoint for discussion streaming
- Delete `ui/` — Streamlit code no longer needed

---

## Design Decisions

### Q1: Same scenario across job roles?
**Decision:** Use SAME scenario (Product Team) for all participants

Controlled stimulus, easier comparison, reduces confounding variables.

---

### Q2: Show report to candidate?
**Decision:** YES — before post-survey

| Element | Candidate | HR Manager |
|---------|-----------|------------|
| OCEAN scores | Yes (simplified) | Yes (detailed) |
| CCS skills | Yes (top 3) | Yes (all) |
| Evidence quotes | Yes (curated) | Yes (all) |
| BFI-44 comparison | No | Yes |
| Ensemble breakdown | No | Yes |
| Transcript | No | Yes |
| Quality flags | No | Yes |

---

### Q3: A2A Protocol?
**Decision:** YES — Hybrid A2A

Moderator controls flow (reproducibility), agents are independent (distinct voice).

| Factor | Custom JSON | Hybrid A2A (chosen) | Full A2A |
|--------|-------------|----------------------|----------|
| Dev time (initial) | ~2 days | ~3-4 days | +10-14 days |
| Dev time (add agent) | Rewrite orchestration | Deploy Agent Card | Deploy Agent Card |
| Reproducibility | High | High (Moderator) | Lower |

---

### Q4: Ensemble Strategy?
**Decision:** True multi-model (3 different models via OpenRouter)

Models: DeepSeek V3, Gemini 2.5 Flash, Grok 4.1 Fast.
Different architectures = genuine diversity, valid ICC, per-model accuracy.

---

### Q5: Storage?
**Decision:** Supabase (hosted PostgreSQL)

| Factor | JSON Files (old) | Supabase (chosen) |
|--------|-----------------|-------------------|
| Concurrent access | File lock needed | Built-in |
| Session persistence | In-memory (lost on restart) | Survives restarts |
| Auth | Hardcoded password | Supabase Auth + JWT |
| Data export | Parse JSON files | SQL queries → CSV |
| Free tier | N/A | 500MB + 50K requests |
| Race conditions | Possible | Impossible (atomic) |

---

### Q6: Demo Mode?
**Decision:** NO — removed entirely

All features require live FastAPI backend, Supabase, and LLM access.
Every test run produces real data for thesis analysis.

---

### Q7: Frontend Framework?
**Decision:** Plan React NOW, implement LATER (Phase 8)

| Factor | Streamlit Only | Streamlit → React |
|--------|---------------|-------------------|
| Dev speed (early phases) | Fast | Same (Streamlit for prototyping) |
| Final product quality | "Prototype" feel | Professional platform |
| Backend changes for React | N/A | Zero (API-first from Phase 0) |
| Chat UX | Page reruns, no streaming | WebSocket, typing indicators |
| FYP demo | Functional but basic | Impressive |
| Risk | None | Extra 4-5 days, but isolated phase |

Streamlit used for Phases 0-7 (rapid testing). React built in Phase 8
against the exact same FastAPI endpoints. No throwaway work because the
backend is API-first from day one.

---

## File Structure

```
server/                                # REFACTORED for Supabase
├── server.py                          # Supabase init, JWT auth, CORS
├── supabase_client.py                 # NEW: shared Supabase client
├── participant_manager.py             # Rewritten: Supabase queries
├── session_manager.py                 # Rewritten: Supabase persistence
├── sanitizer.py                       # NEW: input sanitization
├── models.py                          # Updated survey model
├── bfi44.py                           # Unchanged (scoring logic)
└── pdf_export.py                      # Reads from Supabase

agents/                                # REFACTORED to A2A
├── base_agent.py                      # Extended with A2A task handling
├── group_agents.py                    # A2A-compliant (keep personalities)
├── moderator.py                       # NEW: A2A Moderator
├── trait_selector.py                  # Upgraded: LLM-based + keyword fallback
├── registry.py                        # NEW: Agent discovery
└── agent_cards/                       # NEW
    ├── alex.json
    ├── jordan.json
    └── riley.json

engines/
└── group_engine.py                    # Thin wrapper, Supabase turn persistence

evaluation/
└── trait_evaluator.py                 # True 3-model ensemble + error logging

clients/
└── llm_client.py                      # Multi-model + retry

analysis/                              # NEW
├── statistics.py                      # Pearson, ICC, t-test, Cohen's d
└── plots.py                           # Bland-Altman, scatter, radar

ui/                                    # STREAMLIT (Phases 0-7, removed in Phase 8)
├── app.py                             # No mode toggles, no demo mode
├── schema_config.py                   # Unchanged
├── pages/
│   ├── admin_dashboard.py             # Supabase Auth, session reg, reports, export
│   ├── consent_page.py                # UserId sign-in via Supabase
│   ├── bfi44_page.py                  # Unchanged
│   ├── group_discussion_page.py       # A2A via GroupEngine, no demo code
│   ├── results_page.py                # Report + ensemble detail
│   └── survey_page.py                 # Accuracy + reflection
├── services/
│   └── export_service.py              # NEW: CSV/JSON/PDF
└── components/
    └── report_card.py                 # NEW: Reusable report UI

frontend/                              # REACT (Phase 8, replaces ui/)
├── src/
│   ├── App.tsx                        # Router + auth provider
│   ├── api/
│   │   ├── client.ts                  # FastAPI REST client
│   │   └── supabase.ts               # Supabase JS client
│   ├── pages/                         # Candidate + admin pages
│   └── components/                    # ChatBubble, OceanRadar, etc.
├── package.json
└── tailwind.config.js
```

---

## Timeline Summary

| Phase | Description | Target Date | Status |
|-------|-------------|-------------|--------|
| 0 | Supabase Setup + Demo Mode Removal | Feb 14 | Not Started |
| 1 | Admin Session Management | Feb 15-16 | Not Started |
| 2 | UserId-Based Sign-In + Input Security | Feb 16-17 | Not Started |
| 3 | A2A Agent Infrastructure + Real Ensemble | Feb 17-20 | Not Started |
| 4 | Adaptive AI Behavior + Quality Gates | Feb 20-22 | Not Started |
| 5 | Dual-View Report | Feb 22-23 | Not Started |
| 6 | Enhanced Post-Survey | Feb 23-24 | Not Started |
| 7 | Data Export & Statistical Analysis | Feb 24-26 | Not Started |
| 8 | React Frontend | Feb 27 - Mar 2 | Not Started |

**Total estimated duration:** 17 days (Phases 0-7: core logic, Phase 8: UI polish)

---

## Known Limitations (Document in Thesis)

1. **Single scenario** — personality assessed in one context only
2. **LLM evaluator bias** — 3 models share internet-text training biases
3. **English-only** — prompts and evaluation assume English
4. **15-minute sessions** — limited observation window
5. **Supabase free tier** — 500MB storage, sufficient for N=50
6. **OpenRouter dependency** — all LLM calls route through single provider

---

## Notes

- All dates are tentative
- Phase 0 (Supabase) is a prerequisite — everything depends on it
- Phase 3 is most complex — working A2A + real ensemble
- Phase 3 must be testable end-to-end before Phase 4 adds intelligence
- Existing test data (P001-P003) will NOT be migrated — fresh start in Supabase
- To add agents 4/5 later: agent file + Agent Card + registry entry
- `ANNOTATION_TOOL_UXUI_PLAN.md` is deprecated — not needed
