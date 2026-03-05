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
| 📅 Last Sync | 2026-03-05 16:04 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Ranking with Moving Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate daily percentage returns for each stock, (2) Rank stocks by return within each trading date using ROW_NUMBER(), (3) Compute a 5-day moving average of closing prices for each stock using LAG(), (4) Identify the top 10 performers and bottom 10 performers for the most recent trading date. Use a CTE to structure the window function calculations, then filter and order results by rank. Expected output: stock_code, trading_date, daily_return_pct, rank_within_date, moving_avg_5day, ranked_position._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-03-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Incident Type Classification
  _Download the NSW Road Crash Data and perform the following: (1) Load the CSV and identify missing values, outliers, and inconsistent entries in crash severity, location, and vehicle type columns, (2) Clean date/time fields and handle timezone issues, (3) Standardise location names and remove duplicates, (4) Create a new feature categorising incidents as 'Fatal', 'Serious Injury', 'Minor Injury', or 'Non-Injury' based on available severity indicators, (5) Export a cleaned CSV with summary statistics showing crash counts by type, location, and year. Use pandas and Python best practices for data validation._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-05.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: Extract, Clean, Transform & Analyse
  _Create an end-to-end data pipeline: (1) In Python, fetch or load Australian wine production statistics (volumes, varieties, regions, years) and clean the dataset (handle missing values, standardise region names, convert units to consistent format like tonnes/litres), (2) Load the cleaned data into a local SQLite database using Python, (3) Write SQL queries to: calculate total production by region and variety across all years, compute year-over-year growth rates using LAG(), identify top 5 performing regions and varieties using window functions and CTEs, generate a summary report showing production trends, (4) Export results back to Python and create a summary CSV with insights. Expected deliverables: cleaned CSV, SQLite DB schema, SQL queries, and final analysis CSV._
  📦 Dataset: `Australian wine production statistics — wineaustralia.com open data`
  📁 Submit as: `quest3_2026-03-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
