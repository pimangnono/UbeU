import { redis } from '@/lib/redis';
import { getPersonaById } from '@/data/personas';
import OpenAI from 'openai';

// Initialize OpenAI client
// Ensure OPENAI_API_KEY is set in your .env.local
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

export interface SimulationState {
    id: string;
    personaId: string;
    messages: { role: 'system' | 'user' | 'assistant'; content: string }[];
    status: 'active' | 'completed';
    createdAt: number;
    updatedAt: number;
}

const SIMULATION_PREFIX = 'simulation:';
const EXPIRY_SECONDS = 60 * 60 * 24; // 24 hours

export class AgentOrchestrator {

    /**
     * Starts a new simulation with a specific persona.
     */
    async startSimulation(simulationId: string, personaId: string): Promise<SimulationState> {
        const persona = getPersonaById(personaId);
        if (!persona) {
            throw new Error(`Persona with ID ${personaId} not found`);
        }

        const initialState: SimulationState = {
            id: simulationId,
            personaId,
            messages: [
                { role: 'system', content: persona.systemPrompt }
            ],
            status: 'active',
            createdAt: Date.now(),
            updatedAt: Date.now(),
        };

        await this.saveState(simulationId, initialState);
        return initialState;
    }

    /**
     * Processes a user turn: saves user message, calls LLM, saves assistant response.
     */
    async processTurn(simulationId: string, userMessage: string): Promise<string> {
        const state = await this.loadState(simulationId);
        if (!state) {
            throw new Error(`Simulation ${simulationId} not found`);
        }

        // Append user message
        state.messages.push({ role: 'user', content: userMessage });

        // Call OpenAI
        const completion = await openai.chat.completions.create({
            model: 'gpt-4o', // or gpt-3.5-turbo
            messages: state.messages as any,
        });

        const assistantMessage = completion.choices[0]?.message?.content || "I'm sorry, I couldn't generate a response.";

        // Append assistant message
        state.messages.push({ role: 'assistant', content: assistantMessage });
        state.updatedAt = Date.now();

        // Save updated state
        await this.saveState(simulationId, state);

        return assistantMessage;
    }

    /**
     * Loads simulation state from Redis.
     */
    async loadState(simulationId: string): Promise<SimulationState | null> {
        const data = await redis.get(`${SIMULATION_PREFIX}${simulationId}`);
        if (!data) return null;
        return JSON.parse(data);
    }

    /**
     * Saves simulation state to Redis.
     */
    private async saveState(simulationId: string, state: SimulationState): Promise<void> {
        await redis.set(
            `${SIMULATION_PREFIX}${simulationId}`,
            JSON.stringify(state),
            'EX',
            EXPIRY_SECONDS
        );
    }
}

export const agentOrchestrator = new AgentOrchestrator();
