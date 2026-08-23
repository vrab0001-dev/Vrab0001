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
| 📅 Last Sync | 2026-08-23 10:34 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate the 5-day moving average of closing prices for each stock using AVG() OVER a rolling window, (2) Rank stocks by their price momentum (current price vs 20-day average) using ROW_NUMBER() OVER, (3) Identify stocks that crossed above their 50-day moving average using LAG() to compare current close to previous 50-day average. Return stock ticker, date, close price, 5-day MA, momentum rank, and a flag indicating crossover events. Filter for top 20 stocks by momentum rank and order by date descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-23.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation
  _Download NSW Road Crash Data (contains crash severity, location, vehicle count, etc.). Write a Python/pandas script to: (1) Handle missing values in severity and location columns (document your strategy), (2) Standardise date formats and extract year/month/day, (3) Remove duplicate crash records based on crash ID and timestamp, (4) Create a new feature: crash density per local government area (LGA) per month, (5) Export a cleaned CSV with crashes aggregated by LGA, severity level, and month, showing crash count and average vehicles involved. Include data quality checks (row counts before/after cleaning, null value summary)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-23.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: SQL Analysis + Python ETL
  _Using Australian Wine Production Statistics data: (1) Write a Python script to extract and clean wine production data by region and vintage year (handle missing/inconsistent region names, convert volume to standardised units). (2) Load cleaned data into a local SQLite database. (3) Write a SQL query using CTEs to: calculate total production by region, rank regions by production volume (using DENSE_RANK), calculate year-over-year growth using LAG(), and identify regions with >20% production increase. (4) Export results showing region, vintage, production volume, growth rate, and region rank. Automate the entire pipeline so it can accept a new CSV file and re-run end-to-end. Document assumptions about data quality._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-08-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
