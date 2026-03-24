import { Zap, ArrowRight } from 'lucide-react';
import { ACTOR_COLORS } from '../../types/simulation';

interface ActionEventProps {
  actorId: string;
  displayName: string;
  actionType: string;
  targetKey: string;
  deltas: Record<string, number>;
  colorIndex: number;
}

export function ActionEvent({ displayName, actionType, targetKey, deltas, colorIndex }: ActionEventProps) {
  const color = ACTOR_COLORS[colorIndex % ACTOR_COLORS.length];

  return (
    <div className="flex items-start gap-3 px-3 py-1.5 text-xs">
      <div className="w-7 flex justify-center shrink-0 mt-0.5">
        <Zap size={14} className="text-accent-amber" />
      </div>
      <div className="text-text-muted">
        <span style={{ color }} className="font-medium">[{displayName}]</span>{' '}
        <span className="text-text-secondary">{actionType.replace(/_/g, ' ')}</span>
        {targetKey && (
          <span className="text-text-muted inline-flex items-center gap-0.5">
            {' '}<ArrowRight size={10} /> {targetKey}
          </span>
        )}
        {Object.keys(deltas).length > 0 && (
          <div className="mt-0.5 font-mono text-text-muted">
            {Object.entries(deltas).map(([k, v]) => (
              <span key={k} className={`mr-2 ${v > 0 ? 'text-accent-green' : 'text-accent-red'}`}>
                {k}: {v > 0 ? '+' : ''}{v.toFixed(2)}
              </span>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
