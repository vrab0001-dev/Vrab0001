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
| 📅 Last Sync | 2026-08-31 12:01 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 20-day rolling average closing price for each stock ticker. Then use window functions (ROW_NUMBER and RANK) to rank stocks by their momentum (current price minus 20-day average) within each date, partitioning by date. Include only the top 10 stocks by momentum per date. Expected output: date, ticker, close_price, 20day_avg, momentum, rank_by_momentum. Filter for the last 30 trading days only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-31.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data (CSV format from data.nsw.gov.au). Write a Python pandas script that: (1) removes rows with missing crash_id or longitude/latitude; (2) converts crash_date to datetime format and extracts day_of_week and hour_of_day; (3) creates a severity_category column ('Fatal', 'Serious Injury', 'Other Injury') from severity_level; (4) calculates the number of vehicles and persons involved per crash; (5) exports the cleaned dataset to a new CSV file. Add a summary report showing record count before/after cleaning and top 5 suburbs by crash count._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-31.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using the Australian Weather observations dataset (Bureau of Meteorology via Kaggle): (1) Write a Python pandas script to load the CSV, clean temperature and rainfall data, handle missing values using forward-fill, and calculate monthly average temperature and total rainfall by station; (2) export cleaned monthly aggregates to a temporary CSV; (3) load this into a SQL database or query it with SQL to identify anomalies: stations where the current month's average temperature is >2 standard deviations above/below the 5-year historical average for that month, OR rainfall is >3 standard deviations from the mean. Expected output: station_name, month, actual_temp, avg_temp_5yr, std_dev, anomaly_type (High/Low Temp or High/Low Rainfall)._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg dataset)`
  📁 Submit as: `quest3_2026-08-31.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
