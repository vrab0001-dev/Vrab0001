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
| 📅 Last Sync | 2026-08-13 10:56 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Ranking with Window Functions
  _Using ASX 200 historical stock price data, write a query that calculates the 30-day price momentum for each stock using window functions. Rank stocks by momentum within each sector using ROW_NUMBER(). Include columns: stock_symbol, sector, closing_price, momentum_percentage, sector_rank. Use a CTE to calculate momentum as ((current_price - price_30_days_ago) / price_30_days_ago * 100). Filter to show only the top 5 stocks by momentum in each sector for the most recent date in the dataset._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Export Pipeline
  _Download NSW Road Crash Data (CSV format). Write a Python script using pandas to: (1) Remove rows with >40% missing values; (2) Standardise the 'severity' column by converting to title case and handling variants like 'Non injury crash' vs 'Non-injury crash'; (3) Parse the 'date' column into datetime objects and extract day_of_week; (4) Drop duplicate records based on crash_id; (5) Create a new column 'hour_of_day' from the time field; (6) Save the cleaned dataset to CSV with UTF-8 encoding. Log the number of rows removed at each cleaning step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-13.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis: Python ETL + SQL Analytics
  _Complete a two-stage task: STAGE 1 (Python): Download Melbourne pedestrian counting data. Use pandas to aggregate hourly foot traffic by location, calculate rolling 7-day average, detect outliers using IQR method, and export to a cleaned CSV. STAGE 2 (SQL): Load the cleaned CSV into a database. Write a query using CTEs and window functions to: (a) Calculate rank of locations by average daily traffic; (b) Show month-over-month traffic change using LAG(); (c) Identify the top 3 peak hours across all locations. Return results showing location_name, daily_avg_traffic, traffic_rank, prev_month_avg, traffic_change_pct, peak_hour._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-08-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
