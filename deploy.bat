@echo off
cls
echo ==================================================
echo 🚀 INITIATING GATED DATA DEPLOYMENT PIPELINE
echo ==================================================
echo.

:: STEP 1: Pre-Flight Cryptographic Integrity Audit
echo 🛡️ [1/5] Executing Pre-Flight Security Check...
call verify.bat
if %errorlevel% neq 0 (
    echo.
    echo ❌ ERROR: Deployment halted. Data verification check failed!
    echo Resolve local integrity errors before broadcasting changes.
    echo.
    pause
    exit /b
)
echo.

:: STEP 2: Re-Calculate SHA-256 Signatures for New Builds
echo 🔒 [2/5] Calculating Fresh SHA-256 Checksums...
if not exist dist mkdir dist
certutil -hashfile data\aldob_variant_matrix.xlsx SHA256 | findstr /V "hash" > dist\checksums.txt
certutil -hashfile data\archaeogenetic_sample_log.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
certutil -hashfile data\philological_keyword_index.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
certutil -hashfile data\secondary_variant_matrix.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
echo ✔ Checksums compiled inside dist\checksums.txt
echo.

:: STEP 3: Commit Workspace Tree States to Local Git
echo 💻 [3/5] Staging and Committing all project files...
git add .
git commit -m "Update independent study matrices, tracking configs, and web pages"
echo.

:: STEP 4: Dual Push to Redundant Repositories
echo 🌍 [4/5] Broadcasting to Primary Repo (GitHub) and Mirror (Codeberg)...
git push origin main
git push mirror main
echo.

:: STEP 5: Web Platform Compilation Hook Notice
echo 🌐 [5/5] Sync complete. Static servers are updating live parameters.
echo ==================================================
echo 🎉 DEPLOYMENT PIPELINE COMPLETE!
echo ==================================================
pause
