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
| 📅 Last Sync | 2026-04-22 11:19 AEDT |

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
- [ ] 🗄️ **SQL Quest:** NSW Road Crash Severity Trends with Window Functions
  _Using NSW Road Crash Data, write a SQL query with window functions to identify crash severity patterns. Calculate: (1) ROW_NUMBER() to rank crashes by severity within each Local Government Area, (2) LAG() to compare current month's crash count vs previous month, (3) RANK() to identify top 10 most dangerous intersections by injury count. Use a CTE to aggregate crashes by month, LGA, and severity level. Return LGA, month, crash_count, previous_month_count, month_over_month_change, and severity_rank. Filter for crashes from 2023 onwards only._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest1_2026-04-22.sql`
- [ ] 🐍 **Python Quest:** Clean and Standardise Australian Weather Observations
  _Download the Australian Bureau of Meteorology weather observations dataset (or equivalent Kaggle weather dataset for Australia). Write a pandas script to: (1) handle missing values in temperature, rainfall, and wind speed columns, (2) convert all temperature readings to Celsius, (3) remove duplicate records by station_id and timestamp, (4) standardise location names (strip whitespace, title case), (5) create a new column for season based on month, (6) export cleaned data to a new CSV file. Document any data quality issues found (e.g., outliers, inconsistent units). Aim for 90%+ data completeness in critical fields._
  📦 Dataset: `Australian Weather Observations — Kaggle (jsphyg) or Bureau of Meteorology`
  📁 Submit as: `quest2_2026-04-22.py`
- [ ] ⚡ **Combined Quest:** Australian Energy Demand Analysis Pipeline
  _Build an end-to-end data engineering pipeline using AEMO electricity demand data: (1) In Python: load the CSV/JSON data, clean and validate timestamps, remove anomalies (demand spikes >3 std dev), aggregate hourly demand to daily peak/average, export to a temporary database-ready CSV. (2) In SQL: load cleaned data into a table, create a CTE to calculate 7-day and 30-day rolling averages using window functions, rank days by demand intensity, identify peak demand periods by state and season. (3) Output a summary table with: date, state, peak_demand, avg_demand, 7day_rolling_avg, demand_rank, and season. Expected output: cleaned dataset + SQL results showing seasonal demand patterns and top 5 peak demand days._
  📦 Dataset: `AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-04-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
