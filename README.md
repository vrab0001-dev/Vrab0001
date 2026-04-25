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
| 📅 Last Sync | 2026-04-25 11:17 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility Analysis
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for the top 10 most volatile stocks. Use a CTE to first calculate daily percentage returns, then apply a window function (ROW_NUMBER and frame clause) to compute rolling volatility. Return stock symbol, date, closing price, daily return %, and 30-day rolling volatility, ordered by volatility descending then date. Filter for the last 90 days of data only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (CSV format). Clean the dataset by: (1) handling missing values in injury_type and crash_severity columns, (2) standardising date formats to YYYY-MM-DD, (3) removing duplicate crash records based on crash_id, (4) converting speed_zone to numeric, replacing text values with median speed for that zone. Output a cleaned CSV with columns: crash_id, crash_date, locality, severity, injury_count, speed_zone_numeric. Then create a summary CSV showing crashes per locality, total injuries, and average severity score, sorted by injury_count descending._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-25.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes Pipeline
  _Build a data pipeline: (1) Use Python + pandas to extract Australian weather observations data (Bureau of Meteorology dataset), clean temperature and rainfall columns, handle missing values with forward-fill, and save to a local SQLite database. (2) In SQL, create a query using window functions (RANK, LAG) to identify: the top 5 hottest days by station for the past year, the previous day's temperature (using LAG), and the temperature change. (3) Return: station_name, observation_date, max_temp, prev_day_temp, temp_change, rank_by_station. Export results to CSV. Ensure your Python script handles file I/O and your SQL uses at least one CTE and one window function._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle jsphyg collection)`
  📁 Submit as: `quest3_2026-04-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
