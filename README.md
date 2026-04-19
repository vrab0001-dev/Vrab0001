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
| 📅 Last Sync | 2026-04-19 11:23 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Performance Rankings with Window Functions
  _Using ASX 200 historical stock price data, write a query that calculates for each stock: (1) the 30-day moving average of closing price using a window function, (2) the rank of each stock by percentage gain over the last quarter using RANK(), and (3) the previous day's closing price using LAG(). Filter for the top 20 stocks by percentage gain. Output should include: ticker, company_name, current_close, 30day_moving_avg, rank_by_gain, previous_close, and pct_gain columns, ordered by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains multiple CSV files with crash details, vehicle info, and casualties). Write a Python script using pandas that: (1) loads and merges crash records with casualty data, (2) handles missing values in 'speed_limit' and 'crash_type' columns (impute or drop as appropriate), (3) standardises date formats and extracts crash_hour from timestamp, (4) identifies and flags outlier crash severity scores, (5) produces a summary CSV showing crashes by local government area, hour of day, and severity level. Include data quality checks (row counts before/after cleaning)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-19.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Wine Production Analysis Pipeline
  _Build an end-to-end data pipeline: (1) In Python, scrape or load Australian wine production statistics (by region and vintage year) from Wine Australia data or a Kaggle wine dataset. Clean the data: normalise region names, handle missing vintage years, and convert production volumes to a standard unit (tonnes or litres). (2) Load the cleaned data into a SQLite database with proper schema (regions table, production table with foreign keys). (3) Write SQL queries to find: the top 5 wine-producing regions by total production, year-over-year growth rate for each region using window functions, and regions with declining production trends. (4) Export results to CSV and create a summary report showing insights. Expected output: cleaned_wine_data.csv, wine_analysis.db, and summary_report.txt with query results._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com or Wine Reviews Dataset (Kaggle)`
  📁 Submit as: `quest3_2026-04-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
