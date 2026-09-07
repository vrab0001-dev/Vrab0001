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
| 📅 Last Sync | 2026-09-07 11:36 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Moving Average Crossover Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate the 20-day and 50-day moving averages for the top 5 most traded stocks. Then identify crossover points where the 20-day MA crosses above or below the 50-day MA. Return stock_symbol, date, close_price, ma_20, ma_50, and a column indicating 'BULLISH_CROSS' or 'BEARISH_CROSS' or NULL. Use CTEs to structure the query cleanly. Order results by stock and date._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Categorisation
  _Download NSW Road Crash Data (contains raw incident records with inconsistent formatting, missing values, and mixed data types). Write a Python script using pandas to: (1) handle missing values in injury_count and speed_limit columns intelligently, (2) standardise location names (remove extra spaces, uppercase inconsistencies), (3) create a new severity_category column based on injury_count thresholds (0=No Injury, 1-2=Minor, 3+=Major), (4) filter crashes from the last 24 months only, (5) export the cleaned dataset to CSV with proper encoding. Document your data quality assumptions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-07.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends Pipeline: Python to SQL
  _Build an end-to-end data pipeline: (1) Use Python/pandas to fetch or load Bureau of Meteorology historical weather observations (temperature, rainfall, humidity across major Australian cities). (2) Clean the data: convert temperature to numeric, handle missing rainfall values by forward-filling, standardise city names to proper case. (3) Load the cleaned data into a SQLite database with a weather_observations table. (4) Write a SQL query using window functions to calculate the 7-day rolling average temperature for each city and identify the hottest consecutive 3-day period per city in the dataset. Return city, date, temp, rolling_avg_7day, and hottest_period_flag. Save Python script and SQL query as separate files, with clear documentation of the ETL flow._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-09-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
