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
| 📅 Last Sync | 2026-09-05 11:44 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Volatility Ranking with Window Functions
  _Using ASX 200 historical prices dataset, calculate the daily price change percentage for each stock. Then use window functions (ROW_NUMBER and LAG) to rank stocks by volatility within each trading day, and identify which stocks had the largest single-day swings. Create a CTE to isolate high-volatility days (>5% swing), then produce a result set showing: Date, Stock Symbol, Daily % Change, Volatility Rank (within day), and whether it was a high-volatility day. Sort by date descending and rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data (CSV format). Write a Python script using pandas that: (1) loads the dataset and identifies missing values in critical columns (Crash Severity, Weather Condition, Road Type); (2) removes or imputes duplicates/nulls appropriately; (3) standardises text fields (uppercase inconsistencies, trim whitespace); (4) creates a new column 'Severity_Score' mapping crash severity to numeric values; (5) exports a cleaned CSV. Print summary statistics before/after cleaning (row counts, null percentages) to validate the transformation._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-05.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection & Alerting System
  _Using Australian Weather observations dataset (Bureau of Meteorology or Kaggle), build an end-to-end pipeline: (1) Write a Python script using pandas to load weather CSV data, calculate rolling 7-day average temperature and rainfall per location; (2) Identify anomalies where current values deviate >2 standard deviations from the rolling average; (3) Export anomalies to a new CSV with columns: Location, Date, Metric (temperature/rainfall), Observed Value, Rolling Avg, Deviation. (4) Load this anomaly CSV into SQLite (or your database), then write a SQL query using CTEs and window functions to rank anomalies by severity per location over the last 30 days, and identify locations with 3+ anomalies in that window (potential climate events). Output: Location, Anomaly Count, Max Deviation, Alert Priority (HIGH if 3+ anomalies)._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-09-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
