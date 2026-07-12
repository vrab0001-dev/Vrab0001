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
| 📅 Last Sync | 2026-07-12 11:25 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 7-day moving average of closing prices for the top 10 most traded stocks by volume, (2) Use ROW_NUMBER() to rank each stock's daily returns within its own partition, (3) Use LAG() to calculate day-over-day price change, (4) Filter for only days where the stock outperformed its 7-day moving average. Return: stock_code, date, close_price, moving_avg_7day, daily_return_pct, rank_within_stock. Order by stock_code and date. Expected output: 50-200 rows depending on data span._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data (contains accident records with severity, location, vehicle types, etc.). Write a Python/pandas script to: (1) Load the CSV and identify missing values—document which columns have >20% nulls and decide on imputation strategy, (2) Standardise location data (clean suburb names, handle postcodes), (3) Create new features: day_of_week from crash date, is_fatal (binary from severity), traffic_volume_category (binned from vehicle count), (4) Remove duplicates based on crash_id and date, (5) Export cleaned dataset to a new CSV. Document any data quality issues found and your decisions in comments. Expected output: cleaned CSV with 5+ new columns and <2% nulls._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-12.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Build an end-to-end pipeline using Python + SQL: (1) Download Australian weather observations (temperature, rainfall, wind) from Bureau of Meteorology / Kaggle dataset for 2 states (e.g. NSW, VIC) over past 12 months, (2) Use Python/pandas to clean the data (handle missing values, remove outliers using IQR method, standardise unit formats), (3) Load cleaned data into a local SQLite database (create weather_observations table with proper schema), (4) Write a SQL query with CTEs to: identify anomalous days per station (where temp or rainfall >2 std devs from 30-day rolling mean), rank anomalies by severity, calculate frequency of anomalies per station per month, (5) Export results showing: station_id, date, metric_type, anomaly_severity_rank, rolling_mean_30d, actual_value. Expected output: SQL results CSV with 30-100 anomaly records, plus documented Python script and database schema._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
