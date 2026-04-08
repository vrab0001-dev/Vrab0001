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
| 📅 Last Sync | 2026-04-08 11:16 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility Analysis
  _Using ASX 200 historical stock price data, write a SQL query with window functions to calculate the 30-day rolling standard deviation of daily returns for the top 5 most volatile stocks. Use LAG() to compute daily percentage change, then ROW_NUMBER() to partition by stock symbol and calculate rolling volatility using a window frame. Return stock symbol, date, closing price, daily return %, and 30-day rolling volatility. Order by volatility descending, then by date ascending. Expected output: 5 stocks with their volatility metrics over time, showing how volatility changes across the rolling window._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (from data.nsw.gov.au). Build a Python pandas script to: (1) Load the CSV and inspect for missing values, duplicates, and data type mismatches; (2) Clean and standardise the 'crash date', 'crash time', and 'council area' columns; (3) Remove rows where critical fields (crash date, latitude, longitude) are null; (4) Create new features: 'hour_of_day' from crash time, 'season' from crash date, and 'crash_severity_score' (ordinal encoding of severity level); (5) Export the cleaned dataset to a new CSV. Print a summary report showing rows removed, missing values before/after, and sample of engineered features._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-08.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Wildfire Risk Integration
  _Combine Bureau of Meteorology weather observations with Australian Wildfire dataset. Task: (1) In Python/pandas, load both datasets and merge them by location (latitude/longitude proximity within 50km radius) and date range. Handle missing temperature, rainfall, and humidity values using forward-fill or interpolation. (2) Engineer features: 'fire_weather_index' (combine temperature, humidity, wind speed), 'days_since_rain' (running calculation). (3) Export merged cleaned data to SQLite. (4) Write SQL queries to: identify the top 10 dates/locations with highest fire risk scores, calculate average weather conditions 7 days before confirmed wildfires, and rank states by wildfire frequency vs. precipitation correlation. (5) Output: cleaned merged table, 3 SQL result tables with business insights on weather-fire relationships._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle), Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-04-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
