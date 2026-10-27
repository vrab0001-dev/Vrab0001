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
| 📅 Last Sync | 2026-10-27 13:41 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their 30-day average return within each sector. Use ROW_NUMBER() to identify the top performer per sector, LAG() to calculate day-over-day price changes, and a CTE to compute the 30-day moving average. Return: stock_code, sector, closing_price, 30day_avg_return, rank_in_sector, previous_day_close. Filter for the last 90 days of data and order by sector and rank._
  📦 Dataset: `ASX 200 historical stock prices — Kaggle`
  📁 Submit as: `quest1_2026-10-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Classification Pipeline
  _Download the NSW Road Crash Data (data.nsw.gov.au). Build a Python/pandas script that: (1) loads the CSV and identifies missing values per column; (2) standardises datetime formats for crash_date and crash_time; (3) creates a new column injury_severity by mapping injury counts to categories (no_injury, minor, serious, fatal); (4) removes duplicate rows based on crash_id; (5) filters for crashes in the Sydney metropolitan area only; (6) exports the cleaned dataset to a new CSV with timestamp in filename. Log the number of rows removed at each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-27.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Trend Analysis: Python ETL → SQL Analytics
  _Using AIHW health expenditure data: (1) Write a Python script using pandas to load the CSV, clean column names (remove spaces, standardise to snake_case), handle missing values by forward-filling by state and year, and add a new column real_expenditure_2020_dollars using a fixed CPI deflator. Export to a staging CSV. (2) Load the cleaned data into a SQL database (SQLite or PostgreSQL). (3) Write a SQL query using window functions to calculate year-over-year expenditure growth % by state, rank states by growth, and use LAG() to compare each year to the previous. Return: state, year, expenditure_2020_dollars, yoy_growth_pct, state_rank. Identify the top 3 states with highest average growth over the period._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-10-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
