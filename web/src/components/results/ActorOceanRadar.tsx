import { GlassCard } from '../ui/GlassCard';
import { TRAIT_LABELS, type ActorAnalysisItem, type OceanTraits } from '../../types/simulation';

interface ActorOceanRadarProps {
  actor: ActorAnalysisItem;
}

const TRAITS: Array<keyof OceanTraits> = ['O', 'C', 'E', 'A', 'N'];

function polygonPoints(values: OceanTraits, radius: number, center: number) {
  return TRAITS.map((trait, index) => {
    const angle = (-Math.PI / 2) + (index * Math.PI * 2) / TRAITS.length;
    const value = values[trait] ?? 0.5;
    const x = center + Math.cos(angle) * radius * value;
    const y = center + Math.sin(angle) * radius * value;
    return `${x},${y}`;
  }).join(' ');
}

function gridPoints(scale: number, radius: number, center: number) {
  const values = TRAITS.reduce((acc, trait) => ({ ...acc, [trait]: scale }), {} as OceanTraits);
  return polygonPoints(values, radius, center);
}

export function ActorOceanRadar({ actor }: ActorOceanRadarProps) {
  const size = 260;
  const center = size / 2;
  const radius = 86;
  const largestShift = actor.largest_trait_shift;

  return (
    <GlassCard className="p-5">
      <div className="flex items-start justify-between gap-4 flex-wrap">
        <div>
          <h3 className="text-sm font-semibold text-text-primary">OCEAN Before vs After</h3>
          <p className="text-xs text-text-muted mt-1">
            Grey is the configured prior. Blue is the final estimated behavior profile.
          </p>
        </div>
        <div className="flex items-center gap-3 text-xs text-text-muted">
          <span className="inline-flex items-center gap-1"><span className="w-3 h-3 rounded-full bg-zinc-300 inline-block" /> Initial</span>
          <span className="inline-flex items-center gap-1"><span className="w-3 h-3 rounded-full bg-blue-400 inline-block" /> Final</span>
        </div>
      </div>

      <div className="mt-4 flex items-center justify-center">
        <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} className="overflow-visible">
          {[0.25, 0.5, 0.75, 1].map((scale) => (
            <polygon
              key={scale}
              points={gridPoints(scale, radius, center)}
              fill="none"
              stroke="rgba(100,116,139,0.18)"
              strokeWidth="1"
            />
          ))}
          {TRAITS.map((trait, index) => {
            const angle = (-Math.PI / 2) + (index * Math.PI * 2) / TRAITS.length;
            const x = center + Math.cos(angle) * radius;
            const y = center + Math.sin(angle) * radius;
            const labelX = center + Math.cos(angle) * (radius + 26);
            const labelY = center + Math.sin(angle) * (radius + 26);
            return (
              <g key={trait}>
                <line x1={center} y1={center} x2={x} y2={y} stroke="rgba(100,116,139,0.18)" strokeWidth="1" />
                <text x={labelX} y={labelY} textAnchor="middle" className="fill-slate-500 text-[11px] font-medium">
                  {trait}
                </text>
              </g>
            );
          })}
          <polygon
            points={polygonPoints(actor.initial_traits, radius, center)}
            fill="rgba(148,163,184,0.18)"
            stroke="rgba(148,163,184,0.9)"
            strokeWidth="2"
          />
          <polygon
            points={polygonPoints(actor.final_traits, radius, center)}
            fill="rgba(59,130,246,0.22)"
            stroke="rgba(59,130,246,0.95)"
            strokeWidth="2.5"
          />
        </svg>
      </div>

      <div className="rounded-xl border border-border-subtle bg-bg-elevated/60 p-4 mt-4">
        <div className="text-xs uppercase tracking-wider text-text-muted">Largest Observed Trait Movement</div>
        <div className="text-sm text-text-primary mt-2">
          {largestShift
            ? `${TRAIT_LABELS[largestShift.trait]} moved from ${largestShift.initial.toFixed(2)} to ${largestShift.final.toFixed(2)} (${largestShift.delta >= 0 ? '+' : ''}${largestShift.delta.toFixed(2)}).`
            : 'No trait movement summary was generated.'}
        </div>
        <div className="text-sm text-text-secondary mt-2">
          {largestShift
            ? `Behaviorally, this means the actor finished the run sounding more ${largestShift.delta >= 0 ? '' : 'less '}${TRAIT_LABELS[largestShift.trait].toLowerCase()} than originally configured.`
            : 'The final behavior stayed close to the original persona profile.'}
        </div>
      </div>
    </GlassCard>
  );
}
