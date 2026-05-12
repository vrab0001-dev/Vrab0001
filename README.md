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
| 📅 Last Sync | 2026-05-12 11:51 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates for each trading day in 2025: (1) the daily percentage change for each stock, (2) the rank of each stock by performance that day using RANK(), (3) a 5-day rolling average of the closing price using a window frame, and (4) the cumulative return since the start of the year using SUM() OVER. Filter to show only the top 10 performing stocks on the last trading day of the dataset. Your output should include: stock_code, trading_date, daily_pct_change, rank_that_day, rolling_5day_avg, cumulative_return_ytd._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-05-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download the NSW Road Crash Data dataset. Write a Python script using pandas that: (1) loads the CSV file, (2) handles missing values in the 'Crash Severity' and 'Crash Type' columns by filling with 'Unknown', (3) removes duplicate crash records based on Crash ID, (4) converts date columns to datetime format, (5) extracts the year and month from the crash date, (6) creates a new column 'is_fatal' (1 if severity is 'Fatal', 0 otherwise), and (7) exports a cleaned CSV with summary statistics showing crash counts by severity and month for 2024. Print the first 5 rows and data types to verify correctness._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-12.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Counting: Python ETL + SQL Analysis
  _Using the Melbourne pedestrian counting dataset (from Melbourne Open Data Portal): (1) Write a Python script to download/load the dataset and clean it: remove rows with null counts, convert timestamp to datetime, extract hour and day_of_week, and export to a CSV named 'pedestrian_clean.csv'. (2) Create a SQL query that loads this cleaned CSV into a temporary table, then calculates: the average pedestrian count by hour of day and sensor location, identifies the peak hour for each sensor, and uses a CTE to rank sensors by total daily foot traffic. (3) Output the top 5 busiest sensors, their peak hour, and average counts. Ensure your Python script documents each step and your SQL uses at least one CTE and one window function._
  📦 Dataset: `Melbourne pedestrian counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-05-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
