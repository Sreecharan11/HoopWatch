import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Navbar from './components/Navbar';
import PlayersPage from './pages/PlayersPage';
import TeamsPage from './pages/TeamsPage';
import FavoritesPage from './pages/FavoritesPage';
import EventsPage from './pages/EventsPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={
            <div className="page-container">
              <div className="dashboard-welcome">
                <h2>🏀 Welcome to HoopWatch!</h2>
                <div className="dashboard-stats">
                  <Link to="/players" className="stat-card">
                    <h3>Players</h3>
                    <p>Browse & favorite players</p>
                  </Link>
                  <Link to="/teams" className="stat-card">
                    <h3>Teams</h3>
                    <p>Explore & favorite teams</p>
                  </Link>
                  <Link to="/events" className="stat-card">
                    <h3>Events</h3>
                    <p>Your upcoming games</p>
                  </Link>
                  <Link to="/favorites" className="stat-card">
                    <h3>Favorites</h3>
                    <p>Manage your favorites</p>
                  </Link>
                </div>
              </div>
            </div>
          } />
          <Route path="/players" element={<PlayersPage />} />
          <Route path="/teams" element={<TeamsPage />} />
          <Route path="/events" element={<EventsPage />} />
          <Route path="/favorites" element={<FavoritesPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;