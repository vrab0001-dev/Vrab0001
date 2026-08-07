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
| 📅 Last Sync | 2026-08-07 12:00 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) a 20-day moving average of closing price for each stock, (2) the rank of each stock by daily percentage change within each trading date, and (3) the cumulative return from the first day in the dataset for each stock. Use CTEs to structure the query logically. Return the top 10 stocks by cumulative return over the entire period, showing date, stock symbol, closing price, 20-day moving average, daily rank, and cumulative return percentage._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Calculation
  _Download the NSW Road Crash Data (CSV format). Write a Python/pandas script to: (1) handle missing values in severity, vehicle type, and location columns, (2) standardize date/time formats, (3) remove duplicate crash records based on a composite key (date, location, vehicle count), (4) create a new 'crash_risk_score' column (1-10 scale) based on severity level and number of vehicles involved, (5) generate summary statistics by local government area (LGA), and (6) export a cleaned dataset with new columns to a new CSV file. Document your data quality decisions in code comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-07.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using Australian Bureau of Meteorology weather observations dataset (available on Kaggle), build an end-to-end pipeline: (1) In Python/pandas, load the CSV, clean temperature and rainfall columns (handle missing values, outliers, unit conversions if needed), and calculate monthly averages by station. (2) Export cleaned monthly aggregates to a new CSV. (3) In SQL, load this CSV into a database table, then write a query using window functions (LAG, ROW_NUMBER) to identify: (a) months where temperature exceeded the 12-month rolling average by >2°C for that station, (b) rank stations by deviation severity, and (c) flag potential anomalies. Return results showing station name, month, temperature, rolling average, and anomaly flag. Explain your anomaly detection logic in a comment block._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-08-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
