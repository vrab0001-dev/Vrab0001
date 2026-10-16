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
| 📅 Last Sync | 2026-10-16 12:58 AEDT |

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
  _Using ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) the 20-day moving average for each stock, (2) the rank of stocks by daily percentage gain within each date partition, and (3) identify stocks where today's close price exceeds the 20-day moving average. Use ROW_NUMBER() or RANK() to find top 5 gainers per trading day. Return stock symbol, date, close price, 20-day MA, daily % change, and rank. Filter for dates in Q3 2024 only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Incident Classification
  _Download the NSW Road Crash Data (contains incident reports with missing values, inconsistent formatting, and duplicate records). Clean the dataset by: (1) handling missing values in severity and crash type columns using appropriate imputation, (2) standardising suburb names to title case and removing leading/trailing whitespace, (3) converting date columns to datetime format, (4) removing exact duplicate rows, (5) creating a new 'crash_category' column that classifies crashes as 'Fatal', 'Serious Injury', 'Other Injury', or 'Non-Injury' based on severity column. Export the cleaned dataset to a CSV file. Provide a summary report showing row count before/after cleaning and missing value percentages per column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-16.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL: Database Population & Trend Analysis
  _Build a Python script that: (1) extracts wine production data from the Australian wine production statistics dataset (vintage year, region, variety, production volume in litres), (2) cleans and validates the data (remove nulls, standardise region names, convert volumes to consistent units), (3) creates a SQLite database with a 'wine_production' table, and (4) loads the cleaned data into the table. Then, write SQL queries to: (a) calculate the total production volume by region and vintage year using GROUP BY and ORDER BY, (b) use a CTE to identify regions where production volume increased year-over-year, (c) rank wine varieties by total production across all years using ROW_NUMBER(). Return the top 5 regions by total production and top 10 varieties by volume. Document your ETL pipeline steps in comments._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com / Kaggle`
  📁 Submit as: `quest3_2026-10-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
