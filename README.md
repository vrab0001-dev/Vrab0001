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
| 📅 Last Sync | 2026-07-15 11:13 AEDT |

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
  _Using the ASX 200 historical stock prices dataset, write a SQL query that calculates for each stock: (1) the 20-day moving average of closing price using a window function, (2) the percentage change from the previous day's close using LAG(), and (3) rank stocks by their 20-day price momentum (highest to lowest). Filter results to show only the top 10 momentum stocks as of the most recent trading date. Your output should include: stock_code, date, closing_price, moving_avg_20day, pct_change_prev_day, momentum_rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data dataset. Write a Python script using pandas that: (1) loads the crash CSV, (2) cleans missing values in critical columns (crash_severity, speed_zone, weather_condition) by forward-filling or dropping as appropriate, (3) converts date columns to datetime format, (4) creates new features: hour_of_day (from crash_time), is_weekend (from crash_date), and severity_category (binning crash_severity into High/Medium/Low), (5) removes duplicate records based on crash_id, and (6) exports the cleaned dataset to a new CSV. Log the number of rows removed and columns created._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-15.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Using the Australian Bureau of Meteorology weather observations dataset: (1) Write a Python script that loads historical temperature and rainfall data for 2024, cleans any missing or invalid values, and exports it to a local SQLite database with separate tables for temperature and rainfall. (2) Write SQL queries in the same script that identify: anomaly records where daily temperature exceeds the 95th percentile OR is below the 5th percentile for that month/station, and rainfall events exceeding 150mm. (3) Generate a summary report showing: station_name, anomaly_date, anomaly_type (temp_high/temp_low/heavy_rain), and severity_score. (4) Export the anomaly report to CSV. The script should handle data validation, log processing steps, and handle partial/missing data gracefully._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle jsphyg)`
  📁 Submit as: `quest3_2026-07-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
