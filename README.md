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
| 📅 Last Sync | 2026-09-02 11:43 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Analysis with Window Functions
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify momentum shifts. Use window functions (ROW_NUMBER, LAG) to rank stocks by their price change momentum within each trading week. Create a CTE that identifies the top 5 stocks with the highest positive momentum and bottom 5 with negative momentum for the most recent week in your dataset. Return: stock_code, current_price, 20day_moving_avg, momentum_rank, price_change_pct, and momentum_category (bullish/bearish). Order by momentum_rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-02.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Severity Pipeline
  _Download NSW Road Crash Data (data.nsw.gov.au). Write a Python/pandas script that: (1) loads the CSV and identifies missing values in crash_severity, injury_type, and vehicle_type columns; (2) standardizes injury severity categories (handle typos, case inconsistencies); (3) removes duplicate crash records based on crash_id and timestamp; (4) creates a new column crash_hour extracted from crash_time; (5) filters for crashes in the last 12 months; (6) exports a cleaned CSV with columns: crash_id, crash_date, crash_hour, suburb, injury_type, severity_category, vehicle_count. Print data quality metrics: rows removed, missing values before/after, duplicate count._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-02.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Coral Bleaching Event Detection Pipeline
  _Combine Python and SQL to detect coral bleaching risk periods. (1) In Python: fetch or load Great Barrier Reef monitoring data (temperature, pH, bleaching_index by reef_site and date from AIMS or Kaggle). Clean the dataset: handle missing temperature readings using interpolation, standardize date formats, calculate weekly anomalies (temp deviation from 5-year mean). Export to CSV. (2) In SQL: load the cleaned data into a table. Write a query using CTEs and window functions to: identify reef_sites where temperature exceeded historical mean + 2 standard deviations for 3+ consecutive weeks; rank bleaching events by severity (max_temp_anomaly * duration); calculate the date range of each event. Return: reef_site, event_start_date, event_end_date, max_temp_anomaly, event_duration_weeks, severity_rank. Filter for events in 2024-2025._
  📦 Dataset: `Great Barrier Reef Monitoring Data — AIMS (Australian Institute of Marine Science) or Kaggle`
  📁 Submit as: `quest3_2026-09-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
