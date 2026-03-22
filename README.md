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
| 📅 Last Sync | 2026-03-22 16:11 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Rankings
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate the 30-day rolling average price for each stock symbol, then rank stocks by their current price relative to this rolling average (highest to lowest). Include columns: symbol, current_date, close_price, rolling_avg_30d, price_vs_avg_pct, and rank_by_performance. Filter for the last 5 trading days only and order by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Export Pipeline
  _Download NSW Road Crash Data (CSV format). Write a Python script using pandas to: (1) identify and handle missing values in the Severity and Speed_Zone columns (document your strategy), (2) standardise date formats to YYYY-MM-DD, (3) remove duplicate crash records based on Crash_ID, (4) create a new column Crash_Hour extracted from crash_time, (5) filter for crashes in the last 5 years only, and (6) export the cleaned dataset as a new CSV file. Print a before/after summary showing row counts and data types._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-22.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Health Monitoring Pipeline
  _Using Great Barrier Reef monitoring data from AIMS, build an end-to-end pipeline: (1) Load the coral health observations CSV in Python using pandas, (2) clean the data by removing invalid temperature readings (outside 15-35°C range) and standardising location names to title case, (3) create a SQLite database table called reef_observations with columns: observation_id, location, date_observed, water_temp, coral_health_score, and bleaching_level, (4) insert the cleaned data into SQLite, (5) write a SQL query with a CTE to calculate the average health score by location and identify locations where average health has declined by more than 10% year-over-year, (6) export results to CSV. Document your data quality checks._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-03-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
