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
| 📅 Last Sync | 2026-11-24 18:22 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Trading Performance Streaks
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to identify the longest consecutive days each stock experienced gains (close price higher than previous day). Use ROW_NUMBER and PARTITION BY to group stocks, then calculate streak lengths. Return the top 10 stocks with their longest winning streaks, including stock symbol, streak length in days, and the date range of the streak. Use a CTE to organize your window function logic._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-11-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from the NSW open data portal. Write a Python pandas script that: (1) loads the CSV, (2) identifies and handles missing values in critical columns (crash date, severity, location), (3) standardizes location names (trim whitespace, convert to title case), (4) creates a new 'crash_hour' column extracted from the crash time, (5) removes duplicate records based on crash ID, and (6) exports the cleaned dataset to a new CSV. Document your data quality findings (% of missing data per column, # of duplicates removed)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-24.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends Analysis Pipeline
  _Build an end-to-end pipeline: (1) Use Python pandas to load Australian Weather observations dataset (Bureau of Meteorology / Kaggle), clean temperature and rainfall columns, handle missing values, and aggregate daily data into monthly summaries grouped by weather station. Export to a CSV or SQLite database. (2) Write SQL queries to: calculate the month-over-month temperature change (using LAG window function), identify which stations had the highest rainfall variability (stddev) in the last 12 months, and rank stations by temperature anomaly (deviation from long-term mean). Combine results into a single summary report showing top 5 anomalies by station._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-11-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
