import { ACTOR_COLORS } from '../../types/simulation';

interface ChatBubbleProps {
  actorId: string;
  displayName: string;
  content: string;
  turnIndex: number;
  colorIndex: number;
  highlighted?: boolean;
  dimmed?: boolean;
  onClick?: () => void;
}

export function ChatBubble({
  displayName,
  content,
  turnIndex,
  colorIndex,
  highlighted = false,
  dimmed = false,
  onClick,
}: ChatBubbleProps) {
  const color = ACTOR_COLORS[colorIndex % ACTOR_COLORS.length];

  return (
    <div
      id={`turn-${turnIndex}`}
      className={`flex gap-3 px-4 py-3 rounded-xl transition-all cursor-pointer ${
        highlighted ? 'bg-blue-50 ring-1 ring-blue-200' : 'hover:bg-gray-50'
      } ${dimmed ? 'opacity-35' : ''}`}
      onClick={onClick}
    >
      <div
        className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold text-white shrink-0 mt-0.5"
        style={{ backgroundColor: color }}
      >
        {displayName[0]}
      </div>
      <div className="min-w-0 flex-1">
        <div className="flex items-baseline gap-2 mb-1">
          <span className="text-sm font-semibold" style={{ color }}>{displayName}</span>
          <span className="text-xs text-text-muted font-mono">#{turnIndex}</span>
        </div>
        <div className="text-[15px] text-text-secondary leading-relaxed whitespace-pre-wrap">{content}</div>
      </div>
    </div>
  );
}
