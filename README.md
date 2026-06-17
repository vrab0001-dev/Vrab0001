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
| 📅 Last Sync | 2026-06-17 12:32 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, calculate the 20-day and 50-day moving averages for each stock using window functions. Then identify stocks where the 20-day MA crossed above the 50-day MA in the last 30 days (a bullish signal). Use a CTE to calculate the moving averages, then another CTE to detect crossovers using LAG() to compare consecutive rows. Return the stock symbol, date of crossover, closing price at crossover, and the difference between the two moving averages. Order by most recent crossover first._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Classification
  _Download NSW Road Crash Data from data.nsw.gov.au. Load the CSV and perform the following: (1) Handle missing values in Crash Severity and Injuries columns by filling with 'Unknown' and 0 respectively. (2) Create a new column 'injury_category' that classifies crashes as 'Fatal' (deaths > 0), 'Serious' (serious injuries > 5), 'Moderate' (injuries 1-5), or 'Minor' (injuries = 0). (3) Remove duplicates based on Crash ID. (4) Filter for crashes in the last 5 years. (5) Export the cleaned dataset to a new CSV file with a timestamp in the filename. Print summary statistics showing counts per injury category._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-17.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Download Australian Weather observations data (Bureau of Meteorology dataset on Kaggle). Using Python: (1) Load the CSV, parse dates, and group by station and month. (2) Calculate the 30-year average temperature and rainfall for each month. (3) Create a new column flagging months where temperature deviates by >2 standard deviations from the 30-year mean as 'anomaly'. (4) Export the results (station, date, temp, rainfall, anomaly_flag) to a SQLite database with two tables: 'weather_observations' and 'climate_normals'. Using SQL: (5) Query the database to find the top 10 stations with the most temperature anomalies in the last decade. (6) Calculate the average temperature during anomaly months vs non-anomaly months for each station. Return station name, anomaly_count, avg_temp_anomaly_months, avg_temp_normal_months, and the difference._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-06-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
