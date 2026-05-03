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
| 📅 Last Sync | 2026-05-03 11:44 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Detection with Window Functions
  _Using ASX 200 historical price data, write a SQL query with window functions to identify momentum shifts. Calculate a 5-day moving average of closing prices using AVG() OVER (ORDER BY date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW). Then use LAG() to compare each day's price to the previous day, and identify days where the price crossed above the 5-day MA (bullish signal). Return: date, closing_price, moving_avg_5day, price_change, and a signal column ('BULLISH_CROSS', 'BEARISH_CROSS', or 'NEUTRAL'). Filter for the last 90 days of data. Sort by date descending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash Data (from data.nsw.gov.au). Load the CSV into pandas. Clean the dataset: (1) Remove rows with missing values in critical columns (crash_date, severity, location). (2) Convert crash_date to datetime format. (3) Standardise the 'severity' column (map variations like 'Fatal', 'fatal', 'FATAL' to consistent casing). (4) Extract suburb from location string if it contains commas. (5) Create a new 'risk_score' column: assign scores 1-5 based on severity (1=other, 5=fatal), then multiply by the count of vehicles involved. (6) Export the cleaned dataset to a new CSV file with '_cleaned' suffix. Print summary statistics: total rows processed, rows removed, unique suburbs, top 5 suburbs by average risk_score._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-03.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Trend Analysis Pipeline
  _Build an end-to-end pipeline: (1) Download AIHW health expenditure data (CSV format, by health service or state). (2) Use Python/pandas to load, clean, and aggregate total expenditure by state and year. (3) Calculate year-over-year percentage change and identify states with fastest growth. (4) Export the cleaned aggregated data to a SQL-ready CSV (with columns: state, year, total_expenditure, yoy_change_percent). (5) Create a SQL query using CTEs: first CTE ranks states by average 5-year expenditure growth (newest 5 years available), second CTE calculates cumulative expenditure per state since 2015. Final SELECT should return: state, rank_by_growth, cumulative_expenditure_since_2015, latest_year_total. (6) Document your Python script with comments explaining each transformation step._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-05-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
