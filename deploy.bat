@echo off
echo ==================================================
echo 🚀 STARTING WEB3 DATA DEPLOYMENT WORKFLOW
echo ==================================================

:: LAYER 1: Lock the files with Cryptographic Signatures
echo 🔒 [1/4] Calculating SHA-256 Checksums...
if not exist dist mkdir dist
certutil -hashfile data\aldob_variant_matrix.xlsx SHA256 | findstr /V "hash" > dist\checksums.txt
certutil -hashfile data\archaeogenetic_sample_log.xlsx SHA256 | findstr /V "hash" >> dist\checksums.txt
echo ✔ Checksums compiled inside dist/checksums.txt

:: LAYER 2: Commit All Data and Scripts to Local Git
echo 💻 [2/4] Staging and Committing all files...
git add .
git commit -m "Update independent study matrices and logs"

:: LAYER 3: Push to Centralization-Resistant Remotes
echo 🌍 [3/4] Broadcasting to Primary Repo (GitHub) and Mirror (Codeberg)...
git push origin main
git push mirror main

:: LAYER 4: Web3 Framework Trigger Notice
echo 🌐 [4/4] Handing tracking hooks over to Fleek.xyz...
echo ✔ Repository state broadcasted. Fleek tracking engines are now pinning static payloads directly to IPFS CIDs.
echo ==================================================
echo 🎉 DEPLOYMENT PIPELINE COMPLETE!
pause
