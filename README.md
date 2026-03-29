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
| 📅 Last Sync | 2026-03-29 12:15 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Tracker
  _Using ASX 200 historical prices, write a query with window functions to calculate: (1) the 20-day moving average price for each stock, (2) the rank of stocks by daily percentage change within each date, and (3) identify stocks that hit a new 52-week high on each trading date. Use ROW_NUMBER() or RANK() and LAG() to compare current price against the max price in the preceding 252 trading days. Return stock code, date, closing price, moving average, daily rank, and a flag indicating 52-week high. Order by date descending, then by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Scrubber
  _Download NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas to: (1) load the CSV and identify missing values, outliers, and data type mismatches, (2) standardise suburb names (remove leading/trailing spaces, convert to title case), (3) extract hour from crash datetime and create a new 'time_of_day' column (Morning 6-12, Afternoon 12-18, Evening 18-24, Night 0-6), (4) remove duplicate crash records based on date, location, and severity, (5) export the cleaned dataset to a new CSV. Document all transformations applied and row counts before/after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-29.py`
- [ ] ⚡ **Combined Quest:** Australian Open Tennis Analytics Pipeline
  _Build an end-to-end pipeline: (1) Download Australian Open Tennis results dataset from Kaggle. (2) Use Python/pandas to clean player names, standardise tournament year, remove null match results, and engineer features: player age at tournament, previous Grand Slam wins, seeding rank. (3) Load cleaned data into a SQL database (SQLite or PostgreSQL). (4) Write a SQL query using CTEs to: identify the top 5 most successful players across all years (by win percentage), calculate their average matches per tournament, and rank players by consistency (lowest std dev of win rate year-over-year). (5) Export final results to CSV. Provide both the Python script and SQL query, plus a summary of data quality issues found and how you resolved them._
  📦 Dataset: `Australian Open Tennis Results — Kaggle`
  📁 Submit as: `quest3_2026-03-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
