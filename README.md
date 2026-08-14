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
| 📅 Last Sync | 2026-08-14 10:56 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 30-day moving average for each stock using AVG() OVER a window ordered by date; (2) Rank stocks by their year-to-date percentage return using RANK() OVER; (3) Identify stocks that reached their 52-week high in the last 7 days using LAG() and conditional logic. Return columns: stock_code, current_price, moving_avg_30day, ytd_rank, days_since_52week_high. Order by ytd_rank. Expected output: 15–25 rows showing top performers with their technical metrics._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Classification
  _Download the NSW Road Crash Data (from data.nsw.gov.au). Clean and transform the dataset: (1) Handle missing values in crash_type and severity columns (drop rows with >20% missing, impute others with mode); (2) Create a new 'injury_severity_category' column by binning injury counts into Low (0–2), Medium (3–5), High (6+); (3) Remove duplicate crash records based on crash_id and datetime; (4) Convert date columns to datetime and extract day_of_week and hour_of_day; (5) Export cleaned data to CSV with filename format: nsw_crashes_cleaned_YYYYMMDD.csv. Validate: ensure no null values remain in key columns, check for data type consistency, and print summary statistics (row count before/after, missing value counts)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-14.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis: Python ETL + SQL Reporting
  _Complete a two-stage pipeline: STAGE 1 (Python): Download Australian wine production data (from Wine Australia or Kaggle). Use pandas to: clean region names (standardise case, remove whitespace), convert production volumes to tonnes, filter for years 2015–2025, and save to a local SQLite database (wine_production.db) in a table named 'production'. STAGE 2 (SQL): Write a query on the SQLite database to identify: (1) Top 5 wine-producing regions by total production over the period; (2) Year-over-year growth rate for each region using LAG(); (3) Regions with consistent growth (positive growth for ≥3 consecutive years) using window functions and CTEs. Return: region, total_production_tonnes, avg_yoy_growth_percent, consecutive_growth_years. Export results to CSV. Deliverables: cleaned CSV from Stage 1, SQLite .db file, SQL query file, results CSV from Stage 2._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com) or Kaggle`
  📁 Submit as: `quest3_2026-08-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
