"""
FastAPI backend for Step 2: Live Interview Platform.

Endpoints:
  POST /participant              — create participant, assign scenario
  POST /participant/{pid}/consent — record consent
  POST /participant/{pid}/bfi44  — submit BFI-44, score, store ground truth
  POST /session/create           — create LiveEngine, return opening message
  GET  /session/{sid}/status     — get conversation history + state
  POST /session/{sid}/message    — submit human message, return AI responses
  POST /session/{sid}/end        — end session + run Senior Analyst validation
  POST /participant/{pid}/survey — submit post-session survey
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()

from clients.llm_client import create_client, LLMClient
from step2.bfi44 import score_bfi44
from step2.consulting_scenarios import get_consulting_scenario
from step2.validator_agent import validate_session
from step2.models import (
    SessionState,
    PostSessionSurvey,
    CreateParticipantRequest,
    CreateParticipantResponse,
    ConsentRequest,
    BFI44SubmitRequest,
    BFI44SubmitResponse,
    CreateSessionRequest,
    CreateSessionResponse,
    SessionStatusResponse,
    SubmitMessageRequest,
    SubmitMessageResponse,
    SurveySubmitRequest,
)
from step2.participant import ParticipantManager
from step2.session_manager import SessionManager

# --- App initialization ---

app = FastAPI(
    title="Pressure Cooker — Step 2 Live Interview",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global singletons (initialized on startup)
_client = None
_validator_client = None
_participant_mgr = None
_session_mgr = None


@app.on_event("startup")
async def startup():
    global _client, _validator_client, _participant_mgr, _session_mgr
    _client = create_client()
    # Senior Analyst uses Claude Haiku 4.5 via OpenRouter for post-session validation
    _validator_client = LLMClient(
        pro_model="anthropic/claude-haiku-4.5",
    )
    _participant_mgr = ParticipantManager()
    _session_mgr = SessionManager(client=_client)


def _get_participant_mgr() -> ParticipantManager:
    assert _participant_mgr is not None
    return _participant_mgr


def _get_session_mgr() -> SessionManager:
    assert _session_mgr is not None
    return _session_mgr


# --- Participant endpoints ---

@app.post("/participant", response_model=CreateParticipantResponse)
async def create_participant(req: CreateParticipantRequest):
    """Create a new participant and assign a counterbalanced scenario."""
    mgr = _get_participant_mgr()
    record = mgr.create_participant(name=req.name)
    return CreateParticipantResponse(
        participant_id=record.participant_id,
        assigned_scenario=record.assigned_scenario,
    )


@app.post("/participant/{pid}/consent")
async def record_consent(pid: str, req: ConsentRequest):
    """Record participant consent."""
    mgr = _get_participant_mgr()
    record = mgr.get_participant(pid)
    if record is None:
        raise HTTPException(404, f"Participant {pid} not found")

    record.consent_given = req.consent
    record.consent_timestamp = datetime.now()
    mgr.update_participant(record)
    return {"status": "ok", "consent": req.consent}


@app.post("/participant/{pid}/bfi44", response_model=BFI44SubmitResponse)
async def submit_bfi44(pid: str, req: BFI44SubmitRequest):
    """Submit BFI-44 responses, score them, and store ground truth."""
    mgr = _get_participant_mgr()
    record = mgr.get_participant(pid)
    if record is None:
        raise HTTPException(404, f"Participant {pid} not found")

    # Convert string keys to ints (JSON serialization may stringify keys)
    responses = {int(k): v for k, v in req.responses.items()}

    try:
        scores = score_bfi44(responses)
    except ValueError as e:
        raise HTTPException(400, str(e))

    record.bfi44_raw = responses
    record.bfi44_scores = scores
    record.bfi44_duration_seconds = req.duration_seconds
    mgr.update_participant(record)

    return BFI44SubmitResponse(participant_id=pid, scores_computed=True)


# --- Session endpoints ---

@app.post("/session/create", response_model=CreateSessionResponse)
async def create_session(req: CreateSessionRequest):
    """Create a live interview session and return the opening messages."""
    p_mgr = _get_participant_mgr()
    s_mgr = _get_session_mgr()

    record = p_mgr.get_participant(req.participant_id)
    if record is None:
        raise HTTPException(404, f"Participant {req.participant_id} not found")
    if not record.consent_given:
        raise HTTPException(400, "Participant has not given consent")
    if record.bfi44_scores is None:
        raise HTTPException(400, "BFI-44 not yet completed")
    if record.assigned_scenario is None:
        raise HTTPException(400, "No scenario assigned")

    # Check for existing session
    existing = s_mgr.get_session_by_participant(req.participant_id)
    if existing and existing.state != SessionState.ENDED:
        # Return existing session
        return CreateSessionResponse(
            session_id=existing.session_id,
            opening_messages=[
                {"speaker": t.speaker_name, "content": t.content}
                for t in existing.engine.turns
            ],
        )

    # Load consulting case study
    case_study = None
    try:
        case_study = get_consulting_scenario(record.assigned_scenario)
    except ValueError:
        pass  # Fall back to legacy scenario if not a consulting scenario ID

    # Create new session
    session = s_mgr.create_session(
        participant_id=req.participant_id,
        scenario_id=record.assigned_scenario,
        participant_name=record.name,
        case_study=case_study,
    )

    # Update participant with session ID
    record.session_id = session.session_id
    p_mgr.update_participant(record)

    # Generate opening (compensate timer — LLM latency for opening shouldn't count)
    llm_start = time.time()
    opening_turns = await session.engine.generate_opening()
    if session.engine.start_time is not None:
        session.engine.start_time += time.time() - llm_start

    # Persist state
    s_mgr.persist_session(session.session_id)

    return CreateSessionResponse(
        session_id=session.session_id,
        opening_messages=[
            {"speaker": t.speaker_name, "content": t.content}
            for t in opening_turns
        ],
    )


@app.get("/session/{sid}/status", response_model=SessionStatusResponse)
async def get_session_status(sid: str):
    """Get current session status and conversation history."""
    s_mgr = _get_session_mgr()
    session = s_mgr.get_session(sid)

    if session is None:
        # Try restoring from disk
        session = s_mgr.restore_session(sid)
        if session is None:
            raise HTTPException(404, f"Session {sid} not found")

    engine = session.engine
    return SessionStatusResponse(
        session_id=sid,
        state=engine.state,
        conversation=engine.get_conversation_dicts(),
        elapsed_seconds=engine.elapsed_seconds,
        remaining_seconds=engine.remaining_seconds,
    )


@app.post("/session/{sid}/message", response_model=SubmitMessageResponse)
async def submit_message(sid: str, req: SubmitMessageRequest):
    """Submit a human message and get AI responses back."""
    s_mgr = _get_session_mgr()
    session = s_mgr.get_session(sid)
    if session is None:
        raise HTTPException(404, f"Session {sid} not found")

    engine = session.engine

    if engine.state == SessionState.ENDED:
        raise HTTPException(400, "Session has ended")

    if engine.is_time_expired:
        # Force end
        closing = await engine.end_session()
        s_mgr.persist_session(sid)
        ai_turns = [{"speaker": closing.speaker_name, "content": closing.content}] if closing else []
        return SubmitMessageResponse(
            ai_turns=ai_turns,
            session_state=engine.state,
            elapsed_seconds=engine.elapsed_seconds,
            remaining_seconds=engine.remaining_seconds,
        )

    # Record human turn
    engine.submit_human_turn(req.content)

    # Generate AI responses until it's the human's turn again
    # Compensate engine timer: LLM latency shouldn't count against participant
    llm_start = time.time()
    try:
        ai_turns = await engine.generate_ai_turns_until_human(
            target_speaker=req.target_speaker,
        )
    except Exception as e:
        # Compensate timer even on error
        if engine.start_time is not None:
            engine.start_time += time.time() - llm_start
        s_mgr.persist_session(sid)
        raise HTTPException(
            503,
            detail=f"AI response timed out. Please try again. ({type(e).__name__})",
        )
    # Shift start_time forward so LLM wait doesn't count as elapsed discussion time
    if engine.start_time is not None:
        engine.start_time += time.time() - llm_start

    # Persist state
    s_mgr.persist_session(sid)

    return SubmitMessageResponse(
        ai_turns=[
            {"speaker": t.speaker_name, "content": t.content}
            for t in ai_turns
        ],
        session_state=engine.state,
        elapsed_seconds=engine.elapsed_seconds,
        remaining_seconds=engine.remaining_seconds,
    )


@app.post("/session/{sid}/end")
async def end_session(sid: str):
    """Manually end a session and run post-session validation."""
    s_mgr = _get_session_mgr()
    session = s_mgr.get_session(sid)
    if session is None:
        raise HTTPException(404, f"Session {sid} not found")

    closing = await session.engine.end_session()

    # Finalize and persist session output
    p_mgr = _get_participant_mgr()
    record = p_mgr.get_participant(session.participant_id)

    output = await session.engine.finalize_session_output(session.participant_id)
    p_mgr.save_session_output(session.participant_id, output.model_dump())

    # Run Senior Analyst post-session validation (Claude Haiku 4.5)
    validation_report = None
    if _validator_client and session.engine.case_study:
        try:
            validation_report = await validate_session(
                transcript=session.engine.turns,
                case_study=session.engine.case_study,
                client=_validator_client,
            )
            # Save validation report
            participant_dir = p_mgr._get_dir(session.participant_id)
            participant_dir.mkdir(parents=True, exist_ok=True)
            validation_path = participant_dir / "logic_validation.json"
            with open(validation_path, "w") as f:
                json.dump(validation_report, f, indent=2)
        except Exception as e:
            # Don't fail the session end if validation fails
            validation_report = {"error": str(e)}
            # Still save the error report to disk for debugging
            try:
                participant_dir = p_mgr._get_dir(session.participant_id)
                participant_dir.mkdir(parents=True, exist_ok=True)
                validation_path = participant_dir / "logic_validation.json"
                with open(validation_path, "w") as f:
                    json.dump(validation_report, f, indent=2)
            except Exception:
                pass

    s_mgr.persist_session(sid)

    validation_error = None
    if validation_report and "error" in validation_report:
        validation_error = validation_report["error"]

    return {
        "status": "ended",
        "total_turns": len(session.engine.turns),
        "closing_message": closing.content if closing else None,
        "validation_completed": validation_report is not None and "error" not in validation_report,
        "validation_error": validation_error,
    }


# --- Survey endpoint ---

@app.post("/participant/{pid}/survey")
async def submit_survey(pid: str, req: SurveySubmitRequest):
    """Submit post-session experience survey."""
    mgr = _get_participant_mgr()
    record = mgr.get_participant(pid)
    if record is None:
        raise HTTPException(404, f"Participant {pid} not found")

    survey = PostSessionSurvey(
        participant_id=pid,
        naturalness=req.naturalness,
        authenticity=req.authenticity,
        realism=req.realism,
        engagement=req.engagement,
        recommendation=req.recommendation,
        open_feedback=req.open_feedback,
    )
    record.survey = survey
    mgr.update_participant(record)

    return {"status": "ok", "mean_score": survey.mean_score()}


# --- Health check ---

@app.get("/health")
async def health():
    return {"status": "ok", "service": "pressure-cooker-step2"}
