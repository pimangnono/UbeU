import { useState, type ReactNode } from 'react';

interface TooltipProps {
  content: string;
  children?: ReactNode;
}

export function Tooltip({ content, children }: TooltipProps) {
  const [show, setShow] = useState(false);

  return (
    <span
      className="relative inline-flex items-center"
      onMouseEnter={() => setShow(true)}
      onMouseLeave={() => setShow(false)}
    >
      {children ?? (
        <span className="inline-flex items-center justify-center w-[18px] h-[18px] rounded-full bg-gray-200 text-gray-500 text-[10px] font-bold cursor-help ml-1 shrink-0 hover:bg-gray-300 hover:text-gray-700 transition-colors">
          ?
        </span>
      )}
      {show && (
        <span className="absolute z-[100] bottom-full left-0 mb-2.5 px-4 py-3 text-sm text-gray-700 bg-white border border-gray-200 rounded-xl shadow-lg w-72 whitespace-normal leading-relaxed pointer-events-none">
          {content}
          <span className="absolute top-full left-4 border-[6px] border-transparent border-t-white" />
        </span>
      )}
    </span>
  );
}

interface InfoLabelProps {
  label: string;
  tooltip: string;
  className?: string;
}

export function InfoLabel({ label, tooltip, className = '' }: InfoLabelProps) {
  return (
    <span className={`inline-flex items-center gap-0.5 ${className}`}>
      {label}
      <Tooltip content={tooltip} />
    </span>
  );
}
