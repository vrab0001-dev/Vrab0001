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
| 📅 Last Sync | 2026-03-28 12:06 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify momentum shifts. Write a query using window functions (ROW_NUMBER, LAG, LEAD) to rank each company by the percentage change between current price and 20-day MA, then identify the top 5 gainers and bottom 5 losers on the most recent date. Include a CTE to calculate the moving average, then use it in a ranking query. Output: company_code, current_price, moving_avg_20day, pct_change, momentum_rank, date._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from data.nsw.gov.au. Build a pandas data cleaning script that: (1) handles missing values in crash_severity and location columns (impute or drop strategically), (2) standardises date formats to YYYY-MM-DD, (3) removes duplicate records based on crash_id, (4) creates new features: crash_hour (extracted from time), is_fatal (boolean from severity), and suburb_postcode (parsed from address). Export cleaned data to a new CSV. Document your decisions on missing data handling with inline comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-28.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Combine Python and SQL to build an anomaly detection workflow. (1) Use pandas to load Australian Bureau of Meteorology weather observations (daily max/min temperature, rainfall by station). Clean the data: handle missing values, standardise temperature units to Celsius, remove outliers using IQR method. (2) Load cleaned data into SQLite. (3) Write SQL queries with CTEs to calculate z-scores for temperature and rainfall by station and month. Identify days in the past 12 months where temperature or rainfall deviated >2 standard deviations from the monthly mean. (4) Export anomalies to CSV with columns: station_name, date, metric, observed_value, expected_range, z_score. Output should highlight potential climate anomalies for analysis._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-03-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
