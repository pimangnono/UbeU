import { useQuery, useMutation } from '@tanstack/react-query';
import type { ScenarioCard, SimulationScript, SimulationResults } from '../types/simulation';

const API_BASE = '/api';

async function fetchJson<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${url}`, {
    headers: { 'Content-Type': 'application/json' },
    ...init,
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

export function useScenarios() {
  return useQuery<ScenarioCard[]>({
    queryKey: ['scenarios'],
    queryFn: () => fetchJson('/scenarios'),
  });
}

export function useGenerateScript() {
  return useMutation({
    mutationFn: (params: { brief: string; actor_count?: number; simulation_mode?: string; _signal?: AbortSignal }) => {
      const { _signal, ...body } = params;
      return fetchJson<SimulationScript>('/generate-script', {
        method: 'POST',
        body: JSON.stringify(body),
        signal: _signal,
      });
    },
  });
}

export function useStartSimulation() {
  return useMutation({
    mutationFn: (params: { script: Record<string, unknown>; condition?: string }) =>
      fetchJson<{ simulation_id: string }>('/simulate', {
        method: 'POST',
        body: JSON.stringify(params),
      }),
  });
}

export function useResults(simulationId: string | undefined) {
  return useQuery<SimulationResults>({
    queryKey: ['results', simulationId],
    queryFn: () => fetchJson(`/results/${simulationId}`),
    enabled: !!simulationId,
    refetchInterval: (query) => {
      const data = query.state.data;
      if (data && 'status' in data && (data as Record<string, unknown>).status !== 'complete') {
        return 2000;
      }
      return false;
    },
  });
}
