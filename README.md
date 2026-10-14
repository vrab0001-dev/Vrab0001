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
| 📅 Last Sync | 2026-10-14 13:27 AEDT |

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
  _Using ASX 200 historical price data, calculate a 10-day rolling average of closing prices and identify the top 5 stocks by momentum (price change from 10-day MA). Use window functions ROW_NUMBER() and LAG() to rank stocks and compute day-over-day price changes. Your output should show: stock ticker, date, closing price, 10-day MA, momentum rank, and the number of consecutive days each stock outperformed its MA. Use a CTE to structure the rolling averages, then a second CTE to calculate ranks._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data and perform comprehensive data cleaning: handle missing values in crash location, crash type, and injury severity columns; standardise date formats; remove duplicate crash records; identify and flag outlier coordinates (crashes outside NSW bounds). Engineer new features: extract day of week and hour from crash datetime; create a severity category (minor/moderate/severe/fatal); calculate crash density by local government area. Output a cleaned CSV with original columns plus new engineered features, and generate a summary report (dict or JSON) showing: total crashes processed, % of missing values per column, top 5 LGAs by crash count._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-14.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Dashboard Data Pipeline
  _Build a data pipeline combining Python and SQL: (1) Use pandas to load Australian Wildfire dataset, clean fire location coordinates, extract fire start dates, and calculate fire duration in days. (2) Load Bureau of Meteorology weather observations (temperature, rainfall) and join to fire data by location and date (fuzzy matching on nearest weather station within 50km). (3) Create a SQLite database with two tables: fires (fire_id, location, start_date, duration_days, lat, lon) and weather_observations (station_id, obs_date, temp_max, rainfall). (4) Write SQL queries to: identify the top 10 fires by duration, calculate average temperature and rainfall during fire periods vs non-fire periods by region, and rank months by fire count. Output: the SQLite database file, a CSV of query results, and a Python script that orchestrates the full ETL._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle; Bureau of Meteorology observations — Kaggle`
  📁 Submit as: `quest3_2026-10-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
