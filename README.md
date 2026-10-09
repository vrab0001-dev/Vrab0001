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
| 📅 Last Sync | 2026-10-09 14:24 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Tracker with Window Functions
  _Using ASX 200 historical price data, calculate the 20-day moving average and identify momentum shifts for each stock. Write a query using window functions (ROW_NUMBER, LAG) to: (1) Rank stocks by daily percentage change within each trading date, (2) Calculate the 20-day moving average of closing prices for the top 10 stocks by market cap, (3) Identify dates where a stock's price crossed above/below its moving average. Return stock_code, date, close_price, moving_avg_20, price_momentum_rank, and cross_signal (UP/DOWN/NONE). Use a CTE to pre-filter data for the last 12 months._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (contains crash records with inconsistent date formats, missing values, and duplicate entries). Build a Python/pandas script to: (1) Standardise date columns to YYYY-MM-DD format, (2) Handle missing values in Severity and Location fields using domain-appropriate imputation, (3) Remove exact duplicate rows and near-duplicates (same crash_id but different time entries within 5 minutes), (4) Categorise crashes by severity level and create a summary report showing crash count and injury rate by Local Government Area (LGA), (5) Export cleaned data to CSV and generate a data quality report (rows removed, nulls handled, duplicates found). Save outputs as cleaned_crashes.csv and data_quality_report.txt._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-09.py`
- [ ] ⚡ **Combined Quest:** Weather-Driven Energy Demand Correlation Analysis
  _Combine Australian Weather observations (Bureau of Meteorology dataset) with AEMO electricity demand data. (1) In Python/pandas: load both datasets, align them by date and state, handle missing temperature/humidity readings using forward-fill, and calculate daily average temperature and peak demand per state. (2) In SQL: Create a table joining weather and demand data, then write a query using window functions to calculate the correlation between temperature and peak demand for each state, ranked by correlation strength. (3) Identify anomalies: dates where demand deviated >2 std devs from the temperature-predicted norm using LAG/LEAD to smooth trends. Return state, date, temp_avg, peak_demand_mwh, correlation_coefficient, and anomaly_flag. Document your pipeline in a Python script that orchestrates both data prep and SQL execution._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle jsphyg) + AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-10-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
