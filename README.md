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
| 📅 Last Sync | 2026-04-02 12:11 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum Ranking
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) the 5-day moving average of closing price for each stock, (2) the daily price change percentage, (3) a rank of stocks by momentum (price change) within each date, and (4) identify the top 3 gainers and bottom 3 losers for the most recent date in the dataset. Use ROW_NUMBER and RANK functions. Return columns: date, ticker, close_price, moving_avg_5day, daily_change_pct, momentum_rank. Filter for the last trading date only in final result._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-02.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download the NSW Road Crash Data (contains crashes, vehicles, persons involved). Write a Python script using pandas to: (1) load all three CSV files, (2) handle missing values strategically (identify which columns have >30% nulls and decide whether to drop or impute), (3) standardise date formats to ISO 8601, (4) clean categorical columns (e.g. crash_type, road_user_type) by removing leading/trailing whitespace and converting to lowercase, (5) create a new feature 'severity_score' (0-10 scale) based on injury_level, (6) export cleaned data to a single consolidated CSV. Document your cleaning decisions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-02.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Trend Analysis
  _Create an end-to-end pipeline: (1) Download AIHW health expenditure data (by state, year, and health service type). (2) Use Python/pandas to clean the dataset: standardise column names, convert currency values to numeric types, handle any inconsistent state abbreviations. (3) Load cleaned data into a local SQLite database. (4) Write SQL queries to: calculate year-over-year expenditure growth by state using LAG window function, identify which health service type had the highest spend growth over the 10-year period, and create a summary CTE showing total expenditure by state ranked by spend. (5) Export final analytical results to CSV. Include Python script and SQL file in your submission._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-04-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
