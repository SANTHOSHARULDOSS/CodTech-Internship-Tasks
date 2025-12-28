import hashlib
import time
import os

# --- CONFIGURATION ---
file_to_monitor = "secret.txt"  # The file we want to watch
check_interval = 2              # Check every 2 seconds

def calculate_hash(file_path):
    """Creates a 'fingerprint' (SHA-256 hash) of the file content."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read file in small chunks so it works even on large files
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

# --- MAIN PROGRAM ---
print(f"--- FILE INTEGRITY MONITOR STARTED ---")
print(f"Target: {file_to_monitor}")
print("Press Ctrl+C to stop.\n")

# 1. Get the starting 'fingerprint'
last_hash = calculate_hash(file_to_monitor)

if last_hash is None:
    print(f"ERROR: Could not find '{file_to_monitor}'!")
    print(f"Make sure the file is in the SAME folder as this script.")
else:
    print(f"Initial Hash: {last_hash}")
    print("Monitoring for changes...\n")

    # 2. Start the infinite loop to watch the file
    try:
        while True:
            time.sleep(check_interval) # Wait a bit before checking again
            
            current_hash = calculate_hash(file_to_monitor)
            
            if current_hash != last_hash:
                print("⚠️  ALERT: FILE CHANGED!")
                print(f"Old Hash: {last_hash}")
                print(f"New Hash: {current_hash}")
                print("-" * 30)
                
                # Update the last_hash so we don't keep alerting for the same change
                last_hash = current_hash
            else:
                # Optional: Print a dot to show it's working
                print(".", end="", flush=True)
                
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
