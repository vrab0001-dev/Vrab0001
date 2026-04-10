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
| 📅 Last Sync | 2026-04-10 11:16 AEDT |

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
  _Using ASX 200 historical price data, calculate the 20-day moving average and price momentum (% change from 20 days ago) for each stock using window functions. Use LAG() to access previous prices, then calculate ROW_NUMBER() partitioned by stock symbol ordered by date. Filter to only stocks where the current price is in the top 10% of their 52-week range. Output: stock_symbol, date, close_price, moving_avg_20day, momentum_pct, 52week_rank. Order by momentum_pct DESC._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains raw incident records with missing values, inconsistent location formats, and mixed data types). Clean the dataset by: (1) handling null values in injury_type and crash_severity columns, (2) standardising postcode formats, (3) converting date columns to datetime, (4) removing duplicate records based on crash_id and date, (5) creating a new column 'time_of_day' categorising crash_hour into 'morning' (6-12), 'afternoon' (12-18), 'evening' (18-24), 'night' (0-6). Export cleaned data to CSV. Bonus: create a summary showing crash count by local government area and time_of_day._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-10.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Trends: SQL + Python Pipeline
  _Build a data engineering pipeline: (1) Extract Melbourne pedestrian counting sensor data (CSV from Melbourne Open Data Portal). (2) Use Python/pandas to load, clean (handle sensor outages/null counts), and aggregate hourly counts to daily totals by sensor_id and date. (3) Write cleaned data to a local SQLite database. (4) Query using SQL to find the top 5 sensors by average daily foot traffic, calculate day-over-day growth rate using LAG() window function, and identify anomalies (days where traffic is >2 standard deviations from the 30-day rolling mean). Output final results to CSV showing sensor_id, date, daily_count, growth_rate_pct, is_anomaly._
  📦 Dataset: `Melbourne Pedestrian Counting Sensors — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-04-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
