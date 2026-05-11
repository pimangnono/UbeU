import { Button } from '../ui/Button';

interface ActorEvidenceFilterProps {
  selected: 'relationship' | 'actor_drift' | 'action';
  onSelect: (value: 'relationship' | 'actor_drift' | 'action') => void;
}

export function ActorEvidenceFilter({ selected, onSelect }: ActorEvidenceFilterProps) {
  return (
    <div className="flex items-center gap-2 flex-wrap">
      <Button
        variant={selected === 'relationship' ? 'primary' : 'secondary'}
        size="sm"
        onClick={() => onSelect('relationship')}
      >
        Relationship
      </Button>
      <Button
        variant={selected === 'actor_drift' ? 'primary' : 'secondary'}
        size="sm"
        onClick={() => onSelect('actor_drift')}
      >
        Persona Drift
      </Button>
      <Button
        variant={selected === 'action' ? 'primary' : 'secondary'}
        size="sm"
        onClick={() => onSelect('action')}
      >
        Action
      </Button>
    </div>
  );
}
