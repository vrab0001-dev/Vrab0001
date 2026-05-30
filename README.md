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
| 📅 Last Sync | 2026-05-30 11:54 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Moving Averages
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate a 30-day moving average of closing prices for each stock symbol, (2) Rank stocks by their current price relative to their 30-day moving average (highest performer first), (3) Use ROW_NUMBER to identify the top 5 performers and bottom 5 performers on 2026-05-30, (4) Include columns: symbol, current_close, moving_avg_30d, performance_rank, rank_category. Your output should show which stocks are trading furthest above/below their moving average._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Geo-Aggregation
  _Download NSW Road Crash Data from data.nsw.gov.au. Write a Python pandas script to: (1) Load the CSV and inspect for missing values, duplicates, and data type inconsistencies, (2) Clean crash severity codes and location data (handle null/invalid entries), (3) Extract year and month from crash date column, (4) Aggregate total crashes by Local Government Area (LGA) and severity level, (5) Export a clean CSV with columns: lga, year, month, severity, crash_count, sorted by crash_count descending. Document any data quality issues found._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-30.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a Python + SQL pipeline using Bureau of Meteorology weather observations (Kaggle jsphyg dataset or similar): (1) In Python: Load daily temperature and rainfall CSV files, clean missing values, calculate monthly min/max/average temperatures and total rainfall by station, export to intermediate CSV, (2) In SQL: Create a temp table from the cleaned data, use window functions (LAG, LEAD) to calculate month-on-month temperature and rainfall changes, identify stations with anomalies (>2 standard deviations from 5-year average), (3) Generate a final report showing: station_id, month, temperature_anomaly_flag, rainfall_anomaly_flag, anomaly_magnitude. Focus on Australian stations only._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-05-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
