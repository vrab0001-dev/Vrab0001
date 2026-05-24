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
| 📅 Last Sync | 2026-05-24 12:00 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Performance Rankings with Running Averages
  _Using ASX 200 historical prices data, write a SQL query with window functions to: (1) Calculate the 20-day moving average for each stock's closing price using a window frame, (2) Rank stocks by their latest closing price within each sector using ROW_NUMBER(), (3) Use LAG() to calculate daily percentage change, (4) Filter for only stocks where the current price exceeds the 20-day moving average. Output should show: stock symbol, sector, latest close, 20-day moving average, daily % change, and rank within sector. Use a CTE to structure the moving average calculation separately._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data and write a Python script using pandas to: (1) Load the dataset and identify missing values, inconsistent date formats, and invalid location records, (2) Standardise all date columns to datetime format and extract year, month, day-of-week as new columns, (3) Clean location data by removing nulls and duplicates, (4) Create a new feature 'severity_score' (1-5) based on injury count and crash type, (5) Group crashes by local government area (LGA) and month, calculating mean severity and crash frequency, (6) Export cleaned data to a CSV file with summary statistics printed to console. Output should include data quality report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-24.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: SQL Aggregation + Python Reporting
  _Build an end-to-end data pipeline using Australian wine production statistics: (1) In SQL, write a query using GROUP BY and HAVING to identify regions where total production across all years exceeds 50,000 tonnes, rank regions by average production volume, and calculate year-over-year growth using window functions (LAG). Export results to CSV. (2) In Python, load the SQL output and create a pandas script that: calculates rolling 3-year average production by region, creates a new column for production volatility (std dev), identifies outlier years using IQR method, and generates a summary report showing top 5 regions by stability and top 5 by growth. (3) Visualise the results by exporting a final summary CSV with region, avg_production, volatility_score, and trend_direction (Up/Down/Stable)._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-05-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
