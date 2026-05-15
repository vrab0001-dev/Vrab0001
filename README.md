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
| 📅 Last Sync | 2026-05-15 11:57 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Tracker
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate for each stock: (1) the 30-day rolling average closing price, (2) the rank of each stock by trading volume within each date, and (3) the day-over-day price change using LAG(). Filter for the top 10 most volatile stocks (highest standard deviation of daily returns) in the last 90 days. Return columns: stock_code, date, close_price, rolling_30d_avg, volume_rank, price_change, volatility_rank. Use CTEs to break down the calculation into logical steps._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (2020–2026) and build a pandas data cleaning script that: (1) handles missing values in crash_location, severity, and vehicle_type columns by imputation or removal with justification, (2) standardises date formats and converts to datetime, (3) removes duplicate crash records based on crash_id and timestamp, (4) validates that latitude/longitude fall within NSW bounds (approximately -28° to -34° lat, 141° to 154° long), (5) creates a new column 'hour_of_day' from the crash timestamp, and (6) exports a cleaned CSV. Log all data quality issues (missing counts, duplicates removed, invalid coordinates) to a summary report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-15.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline: (1) Use Python/pandas to load Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) for a single Australian city over 5+ years, clean the data (handle missing values, convert units if needed), and calculate monthly aggregates (mean temp, total rainfall, mean humidity). (2) Load the aggregated data into SQLite. (3) Write SQL queries to identify anomalies: using window functions, calculate the 5-year monthly average and standard deviation for each month (e.g. all Januaries), then flag months where the current value exceeds mean + 2 standard deviations. (4) Export results showing month, actual value, expected range, and anomaly flag. Produce a final summary: How many anomalies detected? Which months/metrics show the most deviation?_
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
