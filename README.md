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
| 📅 Last Sync | 2026-08-22 10:31 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Momentum Tracker
  _Using ASX 200 historical stock price data, write a query that calculates for each company: (1) the 5-day moving average of closing price using a window function, (2) the rank of companies by daily percentage change using RANK(), and (3) identify which companies had their highest closing price in the last 30 days using ROW_NUMBER(). Filter results to show only the top 10 companies by percentage gain on the most recent trading date. Return columns: company_code, date, close_price, moving_avg_5day, rank_by_pct_change, days_since_52week_high._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from the open data portal. Write a Python script using pandas that: (1) loads the CSV and inspects for missing values and data types, (2) cleans crash location data by standardising suburb names (remove extra spaces, convert to title case), (3) converts date columns to datetime format and extracts day_of_week and hour_of_day, (4) removes duplicate crash records based on crash_id, (5) filters to only crashes in the last 5 years, and (6) exports a cleaned CSV with a summary report showing record count before/after cleaning, missing value percentages, and top 5 crash suburbs. Ensure your script is robust and handles edge cases._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-22.py`
- [ ] ⚡ **Combined Quest:** AEMO Electricity Demand Analysis & Reporting
  _Retrieve AEMO electricity demand data (30-minute or hourly interval data for the last 12 months). (1) Use Python/pandas to load, clean, and resample the data to daily totals by state and demand type. (2) Create a SQL database table from the cleaned data. (3) Write SQL queries to: identify peak demand dates for each state using window functions (RANK by demand), calculate month-on-month demand growth using LAG(), and detect anomalies (days where demand was >2 standard deviations above the 90-day rolling average). (4) Export final results showing state, date, total_demand_mwh, month_on_month_growth_pct, and anomaly_flag. Provide both Python script and SQL query files._
  📦 Dataset: `AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-08-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
