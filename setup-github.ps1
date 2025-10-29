# Setup GitHub Remote and Push
# Replace YOUR_USERNAME with your actual GitHub username

Write-Host "Setting up GitHub remote..." -ForegroundColor Green

# Add remote (replace YOUR_USERNAME with your GitHub username)
$username = Read-Host "Enter your GitHub username"
git remote add origin "https://github.com/$username/HoopWatch.git"

Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
git branch -M main
git push -u origin main

Write-Host "Done! Your code is now on GitHub." -ForegroundColor Green
Write-Host "Repository: https://github.com/$username/HoopWatch" -ForegroundColor Cyan

