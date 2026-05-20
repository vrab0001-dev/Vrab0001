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
| 📅 Last Sync | 2026-05-20 12:02 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Performance Ranking with Rolling Averages
  _Using the ASX 200 historical stock prices dataset, write a SQL query with window functions to: (1) Calculate the 20-day and 50-day rolling average closing price for each stock ticker, (2) Rank stocks by their most recent closing price relative to their 50-day average (stocks closest to or above their 50-day average rank highest), (3) Use ROW_NUMBER() to identify the best and worst performing stock in the last 30 days by percentage gain/loss, (4) Return columns: ticker, date, close_price, avg_20_day, avg_50_day, rank_vs_50day, daily_pct_change. Filter for the last 90 days only. Order by rank_vs_50day descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-20.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Summarisation Pipeline
  _Download the NSW Road Crash Data (CSV format from data.nsw.gov.au). Build a Python script using pandas that: (1) Loads the crash data and inspects for missing values, duplicates, and data type mismatches, (2) Cleans the dataset by handling nulls in severity/location columns (document your decisions), (3) Creates a new column 'hour_of_day' extracted from the crash timestamp, (4) Filters for crashes in the last 5 years only, (5) Groups by local government area (LGA) and hour_of_day to find peak crash hours by region, (6) Exports a summary CSV with columns: LGA, hour_of_day, crash_count, avg_severity. Include comments explaining each cleaning decision._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-20.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes: ETL Pipeline with SQL Analytics
  _Build an end-to-end pipeline: (1) Use Python to download or load the Australian Weather observations dataset (Bureau of Meteorology / Kaggle), clean temperature and rainfall columns (handle outliers, missing values), validate data quality, and load into a local SQLite database, creating a table 'weather_observations' with columns: station_id, station_name, observation_date, max_temp_celsius, min_temp_celsius, rainfall_mm. (2) Write SQL queries to: identify stations with the highest temperature extremes (max >= 45°C) in the last 10 years, calculate monthly rainfall totals by state, use a CTE to find stations where max_temp exceeded the 90th percentile for their region, rank states by average maximum temperature using window functions. (3) Export results showing: top 10 hottest days by station, driest and wettest months by state. Document the ETL decisions in code comments._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
