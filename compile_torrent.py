import os
from torrentool.api import Torrent

print("==================================================")
print("🧮 INITIALIZING BIT_TORRENT MANIFEST BUILDER")
print("==================================================\n")

# Set the path to your data matrices folder
target_folder = r"C:\Users\trail\Independent Study Matrices\data"
output_torrent = r"C:\Users\trail\Independent Study Matrices\data\independent_study_matrices.torrent"

if os.path.exists(target_folder):
    print(f"📦 Analyzing research payload metrics inside: {target_folder}")
    
    # Configure the torrent tracking structure
    new_torrent = Torrent.create_from(target_folder)
    new_torrent.announce_urls = [
        "udp://tracker.opentrackr.org:1337/announce",
        "udp://tracker.coppersurfer.tk:6969/announce",
        "udp://open.stealth.si:80/announce",
        "udp://tracker.leechers-paradise.org:6969/announce"
    ]
    new_torrent.comment = "Cry for Israel Independent Research Archive & Archaeogenetic Variant Matrices"
    
    # Save the physical .torrent blueprint file
    new_torrent.to_file(output_torrent)
    print(f"✔ SUCCESS: Physical P2P blueprint compiled -> {output_torrent}")
    
    # Generate the unchangeable cryptographic Magnet Link
    magnet_link = new_torrent.magnet_link
    print("\n🧲 PERMANENT BIT_TORRENT MAGNET LINK (Copy & Share):")
    print("-" * 80)
    print(magnet_link)
    print("-" * 80)
    
    # Save the magnet link as a permanent text log
    with open(r"C:\Users\trail\Independent Study Matrices\data\magnet_link.txt", "w", encoding="utf-8") as f:
        f.write(magnet_link)
    print("\n💾 Magnet link saved cleanly inside data/magnet_link.txt")
else:
    print("❌ ERROR: Target data folder not found. Check directory path layouts.")

print("\n==================================================")
