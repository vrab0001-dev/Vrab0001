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
| 📅 Last Sync | 2026-04-24 11:24 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum Rankings
  _Using ASX 200 historical price data, write a SQL query with window functions to rank stocks by their 30-day price momentum. Calculate the percentage change from 30 days ago to today for each stock using LAG() window function, then rank them with RANK() OVER (ORDER BY momentum DESC). Include columns: stock_symbol, current_price, price_30_days_ago, momentum_percentage, momentum_rank. Filter to show only top 20 gainers and bottom 20 losers. Use a CTE to calculate the 30-day lookback first._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data and build a Python pandas script to clean and standardise it for analysis. Tasks: (1) Handle missing values in crash location, severity, and vehicle type columns (use appropriate strategies: drop, forward-fill, or mode imputation). (2) Standardise date formats to ISO 8601. (3) Create a new column 'time_of_day' by binning hours into 'night', 'morning', 'afternoon', 'evening'. (4) Remove duplicate crash records based on date, location, and time. (5) Export the cleaned dataset as cleaned_crashes.csv. Include data quality report showing original vs cleaned row counts and missing value statistics._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-24.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Python ETL to SQL Analytics
  _Build an end-to-end pipeline: (1) Use Python with pandas to read Australian Bureau of Meteorology weather observation data (or Kaggle's Australian Weather dataset). Clean temperature, rainfall, and humidity columns (handle missing values, outliers, unit conversions if needed). Aggregate daily observations by weather station into daily_weather.csv with columns: station_id, date, avg_temperature, total_rainfall, avg_humidity. (2) Load the cleaned CSV into a SQL database (SQLite or PostgreSQL). (3) Write a SQL query to find the top 10 weather stations with the highest average temperature variance (std dev) over the past year, and identify the month with the greatest temperature swings for each station. Use window functions and CTEs. Output: station_name, avg_variance, peak_variance_month._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-04-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
