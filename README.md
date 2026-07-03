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
| 📅 Last Sync | 2026-07-03 11:46 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock. Use window functions (specifically ROW_NUMBER and LAG) to compute daily percentage change, then apply a rolling window to calculate volatility. Filter for the top 10 most volatile stocks in the last quarter of available data. Expected output: stock_code, date, daily_return_pct, rolling_volatility_30day, ranked by volatility descending._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-07-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation
  _Download NSW Road Crash Data and perform comprehensive data cleaning: handle missing values (fill crash severity nulls with 'Unknown', drop rows with null latitude/longitude), standardise datetime formats, remove duplicate crash records (identified by location + timestamp), and convert speed limit to numeric. Then aggregate by local government area (LGA) and crash severity to produce a summary showing total crashes, injury count, and fatality count per LGA. Export cleaned data to CSV and provide a top-10 most dangerous LGAs report._
  📦 Dataset: `NSW Road Crash Data — NSW Data Portal (data.nsw.gov.au)`
  📁 Submit as: `quest2_2026-07-03.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Build a Python + SQL pipeline: (1) Load Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) from CSV. (2) In Python/pandas, clean the data—remove outliers using IQR method for temperature, interpolate missing rainfall values. (3) Load cleaned data into SQLite. (4) Write SQL queries using CTEs and window functions to identify temperature anomalies: calculate monthly average temp, then compare each observation to its station's 10-year historical average using a window function. (5) Flag observations >2 standard deviations from the mean as anomalies. Export anomaly report grouped by station and month, showing anomaly count and average deviation magnitude._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-07-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
