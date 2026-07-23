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
| 📅 Last Sync | 2026-07-23 11:29 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Moving Averages
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate the 20-day and 50-day moving averages for each stock's closing price, (2) Rank stocks by their current price relative to the 50-day MA (highest performers first), (3) Identify stocks that crossed above their 50-day MA in the last 5 trading days using LAG/LEAD functions. Return columns: stock_code, date, close_price, ma_20, ma_50, performance_rank, days_since_crossover. Order by date DESC, then performance_rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-23.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (from data.nsw.gov.au). Write a Python script using pandas to: (1) Load the CSV and handle missing values in crash severity, vehicle type, and crash location columns, (2) Standardise inconsistent values (e.g. spelling variations in suburb names, mixed case severity levels), (3) Create new features: crash_hour (extracted from datetime), is_weekday (boolean), crash_cluster (group similar locations within 500m using lat/long), (4) Filter out rows with incomplete lat/long data, (5) Export cleaned data to a new CSV with summary statistics printed (total crashes, crashes by severity, top 10 crash suburbs). Code should be well-commented and handle errors gracefully._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-23.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Data Pipeline from CSV to Analytical Dashboard
  _Using Australian Weather Observations dataset (Bureau of Meteorology via Kaggle): (1) Write a Python script to load the CSV, clean temperature and rainfall columns (remove outliers beyond 3 std devs), group by month and station, and aggregate mean temperature, total rainfall, and humidity. Save to a staging SQL-ready CSV. (2) Create a SQL script that imports this staging data into a temp table, then produces a final query showing: for each station and month, the temperature anomaly (actual temp vs 30-year station average), ranking months by rainfall intensity (RANK window function), and a running total of cumulative rainfall across the year (SUM with PARTITION BY station ORDER BY month). Output should include: station_name, month, temp_anomaly, rainfall_rank, cumulative_rainfall. (3) Document the pipeline: which Python libraries you used, any data quality issues found, and why you chose specific SQL window functions._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
