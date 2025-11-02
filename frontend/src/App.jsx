import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import PlayersPage from './pages/PlayersPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={
            <div className="page-container">
              <h1>Dashboard</h1>
              <div className="dashboard-welcome">
                <h2>Welcome to HoopWatch! 🏀</h2>
                <p>Track your favorite NBA players, teams, and games.</p>
                <p>Use the navigation above to explore.</p>
              </div>
            </div>
          } />
          <Route path="/players" element={<PlayersPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;