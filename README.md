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
| 📅 Last Sync | 2026-04-26 11:26 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Moving Average Crossover Detection
  _Using ASX 200 historical stock price data, write a SQL query with window functions to calculate 20-day and 50-day moving averages for a single stock ticker. Identify all dates where the 20-day MA crosses above the 50-day MA (bullish signal) and crosses below (bearish signal). Use LAG or LEAD to detect the crossover points. Return a result set with date, close price, 20-day MA, 50-day MA, and signal type (BUY/SELL/HOLD). Order by date descending._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-04-26.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data and build a pandas cleaning script that: (1) handles missing values in crash location, severity, and vehicle count columns; (2) standardises date/time formats to ISO 8601; (3) categorises crashes by severity (fatal/serious injury/other injury/non-injury) based on the severity column; (4) removes duplicate records based on crash ID and timestamp; (5) exports cleaned data to a CSV file with a timestamp suffix. Log the number of rows removed at each step. Your script should be reusable and accept the input file path as a parameter._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-26.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Health Trend Analysis Pipeline
  _Build an end-to-end pipeline: (1) In Python/pandas, load Great Barrier Reef monitoring data (coral cover %, bleaching events, temperature anomalies). Clean the data by handling missing values, standardising date formats, and aggregating by reef zone and year. Export to a CSV staging file. (2) In SQL, load the cleaned CSV into a temp table. Write a query using CTEs to calculate year-over-year changes in coral health metrics by zone, rank zones by health decline using RANK() OVER, and identify the top 3 zones needing intervention. Return zone, year, coral_cover%, bleaching_event_count, yoy_change%, and danger_rank. Document your assumptions about data quality._
  📦 Dataset: `Great Barrier Reef monitoring data — aims.gov.au`
  📁 Submit as: `quest3_2026-04-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
