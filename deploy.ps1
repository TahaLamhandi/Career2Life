# Career2Life - Deployment Script
# This script helps you quickly deploy your changes to Vercel and Render

Write-Host "🚀 Career2Life Deployment Helper" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (-not (Test-Path .git)) {
    Write-Host "❌ Git repository not found!" -ForegroundColor Red
    Write-Host "Run: git init" -ForegroundColor Yellow
    exit 1
}

# Check git status
Write-Host "📊 Checking git status..." -ForegroundColor Yellow
git status

Write-Host ""
Write-Host "📝 Do you want to commit and push your changes? (Y/N)" -ForegroundColor Green
$response = Read-Host

if ($response -eq 'Y' -or $response -eq 'y') {
    Write-Host ""
    Write-Host "💬 Enter commit message:" -ForegroundColor Green
    $message = Read-Host
    
    if ([string]::IsNullOrWhiteSpace($message)) {
        $message = "Update deployment configurations"
    }
    
    Write-Host ""
    Write-Host "📦 Adding files to git..." -ForegroundColor Yellow
    git add .
    
    Write-Host "💾 Committing changes..." -ForegroundColor Yellow
    git commit -m $message
    
    Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Yellow
    git push
    
    Write-Host ""
    Write-Host "✅ Changes pushed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🌐 Your deployments will automatically update:" -ForegroundColor Cyan
    Write-Host "   - Vercel: https://vercel.com/dashboard" -ForegroundColor White
    Write-Host "   - Render: https://dashboard.render.com" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ℹ️  Deployment cancelled. Run this script again when ready." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📚 For detailed deployment instructions, see DEPLOYMENT_GUIDE.md" -ForegroundColor Cyan
