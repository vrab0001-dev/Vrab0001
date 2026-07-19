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
| 📅 Last Sync | 2026-07-19 11:23 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Ranking
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) 30-day rolling average closing price for each stock, (2) rank each stock by its 30-day rolling average within each date window, and (3) identify the top 5 and bottom 5 performers. Use ROW_NUMBER() and LAG() to show price change from 30 days prior. Output should include: stock_symbol, date, closing_price, rolling_avg_30d, rank_within_date, and pct_change_30d._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains messy collision records with missing values, inconsistent date formats, and categorical errors). Write a Python/pandas script to: (1) parse and standardize crash_date to YYYY-MM-DD format, (2) handle missing values in severity and crash_type columns using appropriate imputation or removal, (3) clean location data by removing duplicates and standardizing suburb names to title case, (4) filter crashes from the last 5 years only, and (5) export a cleaned CSV with row counts before/after cleaning logged to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-19.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a Python + SQL pipeline using Bureau of Meteorology weather observations: (1) In Python, load raw weather CSV (temperature, rainfall, humidity, date, station_id), clean missing values using forward-fill for time series data, and export to a local SQLite database. (2) In SQL, create a CTE to calculate 30-year climate normals (mean temp, mean rainfall) by station and month, then use window functions (ROW_NUMBER, RANK) to identify anomalous readings where current temperature deviates >2 standard deviations from the normal for that station/month. (3) Output the top 20 anomalies ranked by severity with: station_id, date, recorded_temp, normal_temp, deviation_std, and anomaly_rank. Document the data quality issues found in step 1._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-07-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
