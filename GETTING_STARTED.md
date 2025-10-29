# 🚀 Getting Started with HoopWatch

## ✅ Setup Complete!

Your HoopWatch project is fully configured and ready for development. Here's what's been set up:

### Backend (Django)
- ✅ Django 5.2.7 installed
- ✅ Django REST Framework configured
- ✅ CORS headers enabled for React frontend
- ✅ SQLite database created and migrated
- ✅ Admin interface ready

### Frontend (React)
- ✅ React 18 with Vite
- ✅ React Router for navigation
- ✅ Axios for API calls
- ✅ Modern UI with gradient design
- ✅ API proxy configured

### Documentation
- ✅ Comprehensive README
- ✅ Quick setup guide
- ✅ NBA API resources guide
- ✅ Project structure documentation

---

## 🎯 Quick Start (2 Methods)

### Method 1: Using PowerShell Scripts (Easiest)

**Terminal 1 - Backend:**
```powershell
.\start-backend.ps1
```

**Terminal 2 - Frontend:**
```powershell
.\start-frontend.ps1
```

### Method 2: Manual Start

**Terminal 1 - Backend:**
```powershell
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm run dev
```

---

## 🌐 Access Your Application

Once both servers are running:

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | React application |
| Backend API | http://localhost:8000/api | REST API endpoints |
| Django Admin | http://localhost:8000/admin | Admin panel |

---

## 👤 Create Admin User

Before you can access the Django admin, create a superuser:

```powershell
.\venv\Scripts\Activate.ps1
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email (optional)
- Password

---

## 📋 Next Development Steps

### 1. Create Django Apps (Backend)

```powershell
# Activate virtual environment first
.\venv\Scripts\Activate.ps1

# Create apps
python manage.py startapp players
python manage.py startapp games
python manage.py startapp events
python manage.py startapp favorites
```

### 2. Register Apps in Settings

Add to `backend/settings.py` in `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ... existing apps
    'rest_framework',
    'corsheaders',
    'players',
    'games',
    'events',
    'favorites',
]
```

### 3. Create Models

Example `players/models.py`:
```python
from django.db import models

class Player(models.Model):
    api_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

### 4. Create Serializers

Example `players/serializers.py`:
```python
from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
```

### 5. Create Views

Example `players/views.py`:
```python
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
```

### 6. Register URLs

Example `players/urls.py`:
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)

urlpatterns = router.urls
```

Then in `backend/urls.py`:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('players.urls')),
    path('api/', include('rest_framework.urls')),
]
```

### 7. Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 8. Create React Components

Example component structure:
```
frontend/src/
├── components/
│   ├── Navbar.jsx
│   ├── PlayerCard.jsx
│   ├── GameCard.jsx
│   └── FavoriteButton.jsx
├── pages/
│   ├── Dashboard.jsx
│   ├── Players.jsx
│   └── Games.jsx
└── hooks/
    └── useFetch.js
```

### 9. Implement API Calls

Use the pre-configured services in `frontend/src/api/services.js`:

```javascript
import { playerService } from './api/services';

// In your component
const fetchPlayers = async () => {
  try {
    const response = await playerService.getAll();
    setPlayers(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
};
```

---

## 🏀 NBA API Integration

See `NBA_API_RESOURCES.md` for detailed information on integrating NBA data.

**Quick Start with BallDontLie API:**

1. No API key required
2. Free tier: 60 requests/minute
3. Endpoints:
   - Players: `https://www.balldontlie.io/api/v1/players`
   - Teams: `https://www.balldontlie.io/api/v1/teams`
   - Games: `https://www.balldontlie.io/api/v1/games`

---

## 🛠️ Useful Commands

### Backend Commands

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run server
python manage.py runserver

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Run tests
python manage.py test
```

### Frontend Commands

```powershell
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Install new package
npm install package-name
```

---

## 🐛 Troubleshooting

### Backend won't start
- Make sure virtual environment is activated
- Check if port 8000 is available
- Run migrations: `python manage.py migrate`

### Frontend won't start
- Make sure you're in the `frontend` directory
- Run `npm install` to install dependencies
- Check if port 5173 is available

### CORS errors
- Verify both servers are running
- Check `backend/settings.py` has correct CORS origins
- Clear browser cache and restart servers

### Database errors
- Delete `db.sqlite3` and run `python manage.py migrate` again
- Check model definitions for errors

---

## 📚 Documentation Files

- `README.md` - Main project overview
- `SETUP_GUIDE.md` - Quick setup instructions
- `PROJECT_STRUCTURE.md` - Detailed project structure
- `NBA_API_RESOURCES.md` - NBA API integration guide
- `GETTING_STARTED.md` - This file

---

## 🎓 Interview Tips

When presenting this project:

1. **Explain the Architecture:**
   - React frontend communicates with Django backend via REST API
   - CORS configured for cross-origin requests
   - SQLite for development, can scale to PostgreSQL

2. **Highlight Key Features:**
   - User authentication
   - Favorite players/games functionality
   - External API integration
   - Responsive design

3. **Discuss Scalability:**
   - Can migrate to PostgreSQL for production
   - API caching strategy for external NBA data
   - Frontend can be deployed to Vercel/Netlify
   - Backend can be deployed to Heroku/Railway

4. **Show Problem-Solving:**
   - Rate limiting for external APIs
   - Error handling and user feedback
   - Database design for relationships
   - Authentication and authorization

---

## ✨ You're Ready!

Everything is set up and ready to go. Start both servers and begin building your NBA event tracker!

**Happy Coding! 🏀**

---

Need help? Check the documentation files or refer to:
- Django docs: https://docs.djangoproject.com/
- React docs: https://react.dev/
- DRF docs: https://www.django-rest-framework.org/

