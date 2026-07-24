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
| 📅 Last Sync | 2026-07-24 11:25 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using ASX 200 historical price data, calculate a 30-day rolling average price and rank each stock by its momentum (current price vs 30-day average) within each trading date. Use window functions ROW_NUMBER() and LAG() to identify the top 5 gainers and losers each week. Your output should show: stock_code, trading_date, closing_price, 30day_avg, momentum_rank, and weekly_rank. Filter for the last 3 months of data and order by trading_date DESC, momentum_rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data and build a Python script that: (1) loads the CSV, (2) handles missing values in crash_severity and road_type columns by forward-filling, (3) converts date columns to datetime format, (4) removes duplicate records based on crash_id, (5) creates a new column 'crash_year_month' by extracting year-month from the date, (6) exports a cleaned CSV with only crashes from 2023-2024 containing severity, location_suburb, road_type, and crash_year_month. Count and print the number of records removed in each cleaning step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-24.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Trend Report with Python + SQL
  _Use ABARES Australian wine production data. (1) In Python: load the CSV, clean vineyard_area and production_volume columns (handle missing values, convert to numeric), merge with vintage_year data, and export a staging table to a SQLite database. (2) In SQL: query the staged data to calculate year-over-year production growth by wine_region using LAG() and a CTE. Identify regions with >20% growth and <5% growth. Output: region_name, vintage_year, production_volume, yoy_growth_pct, and growth_category. Sort by yoy_growth_pct DESC. Expected runtime: join steps ~10 min, SQL analysis ~15 min._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia / ABARES`
  📁 Submit as: `quest3_2026-07-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
