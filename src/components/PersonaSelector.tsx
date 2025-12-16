'use client';

import { PERSONAS, Persona } from '@/data/personas';
import { useState } from 'react';

interface PersonaSelectorProps {
    onSelect: (personaId: string) => void;
    selectedPersonaId?: string;
}

export default function PersonaSelector({ onSelect, selectedPersonaId }: PersonaSelectorProps) {
    return (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {PERSONAS.map((persona) => (
                <div
                    key={persona.id}
                    onClick={() => onSelect(persona.id)}
                    className={`cursor-pointer border rounded-lg p-4 transition-all hover:shadow-md ${selectedPersonaId === persona.id
                            ? 'border-blue-500 bg-blue-50 ring-2 ring-blue-200'
                            : 'border-gray-200 bg-white'
                        }`}
                >
                    <div className="flex items-center justify-between mb-2">
                        <h3 className="font-semibold text-gray-900">{persona.name}</h3>
                        <span className={`text-xs px-2 py-1 rounded-full ${persona.voice === 'formal' ? 'bg-purple-100 text-purple-700' :
                                persona.voice === 'assertive' ? 'bg-red-100 text-red-700' :
                                    'bg-green-100 text-green-700'
                            }`}>
                            {persona.voice}
                        </span>
                    </div>
                    <p className="text-sm text-gray-500 mb-3">{persona.role}</p>
                    <div className="flex flex-wrap gap-1">
                        {persona.traits.map((trait) => (
                            <span key={trait} className="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded">
                                {trait}
                            </span>
                        ))}
                    </div>
                </div>
            ))}
        </div>
    );
}
