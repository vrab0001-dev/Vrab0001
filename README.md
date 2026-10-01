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
| 📅 Last Sync | 2026-10-01 12:49 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Ranking with Moving Averages
  _Using ASX 200 historical price data, write a query with window functions to: 1) Calculate the 20-day and 50-day moving averages for each stock using ROW_NUMBER and LAG functions, 2) Rank stocks by their year-to-date return using RANK() OVER (PARTITION BY ticker ORDER BY ytd_return DESC), 3) Identify stocks where the 20-day MA crossed above the 50-day MA in the last 10 trading days. Return ticker, date, close_price, ma_20, ma_50, ytd_return_rank, and a flag indicating golden_cross. Order by date descending and rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Score Calculation
  _Download NSW Road Crash Data and build a data cleaning pipeline using pandas: 1) Handle missing values in severity, location (latitude/longitude), and crash type columns with appropriate strategies (drop, forward-fill, or impute), 2) Standardise the date column to ISO format and extract day_of_week and hour_of_day, 3) Remove duplicate crash records based on crash_id and timestamp, 4) Create a risk_score column (0-100) based on: severity (40%), number_of_vehicles (30%), number_of_persons_injured (20%), speed_zone (10%), 5) Filter for crashes with risk_score >= 70 and save to a clean CSV. Output summary statistics: total crashes, crashes by severity, average risk_score, and top 5 risk zones._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-01.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline combining Python and SQL: 1) In Python: Extract Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) from the open dataset. Clean data by removing outliers (temps > 50°C or < -20°C as errors), handle missing rainfall values by forward-filling within 7-day windows, and standardise all numeric columns to z-scores. Save cleaned data to a SQLite database with tables: weather_raw and weather_cleaned. 2) In SQL: Write a query using CTEs and window functions to identify anomalies: for each location, calculate 30-day rolling average temperature and flag any day where actual temp deviates by > 2 standard deviations. Rank anomalies by severity (deviation magnitude) and return: location, date, actual_temp, rolling_avg_temp, deviation_std, anomaly_rank. Filter for anomaly_rank <= 10 per location. 3) Output: Provide both the cleaned CSV and a summary report of top 20 anomalies across all locations._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
