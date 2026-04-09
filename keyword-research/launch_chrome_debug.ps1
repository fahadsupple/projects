# Launch Chrome with remote debugging (separate profile, won't affect existing Chrome)
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$sessionDir = "$env:LOCALAPPDATA\ChromeKPSession"
$port = 9223

Write-Host "Launching Chrome with remote debugging on port $port..." -ForegroundColor Cyan
Write-Host "Your existing Chrome windows are NOT affected." -ForegroundColor Green

& $chrome `
    "--remote-debugging-port=$port" `
    "--user-data-dir=$sessionDir" `
    "--no-first-run" `
    "--window-size=1400,900" `
    "about:blank"

Write-Host "Chrome launched." -ForegroundColor Green
