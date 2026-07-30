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
| 📅 Last Sync | 2026-07-30 11:15 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Analysis with Window Functions
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) 30-day rolling average price for each stock, (2) rank stocks by daily percentage change within each date partition, (3) identify the first date each stock reached its 52-week high using ROW_NUMBER and LEAD functions. Return stock symbol, date, closing price, 30-day MA, daily rank, and first 52-week high date. Use a CTE to pre-calculate daily percentage changes._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data (contains crash records with location, time, severity, vehicle types). Write a Python/pandas script to: (1) clean date/time columns and handle missing values in severity fields, (2) create new features: hour of day, day of week, crash severity category (collapse into 3-4 categories), (3) extract suburb/LGA from location data, (4) identify and remove duplicate records based on crash ID and timestamp. Export cleaned dataset to CSV and generate a summary report showing data quality metrics (missing %, duplicates removed, record count before/after)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-30.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end data engineering pipeline using Australian Weather observations (Bureau of Meteorology dataset): (1) In Python/pandas, load weather CSV data, clean temperature and rainfall columns, handle missing values using forward-fill or interpolation, and aggregate daily data to monthly summaries by station. (2) Load cleaned data into a SQLite database (create schema with tables for stations and monthly_metrics). (3) Write SQL queries using window functions to: calculate 10-year rolling average temperature by station, identify months with anomalous rainfall (values >2 std devs from mean), and rank stations by temperature variability. (4) Export results showing station name, month, temperature anomaly flag, and rainfall rank. Document your data quality checks and transformations in comments._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-07-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
