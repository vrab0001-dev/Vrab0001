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
| 📅 Last Sync | 2026-08-15 10:32 AEDT |

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
  _Using ASX 200 historical prices dataset, write a query that calculates the 20-day moving average price for each stock, identifies the rank of stocks by price momentum (percent change from 20-day low), and flags stocks that have broken above their 52-week high in the last 30 days. Use window functions (ROW_NUMBER, RANK, LAG) and a CTE to structure the analysis. Return: stock_code, current_price, 20day_moving_avg, momentum_rank, days_since_52week_high_break. Order by momentum_rank ascending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (data.nsw.gov.au). Load the dataset and perform: (1) Handle missing values in crash_severity and crash_type columns using appropriate imputation; (2) Parse datetime columns and extract hour_of_day and day_of_week features; (3) Clean location data by removing rows with invalid coordinates (outside NSW bounds: -28 to -34 latitude, 141 to 154 longitude); (4) Create a new column 'injury_severity_score' by mapping crash_severity categories to numeric values; (5) Detect and remove duplicate crash records based on crash_id and timestamp. Output a clean CSV with all transformations applied and log the number of rows removed at each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-15.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Wine Production Pipeline: ETL & Time-Series Analysis
  _Create an end-to-end data pipeline: (1) Extract wine production data (Australian Wine Production Statistics) and clean it using pandas—handle unit conversions (ensure all volumes in litres), remove data quality flags, standardize region names to match a reference list; (2) Load the cleaned data into a local SQLite database with tables: wine_production (year, region, variety, volume_produced, value_aud) and wine_regions (region_name, state); (3) Write SQL queries to: (a) calculate year-over-year growth rate by region using LAG window function, (b) identify the top 5 regions by average production value in the last 5 years, (c) find varieties with declining production trends; (4) Export results to CSV files. Document data quality issues found and resolutions applied._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com / ABARES agriculture.gov.au`
  📁 Submit as: `quest3_2026-08-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
