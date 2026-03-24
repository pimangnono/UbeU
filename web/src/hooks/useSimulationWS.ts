import { useEffect, useRef, useCallback, useState } from 'react';
import type {
  SimEvent,
  TurnEvent,
  ActionEvent,
  RelationshipEvent,
  MetricUpdate,
  ActorMeta,
} from '../types/simulation';

interface SimulationWSState {
  connected: boolean;
  currentPhase: string;
  actors: ActorMeta[];
  turns: TurnEvent[];
  actions: ActionEvent[];
  relationships: RelationshipEvent[];
  metrics: MetricUpdate | null;
  isComplete: boolean;
  error: string | null;
}

export function useSimulationWS(simulationId: string | undefined) {
  const wsRef = useRef<WebSocket | null>(null);
  const retryRef = useRef(0);
  const [state, setState] = useState<SimulationWSState>({
    connected: false,
    currentPhase: '',
    actors: [],
    turns: [],
    actions: [],
    relationships: [],
    metrics: null,
    isComplete: false,
    error: null,
  });

  const handleEvent = useCallback((event: SimEvent) => {
    setState((prev) => {
      switch (event.type) {
        case 'actors_init':
          return { ...prev, actors: event.data.actors };
        case 'turn':
          return { ...prev, turns: [...prev.turns, event.data] };
        case 'action':
          return { ...prev, actions: [...prev.actions, event.data] };
        case 'relationship':
          return { ...prev, relationships: [...prev.relationships, event.data] };
        case 'phase_change':
          return { ...prev, currentPhase: event.data.to };
        case 'metric_update':
          return { ...prev, metrics: event.data };
        case 'complete':
          return { ...prev, isComplete: true };
        case 'error':
          return { ...prev, error: event.data.message };
        case 'ping':
        case 'status':
          return prev;
        default:
          return prev;
      }
    });
  }, []);

  useEffect(() => {
    if (!simulationId) return;

    const connect = () => {
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsUrl = `${protocol}//${window.location.host}/ws/simulation/${simulationId}`;

      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = () => {
        retryRef.current = 0;
        setState((prev) => ({ ...prev, connected: true, error: null }));
      };

      ws.onmessage = (msg) => {
        try {
          const event: SimEvent = JSON.parse(msg.data);
          handleEvent(event);
        } catch {
          // ignore malformed messages
        }
      };

      ws.onclose = (evt) => {
        setState((prev) => ({ ...prev, connected: false }));
        wsRef.current = null;

        // Retry up to 5 times with exponential backoff
        if (retryRef.current < 5 && !evt.wasClean) {
          const delay = Math.min(1000 * 2 ** retryRef.current, 10000);
          retryRef.current++;
          setTimeout(connect, delay);
        }
      };

      ws.onerror = () => {
        if (retryRef.current >= 3) {
          setState((prev) => ({
            ...prev,
            error: 'WebSocket connection failed — is the backend running on port 8000?',
          }));
        }
      };
    };

    connect();

    return () => {
      retryRef.current = 999;
      wsRef.current?.close();
      wsRef.current = null;
    };
  }, [simulationId, handleEvent]);

  return state;
}
