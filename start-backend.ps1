# HoopWatch Backend Startup Script
Write-Host "🏀 Starting HoopWatch Backend..." -ForegroundColor Green

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Check if migrations are needed
Write-Host "Checking database..." -ForegroundColor Yellow
python manage.py migrate --check 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Running migrations..." -ForegroundColor Yellow
    python manage.py migrate
}

# Start server
Write-Host "Starting Django development server..." -ForegroundColor Green
Write-Host "Backend will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Admin panel: http://localhost:8000/admin" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python manage.py runserver

