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
| 📅 Last Sync | 2026-05-28 11:50 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) the 5-day moving average of closing prices for each stock, (2) the day-over-day percentage change ranked by volatility within each stock, and (3) identify stocks where the closing price crossed above their 10-day moving average. Use CTEs to structure the query. Return stock symbol, date, closing price, 5-day MA, percentage change, and a flag indicating crossover events. Order by stock symbol and date._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-28.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning & Missing Value Imputation
  _Download or load the Australian Weather observations dataset (Bureau of Meteorology). Write a Python/pandas script to: (1) identify missing values across temperature, rainfall, and wind speed columns, (2) remove rows where more than 30% of features are missing, (3) impute remaining missing values using forward-fill for time-series columns and median for cross-sectional columns, (4) detect and handle outliers in temperature (flag values >50°C or <-20°C), (5) validate data types and convert date columns to datetime. Output a cleaned CSV file with a data quality report showing before/after record counts and missing value percentages._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest2_2026-05-28.py`
- [ ] ⚡ **Combined Quest:** NSW Crime Trends Pipeline: ETL & Analytical Query
  _Build a mini data pipeline combining Python and SQL: (1) In Python, use pandas to load NSW Bureau of Crime Statistics data, clean offence descriptions (standardise case, remove duplicates), aggregate crimes by suburb and offence type for the last 12 months, and export to a CSV. (2) Create a SQL query that loads this CSV into a temporary table, then calculates: month-over-month crime rate change per suburb using LAG(), ranks suburbs by total crime volume, and identifies top 5 emerging crime types (highest growth rate). Use a CTE to compute growth rates. Output a final result set showing suburb name, offence type, total crimes, growth rate %, and rank. Expected runtime: 45 minutes._
  📦 Dataset: `NSW Bureau of Crime Statistics — bocsar.nsw.gov.au`
  📁 Submit as: `quest3_2026-05-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
