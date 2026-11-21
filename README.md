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
| 📅 Last Sync | 2026-11-21 15:34 AEDT |

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
  _Using ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of closing prices for each stock symbol using window functions. Rank stocks by volatility (highest to lowest) using ROW_NUMBER(). Then use a CTE to filter only stocks in the top 20% volatility tier and return: symbol, current_price, volatility_rank, 30day_std_dev, and price_change_pct (comparing current close to 30 days ago using LAG window function). Order results by volatility_rank ascending._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-11-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains crash records with timestamps, locations, severity, weather conditions). Write a Python/pandas script to: (1) Handle missing values in weather_condition and severity columns by forward-filling within each Local Government Area; (2) Convert timestamp to datetime and extract crash_hour and crash_month; (3) Remove duplicate records based on crash_id; (4) Create a new column injury_rate = (count of injured persons) / (total persons involved); (5) Export cleaned data to CSV. Validate that no nulls remain in critical columns (crash_id, location, severity). Output a summary report showing row counts before/after cleaning and % of data retained._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-21.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk & Climate Correlation Analysis
  _Combine two datasets: Australian Wildfire dataset (Kaggle) and Australian Weather observations (Bureau of Meteorology / Kaggle). (1) In Python/pandas: load both datasets, standardise date formats, merge on nearest date and location (within 50km radius using lat/lon approximation or exact postcode match). Clean merged data, handle missing values in temperature and rainfall columns using interpolation. (2) Calculate monthly fire frequency and average temperature/rainfall by region. Export cleaned merged dataset as CSV. (3) In SQL: load the merged CSV, create a CTE that ranks regions by fire frequency, then join with weather metrics. Write query to identify regions where: (fire_frequency > 75th percentile) AND (average_temperature > 30°C) AND (average_rainfall < 200mm). Return region, fire_count, avg_temp, avg_rainfall, and risk_score (normalized 0-100). Order by risk_score descending._
  📦 Dataset: `Australian Wildfire dataset + Australian Weather observations — Kaggle and Bureau of Meteorology`
  📁 Submit as: `quest3_2026-11-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
