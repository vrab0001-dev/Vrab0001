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
| 📅 Last Sync | 2026-09-27 12:13 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Analysis
  _Using ASX 200 historical price data, write a query with window functions to calculate: (1) 30-day rolling average price for each stock, (2) rank stocks by daily percentage change within each date, (3) identify the top 5 stocks with highest cumulative gains over the entire period using ROW_NUMBER and LAG to compute price differences. Return stock symbol, date, closing price, 30-day moving average, daily rank, and cumulative gain percentage. Order by date descending and rank ascending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-27.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning Pipeline
  _Download Australian Weather observations dataset (Bureau of Meteorology historical data available on Kaggle). Build a pandas script to: (1) handle missing values in temperature, rainfall, and wind speed columns (document your imputation strategy), (2) remove or flag duplicate records based on station ID and timestamp, (3) convert temperature to Celsius if needed and standardize column names to snake_case, (4) create a summary CSV showing data quality metrics (% missing, duplicate count, date range) for each weather station. Output cleaned data and quality report._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest2_2026-09-27.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: Data Ingestion & Reporting
  _Combine Python and SQL: (1) Use Python with pandas to download NSW Road Crash data, clean it (standardize postcode format, remove null crash severity, parse datetime fields), and load into a SQLite database with proper schema (tables: crashes, locations, vehicles). (2) Write SQL queries using CTEs to identify: crash hotspots (suburbs with >50 crashes in past 5 years), peak crash hours using HOUR() function, and calculate a severity score (fatalities × 3 + serious injuries × 2 + other injuries × 1) ranked by location. (3) Export results to CSV showing top 10 hotspots with their severity metrics and recommended safety interventions._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-09-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
