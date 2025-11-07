import {useState, useEffect} from 'react';
import { getFavorites, deleteFavorite } from '../api/services';
import './FavoritesPage.css';

function FavoritesPage() { 
    const [favorites, setFavorites] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchFavorites();
    }, []);

    const fetchFavorites = async () => {
        try {
            const response = await getFavorites();
            setFavorites(response.data);
            setError(null);
        } catch (err) {
            setError('Failed to load favorites');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (favoriteId) => {
        try {
            await deleteFavorite(favoriteId);
            setFavorites(favorites.filter(fav => fav.id !== favoriteId));
        } catch (err) {
            console.error('Failed to delete favorite:', err);
        }
    };

    const playerFavorites = favorites.filter(fav => fav.favorite_type === 'player');
    const teamFavorites = favorites.filter(fav => fav.favorite_type === 'team');

    if (loading) return <div className="loading">Loading...</div>;
    if (error) return <div className="error">{error}</div>;

    if (favorites.length === 0) {
        return (
            <div className="page-container">
                <h1>My Favorites ⭐</h1>
                <div className="empty-state">
                    <p>You haven't favorited anything yet!</p>
                    <p>Go to Players or Teams page to add favorites.</p>
                </div>
            </div>
        );
    }

    return (
        <div className="page-container">
            <h1>My Favorites ⭐</h1>

            {playerFavorites.length > 0 && (
                <div className="favorites-section">
                    <h2 className="section-title">
                        <span className="section-icon">👤</span>
                        Favorite Players ({playerFavorites.length})
                    </h2>
                    <div className="favorites-grid">
                        {playerFavorites.map((favorite) => (
                            <div key={favorite.id} className="favorite-card player-card">
                                <button 
                                    className="delete-btn"
                                    onClick={() => handleDelete(favorite.id)}
                                    title="Remove favorite"
                                >
                                    ❌
                                </button>
                                <div className="favorite-content">
                                    <h3>{favorite.player_name}</h3>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {teamFavorites.length > 0 && (
                <div className="favorites-section">
                    <h2 className="section-title">
                        <span className="section-icon">🏀</span>
                        Favorite Teams ({teamFavorites.length})
                    </h2>
                    <div className="favorites-grid">
                        {teamFavorites.map((favorite) => (
                            <div key={favorite.id} className="favorite-card team-card">
                                <button 
                                    className="delete-btn"
                                    onClick={() => handleDelete(favorite.id)}
                                    title="Remove favorite"
                                >
                                    ❌
                                </button>
                                <div className="favorite-content">
                                    <h3>{favorite.team_name}</h3>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            <div className="results-count">
                Total: {favorites.length} favorite{favorites.length !== 1 ? 's' : ''} 
                ({playerFavorites.length} player{playerFavorites.length !== 1 ? 's' : ''}, {teamFavorites.length} team{teamFavorites.length !== 1 ? 's' : ''})
            </div>
        </div>
    );
};

export default FavoritesPage;

