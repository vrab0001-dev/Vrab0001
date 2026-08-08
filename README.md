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
| 📅 Last Sync | 2026-08-08 10:43 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Ranking with Moving Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate daily percentage returns for each stock, (2) Rank stocks by return within each date using ROW_NUMBER(), (3) Calculate a 7-day moving average of closing price for each stock using LAG(), (4) Identify the top 5 best and worst performing stocks on the most recent date in your dataset. Return columns: date, stock_code, close_price, daily_return_pct, return_rank, moving_avg_7day. Use a CTE to structure the window function logic clearly._
  📦 Dataset: `ASX 200 historical stock prices — Kaggle`
  📁 Submit as: `quest1_2026-08-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Scoring
  _Download the NSW Road Crash Data (contains crash records with timestamps, locations, vehicle counts, injury severity). Write a Python script using pandas to: (1) Load the CSV and inspect for missing values, duplicates, and data type inconsistencies, (2) Handle missing values in critical columns (crash_type, severity, location_code) using appropriate imputation or removal, (3) Create a new 'severity_score' column (0-10 scale) derived from injury counts and crash type, (4) Filter for crashes in Greater Sydney area only, (5) Export cleaned data to a new CSV with datetime columns properly formatted. Document your cleaning decisions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-08.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: ETL Pipeline with SQL Analysis
  _Build a mini ETL pipeline: (1) Use Python/pandas to load Australian Bureau of Meteorology observations (or Kaggle's Australian Weather dataset), clean temperature and rainfall columns (handle missing values, outliers, unit conversions if needed), and load into a local SQLite database with tables: weather_stations (station_id, location, state) and daily_observations (station_id, date, max_temp, min_temp, rainfall_mm). (2) In SQL, write a query using window functions to: Calculate rolling 30-day average temperature and rainfall for each station, identify the hottest and wettest days per station using RANK(), and find stations where the temperature trend is increasing month-over-month using LAG(). (3) Output a summary report: top 3 hottest stations, top 3 wettest regions, and stations with warming trends. Provide both the Python script (.py) and SQL query (.sql)._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-08-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
