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
| 📅 Last Sync | 2026-10-31 13:59 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 30-day moving average for each stock's closing price using AVG() OVER a window; (2) Rank stocks by their year-to-date return using RANK() OVER ORDER BY; (3) Find the date each stock hit its 52-week high using ROW_NUMBER() OVER PARTITION BY stock_id; (4) Calculate the percentage change from previous close using LAG() function. Return a result set with stock_symbol, current_price, moving_avg_30d, ytd_rank, weeks_52_high_date, and pct_change_from_prev. Filter for top 20 performers only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-31.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data (CSV format). Build a Python script using pandas to: (1) Load the raw crash data and identify missing values, data type inconsistencies, and duplicates; (2) Clean crash date/time columns and standardise location data (remove whitespace, standardise postcode format); (3) Create new calculated columns: severity_score (based on injury_type and fatality flags), crash_hour (extracted from time), and distance_from_sydney (calculated from latitude/longitude if available); (4) Filter crashes involving motorcycles only; (5) Export cleaned dataset to a new CSV with summary statistics (total crashes, injury count, average severity by local government area). Expected output: cleaned CSV + summary report printed to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-31.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Trend Analysis: SQL + Python ETL
  _End-to-end data engineering task: (1) Download AIHW health expenditure data (by state, year, and health category). (2) Write Python script to: load CSV, clean column names, handle missing values, and load data into a SQLite database table named 'health_expenditure'. (3) Write a SQL query using CTEs and window functions to: calculate year-on-year expenditure growth by state using LAG(), identify the top 3 health categories by total spend per state using RANK(), and flag states where expenditure exceeded the national average using window functions. (4) Export SQL results back to pandas DataFrame, create a pivot table showing expenditure by state×category, and generate a PNG visualisation (bar chart) of growth rates by state. Expected outputs: populated SQLite DB, cleaned CSV, pivot table CSV, and growth_rates.png chart._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-10-31.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
