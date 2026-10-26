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
| 📅 Last Sync | 2026-10-26 13:04 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Performance Rankings with Rolling Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 20-day and 50-day rolling average closing price for each stock, (2) Rank stocks by their current price relative to the 20-day average (highest outperformers first), (3) Use ROW_NUMBER to identify the top 3 performers in each sector for the most recent date in the dataset. Return columns: ticker, sector, date, close_price, ma_20, ma_50, performance_rank, sector_rank. Use a CTE to organize the window function logic._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-26.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning & Temperature Anomaly Detection
  _Download or load the Australian Weather observations dataset (Bureau of Meteorology). Write a Python/pandas script to: (1) Handle missing values in temperature and rainfall columns using appropriate imputation strategies, (2) Detect and flag outliers in daily maximum temperature using IQR method, (3) Create new columns: temperature_anomaly (difference from 30-year average for that location/month), rainfall_category (low/medium/high based on percentiles), (4) Export cleaned data to CSV with a timestamp. Document your data quality checks and decisions in comments._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest2_2026-10-26.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: Python ETL + SQL Analytics
  _Using NSW Road Crash Data (data.nsw.gov.au): (1) Write a Python script to extract crash records, clean location coordinates (handle nulls/invalid entries), standardize crash type and severity codes, and load into a local SQLite database. (2) Write SQL queries to analyze: top 10 crash locations by frequency, average severity score by day-of-week and hour-of-day (use CASE statements and GROUP BY), identify crash patterns using a CTE that flags high-risk corridors (>50 crashes in 12 months). (3) Export a summary report showing geographic hotspots and temporal patterns. Include error handling in Python and document data transformations._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-10-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
