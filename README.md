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
| 📅 Last Sync | 2026-09-06 11:38 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate daily percentage returns for each stock. Then use window functions (ROW_NUMBER, RANK, LAG) to: (1) rank stocks by daily return within each trading date, (2) identify the top 5 gainers and bottom 5 losers per day, (3) calculate the day-over-day change in closing price using LAG. Filter for the last 30 trading days. Return a result set with date, stock_code, close_price, daily_return_pct, daily_rank, and price_change_vs_previous_day. Use a CTE to stage the returns calculation before ranking._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (contains crash records with location, severity, vehicle type, weather conditions). Write a Python/pandas script to: (1) handle missing values in severity and weather columns (document your strategy), (2) standardise location data (clean postcodes, suburb names for consistency), (3) create new features: crash_severity_score (numeric encoding), weather_risk_category (grouped), time_of_day_bucket (from crash_time), (4) detect and flag outliers in injury counts, (5) generate a summary report showing crash count by severity and weather. Save the cleaned dataset to a new CSV with all transformations applied. Include comments explaining each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-06.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: Extract, Clean, Load & Analyse
  _Build a mini data engineering pipeline using Australian wine production statistics: (1) Python task: fetch or load wine production CSV (region, varietal, vintage, production_volume_litres), clean column names, handle missing vintage years, remove duplicate records, create a varietal_group column (e.g., 'Red', 'White', 'Fortified'), validate production_volume is numeric and positive, export to a staging CSV. (2) SQL task: create a table schema from the staged CSV, load the data, then write a query using window functions and CTEs to: rank varieties by total production volume across all regions, calculate cumulative production by region (using SUM OVER), identify the top-producing region per varietal, and show year-over-year production trends if multiple years exist. Return results sorted by varietal_group and production rank. Document the ETL assumptions and data quality checks you applied._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-09-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
