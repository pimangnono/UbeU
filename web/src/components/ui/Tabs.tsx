import { useState } from 'react';

interface Tab {
  id: string;
  label: string;
}

interface TabsProps {
  tabs: Tab[];
  defaultTab?: string;
  onChange?: (tabId: string) => void;
  children: (activeTab: string) => React.ReactNode;
}

export function Tabs({ tabs, defaultTab, onChange, children }: TabsProps) {
  const [active, setActive] = useState(defaultTab || tabs[0]?.id || '');

  const handleClick = (id: string) => {
    setActive(id);
    onChange?.(id);
  };

  return (
    <div>
      <div className="flex gap-1 border-b border-border-subtle mb-4">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => handleClick(tab.id)}
            className={`px-4 py-2 text-sm font-medium transition-colors border-b-2 cursor-pointer ${
              active === tab.id
                ? 'border-accent-blue text-text-primary'
                : 'border-transparent text-text-muted hover:text-text-secondary'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>
      {children(active)}
    </div>
  );
}
