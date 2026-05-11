import { create } from 'zustand';

interface SelectionState {
  activeTab: 'outcome' | 'actor';
  selectedPhase: string | null;
  selectedActor: string | null;
  selectedChangeId: string | null;
  selectedRelationship: [string, string] | null;
  selectedRelationshipId: string | null;
  selectedEvidenceType: 'relationship' | 'actor_drift' | 'action';
  selectedTurn: number | null;

  setActiveTab: (tab: 'outcome' | 'actor') => void;
  setPhase: (phase: string | null) => void;
  setActor: (actor: string | null) => void;
  setChange: (changeId: string | null) => void;
  setRelationship: (rel: [string, string] | null) => void;
  setRelationshipId: (relationshipId: string | null) => void;
  setEvidenceType: (evidenceType: 'relationship' | 'actor_drift' | 'action') => void;
  setTurn: (turn: number | null) => void;
  clearAll: () => void;
}

export const useSelectionStore = create<SelectionState>((set) => ({
  activeTab: 'outcome',
  selectedPhase: null,
  selectedActor: null,
  selectedChangeId: null,
  selectedRelationship: null,
  selectedRelationshipId: null,
  selectedEvidenceType: 'relationship',
  selectedTurn: null,

  setActiveTab: (tab) => set({ activeTab: tab }),
  setPhase: (phase) => set({ selectedPhase: phase }),
  setActor: (actor) => set({ selectedActor: actor }),
  setChange: (changeId) => set({ selectedChangeId: changeId }),
  setRelationship: (rel) => set({
    selectedRelationship: rel,
    selectedRelationshipId: rel ? `rel:${rel[0]}:${rel[1]}` : null,
  }),
  setRelationshipId: (relationshipId) => set({
    selectedRelationshipId: relationshipId,
    selectedRelationship: relationshipId?.startsWith('rel:')
      ? ((relationshipId.split(':').slice(1, 3) as [string, string]))
      : null,
  }),
  setEvidenceType: (evidenceType) => set({ selectedEvidenceType: evidenceType }),
  setTurn: (turn) => set({ selectedTurn: turn }),
  clearAll: () =>
    set({
      activeTab: 'outcome',
      selectedPhase: null,
      selectedActor: null,
      selectedChangeId: null,
      selectedRelationship: null,
      selectedRelationshipId: null,
      selectedEvidenceType: 'relationship',
      selectedTurn: null,
    }),
}));
