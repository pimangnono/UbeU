import { GlassCard } from '../ui/GlassCard';
import { ACTOR_COLORS } from '../../types/simulation';
import type { ActorArc } from '../../types/simulation';

interface ActorArcsPanelProps {
  arcs: ActorArc[];
  actorIds: string[];
}

export function ActorArcsPanel({ arcs, actorIds }: ActorArcsPanelProps) {
  if (!arcs || arcs.length === 0) return null;

  return (
    <GlassCard className="p-5">
      <h3 className="text-sm font-semibold text-text-secondary mb-4">Actor Arcs</h3>
      <div className="space-y-3">
        {arcs.map((arc, i) => {
          const colorIndex = actorIds.indexOf(arc.actor_id);
          const color = ACTOR_COLORS[colorIndex >= 0 ? colorIndex % ACTOR_COLORS.length : 0];

          return (
            <div key={i} className="flex items-start gap-3">
              <div
                className="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold text-white mt-0.5"
                style={{ backgroundColor: color }}
              >
                {(arc.role || arc.actor_id).charAt(0).toUpperCase()}
              </div>
              <div className="flex-1 min-w-0">
                <div className="text-xs font-medium text-text-muted mb-0.5">{arc.role}</div>
                <p className="text-sm text-text-secondary leading-relaxed">{arc.arc}</p>
              </div>
            </div>
          );
        })}
      </div>
    </GlassCard>
  );
}
