# UbeU V4 Implementation Plan

**Objective:** Validate AI-inferred personality traits against BFI-44 self-report for FYP research.

**Last Updated:** 2026-02-13 (Revised: Hybrid A2A Protocol adopted, 3 agents with scalable architecture)

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

## A2A Multi-Agent Architecture

### Overview

Uses Google's A2A (Agent-to-Agent) protocol with a **Hybrid** approach:
a central **Moderator Agent** orchestrates turn-taking and trait coverage,
while each **Participant Agent** is an independent A2A agent that generates
its own responses with its own personality, memory, and goals.

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

### Agent Cards (A2A Standard)

Each agent exposes a standard A2A Agent Card:

```json
{
  "name": "alex",
  "description": "Assertive, challenging team member who tests ideas directly",
  "url": "http://localhost:8001/a2a",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false
  },
  "skills": [
    {
      "id": "probe_neuroticism",
      "name": "Stress Testing",
      "description": "Applies pressure to observe stress response"
    },
    {
      "id": "probe_extraversion",
      "name": "Assertion Challenge",
      "description": "Challenges candidate to assert themselves"
    }
  ]
}
```

### Turn Flow (A2A Messages)

```
Turn N:
1. Moderator analyzes conversation → TraitTracker identifies gaps
2. Moderator selects 1-2 agents based on trait gaps + agent skills
3. Moderator sends A2A Task to selected agent(s):
   {
     "task": "respond_in_discussion",
     "context": { conversation_history, trait_gaps, elicitation_goal },
     "goal": "probe_conscientiousness"
   }
4. Agent generates response independently (own LLM call, own personality)
5. Agent returns A2A Task result → Moderator appends to conversation
6. Moderator updates TraitTracker state
```

### Current Agents (3) and Trait Coverage

| Agent | Personality | Best For Probing | Elicitation Style |
|-------|-------------|------------------|-------------------|
| Alex | Assertive, challenging | N (stress), E (assertion) | Direct confrontation, time pressure |
| Jordan | Supportive, collaborative | A (cooperation), O (ideas) | Build on ideas, invite opinions |
| Riley | Skeptical, detail-oriented | C (planning), O (unconventional) | Question assumptions, ask for specifics |

### Scaling to 5 Agents (Future)

Adding agents requires only:
1. Create new Agent Card JSON
2. Create agent system prompt
3. Register with Moderator's agent registry

Candidate agents for expansion:

| Agent | Personality | Would Cover |
|-------|-------------|-------------|
| Sam | Diplomatic, process-focused | C (organization), A (mediation) |
| Casey | Energetic, spontaneous | E (social energy), O (brainstorming) |

---

## Implementation Phases

### Phase 1: Admin Session Management (Target: Feb 14-15)
**Status:** Not Started

#### Tasks:
- [ ] Create session registration form in admin dashboard
  - Input: Candidate name, email (optional), job role
  - Auto-generate: userId (P001, P002, etc.)
  - Select: Interview mode(s), scenario template
  - Output: Session config stored in DB/JSON

- [ ] Create session list view
  - Show all registered sessions
  - Status: Pending / In Progress / Completed
  - Quick actions: View report, export data

- [ ] Remove mode toggles from candidate-facing sidebar
  - Mode is pre-configured by admin
  - Candidate cannot change modes

#### Files to modify:
- `ui/pages/admin_dashboard.py` - Add session registration
- `ui/app.py` - Remove candidate-facing mode toggles
- `ui/pages/consent_page.py` - Simplify to userId sign-in

---

### Phase 2: UserId-Based Sign-In (Target: Feb 15-16)
**Status:** Not Started

#### Tasks:
- [ ] Replace registration form with userId sign-in
  - Input: userId only (e.g., P001)
  - Validate against registered sessions
  - Load pre-configured settings (mode, scenario, job role)

- [ ] Session state management
  - Load participant config from stored session
  - Prevent re-entry for completed sessions
  - Handle invalid/expired userIds

#### Files to modify:
- `ui/pages/consent_page.py` - Replace registration with sign-in
- Create `ui/services/session_service.py` - Session lookup logic

---

### Phase 3: A2A Agent Infrastructure (Target: Feb 16-18)
**Status:** Not Started

This phase sets up the A2A communication layer. No adaptive behavior yet —
just getting agents to talk through A2A instead of centralized prompting.

#### Tasks:
- [ ] Set up A2A agent server framework
  - Each agent runs as an A2A-compliant endpoint
  - Shared base class `A2AAgent` for common behavior
  - Agent Card definition per agent (JSON)

- [ ] Implement Moderator Agent
  - Manages conversation turn order
  - Dispatches A2A Tasks to participant agents
  - Collects responses and appends to conversation history
  - Simple round-robin turn selection (adaptive logic in Phase 4)

- [ ] Implement 3 Participant Agents (Alex, Jordan, Riley)
  - Each has own system prompt with personality definition
  - Each receives conversation context via A2A Task
  - Each generates response independently (own LLM call)
  - Returns response via A2A Task result

- [ ] Agent Registry
  - Moderator discovers agents via Agent Cards
  - Registry is a simple config file (JSON/YAML)
  - Adding a new agent = add Agent Card + prompt file + register

- [ ] Wire into group discussion page
  - Replace current centralized agent call with A2A Moderator
  - Conversation history passed as A2A context
  - Agent responses displayed in chat UI

#### A2A Message Schema:

```json
// Moderator → Agent (Task dispatch)
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

// Agent → Moderator (Task result)
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
- Create `agents/base_agent.py` - A2A base class
- Create `agents/moderator.py` - Moderator agent
- Create `agents/participant_agents/alex.py` - Alex agent
- Create `agents/participant_agents/jordan.py` - Jordan agent
- Create `agents/participant_agents/riley.py` - Riley agent
- Create `agents/agent_cards/` - Agent Card JSON files
- Create `agents/registry.py` - Agent registry/discovery
- Modify `ui/pages/group_discussion_page.py` - Wire to A2A Moderator

---

### Phase 4: Adaptive AI Bot Behavior (Target: Feb 18-20)
**Status:** Not Started

Builds on Phase 3's A2A infrastructure. Adds trait tracking and
adaptive elicitation — the Moderator becomes intelligent about
which agent to dispatch and with what goal.

#### Tasks:
- [ ] Implement TraitTracker (integrated into Moderator)
  - Track which OCEAN traits have been observed
  - Track confidence level per trait (low/medium/high)
  - Track supporting evidence (candidate quotes)
  - Identify gaps (traits not yet demonstrated)
  - Track CCS skills observed

- [ ] Adaptive turn selection in Moderator
  - Analyze trait gaps → select best agent for the gap
  - Match agent skills to missing traits:
    - Missing N? → Dispatch Alex (stress testing)
    - Missing A? → Dispatch Jordan (cooperation probe)
    - Missing C? → Dispatch Riley (detail questioning)
  - Rotation logic to prevent one agent dominating

- [ ] Trait elicitation goals in A2A Tasks
  - Moderator includes `elicitation_goal` in task dispatch
  - Agent incorporates goal into response naturally
  - Goal is a hint, not a script — agent maintains own voice

- [ ] Trait elicitation strategies per agent:

  | Trait | Primary Agent | Strategy |
  |-------|--------------|----------|
  | Openness | Jordan / Riley | Propose unconventional solution, gauge reaction |
  | Conscientiousness | Riley | Ask about planning, deadlines, specifics |
  | Extraversion | Alex | Create silence / direct challenge, see if candidate fills it |
  | Agreeableness | Jordan | Create disagreement, observe cooperation |
  | Neuroticism | Alex | Apply mild pressure, observe stress response |

- [ ] Enhanced A2A Task with trait context:

  ```json
  {
    "task_id": "turn_008_jordan",
    "task_type": "respond_in_discussion",
    "input": {
      "conversation_history": [...],
      "your_role": "supportive_collaborator",
      "elicitation_goal": "probe_agreeableness",
      "trait_context": {
        "traits_observed": {"O": 0.6, "E": 0.8, "A": null, "C": null, "N": 0.4},
        "traits_to_probe": ["A", "C"],
        "candidate_engagement": "high",
        "turns_remaining": 7
      },
      "strategy_hint": "Create a mild disagreement with Alex's previous point and see if the candidate takes sides or mediates"
    }
  }
  ```

#### Files to create/modify:
- Create `agents/trait_tracker.py` - Trait tracking logic
- Modify `agents/moderator.py` - Add adaptive turn selection + trait dispatch
- Modify `agents/participant_agents/*.py` - Handle elicitation goals in prompts

---

### Phase 5: Dual-View Report (Target: Feb 20-21)
**Status:** Not Started

#### Tasks:
- [ ] Candidate report view
  - OCEAN trait scores (normalized 0-100%)
  - Top 3 CCS skills demonstrated
  - Key evidence quotes (positive framing)
  - No raw scores or technical details

- [ ] HR manager report view (admin dashboard)
  - Full OCEAN scores with confidence intervals
  - All CCS skills with individual evidence
  - BFI-44 vs AI-inferred comparison chart
  - Conversation transcript with trait annotations
  - Survey responses

- [ ] Report data structure:
  ```json
  {
    "participant_id": "P001",
    "job_role": "Product Manager",
    "scenario": "product_team",
    "bfi44_scores": {"O": 0.72, "C": 0.65, ...},
    "ai_inferred_scores": {"O": 0.68, "C": 0.71, ...},
    "ccs_skills": [
      {"skill": "Decision Making", "score": 4.2, "evidence": ["..."]}
    ],
    "trait_correlation": 0.85,
    "survey_accuracy_rating": 4
  }
  ```

#### Files to modify:
- `ui/pages/results_page.py` - Candidate-friendly report
- `ui/pages/admin_dashboard.py` - HR detailed report view
- Create `ui/components/report_card.py` - Reusable report components

---

### Phase 6: Enhanced Post-Survey (Target: Feb 21-22)
**Status:** Not Started

#### Tasks:
- [ ] Add report accuracy questions:
  - "The personality assessment accurately reflects who I am" (1-5)
  - "The skills assessment matches my self-perception" (1-5)
  - "Which trait felt most/least accurate?" (dropdown)

- [ ] Add reflection questions:
  - "Did the AI teammates feel realistic?" (1-5)
  - "Did you behave naturally during the discussion?" (1-5)
  - "Any moments that felt scripted or artificial?" (open text)

- [ ] Data collection for FYP:
  - Self-reported accuracy validates AI inference
  - Qualitative feedback for thesis discussion section

#### Files to modify:
- `ui/pages/survey_page.py` - Add accuracy questions
- Update survey data model

---

### Phase 7: Data Export & Analysis (Target: Feb 22-23)
**Status:** Not Started

#### Tasks:
- [ ] Export functionality in admin dashboard
  - CSV export: All participants, BFI-44 vs AI scores
  - JSON export: Full session data with transcripts
  - PDF export: Individual participant reports

- [ ] Correlation analysis helpers
  - Pearson correlation: BFI-44 vs AI-inferred per trait
  - Visualization: Scatter plots, Bland-Altman plots
  - Statistical summary for FYP report

#### Files to create:
- `ui/services/export_service.py` - Export logic
- `ui/components/correlation_chart.py` - Visualization

---

## Design Decisions

### Q1: Same scenario across job roles?
**Decision:** Use SAME scenario (Product Team) for all participants

**Rationale:**
- Research validity: Controlled stimulus
- Personality traits are context-independent
- Easier to compare across participants
- Reduces confounding variables

**Alternative considered:** Random assignment to 2-3 scenarios to control for scenario-specific effects. Could implement later if needed.

---

### Q2: Show report to candidate?
**Decision:** YES - Show report BEFORE post-survey

**Rationale:**
- Enables "accuracy" questions in survey
- Provides self-report vs AI-inferred validation data
- More engaging candidate experience
- Reflection improves survey quality

**Report visibility:**
| Element | Candidate | HR Manager |
|---------|-----------|------------|
| OCEAN scores | Yes (simplified) | Yes (detailed) |
| CCS skills | Yes (top 3) | Yes (all) |
| Evidence quotes | Yes (curated) | Yes (all) |
| BFI-44 comparison | No | Yes |
| Transcript | No | Yes |
| Survey responses | No | Yes |

---

### Q3: A2A Protocol vs Custom JSON?
**Decision:** YES — Use Hybrid A2A Protocol

**Previous decision (reversed):** Was "NO — stick with enhanced JSON". Reversed because:
- A2A protocol itself is free (Google open-source)
- LLM costs are the same whether using A2A or custom JSON (driven by multi-agent architecture, not protocol choice)
- A2A provides standardized agent discovery, task lifecycle, and message format — replacing custom code we'd write anyway
- Scalability: adding agents 4, 5, 6 becomes trivial (deploy Agent Card + register)
- Thesis value: using a recognized industry protocol demonstrates engineering maturity

**Hybrid approach:** Moderator Agent provides centralized control (reproducibility, trait coverage guarantees) while each Participant Agent is an independent A2A agent (distinct voice, own memory, own LLM call).

| Factor | Custom JSON | Hybrid A2A (chosen) | Full A2A |
|--------|-------------|----------------------|----------|
| LLM cost | Same | Same | Same |
| Protocol cost | Free | Free | Free |
| Dev time (initial) | ~2 days | ~3-4 days | +10-14 days |
| Dev time (add agent) | Rewrite orchestration | Deploy Agent Card | Deploy Agent Card |
| Agent voice quality | Blurs at 5+ agents | Distinct per agent | Distinct per agent |
| Reproducibility | High | High (Moderator controls) | Lower (emergent) |
| Debugging | Easy | Moderate (per-agent logs) | Hard |
| Research validity | Controlled | Controlled | Variable |
| Thesis presentation | Custom solution | "Uses Google A2A" | "Uses Google A2A" |

---

## File Structure (New/Modified)

```
agents/                                # NEW: A2A agent layer
├── base_agent.py                      # A2A base class (shared by all agents)
├── moderator.py                       # Moderator agent (turn selection, trait tracking)
├── trait_tracker.py                   # Trait/skill tracking logic
├── registry.py                        # Agent discovery and registration
├── participant_agents/
│   ├── alex.py                        # Assertive, challenging
│   ├── jordan.py                      # Supportive, collaborative
│   └── riley.py                       # Skeptical, detail-oriented
└── agent_cards/
    ├── alex.json                      # A2A Agent Card
    ├── jordan.json                    # A2A Agent Card
    └── riley.json                     # A2A Agent Card

ui/
├── app.py                             # Modified: Remove candidate mode toggles
├── schema_config.py                   # Existing: CCS skills config
├── pages/
│   ├── admin_dashboard.py             # Modified: Session registration, reports
│   ├── consent_page.py                # Modified: UserId sign-in only
│   ├── bfi44_page.py                  # No changes
│   ├── group_discussion_page.py       # Modified: Wire to A2A Moderator
│   ├── results_page.py                # Modified: Candidate report view
│   └── survey_page.py                 # Modified: Accuracy questions
├── services/
│   ├── session_service.py             # New: Session management
│   └── export_service.py              # New: Data export
└── components/
    ├── report_card.py                 # New: Report UI components
    └── correlation_chart.py           # New: Visualization
```

---

## Timeline Summary

| Phase | Description | Target Date | Status |
|-------|-------------|-------------|--------|
| 1 | Admin Session Management | Feb 14-15 | Not Started |
| 2 | UserId-Based Sign-In | Feb 15-16 | Not Started |
| 3 | A2A Agent Infrastructure | Feb 16-18 | Not Started |
| 4 | Adaptive AI Bot Behavior | Feb 18-20 | Not Started |
| 5 | Dual-View Report | Feb 20-21 | Not Started |
| 6 | Enhanced Post-Survey | Feb 21-22 | Not Started |
| 7 | Data Export & Analysis | Feb 22-23 | Not Started |

**Total estimated duration:** 10-11 days

---

## Notes

- All dates are tentative and depend on complexity discovered during implementation
- Phase 3 (A2A Infrastructure) and Phase 4 (Adaptive Behavior) are the most complex phases
- Phase 3 should produce a working group discussion with A2A agents before Phase 4 adds intelligence
- Demo mode should continue to work for testing without backend
- Consider user testing after Phase 5 to validate UX before adding survey changes
- To add agents 4 and 5 later: create agent file, Agent Card JSON, and register in registry — no architectural changes needed
