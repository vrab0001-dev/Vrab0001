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
| 📅 Last Sync | 2026-09-21 12:03 AEDT |

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
  _Using ASX 200 historical price data, calculate a 10-day moving average and identify momentum shifts. Write a query using window functions (ROW_NUMBER, LAG) to: (1) rank each stock by daily percentage change within its partition, (2) calculate the 10-day moving average of closing price, (3) flag rows where the current close crosses above/below the moving average, (4) return the top 5 stocks with strongest momentum reversals (biggest gap between current price and 10-day MA). Use a CTE to stage the moving average calculation, then filter results. Expected output: stock_code, date, close_price, moving_avg_10d, momentum_flag, rank_by_change._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-09-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains messy crash records with missing values, inconsistent formatting, and duplicates). Write a Python script using pandas to: (1) load the CSV and inspect data quality, (2) handle missing values in crash_severity and location columns (decide on strategy: drop/fill/forward-fill), (3) standardise datetime formats for crash_date, (4) remove exact duplicates and near-duplicates (same location/date within 5 minutes), (5) create a summary pivot table showing crash_count by severity and day_of_week, (6) export cleaned dataset and summary to separate CSVs. Document your data quality decisions in comments. Expected output: cleaned_crashes.csv and crashes_summary.csv._
  📦 Dataset: `NSW Road Crash Data — NSW Open Data Portal (data.nsw.gov.au)`
  📁 Submit as: `quest2_2026-09-21.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: Extract, Clean, Load
  _Build a mini data pipeline combining Python and SQL. (1) Using Python/pandas: Download or load Australian wine production data (by region and variety). Clean the dataset by: handling missing vintage years, standardising region names (trim whitespace, uppercase), converting production volumes to consistent units (tonnes). Create a staging CSV with cleaned data. (2) Using SQL: Create a SQLite/CSV-based table from the cleaned data. Write a query using GROUP BY and HAVING to find: (a) the top 3 wine regions by total production volume across all varieties, (b) varieties that appear in more than 5 regions, (c) a ranking of regions by production variance (standard deviation), ordered by volatility. Expected deliverables: (i) Python script showing extract→clean→save workflow, (ii) SQL file with the three analytical queries, (iii) cleaned_wine_data.csv staging file._
  📦 Dataset: `Australian wine production statistics — Wine Australia (wineaustralia.com) or ABS agriculture data`
  📁 Submit as: `quest3_2026-09-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
