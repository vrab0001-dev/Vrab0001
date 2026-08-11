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
| 📅 Last Sync | 2026-08-11 10:48 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Tracker
  _Using ASX 200 historical price data, write a query with window functions to calculate: (1) the 20-day moving average for each stock, (2) the rank of stocks by daily percentage change within each trading date, and (3) identify stocks that hit a new 52-week high on each date. Use ROW_NUMBER() and LAG() to compare current price against the previous day's close. Return a result set with stock_code, trading_date, close_price, moving_avg_20day, daily_rank, and is_52week_high flag. Order by trading_date DESC and rank ASC._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-08-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleanup & Aggregation
  _Download NSW Road Crash Data (CSV format) and perform the following cleaning tasks: (1) handle missing values in crash_severity and location columns (drop rows or impute sensibly), (2) parse datetime columns correctly, (3) standardise crash_type values (remove whitespace, convert to lowercase), (4) filter out records with incomplete geographical coordinates, (5) create a new column for crash_year extracted from date, (6) aggregate crashes by local government area and severity level to count incidents per LGA. Export the cleaned dataset and the aggregated summary to separate CSV files. Document any data quality issues found._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-11.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Agriculture Yield Correlation
  _Combine Australian Bureau of Meteorology weather observations (temperature, rainfall) with ABARES crop production data. (1) Use Python/pandas to load both datasets and perform date alignment (match month/year), (2) clean and validate rainfall and temperature columns, handling outliers or missing data, (3) create a Python script that loads the cleaned data into a SQLite database, (4) write a SQL query with CTEs to calculate: average rainfall and temperature by month and state, total crop yield by state and crop type, and a correlation score between rainfall in growing months and final yield. (5) Export results showing which states have the strongest weather-to-yield relationship. Expected output: CSV with state, crop_type, avg_rainfall, avg_temp, total_yield, and correlation_coefficient._
  📦 Dataset: `Australian Weather observations (Bureau of Meteorology) + ABARES crop production data — agriculture.gov.au`
  📁 Submit as: `quest3_2026-08-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
