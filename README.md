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
| 📅 Last Sync | 2026-05-08 11:52 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 20-day moving average and identify stocks with the strongest upward momentum. Write a query using window functions (ROW_NUMBER, LAG) to: (1) compute the closing price change day-over-day for each stock, (2) calculate a 20-day moving average of close prices partitioned by stock symbol, (3) rank stocks by their most recent momentum score (latest close - 20-day MA), and (4) return the top 10 stocks with the strongest positive momentum. Include stock symbol, latest close price, 20-day MA, momentum score, and rank. Use a CTE to organize the window function logic clearly._
  📦 Dataset: `ASX 200 historical stock prices — Kaggle`
  📁 Submit as: `quest1_2026-05-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download the NSW Road Crash Data from the NSW Government open data portal. Write a Python script using pandas to: (1) load the CSV file and inspect data quality (missing values, duplicates, data types), (2) clean the dataset by handling missing values in critical columns (crash location, date, injury count), (3) convert date columns to datetime format, (4) extract new features (day of week, hour of day, season) from the crash datetime, (5) filter crashes involving fatalities or serious injuries only, and (6) aggregate crashes by local government area (LGA) and hour of day to identify high-risk times and locations. Save the cleaned and aggregated results to a new CSV file with meaningful column names and proper data types._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-08.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: SQL Analysis + Python Data Pipeline
  _Build an end-to-end data pipeline using Australian Weather observations data (Bureau of Meteorology / Kaggle). (1) In Python: load the raw weather CSV, clean temperature and rainfall columns (handle missing/invalid values), standardise station names, and export a cleaned parquet file. (2) In SQL: create a table from the cleaned parquet data, then write a complex query using window functions and CTEs to: identify the top 5 weather stations by average monthly temperature anomaly (deviation from station's historical mean), calculate consecutive days above 35°C using LAG/LEAD, rank months by rainfall quartile within each station, and return results showing station name, month, temperature anomaly, max consecutive hot days, and rainfall quartile rank. (3) Document your cleaning decisions and explain why certain anomalies were handled the way they were._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
