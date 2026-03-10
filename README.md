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
| 📅 Last Sync | 2026-03-10 16:00 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of daily returns for the top 10 most volatile stocks. Use window functions (ROW_NUMBER, LAG) to compute daily percentage changes, then rank stocks by volatility. Return a result set with: stock_code, current_price, volatility_rank, rolling_std_dev, and the date range analysed. Order by volatility_rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data from the NSW open data portal. Write a Python/pandas script to: (1) load the CSV; (2) handle missing values in crash_type and severity columns (impute with 'Unknown'); (3) standardise datetime formats in crash_date; (4) remove duplicate records based on crash_id; (5) create a new column 'hour_of_day' from crash_time; (6) aggregate crashes by local government area and severity to produce a summary CSV with columns: LGA, severity, crash_count, avg_casualties. Save output as 'nsw_crashes_summary.csv'._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-10.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis: ETL & Analytics
  _Create an end-to-end data pipeline: (1) Use Python/pandas to extract and clean Australian wine production data (from Wineaustralia or ABS) — handle missing values, standardise region names, and convert production volumes to numeric types; (2) Load cleaned data into a SQLite database with a wine_production table; (3) Write SQL queries to: identify the top 5 regions by total production volume, calculate year-on-year growth rate using LAG window function, and list all regions where production declined by more than 10% in the latest year. Return results as a formatted report showing region, production_volume, yoy_growth_pct, and status (growth/decline)._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com or ABS`
  📁 Submit as: `quest3_2026-03-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
