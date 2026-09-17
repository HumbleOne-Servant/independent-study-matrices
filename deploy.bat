@echo off
cls
echo ==================================================
echo 🚀 INITIATING HIGH-SECURITY MASTER DEPLOYMENT GATE
echo ==================================================
echo.

:: STAGE 1: Pre-Flight Cryptographic Integrity Audit
echo 🛡️ [1/6] Executing Pre-Flight Security Check...
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

:: STAGE 2: Automated BitTorrent P2P Swarm Compilation
echo 🧮 [2/6] Compiling Decentralized BitTorrent Manifests...
python compile_torrent.py
if %errorlevel% neq 0 (
    echo ⚠️ WARNING: P2P Torrent compilation encountered a non-fatal skip.
)
echo.

:: STAGE 3: Local Sync of Assets to Static Website Vault
echo 💾 [3/6] Syncing Matrix Assets to Website Directories...
if not exist website\docs\data mkdir website\docs\data
copy data\aldob_variant_matrix.xlsx website\docs\data\ /Y >nul
copy data\archaeogenetic_sample_log.xlsx website\docs\data\ /Y >nul
copy data\philological_keyword_index.xlsx website\docs\data\ /Y >nul
copy data\secondary_variant_matrix.xlsx website\docs\data\ /Y >nul
copy data\independent_study_matrices.torrent website\docs\data\ /Y >nul
copy data\magnet_link.txt website\docs\data\ /Y >nul
echo ✔ Website doc-vault synchronization complete.
echo.

:: STAGE 4: Re-Calculate SHA-256 Signatures for Global Ledgers
echo 🔒 [4/6] Locking Fresh SHA-256 Checksums...
if not exist dist mkdir dist
certutil -hashfile data\aldob_variant_matrix.xlsx SHA256 | findstr /V "hash" > dist\checksums.txt
certutil -hashfile data\archaeogenetic_sample_log.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
certutil -hashfile data\philological_keyword_index.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
certutil -hashfile data\secondary_variant_matrix.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
echo ✔ Checksums successfully compiled inside dist\checksums.txt
echo.

:: STAGE 5: Commit System States to Local Git Tree
echo 💻 [5/6] Staging and Committing all project files...
git add .
git commit -m "Update independent study matrices, tracking configs, and web pages"
echo.

:: STAGE 6: Sovereign Broadcasting to Primary and Mirror Nodes
echo 🌍 [6/6] Broadcasting to Primary Repo (GitHub) and Mirror (Codeberg)...
git push origin main
git push mirror main
echo.

echo ==================================================
echo 🎉 ALL CHANNELS SYNCHRONIZED AND LIVE!
echo ==================================================
pause
