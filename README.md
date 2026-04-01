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
| 📅 Last Sync | 2026-04-01 12:21 AEDT |

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
  _Using ASX 200 historical price data, write a query with window functions to: (1) Calculate the 30-day price change percentage for each stock using LAG, (2) Rank stocks by momentum within each sector using RANK() OVER (PARTITION BY sector ORDER BY price_change DESC), (3) Identify the top 3 performers and bottom 3 performers per sector, (4) Include a CTE to filter only stocks with at least 20 trading days of data in the last month. Output should show stock_code, sector, current_price, price_30d_ago, momentum_rank, and momentum_percentage._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains messy location strings, missing values, inconsistent date formats). Write a Python script using pandas to: (1) Parse and standardise date columns, (2) Clean location data by extracting suburb/LGA from inconsistent text fields, (3) Handle missing values in severity and vehicle type columns using appropriate imputation, (4) Create a CSV summary by suburb showing total crashes, fatalities, and injuries per month, (5) Generate a data quality report showing % missing values before and after cleaning. Output two files: cleaned_crashes.csv and data_quality_report.txt._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-01.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring: SQL Analysis + Python Reporting
  _Using Great Barrier Reef monitoring data (containing sensor readings, coral health metrics, temperature logs): (1) PYTHON STEP: Load the raw dataset, clean date/time columns, handle missing coral_health_score values, convert temperature readings to standardised units (Celsius), remove duplicate sensor records. Save cleaned data to a database or CSV. (2) SQL STEP: Query the cleaned data to calculate rolling 12-month average temperature per reef_section using window functions (AVG() OVER with ROWS BETWEEN), identify sections with declining coral health trends using LAG(), rank sections by health status. (3) PYTHON STEP: Read SQL results, create a visualisation-ready summary CSV and a markdown report highlighting at-risk reef sections and temperature anomalies. Output files: reef_analysis_summary.csv, reef_health_report.md._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-04-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
