import { agentOrchestrator } from '../src/services/agentOrchestrator';
import { redis } from '../src/lib/redis';

async function main() {
    const simulationId = 'test-sim-' + Date.now();
    const personaId = 'helpful-assistant';

    console.log(`Starting simulation ${simulationId} with persona ${personaId}...`);

    try {
        // 1. Start Simulation
        const state = await agentOrchestrator.startSimulation(simulationId, personaId);
        console.log('Simulation started:', state);

        // 2. Process Turn
        const userMessage = "Hello, can you help me with my resume?";
        console.log(`User says: "${userMessage}"`);

        // Note: This will fail if OPENAI_API_KEY is not set or if Redis is not running.
        // We catch errors to handle them gracefully.
        const response = await agentOrchestrator.processTurn(simulationId, userMessage);
        console.log(`Assistant says: "${response}"`);

        // 3. Verify State Persistence
        const loadedState = await agentOrchestrator.loadState(simulationId);
        console.log('Loaded state from Redis:', loadedState);

        if (loadedState?.messages.length === 3) {
            console.log('SUCCESS: State persisted correctly (System + User + Assistant)');
        } else {
            console.error('FAILURE: State mismatch');
        }

    } catch (error) {
        console.error('Error during test:', error);
    } finally {
        await redis.quit();
    }
}

main();
