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
| 📅 Last Sync | 2026-11-11 14:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Rolling Averages
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate the 20-day rolling average closing price for each stock symbol, (2) Rank stocks by their current closing price relative to their 20-day average (highest premium first), (3) Use LAG() to show the previous day's closing price and calculate daily percentage change, (4) Filter for only stocks trading above their 20-day average. Return columns: symbol, date, close_price, rolling_avg_20d, price_premium_pct, previous_close, daily_pct_change, rank_by_premium. Order by rank ascending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-11.sql`
- [ ] 🐍 **Python Quest:** Clean and Standardise Australian Weather Station Data
  _Download Australian weather observations data (daily min/max temperatures, rainfall, wind speed across multiple stations). Your task: (1) Handle missing values in temperature and rainfall columns (forward-fill for max 2 consecutive days, then drop), (2) Standardise station names to title case and remove leading/trailing whitespace, (3) Convert all temperatures from Celsius to Fahrenheit, (4) Identify and flag anomalies (e.g., max temp < min temp for same day, rainfall > 500mm), (5) Create a new 'month_year' column and calculate monthly aggregates (avg temp, total rainfall) by station, (6) Export cleaned data to CSV with proper datetime indexing. Write a Python script using pandas that logs all cleaning operations performed._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology via Kaggle (jsphyg collection)`
  📁 Submit as: `quest2_2026-11-11.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: Data Pipeline & Trend Analysis
  _Build a complete data engineering pipeline: (1) Download NSW Road Crash data from the official source, (2) Use Python/pandas to clean the data: standardise location names, handle missing severity values, convert date columns to datetime, remove duplicates based on crash_id, (3) Load cleaned data into a SQL database or create a SQL-queryable format, (4) Write SQL queries to find: top 10 crash locations by frequency (past 5 years), monthly trend of fatal vs non-fatal crashes using window functions (ROW_NUMBER, SUM() OVER), and identify locations with increasing crash trends (compare year-over-year growth), (5) Export results to CSV with visualisation-ready columns (month, crash_count, severity_distribution). Document the pipeline steps in comments and measure data quality metrics (% missing values before/after cleaning)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-11-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
