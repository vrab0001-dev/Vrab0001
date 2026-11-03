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
| 📅 Last Sync | 2026-11-03 15:21 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Analysis
  _Using ASX 200 historical price data, write a query with window functions to: (1) Calculate the 20-day moving average for each stock's closing price using AVG() OVER a window; (2) Rank stocks by their 1-month return using RANK() OVER; (3) Use LAG() to find the price change from previous trading day; (4) Filter for stocks where the current price is above the 20-day MA and rank is in top 50. Return stock_code, date, close_price, ma_20day, price_change, and rank. Use a CTE to stage the window calculations before filtering._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash Data (contains crash reports with location, time, severity, vehicle types). Clean the dataset by: (1) Handling missing values in severity and crash_type columns (document your strategy); (2) Standardising location data and geocoding to LGA (Local Government Area); (3) Creating a derived 'risk_score' column (weighted combination of fatality_count, injury_count, and repeat_location_incidents); (4) Grouping by LGA and time period to identify high-risk crash corridors; (5) Exporting clean data to a CSV with validation checks (e.g., no negative counts, dates in valid range). Document your assumptions and data quality issues found._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-03.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL Pipeline
  _Build a mini ETL pipeline: (1) Python: Download/load Australian wine production data (vintage, region, varietal, tonnes produced, value). Clean by handling missing regions, standardising varietal names (e.g. 'Shiraz' vs 'Syrah'), and converting production values to consistent units. (2) SQL: Load cleaned data into a staging table. Write a query using CTEs and window functions to: calculate total production and revenue by region and year; rank varieties by market value within each region; compute year-on-year growth using LAG(); identify top 3 performing region-variety combinations. (3) Export results showing regional trends, growth rates, and top performers. Document the data quality steps and any transformations applied._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-11-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
