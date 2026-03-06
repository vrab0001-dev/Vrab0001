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
| 📅 Last Sync | 2026-03-06 16:01 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns & Momentum Ranking
  _Using ASX 200 historical price data, calculate daily percentage returns for each stock. Use window functions (ROW_NUMBER, LAG, RANK) to: 1) Rank stocks by their 5-day average return (highest to lowest) on each date, 2) Identify stocks with consecutive positive return days, 3) Flag any stock that jumped into the top 10 performers within a single day. Return a result set with stock symbol, date, daily return %, 5-day avg return, rank, and a boolean flag for new top-10 entrants. Use a CTE to pre-calculate the 5-day rolling average._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Export Pipeline
  _Download NSW Road Crash Data from the NSW government open data portal. The dataset contains messy crash records with missing values, inconsistent date formats, and duplicate entries. Write a Python/pandas script to: 1) Load the CSV and inspect data quality (missing %, duplicates), 2) Standardize date columns to YYYY-MM-DD format, 3) Handle missing values in 'Crash Type', 'Severity', and 'Speed Limit' columns using forward-fill or mode imputation, 4) Remove exact duplicates and near-duplicates (same location, date, and crash type within 1 minute), 5) Export a cleaned CSV and a data quality report (rows removed, imputation counts, format changes). Document your decisions in code comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-06.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL: From CSV to Analytics Query
  _Build a mini ETL pipeline: 1) Use Python/pandas to load Australian wine production statistics (by region and vintage year) from the Wine Australia dataset. Clean the data by: removing non-numeric production values, standardizing region names (title case, strip whitespace), and handling missing vintage years by forward-filling or removing rows. 2) Create a SQLite database with a 'wine_production' table. 3) Write a SQL query using CTEs and window functions to: rank regions by total production volume across all years, calculate year-on-year growth % for each region, and identify the top 3 regions with the highest growth trajectory (using LAG and LEAD). Export results to a CSV file showing region, vintage, volume, YoY growth %, and regional rank. Include error handling and logging in your Python script._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com open data`
  📁 Submit as: `quest3_2026-03-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
