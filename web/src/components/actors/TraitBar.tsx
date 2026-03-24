import { TRAIT_LABELS } from '../../types/simulation';

interface TraitBarProps {
  trait: string;
  value: number;
  onChange?: (value: number) => void;
  readonly?: boolean;
  target?: number;
  compact?: boolean;
}

export function TraitBar({ trait, value, onChange, readonly = false, target, compact = false }: TraitBarProps) {
  return (
    <div className={`flex items-center gap-2 ${compact ? 'text-xs' : 'text-sm'}`}>
      <span className="w-4 text-gray-500 font-mono font-semibold">{trait}</span>
      <div className="flex-1 relative">
        {readonly ? (
          <div className="h-1.5 bg-gray-200 rounded-full relative">
            <div
              className="absolute top-0 left-0 h-full bg-blue-500 rounded-full"
              style={{ width: `${value * 100}%` }}
            />
            {target !== undefined && (
              <div
                className="absolute top-1/2 -translate-y-1/2 w-2.5 h-2.5 rounded-full bg-gray-400 border-2 border-white"
                style={{ left: `${target * 100}%` }}
                title={`Target: ${target.toFixed(2)}`}
              />
            )}
          </div>
        ) : (
          <input
            type="range"
            min={0}
            max={1}
            step={0.05}
            value={value}
            onChange={(e) => onChange?.(parseFloat(e.target.value))}
            className="w-full"
          />
        )}
      </div>
      <span className="w-8 text-right text-gray-500 font-mono">{value.toFixed(1)}</span>
    </div>
  );
}

interface TraitBarsProps {
  traits: Record<string, number>;
  onChange?: (trait: string, value: number) => void;
  readonly?: boolean;
  targets?: Record<string, number>;
  compact?: boolean;
}

export function TraitBars({ traits, onChange, readonly = false, targets, compact = false }: TraitBarsProps) {
  return (
    <div className={`flex flex-col ${compact ? 'gap-1' : 'gap-2'}`}>
      {['O', 'C', 'E', 'A', 'N'].map((t) => (
        <TraitBar
          key={t}
          trait={t}
          value={traits[t] ?? 0.5}
          onChange={onChange ? (v) => onChange(t, v) : undefined}
          readonly={readonly}
          target={targets?.[t]}
          compact={compact}
        />
      ))}
    </div>
  );
}
