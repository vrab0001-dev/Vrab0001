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
| 📅 Last Sync | 2026-11-13 14:52 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, calculate a 20-day moving average and identify the top 5 stocks by momentum (price change %) over the last 30 days. Use window functions ROW_NUMBER() and LAG() to rank stocks by their price volatility (standard deviation of daily returns) within each sector. Return: stock_code, sector, current_price, moving_avg_20day, momentum_pct, volatility_rank. Filter for stocks with volume > 1M shares and order by momentum descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Classification
  _Download the NSW Road Crash Data (CSV format). Clean the dataset by: (1) handling missing values in injury_type and crash_type columns (document imputation strategy), (2) standardising date formats to YYYY-MM-DD, (3) removing duplicate records based on crash_id, (4) creating a new severity_score column (0-10 scale) based on number_of_casualties and speed_zone, (5) exporting cleaned data to a new CSV. Provide a data quality report showing before/after row counts, missing value percentages, and outliers detected in casualty counts._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-13.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL Pipeline
  _Build a Python script that: (1) extracts wine production data by region and varietal from the Australian Wine Production Statistics dataset, (2) cleans region names (standardise case, remove extra whitespace), (3) filters for top 10 producing regions, (4) loads the cleaned data into a local SQLite database with proper schema (region, varietal, production_volume_tonnes, year), (5) executes a SQL query to calculate year-over-year growth % for each region, ranked by growth rate. Output: a CSV file containing region, varietal, production_volume_tonnes, year, and yoy_growth_pct, sorted by highest growth._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-11-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
