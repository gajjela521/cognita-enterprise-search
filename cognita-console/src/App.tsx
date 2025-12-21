import { useState } from 'react';

interface SearchResult {
  text: string;
  score: number;
}

interface ApiResponse {
  results: SearchResult[];
}

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setError(null);
    setResults([]);

    try {
      // Connects to Spring Boot Backend (env var or default localhost)
      const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8080';
      const response = await fetch(`${API_BASE_URL}/api/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: query }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch results');
      }

      const data: ApiResponse = await response.json();
      setResults(data.results);
    } catch (err) {
      console.error(err);
      setError('Something went wrong. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <header>
        <h1>Cognita Enterprise Search</h1>
        <h2>Intelligent Knowledge Discovery</h2>
      </header>

      <div className="search-container">
        <form onSubmit={handleSearch}>
          <input
            type="text"
            placeholder="Ask anything about your documents..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Searching...' : 'Search Engine'}
          </button>
        </form>
        {error && <p style={{ color: '#ef4444', marginTop: '1rem' }}>{error}</p>}
      </div>

      <div className="results-grid">
        {results.map((result, index) => (
          <div key={index} className="result-card glass-card">
            <span className="score-badge">Match Score: {result.score.toFixed(4)}</span>
            <p className="result-text">{result.text}</p>
          </div>
        ))}

        {!loading && results.length === 0 && query && !error && (
          <p style={{ color: '#94a3b8' }}>No results found or search not started.</p>
        )}
      </div>
    </>
  );
}

export default App;
