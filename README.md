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
| 📅 Last Sync | 2026-03-17 16:13 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using ASX 200 historical stock price data, write a SQL query that calculates a 20-day moving average of closing prices and identifies momentum shifts for each stock. Use window functions ROW_NUMBER() and LAG() to: (1) rank stocks by price change percentage within each trading day, (2) calculate the 20-day moving average using a window frame, (3) detect when a stock crosses above/below its moving average, and (4) return the top 10 stocks with the strongest upward momentum crossovers in the last 30 trading days. Include date, stock symbol, closing price, moving average, and momentum signal (crossover type) in your output._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download the NSW Road Crash Data (contains incidents, locations, severity, vehicle types, dates). Write a Python/pandas script that: (1) loads the CSV and inspects for missing values, duplicates, and data type mismatches, (2) cleans the dataset by handling nulls in critical columns (severity, crash date, location) and standardizing location names to remove whitespace/case inconsistencies, (3) creates a new feature 'time_of_day' by binning crash hours into periods (Night 22-06, Morning 06-12, Afternoon 12-18, Evening 18-22), (4) aggregates crashes by local government area and time_of_day to identify high-risk periods, and (5) exports a cleaned CSV with summary statistics showing total crashes, severity distribution, and top 5 LGAs by incident count. Validate your cleaning by comparing row counts before/after._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-17.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring: Python ETL + SQL Analytics
  _Build a mini data pipeline using Great Barrier Reef monitoring data (coral bleaching, water temperature, observation dates, reef zones). Step 1 (Python): Load the raw CSV, clean date formats to ISO 8601, remove rows with missing temperature readings, standardize reef zone names to title case, and calculate a new column 'temperature_anomaly' as (observed_temp - 30-year_historical_mean). Save the cleaned data to a new CSV. Step 2 (SQL): Load the cleaned CSV into a database, then write a query using CTEs and window functions to: (1) identify the top 3 reef zones by bleaching severity (using ROW_NUMBER), (2) calculate year-over-year temperature change using LAG(), (3) flag zones where bleaching increased despite stable/cooling temperatures (anomaly detection), and (4) return a summary showing zone name, current bleaching percentage, temperature trend, and anomaly flag. Your output should help identify reef zones requiring urgent intervention._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-03-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
