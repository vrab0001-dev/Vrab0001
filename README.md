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
| 📅 Last Sync | 2026-06-28 12:10 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Rankings
  _Using ASX 200 historical price data, calculate the 20-day and 50-day moving averages for each stock using window functions. Rank stocks by their current price relative to the 50-day moving average (highest first) within each sector. Include a column showing the percentage change from the 20-day MA to current price. Filter to show only stocks where current price > 50-day MA and rank > 5 within their sector. Output: stock_code, sector, current_price, ma_20, ma_50, pct_change, sector_rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from data.nsw.gov.au. Clean the dataset by: (1) removing rows with missing critical fields (crash_date, location, severity), (2) standardising crash_date to YYYY-MM-DD format, (3) extracting day_of_week and hour_of_day from datetime, (4) geocoding location strings to remove duplicates caused by spelling variations, (5) categorising severity into standardised buckets (Fatal, Serious Injury, Other Injury, Non-Injury). Export cleaned data to CSV with new columns: day_of_week, hour_of_day, severity_category. Provide a data quality report showing: rows removed, null counts before/after, and unique values per column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-28.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Using Bureau of Meteorology historical weather data (available on Kaggle as 'Australian Weather Observations'): (1) In Python/pandas, load daily temperature and rainfall data, filter to the last 5 years, calculate 30-day rolling mean temperature and rolling total rainfall by station. (2) Identify anomalies as days where temperature deviates >2 standard deviations from the 30-day mean OR rainfall >95th percentile for that station/month combination. Export anomalies to a staging table in SQLite. (3) In SQL, use a CTE to rank anomalies by severity (deviation magnitude) within each station and month. Create a summary query returning: station_id, month, anomaly_count, max_temp_deviation, max_rainfall_deviation, top_3_anomaly_dates. Output final results to CSV._
  📦 Dataset: `Australian Weather Observations — Kaggle (jsphyg dataset) and Bureau of Meteorology`
  📁 Submit as: `quest3_2026-06-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
