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
| 📅 Last Sync | 2026-06-30 12:05 AEDT |

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
  _Using ASX 200 historical price data, calculate the 20-day moving average and price momentum (% change from 20 days ago) for each stock using LAG and window functions. Identify the top 10 stocks with the highest positive momentum in the last quarter. Include columns: stock_symbol, current_price, moving_avg_20d, momentum_pct, rank_by_momentum. Use a CTE to first calculate the moving average, then rank results._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation
  _Download NSW Road Crash Data and perform the following: (1) Load the CSV and identify missing values, duplicates, and inconsistent date formats; (2) Clean the data by handling nulls in the 'Crash Type' and 'Severity' columns (document your strategy); (3) Create a pandas DataFrame grouped by LGA (Local Government Area) and crash severity, counting incidents per month over the last 12 months; (4) Export a cleaned CSV with the aggregated results showing trends by region. Output should show LGA, Severity, Month, and Incident_Count._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-30.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a data pipeline using Python and SQL: (1) In Python, load Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) for a single state over the last 12 months from Kaggle; (2) Clean the data: handle missing values, convert date strings to datetime, and standardise temperature units to Celsius; (3) Create a SQLite database and load the cleaned data using pandas.to_sql(); (4) In SQL, write a query using window functions to calculate rolling 30-day averages for temperature and identify anomalies (days where temperature deviates >2 standard deviations from the 30-day rolling mean); (5) Export results showing Date, Station, Temperature, Rolling_Avg_30d, Anomaly_Flag. Document your anomaly detection logic._
  📦 Dataset: `Australian Weather Observations — Kaggle (jsphyg) or Bureau of Meteorology`
  📁 Submit as: `quest3_2026-06-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
