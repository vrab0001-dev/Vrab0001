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
| 📅 Last Sync | 2026-06-29 12:10 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates the 5-day and 20-day moving averages for the top 10 most volatile stocks (by standard deviation of daily returns). Use window functions (AVG() OVER) to compute rolling averages, and include columns for: stock_code, date, closing_price, 5day_ma, 20day_ma, daily_return_pct, and volatility_rank. Filter for data from the last 90 trading days. Order by volatility_rank and date. Expected output: ~450 rows (10 stocks × ~45 trading days)._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleanup and Feature Engineering
  _Download NSW Road Crash Data (CSV format). Clean the dataset by: (1) handling missing values in Severity, Speed_Zone, and Weather_Condition columns using appropriate strategies; (2) converting date columns to datetime; (3) removing duplicate crash records based on Crash_ID; (4) creating new features: Day_of_Week, Hour_of_Day (from timestamp), and Casualty_Severity_Category (binning injury counts into Low/Medium/High/Fatal). Export the cleaned dataset as 'nsw_crashes_cleaned.csv'. Print summary statistics showing row count before/after cleaning, missing value counts per column, and distribution of your new categorical features._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-29.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends ETL Pipeline
  _Build a mini ETL pipeline: (1) In Python, load Australian Bureau of Meteorology weather observations (CSV or JSON from Kaggle). Clean the data: standardise temperature units to Celsius, remove rows with missing Temperature or Rainfall, and filter for stations in major Australian cities (Sydney, Melbourne, Brisbane, Perth, Adelaide). Save to a SQLite database in a table called 'weather_observations'. (2) In SQL, write a query using CTEs to calculate: for each city, the monthly average temperature, total monthly rainfall, and rank cities by average temperature within each month. Include a column showing the temperature trend (increasing/decreasing/stable) month-over-month using LAG(). Expected output: 60-72 rows (6 cities × 12 months, or subset of months available). Document your SQL query in a separate .sql file._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: Australian Weather by jsphyg)`
  📁 Submit as: `quest3_2026-06-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
