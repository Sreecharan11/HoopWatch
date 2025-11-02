import {useState, useEffect} from 'react';
import { getPlayers } from '../api/services';
import './PlayersPage.css';

function PlayersPage() { 
    const [players, setPlayers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchPlayers();
    }, []);

    const fetchPlayers = async (searchTerm = '') => {
        try {
          const response = await getPlayers(searchTerm);
          setPlayers(response.data);
          setError(null);
        } catch (err) {
          setError('Failed to load players');
          console.error(err);
        } finally {
          setLoading(false);
        }
      };

      const handleSearch = (e) => {
        const value = e.target.value;
        setSearch(value);
        fetchPlayers(value);
      };

      if (loading) return <div className="loading">Loading...</div>;
      if (error) return <div className="error">{error}</div>;

      return (
        <div className="page-container">
            <h1>NBA Players</h1>

            <div className="search-bar">
                <input 
                type="text" 
                placeholder="Search players" 
                value={search} 
                onChange={handleSearch} 
                />
            </div>

            <div className="table-container">
                <table className="data-table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Position</th>
                            <th>Team</th>
                            <th>Height</th>
                            <th>Weight</th>
                            <th>Jersey Number</th>
                        </tr>
                    </thead>
                    <tbody>
                        {players.map((player) => (
                            <tr key={player.id}>
                                <td>{player.full_name}</td>
                                <td>{player.position}</td>
                                <td>{player.team_name}</td>
                                <td>{player.height || '-'}</td>
                                <td>{player.weight_pounds ? `${player.weight_pounds} lbs` : '-'}</td>
                                <td>{player.jersey_number || '-'}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="results-count">
                Showing {players.length} results
            </div>
        </div>
   
      );
};

export default PlayersPage;