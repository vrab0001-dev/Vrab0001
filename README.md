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
| 📅 Last Sync | 2026-09-17 12:07 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Moving Averages
  _Using ASX 200 historical price data, write a query with window functions to: (1) Calculate the 20-day and 50-day moving averages for each stock using AVG() OVER (PARTITION BY stock_symbol ORDER BY date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW); (2) Rank stocks by their current price relative to their 50-day moving average (price/moving_avg_50) in descending order using RANK(); (3) Use a CTE to filter only stocks where the 20-day MA is above the 50-day MA (bullish signal); (4) Return the top 10 stocks with their symbol, current price, both MAs, the ratio, and rank. Expected output: 10 rows with stock rankings based on bullish momentum._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Severity Categorisation
  _Download NSW Road Crash Data (CSV format). Using pandas: (1) Load the dataset and inspect for missing values, duplicates, and data types; (2) Handle missing values in the 'Crash Severity' column by imputing with 'Unknown' and document how many rows were affected; (3) Create a new column 'Severity_Category' by mapping the existing severity field into 4 buckets: 'Fatal', 'Serious Injury', 'Other Injury', 'Non-Injury'; (4) Use list comprehension to extract hour of day from the 'Crash Time' column and create an 'Hour' feature; (5) Export the cleaned dataset to a new CSV file. Expected output: A cleaned CSV with 4 additional columns (Severity_Category, Hour, imputation_flag) and a summary report showing row counts before/after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-17.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Weather Extremes: Python Processing → SQL Analysis Pipeline
  _Working with Australian Bureau of Meteorology weather observations data: (1) Use Python with pandas to load monthly weather CSV files (temperature, rainfall, wind speed by station); (2) Perform data cleaning: standardise column names to lowercase, convert date strings to datetime, remove rows with missing temperature readings, and interpolate missing rainfall values using forward-fill; (3) Create a Python script that exports cleaned data to a SQLite database (weather_station_data.db) with a table 'observations' (date, station_id, station_name, max_temp, min_temp, rainfall); (4) Write SQL queries to identify: (a) The top 5 hottest days across all stations using window functions (ROW_NUMBER()), (b) Stations with the highest 30-day rolling average rainfall using window functions, (c) A CTE that finds stations where max_temp exceeded the 90th percentile, then joins with daily rainfall to find wet+hot days. Expected output: 1 SQLite database + SQL results showing extremes identified in 3 separate query outputs._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle as jsphyg/australian-weather)`
  📁 Submit as: `quest3_2026-09-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
