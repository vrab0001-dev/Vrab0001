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
| 📅 Last Sync | 2026-07-31 11:29 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Rankings with Window Functions
  _Using ASX 200 historical price data, calculate a 20-day rolling average price for each stock symbol. Then rank stocks by their current price relative to this moving average (current price / MA20) in descending order. Use ROW_NUMBER() to assign a unique rank within each date partition, and LAG() to compare today's price against yesterday's price. Filter for the last 10 trading days and show: symbol, date, close_price, ma20, price_ratio, daily_change, and row_rank. This reveals momentum stocks outperforming their short-term trend._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-31.sql`
- [ ] 🐍 **Python Quest:** Clean & Aggregate NSW Road Crash Data
  _Download NSW Road Crash Data (2020–2025) and perform the following: (1) Handle missing values in injury severity and crash type columns by forward-filling or dropping as appropriate. (2) Standardise date formats to YYYY-MM-DD. (3) Remove duplicate crash records based on crash ID. (4) Create a new column 'month_year' from the date. (5) Aggregate crashes by local government area (LGA) and month, counting total crashes and summing fatalities. (6) Export cleaned data to a new CSV with columns: lga, month_year, crash_count, fatalities. Script should be reproducible and include comments explaining each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-31.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis Pipeline
  _End-to-end task: (1) Use Python/pandas to load Melbourne pedestrian counting sensor data, resample hourly counts to daily totals, and clean outliers (remove days with counts > 3 standard deviations from mean). Export cleaned data to a staging CSV. (2) Load this CSV into a SQL database (SQLite or your choice). (3) Write a SQL query using CTEs to calculate: for each sensor location, the average daily foot traffic, the day of week with highest traffic, and a 7-day rolling average trend. (4) Return results ordered by average traffic (descending) and save to a final output file. This simulates a real data pipeline from raw source → cleaned staging → analytical queries._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-07-31.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
