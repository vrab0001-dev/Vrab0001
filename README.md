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
| 📅 Last Sync | 2026-03-12 16:06 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 30-day rolling average closing price for each stock, (2) the rank of each stock by daily percentage change within each date, and (3) a running total of volume traded. Use ROW_NUMBER() OVER (PARTITION BY stock_symbol ORDER BY date) to identify trading sequences, and LAG() to calculate day-over-day price changes. Return the top 10 stocks by volatility (standard deviation of daily returns) over the past 90 days._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (CSV format) from data.nsw.gov.au. Write a Python script using pandas to: (1) clean the dataset by handling missing values in critical columns (crash_type, severity, location), (2) standardise date formats and location names, (3) remove duplicate records based on crash_id, (4) create a new column for crash_severity_category (group by injury count), and (5) export a cleaned CSV and a summary report showing crash frequency by LGA and severity. Handle edge cases like null geometries and misformatted postcodes._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-12.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Pipeline: Extract, Transform, Load
  _Build a data pipeline combining Python and SQL: (1) Use Python to fetch/load AIHW health expenditure data (by state, year, health service type) from a CSV or API; clean it by removing subtotals, standardising category names, and handling currency formatting. (2) Load the cleaned data into a SQLite or PostgreSQL database. (3) Write a SQL query using CTEs to calculate: year-on-year expenditure growth by state, cumulative expenditure by health service type, and identify states with above-average spending per capita. (4) Export results to a structured JSON file. Document your pipeline with comments explaining data quality checks and transformation logic._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-03-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
