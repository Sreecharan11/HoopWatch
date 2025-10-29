# 📂 HoopWatch Project Structure

## Overview
```
HoopWatch/
├── 📁 backend/              # Django backend configuration
├── 📁 frontend/             # React frontend application
├── 📁 venv/                 # Python virtual environment
├── 📄 manage.py             # Django management script
├── 📄 db.sqlite3            # SQLite database
├── 📄 requirements.txt      # Python dependencies
├── 📄 README.md             # Main documentation
├── 📄 SETUP_GUIDE.md        # Quick setup instructions
├── 📄 NBA_API_RESOURCES.md  # NBA API integration guide
└── 📄 .gitignore            # Git ignore rules
```

## Backend Structure (`/backend`)

```
backend/
├── __init__.py              # Python package marker
├── settings.py              # Django settings (CORS, REST, Database)
├── urls.py                  # URL routing configuration
├── wsgi.py                  # WSGI application entry point
└── asgi.py                  # ASGI application entry point
```

### Key Configurations in `settings.py`:
- ✅ Django REST Framework installed
- ✅ CORS headers configured for React frontend
- ✅ SQLite database configured
- ✅ Session authentication enabled

### Next Steps for Backend:
1. Create Django apps:
   ```bash
   python manage.py startapp players
   python manage.py startapp games
   python manage.py startapp events
   python manage.py startapp favorites
   python manage.py startapp users
   ```

2. Add apps to `INSTALLED_APPS` in `settings.py`

3. Create models in each app's `models.py`

4. Create serializers in each app's `serializers.py`

5. Create views/viewsets in each app's `views.py`

6. Register URLs in each app's `urls.py`

## Frontend Structure (`/frontend`)

```
frontend/
├── 📁 public/               # Static assets
│   └── vite.svg
├── 📁 src/                  # Source code
│   ├── 📁 api/              # API configuration
│   │   ├── axios.js         # Axios instance with interceptors
│   │   └── services.js      # API service functions
│   ├── App.jsx              # Main App component
│   ├── App.css              # App styles
│   ├── main.jsx             # React entry point
│   └── index.css            # Global styles
├── index.html               # HTML template
├── vite.config.js           # Vite configuration (proxy setup)
├── package.json             # Dependencies and scripts
└── package-lock.json        # Locked dependencies
```

### Installed Frontend Dependencies:
- ✅ React 18.3.1
- ✅ React DOM 18.3.1
- ✅ React Router DOM 7.9.5
- ✅ Axios 1.13.1
- ✅ Vite 7.1.7

### Next Steps for Frontend:
1. Create component structure:
   ```
   src/
   ├── components/
   │   ├── Navbar.jsx
   │   ├── Dashboard.jsx
   │   ├── PlayerCard.jsx
   │   ├── GameCard.jsx
   │   ├── EventCard.jsx
   │   └── FavoriteButton.jsx
   ├── pages/
   │   ├── Home.jsx
   │   ├── Players.jsx
   │   ├── Games.jsx
   │   ├── Login.jsx
   │   └── Register.jsx
   ├── context/
   │   └── AuthContext.jsx
   └── hooks/
       └── useFetch.js
   ```

2. Implement routing in `App.jsx`

3. Create API service calls using `services.js`

4. Add state management (Context API or Redux)

## Database Schema (Planned)

### Users (Django built-in)
- id, username, email, password, etc.

### Players
- id, api_id, first_name, last_name, position, team, height, weight
- timestamps (created_at, updated_at)

### Games
- id, api_id, date, home_team, visitor_team, scores, status, season
- timestamps (created_at, updated_at)

### Events
- id, event_type, date, description, player_id, game_id
- timestamps (created_at, updated_at)

### Favorites
- id, user_id, favorite_type (player/game), favorite_id
- timestamps (created_at, updated_at)

## API Endpoints (Planned)

### Authentication
```
POST   /api/auth/register/        # Register new user
POST   /api/auth/login/           # Login
POST   /api/auth/logout/          # Logout
GET    /api/auth/user/            # Get current user
```

### Players
```
GET    /api/players/              # List all players
GET    /api/players/:id/          # Get player details
GET    /api/players/?search=name  # Search players
```

### Games
```
GET    /api/games/                # List all games
GET    /api/games/:id/            # Get game details
GET    /api/games/?status=upcoming # Filter by status
```

### Events
```
GET    /api/events/               # List all events
GET    /api/events/favorites/     # Get events for user's favorites
```

### Favorites
```
GET    /api/favorites/            # Get user's favorites
POST   /api/favorites/            # Add favorite
DELETE /api/favorites/:id/        # Remove favorite
```

## Development Workflow

### 1. Start Development Servers

**Terminal 1 - Backend:**
```bash
.\venv\Scripts\Activate.ps1
python manage.py runserver
# Runs on http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
# Runs on http://localhost:5173
```

### 2. Make Changes

**Backend Changes:**
1. Modify models → `python manage.py makemigrations` → `python manage.py migrate`
2. Create/update serializers
3. Create/update views
4. Update URLs
5. Test in Django REST browsable API

**Frontend Changes:**
1. Create/update components
2. Update routing
3. Add API calls
4. Style with CSS
5. Test in browser

### 3. Test Integration
- Frontend makes API calls to `http://localhost:8000/api`
- Backend responds with JSON data
- CORS is configured to allow requests from `http://localhost:5173`

## Environment Setup

### Python Virtual Environment
- Location: `./venv/`
- Activation: `.\venv\Scripts\Activate.ps1` (Windows)
- Deactivation: `deactivate`

### Node Modules
- Location: `./frontend/node_modules/`
- Install: `npm install` (in frontend directory)

## Important Files

### Configuration Files
- `backend/settings.py` - Django configuration
- `frontend/vite.config.js` - Vite configuration
- `requirements.txt` - Python dependencies
- `frontend/package.json` - Node dependencies

### Documentation Files
- `README.md` - Main project documentation
- `SETUP_GUIDE.md` - Quick setup instructions
- `NBA_API_RESOURCES.md` - NBA API integration guide
- `PROJECT_STRUCTURE.md` - This file

### Git Files
- `.gitignore` - Files to ignore in git

## Ports

- **Frontend:** 5173 (Vite default)
- **Backend:** 8000 (Django default)

## Tech Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend Framework | React 18 | UI components |
| Frontend Build Tool | Vite | Fast development server |
| Frontend Routing | React Router | Client-side routing |
| HTTP Client | Axios | API requests |
| Backend Framework | Django 5.2 | Web framework |
| API Framework | Django REST Framework | RESTful APIs |
| Database | SQLite | Development database |
| CORS | django-cors-headers | Cross-origin requests |

## Interview Highlights

When discussing this project in interviews, emphasize:

1. **Full-Stack Development:** Built both frontend and backend from scratch
2. **Modern Tech Stack:** React + Django + REST API
3. **API Integration:** External NBA data APIs
4. **Database Design:** Relational database with Django ORM
5. **Authentication:** User authentication and authorization
6. **CORS Handling:** Proper configuration for frontend-backend communication
7. **Project Structure:** Clean, maintainable code organization
8. **Documentation:** Comprehensive README and setup guides

---

Ready to build! 🚀

