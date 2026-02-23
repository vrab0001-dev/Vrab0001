import os
import re
import json
import requests
from datetime import datetime, timezone

# --- SYSTEM CONFIGURATION ---
USERNAME = "vrab0001-dev"
RAID_REPO = "data-engineering-raids"
STATS_START = "<!-- VRAB_SYSTEM_STATS_START -->"
STATS_END = "<!-- VRAB_SYSTEM_STATS_END -->"
STATE_FILE = "system_state.json"

# --- LEVEL PROGRESSION ---
LEVELS = [
    {"level": 1,  "title": "Data Cadet",              "xp": 0},
    {"level": 2,  "title": "Junior Analyst",           "xp": 10},
    {"level": 3,  "title": "Data Analyst",             "xp": 25},
    {"level": 4,  "title": "Senior Analyst",           "xp": 50},
    {"level": 5,  "title": "Data Engineer",            "xp": 85},
    {"level": 6,  "title": "Senior Data Engineer",     "xp": 130},
    {"level": 7,  "title": "Data Architect",           "xp": 190},
    {"level": 8,  "title": "Principal Data Engineer",  "xp": 270},
    {"level": 9,  "title": "Data Lead",                "xp": 370},
    {"level": 10, "title": "Chief Data Officer",       "xp": 500},
]

# --- SKILL MAPPING ---
SKILL_MAP = {
    ".sql":  {"name": "SQL",              "xp": 3},
    ".py":   {"name": "Python",           "xp": 3},
    ".sh":   {"name": "Shell Scripting",  "xp": 2},
    ".json": {"name": "JSON & APIs",      "xp": 1},
    ".yml":  {"name": "Automation",       "xp": 2},
    ".yaml": {"name": "Automation",       "xp": 2},
    ".csv":  {"name": "Data Cleaning",    "xp": 1},
    ".ipynb":{"name": "Data Analysis",    "xp": 3},
    ".md":   {"name": "Documentation",    "xp": 1},
}

DAILY_COMPLETION_BONUS = 2  # XP bonus for completing 3+ file types in a day


def load_state():
    """Load persistent state from JSON file."""
    default = {
        "xp": 6,  # Starting XP from SQL raid
        "skills": {
            "SQL": {"level": 1, "xp_contributed": 3},
            "Data Cleaning": {"level": 1, "xp_contributed": 1},
            "Data Modelling": {"level": 1, "xp_contributed": 1},
        },
        "quests_completed": ["SQL Raid: Restructure Indian Govt CPI Data"],
        "last_sync": "N/A",
        "last_xp_date": None,  # Tracks the last date XP was awarded
    }
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return default


def save_state(state):
    """Save state to JSON file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def get_level_info(xp):
    """Return current level dict and next level dict."""
    current = LEVELS[0]
    for lvl in LEVELS:
        if xp >= lvl["xp"]:
            current = lvl
        else:
            break
    next_lvl = None
    idx = LEVELS.index(current)
    if idx + 1 < len(LEVELS):
        next_lvl = LEVELS[idx + 1]
    return current, next_lvl


def build_xp_bar(xp, current_level, next_level, width=20):
    """Build an ASCII XP progress bar."""
    if next_level is None:
        return "█" * width + " MAX"
    lvl_xp = xp - current_level["xp"]
    needed = next_level["xp"] - current_level["xp"]
    filled = int((lvl_xp / needed) * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"{bar} {lvl_xp}/{needed} XP"


def get_headers():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}


def get_todays_commits():
    """Fetch today's commits from the raid repo and return list of files changed."""
    url = f"https://api.github.com/repos/{USERNAME}/{RAID_REPO}/commits"
    today = datetime.now(timezone.utc).date()
    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        if response.status_code == 403:
            print("Warning: GitHub API rate limit. Set GITHUB_TOKEN env var.")
            return [], False
        if response.status_code != 200:
            print(f"Error: GitHub API returned {response.status_code}")
            return [], False

        commits = response.json()
        todays_commits = []
        for commit in commits:
            date_str = commit["commit"]["author"]["date"]
            dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
            if dt == today:
                todays_commits.append(commit["sha"])

        if not todays_commits:
            return [], False

        # Get files changed in today's commits
        files_changed = set()
        for sha in todays_commits:
            r = requests.get(
                f"https://api.github.com/repos/{USERNAME}/{RAID_REPO}/commits/{sha}",
                headers=get_headers(), timeout=10
            )
            if r.status_code == 200:
                for f in r.json().get("files", []):
                    files_changed.add(f["filename"])

        return list(files_changed), True

    except Exception as e:
        print(f"Error fetching commits: {e}")
        return [], False


def process_files(files, state):
    """Detect file types, award XP, unlock skills."""
    extensions_seen = set()
    xp_gained = 0
    new_skills = []

    for filepath in files:
        ext = os.path.splitext(filepath)[1].lower()
        if ext in SKILL_MAP and ext not in extensions_seen:
            extensions_seen.add(ext)
            skill_info = SKILL_MAP[ext]
            skill_name = skill_info["name"]
            xp = skill_info["xp"]
            xp_gained += xp

            if skill_name not in state["skills"]:
                state["skills"][skill_name] = {"level": 1, "xp_contributed": 0}
                new_skills.append(skill_name)

            state["skills"][skill_name]["xp_contributed"] += xp

    # Bonus XP for completing 3+ different file types
    if len(extensions_seen) >= 3:
        xp_gained += DAILY_COMPLETION_BONUS
        print(f"🎉 Daily completion bonus! +{DAILY_COMPLETION_BONUS} XP")

    return xp_gained, new_skills


def build_skills_block(skills):
    """Build the skills section for README."""
    skill_icons = {
        "SQL": "🗄️",
        "Python": "🐍",
        "Shell Scripting": "⚙️",
        "JSON & APIs": "🔌",
        "Automation": "🤖",
        "Data Cleaning": "🧹",
        "Data Analysis": "📊",
        "Data Modelling": "🏗️",
        "Documentation": "📝",
    }
    lines = []
    for skill, info in skills.items():
        icon = skill_icons.get(skill, "⚡")
        lines.append(f"- {icon} **{skill}**")
    return "\n".join(lines) if lines else "- No skills unlocked yet"


def update_readme(state, is_active, xp_gained, new_skills):
    """Write the updated stats block into README.md."""
    try:
        with open("README.md", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found.")
        return

    if STATS_START not in content or STATS_END not in content:
        print("Error: Markers not found in README.md.")
        return

    xp = state["xp"]
    current_level, next_level = get_level_info(xp)
    xp_bar = build_xp_bar(xp, current_level, next_level)
    skills_block = build_skills_block(state["skills"])
    status = "ACTIVE 🟢" if is_active else "IDLE 🔴"
    sync_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    gained_str = f"+{xp_gained} XP today" if xp_gained > 0 else ""
    new_skill_str = ""
    if new_skills:
        new_skill_str = f"\n- 🆕 **New Skills Unlocked:** {', '.join(new_skills)}"

    new_stats = f"""**Status:** {status}

| Stat | Value |
|------|-------|
| 🎖️ Title | {current_level['title']} |
| ⚡ Level | {current_level['level']} |
| 💠 Total XP | {xp} {gained_str} |
| 📅 Last Sync | {sync_time} |

**XP Progress:** `{xp_bar}`

### 🛠️ SKILLS UNLOCKED
{skills_block}{new_skill_str}"""

    pattern = rf"{re.escape(STATS_START)}.*?{re.escape(STATS_END)}"
    replacement = f"{STATS_START}\n{new_stats}\n{STATS_END}"
    updated = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if updated != content:
        with open("README.md", "w") as f:
            f.write(updated)
        print("System: README synchronized.")
    else:
        print("No changes needed.")

    state["last_sync"] = sync_time
    save_state(state)


if __name__ == "__main__":
    print("[ SYSTEM ENGINE STARTING ]")
    state = load_state()

    files, is_active = get_todays_commits()
    print(f"Files changed today: {files}")

    xp_gained = 0
    new_skills = []
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    xp_already_awarded_today = state.get("last_xp_date") == today_str

    if files:
        if xp_already_awarded_today:
            print("XP already awarded today — skipping XP gain. Status and skills still updated.")
            # Still track new skills even if no XP
            _, new_skills = process_files(files, state)
        else:
            xp_gained, new_skills = process_files(files, state)
            state["xp"] += xp_gained
            state["last_xp_date"] = today_str
            print(f"XP gained: {xp_gained} | Total XP: {state['xp']}")
            if new_skills:
                print(f"New skills: {new_skills}")

    current, next_lvl = get_level_info(state["xp"])
    print(f"Level: {current['level']} - {current['title']}")

    update_readme(state, is_active, xp_gained, new_skills)
    print("[ SYSTEM ENGINE DONE ]")
