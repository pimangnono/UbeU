# api.py
"""
Flask REST API - Interface for Next.js frontend communication.
Provides endpoints for chat handling and report generation.
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for Next.js frontend

# Import services
from backend.chat_service import (
    handle_user_message,
    get_chat_history,
    get_session_info,
    clear_session
)
from backend.report_service import (
    get_candidate_report,
    get_skills_with_evidence,
    get_traits_with_evidence,
    get_domain_deep_dive
)


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "interview-memory-backend"})


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Handle a chat message from the user.
    
    Request body:
    {
        "session_id": "uuid",
        "message": "user message text",
        "system_prompt": "optional system prompt"
    }
    
    Response:
    {
        "response": "bot response text",
        "session_id": "uuid"
    }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body required"}), 400
    
    session_id = data.get("session_id")
    message = data.get("message")
    system_prompt = data.get("system_prompt")
    
    if not session_id or not message:
        return jsonify({"error": "session_id and message are required"}), 400
    
    try:
        response = handle_user_message(session_id, message, system_prompt)
        return jsonify({
            "response": response,
            "session_id": session_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/session/<session_id>/history", methods=["GET"])
def get_history(session_id: str):
    """
    Get chat history for a session.
    
    Query params:
    - limit: Max messages to return (default: 20)
    """
    limit = request.args.get("limit", 20, type=int)
    
    try:
        history = get_chat_history(session_id, limit)
        info = get_session_info(session_id)
        
        return jsonify({
            "session_id": session_id,
            "messages": history,
            "info": info
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/session/<session_id>", methods=["DELETE"])
def delete_session(session_id: str):
    """Clear a chat session."""
    try:
        cleared = clear_session(session_id)
        return jsonify({
            "session_id": session_id,
            "cleared": cleared
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/report/<session_id>", methods=["GET"])
def get_report(session_id: str):
    """
    Get the complete assessment report for a candidate.
    
    Returns skills grouped by domain and OCEAN trait analysis.
    """
    try:
        report = get_candidate_report(session_id)
        return jsonify(report)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/report/<session_id>/skills", methods=["GET"])
def get_skills(session_id: str):
    """Get skills with evidence for a session."""
    try:
        skills = get_skills_with_evidence(session_id)
        return jsonify({
            "session_id": session_id,
            "skills": skills
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/report/<session_id>/traits", methods=["GET"])
def get_traits(session_id: str):
    """Get personality traits with evidence for a session."""
    try:
        traits = get_traits_with_evidence(session_id)
        return jsonify({
            "session_id": session_id,
            "traits": traits
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/report/<session_id>/domain/<domain>", methods=["GET"])
def get_domain(session_id: str, domain: str):
    """Get detailed analysis for a specific CCS domain."""
    try:
        analysis = get_domain_deep_dive(session_id, domain)
        return jsonify(analysis)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("API_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
