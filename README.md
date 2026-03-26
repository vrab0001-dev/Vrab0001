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
| 📅 Last Sync | 2026-03-26 12:13 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking
  _Using ASX 200 historical stock price data, write a query with window functions to: (1) Calculate the 30-day price change percentage for each stock using LAG, (2) Rank stocks by momentum within each sector using RANK() OVER, (3) Identify the top 3 performers and bottom 3 performers per sector, (4) Use a CTE to filter only stocks with volume > 1M shares traded. Return sector, stock symbol, current price, 30-day change %, and rank. Order by sector and rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-26.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (from NSW open data portal). Write a Python/pandas script to: (1) Load the CSV and inspect for missing values and data types, (2) Clean date columns and convert to datetime, (3) Handle missing values in crash location and severity fields (document your strategy), (4) Create a new column for crash hour extracted from timestamp, (5) Aggregate crashes by Local Government Area (LGA) and hour-of-day to find peak crash times, (6) Export a cleaned CSV with aggregated counts. Show summary statistics before and after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-26.py`
- [ ] ⚡ **Combined Quest:** Weather Impact on Electricity Demand Analysis
  _Combine Australian Bureau of Meteorology weather observations with AEMO electricity demand data. (1) Use Python/pandas to load and merge both datasets on date and region/state, (2) Clean temperature, humidity, and demand data (handle outliers, missing values), (3) Create features: temperature deviation from historical average, day-of-week, is-weekend flag, (4) Load cleaned data into SQLite, (5) Write SQL query using window functions to calculate: rolling 7-day average demand, demand rank by day-of-week, and correlation of temperature change to demand change using LAG. (6) Identify days where demand exceeded the 90th percentile and temperature was above 30°C. Export results showing date, state, demand, temp, and anomaly flags._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle) + AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-03-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
