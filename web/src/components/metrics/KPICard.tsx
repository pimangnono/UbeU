import { Check, TrendingUp } from 'lucide-react';
import { GlassCard } from '../ui/GlassCard';

interface KPICardProps {
  label: string;
  value: number;
  format?: 'decimal' | 'percent' | 'count';
  good?: 'low' | 'high';
  threshold?: number;
}

export function KPICard({ label, value, format = 'decimal', good = 'low', threshold }: KPICardProps) {
  const formatted =
    format === 'percent' ? `${(value * 100).toFixed(1)}%` :
    format === 'count' ? value.toFixed(1) :
    value.toFixed(3);

  const isGood = threshold !== undefined
    ? (good === 'low' ? value <= threshold : value >= threshold)
    : (good === 'low' ? value < 0.2 : value > 0.5);

  return (
    <GlassCard className="p-3 text-center">
      <div className="text-xs text-text-muted mb-1">{label}</div>
      <div className={`text-xl font-bold font-mono ${isGood ? 'text-accent-green' : 'text-accent-red'}`}>
        {formatted}
      </div>
      <div className="mt-1 flex justify-center">
        {isGood
          ? <Check size={14} className="text-accent-green" />
          : <TrendingUp size={14} className="text-accent-red" />
        }
      </div>
    </GlassCard>
  );
}
