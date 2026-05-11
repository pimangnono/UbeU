# UbeU Simulation Engine

UbeU is a multi-stakeholder simulation demo for exploring how AI-generated actors debate, negotiate, and shift their positions over time.

The current product surface in this repository is the web demo:
- `Setup`: choose a scenario, generate stakeholders, review the simulation, and launch it
- `Live Monitoring`: watch turns, relationship shifts, and actions stream in real time
- `Results`: inspect outcome analysis, actor analysis, relationship change, and transcript evidence

## Requirements

- Python 3.10+
- Node.js 18+
- An `OPENROUTER_API_KEY` environment variable for script generation and simulation runs

## Backend Setup

Install Python dependencies from the repo root:

```bash
pip install -r requirements.txt
```

Set your API key:

```bash
export OPENROUTER_API_KEY=your_key_here
```

Start the backend on port `8000`:

```bash
python3 -m uvicorn simulation_engine.api:app --host 0.0.0.0 --port 8000
```

## Frontend Setup

In a second terminal, install the web dependencies:

```bash
cd web
npm install
```

Start the Vite dev server on port `5173`:

```bash
npm run dev -- --host 127.0.0.1 --port 5173
```

Open:

```text
http://127.0.0.1:5173
```

## Demo Flow

To run the Singapore HDB demo in the web UI:

1. Open `http://127.0.0.1:5173/setup`
2. Choose one scenario or write on your own
3. Set the actor count you want
4. Choose either:
   - `Guided`: you provide a desired outcome
   - `Exploratory`: the discussion evolves without a fixed target outcome
5. Click `Generate Stakeholders`
6. Review the generated actors and relationships
7. Click `Review & Launch`
8. Click `Launch Simulation`
9. Watch the run in `Live Monitoring`
10. Open `View Result` when the run completes

## Notes

- The frontend talks to the backend through Vite proxies:
  - `/api` -> `http://localhost:8000`
  - `/ws` -> `ws://localhost:8000`
- If the UI says the WebSocket failed, first confirm the backend is still listening on port `8000`.
- Results are persisted under `simulation_engine/.sim_results/` so they survive backend restarts.

## Useful Commands

Run backend tests:

```bash
PYTHONPATH=. pytest -q
```

Run the frontend production build:

```bash
cd web
npm run build
```
