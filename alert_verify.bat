@echo off
:: Force the script to jump to your absolute project directory immediately
cd /d "C:\Users\trail\Independent Study Matrices"

:: Run the verification engine natively and wait for the exit status code
powershell -Command "$good = $true; Get-Content dist/checksums.txt | ForEach-Object { if ($_ -match 'SHA-256 for (.+?): (.+)') { $file=$Matches.Groups[1].Value.Trim(); $expected=$Matches.Groups[2].Value.Trim().ToLower(); if (Test-Path $file) { $actual = (Get-FileHash $file -Algorithm SHA256).Hash.ToLower(); if ($actual -ne $expected) { $good = $false } } else { $good = $false } } }; if (-not $good) { exit 1 }"
set EXIT_CODE=%errorlevel%

:: Fire native Windows popup dialog cards based on the exit return code
if %EXIT_CODE% equ 0 (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $ws.Popup('✔ INTEGRITY VERIFIED: All local research matrices match their cryptographic hashes. Your workspace is 100% secure.', 0, 'Cryptographic Audit Success', 64)" >nul
) else (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $ws.Popup('🚨 SECURITY ALERT: Matrix verification failed! One or more spreadsheets have been tampered with or corrupted.', 0, 'Data Integrity Violation', 16)" >nul
)
