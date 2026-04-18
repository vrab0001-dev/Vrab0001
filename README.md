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
| 📅 Last Sync | 2026-04-18 11:14 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Volatility Ranking with Window Functions
  _Using the ASX 200 historical stock prices dataset, calculate the 30-day rolling standard deviation of closing prices for the top 10 most volatile stocks. Use window functions (specifically ROW_NUMBER and OVER clauses) to rank stocks by volatility. Your query should: (1) Calculate daily percentage change in closing price, (2) compute rolling 30-day standard deviation using window frames, (3) rank stocks by max volatility in descending order, (4) return stock symbol, current price, rolling volatility, and volatility rank. Expected output: 10 rows with stock symbols and their volatility metrics ordered by rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Time Series Aggregation
  _Download the NSW Road Crash Data (contains crash incidents with dates, locations, severity). Clean the dataset by: (1) handling missing values in the 'Crash Severity' and 'Weather Condition' columns using appropriate imputation or removal, (2) converting date columns to datetime format, (3) removing duplicate crash records based on Crash ID, (4) standardising location names (trim whitespace, convert to title case). Then aggregate crashes by month and severity level to create a time series. Export the cleaned dataset to a new CSV file and a summary CSV showing monthly crash counts by severity. Expected output: two cleaned CSV files with no nulls in critical columns and consistent formatting._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-18.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Wine Production ETL: Load, Transform, Join with ABS Data
  _Build a mini ETL pipeline combining Wine Australia production statistics with ABS demographic data for Australian wine regions. Steps: (1) Use Python/pandas to load wine production data (CSV or scrape from Wine Australia summary), clean vintage years and production volumes, handle missing regions, (2) download ABS Census 2021 data for regional population counts, (3) create a SQLite database with two tables: 'wine_production' (vintage, region, volume, variety) and 'region_demographics' (region, population, postcode), (4) write SQL queries to: calculate production per capita by region, identify the top 3 regions by volume growth year-on-year using window functions (LAG), and find regions where production exceeds 1 million litres but population is under 50k. Expected output: a SQLite .db file with clean tables and a summary CSV showing top growing regions with per-capita production metrics._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com and ABS Census 2021 — abs.gov.au`
  📁 Submit as: `quest3_2026-04-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
