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
| 📅 Last Sync | 2026-03-14 16:01 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using the ASX 200 historical stock prices dataset, write a SQL query with window functions to: (1) Calculate the 5-day moving average of closing prices for each stock ticker, (2) Rank stocks by their price momentum (difference between current close and 5-day MA) within each trading week, (3) Identify the top 10 stocks with the strongest upward momentum in the most recent week. Use ROW_NUMBER() or RANK() and LAG() window functions. Expected output: ticker, date, closing_price, moving_avg_5day, momentum_rank, momentum_value. Order by momentum_rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring Pipeline
  _Download NSW Road Crash Data (from data.nsw.gov.au). Write a Python script using pandas to: (1) Load the crash CSV and handle missing values in crash_type, severity, and location fields using appropriate imputation or removal, (2) Standardise location data by removing whitespace and converting to title case, (3) Create a risk_score column (0-100) based on severity (fatal=100, serious injury=75, other injury=50, non-injury=25) weighted by number of vehicles involved, (4) Export the cleaned dataset to a new CSV with only relevant columns: crash_id, date, location, severity, vehicles_involved, risk_score. Add logging to track rows removed and transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-14.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection & Reporting System
  _Using the Australian Weather Observations dataset (Bureau of Meteorology via Kaggle), build an end-to-end pipeline: (1) In Python/pandas: load daily temperature and rainfall data, clean missing values, and calculate rolling 30-day averages for each station, (2) Identify anomalies where daily temperature deviates >2 standard deviations from the 30-day rolling mean, (3) Export anomalies to a staging CSV with columns: station_id, date, temperature, anomaly_flag, deviation_magnitude. (4) In SQL: create a table from the staging CSV, then write a query to rank anomalies by severity per station-month combination using PARTITION BY, and generate a summary report: station_id, anomaly_month, anomaly_count, max_deviation, avg_deviation. (5) Return top 15 anomaly hotspots across Australia._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg dataset)`
  📁 Submit as: `quest3_2026-03-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
