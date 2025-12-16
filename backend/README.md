# Interview Memory Backend

Python backend service for the interview assessment memory system.

## Architecture

- **Redis (DB 0)**: Short-term memory - stores last 20 chat messages
- **Redis (DB 1)**: Celery message broker  
- **Neo4j**: Long-term memory - structured skill/trait knowledge graph
- **Celery**: Async background processing for graph extraction

## Setup

1. **Install dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   ```bash
   cp env.example .env
   # Edit .env with your credentials
   ```

3. **Start services**:
   ```bash
   # Terminal 1: Flask API
   python -m backend.api
   
   # Terminal 2: Celery Worker
   celery -A backend.celery_config worker --loglevel=info
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat` | Send message, get response |
| GET | `/api/session/{id}/history` | Get chat history |
| DELETE | `/api/session/{id}` | Clear session |
| GET | `/api/report/{id}` | Get assessment report |
| GET | `/api/report/{id}/skills` | Get skills with evidence |
| GET | `/api/report/{id}/traits` | Get OCEAN traits |

## File Structure

```
backend/
├── api.py              # Flask REST API
├── chat_service.py     # Redis hot path
├── worker.py           # Celery background tasks
├── report_service.py   # Neo4j report queries
├── schema_config.py    # CCS & OCEAN ontology
├── celery_config.py    # Celery settings
└── requirements.txt    # Dependencies
```
