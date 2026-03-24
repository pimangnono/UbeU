import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Setup from './pages/Setup';
import LiveMonitoring from './pages/LiveMonitoring';
import Results from './pages/Results';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30_000,
      retry: 1,
    },
  },
});

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/setup" element={<Setup />} />
          <Route path="/simulation/:id" element={<LiveMonitoring />} />
          <Route path="/simulation/:id/results" element={<Results />} />
          <Route path="*" element={<Navigate to="/setup" replace />} />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}
