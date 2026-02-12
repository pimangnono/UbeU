"""
FastAPI Backend for V3: Dual-Mode AI Interview Platform.

Endpoints:
  POST /participant              — create participant, assign condition
  POST /participant/{pid}/consent — record consent
  POST /participant/{pid}/bfi44  — submit BFI-44, score, store ground truth
  POST /session/create           — create CaseEngine or GroupEngine session
  GET  /session/{sid}/status     — get conversation history + state
  POST /session/{sid}/message    — submit message, return AI responses
  POST /session/{sid}/end        — end session, run evaluation
  POST /participant/{pid}/survey — submit post-study survey
  GET  /hr/candidates            — list all completed candidates
  GET  /hr/candidate/{pid}       — get full candidate report
  GET  /hr/compare               — multi-candidate comparison view
"""

import sys
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()

from clients.llm_client import create_client, LLMClient
from server.bfi44 import score_bfi44
from server.models import (
    StudyPhase,
    InterviewMode,
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
    EndSessionRequest,
    EndSessionResponse,
    SurveySubmitRequest,
    PostSessionSurvey,
    CandidateSummary,
    CandidateComparison,
    CandidateReport,
)
from server.participant_manager import ParticipantManager
from server.session_manager import SessionManager
from utils.models import SessionState

# --- App initialization ---

app = FastAPI(
    title="UbeU V3 — Dual-Mode AI Interview Platform",
    version="3.0.0",
    description="Within-subject study: Mode 1 (Case Study) + Mode 2 (Group Discussion)",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global singletons
_client: LLMClient = None
_participant_mgr: ParticipantManager = None
_session_mgr: SessionManager = None


@app.on_event("startup")
async def startup():
    global _client, _participant_mgr, _session_mgr
    _client = create_client()
    _participant_mgr = ParticipantManager()
    _session_mgr = SessionManager(client=_client)


def _get_participant_mgr() -> ParticipantManager:
    assert _participant_mgr is not None
    return _participant_mgr


def _get_session_mgr() -> SessionManager:
    assert _session_mgr is not None
    return _session_mgr


# =============================================================================
# PARTICIPANT ENDPOINTS
# =============================================================================

@app.post("/participant", response_model=CreateParticipantResponse)
async def create_participant(req: CreateParticipantRequest):
    """Create a new participant with counterbalanced condition assignment."""
    mgr = _get_participant_mgr()
    record = mgr.create_participant(name=req.name, email=req.email)

    first_mode = "case" if record.condition.value == "case_first" else "group"

    return CreateParticipantResponse(
        participant_id=record.participant_id,
        condition=record.condition,
        first_mode=first_mode,
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
    if req.consent:
        record.current_phase = StudyPhase.BFI44
    mgr.update_participant(record)

    return {"status": "ok", "consent": req.consent, "next_phase": record.current_phase.value}


@app.post("/participant/{pid}/bfi44", response_model=BFI44SubmitResponse)
async def submit_bfi44(pid: str, req: BFI44SubmitRequest):
    """Submit BFI-44 responses, score them, and store ground truth."""
    mgr = _get_participant_mgr()
    record = mgr.get_participant(pid)
    if record is None:
        raise HTTPException(404, f"Participant {pid} not found")

    # Convert string keys to ints
    responses = {int(k): v for k, v in req.responses.items()}

    try:
        scores = score_bfi44(responses)
    except ValueError as e:
        raise HTTPException(400, str(e))

    record.bfi44_raw = responses
    record.bfi44_scores = scores
    record.bfi44_duration_seconds = req.duration_seconds

    # Advance to first interview
    next_phase = mgr.advance_phase(pid)

    return BFI44SubmitResponse(
        participant_id=pid,
        scores_computed=True,
        next_phase=next_phase,
    )


# =============================================================================
# SESSION ENDPOINTS
# =============================================================================

@app.post("/session/create", response_model=CreateSessionResponse)
async def create_session(req: CreateSessionRequest):
    """Create a new interview session (Mode 1 or Mode 2)."""
    p_mgr = _get_participant_mgr()
    s_mgr = _get_session_mgr()

    record = p_mgr.get_participant(req.participant_id)
    if record is None:
        raise HTTPException(404, f"Participant {req.participant_id} not found")

    if req.mode == InterviewMode.CASE_STUDY:
        # Mode 1: Case Study
        session = s_mgr.create_case_session(
            participant_id=record.participant_id,
            participant_name=record.name,
            case_id=record.case_scenario_id,
        )
        # Generate opening
        opening_turns = await session.engine.generate_opening()

        return CreateSessionResponse(
            session_id=session.session_id,
            mode=InterviewMode.CASE_STUDY,
            opening_messages=[
                {"speaker": t.speaker_name, "content": t.content}
                for t in opening_turns
            ],
            problem_statement=session.engine.case_study.problem_statement,
            company_name=session.engine.case_study.company_name,
            case_data=[],  # Data revealed progressively
        )

    else:
        # Mode 2: Group Discussion
        session = s_mgr.create_group_session(
            participant_id=record.participant_id,
            participant_name=record.name,
            scenario_id=record.group_scenario_id,
        )
        # Generate opening
        opening_turns = await session.engine.generate_opening()

        return CreateSessionResponse(
            session_id=session.session_id,
            mode=InterviewMode.GROUP_DISCUSSION,
            opening_messages=[
                {"speaker": t.speaker_name, "content": t.content}
                for t in opening_turns
            ],
            scenario_brief=session.engine.scenario.brief,
            agents=["Alex", "Jordan", "Riley"],
        )


@app.get("/session/{sid}/status", response_model=SessionStatusResponse)
async def get_session_status(sid: str):
    """Get current session status and conversation history."""
    s_mgr = _get_session_mgr()
    session = s_mgr.get_session(sid)
    if session is None:
        raise HTTPException(404, f"Session {sid} not found")

    engine = session.engine
    conversation = [
        {
            "turn_number": t.turn_number,
            "speaker": t.speaker_name,
            "speaker_role": t.speaker_role.value,
            "content": t.content,
        }
        for t in engine.turns
    ]

    response = SessionStatusResponse(
        session_id=sid,
        mode=engine.mode,
        state=engine.state,
        conversation=conversation,
        elapsed_seconds=engine.elapsed_seconds,
        remaining_seconds=engine.remaining_seconds,
    )

    # Mode-specific info
    if engine.mode == InterviewMode.CASE_STUDY:
        response.revealed_data = engine.get_revealed_data()
    else:
        response.trait_coverage = engine.get_trait_coverage()

    return response


@app.post("/session/{sid}/message", response_model=SubmitMessageResponse)
async def submit_message(sid: str, req: SubmitMessageRequest):
    """Submit participant message and get AI response(s)."""
    s_mgr = _get_session_mgr()
    session = s_mgr.get_session(sid)
    if session is None:
        raise HTTPException(404, f"Session {sid} not found")

    engine = session.engine

    # Check session state
    if engine.state == SessionState.ENDED:
        raise HTTPException(400, "Session has ended")

    # Submit participant turn
    await engine.submit_candidate_turn(req.content)

    # Generate AI response(s)
    ai_turns = await engine.generate_ai_response()

    # Persist session
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


@app.post("/session/{sid}/end", response_model=EndSessionResponse)
async def end_session(sid: str):
    """End session and run evaluation."""
    p_mgr = _get_participant_mgr()
    s_mgr = _get_session_mgr()
    session = s_mgr.get_session(sid)

    if session is None:
        raise HTTPException(404, f"Session {sid} not found")

    engine = session.engine
    engine.end_session()

    # Get participant record
    record = p_mgr.get_participant(session.participant_id)
    if record is None:
        raise HTTPException(404, f"Participant {session.participant_id} not found")

    # Save session output
    session_output = engine.to_session_output()

    summary = {}
    if engine.mode == InterviewMode.CASE_STUDY:
        # Run Mode 1 evaluation
        from evaluation.logic_evaluator import LogicEvaluator
        evaluator = LogicEvaluator(_client)
        assessment = await evaluator.evaluate(engine.turns, record.name)

        record.case_completed = True
        record.case_session_id = sid
        record.case_assessment = assessment
        record.case_stats = engine.compute_session_stats()

        summary = {
            "overall_score": assessment.overall_score,
            "strengths": assessment.strengths,
            "development_areas": assessment.development_areas,
        }

        p_mgr.save_session_output(record.participant_id, "case", session_output.__dict__)

    else:
        # Run Mode 2 evaluation
        from evaluation.trait_evaluator import TraitEvaluator
        evaluator = TraitEvaluator(_client)
        stats = engine.compute_session_stats()
        assessment = await evaluator.evaluate_ensemble(engine.turns, record.name, stats)

        record.group_completed = True
        record.group_session_id = sid
        record.group_assessment = assessment
        record.group_stats = stats

        summary = {
            "personality_vector": assessment.to_vector().to_dict(),
            "strengths": assessment.strengths,
            "development_areas": assessment.development_areas,
        }

        p_mgr.save_session_output(record.participant_id, "group", session_output.__dict__)

    # Advance phase
    next_phase = p_mgr.advance_phase(record.participant_id)

    return EndSessionResponse(
        session_id=sid,
        mode=engine.mode,
        next_phase=next_phase,
        summary=summary,
    )


@app.post("/participant/{pid}/survey")
async def submit_survey(pid: str, req: SurveySubmitRequest):
    """Submit post-study survey."""
    mgr = _get_participant_mgr()
    record = mgr.get_participant(pid)
    if record is None:
        raise HTTPException(404, f"Participant {pid} not found")

    survey = PostSessionSurvey(
        case_naturalness=req.case_naturalness,
        case_challenge=req.case_challenge,
        case_fairness=req.case_fairness,
        group_naturalness=req.group_naturalness,
        group_authenticity=req.group_authenticity,
        group_engagement=req.group_engagement,
        overall_recommendation=req.overall_recommendation,
        preferred_mode=req.preferred_mode,
        open_feedback=req.open_feedback,
    )

    record.survey = survey
    record.completed_at = datetime.now()
    record.current_phase = StudyPhase.COMPLETE
    mgr.update_participant(record)

    return {"status": "ok", "phase": StudyPhase.COMPLETE.value}


# =============================================================================
# HR DASHBOARD ENDPOINTS
# =============================================================================

@app.get("/hr/candidates")
async def list_candidates():
    """List all completed candidates for HR dashboard."""
    mgr = _get_participant_mgr()
    completed = mgr.list_completed_participants()

    summaries = []
    for record in completed:
        summary = CandidateSummary(
            participant_id=record.participant_id,
            name=record.name,
            completed_at=record.completed_at,
        )

        if record.case_assessment:
            summary.logic_overall_score = record.case_assessment.overall_score
            summary.logic_strengths = record.case_assessment.strengths
            summary.logic_weaknesses = record.case_assessment.development_areas

        if record.group_assessment:
            summary.personality_vector = record.group_assessment.to_vector()
            summary.personality_strengths = record.group_assessment.strengths
            summary.personality_areas = record.group_assessment.development_areas

        summaries.append(summary)

    return {"candidates": [s.model_dump() for s in summaries]}


@app.get("/hr/candidate/{pid}")
async def get_candidate_report(pid: str):
    """Get full candidate report."""
    mgr = _get_participant_mgr()
    record = mgr.get_participant(pid)
    if record is None:
        raise HTTPException(404, f"Participant {pid} not found")

    report = CandidateReport(
        participant_id=record.participant_id,
        name=record.name,
        assessment_date=record.completed_at or record.created_at,
        bfi44_scores=record.bfi44_scores,
        logic_assessment=record.case_assessment,
        case_stats=record.case_stats,
        personality_assessment=record.group_assessment,
        group_stats=record.group_stats,
        survey=record.survey,
    )

    # Calculate personality accuracy if both ground truth and inference exist
    if record.bfi44_scores and record.group_assessment:
        gt = record.bfi44_scores
        inferred = record.group_assessment.to_vector()
        report.personality_accuracy = {
            "O": {"ground_truth": gt.O, "inferred": inferred.O, "diff": abs(gt.O - inferred.O)},
            "C": {"ground_truth": gt.C, "inferred": inferred.C, "diff": abs(gt.C - inferred.C)},
            "E": {"ground_truth": gt.E, "inferred": inferred.E, "diff": abs(gt.E - inferred.E)},
            "A": {"ground_truth": gt.A, "inferred": inferred.A, "diff": abs(gt.A - inferred.A)},
            "N": {"ground_truth": gt.N, "inferred": inferred.N, "diff": abs(gt.N - inferred.N)},
            "mean_abs_error": sum([
                abs(gt.O - inferred.O),
                abs(gt.C - inferred.C),
                abs(gt.E - inferred.E),
                abs(gt.A - inferred.A),
                abs(gt.N - inferred.N),
            ]) / 5,
        }

    return report.model_dump()


@app.get("/hr/compare")
async def compare_candidates(pids: str = ""):
    """Compare multiple candidates side-by-side."""
    mgr = _get_participant_mgr()

    # Parse comma-separated PIDs or get all
    if pids:
        pid_list = [p.strip() for p in pids.split(",")]
    else:
        pid_list = [r.participant_id for r in mgr.list_completed_participants()]

    summaries = []
    for pid in pid_list:
        record = mgr.get_participant(pid)
        if record and record.case_completed and record.group_completed:
            summary = CandidateSummary(
                participant_id=record.participant_id,
                name=record.name,
                completed_at=record.completed_at,
            )
            if record.case_assessment:
                summary.logic_overall_score = record.case_assessment.overall_score
            if record.group_assessment:
                summary.personality_vector = record.group_assessment.to_vector()
            summaries.append(summary)

    # Build rankings
    rankings = {}
    if summaries:
        # Logic ranking
        sorted_by_logic = sorted(
            [s for s in summaries if s.logic_overall_score],
            key=lambda x: x.logic_overall_score,
            reverse=True,
        )
        rankings["logic"] = [s.participant_id for s in sorted_by_logic]

        # Trait rankings
        for trait in ["O", "C", "E", "A", "N"]:
            sorted_by_trait = sorted(
                [s for s in summaries if s.personality_vector],
                key=lambda x: getattr(x.personality_vector, trait),
                reverse=True,
            )
            rankings[f"trait_{trait}"] = [s.participant_id for s in sorted_by_trait]

    comparison = CandidateComparison(
        candidates=summaries,
        dimension_rankings=rankings,
    )

    return comparison.model_dump()


# =============================================================================
# HEALTH CHECK
# =============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": "3.0.0",
        "modes": ["case_study", "group_discussion"],
    }
