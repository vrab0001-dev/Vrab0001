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
| 📅 Last Sync | 2026-06-25 12:03 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum with Window Functions
  _Using ASX 200 historical price data, calculate the daily price momentum for each stock. Create a CTE that ranks stocks by their 7-day average return (using LAG to compare current close to 7 days ago), then identify the top 5 and bottom 5 performers on 2026-06-25. Output should include: stock symbol, date, close price, 7-day return %, and rank within top/bottom performers. Use ROW_NUMBER() PARTITION BY symbol to ensure correct lag calculation across date ranges._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Classification
  _Download NSW Road Crash Data (raw CSV format). Clean the dataset by: (1) removing rows with >30% missing values, (2) standardising date columns to YYYY-MM-DD format, (3) creating a new 'severity_score' column (0-10 scale) based on injury count and vehicle damage rating, (4) detecting and flagging duplicate crash records using crash location + timestamp, (5) exporting cleaned data to a new CSV with a data quality report (rows removed, missing % per column, duplicates found). Use pandas and provide summary statistics._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-25.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: Python ETL + SQL Analytics
  _Part A (Python): Extract Australian Weather observations data (Bureau of Meteorology / Kaggle). Clean temperature, rainfall, and humidity columns (handle missing values, validate ranges: temp -10 to 50°C, rainfall 0-500mm, humidity 0-100%). Load cleaned data into a local SQLite database with tables: weather_observations (station_id, date, temperature, rainfall, humidity, pressure). Part B (SQL): Query the database to calculate: (1) 30-day rolling average temperature per station using window functions, (2) stations with rainfall in top 10% for their climate zone (use PERCENT_RANK()), (3) CTE identifying heatwave events (3+ consecutive days >35°C). Output results as CSV for each query._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
