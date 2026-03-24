import { create } from 'zustand';

interface SelectionState {
  selectedPhase: string | null;
  selectedActor: string | null;
  selectedRelationship: [string, string] | null;
  selectedTurn: number | null;

  setPhase: (phase: string | null) => void;
  setActor: (actor: string | null) => void;
  setRelationship: (rel: [string, string] | null) => void;
  setTurn: (turn: number | null) => void;
  clearAll: () => void;
}

export const useSelectionStore = create<SelectionState>((set) => ({
  selectedPhase: null,
  selectedActor: null,
  selectedRelationship: null,
  selectedTurn: null,

  setPhase: (phase) => set({ selectedPhase: phase }),
  setActor: (actor) => set({ selectedActor: actor }),
  setRelationship: (rel) => set({ selectedRelationship: rel }),
  setTurn: (turn) => set({ selectedTurn: turn }),
  clearAll: () =>
    set({
      selectedPhase: null,
      selectedActor: null,
      selectedRelationship: null,
      selectedTurn: null,
    }),
}));
