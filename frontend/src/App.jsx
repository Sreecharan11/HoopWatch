import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>🏀 HoopWatch</h1>
          <p>Track your favorite NBA players and games</p>
        </header>
        
        <Routes>
          <Route path="/" element={
            <div className="welcome">
              <h2>Welcome to HoopWatch!</h2>
              <p>Your NBA event tracking application</p>
              <div className="info">
                <h3>Features Coming Soon:</h3>
                <ul>
                  <li>📊 Dashboard with upcoming events</li>
                  <li>⭐ Favorite players and games</li>
                  <li>🔔 Event notifications</li>
                  <li>📅 Game schedules</li>
                </ul>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  )
}

export default App

