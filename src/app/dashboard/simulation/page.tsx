'use client';

import { useState } from 'react';
import PersonaSelector from '@/components/PersonaSelector';
import ChatInterface from '@/components/ChatInterface';

export default function SimulationPage() {
    const [selectedPersonaId, setSelectedPersonaId] = useState<string | null>(null);
    const [simulationId, setSimulationId] = useState<string>('');

    const handlePersonaSelect = (id: string) => {
        setSelectedPersonaId(id);
        // Generate a random simulation ID for this session
        setSimulationId(`sim-${Date.now()}`);
    };

    return (
        <div className="p-8 max-w-6xl mx-auto">
            <h1 className="text-3xl font-bold mb-8 text-gray-900">AI Simulation Playground</h1>

            {!selectedPersonaId ? (
                <div className="space-y-6">
                    <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
                        <h2 className="text-xl font-semibold mb-2 text-blue-900">Select a Persona</h2>
                        <p className="text-blue-700 mb-4">
                            Choose an AI persona to start a simulation. Each persona has a unique voice and role.
                        </p>
                        <PersonaSelector onSelect={handlePersonaSelect} />
                    </div>
                </div>
            ) : (
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div className="lg:col-span-1 space-y-6">
                        <div className="bg-white border rounded-lg p-6 shadow-sm">
                            <h3 className="font-semibold text-gray-700 mb-4">Current Session</h3>
                            <div className="space-y-3 text-sm">
                                <div>
                                    <span className="text-gray-500 block">Simulation ID</span>
                                    <span className="font-mono text-gray-900">{simulationId}</span>
                                </div>
                                <div>
                                    <span className="text-gray-500 block">Persona ID</span>
                                    <span className="font-mono text-gray-900">{selectedPersonaId}</span>
                                </div>
                                <button
                                    onClick={() => setSelectedPersonaId(null)}
                                    className="w-full mt-4 px-4 py-2 border border-gray-300 rounded text-gray-600 hover:bg-gray-50"
                                >
                                    End Session & Change Persona
                                </button>
                            </div>
                        </div>
                    </div>

                    <div className="lg:col-span-2">
                        <ChatInterface
                            simulationId={simulationId}
                            personaId={selectedPersonaId}
                        />
                    </div>
                </div>
            )}
        </div>
    );
}
