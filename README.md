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
| 📅 Last Sync | 2026-07-18 11:17 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum with Window Functions
  _Using ASX 200 historical price data, calculate the 5-day moving average and momentum (percentage change) for each stock using window functions. Write a query that: (1) ranks stocks by their latest momentum score using ROW_NUMBER() partitioned by stock symbol, (2) uses LAG() to compare current price against previous day's close, (3) filters for stocks in the top 10 gainers over the last 30 days, and (4) returns symbol, date, close price, 5-day moving average, and momentum percentage. Use a CTE to organize the window function logic._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download NSW Road Crash Data from the open data portal. Write a Python script using pandas that: (1) loads the CSV and identifies missing values, duplicates, and data type inconsistencies, (2) cleans date/time columns and standardizes categorical values (e.g., crash type, severity), (3) creates a new derived column for crash severity category (minor/moderate/severe) based on injury counts, (4) removes outliers (e.g., crash records with implausible coordinates), and (5) exports a cleaned dataset to a new CSV. Document all transformations in comments. Expected output: clean CSV with no null values in critical columns and consistent data types._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-18.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis: Peak Hours Detection
  _Combine Python and SQL to analyze Melbourne pedestrian counting data. Step 1 (Python): Load the pedestrian sensor data CSV, clean timestamps, handle missing values, and create hourly aggregated counts per sensor location. Save to a local SQLite database using pandas.to_sql(). Step 2 (SQL): Query the database to identify peak traffic hours (top 3 hours by volume) for each sensor location using ROW_NUMBER() and window functions. Calculate the percentage contribution of peak hours to total daily traffic. Return: sensor_id, location, peak_hour, hourly_count, and percentage_of_daily_total. Combine results back into a Python script that exports a summary report (CSV) ranking sensors by peak hour traffic intensity._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-07-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
