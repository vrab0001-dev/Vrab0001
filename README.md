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
| 📅 Last Sync | 2026-08-10 10:48 AEDT |

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
  _Using ASX 200 historical stock price data, write a query with window functions to: (1) Calculate daily percentage returns for each stock, (2) Rank stocks by return within each trading day using ROW_NUMBER() or RANK(), (3) Compute a 5-day moving average of closing prices using LAG() or a window frame, (4) Identify the top 3 performers and bottom 3 performers for each week. Return columns: date, stock_code, daily_return_pct, rank_by_day, moving_avg_5day, weekly_rank. Use CTEs to organize your logic cleanly._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-08-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (contains crash incidents with location, date, injury severity, road conditions). Build a Python/pandas script to: (1) Load the CSV and inspect for missing values, duplicates, and data type issues, (2) Clean location data (standardize suburb names, handle null coordinates), (3) Convert date columns to datetime and extract year/month/day_of_week, (4) Remove or flag rows with incomplete severity or location data, (5) Aggregate crashes by suburb and severity level, (6) Export a cleaned dataset and a summary report showing top 10 crash hotspots. Ensure the output is production-ready with proper error handling._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-10.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection & Historical Context
  _Combine Python and SQL for a weather analysis task: (1) In Python, download or load Australian Weather observations (Bureau of Meteorology or Kaggle dataset by jsphyg). Clean temperature, rainfall, and humidity columns; handle missing data via interpolation or forward-fill. (2) Load the cleaned data into a local SQLite database. (3) Write a SQL query using window functions (LAG, LEAD) to identify days where temperature or rainfall deviated significantly from the 30-day rolling average. Flag anomalies where the value is >2 standard deviations from the rolling mean. (4) Output a report: station_name, date, metric (temperature/rainfall), observed_value, rolling_mean, deviation_std, anomaly_flag. (5) In Python, visualize the top 5 anomalies per metric as a summary table or plot. Document your findings in a short text summary (3-5 sentences) on data quality and unusual weather patterns detected._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-08-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
