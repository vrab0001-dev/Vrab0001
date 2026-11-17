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
| 📅 Last Sync | 2026-11-17 16:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Rankings with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility within each month using ROW_NUMBER(). Then use a CTE to identify the top 5 most volatile stocks for each calendar month. Expected output: a table with month, stock_code, volatility_rank, rolling_std_dev, and closing_price. Use LAG() to calculate daily percentage returns, then STDDEV() as a window function partitioned by stock and 30-day windows._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data and perform the following: (1) Handle missing values in injury_level and crash_type columns using mode imputation. (2) Create a new feature 'time_of_day' by binning the crash_hour into periods (morning: 6-12, afternoon: 12-17, evening: 17-22, night: 22-6). (3) Standardise suburb names (strip whitespace, convert to title case). (4) Remove duplicate records based on crash_id, date, and location. (5) Export a cleaned CSV with 10 new columns. Expected deliverable: cleaned_nsw_crashes.csv with no null values in critical columns and consistent data types._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-17.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: SQL + Python ETL
  _Build a mini data pipeline: (1) Download Australian wine production statistics by region and vintage year. (2) Use Python pandas to load the CSV, clean region names (standardise case/spacing), validate vintage years (must be 1980-2024), and remove rows with null production volumes. (3) Calculate a new column 'production_per_capita' by joining with ABS population data by region (you may mock this if unavailable). (4) Export to a temporary staging table structure via Python. (5) Write SQL queries to: identify the top 3 wine regions by average production over the last 10 years, calculate year-on-year production growth rate using LAG(), and rank vintage years by total national output using ROW_NUMBER(). Expected output: (a) cleaned_wine_data.csv, (b) a SQL script with 3 analytical queries, (c) a summary report showing top regions and growth trends._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com) + ABS Census 2021 for population context`
  📁 Submit as: `quest3_2026-11-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
