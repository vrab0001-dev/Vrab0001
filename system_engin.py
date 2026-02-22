import os
import re
import requests
from datetime import datetime

# --- SYSTEM CONFIGURATION ---
USERNAME = "vrab0001-dev" 
RAID_REPO = "data-engineering-raids"

def check_github_activity():
    """Checks the Raid Dungeon for today's commits."""
    url = f"https://api.github.com/repos/{USERNAME}/{RAID_REPO}/commits"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return False
        
        commits = response.json()
        for commit in commits:
            date_str = commit['commit']['author']['date']
            # Format: 2026-02-22T14:43:00Z
            dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
            if dt == datetime.today().date():
                return True
    except Exception as e:
        print(f"System Error: {e}")
        return False
    return False

def update_status_window(is_active):
    """Replaces the stats in the README without duplicating text."""
    try:
        with open("README.md", "r") as f:
            content = f.read()

        # Progression Logic
        level = 3 # Base Level
        status = "ACTIVE 🟢" if is_active else "IDLE 🔴"
        rank = "E-Rank Hunter"
        sync_time = datetime.now().strftime('%Y-%m-%d %H:%M')

        new_stats_block = (
            f"**Current Status:** {status}\n"
            f"- **Level:** {level}\n"
            f"- **Rank:** {rank}\n"
            f"- **Last Sync:** {sync_time}"
        )

        # THE FIX: This regex finds EVERYTHING between the two markers and swaps it.
        # The 're.DOTALL' ensures it doesn't get stuck on new lines.
        marker_pattern = r".*?"
        replacement = f"\n{new_stats_block}\n"
        
        if re.search(marker_pattern, content, re.DOTALL):
            updated_content = re.sub(marker_pattern, replacement, content, flags=re.DOTALL)
            
            with open("README.md", "w") as f:
                f.write(updated_content)
            print("System: Status Window Updated successfully.")
        else:
            print("System Error: Could not find markers in README.md")

    except FileNotFoundError:
        print("System Error: README.md not found.")

if __name__ == "__main__":
    activity_detected = check_github_activity()
    update_status_window(activity_detected)