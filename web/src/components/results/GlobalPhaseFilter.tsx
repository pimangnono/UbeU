import { Filter } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';
import { PhaseScrubber } from './PhaseScrubber';

interface GlobalPhaseFilterProps {
  phases: string[];
  selectedPhase: string | null;
  onSelectPhase: (phase: string | null) => void;
}

export function GlobalPhaseFilter({
  phases,
  selectedPhase,
  onSelectPhase,
}: GlobalPhaseFilterProps) {
  return (
    <GlassCard className="p-4">
      <div className="flex items-start gap-3 flex-wrap">
        <div className="flex items-center gap-2 text-sm font-semibold text-text-primary">
          <Filter size={16} className="text-accent-blue" />
          Global Phase Filter
        </div>
        <div className="flex-1 min-w-[260px]">
          <PhaseScrubber phases={phases} selectedPhase={selectedPhase} onSelectPhase={onSelectPhase} />
        </div>
      </div>
    </GlassCard>
  );
}
