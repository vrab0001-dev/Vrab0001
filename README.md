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
| 📅 Last Sync | 2026-10-07 14:02 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using ASX 200 historical price data, calculate the 20-day moving average and momentum rank for each stock. Use window functions (ROW_NUMBER, LAG) to: 1) Partition by stock symbol and order by date; 2) Calculate price change from previous day using LAG(); 3) Compute 20-day moving average of closing prices; 4) Rank stocks by momentum (highest positive change) within each date using ROW_NUMBER(). Return top 10 momentum stocks for the most recent date in your dataset. Expected output: stock_symbol, date, close_price, price_change, moving_avg_20d, momentum_rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (data.nsw.gov.au) and perform comprehensive data cleaning: 1) Identify and handle missing values in crash_date, time, severity, and location columns; 2) Standardise date/time formats and extract hour_of_day and day_of_week features; 3) Remove duplicates based on crash_id; 4) Validate latitude/longitude coordinates are within NSW bounds (-28.0 to -34.3 lat, 140.6 to 154.7 lon); 5) Create a severity_category column (map numeric codes to 'Fatal', 'Serious Injury', 'Other Injury'); 6) Export cleaned dataset to CSV with data quality report (rows removed, % missing per column). Expected output: cleaned_crashes.csv + data_quality_report.txt._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-07.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: Extract, Transform, Load & Analyse
  _Using Australian Bureau of Meteorology weather observations dataset (or jsphyg Kaggle weather data): 1) Write a Python script to load weather CSV, clean temperature/rainfall columns (remove outliers >50°C or <-20°C for temp; rainfall <0 invalid), and standardise location names; 2) Load cleaned data into a SQLite database (create weather_observations table with columns: station_id, date, temp_max, temp_min, rainfall, location); 3) Write SQL queries to: calculate monthly average max temperature by location using CTEs, identify top 5 driest months (lowest rainfall) using window functions (ROW_NUMBER), and find locations where temp exceeded 40°C in the last 12 months. Expected output: SQLite database file + Python script + SQL query results showing location, month, avg_temp, and drought ranking._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
