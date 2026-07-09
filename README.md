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
| 📅 Last Sync | 2026-07-09 11:45 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical stock price data, write a SQL query with window functions to calculate: (1) the 20-day moving average price for each stock, (2) the price rank within each trading day (highest to lowest), and (3) the day-over-day percentage change using LAG(). Filter for stocks where the 20-day moving average increased by more than 2% over the last 10 days. Output: stock_code, trading_date, close_price, moving_avg_20day, price_rank_daily, pct_change_daily, sorted by trading_date DESC and price_rank_daily ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (from data.nsw.gov.au). Clean the dataset by: (1) removing duplicate rows, (2) handling missing values in severity and crash_type columns (drop rows where >30% data missing in critical columns), (3) standardising date formats to YYYY-MM-DD, (4) correcting geocoordinates (filter out invalid lat/long outside NSW bounds: -28.0 to -34.5, 140.0 to 154.0). Then aggregate crashes by Local Government Area (LGA) and severity level. Output a CSV with columns: lga_name, severity, crash_count, avg_casualty_count, sorted by crash_count DESC. Include a data quality report showing rows removed at each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-09.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends Data Pipeline
  _Build a Python + SQL pipeline using Australian Bureau of Meteorology weather observations (available on Kaggle as 'Australian Weather'): (1) In Python, load the CSV, clean temperature and rainfall columns (remove outliers >3 standard deviations, handle nulls with forward-fill), convert date strings to datetime, and export to a staging CSV. (2) In SQL, create a table from the staging CSV and write a CTE-based query to: identify the top 5 weather stations with highest average temperature increase (using window functions to calculate 30-day rolling avg), find months with anomalous rainfall (>2 std devs from station's historical mean), and rank stations by data completeness. Output: station_name, location_state, avg_temp_trend, anomaly_count, data_completeness_pct, ranked by avg_temp_trend DESC._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-07-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
