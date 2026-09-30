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
| 📅 Last Sync | 2026-09-30 12:44 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Moving Averages
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate the 20-day and 50-day moving averages for each stock's closing price using a CTE, (2) Rank stocks by their YTD percentage gain using RANK() OVER(), (3) Use LAG() to calculate day-over-day price changes, (4) Filter only stocks where the 20-day MA is above the 50-day MA (bullish crossover signal). Return stock symbol, current price, YTD gain rank, and both moving averages. Order by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Scoring Pipeline
  _Download NSW Road Crash Data (contains crash details, locations, severity, vehicle types, road conditions). Write a Python/pandas script to: (1) Load the dataset and handle missing values (document imputation strategy for each column), (2) Standardise location data (remove duplicates, geocode suburb names), (3) Create a new 'crash_severity_score' column using weighted logic (injuries × 10 + fatalities × 50 + property damage × 2), (4) Group by Local Government Area (LGA) and calculate mean severity score, fatality rate, and crash frequency, (5) Export cleaned data and LGA summary statistics to separate CSV files. Include data quality report (null counts, outliers detected)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-30.py`
- [ ] ⚡ **Combined Quest:** Australian Bureau of Meteorology Weather Extremes Analysis Pipeline
  _Build an end-to-end pipeline using Python and SQL: (1) In Python: Download Bureau of Meteorology weather observations (temperature, rainfall, wind speed for major Australian cities), clean the data (handle missing timestamps, convert units), and load into a SQLite database with tables for daily_observations and city_metadata. (2) In SQL: Write queries with CTEs and window functions to identify: (a) For each city, the hottest and coldest days recorded with RANK(), (b) Rolling 7-day average rainfall using ROW_NUMBER() and PARTITION BY, (c) Cities where max temperature exceeded the 95th percentile in the last 30 days, (d) Month-over-month temperature trend analysis using LAG(). (3) Export results to CSV and write a brief summary of findings (which city had most extreme weather events). Document your data pipeline logic._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-09-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
