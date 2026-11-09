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
| 📅 Last Sync | 2026-11-09 14:23 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 20-day and 50-day rolling average closing price for each stock ticker, (2) Rank stocks by their price momentum (current price vs 50-day average) within each trading month, (3) Identify stocks that crossed above their 50-day average in the last 30 days. Use ROW_NUMBER() and LAG() window functions. Return: ticker, date, close_price, ma_20, ma_50, momentum_rank, and a flag indicating crossover events. Order by date descending and momentum_rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Incident Type Classification
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python pandas script to: (1) Load the crash data CSV, (2) Clean missing values in critical columns (crash_date, location, severity, vehicle_type), (3) Standardise date formats and extract year, month, hour_of_day from crash timestamps, (4) Categorise crashes into severity buckets (Fatal, Serious Injury, Other Injury, Non-Injury) based on the injury_type column, (5) Remove duplicate records based on crash_id, (6) Export the cleaned dataset to a new CSV file with a timestamp suffix. Document any data quality issues found in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-09.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: SQL Analysis + Python ETL Pipeline
  _Using the Bureau of Meteorology / Australian Weather observations dataset (available on Kaggle): (1) Write a Python script to download/load the weather CSV, perform initial cleaning (handle missing temps, standardise station names, validate date ranges), and load it into a local SQLite database. (2) Write SQL queries to: identify stations with the highest temperature variance by season, calculate the 3-month rolling average of rainfall by region, rank states by average maximum temperature for each month of the year using window functions. (3) Export SQL results back to Python, create a summary DataFrame showing top 5 hottest and wettest regions, and save as a formatted CSV report. Expected deliverables: (a) Python ETL script, (b) SQL query file, (c) Summary report CSV._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg)`
  📁 Submit as: `quest3_2026-11-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
