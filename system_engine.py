import os
import re
import requests
from datetime import datetime

# --- SYSTEM CONFIGURATION ---
USERNAME = "vrab0001-dev" 
RAID_REPO = "data-engineering-raids"

def check_activity():
    url = f"https://api.github.com/repos/{USERNAME}/{RAID_REPO}/commits"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200: return False
        commits = response.json()
        for commit in commits:
            date_str = commit['commit']['author']['date']
            dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
            if dt == datetime.today().date():
                return True
    except:
        return False
    return False

def update_readme(is_active):
    try:
        with open("README.md", "r") as f:
            content = f.read()

        status = "ACTIVE 🟢" if is_active else "IDLE 🔴"
        sync_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        # This is the EXACT block that will be injected
        new_stats = (
            f"**Current Status:** {status}\n"
            f"- **Level:** 3\n"
            f"- **Rank:** E-Rank Hunter\n"
            f"- **Last Sync:** {sync_time}"
        )

        # FIX: The regex now looks for everything between the tags (including newlines)
        # and swaps it for the clean block.
        pattern = r".*?"
        replacement = f"\n{new_stats}\n"
        
        # Only write if we actually find the markers to avoid corruption
        if "" in content:
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            with open("README.md", "w") as f:
                f.write(updated_content)
            print("System: Stats synchronized.")
        else:
            print("Error: Markers not found!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme(check_activity())