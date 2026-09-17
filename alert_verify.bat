@echo off
cd /d "C:\Users\trail\Independent Study Matrices"

:: Run the verification engine in the background and capture the result
call verify.bat >nul 2>&1
set EXIT_CODE=%errorlevel%

:: Trigger native Windows pop-up alert dialog boxes using a fast PowerShell call
if %EXIT_CODE% equ 0 (
    powershell -Command "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; [System.Windows.Forms.MessageBox]::Show('✔ INTEGRITY VERIFIED: All local research matrices match their cryptographic hashes. Your workspace is 100% secure.', 'Cryptographic Audit Success', [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)"
) else (
    powershell -Command "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; [System.Windows.Forms.MessageBox]::Show('🚨 SECURITY ALERT: Matrix verification failed! One or more spreadsheets have been tampered with or corrupted.', 'Data Integrity Violation', [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)"
)
