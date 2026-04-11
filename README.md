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
| 📅 Last Sync | 2026-04-11 11:12 AEDT |

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
- [ ] 🗄️ **SQL Quest:** AFL Season Performance Rankings with Running Averages
  _Using AFL match results data, write a query that ranks teams by their cumulative win percentage across a full season using window functions. Calculate a running average of points scored per match for each team ordered by round number. Include columns: Team, Round, Points_For, Running_Avg_Points, Win_Percentage_to_Date, and Rank_by_Wins. Use ROW_NUMBER() or RANK() to handle ties appropriately, and a CTE to pre-calculate team performance metrics before the final ranking window._
  📦 Dataset: `AFL Match Results — Kaggle (AFL historical match data)`
  📁 Submit as: `quest1_2026-04-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data and perform the following: (1) Load the CSV and identify missing values, data type inconsistencies, and outliers in crash severity, vehicle count, and speed limit columns. (2) Clean the data by handling nulls appropriately (drop/fill based on column importance). (3) Engineer 3 new features: crash_severity_category (High/Medium/Low based on injury count), is_nighttime (based on crash time), and crash_cluster (group crashes within 100m radius and 5min time window). (4) Export the cleaned dataset to a new CSV. Document all transformations in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-11.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Create an end-to-end pipeline: (1) In Python, load Australian Bureau of Meteorology weather observations (temperature, rainfall, pressure). Clean the data by removing duplicates, handling missing values, and converting dates to datetime objects. (2) Calculate monthly aggregates (mean temp, total rainfall, median pressure) grouped by location. (3) Write these aggregates to a SQL database or CSV as staging data. (4) In SQL, identify locations with anomalies using window functions: flag any month where temperature deviates >2 standard deviations from the 12-month rolling average, or rainfall is in the top 5% for that location historically. (5) Return a result set with: Location, Month, Temperature_Anomaly_Flag, Rainfall_Percentile, and Anomaly_Type. Include a CTE for calculating rolling statistics._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology via Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-04-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
