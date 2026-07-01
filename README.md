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
| 📅 Last Sync | 2026-07-01 12:09 AEDT |

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
  _Using ASX 200 historical stock price data, write a query that calculates a 30-day rolling average price and identifies momentum shifts. For each stock symbol and date, compute: (1) the closing price, (2) a 30-day LAG of the closing price, (3) ROW_NUMBER() partitioned by symbol ordered by date, (4) the percentage change from 30 days ago. Then use a CTE to filter only dates where the percentage change exceeds 5% (either direction) and rank these momentum events by magnitude within each stock. Return symbol, date, closing_price, pct_change, and momentum_rank. Order by symbol and date._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data (2020-2026). Load the CSV into a pandas DataFrame and perform the following: (1) Handle missing values in crash severity, location, and injury count columns (document your strategy). (2) Parse datetime columns correctly and extract day_of_week and hour_of_day features. (3) Standardise location data by removing leading/trailing whitespace and converting to title case. (4) Create a severity_category column mapping numeric codes to 'Fatal', 'Serious Injury', 'Other Injury', 'Non-Injury'. (5) Remove duplicate crash records based on crash ID and timestamp. (6) Save the cleaned dataset to a new CSV file. Output a summary report showing: original row count, cleaned row count, missing values per column before/after, and the first 5 rows of cleaned data._
  📦 Dataset: `NSW Road Crash Data — NSW Open Data Portal (data.nsw.gov.au)`
  📁 Submit as: `quest2_2026-07-01.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end data engineering pipeline: (1) In Python, load Australian weather observations data (temperature, rainfall, pressure from Bureau of Meteorology or Kaggle jsphyg dataset). Clean the data: handle missing values via interpolation, standardise station names, validate temperature ranges (-10°C to 50°C for Australia). (2) Create a CSV output with clean records including: station_id, date, temperature, rainfall, pressure. (3) Load this cleaned CSV into a SQL database (SQLite or PostgreSQL). (4) Write a SQL query using window functions to detect temperature anomalies: compute a 7-day rolling average temperature per station, then flag any day where actual temp deviates more than 2 standard deviations from the rolling average. (5) Return: station_id, date, actual_temp, rolling_avg_temp, z_score, is_anomaly. Export anomaly results to a final CSV. Document your anomaly detection logic in comments._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology or Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-07-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
