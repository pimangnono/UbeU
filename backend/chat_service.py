# chat_service.py
"""
Chat Service - The "Hot Path" for real-time conversation handling.
Manages short-term memory using Redis Lists for immediate LLM context.
"""

import redis
import json
import os
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Redis DB 0: Chat History (Hot Storage)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

# OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Constants
CHAT_PREFIX = "chat:"
MAX_HISTORY_LENGTH = 20  # Keep last 20 messages (10 turns)
MIN_WORDS_FOR_EXTRACTION = 10  # Only extract from substantial responses


def get_redis_key(session_id: str) -> str:
    """Generate Redis key for chat history."""
    return f"{CHAT_PREFIX}{session_id}"


def get_chat_history(session_id: str, limit: int = MAX_HISTORY_LENGTH) -> list[dict]:
    """
    Retrieve chat history from Redis.
    Returns messages in chronological order (oldest first).
    """
    key = get_redis_key(session_id)
    # LRANGE returns newest first (since we LPUSH), so reverse
    messages = redis_client.lrange(key, 0, limit - 1)
    parsed = [json.loads(msg) for msg in messages]
    return list(reversed(parsed))  # Chronological order


def save_message(session_id: str, role: str, content: str) -> None:
    """
    Save a message to Redis chat history.
    Automatically trims to keep only recent messages.
    """
    key = get_redis_key(session_id)
    message = json.dumps({"role": role, "content": content})
    
    # LPUSH adds to the front (newest first)
    redis_client.lpush(key, message)
    
    # Keep only the last MAX_HISTORY_LENGTH messages
    redis_client.ltrim(key, 0, MAX_HISTORY_LENGTH - 1)
    
    # Set expiry (24 hours)
    redis_client.expire(key, 60 * 60 * 24)


def should_extract_to_graph(text: str) -> bool:
    """
    Determine if text is substantial enough for graph extraction.
    Skip short acknowledgments like "Okay", "Yes", etc.
    """
    word_count = len(text.split())
    return word_count >= MIN_WORDS_FOR_EXTRACTION


def handle_user_message(
    session_id: str, 
    user_message: str,
    system_prompt: Optional[str] = None
) -> str:
    """
    Handle an incoming user message - the main hot path.
    
    1. Save user message to Redis
    2. Trigger async extraction if message is substantial
    3. Generate LLM response using recent context
    4. Save assistant response to Redis
    5. Return response
    """
    # Import here to avoid circular imports
    from backend.worker import process_interview_segment
    
    # --- 1. Save User Message to Redis ---
    save_message(session_id, "user", user_message)
    
    # --- 2. Handoff to Cold Path (if substantial) ---
    if should_extract_to_graph(user_message):
        # .delay() offloads this to Celery background worker
        process_interview_segment.delay(session_id, user_message)
    
    # --- 3. Generate Reply using LLM ---
    history = get_chat_history(session_id)
    
    # Build messages for OpenAI
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.extend(history)
    
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    
    bot_response = completion.choices[0].message.content or "I'm sorry, I couldn't generate a response."
    
    # --- 4. Save Bot Response to Redis ---
    save_message(session_id, "assistant", bot_response)
    
    return bot_response


def get_session_info(session_id: str) -> dict:
    """Get information about a chat session."""
    key = get_redis_key(session_id)
    message_count = redis_client.llen(key)
    ttl = redis_client.ttl(key)
    
    return {
        "session_id": session_id,
        "message_count": message_count,
        "ttl_seconds": ttl if ttl > 0 else None,
        "exists": message_count > 0
    }


def clear_session(session_id: str) -> bool:
    """Clear a chat session from Redis."""
    key = get_redis_key(session_id)
    return redis_client.delete(key) > 0
