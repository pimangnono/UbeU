import { CheckCircle, AlertTriangle, XCircle, Lightbulb, Sparkles } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import type { SimulationConclusion } from '../../types/simulation';

interface ConclusionPanelProps {
  conclusion: SimulationConclusion;
  actorNames: Record<string, string>;
}

const OUTCOME_CONFIG = {
  achieved: {
    icon: CheckCircle,
    label: 'Achieved',
    color: 'text-accent-green',
    bg: 'bg-emerald-500/15',
    border: 'border-emerald-500/30',
  },
  partial: {
    icon: AlertTriangle,
    label: 'Partial',
    color: 'text-accent-amber',
    bg: 'bg-amber-500/15',
    border: 'border-amber-500/30',
  },
  not_achieved: {
    icon: XCircle,
    label: 'Not Achieved',
    color: 'text-accent-red',
    bg: 'bg-red-500/15',
    border: 'border-red-500/30',
  },
} as const;

export function ConclusionPanel({ conclusion, actorNames }: ConclusionPanelProps) {
  if (conclusion.mode === 'guided') {
    return <GuidedConclusion conclusion={conclusion} actorNames={actorNames} />;
  }
  return <ExploratoryConclusion conclusion={conclusion} actorNames={actorNames} />;
}

function GuidedConclusion({ conclusion }: ConclusionPanelProps) {
  const outcome = conclusion.outcome_achieved || 'partial';
  const config = OUTCOME_CONFIG[outcome];
  const Icon = config.icon;

  return (
    <GlassCard className="p-5">
      <div className="flex items-start gap-4">
        <div className={`flex-shrink-0 p-2 rounded-lg ${config.bg} ${config.border} border`}>
          <Icon size={24} className={config.color} />
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 mb-2">
            <h3 className="text-sm font-semibold text-text-primary">Outcome</h3>
            <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${config.bg} ${config.color}`}>
              {config.label}
            </span>
          </div>
          <p className="text-sm text-text-secondary leading-relaxed">
            {conclusion.outcome_summary}
          </p>

          {conclusion.contributing_factors && conclusion.contributing_factors.length > 0 && (
            <div className="mt-4">
              <h4 className="text-xs font-medium text-text-muted mb-2 uppercase tracking-wider">Contributing Factors</h4>
              <ul className="space-y-1.5">
                {conclusion.contributing_factors.map((factor, i) => (
                  <li key={i} className="text-sm text-text-secondary flex items-start gap-2">
                    <span className="text-accent-blue mt-1 flex-shrink-0">&#8227;</span>
                    {factor}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </GlassCard>
  );
}

function ExploratoryConclusion({ conclusion }: ConclusionPanelProps) {
  return (
    <GlassCard className="p-5">
      <div className="flex items-start gap-4">
        <div className="flex-shrink-0 p-2 rounded-lg bg-violet-500/15 border border-violet-500/30">
          <Lightbulb size={24} className="text-violet-400" />
        </div>
        <div className="flex-1 min-w-0">
          <h3 className="text-sm font-semibold text-text-primary mb-2">What Emerged</h3>
          <p className="text-sm text-text-secondary leading-relaxed">
            {conclusion.outcome_summary}
          </p>

          {conclusion.key_discoveries && conclusion.key_discoveries.length > 0 && (
            <div className="mt-4">
              <h4 className="text-xs font-medium text-text-muted mb-2 uppercase tracking-wider">Key Discoveries</h4>
              <ul className="space-y-1.5">
                {conclusion.key_discoveries.map((discovery, i) => (
                  <li key={i} className="text-sm text-text-secondary flex items-start gap-2">
                    <Sparkles size={14} className="text-violet-400 mt-0.5 flex-shrink-0" />
                    {discovery}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {conclusion.emergent_patterns && conclusion.emergent_patterns.length > 0 && (
            <div className="mt-4">
              <h4 className="text-xs font-medium text-text-muted mb-2 uppercase tracking-wider">Emergent Patterns</h4>
              <ul className="space-y-1.5">
                {conclusion.emergent_patterns.map((pattern, i) => (
                  <li key={i} className="text-sm text-text-secondary flex items-start gap-2">
                    <span className="text-violet-400 mt-1 flex-shrink-0">&#8227;</span>
                    {pattern}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </GlassCard>
  );
}
