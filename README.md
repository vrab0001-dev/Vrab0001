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
| 📅 Last Sync | 2026-06-07 12:13 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 30-day moving average price for each stock using AVG() OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW). (2) Rank stocks by their latest closing price performance (percentage change from 30 days ago) using RANK() OVER (ORDER BY pct_change DESC). (3) Identify stocks that crossed above their 30-day moving average in the last 7 days using LAG() to compare current price to previous moving average. Return: ticker, date, close_price, moving_avg_30d, pct_change_30d, rank, and a flag column 'crossed_above_ma' (Y/N). Filter for only the top 20 performers by rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data (from data.nsw.gov.au). Write a Python script using pandas to: (1) Load the CSV and inspect for missing values, duplicates, and data type inconsistencies. (2) Clean the data by handling null values in 'Severity', 'Crash Type', and 'Weather' columns (document your strategy—drop, fill, or flag). (3) Standardize text columns (convert to lowercase, strip whitespace, fix common spelling variations). (4) Create new calculated columns: 'crash_year' from the crash date, 'is_fatal' (1 if severity='Fatal', 0 otherwise), and 'time_of_day' (categorise Hour into 'Night' 00-05, 'Morning' 06-11, 'Afternoon' 12-17, 'Evening' 18-23). (5) Export the cleaned dataset to a new CSV file. Output: a summary report showing original vs. cleaned row counts, missing value counts before/after, and sample of cleaned data._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-07.py`
- [ ] ⚡ **Combined Quest:** Bureau of Meteorology Weather Analysis: Python ETL to SQL Analytical Queries
  _Using Australian Weather observations data (Bureau of Meteorology / Kaggle jsphyg version): (1) In Python, load the raw weather CSV, clean temperature and rainfall columns (handle missing values, outliers, and unit conversions if needed), standardise station names and dates, and export to a clean CSV. (2) Create a SQL schema with two tables: stations (station_id, station_name, state, latitude, longitude) and observations (observation_date, station_id, temp_max, temp_min, rainfall_mm). (3) Write a SQL query with a CTE to calculate: For each state, the average max temperature and total rainfall for each month in the dataset. Then use a second CTE to identify months where rainfall was above the state's historical average. Finally, use a window function RANK() OVER (PARTITION BY state ORDER BY avg_max_temp DESC) to rank months within each state by temperature. Return: state, month, avg_max_temp, total_rainfall, is_above_avg_rainfall (Y/N), and temp_rank_in_state._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle jsphyg dataset)`
  📁 Submit as: `quest3_2026-06-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
