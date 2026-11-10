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
| 📅 Last Sync | 2026-11-10 15:59 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate the 30-day price momentum for each stock. Use ROW_NUMBER() to rank stocks by momentum within each date partition, and LAG() to compare current price against the price 30 days ago. Return the top 10 stocks with highest positive momentum on the most recent date in the dataset, showing stock symbol, current price, price 30 days ago, momentum percentage, and rank. Use a CTE to calculate the momentum in a separate step for clarity._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download the NSW Road Crash Data from data.nsw.gov.au. Load the CSV into pandas and perform the following: (1) Remove rows with missing values in critical columns (crash date, severity, location). (2) Convert crash date to datetime format. (3) Create a new column 'month_year' extracted from crash date. (4) Group by month_year and severity to count crashes per severity level per month. (5) Calculate a 3-month rolling average of total crashes. (6) Export the cleaned and aggregated data to a new CSV file named 'nsw_crash_summary.csv'. Print summary statistics showing trend direction (increase/decrease) over the last 6 months._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-10.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL Pipeline
  _Build a Python script that extracts Australian wine production data (by region and variety) from wineaustralia.com or a Kaggle wine dataset. (1) Use pandas to clean the data: handle missing values, standardize region names, convert production volumes to consistent units (tonnes). (2) Create a SQLite database with a schema containing tables for regions, varieties, and production facts. (3) Use SQL to write a query that ranks wine regions by total production volume across all varieties in the most recent year, and calculates year-on-year growth percentage. (4) Create a second query using a CTE to identify 'emerging varieties' (varieties that increased production by >20% YoY). (5) Export both query results to separate CSV files. Include error handling for missing data and log the ETL process with timestamps._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia or Kaggle`
  📁 Submit as: `quest3_2026-11-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
