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
| 📅 Last Sync | 2026-08-27 15:27 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using ASX 200 historical prices dataset, calculate a 20-day rolling average price and identify stocks that have crossed above their rolling average in the last 5 trading days. Use window functions (AVG() OVER, ROW_NUMBER() OVER) and CTEs to: (1) calculate the 20-day rolling average for each stock, (2) identify crossover events where close price > rolling average and the previous close was <= rolling average, (3) rank these crossover events by stock symbol and date. Return: stock_symbol, crossover_date, close_price, rolling_avg_20, days_since_crossover. Order by most recent crossovers first._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (from NSW Open Data). Write a Python/pandas script to: (1) load the raw crash CSV, (2) clean date/time columns into proper datetime format, (3) handle missing values in Severity and Crash Type fields using mode imputation, (4) remove duplicate records based on Crash ID and Date, (5) create a new column 'time_of_day' categorising crashes as Morning (6-12), Afternoon (12-18), Evening (18-24), Night (0-6), (6) aggregate by Local Government Area and time_of_day to count total crashes, injuries, and fatalities, (7) export cleaned data and aggregated summary to separate CSV files. Include error handling and print a data quality report (missing %, duplicates removed, final row count)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-27.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Using Australian Weather observations dataset (Bureau of Meteorology / Kaggle), build an end-to-end pipeline: (1) In Python/pandas: load weather CSV, clean temperature and rainfall columns (handle missing/outlier values using IQR method), aggregate daily maximum temperature and total rainfall by station and month, (2) Export cleaned aggregated data to a staging table in SQL, (3) In SQL: Use window functions (RANK() OVER, LAG()) to identify temperature and rainfall anomalies — flag any day where max temp is in top 5% for that station-month combination or rainfall is in bottom 5% (drought risk). Create a CTE that combines both anomalies and returns: station_name, date, max_temp, rainfall, anomaly_type, severity_rank. (4) In Python: query results back and generate a summary report counting anomalies by station and type. Save anomaly report as CSV with visualisation-ready columns._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-08-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
