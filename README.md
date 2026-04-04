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
| 📅 Last Sync | 2026-04-04 12:08 AEDT |

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
  _Using ASX 200 historical stock price data, write a SQL query with window functions to calculate 30-day price momentum for each stock. Specifically: (1) Use LAG() to get the closing price from 30 days prior; (2) Calculate percentage change: ((current_close - price_30_days_ago) / price_30_days_ago) * 100; (3) Use ROW_NUMBER() PARTITION BY stock_symbol to rank trading days chronologically; (4) Filter for the most recent trading date only; (5) Return top 10 stocks by momentum (ascending and descending). Expected output: stock_symbol, current_close, price_30_days_ago, momentum_percentage, momentum_rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (available as CSV). Write a Python pandas script to: (1) Load the dataset and inspect for missing values, duplicates, and data types; (2) Handle missing values in crash_severity and crash_type columns (document your imputation strategy); (3) Create new features: crash_hour from crash_time, is_fatal (boolean from severity), day_of_week from crash_date; (4) Remove rows where geographic coordinates are NULL; (5) Standardize location_name to title case; (6) Export cleaned dataset to a new CSV file with row count and column count logged to console. Expected output: cleaned CSV file + summary statistics (original vs cleaned row counts, null value counts before/after)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-04.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Data Pipeline: ETL & Anomaly Detection
  _Build an end-to-end data engineering pipeline using Australian Weather observations (Bureau of Meteorology dataset available on Kaggle). Part A (Python): (1) Load weather CSV (temperature, rainfall, humidity, wind_speed by station_id and date); (2) Clean data: handle missing values via forward-fill by station, remove outliers using IQR method for temperature; (3) Create a processed CSV with cleaned data + a new feature: rolling_7day_avg_temp (7-day moving average grouped by station). Part B (SQL): (1) Load the cleaned CSV into a SQLite database; (2) Write a CTE-based query to identify anomalies: days where temperature deviates >2 standard deviations from the 30-day rolling mean per station; (3) RANK anomalies by severity (std_dev_distance) within each station using window functions; (4) Return: station_id, date, temp, rolling_mean, std_dev_distance, anomaly_rank. Expected output: cleaned CSV file + SQL query result showing top 20 temperature anomalies across all stations._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-04-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
