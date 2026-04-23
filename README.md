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
| 📅 Last Sync | 2026-04-23 11:24 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Rankings
  _Using ASX 200 historical price data, write a query with window functions to calculate the 30-day rolling return percentage for each stock symbol. Use ROW_NUMBER() to rank stocks by rolling return within each date partition, and LEAD() to compare current closing price with price 30 days ago. Return top 10 best and bottom 10 worst performers on the most recent date in the dataset. Include columns: symbol, date, close_price, price_30days_ago, rolling_return_pct, and rank_within_date._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-23.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from the NSW government open data portal. Build a Python script using pandas that: (1) loads the CSV, (2) removes rows with missing crash_date or crash_type, (3) converts crash_date to datetime format, (4) standardises the crash_type column to title case, (5) creates a new column severity_category by binning injury_count into 'minor' (0-2), 'moderate' (3-5), 'severe' (6+), (6) exports the cleaned dataset as 'nsw_crashes_cleaned.csv'. Print a summary showing row count before/after cleaning and value counts for severity_category._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-23.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Trends: SQL + Python ETL
  _Using Melbourne pedestrian counting data: (1) In Python, load the CSV, clean it (handle nulls, ensure datetime format for date column), group by sensor_name and month, and calculate average daily foot traffic per month. Export as 'pedestrian_monthly.csv'. (2) In SQL, load pedestrian_monthly.csv into a table, then write a query using CTEs to: identify sensors with highest peak month traffic, calculate month-over-month growth rate using LAG(), and rank sensors by average annual traffic. Return top 5 sensors with their peak month, traffic volume, and YoY growth trend._
  📦 Dataset: `Melbourne Pedestrian Counting Data — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-04-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
