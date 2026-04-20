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
| 📅 Last Sync | 2026-04-20 11:23 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Analysis with Window Functions
  _Using ASX 200 historical price data, calculate the 7-day rolling standard deviation of daily returns for the top 10 most volatile stocks. Use window functions (specifically ROW_NUMBER and frame clauses) to rank stocks by volatility and identify which stocks had the highest volatility in the most recent trading week. Expected output: a table with stock ticker, date, closing price, daily return percentage, 7-day rolling volatility rank, and cumulative volatility score ordered by date descending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-20.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Geocoding Pipeline
  _Download NSW Road Crash Data (contains suburb names, crash severity, number of vehicles involved). Write a Python script using pandas to: (1) clean missing values in the 'Crash Date' and 'Suburb' columns, (2) standardise suburb names to title case, (3) create a new column categorising crashes into severity bins (Minor: 1 vehicle, Moderate: 2-3 vehicles, Major: 4+ vehicles), (4) export cleaned data to CSV with summary statistics showing crash counts by severity and top 5 affected suburbs. Expected output: cleaned CSV file plus a summary report printed to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-20.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Using Bureau of Meteorology weather observation data (daily temperature, rainfall, humidity): (1) Write a Python script to load CSV data, calculate 30-day rolling average temperature by city, and flag anomalies where daily temperature deviates >2 standard deviations from the rolling mean. Save anomaly records to a new CSV. (2) Load this anomaly CSV into a database and write a SQL query using CTEs to: identify cities with the most anomalies in the last 90 days, calculate the anomaly frequency rate (anomalies per 30-day period), and rank cities by anomaly severity. Expected output: anomaly CSV file + SQL results showing top 10 cities ranked by anomaly frequency with anomaly counts and average temperature deviation magnitude._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-04-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
