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
| 📅 Last Sync | 2026-11-08 14:00 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 5-day moving average and identifies stocks that have gained more than 10% over the last 20 trading days. Use window functions (AVG() OVER, ROW_NUMBER() OVER) and a CTE to rank stocks by momentum. Your output should show: stock_code, current_price, 5day_moving_avg, 20day_return_pct, and momentum_rank. Order by momentum_rank ascending._
  📦 Dataset: `ASX 200 historical stock prices — Kaggle`
  📁 Submit as: `quest1_2026-11-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Incident Aggregation
  _Download the NSW Road Crash dataset and clean it thoroughly: handle missing values in crash location and severity columns (decide: drop vs. impute), standardise crash_type values (remove whitespace, convert to uppercase), remove duplicate crash_id records, and convert date columns to datetime format. Then aggregate crashes by suburb and crash_type to produce a summary table showing crash_count, avg_severity_score, and date_range per suburb. Export to cleaned_crashes_summary.csv._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-08.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis: Python ETL + SQL Analytics
  _Part 1 (Python): Extract Melbourne pedestrian counting data, parse the timestamp column, resample to hourly foot traffic counts, and load into a SQLite database table called pedestrian_traffic (columns: sensor_id, location_name, traffic_datetime, hourly_count). Part 2 (SQL): Query the database to find peak traffic hours (top 3 hours by total count), identify which sensor locations have the most consistent traffic using variance, and create a summary showing location_name, peak_hour, avg_hourly_count, and consistency_score (inverse of variance). Export results to peak_traffic_analysis.csv. This simulates a real data pipeline: ingest → transform → load → analyse._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-11-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
