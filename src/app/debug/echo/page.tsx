'use client';

import { useState, useEffect, useRef } from 'react';

export default function EchoDebugPage() {
    const [status, setStatus] = useState('Disconnected');
    const [messages, setMessages] = useState<string[]>([]);
    const [input, setInput] = useState('');
    const ws = useRef<WebSocket | null>(null);

    useEffect(() => {
        // Connect to FastAPI WebSocket
        const socket = new WebSocket('ws://localhost:8000/ws/debug-user');

        socket.onopen = () => setStatus('Connected to Backend');
        socket.onclose = () => setStatus('Disconnected');

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setMessages(prev => [...prev, `📩 ${data.sender}: ${data.text}`]);
        };

        ws.current = socket;

        return () => socket.close();
    }, []);

    const sendMessage = () => {
        if (ws.current && input) {
            const payload = { text: input, sender: "User" };
            ws.current.send(JSON.stringify(payload));
            setMessages(prev => [...prev, `ME: ${input}`]);
            setInput('');
        }
    };

    return (
        <div style={{ padding: 40, fontFamily: 'monospace' }}>
            <h1>🔌 The Spine Test (Echo Loop)</h1>
            <div style={{
                padding: 10,
                background: status === 'Connected to Backend' ? '#dcfce7' : '#fee2e2',
                borderRadius: 8,
                marginBottom: 20
            }}>
                Status: <strong>{status}</strong>
            </div>

            <div style={{
                border: '1px solid #ccc',
                height: 300,
                overflowY: 'scroll',
                padding: 10,
                marginBottom: 20
            }}>
                {messages.map((m, i) => <div key={i}>{m}</div>)}
            </div>

            <input
                value={input}
                onChange={e => setInput(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && sendMessage()}
                placeholder="Type to test Redis..."
                style={{ padding: 10, width: '300px' }}
            />
            <button onClick={sendMessage} style={{ padding: '10px 20px', marginLeft: 10 }}>
                Send
            </button>
        </div>
    );
}
