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
| 📅 Last Sync | 2026-07-13 11:26 AEDT |

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
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify stocks that have exceeded their moving average by more than 5% in the last 30 days. Use window functions (AVG() OVER, ROW_NUMBER()) to rank stocks by momentum strength. Your output should show: stock_code, current_price, moving_avg_20day, momentum_percentage, and momentum_rank. Filter for only the top 10 momentum gainers._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data and clean it for analysis: (1) Handle missing values in injury_type and crash_type columns using appropriate strategies; (2) Standardise datetime columns to ISO format; (3) Remove duplicate crash records based on crash_id and date; (4) Create new features: time_of_day (morning/afternoon/night), severity_category (minor/moderate/severe), and weekday name; (5) Export cleaned dataset to CSV with consistent naming conventions. Provide a data quality report showing row counts before/after cleaning and missing value percentages._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-13.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Foot Traffic Trend Analysis Pipeline
  _Build an end-to-end pipeline: (1) Using Python, download Melbourne Pedestrian Counting data and clean it (handle nulls, validate date ranges, ensure sensor_id consistency); (2) Aggregate hourly counts to daily totals by sensor location using pandas; (3) Load cleaned data into a SQL database or create a temporary table; (4) Write SQL queries to: find the top 5 busiest locations by average daily foot traffic, calculate week-over-week percentage change for each sensor in the last 30 days, identify anomalies (days with traffic >2 standard deviations from monthly average); (5) Export results showing location_name, avg_daily_traffic, wow_change_percent, and anomaly_flag. Provide documentation of your data pipeline decisions._
  📦 Dataset: `Melbourne Pedestrian Counting Data — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-07-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
