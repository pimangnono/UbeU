import { InfoLabel } from '../ui/Tooltip';
import { TraitBars } from './TraitBar';
import { DispositionChip } from './DispositionChip';
import type { StakeholderActor, Disposition } from '../../types/simulation';

interface ActorDetailPanelProps {
  actor: StakeholderActor;
  color: string;
  onUpdate: (actor: StakeholderActor) => void;
  onClose: () => void;
}

function EditableList({
  items,
  onChange,
  placeholder,
}: {
  items: string[];
  onChange: (items: string[]) => void;
  placeholder: string;
}) {
  const updateItem = (index: number, value: string) => {
    const next = [...items];
    next[index] = value;
    onChange(next);
  };

  const removeItem = (index: number) => {
    onChange(items.filter((_, i) => i !== index));
  };

  const addItem = () => {
    onChange([...items, '']);
  };

  return (
    <div className="space-y-1.5">
      {items.map((item, i) => (
        <div key={i} className="flex gap-1.5">
          <input
            type="text"
            value={item}
            onChange={(e) => updateItem(i, e.target.value)}
            className="flex-1 bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500/30"
            placeholder={placeholder}
          />
          <button
            onClick={() => removeItem(i)}
            className="text-gray-400 hover:text-red-500 px-1.5 text-sm cursor-pointer"
          >
            ×
          </button>
        </div>
      ))}
      <button
        onClick={addItem}
        className="text-xs text-blue-500 hover:text-blue-600 cursor-pointer font-medium"
      >
        + Add
      </button>
    </div>
  );
}

export function ActorDetailPanel({ actor, color, onUpdate, onClose }: ActorDetailPanelProps) {
  const updateTrait = (trait: string, value: number) => {
    onUpdate({ ...actor, personality_prior: { ...actor.personality_prior, [trait]: value } });
  };

  const updateDisposition = (d: Disposition) => {
    onUpdate({ ...actor, strategic_disposition: d });
  };

  const updateCommStyle = (key: string, value: string) => {
    onUpdate({
      ...actor,
      communication_style: { ...actor.communication_style, [key]: value },
    });
  };

  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow-sm">
      <div className="p-6">
        {/* Header */}
        <div className="flex items-center justify-between mb-5">
          <div className="flex items-center gap-3">
            <div
              className="w-12 h-12 rounded-full flex items-center justify-center text-lg font-bold text-white"
              style={{ backgroundColor: color }}
            >
              {actor.role[0]}
            </div>
            <div>
              <div className="font-semibold text-lg text-gray-900">{actor.role}</div>
              <div className="text-sm text-gray-500">{actor.display_name}</div>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 text-xl cursor-pointer p-1"
          >
            ×
          </button>
        </div>

        {/* Two-column layout */}
        <div className="grid grid-cols-2 gap-6">
          {/* Left column */}
          <div className="space-y-5">
            {/* OCEAN Traits */}
            <div>
              <InfoLabel
                label="OCEAN Personality Traits"
                tooltip="Big Five personality model. O=Openness (creativity, curiosity), C=Conscientiousness (discipline, reliability), E=Extraversion (energy, sociability), A=Agreeableness (cooperation, empathy), N=Neuroticism (anxiety, emotional reactivity). The engine uses these to generate consistent behavior."
                className="text-sm font-semibold text-gray-600 mb-2"
              />
              <TraitBars traits={actor.personality_prior} onChange={updateTrait} />
            </div>

            {/* Disposition */}
            <div>
              <InfoLabel
                label="Strategic Disposition"
                tooltip="The actor's default negotiation posture. Cooperative: seeks mutual benefit and compromise. Neutral: adapts to the situation. Competitive: pursues own interests, may trade. Adversarial: actively blocks opposing interests."
                className="text-sm font-semibold text-gray-600 mb-2"
              />
              <DispositionChip value={actor.strategic_disposition} onChange={updateDisposition} />
            </div>

            {/* Communication Style */}
            <div>
              <InfoLabel
                label="Communication Style"
                tooltip="How this actor speaks. 'Tone' affects formality and warmth (e.g., diplomatic, blunt, cautious). 'Brevity' controls how verbose they are (concise, moderate, verbose). These influence the generated dialogue style."
                className="text-sm font-semibold text-gray-600 mb-2"
              />
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="text-xs text-gray-500 block mb-0.5">Tone</label>
                  <select
                    value={actor.communication_style?.tone || 'neutral'}
                    onChange={(e) => updateCommStyle('tone', e.target.value)}
                    className="w-full bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm text-gray-800"
                  >
                    {['diplomatic', 'neutral', 'assertive', 'cautious', 'blunt', 'empathetic', 'formal'].map((t) => (
                      <option key={t} value={t}>{t.charAt(0).toUpperCase() + t.slice(1)}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="text-xs text-gray-500 block mb-0.5">Brevity</label>
                  <select
                    value={actor.communication_style?.brevity || 'moderate'}
                    onChange={(e) => updateCommStyle('brevity', e.target.value)}
                    className="w-full bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm text-gray-800"
                  >
                    {['concise', 'moderate', 'verbose'].map((b) => (
                      <option key={b} value={b}>{b.charAt(0).toUpperCase() + b.slice(1)}</option>
                    ))}
                  </select>
                </div>
              </div>
            </div>
          </div>

          {/* Right column */}
          <div className="space-y-5">
            {/* Incentives */}
            <div>
              <InfoLabel
                label="Incentives"
                tooltip="What this actor wants to achieve. These motivations drive their proposals and alliances during the simulation. Be specific — e.g., 'Reduce costs by 20%' is better than 'Save money'."
                className="text-sm font-semibold text-gray-600 mb-2"
              />
              <EditableList
                items={actor.incentives}
                onChange={(items) => onUpdate({ ...actor, incentives: items })}
                placeholder="e.g., Increase market share"
              />
            </div>

            {/* Concerns */}
            <div>
              <InfoLabel
                label="Concerns"
                tooltip="What this actor worries about or wants to prevent. Concerns create natural tension between actors — they'll push back when these are threatened."
                className="text-sm font-semibold text-gray-600 mb-2"
              />
              <EditableList
                items={actor.concerns}
                onChange={(items) => onUpdate({ ...actor, concerns: items })}
                placeholder="e.g., Regulatory risk"
              />
            </div>

            {/* Experience */}
            <div>
              <InfoLabel
                label="Experience Summary"
                tooltip="Background and expertise that shapes this actor's credibility and perspective. Affects how other actors respond to their arguments."
                className="text-sm font-semibold text-gray-600 mb-2"
              />
              <textarea
                value={actor.experience_summary || ''}
                onChange={(e) => onUpdate({ ...actor, experience_summary: e.target.value })}
                className="w-full bg-white border border-gray-200 rounded-lg px-3 py-2 text-sm text-gray-800 h-20 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500/30"
                placeholder="e.g., 15 years in financial regulation..."
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
