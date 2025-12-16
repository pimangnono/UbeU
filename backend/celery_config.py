# celery_config.py
"""
Celery configuration for background task processing.
Uses Redis DB 1 as the message broker.
"""

from celery import Celery

# Redis DB 0: Chat History (Hot Storage)
# Redis DB 1: Celery Broker (Task Queue)
REDIS_BROKER_URL = "redis://localhost:6379/1"
REDIS_RESULT_BACKEND = "redis://localhost:6379/1"

# Create Celery app
celery_app = Celery(
    "interview_worker",
    broker=REDIS_BROKER_URL,
    backend=REDIS_RESULT_BACKEND,
    include=["backend.worker"]
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30,  # 30 second timeout per task
    worker_prefetch_multiplier=1,  # Process one task at a time
    task_acks_late=True,  # Acknowledge after task completion
)
