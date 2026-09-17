@echo off
cls
echo ==================================================
echo 🔒 CRYPTOGRAPHIC INTEGRITY AUDIT ENGINE
echo ==================================================
echo.
echo Checking local data assets against compiled signatures...
echo.

if not exist dist\checksums.txt (
    echo ❌ ERROR: Central checksum manifest ^(dist\checksums.txt^) is missing!
    echo Run deploy.bat first to establish a signature baseline.
    echo.
    pause
    exit /b
)

powershell -Command "$good = $true; Get-Content dist/checksums.txt | ForEach-Object { if ($_ -match 'SHA-256 for (.+?): (.+)') { $file=$Matches[1].Trim(); $expected=$Matches[2].Trim().ToLower(); if (Test-Path $file) { $actual = (Get-FileHash $file -Algorithm SHA256).Hash.ToLower(); if ($actual -eq $expected) { Write-Host """✔ VALID: $file integrity confirmed.""" -ForegroundColor Green } else { Write-Host """❌ COMPROMISED: $file signature mismatch!""" -ForegroundColor Red; $good = $false } } else { Write-Host """⚠️ MISSING: $file not found.""" -ForegroundColor Yellow; $good = $false } } }; if (-not $good) { exit 1 }"

echo.
echo ==================================================
echo Pipeline check complete. Workspace secure.
echo ==================================================
pause
