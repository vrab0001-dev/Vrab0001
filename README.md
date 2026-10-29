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
| 📅 Last Sync | 2026-10-29 14:12 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns & Ranking
  _Using ASX 200 historical price data, calculate the daily percentage return for each stock. Use a window function (ROW_NUMBER or RANK) to rank stocks by return within each trading date, partitioned by date. Then use a CTE to identify the top 5 and bottom 5 performers for each date. Return: date, stock_symbol, close_price, daily_return_pct, rank_within_date. Filter for the last 30 trading days only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash data (CSV format). Clean the dataset by: (1) removing rows with missing critical fields (crash_date, latitude, longitude, severity); (2) standardising date formats to YYYY-MM-DD; (3) handling inconsistent severity labels (map variations to standard categories: Fatal, Serious Injury, Other Injury); (4) removing duplicate records based on crash_id; (5) calculating a risk_score (1-10) based on severity and number of vehicles involved. Export the cleaned dataset to a new CSV with all original columns plus risk_score. Provide a data quality report (rows removed, % missing values before/after)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-29.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies: Python ETL → SQL Analysis
  _Step 1 (Python): Download Australian Weather observations dataset (temperature, rainfall, humidity by station/date). Use pandas to: clean missing values, convert all temperatures to Celsius, filter for the last 12 months, calculate rolling 7-day average temperature and total rainfall by station. Export to CSV. Step 2 (SQL): Load the cleaned CSV into a database. Write a query using window functions (LAG, LEAD) to identify temperature anomalies: flag any day where the temperature deviation from the 7-day rolling average exceeds 2 standard deviations. Return: station_name, date, temp, rolling_avg, deviation_std, is_anomaly (boolean). Include the top 10 stations with the most anomalies._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
