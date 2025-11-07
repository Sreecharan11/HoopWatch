import {useState, useEffect} from 'react';
import { getTeams, getFavorites, addFavorite, deleteFavorite } from '../api/services';
import './TeamsPage.css';

function TeamsPage() { 
    const [teams, setTeams] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchTeams();
        fetchFavorites();
    }, []);

    const fetchTeams = async (searchTerm = '') => {
        try {
          const response = await getTeams(searchTerm);
          setTeams(response.data);
          setError(null);
        } catch (err) {
          setError('Failed to load teams');
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
        fetchTeams(value);
    };

    const isFavorited = (teamId) => {
        return favorites.some(fav => fav.team === teamId);
    };

    const handleFavoriteToggle = async (teamId) => {
        try {
            const existingFavorite = favorites.find(fav => fav.team === teamId);
            
            if (existingFavorite) {
                await deleteFavorite(existingFavorite.id);
                setFavorites(favorites.filter(fav => fav.id !== existingFavorite.id));
            } else {
                const response = await addFavorite({
                    favorite_type: 'team',
                    team: teamId
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
            <h1>NBA Teams</h1>

            <div className="search-bar">
                <input 
                type="text" 
                placeholder="Search teams" 
                value={search} 
                onChange={handleSearch} 
                />
            </div>

            <div className="teams-grid">
                {teams.map((team) => (
                    <div key={team.id} className="team-card">
                        <button 
                            className={`favorite-btn ${isFavorited(team.id) ? 'favorited' : ''}`}
                            onClick={() => handleFavoriteToggle(team.id)}
                            title={isFavorited(team.id) ? 'Remove from favorites' : 'Add to favorites'}
                        >
                            {isFavorited(team.id) ? '❤️' : '🤍'}
                        </button>
                        <h3>{team.full_name}</h3>
                        <p className="team-abbreviation">{team.abbreviation}</p>
                        <p className="team-conference">{team.conference}</p>
                        <p className="team-division">{team.division}</p>
                    </div>
                ))}
            </div>

        </div>
      );
};

export default TeamsPage;

