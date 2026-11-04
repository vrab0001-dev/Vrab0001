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
| 📅 Last Sync | 2026-11-04 14:40 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 20-day moving average of closing price for each stock, (2) the rank of stocks by daily percentage change within each date, and (3) identify stocks that reached a new 52-week high on each trading day. Use ROW_NUMBER() OVER (PARTITION BY stock_code ORDER BY date) and LAG() to compute daily % change. Filter for dates in 2026 only. Return stock_code, date, close_price, moving_avg_20d, daily_pct_change_rank, and is_52week_high flag. Expected output: ~500-1000 rows showing momentum leaders each week._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains crash details, injury severity, vehicle types, road conditions). Write a Python/pandas script to: (1) handle missing values in Latitude/Longitude by filling with suburb centroids, (2) standardise Speed Zone values (remove typos, convert to numeric), (3) categorise crashes by severity (No Injury, Other Injury, Serious Injury, Fatality), (4) aggregate crashes by Local Government Area and severity, (5) export cleaned data to CSV with summary statistics. Include data quality checks (e.g., crashes per LGA, injury distribution). Expected output: cleaned dataset + summary CSV showing top 10 LGAs by crash count and injury breakdown._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-04.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline: (1) Extract Australian Weather observations data (Bureau of Meteorology / Kaggle) covering multiple stations for 2024-2026. (2) In Python/pandas: load the CSV, clean temperature/rainfall/humidity columns (handle nulls, outliers), calculate rolling 30-day averages by station, and export to a temporary SQLite database. (3) In SQL: create a CTE to compute z-scores for each observation (deviation from station's historical mean), use window functions to identify consecutive days of anomalies (temp > 2 std dev), and rank stations by anomaly frequency. (4) Export results showing station_name, anomaly_date, temperature, z_score, anomaly_duration_days. Expected output: SQL query results identifying heatwave periods and anomaly hotspots across Australia._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle jsphyg)`
  📁 Submit as: `quest3_2026-11-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
