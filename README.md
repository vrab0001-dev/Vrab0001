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
| 📅 Last Sync | 2026-07-22 11:21 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 30-day rolling average price for each stock, (2) the rank of each stock by price change percentage within each month, and (3) identify the top 5 best-performing stocks (by percentage gain) in the most recent month. Use ROW_NUMBER() and LAG() to compare current price against price 30 days prior. Return columns: ticker, date, price, 30day_avg, monthly_rank, pct_change. Filter only for stocks in the ASX 200 index._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains raw incident records with messy formatting). Write a Python pandas script to: (1) handle missing values in crash severity, location, and time columns, (2) standardise datetime formats, (3) remove duplicate records based on crash ID, (4) create new features: hour_of_day (from time), is_weekend (from date), severity_category (map numeric codes to High/Medium/Low), (5) aggregate crashes by Local Government Area (LGA) and severity, counting incidents per category. Export cleaned data to CSV with summary statistics printed (total crashes, crashes by severity, top 5 LGAs by incident count)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-22.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes Pipeline
  _Using Australian Bureau of Meteorology weather observation data (or Kaggle's jsphyg dataset): (1) Write a Python script using pandas to load raw weather CSV files, clean temperature and rainfall columns (handle unit conversions if needed, remove outliers >50°C or <-50°C), and aggregate daily readings to monthly summaries (min temp, max temp, mean temp, total rainfall) by station. (2) Load this cleaned data into a SQL database (SQLite or local PostgreSQL). (3) Write a SQL query with CTEs to identify: for each month in the dataset, which station recorded the highest temperature anomaly (actual max temp minus 10-year average max temp for that month), and rank the top 10 temperature anomalies across all months and stations. Return: month, station_name, actual_max_temp, historical_avg_temp, anomaly_value, anomaly_rank._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-07-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
