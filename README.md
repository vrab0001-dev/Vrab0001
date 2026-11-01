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
| 📅 Last Sync | 2026-11-01 13:55 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their 30-day price momentum. Calculate the percentage change from 30 days ago to today for each stock using LAG() and RANK() functions. Include columns: stock_symbol, current_price, price_30_days_ago, momentum_pct, momentum_rank. Filter only for stocks with valid 30-day history and order by momentum_rank. Use a CTE to calculate lagged prices, then a second CTE to compute momentum percentages._
  📦 Dataset: `ASX 200 historical stock prices — Kaggle`
  📁 Submit as: `quest1_2026-11-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (CSV format). Write a Python script using pandas to: (1) Load the dataset and identify missing values and inconsistent data types; (2) Clean the crash_severity column by standardizing values (e.g., 'Fatal', 'Serious injury', 'Other injury'); (3) Parse date columns into datetime format; (4) Remove duplicate crash records based on crash_id; (5) Create a new column for crash_hour extracted from time data; (6) Aggregate crashes by local government area (LGA) and severity, counting total incidents; (7) Export cleaned data to a new CSV file with summary statistics printed to console (total crashes, crashes by severity, top 5 LGAs by incident count)._
  📦 Dataset: `NSW Road Crash Data — Transport for NSW (data.nsw.gov.au)`
  📁 Submit as: `quest2_2026-11-01.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Hourly Footfall Analysis & Anomaly Detection
  _Combine Python and SQL to analyze Melbourne pedestrian counting data. (1) In Python: Load the pedestrian CSV dataset, clean datetime columns, handle missing sensor readings, and aggregate hourly footfall counts by sensor location. Save to a SQL database (SQLite). (2) In SQL: Write a query using window functions (AVG() OVER, ROW_NUMBER()) to calculate the 7-day rolling average of hourly footfall for each sensor. Identify anomaly_hours where current hourly count deviates by more than 2 standard deviations from the rolling average. (3) Export results showing sensor_id, timestamp, actual_count, rolling_avg_7day, anomaly_flag, and anomaly_severity. Expected output: 100-500 flagged anomaly records representing unusual pedestrian patterns._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-11-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
