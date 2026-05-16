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
| 📅 Last Sync | 2026-05-16 11:50 AEDT |

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
  _Using ASX 200 historical price data, write a query that calculates the 30-day rolling average price for each stock, then ranks stocks by their current price relative to their rolling average (price / rolling_avg). Include a window function to show the rank change from the previous day for each stock. Return: stock_code, date, close_price, rolling_avg_30d, price_to_avg_ratio, current_rank, rank_change. Filter for the top 10 best and bottom 10 worst performers in the last 7 days._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Enrichment
  _Download NSW Road Crash Data (contains crashes, vehicles, persons involved). Clean the dataset by: (1) removing rows with >40% missing values per row, (2) standardising date/time formats, (3) handling missing values in numeric columns (speed_zone, posted_speed_limit) using median by crash_type, (4) categorising crash severity into 'Fatal', 'Serious', 'Non-serious' based on injury_type, (5) creating a new feature 'time_of_day' (Morning 06-12, Afternoon 12-18, Evening 18-00, Night 00-06). Output a clean CSV with these transformations applied. Include a summary report showing % of rows removed, missing value patterns before/after, and top 5 crash locations._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-16.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using Bureau of Meteorology Australian Weather Observations dataset: (1) Write a Python script to load, clean, and transform daily temperature & rainfall observations (handle missing values, standardise units). (2) Create a SQL query that calculates monthly mean temperature and total rainfall by station. (3) Use a window function (LAG) in SQL to find temperature/rainfall anomalies (days exceeding 2 standard deviations from 30-day rolling mean). (4) Python: merge the SQL results back, flag anomalies, and export a report showing top 10 most extreme weather events in the past year by station and state. Include visualisation: bar chart of anomaly counts by state, line chart of temperature trends for 3 major cities._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
