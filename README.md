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
| 📅 Last Sync | 2026-08-17 10:32 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that ranks each stock by its percentage gain over the last 90 trading days. Use window functions (ROW_NUMBER, RANK, LAG) to calculate the percentage change from the opening price 90 days ago to the most recent closing price. Include columns: stock_code, company_name, price_90_days_ago, current_price, percentage_gain, and rank_by_gain. Filter to show only the top 20 performers. Use a CTE to first calculate the 90-day lagged prices, then perform the ranking in the main query._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Geocoding Preparation
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python pandas script that: (1) loads the CSV, (2) identifies and handles missing values in key columns (latitude, longitude, crash_type, severity), (3) removes duplicate crash records based on crash_id and timestamp, (4) standardises the crash_type values to consistent casing and removes typos, (5) filters crashes from the last 12 months, (6) creates a new column 'severity_category' grouping severity levels into 'Minor', 'Moderate', 'Severe', (7) exports the cleaned dataset to a new CSV. Print a data quality report showing row counts before/after cleaning and missing value percentages._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-17.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Trend Analysis: Python ETL + SQL Analytics
  _Complete a full data engineering pipeline: (1) Use Python & pandas to scrape or load wine production statistics (by region and year) from Wine Australia or a Kaggle wine dataset. Clean the data: standardise region names, handle any missing production volumes, and convert currency/units to consistent formats. (2) Load the cleaned data into a SQLite database with two tables: regions (region_id, region_name, state) and production (production_id, region_id, year, volume_tonnes, value_aud). (3) Write SQL queries to find: the top 3 regions by average production volume over the last 10 years, the year-on-year growth rate for each region using LAG(), and regions with declining production using a CTE. (4) Export results to CSV. Provide Python script and SQL file separately._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia or Kaggle`
  📁 Submit as: `quest3_2026-08-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
