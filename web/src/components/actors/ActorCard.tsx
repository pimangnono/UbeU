import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronUp, ChevronDown } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { InfoLabel } from '../ui/Tooltip';
import { TraitBars } from './TraitBar';
import { DispositionChip } from './DispositionChip';
import type { StakeholderActor, Disposition } from '../../types/simulation';

interface ActorCardProps {
  actor: StakeholderActor;
  color: string;
  index: number;
  onUpdate?: (actor: StakeholderActor) => void;
  readonly?: boolean;
}

export function ActorCard({ actor, color, index, onUpdate, readonly = false }: ActorCardProps) {
  const [expanded, setExpanded] = useState(false);

  const updateTrait = (trait: string, value: number) => {
    if (!onUpdate) return;
    onUpdate({
      ...actor,
      personality_prior: { ...actor.personality_prior, [trait]: value },
    });
  };

  const updateDisposition = (d: Disposition) => {
    if (!onUpdate) return;
    onUpdate({ ...actor, strategic_disposition: d });
  };

  return (
    <GlassCard
      hover
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.08 }}
      className="relative overflow-hidden"
    >
      {/* Color accent bar */}
      <div className="absolute top-0 left-0 w-1 h-full rounded-l-xl" style={{ backgroundColor: color }} />

      <div className="pl-3">
        {/* Header */}
        <div className="flex items-center gap-3 mb-3">
          <div
            className="w-10 h-10 rounded-full flex items-center justify-center text-base font-bold text-white shrink-0"
            style={{ backgroundColor: color }}
          >
            {actor.role[0]}
          </div>
          <div className="min-w-0">
            <div className="font-semibold text-base text-text-primary truncate">{actor.role}</div>
            <div className="text-sm text-text-muted truncate">{actor.display_name}</div>
          </div>
        </div>

        {/* Trait bars + disposition */}
        <div className="space-y-3">
          <div>
            <InfoLabel label="OCEAN Traits" tooltip="Big Five personality traits. Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism. Each ranges from 0.0 (low) to 1.0 (high). Drag the sliders to adjust." className="text-xs font-semibold text-text-muted mb-1.5" />
            <TraitBars
              traits={actor.personality_prior}
              onChange={readonly ? undefined : updateTrait}
              readonly={readonly}
              compact
            />
          </div>
          <div>
            <InfoLabel label="Disposition" tooltip="How this actor approaches negotiation. Cooperative: seeks win-win. Neutral: flexible. Competitive: seeks advantage. Adversarial: actively opposes others." className="text-xs font-semibold text-text-muted mb-1.5" />
            <DispositionChip
              value={actor.strategic_disposition}
              onChange={readonly ? undefined : updateDisposition}
              readonly={readonly}
            />
          </div>
        </div>

        {/* Expand drawer */}
        <button
          onClick={() => setExpanded(!expanded)}
          className="mt-3 text-sm text-accent-blue hover:text-blue-400 transition-colors w-full text-left cursor-pointer font-medium"
        >
          <span className="inline-flex items-center gap-1">
            {expanded ? <><ChevronUp size={14} /> Collapse Details</> : <><ChevronDown size={14} /> Expand Details</>}
          </span>
        </button>

        <AnimatePresence>
          {expanded && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="overflow-hidden"
            >
              <div className="pt-3 space-y-3 text-sm">
                {actor.incentives.length > 0 && (
                  <div>
                    <InfoLabel label="Incentives" tooltip="What this actor wants to achieve. These motivations drive their behavior in the simulation." className="text-xs font-semibold text-text-muted mb-1" />
                    <ul className="list-disc list-inside text-text-secondary space-y-0.5">
                      {actor.incentives.map((inc, i) => <li key={i}>{inc}</li>)}
                    </ul>
                  </div>
                )}
                {actor.concerns.length > 0 && (
                  <div>
                    <InfoLabel label="Concerns" tooltip="What this actor is worried about or wants to avoid. These create tension and conflict in the simulation." className="text-xs font-semibold text-text-muted mb-1" />
                    <ul className="list-disc list-inside text-text-secondary space-y-0.5">
                      {actor.concerns.map((c, i) => <li key={i}>{c}</li>)}
                    </ul>
                  </div>
                )}
                {actor.experience_summary && (
                  <div>
                    <InfoLabel label="Experience" tooltip="Background and expertise that shapes this actor's perspective and credibility." className="text-xs font-semibold text-text-muted mb-1" />
                    <div className="text-text-secondary">{actor.experience_summary}</div>
                  </div>
                )}
                {actor.communication_style && Object.keys(actor.communication_style).length > 0 && (
                  <div>
                    <InfoLabel label="Communication Style" tooltip="How this actor expresses themselves: tone (e.g., diplomatic, blunt), brevity (verbose vs. concise), and other speech patterns." className="text-xs font-semibold text-text-muted mb-1" />
                    <div className="text-text-secondary">
                      {Object.entries(actor.communication_style).map(([k, v]) => `${k}: ${v}`).join(', ')}
                    </div>
                  </div>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </GlassCard>
  );
}
