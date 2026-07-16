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
| 📅 Last Sync | 2026-07-16 11:22 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking
  _Using ASX 200 historical price data, write a query with window functions to rank stocks by their 30-day price momentum. Calculate the percentage change from 30 days ago to the most recent close price for each stock. Use ROW_NUMBER() to rank stocks from best to worst momentum, and LAG() to retrieve the price from 30 days prior. Include columns: stock_symbol, current_price, price_30_days_ago, momentum_percentage, momentum_rank. Filter for the top 20 movers. Expected output: A sorted table showing which ASX 200 stocks have gained the most and least over the past month._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (2020-2025) and build a pandas data cleaning script. Tasks: (1) Remove or impute null values in crash_severity, crash_type, and accident_date columns; (2) Standardise date formats to YYYY-MM-DD; (3) Convert crash_severity to a categorical type with ordered levels (Minor, Moderate, Severe, Fatal); (4) Create a new column 'crash_hour' by extracting hour from accident_datetime; (5) Remove duplicate rows based on crash_id; (6) Export cleaned data to a CSV file. Expected output: A cleaned CSV with 5+ new/transformed columns and a data quality report showing % null values before/after, row count reduction, and data type conversions._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-16.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Weather Patterns ETL & Analysis
  _Build a mini ETL pipeline: (1) Download Australian Weather observations data (Bureau of Meteorology dataset via Kaggle); (2) Use Python/pandas to clean the data: standardise column names (lowercase, snake_case), handle missing temperature/rainfall values via forward-fill, and group daily observations by station_id and date; (3) Load the cleaned data into a SQLite database with two tables: weather_stations (station_id, station_name, state) and daily_weather (date, station_id, avg_temp, max_temp, rainfall_mm); (4) Write a SQL query using CTEs to find the top 10 stations with the highest average rainfall in the last 90 days, ranked by rainfall_total. Include a secondary ranking by temperature_variance (max_temp - min_temp) within each station. Expected output: A Python script that performs the ETL, a SQLite database file, and a results CSV showing the top 10 rainiest stations with their average conditions._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
