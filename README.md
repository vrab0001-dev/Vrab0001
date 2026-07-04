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
| 📅 Last Sync | 2026-07-04 11:45 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Monthly Performance Rankings with Window Functions
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate monthly returns for each stock using LAG to compare closing prices month-over-month, (2) Rank stocks within each month by return percentage using RANK(), (3) Identify the top 5 and bottom 5 performers per month, (4) Add a running average of closing price over the previous 3 months using a window frame. Return columns: stock_code, month, closing_price, monthly_return_pct, rank_in_month, 3month_avg_price. Filter for 2025 data only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Classification
  _Download NSW Road Crash Data from data.nsw.gov.au. Write a pandas script to: (1) Load the CSV and identify missing values, data types, and anomalies, (2) Clean location data by removing null coordinates and standardizing suburb names to title case, (3) Handle datetime columns (crash_date, crash_time) by parsing and extracting day_of_week and hour_of_day, (4) Create a severity_category column using pd.cut() based on injury_count (0=property_only, 1-2=minor, 3+=serious), (5) Remove duplicate rows based on unique crash identifiers, (6) Export the cleaned dataset to cleaned_nsw_crashes_2025.csv. Print a summary report: row counts before/after, missing value percentages, and value counts for severity_category._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-04.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline using Bureau of Meteorology Australian weather observations data: (1) In Python, load the CSV (temperatures, rainfall, wind speed by station and date), clean missing values using forward-fill within each station, and standardize units (convert Fahrenheit to Celsius if needed), (2) Create a feature-engineered dataset with rolling 7-day average temperature and total rainfall per station, (3) Write the cleaned data to a SQLite database with two tables: raw_observations and processed_features, (4) In SQL, write a CTE-based query to identify temperature anomalies: calculate mean and std_dev per station using window functions, flag days where temp deviates >2 std_dev from the mean, (5) Return: station_id, observation_date, actual_temp, mean_temp, anomaly_flag, days_since_last_anomaly (use LAG). Export results showing which stations had the most anomalies in the past year._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: Australian Weather by jsphyg)`
  📁 Submit as: `quest3_2026-07-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
