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
| 📅 Last Sync | 2026-11-16 14:31 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query that ranks stocks by their year-to-date percentage return using window functions. Calculate for each stock: (1) ROW_NUMBER() ranked by YTD return descending, (2) the percentage change from start of year to most recent date, (3) LAG() to show the previous trading day's close price for comparison, (4) a running average of the last 20 trading days using a window frame. Filter to show only the top 20 performers and bottom 10 performers. Expected output: 30 rows with columns: stock_symbol, ytd_return_pct, rank, previous_close, twenty_day_moving_avg, trading_date._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas that: (1) loads the crash CSV file, (2) handles missing values intelligently (document your strategy for each column), (3) converts date/time columns to datetime objects, (4) extracts features like day_of_week, hour_of_day, is_nighttime (between 22:00-06:00), and severity_category (group injury levels), (5) removes duplicates based on crash_id, (6) exports a cleaned CSV with only relevant columns. Expected output: a cleaned CSV file with at least 15 columns and a summary report showing null counts before/after cleaning and row counts before/after deduplication._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-16.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Analysis: Python ETL + SQL Analytics
  _Working with AIHW health expenditure data: (1) Use Python to extract and clean the health expenditure CSV (handle currency formats, missing values, and inconsistent state abbreviations), normalise state names to standard two-letter codes (NSW, VIC, QLD, etc.), and load the cleaned data into a SQLite database with appropriate schema and indexes. (2) Write SQL queries to: calculate total health spending by state and year, use a CTE to rank states by spending growth rate year-over-year, and create a window function query showing each state's spending as a percentage of national total, with a RANK() of states by their percentage share. (3) Output: a cleaned CSV, a SQLite .db file, and a results CSV containing the window function output (state, year, spending, pct_of_national, rank). Expected deliverables: 3 files demonstrating full data pipeline from raw to analytics-ready._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-11-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
