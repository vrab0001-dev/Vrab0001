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
| 📅 Last Sync | 2026-08-12 10:55 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Trading Signals
  _Using the ASX 200 historical prices dataset, create a query that calculates a 10-day and 20-day moving average for each stock using window functions. Then use a CTE to identify stocks where the 10-day MA crossed above the 20-day MA (golden cross signal) on the most recent trading date. Return the stock symbol, date, 10-day MA, 20-day MA, and the price on that date. Order by price change momentum (highest first). This simulates identifying potential buy signals for momentum traders._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas that: (1) loads the CSV file; (2) identifies and handles missing values in critical columns (crash_date, latitude, longitude, severity); (3) removes duplicate crash records based on crash_id; (4) standardises the severity column to title case; (5) converts crash_date to datetime format; (6) filters crashes from the last 3 years only; (7) exports the cleaned dataset to a new CSV file named 'nsw_crashes_cleaned.csv'. Print a summary showing row counts before/after cleaning and missing value counts._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-12.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using the Australian Weather Observations dataset (Bureau of Meteorology via Kaggle), build an end-to-end pipeline: (1) In Python, load the weather CSV and clean it: handle missing values in temperature and rainfall columns, remove invalid readings (e.g., temperature > 60°C), and standardise date formats; (2) Save the cleaned data to a SQLite database; (3) Write SQL queries to calculate monthly average temperature and total rainfall by station using window functions to compute a 3-month rolling average; (4) In Python, query the results and identify stations where the current month's temperature exceeds the rolling 3-month average by more than 2°C (heat anomaly signal); (5) Export anomalies to a CSV report with station name, date, actual temp, rolling avg, and anomaly flag. Expected output: a clean anomaly report suitable for environmental monitoring._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle version by jsphyg)`
  📁 Submit as: `quest3_2026-08-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
