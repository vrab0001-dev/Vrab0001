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
| 📅 Last Sync | 2026-10-08 14:18 AEDT |

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
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify the top 10 stocks by momentum (current price vs. 20-day MA). Use a CTE to compute the moving average with ROW_NUMBER partitioned by stock ticker, then rank stocks by momentum percentage. Output: ticker, current_price, ma_20_day, momentum_pct, rank. Filter for stocks with at least 20 trading days of data._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleansing Pipeline
  _Load NSW Road Crash Data (CSV format) and build a data cleaning script using pandas. Tasks: (1) Remove duplicate crash records based on crash ID; (2) Handle missing values in 'Speed zone' and 'Weather condition' columns by filling with 'Unknown'; (3) Convert datetime columns to proper datetime format; (4) Create a new column 'severity_category' by binning 'Number of persons injured' into Low (0-1), Medium (2-5), High (6+); (5) Export cleaned dataset as 'nsw_crashes_cleaned.csv'. Validate row counts before/after and document any data quality issues found._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-08.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring ETL Pipeline
  _Build an ETL workflow combining Python and SQL: (1) In Python: Download/load Great Barrier Reef monitoring data (bleaching events, temperature anomalies), clean null values, parse dates, and load into a SQLite database as table 'reef_monitoring'; (2) In SQL: Query the table to find sites with the highest coral bleaching incidents in the last 5 years, calculate YoY temperature anomaly trends using LAG window function, and create a summary report ranking reef zones by health risk (combine bleaching frequency + temp anomaly severity). (3) Export results as CSV showing zone_name, total_bleaching_events, avg_temp_anomaly, health_risk_score, trend_direction. Document any data quality assumptions made during the Python phase._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-10-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
