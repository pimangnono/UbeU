from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import redis
import json
import asyncio

app = FastAPI()

# Allow CORS for Next.js (Port 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis Connection (Hot Path)
# Note: host is 'localhost' because we run this script outside Docker for now
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.get("/")
def health_check():
    return {"status": "UbeU Backend is running"}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    print(f"Client {client_id} connected.")

    try:
        while True:
            # 1. Receive JSON from Frontend
            data = await websocket.receive_text()
            message_data = json.loads(data)

            # 2. Store in Redis (The "Memory")
            # We push to a list so we have history
            redis_key = f"chat:{client_id}"
            redis_client.rpush(redis_key, json.dumps(message_data))

            # 3. Echo Logic (Simulating the 'Orchestrator' for now)
            # In the future, this is where the LLM / Orchestrator logic goes.
            response = {
                "sender": "System",
                "text": f"Echo: You said '{message_data['text']}'. (Saved to Redis)",
                "timestamp": "now"
            }

            # 4. Send back to Frontend
            await websocket.send_text(json.dumps(response))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
