import { Button } from '../ui/Button';

interface ResultsTabsProps {
  activeTab: 'outcome' | 'actor';
  onChange: (tab: 'outcome' | 'actor') => void;
}

export function ResultsTabs({ activeTab, onChange }: ResultsTabsProps) {
  return (
    <div className="flex items-center gap-2">
      <Button
        variant={activeTab === 'outcome' ? 'primary' : 'secondary'}
        size="sm"
        onClick={() => onChange('outcome')}
      >
        Outcome Analysis
      </Button>
      <Button
        variant={activeTab === 'actor' ? 'primary' : 'secondary'}
        size="sm"
        onClick={() => onChange('actor')}
      >
        Actor Analysis
      </Button>
    </div>
  );
}
