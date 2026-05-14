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
| 📅 Last Sync | 2026-05-14 11:58 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Rolling Averages
  _Using the ASX 200 historical prices dataset, write a query with window functions to: (1) Calculate the 20-day and 50-day rolling average closing price for each stock symbol, (2) Rank stocks by their current price relative to the 50-day average (highest outperformers first), (3) Use ROW_NUMBER to identify the top 3 best and worst performers in the last 90 days by percentage gain/loss. Return columns: symbol, date, close_price, avg_20day, avg_50day, rank, performance_pct. Filter for the last 90 trading days only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Scoring
  _Download the NSW Road Crash Data (data.nsw.gov.au). Write a Python script using pandas to: (1) Load the CSV and identify missing values, data type inconsistencies, and duplicates, (2) Clean the dataset by handling NaN values strategically (drop or fill based on column importance), (3) Create a new 'severity_score' column (1-5 scale) based on number of fatalities, injuries, and vehicle count, (4) Export the cleaned dataset to a new CSV. Document which rows were removed and why. Expected output: cleaned CSV with 3+ new derived columns and a cleaning report (print summary statistics before/after)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-14.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL Pipeline
  _Build a mini ETL pipeline combining Python and SQL: (1) Use Python pandas to scrape or load wine production statistics by region and vintage year from Wine Australia data or a Kaggle wine dataset, (2) Clean the data (handle missing values, standardise region names, convert production volumes to consistent units), (3) Load the cleaned data into a SQLite database (create tables: regions, vintages, production_stats), (4) Write SQL queries to calculate: total production by region over last 5 years, year-on-year growth %, and identify the top 3 growing regions. Return a summary report showing region, total_production_tonnes, growth_pct, and ranking. Submit: cleaned CSV, SQLite .db file, and SQL query file._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia or Kaggle`
  📁 Submit as: `quest3_2026-05-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
