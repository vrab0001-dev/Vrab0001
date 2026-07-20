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
| 📅 Last Sync | 2026-07-20 11:27 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Ranking with Moving Averages
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate daily percentage return for each stock, (2) Rank stocks by return within each trading date using ROW_NUMBER(), (3) Compute a 5-day moving average of closing prices for each stock using LAG(), (4) Identify stocks that had both top-10 returns AND moving averages above their 20-day average on any single date. Return date, stock_code, daily_return, rank, moving_avg_5d, and a flag indicating top performers. Order by date DESC and rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-20.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Geospatial Aggregation
  _Download NSW Road Crash Data (contains raw records with inconsistent formatting, missing values, and coordinate errors). Using pandas: (1) Clean crash dates by standardizing formats and removing invalid entries, (2) Handle missing latitude/longitude values by removing or imputing based on suburb geocoding, (3) Standardize crash type and severity categories (fix typos, case sensitivity), (4) Create a new CSV with crashes aggregated by Local Government Area (LGA), showing total crashes, injury count, and fatalities per LGA, (5) Export results sorted by fatality count DESC. Document all transformations in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-20.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Station Data Pipeline: SQL + Python
  _Build a mini data pipeline: (1) In Python, download Bureau of Meteorology observation data (multiple weather stations, daily readings with temperature, rainfall, humidity), clean missing values, handle sensor errors, convert units if needed, and load into a local SQLite database. (2) In SQL, write a query using CTEs to: find the 10 hottest days per station over the past year, calculate rolling 7-day rainfall averages, identify stations with anomalous temperature spikes (>5°C above 30-day rolling mean), and join this analysis to identify which LGAs or regions are most affected by extreme weather. (3) Export final results (station, date, anomaly_flag, rolling_rainfall_mm, context) as CSV. Provide both .py and .sql files with clear documentation._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
