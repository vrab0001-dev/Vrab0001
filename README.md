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
| 📅 Last Sync | 2026-09-28 12:17 AEDT |

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
  _Using ASX 200 historical stock price data, write a SQL query with window functions to calculate: (1) a 20-day moving average of closing prices for each stock, (2) the percentage change from the previous day's close using LAG(), (3) a rank of stocks by daily percentage gain within each date partition, and (4) identify the top 5 stocks with the highest cumulative gains over the entire dataset using a CTE. Output should show stock_code, date, close_price, moving_avg_20day, pct_change_prev_day, daily_rank, and cumulative_gain. Filter to only stocks in the top 50 by trading volume._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring Pipeline
  _Download NSW Road Crash Data (contains crash records with location, severity, weather conditions, road type). Build a Python/pandas script to: (1) handle missing values in weather_condition and road_type by imputing with mode per local government area, (2) remove duplicate crash records based on date, location coordinates, and vehicle count, (3) create a crash_severity_score (0-100) combining injury_count, vehicle_count, and speed_zone, (4) filter to crashes in the last 5 years, (5) export clean dataset to CSV with summary statistics printed (mean severity by council, crash count trends by month). Handle edge cases like invalid coordinates and future dates._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-28.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Analysis: Extract, Transform, Load & Report
  _Using AIHW health expenditure data by state and health sector: (1) In Python, download/load the dataset, clean column names, convert currency strings to floats, handle missing values, and pivot the data so each row is state + year with columns for hospital, mental_health, aged_care, primary_care spending. Save cleaned data to a SQLite database in a table called health_spending. (2) In SQL, write a query using CTEs to calculate: year-over-year percentage change in spending by state and sector, identify the top 3 states with fastest-growing mental health spending, and rank sectors by total spending growth across all states over the period. (3) Output a single result set showing state, sector, yoy_pct_change, growth_rank, and a category flag ('High Growth' if >8%, 'Moderate' if 3-8%, 'Low' if <3%)._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-09-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
