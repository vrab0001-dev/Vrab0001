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
| 📅 Last Sync | 2026-04-12 11:20 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility & Momentum Tracker
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation (volatility) and 14-day momentum (price change) for each stock. Use window functions ROW_NUMBER() and LAG() to identify the top 5 most volatile stocks and their price trends over the last quarter. Return: stock_code, current_price, volatility_30day, momentum_14day, rank_by_volatility, ordered by volatility descending. Use a CTE to stage the price movements before calculating window functions._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Zone Mapper
  _Download NSW Road Crash Data (contains collision records with location, severity, conditions). Clean the dataset by: (1) removing rows with missing latitude/longitude, (2) standardising speed_zone values (convert text variations to consistent format), (3) parsing crash_date into datetime and extracting hour_of_day, (4) creating a severity_category column mapping injury_count to 'minor', 'moderate', 'severe'. Export a cleaned CSV. Then identify the top 10 postcodes with highest crash frequency and average severity score. Output: postcode, crash_count, avg_severity, sorted by crash_count descending._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-12.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Part 1 (Python): Load Australian Bureau of Meteorology weather observations (temperature, rainfall, wind speed across multiple stations). Clean missing values using forward-fill method. Calculate monthly aggregates: mean_temp, total_rainfall, max_wind_speed per station. Export to CSV. Part 2 (SQL): Load the cleaned CSV into a database. Write a query using CTEs and window functions to: (1) calculate the 5-year rolling average temperature per station, (2) identify months where temp exceeded the rolling avg by >2 std devs (anomalies), (3) rank anomalies by severity within each station. Return: station_name, month, temperature, anomaly_flag, severity_rank. Order by station and severity_rank descending._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-04-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
