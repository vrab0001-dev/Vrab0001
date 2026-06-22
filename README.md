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
| 📅 Last Sync | 2026-06-22 12:34 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Rankings
  _Using ASX 200 historical price data, write a query that calculates the 30-day rolling average closing price for each stock, then ranks stocks by their rolling average performance within each month. Use window functions ROW_NUMBER() OVER (PARTITION BY month ORDER BY rolling_avg DESC) to identify the top 5 performers each month. Include the stock symbol, date, closing price, rolling average, and rank. Filter results to show only the top 10 ranked stocks per month for the last 12 months. Expected output: a result set showing monthly performance rankings with 120 rows (10 stocks × 12 months)._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Pipeline
  _Download NSW Road Crash Data from the official source. Your task: (1) Load the CSV into pandas and identify missing values in key columns (crash_date, severity, suburb, vehicle_count). (2) Handle missing severity values by imputing with the mode per suburb. (3) Create a new column 'crash_hour' by extracting the hour from the timestamp. (4) Remove duplicate crash records based on crash_id. (5) Filter to crashes occurring in the last 2 years. (6) Export three cleaned CSVs: crashes_by_severity.csv, crashes_by_suburb.csv (top 20 suburbs), and crashes_by_hour.csv (hourly distribution). Validate row counts at each step and print a data quality report showing null counts before and after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-22.py`
- [ ] ⚡ **Combined Quest:** Australian Weather & Wildfire Correlation Analysis
  _Combine two datasets: Australian Weather Observations (daily temperature, rainfall, humidity) and Australian Wildfire incidents (date, location, area burned). (1) In Python: load both CSVs, clean date formats to YYYY-MM-DD, merge on nearest date within 3 days using pandas merge_asof(), aggregate weather metrics by week and state. (2) In SQL: create a temp table from the merged Python output, then write a query using CTEs to calculate: (a) average temperature and rainfall per state per month, (b) total area burned per state per month, (c) correlation score (simple: normalized temperature difference × rainfall deficit) against burned area. Rank states by correlation strength using ROW_NUMBER(). (3) Output: a final CSV showing month, state, avg_temp, total_rainfall, area_burned, and correlation_rank. Expected insight: identify which states show strongest weather-to-wildfire relationships._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle) + Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-06-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
