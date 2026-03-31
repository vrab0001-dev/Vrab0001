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
| 📅 Last Sync | 2026-03-31 12:14 AEDT |

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
  _Using ASX 200 historical stock price data, calculate the 20-day moving average and identify stocks that have gained more than 10% in the last 30 days. Use window functions (AVG() OVER and ROW_NUMBER() OVER) to rank stocks by their 30-day performance. Return the top 10 performing stocks with columns: stock_symbol, current_price, price_30_days_ago, percentage_gain, moving_average_20day, rank. Use a CTE to structure the moving average calculation separately._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-31.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Generator
  _Download NSW Road Crash Data (contains crash records with location, date, severity, vehicle count). Clean the dataset by: (1) handling missing values in severity and location fields, (2) converting date strings to datetime, (3) removing duplicate crash records, (4) standardising location names. Then create a new column 'risk_score' calculated as (severity_level × vehicle_count) / weather_impact_factor. Export the cleaned dataset to CSV and provide a summary report showing: total crashes cleaned, missing values removed, and top 5 high-risk locations._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-31.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a Python script that (1) reads Australian Bureau of Meteorology weather observations (temperature, rainfall, wind speed by station and date), (2) cleans the data (handle missing values, standardise units), (3) exports to a SQLite database. Then execute SQL queries to: (a) calculate 30-day rolling average temperature by station using window functions, (b) identify anomalies where temperature deviates >2 standard deviations from the 30-day average, (c) rank stations by anomaly frequency. Return results showing: station_name, anomaly_date, temperature, rolling_average, deviation_std, anomaly_rank. Combine Python and SQL results into a final summary CSV report._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-03-31.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
