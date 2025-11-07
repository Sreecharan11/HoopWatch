import {useState, useEffect} from 'react';
import { getPlayers, getFavorites, addFavorite, deleteFavorite } from '../api/services';
import './PlayersPage.css';

function PlayersPage() { 
    const [players, setPlayers] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchPlayers();
        fetchFavorites();
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

    const fetchFavorites = async () => {
        try {
            const response = await getFavorites();
            setFavorites(response.data);
        } catch (err) {
            console.error('Failed to load favorites:', err);
        }
    };

    const handleSearch = (e) => {
        const value = e.target.value;
        setSearch(value);
        fetchPlayers(value);
    };

    const isFavorited = (playerId) => {
        return favorites.some(fav => fav.player === playerId);
    };

    const handleFavoriteToggle = async (playerId) => {
        try {
            const existingFavorite = favorites.find(fav => fav.player === playerId);
            
            if (existingFavorite) {
                await deleteFavorite(existingFavorite.id);
                setFavorites(favorites.filter(fav => fav.id !== existingFavorite.id));
            } else {
                const response = await addFavorite({
                    favorite_type: 'player',
                    player: playerId
                });
                setFavorites([...favorites, response.data]);
            }
        } catch (err) {
            console.error('Failed to toggle favorite:', err);
            console.error('Error details:', err.response?.data);
        }
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
                            <th>Favorite</th>
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
                                <td>
                                    <button 
                                        className={`favorite-btn ${isFavorited(player.id) ? 'favorited' : ''}`}
                                        onClick={() => handleFavoriteToggle(player.id)}
                                        title={isFavorited(player.id) ? 'Remove from favorites' : 'Add to favorites'}
                                    >
                                        {isFavorited(player.id) ? '❤️' : '🤍'}
                                    </button>
                                </td>
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

        </div>
   
      );
};

export default PlayersPage;