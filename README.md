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
| 📅 Last Sync | 2026-03-25 12:07 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Ranking with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day price momentum for each stock. Use window functions (ROW_NUMBER, LAG) to rank stocks by momentum within each trading week. Specifically: (1) Calculate the price change from 30 days ago to today using LAG(). (2) Rank stocks by momentum percentile within each calendar week using ROW_NUMBER() OVER (PARTITION BY week ORDER BY momentum DESC). (3) Filter for only the top 10 momentum stocks per week. (4) Return: stock_code, trading_date, price_change_pct, momentum_rank, week_number. Use a CTE to structure the calculation cleanly._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data and perform data cleaning: (1) Load the CSV and identify missing values, duplicates, and data type mismatches. (2) Clean crash_date column (convert to datetime), handle any malformed entries. (3) Extract new features: day_of_week, hour_of_day from crash_date_time. (4) Create a severity_score by mapping injury_level (fatal=3, serious=2, other=1) and counting vehicles involved. (5) Remove crashes with incomplete location data (missing latitude/longitude). (6) Save cleaned dataset as cleaned_nsw_crashes.csv with all original + new columns. Document any rows dropped and why in a summary report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-25.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes Analysis Pipeline
  _Create an end-to-end pipeline combining Python and SQL: (1) Use Python (pandas) to load Australian Bureau of Meteorology weather observations data. Clean temperature, rainfall, and wind speed columns (handle missing values, outliers). (2) Write cleaned data to a local SQLite database in a table called weather_observations. (3) In SQL, use window functions to identify extreme weather events: calculate 7-day rolling average temperature, rank days by max_temp within each month, and flag any day in the top 5% hottest/coldest per month. (4) Query the database to find: Which Australian state/region had the most extreme temperature swings (biggest gap between max and min) in the last 12 months? (5) Return: state, month, avg_temp_swing, extreme_rank. Save results to extremes_report.csv from Python._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-03-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
