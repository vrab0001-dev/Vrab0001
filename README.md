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
| 📅 Last Sync | 2026-10-03 12:39 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 30-day moving average for each stock's closing price using AVG() OVER (PARTITION BY stock_code ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW); (2) Rank stocks by their latest closing price within each sector using RANK() OVER (PARTITION BY sector ORDER BY close_price DESC); (3) Calculate the percentage change from the previous day using LAG() OVER (PARTITION BY stock_code ORDER BY date); (4) Identify the date each stock hit its 52-week high using ROW_NUMBER(). Return the top 10 stocks by recent performance with all calculated columns. Expected output: stock_code, sector, date, close_price, moving_avg_30d, sector_rank, pct_change_prev_day, weeks_52_high_date._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-10-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download the NSW Road Crash Data (contains accident details, location, casualties, vehicle types). Write a Python/pandas script to: (1) Load the CSV and identify missing values—document which columns have >20% missingness and decide on imputation or removal strategy; (2) Clean location data by extracting latitude/longitude from address fields (or use provided geo columns); (3) Create new features: time_of_day (from crash_time: early_morning, morning, afternoon, evening, night), severity_score (based on casualty counts and injury types), and road_type_category (group road types into Highway, Urban, Rural); (4) Remove duplicates based on crash_id and timestamp; (5) Export cleaned dataset to a new CSV. Expected output: cleaned CSV with 15-20 additional rows removed, 3 new feature columns, all data types correct (datetime, numeric, categorical), no nulls in critical columns._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-03.py`
- [ ] ⚡ **Combined Quest:** Tourism Hotspot Analysis: Visitor Patterns and Venue Performance
  _Combine Melbourne Pedestrian Counting data (foot traffic at major locations) with Tourism Research Australia visitor demographics. Task: (1) Use Python/pandas to load pedestrian_count.csv (hourly/daily foot traffic by sensor location) and clean it—handle missing hours, remove sensor malfunctions (erratic spikes >3 std dev), aggregate to daily totals by location; (2) Load and merge visitor demographic data (nationality, visit purpose, length of stay); (3) Use SQL to query the cleaned data: identify top 5 locations by average daily foot traffic, calculate hourly peak times using RANK() OVER (PARTITION BY location ORDER BY avg_hourly_count DESC), determine if international vs domestic visitors correlate with foot traffic patterns using GROUP BY and HAVING clauses; (4) Create a summary report showing: location, avg_daily_traffic, peak_hour, traffic_trend (increasing/decreasing over last 30 days using LAG), visitor_type_split. Expected output: SQL query results in CSV + Python script demonstrating end-to-end ETL, with at least 10 cleaned records per location._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal; Tourism Research Australia visitor data — tra.gov.au`
  📁 Submit as: `quest3_2026-10-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
