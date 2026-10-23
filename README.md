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
| 📅 Last Sync | 2026-10-23 13:18 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) ROW_NUMBER() to rank each stock by daily closing price within its date partition, (2) LAG() to find the price change from previous day, (3) a CTE to identify stocks with 3+ consecutive days of price increases. Return stock symbol, date, closing price, price change, and consecutive_up_days. Filter for stocks with at least 5 consecutive up days in the dataset period._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-23.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (CSV format). Write a Python/pandas script to: (1) load the dataset and inspect for missing values and data types, (2) clean date columns and standardise location names (remove extra whitespace, convert to title case), (3) filter crashes with fatalities >= 1, (4) aggregate by local government area (LGA) to count total crashes, fatalities, and injuries, (5) export cleaned results to a new CSV file sorted by fatalities descending. Document any data quality issues found and how you handled them._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-23.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Data Pipeline: SQL + Python
  _Create an end-to-end data engineering task: (1) Use Python to fetch or load Bureau of Meteorology weather observations (daily max temp, rainfall, wind speed for 3+ Australian cities over 12 months), clean missing values using forward-fill or interpolation, and load into a SQLite database with proper schema (date, location, temp_max, rainfall_mm, wind_speed_kmh). (2) Write SQL queries using window functions (RANK, LAG) to calculate: rolling 7-day average temperature per city, month-over-month rainfall change, and identify extreme weather days (temp > 95th percentile OR rainfall > 95th percentile). (3) Export final results (city, date, metric, value) back to CSV. Include error handling and data validation checks in your Python code._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
