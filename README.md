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
| 📅 Last Sync | 2026-03-09 16:11 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Rolling Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate a 20-day rolling average closing price for each stock, (2) Rank stocks by their current price relative to their 20-day average (highest outperformers first), (3) Use LAG to show price change from the previous trading day, (4) Filter for stocks where current price exceeds rolling average by at least 5%. Return columns: stock_symbol, current_price, rolling_avg_20d, price_change_pct, rank. Use a CTE to structure the rolling average calculation first._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Hotspot Identification
  _Download the NSW Road Crash Data (from data.nsw.gov.au). Write a Python script using pandas to: (1) Clean missing values in latitude/longitude columns by removing or imputing with suburb centroids, (2) Standardise date formats and extract year/month/day_of_week, (3) Remove duplicate crash records (same location, date, time within 1 minute), (4) Identify the top 10 crash hotspots (by latitude/longitude grid cell of 0.01 degrees), (5) Export a cleaned CSV with columns: crash_id, date, day_of_week, latitude, longitude, severity, vehicle_count. Include data quality report showing rows removed and reason._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-09.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis: Data Pipeline & Trend Query
  _Build an end-to-end data pipeline: (1) In Python, fetch/download Australian wine production statistics (by region and year), clean inconsistent region names (e.g. 'South Australia' vs 'S.A.'), handle missing production volumes by forward-filling, and load into a SQLite database with tables: regions, vintages, production_data. (2) In SQL, write a query using CTEs and window functions to calculate: year-over-year production growth rate by region, rank regions by growth rate for the latest vintage, and identify regions with declining production (negative growth for 3+ consecutive years). Return: region, vintage, production_volume, yoy_growth_pct, rank, trend_status (declining/stable/growing). Expected output: CSV file ready for dashboard visualisation._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com / Kaggle`
  📁 Submit as: `quest3_2026-03-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
