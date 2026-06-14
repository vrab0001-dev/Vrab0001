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
| 📅 Last Sync | 2026-06-14 12:28 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate a 20-day moving average and identify the top 5 stocks by momentum (price change % over last 20 days). Use ROW_NUMBER() or RANK() to rank stocks within each date partition, and LAG() to calculate day-over-day percentage changes. Return stock symbol, date, closing price, 20-day moving average, and momentum rank. Filter for the last 90 days of data only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaner & Aggregator
  _Download NSW Road Crash Data (CSV format). Write a Python/pandas script to: (1) identify and handle missing values in crash severity and location columns, (2) standardise postcode format to 4 digits, (3) parse crash datetime strings into separate date and time columns, (4) remove duplicate crash records based on crash ID, (5) create a new column for crash severity category (minor/moderate/severe based on injury count), and (6) export a cleaned CSV with summary statistics showing crashes by LGA and severity. Include data quality checks (row count before/after, missing value counts)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-14.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Pipeline: Clean, Load & Analyse
  _Build a mini data pipeline using Python and SQL: (1) Use pandas to load AIHW health expenditure data (by state and category), clean column names (lowercase, remove spaces), handle any missing or mixed-type values in spending amounts, and export to a clean CSV. (2) Create a SQLite database and load the cleaned CSV into a table called 'health_spending'. (3) Write a SQL query with CTEs to calculate: total spending by state, year-over-year growth rate (%), and identify the top 3 spending categories per state. Return results showing state, category, total spending, and YoY growth %. Expected output: a SQL result set ranked by growth rate descending._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-06-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
