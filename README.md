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
| 📅 Last Sync | 2026-03-21 15:53 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Tracker with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 20-day moving average price for each stock using AVG() OVER (PARTITION BY symbol ORDER BY date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW); (2) Rank stocks each day by percentage gain using RANK() OVER (PARTITION BY date ORDER BY daily_return DESC); (3) Identify stocks where price crossed above their 20-day moving average using LAG() to compare current price vs previous moving average. Return symbol, date, close_price, moving_avg_20, rank_by_return, and a flag indicating crossover events. Filter for crossovers only in the last 30 days of data._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Profile Generator
  _Download NSW Road Crash Data (contains crash records with location, date, severity, road conditions). Using pandas: (1) Clean the dataset by handling missing values in 'Speed limit', 'Weather', and 'Crash type' columns (impute speed limit with median by road class, forward-fill weather); (2) Create a new 'risk_category' column using pd.cut() to bin crashes into Low/Medium/High/Critical based on injury count; (3) Generate a summary CSV with columns: [lga_name, total_crashes, avg_severity_score, wet_weather_crashes, night_crashes_pct, risk_category]. (4) Identify and flag any rows with >3 data quality issues. Output cleaned dataset and summary report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-21.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Flow Analysis: Peak Hours & Trend Detection
  _Combine Python and SQL to analyse Melbourne pedestrian counting sensor data. (1) In Python: Load the Melbourne pedestrian dataset (CSV with sensor_id, date, hour, count). Clean by removing null counts, standardise sensor_id naming, and create a 'day_of_week' column. Resample to hourly aggregates per sensor. Export to a temporary SQL-compatible format (CSV or SQLite). (2) In SQL: Write a CTE-based query to (a) Calculate hourly peak traffic per sensor using ROW_NUMBER() OVER (PARTITION BY sensor_id, hour ORDER BY count DESC) to find top 10 hours; (b) Use another CTE to compute week-over-week growth rate using LAG() OVER (PARTITION BY sensor_id, hour ORDER BY week); (c) Generate final output: [sensor_name, hour, avg_weekly_count, peak_count, wow_growth_pct, trend_direction]. (3) Return sensors with >20% growth trending upward in the 8-10am window (potential new commute patterns)._
  📦 Dataset: `Melbourne Pedestrian Counting Data — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-03-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
