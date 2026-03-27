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
| 📅 Last Sync | 2026-03-27 12:13 AEDT |

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
  _Using ASX 200 historical stock price data, write a query that calculates the 5-day and 20-day moving averages for each stock using window functions. Then rank stocks by their current price relative to the 20-day moving average (stocks trading above their 20-day MA ranked first). Use a CTE to first calculate the moving averages, then a second CTE to rank stocks. Return: stock_code, current_price, ma_5day, ma_20day, price_to_ma_ratio, rank. Filter to top 20 stocks only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains crash records with location, date, severity, vehicle type, etc.). Write a Python script using pandas to: (1) handle missing values in severity and location fields by filling with 'Unknown'; (2) standardise date format to YYYY-MM-DD; (3) remove duplicate crash records based on crash ID; (4) create a new column 'crash_hour' extracted from time; (5) aggregate crashes by LGA (Local Government Area) and severity level, counting total crashes and calculating average number of vehicles involved; (6) export results to a CSV file. Expected output: CSV with columns LGA, severity, total_crashes, avg_vehicles_involved._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-27.py`
- [ ] ⚡ **Python + SQL Quest:** AIHW Health Expenditure Trend Analysis Pipeline
  _Build a data pipeline: (1) Using Python pandas, load AIHW health expenditure data (includes year, state, expenditure category, amount). Clean the data by converting amounts to numeric, handling missing years, and standardising state names to full names (e.g., NSW, VIC). (2) Export the cleaned data to a local SQLite database in a table called 'health_expenditure'. (3) Write SQL queries to: calculate year-over-year expenditure growth by state and category using LAG window function; identify which state had highest total expenditure growth from 2015 to latest year; rank expenditure categories by absolute spend in the most recent year. Return three result sets: growth_by_state_category, top_growth_state, category_rankings. Document your Python script and SQL queries clearly._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-03-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
