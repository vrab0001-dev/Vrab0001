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
| 📅 Last Sync | 2026-06-06 11:57 AEDT |

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
  _Using ASX 200 historical stock price data, calculate a 20-day moving average and identify stocks that have gained >10% over the last 30 days. Use window functions (ROW_NUMBER, LAG) to rank stocks by momentum within each sector. Return the top 5 performers per sector with columns: ticker, sector, current_price, price_30_days_ago, pct_gain, moving_avg_20day, rank_in_sector. Use a CTE to calculate the 30-day price change first._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleanup and Risk Scoring
  _Load NSW Road Crash Data (CSV format) and perform data cleaning: handle missing values in injury_type and crash_severity columns, standardise suburb names to title case, remove duplicate crash records by crash_id, and convert date columns to datetime format. Then engineer a risk_score feature: multiply severity_level (1-5 scale) by number_of_vehicles involved. Export the cleaned dataset to a new CSV with columns: crash_id, date, suburb, severity, injury_count, vehicle_count, risk_score. Print summary statistics showing crashes by severity and top 10 high-risk suburbs._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-06.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Download Australian Bureau of Meteorology weather observations (temperature, rainfall, wind speed) for the last 12 months. In Python: load the CSV, clean missing values using forward-fill, and aggregate daily observations to monthly averages by station. Calculate z-scores for each metric to identify anomalies (|z-score| > 2). Export the aggregated and scored data to a SQLite database. In SQL: query the database to find the top 10 station-month combinations with the highest temperature anomalies, calculate a monthly anomaly_count per station, and rank stations by overall weather instability. Return: station_name, month, avg_temp, temp_anomaly_zscore, anomaly_count, instability_rank. Present findings as a ranked table._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
