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
| 📅 Last Sync | 2026-06-27 11:59 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility with Window Functions
  _Using ASX 200 historical price data, calculate the 20-day rolling standard deviation of daily returns for the top 5 most volatile stocks. Use window functions (ROW_NUMBER, LAG) to compute daily percentage change, then a CTE to calculate rolling volatility. Return stock symbol, date, closing price, daily return %, and 20-day rolling volatility. Order by volatility descending, then by date. Expected output: 5 stocks × ~20 rows each showing volatility trends._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data from data.nsw.gov.au. Write a Python/pandas script to: (1) clean missing values in crash severity and location fields, (2) standardise date formats, (3) remove duplicate crash records, (4) create a new column 'hour_of_day' from timestamp, (5) aggregate crashes by hour_of_day and severity level, (6) export cleaned dataset to CSV and summary statistics to a second CSV. Handle edge cases like null severity codes. Expected output: two CSV files (cleaned crashes + hourly severity summary) with data quality report printed to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-27.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic: Python ETL + SQL Analytics
  _Part A (Python): Download Melbourne pedestrian counting data from Melbourne Open Data Portal. Write a Python script to load the JSON/CSV, clean timestamps, handle missing sensor readings, and load into a SQLite database table 'pedestrian_counts' with columns: sensor_id, sensor_name, date, hour, count. Part B (SQL): Query the database to find: (1) top 5 sensors by total foot traffic over the full dataset period, (2) hourly traffic patterns (average count by hour of day across all sensors), (3) a CTE-based query identifying 'peak hours' (hours where avg traffic > 90th percentile) and rank sensors by peak hour traffic. Export SQL results to CSV. Expected deliverable: populated SQLite DB + 3 analytical CSV outputs._
  📦 Dataset: `Melbourne Pedestrian Counts — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-06-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
