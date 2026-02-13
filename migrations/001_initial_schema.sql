-- UbeU V4: Initial Supabase Schema
-- Run this in the Supabase SQL editor after creating your project.

-- ============================================================================
-- TABLES
-- ============================================================================

-- Participants (replaces outputs/participants/{pid}/record.json)
CREATE TABLE participants (
    id TEXT PRIMARY KEY,                    -- P001, P002, ...
    name TEXT NOT NULL,
    email TEXT,
    job_role TEXT,
    status TEXT DEFAULT 'pending',          -- pending, in_progress, completed
    current_phase TEXT DEFAULT 'consent',   -- consent, bfi44, mode_1_interview, etc.
    condition TEXT DEFAULT 'case_first',    -- case_first, group_first
    interview_mode TEXT DEFAULT 'group',    -- case, group, both
    scenario_id TEXT DEFAULT 'product_team',
    case_scenario_id TEXT,
    group_scenario_id TEXT,
    consent_given BOOLEAN DEFAULT FALSE,
    consent_at TIMESTAMPTZ,
    -- Assessment results stored as JSONB (denormalized for Phase 0)
    case_completed BOOLEAN DEFAULT FALSE,
    case_session_id TEXT,
    case_assessment JSONB,
    case_stats JSONB,
    group_completed BOOLEAN DEFAULT FALSE,
    group_session_id TEXT,
    group_assessment JSONB,
    group_stats JSONB,
    survey JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);

-- BFI-44 responses and scores
CREATE TABLE bfi44_results (
    participant_id TEXT PRIMARY KEY REFERENCES participants(id),
    raw_responses JSONB NOT NULL,           -- {1: 4, 2: 2, ...}
    scores JSONB NOT NULL,                  -- {O: 0.72, C: 0.65, ...}
    duration_seconds REAL,
    submitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- Session transcripts
CREATE TABLE sessions (
    id TEXT PRIMARY KEY,                    -- UUID
    participant_id TEXT REFERENCES participants(id),
    mode TEXT NOT NULL,                     -- case_study, group
    scenario_id TEXT,
    status TEXT DEFAULT 'active',           -- active, ended
    started_at TIMESTAMPTZ DEFAULT NOW(),
    ended_at TIMESTAMPTZ,
    duration_seconds INTEGER
);

-- Conversation turns
CREATE TABLE turns (
    id SERIAL PRIMARY KEY,
    session_id TEXT REFERENCES sessions(id),
    turn_number INTEGER NOT NULL,
    speaker_name TEXT NOT NULL,             -- Candidate, Alex, Jordan, Riley
    speaker_role TEXT NOT NULL,             -- candidate, alex, jordan, riley
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- AI personality assessment results (Phase 3+: per-model ensemble)
CREATE TABLE assessments (
    id SERIAL PRIMARY KEY,
    participant_id TEXT REFERENCES participants(id),
    session_id TEXT REFERENCES sessions(id),
    mode TEXT NOT NULL,                     -- case_study, group
    scores JSONB,                           -- {O: 0.68, C: 0.71, ...}
    confidence JSONB,                       -- {O: 0.85, C: 0.78, ...}
    deepseek_scores JSONB,
    gemini_scores JSONB,
    grok_scores JSONB,
    evidence JSONB,
    strengths TEXT[],
    development_areas TEXT[],
    behavioral_summary TEXT,
    quality_flags JSONB DEFAULT '{}',
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
    trait_coverage JSONB
);

-- Post-survey responses
CREATE TABLE surveys (
    participant_id TEXT PRIMARY KEY REFERENCES participants(id),
    personality_accuracy INTEGER,           -- 1-5
    skills_accuracy INTEGER,                -- 1-5
    most_accurate_trait TEXT,
    least_accurate_trait TEXT,
    ai_realism INTEGER,                     -- 1-5
    natural_behavior INTEGER,               -- 1-5
    scripted_moments TEXT,
    group_naturalness INTEGER,
    group_engagement INTEGER,
    overall_recommendation INTEGER,
    open_feedback TEXT,
    submitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================================================
-- ROW LEVEL SECURITY
-- ============================================================================

ALTER TABLE participants ENABLE ROW LEVEL SECURITY;
ALTER TABLE bfi44_results ENABLE ROW LEVEL SECURITY;
ALTER TABLE sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE turns ENABLE ROW LEVEL SECURITY;
ALTER TABLE assessments ENABLE ROW LEVEL SECURITY;
ALTER TABLE session_stats ENABLE ROW LEVEL SECURITY;
ALTER TABLE surveys ENABLE ROW LEVEL SECURITY;

-- Service role (backend) has full access to all tables.
-- These policies allow the backend (using SUPABASE_SERVICE_KEY) to do everything.
-- More granular candidate-level policies will be added in Phase 2.

CREATE POLICY "Service role full access" ON participants
    FOR ALL USING (true) WITH CHECK (true);

CREATE POLICY "Service role full access" ON bfi44_results
    FOR ALL USING (true) WITH CHECK (true);

CREATE POLICY "Service role full access" ON sessions
    FOR ALL USING (true) WITH CHECK (true);

CREATE POLICY "Service role full access" ON turns
    FOR ALL USING (true) WITH CHECK (true);

CREATE POLICY "Service role full access" ON assessments
    FOR ALL USING (true) WITH CHECK (true);

CREATE POLICY "Service role full access" ON session_stats
    FOR ALL USING (true) WITH CHECK (true);

CREATE POLICY "Service role full access" ON surveys
    FOR ALL USING (true) WITH CHECK (true);

-- ============================================================================
-- INDEXES
-- ============================================================================

CREATE INDEX idx_participants_status ON participants(status);
CREATE INDEX idx_sessions_participant ON sessions(participant_id);
CREATE INDEX idx_turns_session ON turns(session_id);
CREATE INDEX idx_assessments_participant ON assessments(participant_id);
