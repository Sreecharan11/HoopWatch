# 🚀 Quick Setup Guide for HoopWatch

## First Time Setup

### 1. Backend Setup (5 minutes)

Open a terminal in the project root:

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Verify Django is installed
python -m django --version

# Run migrations to set up database
python manage.py migrate

# Create admin user (follow prompts)
python manage.py createsuperuser

# Start backend server
python manage.py runserver
```

✅ Backend should be running at `http://localhost:8000`

### 2. Frontend Setup (3 minutes)

Open a **new terminal** in the project root:

```powershell
# Navigate to frontend
cd frontend

# Verify dependencies are installed
npm list --depth=0

# Start frontend server
npm run dev
```

✅ Frontend should be running at `http://localhost:5173`

## Daily Development Workflow

### Starting the Application

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

### Stopping the Application

Press `Ctrl+C` in each terminal window.

## Verification Checklist

- [ ] Backend running at `http://localhost:8000`
- [ ] Frontend running at `http://localhost:5173`
- [ ] Can access Django admin at `http://localhost:8000/admin`
- [ ] Frontend displays HoopWatch welcome page
- [ ] No CORS errors in browser console

## Common Issues & Solutions

### Issue: "python not found"
**Solution:** Make sure Python is installed and in your PATH

### Issue: "npm not found"
**Solution:** Install Node.js from nodejs.org

### Issue: Virtual environment activation fails
**Solution:** 
- Windows: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then try activating again

### Issue: Port already in use
**Solution:**
- Backend: Use `python manage.py runserver 8001` (different port)
- Frontend: Vite will automatically suggest another port

### Issue: CORS errors
**Solution:** 
- Make sure both servers are running
- Check `backend/settings.py` has correct CORS origins
- Clear browser cache

## Next Development Steps

1. **Create Django Apps:**
   ```bash
   python manage.py startapp players
   python manage.py startapp games
   python manage.py startapp events
   ```

2. **Add apps to `INSTALLED_APPS` in `backend/settings.py`**

3. **Create models, serializers, and views**

4. **Build React components in `frontend/src/`**

## Useful Commands

### Backend
```bash
# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Open Django shell
python manage.py shell
```

### Frontend
```bash
# Install new package
npm install package-name

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project URLs

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000/api
- **Django Admin:** http://localhost:8000/admin
- **Django REST API Browser:** http://localhost:8000/api (when endpoints are created)

---

Happy coding! 🏀

