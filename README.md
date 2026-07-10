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
| 📅 Last Sync | 2026-07-10 11:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum Ranking
  _Using ASX 200 historical stock price data, create a CTE-based query that calculates the 7-day price momentum (current close - close 7 days ago) for each stock. Then use window functions (ROW_NUMBER, RANK) to rank stocks daily by momentum, and identify the top 5 gainers and bottom 5 losers for each trading date. Your output should show date, stock symbol, closing price, 7-day momentum, and momentum rank. Use LAG window function to access previous rows efficiently._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Zone Mapping
  _Download NSW Road Crash Data from data.nsw.gov.au. Write a pandas script to: (1) Load the CSV and inspect missing values in crash severity, location, and casualty columns; (2) Standardise suburb names (handle whitespace, case inconsistencies); (3) Remove duplicate crash records based on crash ID and date; (4) Create a new column 'casualty_severity_ratio' = total_casualties / number_of_vehicles (handle division by zero); (5) Filter crashes with severity='Fatal' and export to a cleaned CSV. Your script should include data validation checks and print a summary report of rows dropped and transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-10.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: Data Pipeline & Analysis
  _Build a mini data engineering pipeline: (1) Use Python with pandas to load Australian Weather observations data (Bureau of Meteorology / Kaggle jsphyg dataset), clean temperature and rainfall columns (handle missing values, outliers, unit conversions if needed), and insert cleaned records into a local SQLite database with a schema: weather_stations(station_id, station_name, state), daily_observations(date, station_id, temp_max, temp_min, rainfall_mm). (2) Write SQL queries using CTEs to: calculate 30-day rolling average temperature by station, identify the hottest day per state in the dataset, and rank stations by total annual rainfall using window functions. Export results to CSV. Your deliverable: Python script + SQL queries + 2 output CSVs (rolling temps, state rankings)._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
