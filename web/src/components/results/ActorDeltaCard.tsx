import { ArrowRight, UserRound } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { ACTOR_COLORS, type ActorFinalStateSummary, type StakeholderActor } from '../../types/simulation';

interface ActorDeltaCardProps {
  actor: StakeholderActor;
  actorIndex: number;
  summary?: ActorFinalStateSummary;
  selected?: boolean;
  onSelect?: () => void;
}

export function ActorDeltaCard({ actor, actorIndex, summary, selected = false, onSelect }: ActorDeltaCardProps) {
  const color = ACTOR_COLORS[actorIndex % ACTOR_COLORS.length];
  const traits = ['O', 'C', 'E', 'A', 'N'] as const;

  return (
    <GlassCard
      hover
      className={`p-4 cursor-pointer ${selected ? 'ring-2 ring-accent-blue/40 bg-blue-50/40' : ''}`}
      onClick={onSelect}
    >
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full text-white flex items-center justify-center" style={{ backgroundColor: color }}>
              <UserRound size={16} />
            </div>
            <div>
              <div className="text-sm font-semibold text-text-primary">{actor.role}</div>
              <div className="text-xs text-text-muted">{actor.display_name}</div>
            </div>
          </div>

          <div className="mt-3 grid grid-cols-2 gap-3 text-xs">
            <div>
              <div className="uppercase tracking-wider text-text-muted mb-1">Initial stance</div>
              <div className="text-text-secondary">{summary?.initial_stance_summary || actor.strategic_disposition}</div>
            </div>
            <div>
              <div className="uppercase tracking-wider text-text-muted mb-1">End state</div>
              <div className="text-text-secondary">{summary?.end_state_summary || 'No summary available'}</div>
            </div>
          </div>

          <div className="mt-3 space-y-1.5">
            {traits.map((trait) => {
              const initial = actor.personality_prior[trait] ?? 0.5;
              const final = summary?.final_trait_estimate?.[trait] ?? initial;
              return (
                <div key={trait} className="flex items-center gap-2 text-[11px]">
                  <span className="w-4 font-mono text-text-muted">{trait}</span>
                  <div className="flex-1 h-2 rounded-full bg-bg-elevated relative overflow-hidden">
                    <div className="absolute inset-y-0 left-0 bg-zinc-300/70" style={{ width: `${initial * 100}%` }} />
                    <div className="absolute inset-y-0 bg-blue-400/70" style={{ width: `${final * 100}%` }} />
                  </div>
                  <span className="w-16 text-right text-text-muted font-mono">
                    {initial.toFixed(2)} <ArrowRight size={10} className="inline" /> {final.toFixed(2)}
                  </span>
                </div>
              );
            })}
          </div>

          <div className="mt-3 space-y-1 text-xs text-text-secondary">
            {summary?.strongest_trait_shift && Math.abs(summary.strongest_trait_shift.delta) > 0.01 && (
              <div>
                Strongest trait shift: {summary.strongest_trait_shift.trait} {summary.strongest_trait_shift.initial.toFixed(2)} → {summary.strongest_trait_shift.final.toFixed(2)}
                {' '}({summary.strongest_trait_shift.delta >= 0 ? '+' : ''}{summary.strongest_trait_shift.delta.toFixed(2)}).
              </div>
            )}
            {summary?.top_relationship_shift && (
              Math.abs(summary.top_relationship_shift.trust_delta) > 0.01 || Math.abs(summary.top_relationship_shift.tension_delta) > 0.01
            ) ? (
              <div>
                Strongest relationship shift: toward {summary?.top_relationship_shift?.target_label},
                {' '}trust {summary?.top_relationship_shift?.trust_delta >= 0 ? '+' : ''}{summary?.top_relationship_shift?.trust_delta.toFixed(2)},
                {' '}tension {summary?.top_relationship_shift?.tension_delta >= 0 ? '+' : ''}{summary?.top_relationship_shift?.tension_delta.toFixed(2)}.
              </div>
            ) : (
              <div>No meaningful relationship shift was recorded for this actor.</div>
            )}
          </div>
        </div>
      </div>
    </GlassCard>
  );
}
