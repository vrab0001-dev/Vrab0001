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
| 📅 Last Sync | 2026-09-23 12:09 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 5-day moving average of closing prices and identifies momentum shifts. Use a CTE to filter for stocks with price increases over the last 20 trading days, then use window functions (LAG, ROW_NUMBER, AVG OVER) to rank stocks by momentum strength. Return the top 10 stocks with the highest 5-day moving average momentum, including: stock ticker, current close price, 5-day MA, 20-day price change percentage, and rank. Use PARTITION BY to handle each stock separately._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-23.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Missing Data Imputation
  _Download the NSW Road Crash Data from data.nsw.gov.au (crash details, injury levels, locations). Load the dataset into pandas and perform: (1) identify all columns with missing values and document percentages; (2) remove rows where critical fields (crash date, location coordinates, severity) are missing; (3) standardise the 'crash_type' column by converting to lowercase and trimming whitespace; (4) create a new 'year_month' column from crash date; (5) fill missing 'speed_zone' values with the mode speed zone for that local government area; (6) export the cleaned dataset to a new CSV file. Document your data quality report as a summary dict showing original row count, final row count, and missing value statistics._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-23.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Seasonality Pipeline
  _Build an end-to-end pipeline: (1) Use Python/pandas to load Melbourne pedestrian counting data (from Melbourne Open Data Portal); clean the data by handling missing hourly counts and removing sensor outliers (values > 3 standard deviations from mean per sensor). (2) Create aggregated CSVs: one with daily totals per sensor, one with hourly averages by month. (3) Load the cleaned daily aggregates into a SQL database (SQLite or local DB); write a SQL query using window functions to calculate: month-over-month percentage change in foot traffic per sensor, rank sensors by seasonality volatility (coefficient of variation), and identify peak pedestrian months. (4) Return results showing top 5 most variable sensors, their peak months, and seasonal trends. Document your pipeline steps in comments._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-09-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
