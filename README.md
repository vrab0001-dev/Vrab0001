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
| 📅 Last Sync | 2026-04-16 11:23 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Moving Average & Volatility Ranking
  _Using ASX 200 historical price data, write a query with window functions to calculate: (1) 20-day and 50-day moving averages for each stock using AVG() OVER with ROWS BETWEEN, (2) daily percentage change using LAG(), (3) rolling 30-day volatility (standard deviation of daily returns), (4) rank each stock by volatility within its sector on the most recent date. Return stock symbol, date, close price, 20-day MA, 50-day MA, daily % change, volatility, and volatility rank. Use a CTE to organise the window function calculations, then filter for the last trading date only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash Data (data.nsw.gov.au). Clean the dataset by: (1) handling missing values in crash severity, location, and vehicle type columns (document your strategy for each), (2) standardising date formats and extracting day-of-week and hour-of-day from crash timestamp, (3) removing duplicate records based on crash ID, (4) validating latitude/longitude are within NSW bounds (approximately -28 to -34 latitude, 141 to 154 longitude). Then create a risk score column: (severity weight × injury count + vehicle count) / traffic volume estimate. Export cleaned data to a new CSV with all new columns. Document any data quality issues found and decisions made._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-16.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: Data Pipeline & Analytics
  _Build a mini data engineering pipeline: (1) Use Python to load Australian Bureau of Meteorology weather observations data (or use Kaggle Australian Weather dataset). Clean columns for temperature, rainfall, humidity, and wind speed; handle missing values via interpolation or forward-fill for time-series data. Standardise date formats. (2) Export cleaned data to a staging CSV. (3) Create a SQL schema and load the CSV into a local database (SQLite or PostgreSQL). (4) Write a SQL query using CTEs and window functions to: find the 7-day rolling average temperature by station, identify the coldest and warmest days per month per state, rank stations by average rainfall, and flag anomalies (temperatures >2 standard deviations from the 30-day rolling mean). Return a summary report with station name, state, metric, and anomaly flag. Document the entire pipeline from raw → cleaned → loaded → analysed._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (BoM) or Kaggle jsphyg dataset`
  📁 Submit as: `quest3_2026-04-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
