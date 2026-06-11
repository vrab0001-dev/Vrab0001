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
| 📅 Last Sync | 2026-06-11 12:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Moving Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate a 20-day moving average of closing price for each stock symbol, (2) Rank stocks by their current price relative to their 20-day moving average (greatest outperformers first), (3) Use LAG to calculate day-over-day price changes, (4) Filter only stocks where the current price is at least 5% above their 20-day moving average. Return stock symbol, current price, 20-day moving average, percentage above MA, day-over-day change, and rank. Order by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-11.sql`
- [ ] 🐍 **Python Quest:** Clean and Standardise NSW Road Crash Data
  _Download the NSW Road Crash Data dataset. Write a Python/pandas script to: (1) Load the CSV and inspect data types and missing values, (2) Handle missing values in critical columns (crash location, severity, vehicle count) using appropriate strategies (drop, forward-fill, or impute), (3) Standardise location data by converting street names to title case and removing leading/trailing whitespace, (4) Create a new column 'crash_month_year' from the date field, (5) Remove duplicate rows based on crash ID, (6) Export the cleaned dataset to a new CSV file. Document your data quality decisions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-11.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: Load, Clean, Analyse with SQL
  _Using the Australian Weather observations dataset from Bureau of Meteorology (or Kaggle equivalent): (1) Write a Python script to download/load the CSV, clean temperature and rainfall columns (handle missing values, outliers, data type conversions), and create date-time columns, (2) Load the cleaned data into a SQLite database, (3) Write a SQL query using CTEs to: calculate monthly average temperature and total rainfall by station, rank stations by temperature variance, identify months where rainfall exceeded the 90th percentile for that station, (4) Return station name, month, avg temperature, total rainfall, rainfall percentile rank, and temperature variance rank. Order by station and month. Export final results to CSV._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
