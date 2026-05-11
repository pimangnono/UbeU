import { Button } from '../ui/Button';

interface PhaseScrubberProps {
  phases: string[];
  selectedPhase: string | null;
  onSelectPhase: (phase: string | null) => void;
}

export function PhaseScrubber({ phases, selectedPhase, onSelectPhase }: PhaseScrubberProps) {
  if (phases.length === 0) return null;

  return (
    <div className="flex items-center gap-2 flex-wrap">
      <Button
        variant={selectedPhase === null ? 'primary' : 'secondary'}
        size="sm"
        onClick={() => onSelectPhase(null)}
      >
        All phases
      </Button>
      {phases.map((phase) => (
        <Button
          key={phase}
          variant={selectedPhase === phase ? 'primary' : 'secondary'}
          size="sm"
          onClick={() => onSelectPhase(phase)}
        >
          {phase}
        </Button>
      ))}
    </div>
  );
}
