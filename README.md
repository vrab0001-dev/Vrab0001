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
| 📅 Last Sync | 2026-05-13 11:56 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Momentum Rankings
  _Using ASX 200 historical price data, write a query with window functions to: (1) Calculate the 5-day price change percentage for each stock using LAG(), (2) Rank stocks daily by momentum using RANK() OVER (PARTITION BY date ORDER BY price_change DESC), (3) Use a CTE to identify the top 10 and bottom 10 momentum stocks for the most recent trading date. Return: stock_code, date, close_price, 5day_change_pct, momentum_rank. Sort by momentum_rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains multiple CSV files with crash details, vehicles, persons involved). Write a Python/pandas script to: (1) Load and inspect all CSV files, (2) Clean: handle missing values in severity/crash_type columns (document your strategy), standardise date formats, remove duplicates on crash_id, (3) Merge crash and persons tables on crash_id, (4) Create a summary CSV with crashes grouped by local_govt_area, severity, and year. Output: LGA, severity, year, crash_count, injury_count. Save as 'nsw_crashes_summary.csv'._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-13.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Score Pipeline
  _Build a data pipeline combining wildfire incident data with Bureau of Meteorology observations: (1) In Python: load Australian Wildfire dataset (Kaggle) and weather observations CSV. Clean wildfire data (standardise state names, handle missing coordinates). Merge on date and location (nearest station within 50km). (2) In SQL: create a temp table from the merged CSV, calculate a risk_score = (fire_frequency_last_30days * 10) + (max_temp_anomaly) + (days_since_rain), rank locations by risk_score using ROW_NUMBER() for each state. (3) Export top 20 highest-risk locations with state, location, risk_score, last_fire_date, current_temp_anomaly to 'wildfire_risk_report.csv'._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle; Bureau of Meteorology observations — Bureau of Meteorology`
  📁 Submit as: `quest3_2026-05-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
