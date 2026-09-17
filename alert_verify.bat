@echo off
cd /d "C:\Users\trail\Independent Study Matrices"

:: Run the verification engine in the background and capture the result
call verify.bat >nul 2>&1
set EXIT_CODE=%errorlevel%

:: Trigger native Windows pop-up alert dialog boxes using WScript Shell via PowerShell
if %EXIT_CODE% equ 0 (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $ws.Popup('✔ INTEGRITY VERIFIED: All local research matrices match their cryptographic hashes. Your workspace is 100% secure.', 0, 'Cryptographic Audit Success', 64)" >nul
) else (
    powershell -Command "$ws = New-Object -ComObject WScript.Shell; $ws.Popup('🚨 SECURITY ALERT: Matrix verification failed! One or more spreadsheets have been tampered with or corrupted.', 0, 'Data Integrity Violation', 16)" >nul
)
