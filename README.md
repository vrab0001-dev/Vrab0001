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
| 📅 Last Sync | 2026-10-21 13:17 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Volatility Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of daily returns for each stock. Use window functions (ROW_NUMBER, LAG) to: 1) Calculate daily percentage returns using LAG(close_price), 2) Compute rolling 30-day standard deviation partitioned by stock symbol, 3) Rank stocks by volatility (highest to lowest) using RANK() OVER, 4) Return top 10 most volatile stocks with their average volatility score, trading volume average, and date range. Expected output: 10 rows with columns: rank, stock_symbol, avg_volatility, avg_volume, date_first, date_last._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (crash records with location, date, severity, vehicle type). Using pandas: 1) Handle missing values in Latitude/Longitude by removing rows or imputing with median by region, 2) Parse datetime columns and extract hour_of_day, day_of_week, month, 3) Categorise crash severity into ordinal levels (Low/Medium/High/Fatal), 4) Create a new feature 'peak_hour' (True if hour between 7-9 or 16-19), 5) Remove duplicate records based on crash ID, 6) Export cleaned dataset to CSV with 20+ rows validation output showing before/after row counts and null percentages per column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-21.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Using Australian Weather Observations dataset (daily temperature, rainfall, humidity): 1) In Python/pandas: load data, handle missing values, calculate rolling 30-day mean and standard deviation for temperature by location (state), 2) Flag anomalies as days where temperature is >2 standard deviations from rolling mean, 3) Create a CSV with columns: date, location, temp, rolling_mean, rolling_std, anomaly_flag (Boolean), 4) Load this CSV into SQL and write a query to: identify locations with most anomalies in past 90 days, calculate anomaly frequency (%), use CTE to rank locations by anomaly severity, 5) Export final report: top 5 locations, anomaly count, anomaly percentage, date range of anomalies. Expected output: SQL result set with 5 rows ranked by anomaly frequency descending._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
