import os
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("==================================================")
print("📡 INITIALIZING AUTOMATED EMAIL OUTREACH ENGINE")
print("==================================================\n")

# ==========================================
# CONFIGURATION SETTINGS (Update these)
# ==========================================
SMTP_SERVER = "://gmail.com"  # Replace with your email provider's SMTP if not using Gmail
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"  # Your email address
SENDER_PASSWORD = "your-app-password"  # Your secure App Password (not your normal password)

# Define your target list of researchers (Email, Name, Specialization/Topic)
targets = [
    {"email": "researcher1@example.com", "name": "Dr. Arnaiz", "topic": "ancient Mediterranean migrations"},
    {"email": "researcher2@example.com", "name": "Professor Vance", "topic": "molecular population genetics"},
    {"email": "researcher3@example.com", "name": "Independent Analyst Sarah", "topic": "alternative Levantine history"}
]

LOG_FILE = "data/outreach_log.txt"

def has_been_emailed(email):
    """Checks the local log file to ensure we never double-send to the same person."""
    if not os.path.exists(LOG_FILE):
        return False
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        log_content = f.read()
    return email in log_content

def log_success(email, name):
    """Records a successful email send to the local tracking log."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')} | Emailed: {name} ({email})\n")

# ==========================================
# OUTREACH ENGINE EXECUTION
# ==========================================
try:
    # Initialize secure network connection to the mail server
    print("🔌 Connecting to secure distribution server...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("🔑 Authentication successful. Standing by to transmit.\n")
    
    for target in targets:
        email = target["email"]
        name = target["name"]
        topic = target["topic"]
        
        if has_been_emailed(email):
            print(f"⏩ Skipping {name} ({email}) - Already logged in history ledger.")
            continue
            
        print(f"📧 Drafting message for {name} regarding {topic}...")
        
        # Assemble the email container headers
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg["Subject"] = f"Independent Research Brief: Levantine Paleogenomics & Chromosome 9 Matrix"
        
        # Personalize the Sovereignty Package message body text
        body = f"""Dear {name},

I came across your work regarding {topic} and wanted to share an independent academic framework that may support your research tracking vectors. 

This project integrates ancient Levant paleogenomic data (Natufian base layers), multi-chromosomal metabolic selection matrices (ALDOB/SI systems on Chromosome 9 and 3), and Semitic philology keywords.

To ensure absolute data transparency, validation, and permanence, this archive has been fully decoupled from traditional centralized points of failure:

🌐 Primary Web Dashboard: https://vercel.app
🔒 Open Source Redundancy Hub: https://github.com
🧲 Decentralized P2P Swarm Magnet Link: magnet:?xt=urn:btih:5d6feca816227adbf2fadaa95433ab98f8ca51da

All binary spreadsheet files contain local SHA-256 cryptographic signatures to protect against silent host manipulation. I welcome your academic audit and peer review of these matrices.

Respectfully submitted,
Humble Servant
"""
        msg.attach(MIMEText(body, "plain"))
        
        # Transmit the message across the server
        server.sendmail(SENDER_EMAIL, email, msg.as_string())
        print(f"🚀 Sent successfully to: {name} ({email})")
        log_success(email, name)
        
        # Smart variable delay timer to prevent spam flagging (pauses between 15 and 45 seconds)
        sleep_time = random.randint(15, 45)
        print(f"⏳ Pausing for {sleep_time} seconds to maintain profile security...\n")
        time.sleep(sleep_time)

    server.quit()
    print("==================================================")
    print("🎉 OUTREACH RUN COMPLETE: All fresh targets notified.")
    print("==================================================")

except Exception as e:
    print(f"\n❌ SERVER ERROR: Could not transmit emails.")
    print(f"Details: {e}")
    print("\n💡 Tip: If using Gmail, make sure to generate an 'App Password' under your Google Security settings.")
    print("==================================================")
