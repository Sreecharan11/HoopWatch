import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-logo">
                    🏀 HoopWatch
                </Link>
                <ul className="nav-menu">
                    <li><Link to="/">Dashboard</Link></li>
                    <li><Link to="/players">Players</Link></li>
                    <li><Link to="/teams">Teams</Link></li>
                    <li><Link to="/events">Events 📅</Link></li>
                    <li><Link to="/favorites">Favorites ⭐</Link></li>
                </ul>
            </div>
        </nav>
    );
};

export default Navbar;