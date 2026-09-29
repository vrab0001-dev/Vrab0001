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
| 📅 Last Sync | 2026-09-29 13:02 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) 20-day moving average of closing price for each stock, (2) ROW_NUMBER ranking stocks by daily volume within each date, (3) LAG function to calculate day-over-day price change percentage. Filter for the top 10 stocks by average daily volume in the last 90 days. Return columns: stock_code, date, close_price, moving_avg_20day, volume_rank_by_date, price_change_pct. Use a CTE to stage the moving averages before final selection._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Automation
  _Download NSW Road Crash Data (CSV format). Clean the dataset by: (1) handling missing values in crash severity and road type columns (document your strategy), (2) standardising date formats and extracting year, month, day_of_week as separate columns, (3) removing duplicate crash records based on crash ID, (4) creating a new 'risk_score' column (1-10) based on severity level and number of vehicles involved. Use pandas to automate this and export a cleaned CSV with columns: crash_id, date, year, month, day_of_week, location, severity, vehicle_count, risk_score. Include a summary report showing % of rows removed and any imputation decisions made._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-29.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Python ETL + SQL Analytics
  _Part A (Python): Download Australian Weather Observations dataset (Bureau of Meteorology historical data via Kaggle). Write a Python/pandas script to: extract daily min/max temperatures, rainfall, and wind speed for major cities (Sydney, Melbourne, Brisbane, Perth). Clean missing values using forward-fill for weather readings. Aggregate to weekly averages per city. Output to a SQLite database (weather.db) with a table named 'weekly_weather' (columns: city, week_start_date, avg_temp_min, avg_temp_max, total_rainfall, avg_wind_speed). Part B (SQL): Query the SQLite database to identify: (1) which city had the highest temperature variance (max - min) over the past 12 weeks using window functions, (2) weeks where rainfall exceeded the city's 90th percentile threshold (use PERCENT_RANK), (3) a CTE to rank cities by average wind speed and identify outlier weeks. Return: city, metric_name, metric_value._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg/australian-weather-observations)`
  📁 Submit as: `quest3_2026-09-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
