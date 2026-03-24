interface PhaseDividerProps {
  phaseName: string;
}

export function PhaseDivider({ phaseName }: PhaseDividerProps) {
  return (
    <div className="flex items-center gap-3 py-2 px-3">
      <div className="flex-1 h-px bg-border-subtle" />
      <span className="text-xs font-semibold text-text-muted tracking-wider uppercase">
        {phaseName} Phase
      </span>
      <div className="flex-1 h-px bg-border-subtle" />
    </div>
  );
}
