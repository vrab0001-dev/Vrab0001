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
| 📅 Last Sync | 2026-07-14 11:15 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 10-day moving average price and ranks each stock by its percentage gain over the last 30 days. Use window functions (ROW_NUMBER, AVG OVER, LAG) to compute: (1) the 10-day moving average closing price for each stock, (2) the percentage change from 30 days ago to today, (3) a rank of stocks by percentage gain (highest first). Filter for only the top 10 performing stocks. Expected output: stock_code, current_price, moving_avg_10d, pct_gain_30d, gain_rank. Order by gain_rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data (CSV format). Write a Python script using pandas to: (1) handle missing values in injury_type and crash_type columns (drop rows where both are null, forward-fill others), (2) parse crash_date as datetime, (3) extract hour from crash_time and categorise into shift periods (night 00-06, morning 06-12, afternoon 12-18, evening 18-24), (4) remove duplicate rows based on crash_id, (5) aggregate crashes by local government area (LGA) and shift_period to count total crashes and average fatalities, (6) export the cleaned aggregated data to a CSV file with columns: lga, shift_period, total_crashes, avg_fatalities. Print a summary showing the LGA with the highest crash count._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-14.py`
- [ ] ⚡ **Combined Quest:** Bureau of Meteorology Temperature Anomaly Detection Pipeline
  _Create a Python script that: (1) loads Australian Weather observations (daily min/max temperatures by station and date from Kaggle or BOM), (2) cleans the data (remove nulls, validate temperature ranges -20°C to 50°C), (3) calculates a 30-day rolling average temperature for each weather station, (4) exports the cleaned and enriched data (with rolling average) to a SQLite database table called 'weather_daily', (5) then write a SQL query against that database that identifies temperature anomalies: find all days where the actual max_temp exceeds the 30-day rolling average by more than 3°C, grouped by station_name, and ranked by anomaly magnitude. Output: station_name, anomaly_date, max_temp, rolling_avg_30d, anomaly_magnitude_c, anomaly_rank. Expected to reveal heatwave patterns._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-07-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
