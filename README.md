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
| 📅 Last Sync | 2026-09-01 12:22 AEDT |

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
  _Using ASX 200 historical prices dataset, write a query with window functions to rank stocks by 30-day price momentum within each sector. Calculate the percentage change from 30 days ago using LAG(), partition by sector, order by percentage change descending. Include columns: stock_symbol, sector, current_price, price_30_days_ago, pct_change, and momentum_rank. Filter for only the top 5 momentum gainers per sector on the most recent date in the dataset._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (CSV format). Write a Python script using pandas to: (1) handle missing values in the Crash Type and Weather Condition columns by filling with 'Unknown'; (2) standardise date formats in the Crash Date column to YYYY-MM-DD; (3) filter for crashes between 2020-2024; (4) create a new column 'Severity' categorising crashes as 'Fatal', 'Serious Injury', or 'Other' based on Injury Type; (5) aggregate crashes by Local Government Area (LGA) and Severity, counting incidents. Output a cleaned CSV with LGA, Severity, and crash_count columns, sorted by crash_count descending._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-01.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Bureau of Meteorology Integration
  _Using Australian Weather observations dataset (Bureau of Meteorology / Kaggle), write a Python script to: (1) load weather CSV data (temperature, rainfall, humidity by station and date); (2) clean the data—remove duplicates, handle missing values for rainfall (fill with 0), standardise temperature to Celsius; (3) create a pandas DataFrame with station_id, date, avg_temp, total_rainfall, and humidity columns; (4) export to a local SQLite database with a 'weather_stations' table. Then write a SQL query against that database to find the top 5 stations with the highest average temperature in the most recent month, and calculate a 7-day rolling average of rainfall for each station. Output: station_name, avg_temp_month, rolling_avg_rainfall_7day._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-09-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
