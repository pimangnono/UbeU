"""FastAPI backend for the UbeU Simulation Engine web UI.

Provides REST endpoints for script generation, simulation execution,
and results retrieval, plus WebSocket streaming for live monitoring.
"""

from __future__ import annotations

import asyncio
import json
import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from simulation_engine.results_analysis import ensure_results_analysis

# Persistent result storage directory (survives server reloads)
_RESULTS_DIR = Path(__file__).parent / ".sim_results"
_RESULTS_DIR.mkdir(exist_ok=True)

app = FastAPI(title="UbeU Simulation Engine", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── In-memory stores ──────────────────────────────────────────────────────────

# simulation_id → {"status", "script", "result", "events", "task"}
_simulations: dict[str, dict[str, Any]] = {}


def _save_result(simulation_id: str, result: dict[str, Any]):
    """Persist result to disk so it survives server reloads."""
    path = _RESULTS_DIR / f"{simulation_id}.json"
    path.write_text(json.dumps(result, default=str), encoding="utf-8")


def _load_result(simulation_id: str) -> dict[str, Any] | None:
    """Load a previously saved result from disk."""
    path = _RESULTS_DIR / f"{simulation_id}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None

# Lazily initialized LLM client + graph runner
_gen_client = None
_graph_runner = None


def _get_client():
    global _gen_client
    if _gen_client is None:
        from clients.llm_client import LLMClient
        _gen_client = LLMClient()
    return _gen_client


def _get_runner():
    global _graph_runner
    if _graph_runner is None:
        from simulation_engine.graph_runner import StakeholderSimulationGraphRunner
        _graph_runner = StakeholderSimulationGraphRunner(
            _get_client(),
            style_slots=["integrator", "planner", "challenger", "skeptic"],
        )
    return _graph_runner


# ── Request / Response Models ─────────────────────────────────────────────────

class BriefRequest(BaseModel):
    brief: str
    actor_count: int | None = None
    simulation_mode: str | None = None  # "guided" or "exploratory"


class SimulateRequest(BaseModel):
    script: dict[str, Any]
    condition: str = "engine_controller"


class ScriptPatch(BaseModel):
    stakeholders: list[dict[str, Any]] | None = None
    phases: list[dict[str, Any]] | None = None
    simulation_mode: str | None = None


class ScenarioCard(BaseModel):
    id: str
    title: str
    brief: str
    actor_count: int
    tags: list[str] = Field(default_factory=list)
    category: str = ""          # e.g. "guided-policy", "exploratory-business"
    simulation_mode: str = ""   # "guided" or "exploratory"


# ── Demo: Pre-built Scenarios from Benchmark Briefs ──────────────────────────
# NOTE: Demo only — remove for production release

_BRIEF_TITLES: dict[str, str] = {
    "california_ab5_gig_classification": "California AB5 Gig Worker Law",
    "eu_gdpr_implementation": "EU GDPR Implementation",
    "japan_intern_training_reform": "Japan Intern Training Reform",
    "nyc_congestion_pricing": "NYC Congestion Pricing",
    "singapore_hdb_waittime_crisis": "Singapore HDB Wait Time Crisis",
    "boeing_737max_return": "Boeing 737 MAX Return to Service",
    "netflix_password_crackdown": "Netflix Password Crackdown",
    "starbucks_unionization": "Starbucks Unionization Wave",
    "microsoft_activision_merger": "Microsoft-Activision Merger",
    "zoom_return_to_office": "Zoom Return to Office Mandate",
    "flint_water_crisis": "Flint Water Crisis",
    "australia_robodebt": "Australia Robodebt Scheme",
    "uk_post_office_horizon": "UK Post Office Horizon Scandal",
    "sf_homelessness_policy": "SF Homelessness Policy",
    "fukushima_nuclear_restart": "Fukushima Nuclear Restart Debate",
    "wework_ipo_collapse": "WeWork IPO Collapse",
    "ftx_collapse": "FTX Crypto Exchange Collapse",
    "svb_bank_run": "Silicon Valley Bank Run",
    "peloton_demand_cliff": "Peloton Post-Pandemic Cliff",
    "theranos_whistleblower": "Theranos Whistleblower Aftermath",
}

_BRIEF_TAGS: dict[str, list[str]] = {
    "california_ab5_gig_classification": ["labor", "gig economy"],
    "eu_gdpr_implementation": ["privacy", "technology"],
    "japan_intern_training_reform": ["labor", "immigration"],
    "nyc_congestion_pricing": ["urban", "transportation"],
    "singapore_hdb_waittime_crisis": ["housing", "urban"],
    "boeing_737max_return": ["aviation", "safety"],
    "netflix_password_crackdown": ["streaming", "business"],
    "starbucks_unionization": ["labor", "corporate"],
    "microsoft_activision_merger": ["gaming", "antitrust"],
    "zoom_return_to_office": ["remote work", "corporate"],
    "flint_water_crisis": ["public health", "government"],
    "australia_robodebt": ["welfare", "automation"],
    "uk_post_office_horizon": ["IT failure", "justice"],
    "sf_homelessness_policy": ["homelessness", "urban"],
    "fukushima_nuclear_restart": ["energy", "safety"],
    "wework_ipo_collapse": ["startup", "finance"],
    "ftx_collapse": ["crypto", "fraud"],
    "svb_bank_run": ["banking", "crisis"],
    "peloton_demand_cliff": ["consumer", "post-pandemic"],
    "theranos_whistleblower": ["healthcare", "fraud"],
}


_BRIEF_CATEGORIES: dict[str, str] = {
    # Labor & Employment
    "california_ab5_gig_classification": "Labor & Employment",
    "japan_intern_training_reform": "Labor & Employment",
    "starbucks_unionization": "Labor & Employment",
    "zoom_return_to_office": "Labor & Employment",
    # Urban Policy
    "nyc_congestion_pricing": "Urban Policy",
    "singapore_hdb_waittime_crisis": "Urban Policy",
    "sf_homelessness_policy": "Urban Policy",
    "flint_water_crisis": "Urban Policy",
    # Corporate Crisis
    "boeing_737max_return": "Corporate Crisis",
    "netflix_password_crackdown": "Corporate Crisis",
    "microsoft_activision_merger": "Corporate Crisis",
    "peloton_demand_cliff": "Corporate Crisis",
    # Finance & Fraud
    "wework_ipo_collapse": "Finance & Fraud",
    "ftx_collapse": "Finance & Fraud",
    "svb_bank_run": "Finance & Fraud",
    "theranos_whistleblower": "Finance & Fraud",
    # Tech & Governance
    "eu_gdpr_implementation": "Tech & Governance",
    "australia_robodebt": "Tech & Governance",
    "uk_post_office_horizon": "Tech & Governance",
    "fukushima_nuclear_restart": "Tech & Governance",
}


def _build_demo_scenarios() -> list[dict[str, Any]]:
    """Build 20 scenario cards from benchmark briefs. Demo only."""
    from simulation_engine.final_benchmark_briefs import FINAL_BENCHMARK_BRIEFS

    scenarios = []
    for b in FINAL_BENCHMARK_BRIEFS:
        scenarios.append({
            "id": b.brief_id,
            "title": _BRIEF_TITLES.get(b.brief_id, b.brief_id.replace("_", " ").title()),
            "brief": b.brief_text,
            "actor_count": 4,
            "tags": _BRIEF_TAGS.get(b.brief_id, []),
            "category": _BRIEF_CATEGORIES.get(b.brief_id, "Other"),
            "simulation_mode": b.simulation_mode,
        })
    return scenarios


PRE_BUILT_SCENARIOS: list[dict[str, Any]] = _build_demo_scenarios()


# ── REST Endpoints ────────────────────────────────────────────────────────────

@app.get("/api/scenarios")
async def list_scenarios() -> list[dict[str, Any]]:
    """Pre-built scenario cards for quick-start."""
    return PRE_BUILT_SCENARIOS


@app.post("/api/generate-script")
async def generate_script(req: BriefRequest) -> dict[str, Any]:
    """Generate a SimulationScript from a brief description."""
    from simulation_engine.run_exp3_userinput import generate_script_from_brief

    try:
        client = _get_client()
        brief_id = f"web_{uuid.uuid4().hex[:8]}"
        script = await generate_script_from_brief(
            client,
            req.brief,
            brief_id,
            actor_count=req.actor_count,
            simulation_mode=req.simulation_mode,
        )
        return script.to_dict()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/api/simulate")
async def start_simulation(req: SimulateRequest) -> dict[str, str]:
    """Start an async simulation. Returns simulation_id for WebSocket."""
    from simulation_engine.script import SimulationScript

    script = SimulationScript.from_dict(req.script)
    simulation_id = script.simulation_id or f"sim_{uuid.uuid4().hex[:8]}"

    _simulations[simulation_id] = {
        "status": "pending",
        "script": req.script,
        "result": None,
        "events": [],
        "ws_clients": [],
        "task": None,
    }

    # Launch simulation in background
    task = asyncio.create_task(_run_simulation(simulation_id, script, req.condition))
    _simulations[simulation_id]["task"] = task

    return {"simulation_id": simulation_id}


@app.get("/api/results/{simulation_id}")
async def get_results(simulation_id: str) -> dict[str, Any]:
    """Complete results for a finished simulation."""
    sim = _simulations.get(simulation_id)
    if sim is not None:
        if sim["status"] != "complete":
            return {"status": sim["status"], "events_so_far": len(sim["events"])}
        sim["result"] = ensure_results_analysis(sim["result"])
        return sim["result"]

    # Fall back to disk (survives server reloads)
    disk_result = _load_result(simulation_id)
    if disk_result:
        disk_result = ensure_results_analysis(disk_result)
        return disk_result

    return {"error": "Simulation not found"}


@app.patch("/api/script/{simulation_id}")
async def update_script(simulation_id: str, patch: ScriptPatch) -> dict[str, Any]:
    """Update actors/params on a pending simulation's script."""
    sim = _simulations.get(simulation_id)
    if sim is None:
        return {"error": "Simulation not found"}
    if sim["status"] != "pending":
        return {"error": "Simulation already started"}

    script_data = sim["script"]
    if patch.stakeholders is not None:
        script_data["stakeholders"] = patch.stakeholders
    if patch.phases is not None:
        script_data["phases"] = patch.phases
    if patch.simulation_mode is not None:
        script_data["simulation_mode"] = patch.simulation_mode

    return {"status": "updated"}


@app.get("/api/simulation/{simulation_id}/status")
async def simulation_status(simulation_id: str) -> dict[str, Any]:
    """Check simulation status and event count."""
    sim = _simulations.get(simulation_id)
    if sim is None:
        return {"error": "Simulation not found"}
    return {
        "status": sim["status"],
        "events_count": len(sim["events"]),
    }


# ── WebSocket ─────────────────────────────────────────────────────────────────

@app.websocket("/ws/simulation/{simulation_id}")
async def simulation_ws(websocket: WebSocket, simulation_id: str):
    """Stream simulation events in real-time."""
    await websocket.accept()

    sim = _simulations.get(simulation_id)
    if sim is None:
        await websocket.send_json({"type": "error", "data": {"message": "Simulation not found"}})
        await websocket.close()
        return

    # Register this client
    sim["ws_clients"].append(websocket)

    try:
        # Send all existing events first (catch-up)
        for event in sim["events"]:
            await websocket.send_json(event)

        # Keep connection alive, wait for new events or completion
        while sim["status"] not in ("complete", "error"):
            try:
                # Use ping/pong to keep alive, also allows client messages
                data = await asyncio.wait_for(websocket.receive_text(), timeout=30.0)
            except asyncio.TimeoutError:
                # Send keepalive
                await websocket.send_json({"type": "ping", "data": {}})
            except WebSocketDisconnect:
                break

        # Send final completion event if not already sent
        if sim["status"] == "complete" and sim["result"]:
            await websocket.send_json({
                "type": "complete",
                "data": {"simulation_id": simulation_id},
            })

    except WebSocketDisconnect:
        pass
    finally:
        if websocket in sim.get("ws_clients", []):
            sim["ws_clients"].remove(websocket)


# ── Simulation Runner ─────────────────────────────────────────────────────────

async def _broadcast_event(simulation_id: str, event: dict[str, Any]):
    """Broadcast an event to all connected WebSocket clients."""
    sim = _simulations.get(simulation_id)
    if sim is None:
        return
    sim["events"].append(event)
    dead_clients = []
    for ws in sim.get("ws_clients", []):
        try:
            await ws.send_json(event)
        except Exception:
            dead_clients.append(ws)
    for ws in dead_clients:
        sim["ws_clients"].remove(ws)


async def _run_simulation(simulation_id: str, script, condition: str):
    """Run the simulation and stream events via WebSocket in real-time."""
    from simulation_engine.key_moments import extract_key_moments
    from simulation_engine.conclusion import generate_conclusion

    sim = _simulations[simulation_id]
    sim["status"] = "running"

    await _broadcast_event(simulation_id, {
        "type": "status",
        "data": {"status": "running", "simulation_id": simulation_id},
    })

    # Send actor metadata up front so UI can render all actors immediately
    actors_meta = []
    for actor_spec in script.stakeholders:
        actors_meta.append({
            "actor_id": actor_spec.actor_id,
            "display_name": actor_spec.display_name,
            "role": actor_spec.role,
            "disposition": getattr(actor_spec, "strategic_disposition", "neutral"),
        })
    await _broadcast_event(simulation_id, {
        "type": "actors_init",
        "data": {"actors": actors_meta},
    })

    try:
        runner = _get_runner()

        # Real-time callback: stream turns + relationship events as they happen
        async def on_event(event_data: dict, phase: str):
            event_type = event_data.pop("_type", "unknown")
            if event_type == "phase_change":
                await _broadcast_event(simulation_id, {
                    "type": "phase_change",
                    "data": {"from": event_data["from"], "to": event_data["to"]},
                })
            elif event_type == "turn":
                await _broadcast_event(simulation_id, {
                    "type": "turn",
                    "data": event_data,
                })
            elif event_type == "relationship":
                await _broadcast_event(simulation_id, {
                    "type": "relationship",
                    "data": event_data,
                })

        result = await runner.run_streaming(script, condition, on_event=on_event)

        runtime_summary = result.get("runtime_summary", {})
        metrics = result.get("metrics")

        # Relationship events already streamed inline; send actions post-hoc
        for action in runtime_summary.get("executed_actions", []):
            await _broadcast_event(simulation_id, {
                "type": "action",
                "data": {
                    "actor_id": action.get("owner_actor_id", ""),
                    "action_type": action.get("action_type", ""),
                    "target_key": action.get("target_key", ""),
                    "deltas": action.get("applied_delta", {}),
                    "phase": action.get("phase_name", ""),
                },
            })

        # Compute metrics and extract key moments
        metrics_dict = metrics.to_dict() if hasattr(metrics, "to_dict") else dict(metrics) if metrics else {}
        key_moments = extract_key_moments(runtime_summary)

        # Generate structured conclusion
        script_dict = script.to_dict() if hasattr(script, "to_dict") else script
        try:
            conclusion = await generate_conclusion(
                _get_client(), runtime_summary, key_moments, script_dict,
            )
        except Exception as exc:
            import traceback
            traceback.print_exc()
            conclusion = None

        # Final metric update
        await _broadcast_event(simulation_id, {
            "type": "metric_update",
            "data": {
                "persona_drift_mae": metrics_dict.get("persona_drift_mae", 0),
                "commitment_contradiction_rate": metrics_dict.get("commitment_contradiction_rate", 0),
                "relationship_inconsistency": metrics_dict.get("relationship_inconsistency", 0),
                "envelope_violations": metrics_dict.get("envelope_violations", 0),
            },
        })

        # Store full result
        full_result = {
            "simulation_id": simulation_id,
            "runtime_summary": runtime_summary,
            "metrics": metrics_dict,
            "key_moments": key_moments,
            "conclusion": conclusion,
            "script": script_dict,
        }
        full_result = ensure_results_analysis(full_result)
        sim["result"] = full_result
        sim["status"] = "complete"
        _save_result(simulation_id, full_result)

        await _broadcast_event(simulation_id, {
            "type": "complete",
            "data": {"simulation_id": simulation_id},
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        sim["status"] = "error"
        await _broadcast_event(simulation_id, {
            "type": "error",
            "data": {"message": str(e)},
        })


# ── Health Check ──────────────────────────────────────────────────────────────

@app.get("/api/health")
async def health():
    return {"status": "ok", "simulations_count": len(_simulations)}
