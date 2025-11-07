import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
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
              <h1>🏀 HoopWatch Dashboard</h1>
              <div className="dashboard-welcome">
                <h2>Welcome to HoopWatch!</h2>
                <p>Your personalized NBA tracking app with CRUD functionality!</p>
                <div className="dashboard-stats">
                  <div className="stat-card">
                    <h3>Players</h3>
                    <p>Browse & favorite players</p>
                  </div>
                  <div className="stat-card">
                    <h3>Teams</h3>
                    <p>Explore & favorite teams</p>
                  </div>
                  <div className="stat-card">
                    <h3>Events</h3>
                    <p>Your upcoming games</p>
                  </div>
                  <div className="stat-card">
                    <h3>Favorites</h3>
                    <p>Manage your favorites</p>
                  </div>
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