# start_chrome_debug.ps1
# Closes Chrome and reopens it with remote debugging on port 9222
# Run this from PowerShell (as normal user, no admin needed)

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$debugPort = 9222

Write-Host "Closing all Chrome windows..." -ForegroundColor Yellow
Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 2

Write-Host "Starting Chrome with remote debugging on port $debugPort..." -ForegroundColor Green
Start-Process $chromePath -ArgumentList `
    "--remote-debugging-port=$debugPort",
    "--profile-directory=Default",
    "--no-first-run"

Start-Sleep -Seconds 3
Write-Host "Chrome started. You can now run: node keyword_planner.js `"your keyword`"" -ForegroundColor Cyan
Write-Host "Port $debugPort is ready for automation." -ForegroundColor Cyan
