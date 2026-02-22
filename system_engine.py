import os
import re
import argparse
import requests
from datetime import datetime

# --- SYSTEM CONFIGURATION ---
USERNAME = "vrab0001-dev" 
RAID_REPO = "data-engineering-raids"
STATS_START = "<!-- STATS_START -->"
STATS_END = "<!-- STATS_END -->"


def init_readme(dry_run=False):
    try:
        with open("README.md", "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    if STATS_START in content and STATS_END in content:
        print("Info: README.md already contains stat markers.")
        return

    placeholder = (
        f"{STATS_START}\n"
        "**Current Status:** UNKNOWN\n"
        "- **Level:** 3\n"
        "- **Rank:** E-Rank Hunter\n"
        "- **Last Sync:** N/A\n"
        f"{STATS_END}\n"
    )

    # Insert after the first heading if present, else append at end
    if content:
        lines = content.splitlines()
        insert_at = None
        for i, line in enumerate(lines):
            if line.strip().startswith("#"):
                insert_at = i + 1
                break
        if insert_at is None:
            new_content = content + "\n\n" + placeholder
        else:
            lines.insert(insert_at, placeholder)
            new_content = "\n".join(lines)
    else:
        new_content = placeholder

    if dry_run:
        print("Dry-run: would insert the following into README.md:\n")
        print(placeholder)
        return

    with open("README.md", "w") as f:
        f.write(new_content)
    print("Inserted stat markers into README.md")

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

def update_readme(is_active, dry_run=False):
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
        # Replace only the block between explicit markers to avoid rewriting
        # the whole file (which can trigger watchers and cause infinite loops).
        if STATS_START in content and STATS_END in content:
            pattern = rf"{re.escape(STATS_START)}.*?{re.escape(STATS_END)}"
            replacement = f"{STATS_START}\n{new_stats}\n{STATS_END}"
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

            # Only write if content would change (prevents unnecessary file touch)
            if updated_content != content:
                if dry_run:
                    print("Dry-run: updated README preview:\n")
                    print(updated_content)
                    return
                with open("README.md", "w") as f:
                    f.write(updated_content)
                print("System: Stats synchronized.")
            else:
                print("No changes needed; README.md already up-to-date.")
        else:
            print("Error: Markers not found in README.md. Please add the markers:", STATS_START, STATS_END)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update project README status block")
    parser.add_argument("--init", action="store_true", help="Insert stat markers into README.md")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing files")
    args = parser.parse_args()

    if args.init:
        init_readme(dry_run=args.dry_run)
    else:
        update_readme(check_activity(), dry_run=args.dry_run)