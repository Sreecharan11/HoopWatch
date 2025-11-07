import {useState, useEffect} from 'react';
import { getMyEvents } from '../api/services';
import './EventsPage.css';

function EventsPage() { 
    const [events, setEvents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchEvents();
    }, []);

    const fetchEvents = async () => {
        try {
            const response = await getMyEvents();
            setEvents(response.data);
            setError(null);
        } catch (err) {
            setError('Failed to load events');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', { 
            weekday: 'long', 
            month: 'long', 
            day: 'numeric',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    };

    const groupReasonsByType = (reasons) => {
        const teams = reasons.filter(r => r.type === 'team').map(r => r.name);
        const players = reasons.filter(r => r.type === 'player').map(r => r.name);
        return { teams, players };
    };

    if (loading) return <div className="loading">Loading your events...</div>;
    if (error) return <div className="error">{error}</div>;

    if (events.length === 0) {
        return (
            <div className="page-container">
                <h1>My Upcoming Events 📅</h1>
                <div className="empty-state">
                    <div className="empty-icon">🏀</div>
                    <h2>No Upcoming Events</h2>
                    <p>You don't have any favorited players or teams yet!</p>
                    <p>Go to the Players or Teams page to add favorites and see their upcoming games here.</p>
                </div>
            </div>
        );
    }

    return (
        <div className="page-container">
            <h1>My Upcoming Events 📅</h1>
            <p className="events-subtitle">Games featuring your favorite players and teams</p>

            <div className="events-list">
                {events.map((event) => {
                    const { teams, players } = groupReasonsByType(event.favorite_reasons || []);
                    
                    return (
                        <div key={event.id} className="event-card">
                            <div className="event-date">
                                {formatDate(event.date)}
                            </div>
                            
                            <div className="event-matchup">
                                <div className="event-team visitor">
                                    <span className="team-name">{event.visitor_team_name}</span>
                                    <span className="team-label">Away</span>
                                </div>
                                
                                <div className="vs-badge">VS</div>
                                
                                <div className="event-team home">
                                    <span className="team-name">{event.home_team_name}</span>
                                    <span className="team-label">Home</span>
                                </div>
                            </div>

                            <div className="event-favorites">
                                {teams.length > 0 && (
                                    <div className="favorite-reason">
                                        <span className="reason-icon">⭐</span>
                                        <span className="reason-text">
                                            <strong>Favorite Team{teams.length > 1 ? 's' : ''}:</strong> {teams.join(', ')}
                                        </span>
                                    </div>
                                )}
                                
                                {players.length > 0 && (
                                    <div className="favorite-reason">
                                        <span className="reason-icon">👤</span>
                                        <span className="reason-text">
                                            <strong>Favorite Player{players.length > 1 ? 's' : ''}:</strong> {players.join(', ')}
                                        </span>
                                    </div>
                                )}
                            </div>
                        </div>
                    );
                })}
            </div>

        </div>
    );
};

export default EventsPage;

