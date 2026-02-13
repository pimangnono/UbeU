# Annotation Tool: UI/UX Design Specification

## Executive Summary

This document specifies the design for a **Human Annotation Interface** that enables blind evaluation of synthetic group interview dialogues. The tool serves two purposes:

1. **Validation**: Collect human personality judgments to compare against ground truth
2. **Presentation**: Provide a visually compelling demonstration for thesis defense

**Design Philosophy**: Minimize cognitive load, maximize annotation consistency, prevent bias contamination.

---

## 1. System Overview

### 1.1 Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ANNOTATION TOOL ARCHITECTURE                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Session    │     │   Streamlit      │     │   Annotation     │
│   JSON Files │────▶│   Application    │────▶│   Output JSON    │
│  (Blinded)   │     │                  │     │                  │
└──────────────┘     └──────────────────┘     └──────────────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  IRR Calculator  │
                     │  (Post-process)  │
                     └──────────────────┘
```

### 1.2 User Roles

| Role | Access | Purpose |
|------|--------|---------|
| **Rater** | Annotation interface only | Provide blind evaluations |
| **Researcher** | Full system + ground truth | Analyze results, calculate IRR |
| **Demo Viewer** | Playback mode only | Watch simulation replay |

---

## 2. Visual Design Specification

### 2.1 Main Interface Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🔥 Pressure Cooker Annotation Tool              [Rater: R01] [Progress: 3/50] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────┐  ┌──────────────────────────────────┐  │
│  │                                 │  │  CONVERSATION LOG                │  │
│  │      2D MEETING SCENE           │  │  ┌────────────────────────────┐  │  │
│  │                                 │  │  │ [T1] Manager:              │  │  │
│  │         [Manager]               │  │  │ "예산이 40% 삭감되었습니다" │  │  │
│  │            👔                   │  │  └────────────────────────────┘  │  │
│  │            │                    │  │  ┌────────────────────────────┐  │  │
│  │   [Provoker]    [Mediator]      │  │  │ [T2] Provoker:             │  │  │
│  │      😠    ┌───┐    😊          │  │  │ "김 대리 파트를 없앱시다"   │  │  │
│  │      │     │ ○ │    │           │  │  └────────────────────────────┘  │  │
│  │      │     └───┘    │           │  │  ┌────────────────────────────┐  │  │
│  │      │              │           │  │  │ [T3] Candidate: ⭐         │  │  │
│  │         [Candidate]             │  │  │ "그건 좀 부당한 것 같은데요" │  │  │
│  │       💬 "그건..."              │  │  │ [Click to Annotate]        │  │  │
│  │            😰                   │  │  └────────────────────────────┘  │  │
│  │                                 │  │                                  │  │
│  └─────────────────────────────────┘  └──────────────────────────────────┘  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  ANNOTATION PANEL (appears when candidate turn selected)               │  │
│  │  ┌─────────────────────────────────────────────────────────────────┐  │  │
│  │  │ Turn 3: "그건 좀 부당한 것 같은데요..."                          │  │  │
│  │  ├─────────────────────────────────────────────────────────────────┤  │  │
│  │  │ Intent:  [Defense/Justification ▼]                              │  │  │
│  │  │                                                                  │  │  │
│  │  │ Confidence: ○ Low  ◉ Medium  ○ High                             │  │  │
│  │  │                                                                  │  │  │
│  │  │ Note (optional): [________________________]  [💾 Save] [Skip ▶] │  │  │
│  │  └─────────────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Meeting Scene Design (2D)

**Visual Requirements:**

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                     ┌──────────────────┐                        │
│                     │    Manager 👔    │                        │
│                     │   (Facilitator)  │                        │
│                     └──────────────────┘                        │
│                              │                                  │
│                              │                                  │
│    ┌─────────────┐    ┌──────────┐    ┌─────────────┐          │
│    │ Provoker 😠 │    │  TABLE   │    │ Mediator 😊 │          │
│    │ (Manager Kim)│    │    ○     │    │  (Sarah)    │          │
│    └─────────────┘    └──────────┘    └─────────────┘          │
│           │                                   │                 │
│           │                                   │                 │
│           │      ┌─────────────────┐         │                 │
│           │      │  Candidate 😰   │         │                 │
│           │      │    (Minu)       │         │                 │
│           │      │                 │         │                 │
│           │      │  💬 ┌─────────────────────┐                 │
│           │      │     │ "그건 좀 부당한    │                 │
│           │      │     │  것 같은데요..."   │                 │
│           │      │     └─────────────────────┘                 │
│           │      └─────────────────┘                           │
│                                                                 │
│  Background: Soft green gradient (meeting room atmosphere)      │
└─────────────────────────────────────────────────────────────────┘
```

**Active Speaker Indicators:**

| State | Visual Treatment |
|-------|------------------|
| Idle | Normal avatar, gray border |
| Speaking | Golden glow effect, speech bubble appears |
| Finished Speaking | Bubble fades, avatar returns to idle |
| Candidate (always highlighted) | Subtle blue background tint |

**Speech Bubble Specifications:**

```css
.speech-bubble {
    background: white;
    border: 2px solid [speaker-color];
    border-radius: 15px;
    padding: 12px 16px;
    max-width: 220px;
    font-size: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    
    /* Tail pointing to speaker */
    &::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 25px;
        border-width: 10px 10px 0;
        border-style: solid;
        border-color: [speaker-color] transparent transparent;
    }
}
```

**Color Scheme:**

| Agent | Primary Color | Semantic |
|-------|---------------|----------|
| Manager | `#4A90D9` (Blue) | Authority, Neutral |
| Provoker | `#D94A4A` (Red) | Conflict, Challenge |
| Mediator | `#4AD98F` (Green) | Harmony, Support |
| Candidate | `#D9A84A` (Gold) | Focus, Subject |

---

## 3. Conversation Log Panel

### 3.1 Turn Card Design

```
┌──────────────────────────────────────────────────────────────┐
│  [T3] Candidate                                    ⭐ 📝     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  "그건 좀 부당한 것 같은데요. 제 파트가 핵심인데            │
│   이걸 없애면 프로젝트 자체가 무너집니다."                   │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  ✅ Annotated: Defense/Justification (High confidence)       │
└──────────────────────────────────────────────────────────────┘

Legend:
  ⭐ = Candidate turn (requires annotation)
  📝 = Click to annotate/edit
  ✅ = Annotation complete
  ⚠️ = Annotation pending
```

### 3.2 Visual Differentiation

| Speaker Type | Card Style |
|--------------|------------|
| System Manager | Light blue background, small font, italicized |
| Provoker | Light red left border |
| Mediator | Light green left border |
| **Candidate** | **Gold left border, slightly larger, star icon** |

### 3.3 Interaction States

```
┌─────────────────────────────────────────┐
│  UNANNOTATED (Candidate Turn)           │
│  ┌───────────────────────────────────┐  │
│  │ [T5] Candidate              ⭐ 📝 │  │
│  │ "..." (text)                      │  │
│  │ ──────────────────────────────── │  │
│  │ ⚠️ Needs annotation               │  │
│  └───────────────────────────────────┘  │
│           │                             │
│           │ Click                       │
│           ▼                             │
│  SELECTED (Editing)                     │
│  ┌───────────────────────────────────┐  │
│  │ [T5] Candidate              ⭐ ✏️ │  │
│  │ "..." (text)                      │  │
│  │ ════════════════════════════════ │  │
│  │ 🔷 Currently editing              │  │
│  │ Border: thick gold                │  │
│  └───────────────────────────────────┘  │
│           │                             │
│           │ Save                        │
│           ▼                             │
│  ANNOTATED (Complete)                   │
│  ┌───────────────────────────────────┐  │
│  │ [T5] Candidate              ⭐ ✓  │  │
│  │ "..." (text)                      │  │
│  │ ──────────────────────────────── │  │
│  │ ✅ Defense/Justification (High)   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## 4. Annotation Panel Design

### 4.1 Two-Phase Annotation Workflow

**Critical UX Decision**: Separate **per-turn intent annotation** from **end-of-session personality rating**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ANNOTATION WORKFLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

    PHASE 1: Per-Turn Intent Annotation
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                                                                         │
    │   For EACH candidate turn:                                              │
    │                                                                         │
    │   ┌─────────────────────────────────────────────────────────────────┐  │
    │   │  Turn 3: "그건 좀 부당한 것 같은데요..."                         │  │
    │   │                                                                  │  │
    │   │  What is the PRIMARY intent of this statement?                   │  │
    │   │                                                                  │  │
    │   │  ┌──────────────────┐  ┌──────────────────┐                     │  │
    │   │  │ 🛡️ Defense       │  │ ⚔️ Attack        │                     │  │
    │   │  │ □ Justification  │  │ □ Criticism      │                     │  │
    │   │  │ □ Deflection     │  │ □ Personal       │                     │  │
    │   │  └──────────────────┘  └──────────────────┘                     │  │
    │   │                                                                  │  │
    │   │  ┌──────────────────┐  ┌──────────────────┐                     │  │
    │   │  │ 🤝 Collaboration │  │ 😟 Emotional     │                     │  │
    │   │  │ □ Proposal       │  │ □ Anxiety        │                     │  │
    │   │  │ □ Agreement      │  │ □ Frustration    │                     │  │
    │   │  │ □ Compromise     │  │ □ Enthusiasm     │                     │  │
    │   │  └──────────────────┘  └──────────────────┘                     │  │
    │   │                                                                  │  │
    │   │  ┌──────────────────┐  ┌──────────────────┐                     │  │
    │   │  │ 👉 Blame Shift   │  │ 🚪 Withdrawal    │                     │  │
    │   │  │ □ External       │  │ □ Avoidance      │                     │  │
    │   │  │ □ Colleague      │  │ □ Deferral       │                     │  │
    │   │  └──────────────────┘  └──────────────────┘                     │  │
    │   │                                                                  │  │
    │   │  Confidence: [ Low ◉ Medium ○ High ]                            │  │
    │   │                                                                  │  │
    │   │  [💾 Save & Next]                            [Skip ▶]           │  │
    │   └──────────────────────────────────────────────────────────────────┘  │
    │                                                                         │
    └─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      │ After ALL turns annotated
                                      ▼
    PHASE 2: End-of-Session Personality Rating
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                                                                         │
    │   Based on the ENTIRE conversation, rate the Candidate's personality:   │
    │                                                                         │
    │   ┌─────────────────────────────────────────────────────────────────┐  │
    │   │                                                                  │  │
    │   │   Neuroticism (Emotional Stability)                             │  │
    │   │   Calm, stable ○───○───◉───○───○ Anxious, reactive              │  │
    │   │                1   2   3   4   5                                 │  │
    │   │                                                                  │  │
    │   │   Extraversion                                                   │  │
    │   │   Reserved     ○───◉───○───○───○ Outgoing, assertive            │  │
    │   │                1   2   3   4   5                                 │  │
    │   │                                                                  │  │
    │   │   Openness                                                       │  │
    │   │   Conventional ○───○───◉───○───○ Creative, curious              │  │
    │   │                1   2   3   4   5                                 │  │
    │   │                                                                  │  │
    │   │   Agreeableness                                                  │  │
    │   │   Challenging  ○───○───○───◉───○ Cooperative, trusting          │  │
    │   │                1   2   3   4   5                                 │  │
    │   │                                                                  │  │
    │   │   Conscientiousness                                              │  │
    │   │   Careless     ○───○───◉───○───○ Organized, reliable            │  │
    │   │                1   2   3   4   5                                 │  │
    │   │                                                                  │  │
    │   │   Overall Confidence: [ Low ○ Medium ◉ High ]                   │  │
    │   │                                                                  │  │
    │   │   [Submit Session Annotation]                                    │  │
    │   └──────────────────────────────────────────────────────────────────┘  │
    │                                                                         │
    └─────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Intent Selection UI (Grouped Categories)

**Design Rationale**: Group related intents visually to reduce cognitive load.

```python
INTENT_GROUPS = {
    "Defense": {
        "icon": "🛡️",
        "color": "#5B9BD5",
        "options": [
            ("Justification", "Providing reasons or evidence"),
            ("Deflection", "Redirecting without addressing"),
        ]
    },
    "Attack": {
        "icon": "⚔️", 
        "color": "#FF6B6B",
        "options": [
            ("Criticism", "Critiquing ideas or work"),
            ("Personal", "Critiquing person's character"),
        ]
    },
    "Collaboration": {
        "icon": "🤝",
        "color": "#51CF66",
        "options": [
            ("Proposal", "Suggesting a solution"),
            ("Agreement", "Supporting another's idea"),
            ("Compromise", "Offering middle ground"),
        ]
    },
    "Emotional": {
        "icon": "😟",
        "color": "#FAB005",
        "options": [
            ("Anxiety", "Expressing worry or uncertainty"),
            ("Frustration", "Expressing irritation"),
            ("Enthusiasm", "Expressing positive engagement"),
        ]
    },
    "Blame_Shifting": {
        "icon": "👉",
        "color": "#BE4BDB",
        "options": [
            ("External", "Blaming circumstances"),
            ("Colleague", "Blaming specific person"),
        ]
    },
    "Withdrawal": {
        "icon": "🚪",
        "color": "#868E96",
        "options": [
            ("Avoidance", "Steering away from conflict"),
            ("Deferral", "Postponing decision"),
        ]
    },
    "Assertion": {
        "icon": "💪",
        "color": "#20C997",
        "options": [
            ("Confident", "Stating position with conviction"),
            ("Aggressive", "Dominating forcefully"),
        ]
    }
}
```

### 4.3 Confidence Scale Design

Use **3-point scale** (not 5) to reduce decision fatigue:

```
┌─────────────────────────────────────────────────────────────────┐
│  How confident are you in this annotation?                      │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │     😐      │  │     🙂      │  │     😊      │             │
│  │    Low      │  │   Medium    │  │    High     │             │
│  │             │  │     ◉       │  │             │             │
│  │  Guessing   │  │   Likely    │  │   Certain   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  Tooltip: "Low = Multiple intents seem equally possible"        │
│           "Medium = This seems like the best fit"               │
│           "High = I'm very sure about this"                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Blind Annotation Protocol

### 5.1 Information Hiding Rules

**MUST HIDE from Raters:**

| Hidden Element | Reason |
|----------------|--------|
| Ground truth personality scores | Prevents confirmation bias |
| Ground truth intent tags | Prevents anchoring |
| Profile label (e.g., "defensive_anxious") | Prevents stereotyping |
| Candidate's inner thoughts | These are simulation artifacts |
| Behavior notes | These are automated, not ground truth |
| Other raters' annotations | Prevents groupthink |

**MUST SHOW to Raters:**

| Visible Element | Reason |
|-----------------|--------|
| Scenario description | Provides context |
| All speaker text | Required for judgment |
| Turn numbers | Navigation |
| Speaker roles (not personality) | Attribution |

### 5.2 Session Blinding Function

```python
def prepare_blinded_session(raw_session: dict) -> dict:
    """
    Remove all ground truth labels for blind annotation.
    
    Input: Full session JSON with all metadata
    Output: Blinded session safe for rater viewing
    """
    
    blinded = {
        "session_id": raw_session["meta_data"]["session_id"],
        "scenario": {
            "title": raw_session["meta_data"]["scenario"]["title"],
            "description": raw_session["meta_data"]["scenario"]["setup"],
            # DO NOT include: elicits, assessment_mapping
        },
        "participants": [
            {"role": "Manager", "name": "Facilitator"},
            {"role": "Provoker", "name": "Manager Kim"},
            {"role": "Mediator", "name": "Sarah"},
            {"role": "Candidate", "name": "Minu"}
            # DO NOT include: personality scores, behavioral focus
        ],
        "dialogue": [
            {
                "turn_id": turn["turn_id"],
                "speaker_role": turn["speaker_role"],
                "text": turn["text"],
                # DO NOT include: intent_tag, inner_thought, behavior_notes
            }
            for turn in raw_session["dialogue_log"]
        ]
    }
    
    return blinded
```

### 5.3 Preventing Bias Leakage

**UI Safeguards:**

```python
# In Streamlit app
def validate_session_is_blinded(session: dict) -> bool:
    """Verify no ground truth leaked into session data."""
    
    FORBIDDEN_KEYS = [
        "ground_truth_personality",
        "intent_tag",
        "inner_thought",
        "behavior_notes",
        "expected_behaviors",
        "profile_label",
        "bfi_prompts_used"
    ]
    
    session_str = json.dumps(session)
    
    for key in FORBIDDEN_KEYS:
        if key in session_str:
            raise ValueError(f"BIAS LEAK DETECTED: {key} found in session")
    
    return True
```

---

## 6. Rater Management

### 6.1 Rater Onboarding Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          RATER ONBOARDING                                    │
└─────────────────────────────────────────────────────────────────────────────┘

Step 1: Registration
┌─────────────────────────────────────────────────────────────────┐
│  Welcome to the Annotation Tool                                 │
│                                                                 │
│  Please enter your Rater ID: [___________]                      │
│                                                                 │
│  (This will be assigned by the researcher)                      │
│                                                                 │
│  [Continue →]                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
Step 2: Instructions
┌─────────────────────────────────────────────────────────────────┐
│  📋 Annotation Instructions                                     │
│                                                                 │
│  You will watch simulated group interviews and:                 │
│                                                                 │
│  1. For each CANDIDATE statement, identify the PRIMARY intent   │
│  2. After the full conversation, rate the candidate's           │
│     personality on 5 dimensions                                 │
│                                                                 │
│  ⚠️ Important:                                                  │
│  • Focus only on what you SEE in the text                       │
│  • Don't assume hidden motivations                              │
│  • If unsure, use Low confidence and your best guess            │
│                                                                 │
│  [I understand, continue →]                                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
Step 3: Practice Session
┌─────────────────────────────────────────────────────────────────┐
│  🎯 Practice Annotation                                         │
│                                                                 │
│  Let's try one practice session to make sure you understand.    │
│                                                                 │
│  [Start Practice →]                                             │
│                                                                 │
│  (Practice session does not count toward study data)            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
Step 4: Begin Actual Annotation
┌─────────────────────────────────────────────────────────────────┐
│  ✅ You're ready!                                               │
│                                                                 │
│  You have been assigned 50 sessions to annotate.                │
│  Estimated time: 2-3 hours total (can be split across days)     │
│                                                                 │
│  Progress is saved automatically.                               │
│                                                                 │
│  [Begin Session 1 →]                                            │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Session Assignment Strategy

**For Inter-Rater Reliability (IRR):**

```python
# Assignment matrix for 50 sessions with 3 raters
SESSION_ASSIGNMENTS = {
    # Core IRR set: ALL raters annotate these (for calculating agreement)
    "irr_core": {
        "sessions": ["sim_001", "sim_002", ..., "sim_020"],  # 20 sessions
        "raters": ["R01", "R02", "R03"]  # All 3 raters
    },
    
    # Extended set: Each session gets 1 rater (for coverage)
    "extended": {
        "sim_021": ["R01"],
        "sim_022": ["R02"],
        "sim_023": ["R03"],
        # ... distributed evenly
    }
}

# Result:
# - 20 sessions × 3 raters = 60 annotations for IRR calculation
# - 30 sessions × 1 rater = 30 additional annotations for coverage
# - Total: 50 unique sessions, 90 total annotations
```

---

## 7. Progress & Feedback

### 7.1 Progress Indicators

```
┌─────────────────────────────────────────────────────────────────┐
│  SESSION PROGRESS                                               │
│                                                                 │
│  Session 7 of 50                                                │
│  ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 14%          │
│                                                                 │
│  Current Session: Turn 4 of 15                                  │
│  Candidate turns annotated: 1 of 5  ⭐⚪⚪⚪⚪                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Completion Feedback

```
┌─────────────────────────────────────────────────────────────────┐
│  ✅ Session Complete!                                           │
│                                                                 │
│  Summary:                                                       │
│  • Turns annotated: 5/5                                         │
│  • Average confidence: Medium                                   │
│  • Time spent: 4 min 23 sec                                     │
│                                                                 │
│  Your personality ratings for this candidate:                   │
│  N: ████░ 4.0   E: ██░░░ 2.0   O: ███░░ 3.0                    │
│  A: ██░░░ 2.0   C: ██░░░ 2.0                                    │
│                                                                 │
│  [Next Session →]  [Take a Break]  [Save & Exit]               │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 Fatigue Prevention

```python
# Automatic break reminders
FATIGUE_THRESHOLDS = {
    "sessions_before_break": 10,
    "minutes_before_break": 30,
    "max_sessions_per_day": 25
}

def check_fatigue(rater_stats: dict) -> Optional[str]:
    """Return break recommendation if thresholds exceeded."""
    
    if rater_stats["sessions_today"] >= FATIGUE_THRESHOLDS["max_sessions_per_day"]:
        return "daily_limit_reached"
    
    if rater_stats["consecutive_sessions"] >= FATIGUE_THRESHOLDS["sessions_before_break"]:
        return "break_recommended"
    
    if rater_stats["minutes_since_break"] >= FATIGUE_THRESHOLDS["minutes_before_break"]:
        return "break_recommended"
    
    return None
```

**Break Reminder UI:**

```
┌─────────────────────────────────────────────────────────────────┐
│  ☕ Time for a break!                                           │
│                                                                 │
│  You've completed 10 sessions. Great work!                      │
│                                                                 │
│  Taking short breaks helps maintain annotation quality.         │
│  We recommend a 5-10 minute break.                              │
│                                                                 │
│  [Continue Anyway]  [Take Break (5 min)]  [Save & Exit]        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Data Export Format

### 8.1 Per-Session Annotation Output

```json
{
  "annotation_meta": {
    "session_id": "sim_2024_0120_001",
    "rater_id": "R01",
    "started_at": "2024-01-20T14:30:00Z",
    "completed_at": "2024-01-20T14:34:23Z",
    "duration_seconds": 263,
    "tool_version": "1.0.0"
  },
  
  "turn_annotations": [
    {
      "turn_id": 3,
      "speaker_role": "Candidate",
      "annotated_intent": "Defense/Justification",
      "confidence": "high",
      "note": null,
      "time_to_annotate_ms": 4200
    },
    {
      "turn_id": 5,
      "speaker_role": "Candidate",
      "annotated_intent": "Emotional/Anxiety",
      "confidence": "medium",
      "note": "Seemed flustered by the personal attack",
      "time_to_annotate_ms": 6100
    }
  ],
  
  "personality_rating": {
    "Neuroticism": 4.0,
    "Extraversion": 2.5,
    "Openness": 3.0,
    "Agreeableness": 2.0,
    "Conscientiousness": 2.0,
    "overall_confidence": "medium"
  },
  
  "quality_flags": {
    "all_turns_annotated": true,
    "personality_complete": true,
    "avg_confidence": "medium",
    "suspected_low_effort": false
  }
}
```

### 8.2 Aggregated IRR Export

```json
{
  "irr_report": {
    "generated_at": "2024-01-25T10:00:00Z",
    "n_sessions": 20,
    "n_raters": 3,
    "n_total_annotations": 60
  },
  
  "intent_agreement": {
    "krippendorff_alpha": 0.72,
    "interpretation": "Substantial agreement",
    "per_category_agreement": {
      "Defense": 0.78,
      "Attack": 0.81,
      "Collaboration": 0.69,
      "Emotional": 0.65,
      "Blame_Shifting": 0.74,
      "Withdrawal": 0.58
    }
  },
  
  "personality_agreement": {
    "icc_two_way_random": {
      "Neuroticism": 0.81,
      "Extraversion": 0.76,
      "Openness": 0.52,
      "Agreeableness": 0.71,
      "Conscientiousness": 0.68
    },
    "mean_icc": 0.70
  },
  
  "quality_metrics": {
    "completion_rate": 1.0,
    "avg_time_per_session_seconds": 285,
    "low_confidence_rate": 0.12
  }
}
```

---

## 9. Playback Mode (Demo)

### 9.1 Auto-Play Feature

For thesis defense demo, include an auto-play mode:

```
┌─────────────────────────────────────────────────────────────────┐
│  🎬 DEMO MODE: Auto-Playback                                    │
│                                                                 │
│  Speed: [ Slow ◉ Normal ○ Fast ]                                │
│                                                                 │
│  [▶ Play] [⏸ Pause] [⏮ Restart] [⏭ Skip to End]               │
│                                                                 │
│  ─────────────────●───────────────────────────────              │
│  Turn 6 of 15                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 Playback Timing

```python
PLAYBACK_SPEEDS = {
    "slow": {
        "text_reveal_ms_per_char": 50,  # Typewriter effect
        "pause_after_turn_ms": 2000,
        "bubble_fade_ms": 500
    },
    "normal": {
        "text_reveal_ms_per_char": 30,
        "pause_after_turn_ms": 1200,
        "bubble_fade_ms": 300
    },
    "fast": {
        "text_reveal_ms_per_char": 10,
        "pause_after_turn_ms": 600,
        "bubble_fade_ms": 200
    }
}
```

---

## 10. Implementation Checklist

### 10.1 MVP (Minimum Viable Product) - Day 1

- [ ] Basic Streamlit layout (scene + chat + annotation panel)
- [ ] 2D meeting scene with avatar positions
- [ ] Speech bubble for active speaker
- [ ] Load blinded session from JSON
- [ ] Intent selection (grouped buttons)
- [ ] Save annotation to JSON file

### 10.2 Complete Version - Day 2

- [ ] Rater ID and progress tracking
- [ ] End-of-session personality rating
- [ ] Confidence indicators
- [ ] Export functionality
- [ ] Multiple session navigation
- [ ] Break reminders

### 10.3 Polish - Day 3 (if time permits)

- [ ] Auto-play demo mode
- [ ] Avatar images (replace emojis)
- [ ] Animations (bubble appear/fade)
- [ ] IRR calculation script
- [ ] Instructions/onboarding flow

---

## 11. Success Metrics

### 11.1 Annotation Quality Targets

| Metric | Target | Minimum Acceptable |
|--------|--------|-------------------|
| Krippendorff's α (Intent) | ≥ 0.70 | ≥ 0.60 |
| ICC (Personality) | ≥ 0.70 | ≥ 0.60 |
| Completion Rate | 100% | ≥ 95% |
| Avg Confidence | Medium-High | ≥ Low-Medium |

### 11.2 Usability Targets

| Metric | Target |
|--------|--------|
| Time per session | 3-5 minutes |
| Rater reported ease | ≥ 4/5 |
| Zero critical errors | Required |

---

## 12. Appendix: Complete Streamlit Code Template

See `annotation_app.py` in the implementation package.

```python
# Run with: streamlit run annotation_app.py
# Requires: pip install streamlit
```
