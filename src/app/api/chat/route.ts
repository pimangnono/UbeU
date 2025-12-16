import { NextRequest, NextResponse } from 'next/server';
import { agentOrchestrator } from '@/services/agentOrchestrator';

export async function POST(req: NextRequest) {
    try {
        const body = await req.json();
        const { simulationId, message, personaId, action } = body;

        if (action === 'start') {
            if (!simulationId || !personaId) {
                return NextResponse.json({ error: 'Missing simulationId or personaId' }, { status: 400 });
            }
            const state = await agentOrchestrator.startSimulation(simulationId, personaId);
            return NextResponse.json(state);
        }

        if (action === 'chat') {
            if (!simulationId || !message) {
                return NextResponse.json({ error: 'Missing simulationId or message' }, { status: 400 });
            }
            const response = await agentOrchestrator.processTurn(simulationId, message);
            return NextResponse.json({ response });
        }

        return NextResponse.json({ error: 'Invalid action' }, { status: 400 });

    } catch (error: any) {
        console.error('API Error:', error);
        return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
    }
}
