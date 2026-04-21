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
| 📅 Last Sync | 2026-04-21 11:20 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Top Movers: Window Functions Analysis
  _Using ASX 200 historical prices data, write a SQL query with window functions to identify the top 5 performing stocks by percentage gain over the last 30 days. Use ROW_NUMBER() to rank stocks within each date, LAG() to calculate day-over-day changes, and a CTE to filter the final results. Your output should include: stock symbol, current price, price 30 days ago, percentage gain, and rank. Order by percentage gain descending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data: Cleaning and Severity Classification
  _Download NSW Road Crash Data (injury type, speed zone, weather conditions). Use pandas to: (1) handle missing values in weather_condition and speed_zone columns (fill with 'Unknown'), (2) standardise date format to YYYY-MM-DD, (3) create a new 'severity_score' column based on injury_type (Fatal=3, Serious=2, Other=1), (4) remove duplicates based on crash_id, (5) export cleaned data to a new CSV file with filename 'nsw_crashes_cleaned_YYYYMMDD.csv' using today's date. Count and report how many rows were removed in each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-21.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies: SQL + Python ETL Pipeline
  _Create an end-to-end ETL pipeline: (1) Use Python/pandas to load Australian Weather observations (temperature, rainfall, pressure data), clean it (handle missing values, convert units if needed), and export to a CSV. (2) Load this cleaned CSV into a SQL database or create an in-memory SQLite table. (3) Write a SQL query using CTEs and window functions to: identify stations with temperature anomalies (values >2 standard deviations from 30-day rolling average), calculate the anomaly magnitude, and rank anomalies by severity. (4) Export results showing: station_id, date, temperature, rolling_avg, anomaly_magnitude, and rank. Provide both the Python script and SQL query._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-04-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
