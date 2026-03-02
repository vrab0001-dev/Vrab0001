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
QUESTS_START = "<!-- VRAB_QUESTS_START -->"
QUESTS_END = "<!-- VRAB_QUESTS_END -->"
STATE_FILE = "system_state.json"

# --- LEVEL PROGRESSION ---
LEVELS = [
    {"level": 1, "title": "Data Cadet",            "xp": 0},
    {"level": 2, "title": "Junior Data Analyst",   "xp": 10},
    {"level": 3, "title": "Data Analyst",          "xp": 25},
    {"level": 4, "title": "SQL Developer",         "xp": 50},
    {"level": 5, "title": "Python Developer",      "xp": 85},
    {"level": 6, "title": "Junior Data Engineer",  "xp": 130},
    {"level": 7, "title": "Data Engineer",         "xp": 190},
    {"level": 8, "title": "Cloud Data Engineer",   "xp": 270},
]

# --- SKILL MAPPING ---
SKILL_MAP = {
    ".sql":  {"name": "SQL",             "xp": 3},
    ".py":   {"name": "Python",          "xp": 3},
    ".sh":   {"name": "Shell Scripting", "xp": 2},
    ".json": {"name": "JSON & APIs",     "xp": 1},
    ".yml":  {"name": "Automation",      "xp": 2},
    ".yaml": {"name": "Automation",      "xp": 2},
    ".csv":  {"name": "Data Cleaning",   "xp": 1},
    ".ipynb":{"name": "Data Analysis",   "xp": 3},
    ".md":   {"name": "Documentation",   "xp": 1},
}

DAILY_COMPLETION_BONUS = 2


# ─────────────────────────────────────────────
# STATE
# ─────────────────────────────────────────────

def load_state():
    default = {
        "xp": 6,
        "skills": {
            "SQL":           {"level": 1, "xp_contributed": 3},
            "Data Cleaning": {"level": 1, "xp_contributed": 1},
            "Data Modelling":{"level": 1, "xp_contributed": 1},
        },
        "quests_completed": ["SQL Raid: Restructure Indian Govt CPI Data"],
        "daily_quests": [],
        "last_quest_date": None,
        "last_xp_date": None,
        "last_sync": "N/A",
    }
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return default


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ─────────────────────────────────────────────
# LEVEL & XP
# ─────────────────────────────────────────────

def get_level_info(xp):
    current = LEVELS[0]
    for lvl in LEVELS:
        if xp >= lvl["xp"]:
            current = lvl
        else:
            break
    idx = LEVELS.index(current)
    next_lvl = LEVELS[idx + 1] if idx + 1 < len(LEVELS) else None
    return current, next_lvl


def build_xp_bar(xp, current_level, next_level, width=20):
    if next_level is None:
        return "█" * width + " MAX"
    lvl_xp = xp - current_level["xp"]
    needed = next_level["xp"] - current_level["xp"]
    filled = int((lvl_xp / needed) * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"{bar} {lvl_xp}/{needed} XP"


# ─────────────────────────────────────────────
# GITHUB
# ─────────────────────────────────────────────

def get_headers():
    token = os.environ.get("RAID_TOKEN")
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}


def get_todays_commits():
    url = f"https://api.github.com/repos/{USERNAME}/{RAID_REPO}/commits"
    today = datetime.now(timezone.utc).date()
    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        if response.status_code == 403:
            print("Warning: GitHub API rate limit. Set RAID_TOKEN env var.")
            return [], False
        if response.status_code != 200:
            print(f"Error: GitHub API returned {response.status_code}")
            return [], False

        commits = response.json()
        todays_shas = []
        for commit in commits:
            date_str = commit["commit"]["author"]["date"]
            dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").date()
            if dt == today:
                todays_shas.append(commit["sha"])

        if not todays_shas:
            return [], False

        files_changed = set()
        for sha in todays_shas:
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


# ─────────────────────────────────────────────
# QUEST GENERATION
# ─────────────────────────────────────────────

def generate_quests(level, title, skills):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Warning: ANTHROPIC_API_KEY not set. Skipping quest generation.")
        return None

    skill_list = ", ".join(skills.keys()) if skills else "none yet"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    prompt = f"""You are a data engineering mentor generating daily practice quests for a learner based in Australia.

Player profile:
- Level: {level} ({title})
- Skills unlocked: {skill_list}
- Date: {today}

Skill assessment results:
- SQL: Intermediate — knows JOINs, GROUP BY, HAVING, subqueries. Ready for window functions (ROW_NUMBER, RANK, LAG, LEAD), CTEs, complex analytical queries.
- Python: Beginner-Intermediate — knows lists, dicts, list comprehensions, basic pandas. Ready for data cleaning scripts, CSV automation, file I/O.

Generate exactly 3 daily quests. Rules:
1. Quest 1: A SQL challenge using window functions, CTEs, or complex aggregations.
2. Quest 2: A Python/pandas challenge involving data cleaning, transformation, or automation.
3. Quest 3: A combined data engineering task involving both Python and SQL.

DATASET RULES — this is critical:
- Prioritise real Australian open datasets from these sectors and sources:

  FINANCE: ASX 200 historical prices (Kaggle), RBA interest rate decisions (rba.gov.au), ASIC company filings (data.gov.au)
  TRANSPORT: NSW Road Crash Data (data.nsw.gov.au), BITRE aviation statistics (bitre.gov.au), Transport for NSW open data (opendata.transport.nsw.gov.au)
  ENVIRONMENT & CLIMATE: Australian Weather observations (Bureau of Meteorology / Kaggle by jsphyg), Australian Wildfire dataset (Kaggle), Great Barrier Reef monitoring data (aims.gov.au)
  HEALTH: AIHW health expenditure data (aihw.gov.au), COVID-19 Australia dataset (Kaggle), PBS prescription data (data.gov.au)
  AGRICULTURE: ABARES crop production data (agriculture.gov.au), Australian wine production statistics (wineaustralia.com), Livestock slaughter data (abs.gov.au)
  DEMOGRAPHICS & SOCIETY: ABS Census 2021 (abs.gov.au), Australian Electoral Commission results (aec.gov.au), ACNC charity data (acnc.gov.au)
  CRIME & JUSTICE: NSW Bureau of Crime Statistics (bocsar.nsw.gov.au), Victorian Crime Statistics (crimestatistics.vic.gov.au)
  ENERGY: AEMO electricity demand data (aemo.com.au), Australian energy statistics (energy.gov.au)
  SPORT: AFL match results (Kaggle / afltables.com), Australian Open Tennis results (Kaggle), Cricket Australia stats (Kaggle)
  TOURISM: Tourism Research Australia data (tra.gov.au), Melbourne pedestrian counting (Melbourne Open Data Portal)

- Rotate sectors daily so the player gets exposure to different industries over time.
- Only name datasets you are confident actually exist and are freely available. If unsure, use a well-known Kaggle dataset.
- Do NOT include any URLs. Just the dataset name and where to find it (site name only).

Tasks must be specific, actionable, and take 30-60 minutes. No trivial tasks.

Respond ONLY with a JSON array of exactly 3 objects. No preamble, no markdown fences, just raw JSON:
[
  {{
    "type": "SQL",
    "title": "Short quest title",
    "description": "Specific task description explaining exactly what to do and what the expected output is",
    "dataset": "Dataset name — where to find it (site name only, no URL)",
    "file_ext": ".sql"
  }}
]"""

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "system": "You are a data engineering mentor. Always respond with raw JSON only, no markdown, no explanation.",
                "max_tokens": 1000,
                "messages": [{{"role": "user", "content": prompt}}],
            },
            timeout=30,
        )

        if response.status_code != 200:
            print(f"Claude API error: {response.status_code} - {response.text}")
            return None

        raw = response.json()["content"][0]["text"].strip()
        raw = re.sub(r"```json|```", "", raw).strip()
        return json.loads(raw)

    except Exception as e:
        print(f"Quest generation failed: {e}")
        return None


def build_quests_block(quests, files_today):
    if not quests:
        return "_No quests generated yet. Will appear on next sync._"

    extensions_today = {os.path.splitext(f)[1].lower() for f in files_today if isinstance(f, str)}

    lines = []
    for q in quests:
        completed = q.get("file_ext", "") in extensions_today
        tick = "x" if completed else " "
        icon = {"SQL": "🗄️", "Python": "🐍", "Data": "📊"}.get(q["type"], "⚡")
        dataset = q.get("dataset", "")
        line = f"- [{tick}] {icon} **{q['type']} Quest:** {q['title']}\n  _{q['description']}_\n  📦 Dataset: `{dataset}`"
        lines.append(line)

    return "\n".join(lines)


# ─────────────────────────────────────────────
# SKILLS
# ─────────────────────────────────────────────

def process_files(files, state):
    extensions_seen = set()
    xp_gained = 0
    new_skills = []

    for filepath in files:
        if not isinstance(filepath, str):
            continue
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

    if len(extensions_seen) >= 3:
        xp_gained += DAILY_COMPLETION_BONUS
        print(f"Daily completion bonus! +{DAILY_COMPLETION_BONUS} XP")

    return xp_gained, new_skills


def build_skills_block(skills):
    skill_icons = {
        "SQL":            "🗄️",
        "Python":         "🐍",
        "Shell Scripting":"⚙️",
        "JSON & APIs":    "🔌",
        "Automation":     "🤖",
        "Data Cleaning":  "🧹",
        "Data Analysis":  "📊",
        "Data Modelling": "🏗️",
        "Documentation":  "📝",
    }
    lines = [f"- {skill_icons.get(s, '⚡')} **{s}**" for s in skills]
    return "\n".join(lines) if lines else "- No skills unlocked yet"


# ─────────────────────────────────────────────
# README UPDATE
# ─────────────────────────────────────────────

def update_readme(state, is_active, xp_gained, new_skills, files_today):
    try:
        with open("README.md", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found.")
        return

    for marker in [STATS_START, STATS_END, QUESTS_START, QUESTS_END]:
        if marker not in content:
            print(f"Error: Marker '{marker}' not found in README.md.")
            return

    xp = state["xp"]
    current_level, next_level = get_level_info(xp)
    xp_bar = build_xp_bar(xp, current_level, next_level)
    skills_block = build_skills_block(state["skills"])
    status = "ACTIVE 🟢" if is_active else "IDLE 🔴"
    sync_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    gained_str = f"+{xp_gained} XP today" if xp_gained > 0 else ""
    new_skill_str = f"\n- 🆕 **New Skills Unlocked:** {', '.join(new_skills)}" if new_skills else ""

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

    quests_block = build_quests_block(state.get("daily_quests", []), files_today)

    updated = re.sub(
        rf"{re.escape(STATS_START)}.*?{re.escape(STATS_END)}",
        f"{STATS_START}\n{new_stats}\n{STATS_END}",
        content, flags=re.DOTALL
    )
    updated = re.sub(
        rf"{re.escape(QUESTS_START)}.*?{re.escape(QUESTS_END)}",
        f"{QUESTS_START}\n{quests_block}\n{QUESTS_END}",
        updated, flags=re.DOTALL
    )

    if updated != content:
        with open("README.md", "w") as f:
            f.write(updated)
        print("System: README synchronized.")
    else:
        print("No changes needed.")

    state["last_sync"] = sync_time
    save_state(state)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("[ SYSTEM ENGINE STARTING ]")
    state = load_state()
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    files, is_active = get_todays_commits()
    print(f"Files changed today: {files}")

    xp_gained = 0
    new_skills = []

    if files:
        if state.get("last_xp_date") == today_str:
            print("XP already awarded today — skipping XP gain.")
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

    # Generate quests once per day
    if state.get("last_quest_date") != today_str:
        print("Generating daily quests...")
        quests = generate_quests(current["level"], current["title"], state["skills"])
        if quests:
            state["daily_quests"] = quests
            state["last_quest_date"] = today_str
            print(f"Generated {len(quests)} quests.")
        else:
            print("Quest generation failed, keeping previous quests.")
    else:
        print("Quests already generated today.")

    update_readme(state, is_active, xp_gained, new_skills, files)
    print("[ SYSTEM ENGINE DONE ]")