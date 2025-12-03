import Link from 'next/link';

export default function Home() {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
      background: 'var(--bg-body)',
      gap: '2rem'
    }}>
      <h1 style={{ fontSize: '3rem', fontWeight: 'bold', color: 'var(--primary)' }}>UbeU</h1>
      <p style={{ fontSize: '1.25rem', color: 'var(--text-secondary)' }}>Interactive Interview Platform</p>

      <div style={{ display: 'flex', gap: '1rem' }}>
        <Link href="/dashboard" className="btn btn-primary" style={{ padding: '1rem 2rem', fontSize: '1.1rem' }}>
          Login as HR Manager
        </Link>
        <button className="btn btn-outline" style={{ padding: '1rem 2rem', fontSize: '1.1rem' }} disabled>
          Candidate Login (Coming Soon)
        </button>
      </div>
    </div>
  );
}
