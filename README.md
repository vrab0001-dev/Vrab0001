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
| 📅 Last Sync | 2026-10-28 13:50 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Average Momentum
  _Using the ASX 200 historical prices dataset, calculate a 20-day rolling average for the top 5 most volatile stocks (by standard deviation of daily returns). Use window functions to compute the rolling average and rank stocks by volatility. Return: stock symbol, date, closing price, 20-day rolling average, volatility rank, and row number partitioned by stock ordered by date. Filter results to show only the last 10 trading days for each stock._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-10-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data and perform the following: (1) Clean missing values in crash severity, accident type, and location columns using appropriate strategies (mode for categorical, forward-fill for temporal). (2) Create a new column 'crash_cluster' grouping crashes into geographic regions using postcode ranges. (3) Generate a summary CSV with columns: region, total_crashes, fatalities, serious_injuries, most_common_accident_type, and average_vehicles_involved. (4) Validate data integrity by asserting no nulls remain in critical columns._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-28.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Pipeline
  _Build a data pipeline combining Python and SQL: (1) In Python, download Bureau of Meteorology weather observations (or use Kaggle Australian Weather dataset), clean temperature and rainfall columns, and load into a local SQLite database. (2) In SQL, use CTEs and window functions to identify temperature anomalies: calculate the 30-year normal (average) temperature for each month and location, then flag days where actual temperature deviates >2 standard deviations from the norm. (3) Export results showing: station_id, date, observed_temp, normal_temp, deviation_std, is_anomaly. (4) Create a Python summary script that reads the SQL output and generates a report of the top 10 most anomalous days across all stations._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-10-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
