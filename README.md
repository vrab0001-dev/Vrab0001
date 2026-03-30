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
| 📅 Last Sync | 2026-03-30 12:17 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their 7-day price momentum. Calculate the percentage change from 7 days ago using LAG(), then use RANK() to identify the top 10 gainers and bottom 10 losers for the most recent trading date. Include columns: stock_symbol, current_price, price_7_days_ago, momentum_percent, momentum_rank. Order by momentum_rank ascending. This tests your understanding of LAG() for time-series analysis, window function ordering, and multi-column ranking._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download the NSW Road Crash Data from NSW Open Data. Write a Python/pandas script to: (1) Load the CSV and identify missing values in critical columns (crash_severity, council_area, speed_zone); (2) Handle missing crash_severity by mode-imputation within each council_area; (3) Remove rows with missing council_area; (4) Create a new 'risk_score' column calculated as: (number_of_casualties * 2) + (1 if speed_zone > 80 else 0); (5) Export the cleaned dataset to a new CSV with filename cleaned_nsw_crashes_20260330.csv. Include a summary print statement showing rows removed and risk_score distribution (min, max, mean)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-30.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Impact Analysis Pipeline
  _Build an end-to-end data pipeline: (1) In Python, download/load the Australian Wildfire dataset (Kaggle). Clean and transform it: parse date columns, handle null values in fire_size_acres and state columns, create a new column month_year from the date. Export to CSV as wildfire_cleaned.csv. (2) Create a SQL database table from this CSV. (3) Write a SQL query using CTEs to: calculate total acres burned per state per month, then use window functions (ROW_NUMBER) to rank months within each state by acres burned. Find the top 3 most damaging months for each state. Return columns: state, month_year, acres_burned, month_rank. (4) In Python, read the SQL query results and create a summary report (printed to console) showing: which state had the worst month on record and total acres across all states. This tests your ability to orchestrate Python data prep, SQL analytics, and CTEs._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-03-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
