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
| 📅 Last Sync | 2026-09-11 11:48 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling average price for each stock and rank stocks by their current price relative to their 30-day average (best performers first). Use window functions ROW_NUMBER() and AVG() OVER() to identify the top 10 stocks with the highest price-to-moving-average ratio on the most recent date in the dataset. Include columns: stock_code, current_price, moving_avg_30d, ratio, rank. Filter to include only stocks with at least 30 days of trading data._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleanup and Aggregation Pipeline
  _Download or load the NSW Road Crash Data (focus on the crash/incident records). Build a Python script that: (1) handles missing values in key columns (crash_type, severity, location), (2) standardises date formats to YYYY-MM-DD, (3) cleans the location field by removing extra whitespace and converting to title case, (4) removes duplicate rows based on crash_id, (5) exports a cleaned CSV file. Then create a summary report showing crash counts by severity level and top 5 crash types. Save the cleaned data and summary as separate CSV files._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-11.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Create an end-to-end pipeline: (1) Use Python/pandas to load Bureau of Meteorology weather observations data, clean temperature and rainfall columns (handle missing values, convert units if needed), and calculate monthly averages for 3 Australian cities. (2) Export the cleaned monthly aggregates to a CSV file. (3) Write a SQL query against this CSV (load it into a temporary table or use DuckDB/SQLite) to identify months where temperature was more than 2 standard deviations above the city's historical mean (anomalies). Return: city, month, avg_temperature, historical_mean, std_dev, anomaly_flag. Your Python script should orchestrate both steps and log the number of anomalies detected per city._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle jsphyg) or AIMS weather station data`
  📁 Submit as: `quest3_2026-09-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
