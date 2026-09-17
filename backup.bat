@echo off
cls
echo ==================================================
echo 📦 AUTOMATED COLD STORAGE BACKUP ENGINE
echo ==================================================
echo.

:: Generate an accurate system date and time stamp for the archive name
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do set mydate=%%c-%%a-%%b
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set mytime=%%a%%b

set BACKUP_DIR=backups
set ARCHIVE_NAME=%BACKUP_DIR%\independent_study_backup_%mydate%_%mytime%.zip

if not exist %BACKUP_DIR% mkdir %BACKUP_DIR%

echo [1/2] Bundling critical research directories and tracking files...
powershell -Command "Compress-Archive -Path 'data', 'dist', 'website', 'generate_matrices.py', 'deploy.bat', 'verify.bat' -DestinationPath '%ARCHIVE_NAME%' -Force"

if %errorlevel% equ 0 (
    echo.
    echo ==================================================
    echo ✅ BACKUP SUCCESS: Workspace archived securely.
    echo Target Path: %ARCHIVE_NAME%
    echo ==================================================
) else (
    echo.
    echo ==================================================
    echo ❌ ERROR: Automated compression pipeline failed!
    echo ==================================================
)

pause
