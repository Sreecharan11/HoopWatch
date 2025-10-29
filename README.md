# 🏀 HoopWatch - NBA Event Tracker

A full-stack web application for tracking NBA players, games, and events. Users can favorite players and games to see upcoming events on their personalized dashboard.

## 🛠️ Tech Stack

### Frontend
- **React** - UI library
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls

### Backend
- **Django 5.2.7** - Python web framework
- **Django REST Framework** - RESTful API
- **SQLite** - Database (development)

### Key Features (Planned)
- ⭐ Favorite NBA players and games
- 📊 Personalized dashboard with upcoming events
- 🔔 Event tracking and notifications
- 📅 Game schedules and player statistics
- 🔐 User authentication and profiles

## 📁 Project Structure

```
HoopWatch/
├── backend/                 # Django backend
│   ├── settings.py         # Django settings with CORS and REST framework
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── frontend/               # React frontend
│   ├── src/
│   │   ├── api/           # API utilities
│   │   │   └── axios.js   # Axios configuration
│   │   ├── App.jsx        # Main App component
│   │   ├── App.css        # App styles
│   │   ├── main.jsx       # Entry point
│   │   └── index.css      # Global styles
│   ├── index.html         # HTML template
│   ├── vite.config.js     # Vite configuration
│   └── package.json       # Frontend dependencies
├── venv/                   # Python virtual environment
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13+ installed
- Node.js 22+ installed
- npm or yarn package manager

### Backend Setup

1. **Activate the virtual environment:**

   Windows (PowerShell):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Windows (Command Prompt):
   ```cmd
   .\venv\Scripts\activate.bat
   ```

   macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

2. **Install Python dependencies (if needed):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (for Django admin):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

   The backend will run at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies (if needed):**
   ```bash
   npm install
   ```

3. **Start the Vite development server:**
   ```bash
   npm run dev
   ```

   The frontend will run at `http://localhost:5173`

## 🔧 Development

### Running Both Servers

You'll need two terminal windows:

**Terminal 1 - Backend:**
```bash
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Django Admin

Access the Django admin panel at `http://localhost:8000/admin` using the superuser credentials you created.

## 📝 Next Steps

### Backend Development
1. Create Django apps for:
   - `users` - User authentication and profiles
   - `players` - NBA player data
   - `games` - Game schedules and information
   - `events` - Event tracking
   - `favorites` - User favorites

2. Define models for:
   - Player (name, team, position, stats)
   - Game (date, teams, venue, status)
   - Event (type, date, player/game reference)
   - UserFavorite (user, player/game reference)

3. Create API endpoints:
   - `/api/players/` - List and detail views
   - `/api/games/` - Game schedules
   - `/api/events/` - Event listings
   - `/api/favorites/` - User favorites CRUD
   - `/api/auth/` - Authentication endpoints

### Frontend Development
1. Create components:
   - `Dashboard` - Main user dashboard
   - `PlayerList` - Browse players
   - `GameList` - Browse games
   - `EventCard` - Display event information
   - `FavoriteButton` - Toggle favorites
   - `Navbar` - Navigation
   - `Login/Register` - Authentication forms

2. Implement routing:
   - `/` - Dashboard
   - `/players` - Player list
   - `/games` - Game list
   - `/login` - Login page
   - `/register` - Registration page

3. API Integration:
   - Use the configured axios instance in `src/api/axios.js`
   - Create service files for different API endpoints
   - Implement state management (Context API or Redux)

### External NBA API Integration
Consider integrating with:
- [NBA API](https://www.balldontlie.io/) - Free NBA stats API
- [ESPN API](http://www.espn.com/apis/devcenter/docs/) - Sports data
- [The Sports DB](https://www.thesportsdb.com/api.php) - Sports database

## 🔐 Environment Variables

For production, create a `.env` file:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 📦 Building for Production

### Frontend
```bash
cd frontend
npm run build
```

The built files will be in `frontend/dist/`

### Backend
1. Update `settings.py` for production
2. Use a production-ready database (PostgreSQL)
3. Configure static files serving
4. Set up a WSGI server (Gunicorn)

## 🤝 Contributing

This is a portfolio/interview project, but suggestions are welcome!

## 📄 License

This project is open source and available for educational purposes.

## 🎯 Interview Talking Points

- **Full-stack development** - React frontend + Django backend
- **RESTful API design** - Django REST Framework
- **Modern frontend tooling** - Vite, React Router
- **Database design** - SQLite with Django ORM
- **CORS handling** - Cross-origin requests between frontend/backend
- **API integration** - External NBA data APIs
- **User authentication** - Django session authentication
- **Responsive design** - Modern CSS and component architecture

---

Built with ❤️ for NBA fans and tech enthusiasts

