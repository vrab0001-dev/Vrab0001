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
| 📅 Last Sync | 2026-09-08 11:47 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 20-day rolling average price for each stock, (2) the rank of each stock by daily percentage change within its sector, and (3) identify stocks that hit a new 52-week high on each trading date. Use ROW_NUMBER(), AVG() OVER(), and RANK() OVER() partitioned by stock ticker and date windows. Return top 10 stocks with the largest positive momentum (current price vs. 20-day average) sorted by sector and date._
  📦 Dataset: `ASX 200 Historical Stock Data — Kaggle`
  📁 Submit as: `quest1_2026-09-08.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning & Aggregation
  _Download or load Australian Bureau of Meteorology weather observations (or use the Kaggle Australian Weather dataset). Write a Python/pandas script to: (1) handle missing values in temperature, rainfall, and wind speed columns using forward-fill and interpolation, (2) identify and flag outliers using IQR method, (3) aggregate daily observations to monthly summaries by location, (4) create a new 'season' column based on month (meteorological seasons), and (5) export cleaned data to CSV. Validate that no NaN values remain in critical columns and document your cleaning decisions._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest2_2026-09-08.py`
- [ ] ⚡ **Python + SQL Quest:** NSW Road Crash Injury Severity Pipeline
  _Combine Python and SQL to build a mini ETL pipeline: (1) Load NSW Road Crash Data (data.nsw.gov.au) using pandas, cleaning location coordinates, date formats, and injury severity classifications. (2) Use Python to geocode crash locations into LGA (Local Government Area) using a reference lookup or manual mapping. (3) Load cleaned data into a SQLite database. (4) Write SQL queries to identify: top 5 LGAs by crash frequency, average injury severity by road type, and crashes occurring during off-peak hours (10pm-6am) with speed limits >80km/h. (5) Export results to CSV. Document data quality issues found and how you resolved them._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-09-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
