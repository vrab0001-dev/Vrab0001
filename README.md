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
| 📅 Last Sync | 2026-05-19 12:03 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate a 20-day moving average of closing prices for each stock symbol, (2) Rank stocks by their price momentum (current price vs. 20-day MA) within each trading week, (3) Use LAG to find the day-over-day percentage change, (4) Filter only stocks where the current price is >5% above their 20-day MA. Return stock symbol, trading date, close price, 20-day MA, momentum rank, and daily % change. Order by trading date DESC and momentum rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Severity Classification
  _Download NSW Road Crash Data (accident-level records). Create a Python/pandas script to: (1) Load the CSV and inspect for missing values, duplicates, and data type mismatches, (2) Clean the 'crash_date' column and extract year, month, day_of_week, (3) Handle missing injury severity codes by imputing with the mode for that crash type, (4) Create a new 'severity_category' column mapping injury counts to labels (Fatal, Serious, Other), (5) Remove rows with incomplete location data (null latitude/longitude), (6) Export cleaned data to a new CSV with columns: crash_id, crash_date, year, month, day_of_week, severity_category, location_suburb, latitude, longitude. Print summary statistics: total crashes, crashes by severity, missing data counts before/after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-19.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Pipeline: Extract, Transform, Load
  _Build an end-to-end data engineering pipeline using Python and SQL: (1) In Python, download Australian Weather Observations data (Bureau of Meteorology / Kaggle jsphyg dataset) and clean it: standardize temperature/rainfall columns, handle missing values via forward-fill, remove duplicate timestamps per station, (2) Calculate rolling 30-day mean temperature and total rainfall per weather station using pandas, (3) Identify temperature anomalies as values >2 standard deviations from the 30-day mean, (4) Export cleaned data and anomalies to CSV, then load both into SQLite (or your chosen database), (5) Write a SQL query to find the top 10 weather stations with highest anomaly frequency in the past 6 months, including station name, state, anomaly count, and average anomaly magnitude. Return results sorted by anomaly count DESC._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
