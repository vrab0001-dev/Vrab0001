# ⚡ [ SYSTEM STATUS: ONLINE ]

### 👤 PLAYER: Vrab0001
### 🌏 REGION: Australia

---

<!-- VRAB_SYSTEM_STATS_START -->
**Status:** IDLE 🔴

| Stat | Value |
|------|-------|
| 🎖️ Title | Data Cadet |
| ⚡ Level | 1 |
| 💠 Total XP | 9  |
| 📅 Last Sync | 2026-05-22 12:03 AEDT |

**XP Progress:** `██████████████████░░ 9/10 XP`

### 🛠️ SKILLS UNLOCKED
- 🗄️ **SQL**
- 🧹 **Data Cleaning**
- 🏗️ **Data Modelling**
- 🐍 **Python**
<!-- VRAB_SYSTEM_STATS_END -->

---

### 📜 DAILY QUEST LOG

<!-- VRAB_QUESTS_START -->
- [ ] 🗄️ **SQL Quest:** RBA Interest Rate Trend Analysis with Window Functions
  _Using RBA interest rate decisions dataset, write a SQL query with window functions to: (1) Calculate the monthly average interest rate, (2) Use ROW_NUMBER() to rank each decision chronologically, (3) Use LAG() to find the previous month's rate and calculate the month-on-month change in basis points, (4) Use a CTE to filter only decisions where the rate changed by more than 25 basis points, and (5) Return the decision date, rate, change in basis points, and rank ordered by date. Expected output: 15-30 rows showing significant rate movements since 2020._
  📦 Dataset: `RBA Interest Rate Decisions — rba.gov.au`
  📁 Submit as: `quest1_2026-05-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download the NSW Road Crash Data (CSV format). Write a Python/pandas script to: (1) Load the dataset and identify missing values in crash_severity, day_of_week, and weather columns, (2) Handle missing values using forward-fill for time-series columns and mode-fill for categorical columns, (3) Create new features: hour_of_day from crash_time, is_weekend from day_of_week, and severity_risk_score (ordinal encoding of crash_severity), (4) Remove rows where crash_latitude or crash_longitude are null, (5) Export the cleaned dataset to a new CSV file. Expected output: Cleaned CSV with 10+ additional features and <5% missing data._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-22.py`
- [ ] ⚡ **Combined Quest:** AFL Match Performance Trends: Python ETL + SQL Analytics
  _Using AFL match results dataset (Kaggle): (1) Python task: Write a pandas script to load the AFL CSV, clean team names (standardise case, remove trailing spaces), convert dates to datetime, and calculate rolling 5-match average points for each team. Export to a new CSV with columns: match_date, team, opponent, points, points_for, points_against, rolling_avg_points. (2) SQL task: Load the cleaned CSV into a database table. Write a query using CTEs and window functions to: Find the top 3 teams by average points scored in 2024, rank their performances by round using RANK(), calculate their win percentage (matches where points_for > points_against), and return team name, avg_points, win_percentage, and rank. Expected output: Table showing top 3 teams with season performance metrics._
  📦 Dataset: `AFL Match Results — Kaggle`
  📁 Submit as: `quest3_2026-05-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
