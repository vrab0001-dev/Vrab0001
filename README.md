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
| 📅 Last Sync | 2026-07-28 11:21 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, calculate a 20-day moving average for the top 5 most traded stocks. Use window functions (AVG() OVER) to compute the moving average, then use ROW_NUMBER() to rank stocks by their latest price momentum (current price vs 20-day MA). Finally, use LAG() to compare each day's closing price with the previous day's close. Your output should show: stock_code, trade_date, close_price, moving_avg_20day, price_change_from_previous_day, momentum_rank. Filter for the last 90 days of data and order by trade_date DESC, momentum_rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data (CSV format). Your task: (1) Clean the dataset by handling missing values in the 'Speed Limit', 'Road Type', and 'Weather Condition' columns using appropriate imputation; (2) Create a new feature 'crash_severity_score' (0-100) based on number of persons injured and vehicles involved; (3) Convert date columns to datetime format and extract 'day_of_week', 'month', 'hour_of_crash'; (4) Remove duplicate records based on crash ID; (5) Export the cleaned dataset to a new CSV file. Document any data quality issues you find and your imputation strategy in a brief text summary._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-28.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Wildfire Risk Correlation
  _Combine two datasets: (1) Australian Weather Observations (Bureau of Meteorology / Kaggle), and (2) Australian Wildfire Dataset (Kaggle). Use Python to clean both datasets, aggregate daily weather metrics (temperature, humidity, rainfall) by region/location, and merge with wildfire occurrence data. Then, using SQL, create a CTE that calculates: for each region, the average temperature 7 days before a wildfire event vs 7 days before non-fire days. Use window functions to lag weather data by 1-7 days. Output: region, avg_temp_before_fire, avg_temp_before_nofire, humidity_variance, rainfall_mm, fire_count. Identify which regions show the strongest correlation between temperature spikes and subsequent fire events. Present findings as a sorted table._
  📦 Dataset: `Australian Weather Observations — Kaggle (jsphyg); Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-07-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
