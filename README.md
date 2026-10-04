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
| 📅 Last Sync | 2026-10-04 14:10 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Moving Average Momentum Tracker
  _Using ASX 200 historical price data, write a query with window functions to calculate the 20-day and 50-day moving averages for each stock ticker. Then use a CTE to identify stocks where the 20-day MA crossed above the 50-day MA (bullish signal) in the last 10 trading days. Return ticker, date of crossover, closing price on that date, and the volume traded. Order by most recent crossover first. This tests ROW_NUMBER, LAG, and complex CTEs._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (contains crash records with location, time, vehicle types, injury severity). Write a Python/pandas script that: (1) loads the CSV, (2) handles missing values in key columns (crash_date, latitude, longitude, severity) by imputation or removal, (3) standardises datetime formats, (4) removes duplicate crash records, (5) creates a new column 'crash_hour' extracted from crash_time, (6) filters crashes in Greater Sydney (lat/lon bounds), and (7) exports a cleaned CSV. Include error handling for file I/O and data type mismatches._
  📦 Dataset: `NSW Road Crash Data — NSW Open Data Portal (data.nsw.gov.au)`
  📁 Submit as: `quest2_2026-10-04.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes ETL Pipeline
  _Build a mini data pipeline: (1) Use Python/pandas to download Australian Bureau of Meteorology weather observations (CSV format), clean temperature and rainfall columns (handle nulls, convert to numeric), and standardise date formats. (2) Load the cleaned data into a local SQLite database. (3) Write SQL queries to find: the top 10 hottest days across all stations, stations with highest average rainfall by month, and use a window function (ROW_NUMBER) to identify the hottest day per station per season. Export results to separate CSVs. This tests end-to-end Python→SQL→Python workflow._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-10-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
