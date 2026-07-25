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
| 📅 Last Sync | 2026-07-25 11:25 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Detection with Window Functions
  _Using ASX 200 historical prices dataset, write a SQL query with window functions to identify momentum shifts. Calculate a 5-day moving average price using AVG() OVER (PARTITION BY symbol ORDER BY date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW). Then use LAG() to compare current price against the 5-day MA from the previous day. Flag rows where price crosses above the MA (bullish signal) or below (bearish signal). Return symbol, date, close_price, moving_avg_5day, prior_ma, and signal_type. Order by symbol and date. Expected output: 50-100 rows showing momentum shift events._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Hotspot Mapping
  _Download NSW Road Crash Data from data.nsw.gov.au. Clean the dataset by: (1) removing rows with missing latitude/longitude coordinates, (2) converting date columns to datetime format, (3) standardising severity_level values to uppercase, (4) filtering crashes from 2022 onwards only, (5) removing duplicate records based on crash_id. Then create a summary CSV containing: suburb name, crash count, total injuries, total fatalities, and average severity score (1-5 scale). Sort by crash count descending. Save output as 'nsw_crash_hotspots_cleaned.csv'. Expected output: 50-150 suburbs ranked by crash frequency._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-25.py`
- [ ] ⚡ **Python + SQL Quest:** AIHW Health Expenditure Trend Analysis Pipeline
  _Build an end-to-end pipeline: (1) Download AIHW health expenditure data (CSV format). (2) Use Python/pandas to clean the dataset: remove null values in expenditure columns, convert currency to float, add a year-extracted column. (3) Create a SQLite database and load cleaned data into a table called 'health_expenditure'. (4) Write a SQL query using CTEs to: calculate year-over-year expenditure growth % by health service category (hospital, primary care, mental health, etc.). Use LAG() to get prior year values. (5) Return top 5 categories with highest growth rates. Export results to 'health_expenditure_growth.csv'. Expected output: 5 rows showing category, year, expenditure, prior_year_expenditure, and growth_percentage._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-07-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
