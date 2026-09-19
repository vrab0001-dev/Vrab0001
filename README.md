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
| 📅 Last Sync | 2026-09-19 11:59 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, calculate the 20-day and 50-day moving averages for the top 5 most volatile stocks. Use window functions (AVG() OVER) to compute rolling averages. Then identify stocks where the 20-day MA crossed above the 50-day MA in the last 30 days using LAG() to detect the crossover point. Return stock symbol, crossover date, and both moving averages on that date. Order by crossover date descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from data.nsw.gov.au. Load the CSV into pandas and perform: (1) handle missing values in crash severity and crash type columns using forward fill, then drop rows with >30% missing data; (2) standardise date columns to YYYY-MM-DD format; (3) create new columns: crash_hour (extracted from time), is_fatal (boolean), speed_zone_category (binned from numeric speed data); (4) remove duplicate rows based on crash ID; (5) export cleaned data to a new CSV with '_cleaned' suffix. Document data quality metrics (rows dropped, missing % before/after) in a summary dictionary printed to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-19.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Anomaly Detection
  _Part 1 (Python): Load Melbourne pedestrian counting data from Melbourne Open Data Portal. Clean the dataset by handling missing hourly counts and converting timestamps to datetime. Calculate daily total foot traffic and 7-day rolling average for each sensor location. Identify anomalies as days where traffic deviates >2 standard deviations from the rolling average. Export anomalies (date, sensor location, actual count, expected range) to CSV. Part 2 (SQL): Load the anomalies CSV into a database table. Write a query using CTEs to: (a) rank anomalies by severity (deviation magnitude) per location, (b) count anomalies per month, (c) identify which sensor locations experienced >5 anomalies in any single month. Return location name, anomaly month, anomaly count, and top 3 most severe individual anomalies for that location/month combo._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-09-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
