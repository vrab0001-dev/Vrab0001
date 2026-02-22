import os
import re
import requests
from datetime import datetime

# --- CONFIGURATION ---
# Replace with your actual GitHub username
USERNAME = "Vrab0001" 
RAID_REPO = "data-engineering-raids"

def check_github_activity():
    """Checks the GitHub API to see if you pushed code to the Raid Repo today."""
    url = f"https://api.github.com/repos/{USERNAME}/{RAID_REPO}/commits"
    response = requests.get(url)
    if response.status_code != 200:
        return False
    
    commits = response.json()
    for commit in commits:
        commit_date = commit['commit']['author']['date']
        dt = datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ").date()
        if dt == datetime.today().date():
            return True
    return False

def calculate_level(commit_count):
    """Simple progression logic: Level = Total Commits / 5 (minimum Level 1)"""
    level = 1 + (commit_count // 5)
    return level

def update_readme(level, active_today):
    """Overwrites the stats in your README based on activity."""
    with open("README.md", "r") as f:
        content = f.read()

    status = "ACTIVE 🟢" if active_today else "IDLE 🔴"
    rank = "E-Rank Hunter"
    if level > 10: rank = "D-Rank Hunter"
    if level > 25: rank = "C-Rank Hunter"

    new_stats = (
        f"**Current Status:** {status}\n"
        f"- **Level:** {level}\n"
        f"- **Rank:** {rank}\n"
        f"- **Last Sync:** {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )

    # Injects the stats between these markers in your README
    pattern = r".*?"
    replacement = f"\n{new_stats}\n"
    
    if "" in content:
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open("README.md", "w") as f:
            f.write(updated_content)
        return True
    return False

if __name__ == "__main__":
    activity = check_github_activity()
    # In a real scenario, we'd fetch total commit count from API
    # For now, let's assume we pull the count from the repo stats
    level = calculate_level(10) # Placeholder: you can expand this logic
    update_readme(level, activity)
    print("System: Stats Synchronized.")