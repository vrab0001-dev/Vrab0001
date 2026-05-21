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
| 📅 Last Sync | 2026-05-21 12:01 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate daily percentage returns for each stock, (2) Rank stocks by return within each date using ROW_NUMBER(), (3) Compute a 7-day moving average of closing prices using a window frame, (4) Identify the top 5 best and worst performers for each trading day. Return columns: date, stock_code, close_price, daily_return_pct, return_rank, moving_avg_7day. Use CTEs to structure the query logically._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (CSV format). Build a Python/pandas script to: (1) Load the dataset and identify missing values, data type mismatches, and outliers in crash severity, injury count, and speed limit columns, (2) Clean the data by handling nulls, standardising categorical fields (e.g., crash type, vehicle type), and removing duplicates, (3) Aggregate crashes by local government area (LGA) and crash severity, (4) Export a cleaned CSV and a summary report showing crash counts, injury rates, and top 10 high-risk LGAs. Include data quality checks before and after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-21.py`
- [ ] ⚡ **Combined Quest:** Bureau of Meteorology Weather Anomaly Detection Pipeline
  _Combine Python and SQL to build an end-to-end pipeline: (1) In Python, download Australian weather observations (temperature, rainfall, pressure) from Bureau of Meteorology dataset or Kaggle jsphyg weather data, clean missing values, and load into a local SQLite database, (2) In SQL, calculate monthly climate normals (30-year average) for each weather station using window functions and CTEs, (3) Identify anomalies: months where temperature or rainfall deviated >2 standard deviations from the normal using LAG() and LEAD() to compare consecutive months, (4) Export results showing station name, date, observed value, normal value, deviation, and anomaly flag. Provide both the Python loader script and the SQL analysis query._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-05-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
