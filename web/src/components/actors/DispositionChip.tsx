import { HeartHandshake, Scale, Swords, ShieldAlert } from 'lucide-react';
import { DISPOSITION_CONFIG, type Disposition } from '../../types/simulation';

interface DispositionChipProps {
  value: Disposition;
  onChange?: (value: Disposition) => void;
  readonly?: boolean;
}

const dispositions: Disposition[] = ['cooperative', 'neutral', 'competitive', 'adversarial'];

const DISPOSITION_ICONS: Record<Disposition, React.ReactNode> = {
  cooperative: <HeartHandshake size={12} />,
  neutral: <Scale size={12} />,
  competitive: <Swords size={12} />,
  adversarial: <ShieldAlert size={12} />,
};

export function DispositionChip({ value, onChange, readonly = false }: DispositionChipProps) {
  if (readonly) {
    const cfg = DISPOSITION_CONFIG[value];
    return (
      <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium ${cfg.bg} ${cfg.color}`}>
        {DISPOSITION_ICONS[value]} {value}
      </span>
    );
  }

  return (
    <div className="flex gap-1.5 flex-wrap">
      {dispositions.map((d) => {
        const cfg = DISPOSITION_CONFIG[d];
        const selected = d === value;
        return (
          <button
            key={d}
            onClick={() => onChange?.(d)}
            className={`flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium transition-all cursor-pointer ${
              selected ? `${cfg.bg} ${cfg.color} ring-1 ring-current` : 'bg-gray-100 text-gray-400 hover:text-gray-600'
            }`}
          >
            {DISPOSITION_ICONS[d]} {d}
          </button>
        );
      })}
    </div>
  );
}
