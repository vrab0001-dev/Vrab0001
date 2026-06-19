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
| 📅 Last Sync | 2026-06-19 12:46 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns & Moving Averages
  _Using ASX 200 historical prices, calculate daily percentage returns for each stock using LAG(). Then, compute a 20-day and 50-day moving average of closing prices using window functions. Finally, identify stocks where the 20-day MA crossed above the 50-day MA (bullish signal) on the most recent date. Use a CTE to structure the moving averages, and return stock_code, date, close_price, ma_20, ma_50, and a flag indicating if a crossover occurred. Order by stock_code._
  📦 Dataset: `ASX 200 historical stock prices — Kaggle`
  📁 Submit as: `quest1_2026-06-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Summary Export
  _Download NSW Road Crash Data (CSV format from data.nsw.gov.au). Load it into pandas and perform: (1) Remove or fill missing values in critical columns (crash_type, severity, number_of_vehicles). (2) Standardise date formats and ensure consistency. (3) Create a new column 'year_month' from the crash date. (4) Generate a summary CSV showing crashes by severity and year_month. (5) Identify and flag rows with anomalies (e.g., more vehicles than occupants). Save the cleaned dataset and summary report as separate CSVs with timestamps in filenames._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-19.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Weather Anomaly Detection Pipeline
  _Download Australian Bureau of Meteorology weather observations (daily temperature, rainfall, wind speed data from Kaggle or BoM). Use Python to: (1) Load CSV and clean data (handle missing values, convert data types). (2) Calculate rolling 30-day mean and standard deviation for temperature by location. (3) Flag days where temperature deviated >2 standard deviations from the mean (anomalies). (4) Export cleaned data with anomaly flags to SQLite database. Then, use SQL to: (1) Rank locations by anomaly frequency using DENSE_RANK(). (2) Use a CTE to identify weeks with the most anomalies per location. (3) Return top 10 location-week combinations ordered by anomaly count. Output should include location, week, anomaly_count, and rank._
  📦 Dataset: `Australian Weather observations (daily data) — Bureau of Meteorology via Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-06-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
