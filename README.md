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
| 📅 Last Sync | 2026-04-03 12:14 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Performance Ranking with Moving Averages
  _Using ASX 200 historical price data, write a query that: (1) calculates a 20-day moving average of closing prices for each stock; (2) ranks stocks daily by percentage gain using ROW_NUMBER() partitioned by date; (3) identifies stocks that ranked in the top 10 gainers for at least 3 consecutive trading days using a CTE and LAG/LEAD window functions. Return: stock_code, date, close_price, moving_avg_20day, daily_rank, consecutive_top10_days. Order by date descending, then rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Geocoding Preparation
  _Download NSW Road Crash Data (CSV format). Clean the dataset by: (1) removing rows with >30% missing values; (2) standardising postcode format to 4 digits, removing invalid postcodes; (3) converting crash_date to datetime and extracting day_of_week, hour_of_day as new columns; (4) categorising crash_severity into 'Fatal', 'Serious Injury', 'Other Injury', 'Non-Injury' based on injury counts; (5) deduplicating rows based on crash_id, date, location. Output a cleaned CSV with 15+ columns. Document data quality metrics: original row count, final row count, % missing values removed per column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-03.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: Transform & Load Analysis
  _Build a data engineering pipeline: (1) Python: Download Australian wine production data (vintage, region, variety, production volume). Clean using pandas: remove outliers (production >3 std devs from mean), standardise region names (title case, trim whitespace), handle missing variety data by grouping to 'Other'. Export to a temporary table schema (CSV or SQLite). (2) SQL: Load the cleaned data into a database. Write a query using window functions to: rank regions by total production volume (all-time), calculate year-over-year % change in production by region using LAG(), identify the top 3 varieties per region by volume using RANK(). Return: region, variety, year, production_volume, region_rank, yoy_change_pct, variety_rank_in_region. (3) Combine results: use Python to read SQL output, create a summary report showing top 5 regions, their growth trends, and variety diversity scores._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-04-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
