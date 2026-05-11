import { ACTOR_COLORS, type OceanTraits } from '../../types/simulation';

interface DumbbellChartProps {
  actorPriors: Record<string, OceanTraits>;
  actorEstimates: Record<string, OceanTraits>;
  actorNames: Record<string, string>;
  actorIds: string[];
}

export function DumbbellChart({ actorPriors, actorEstimates, actorNames, actorIds }: DumbbellChartProps) {
  const traits = ['O', 'C', 'E', 'A', 'N'] as const;

  return (
    <div className="space-y-4">
      {actorIds.map((actorId, actorIdx) => {
        const priors = actorPriors[actorId];
        const estimates = actorEstimates[actorId];
        if (!priors) return null;
        const color = ACTOR_COLORS[actorIdx % ACTOR_COLORS.length];

        return (
          <div key={actorId}>
            <div className="text-sm font-medium mb-2" style={{ color }}>
              {actorNames[actorId] || actorId}
            </div>
            <div className="space-y-1.5">
              {traits.map((t) => {
                const target = priors[t] ?? 0.5;
                const actual = estimates?.[t] ?? target;
                const left = Math.min(target, actual);
                const right = Math.max(target, actual);
                const error = Math.abs(target - actual);

                return (
                  <div key={t} className="flex items-center gap-2 text-xs">
                    <span className="w-4 text-text-muted font-mono">{t}</span>
                    <div className="flex-1 h-3 bg-bg-elevated rounded-full relative">
                      {/* Range bar */}
                      <div
                        className="absolute top-1/2 -translate-y-1/2 h-1 rounded-full"
                        style={{
                          left: `${left * 100}%`,
                          width: `${(right - left) * 100}%`,
                          backgroundColor: error > 0.15 ? '#ef4444' : error > 0.1 ? '#f59e0b' : '#10b981',
                          opacity: 0.5,
                        }}
                      />
                      {/* Target dot */}
                      <div
                        className="absolute top-1/2 -translate-y-1/2 w-2.5 h-2.5 rounded-full border-2 border-bg-primary"
                        style={{ left: `${target * 100}%`, transform: 'translate(-50%, -50%)', backgroundColor: '#a1a1aa' }}
                        title={`Target: ${target.toFixed(2)}`}
                      />
                      {/* Actual dot */}
                      {estimates && (
                        <div
                          className="absolute top-1/2 -translate-y-1/2 w-2.5 h-2.5 rounded-full border-2 border-bg-primary"
                          style={{ left: `${actual * 100}%`, transform: 'translate(-50%, -50%)', backgroundColor: color }}
                          title={`Actual: ${actual.toFixed(2)}`}
                        />
                      )}
                    </div>
                    <span className="w-16 text-right text-text-muted font-mono">
                      {target.toFixed(2)} → {actual.toFixed(2)}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}
