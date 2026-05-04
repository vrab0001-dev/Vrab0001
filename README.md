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
| 📅 Last Sync | 2026-05-04 11:45 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum with Window Functions
  _Using ASX 200 historical stock price data, calculate a 30-day rolling average price and identify momentum shifts. Write a query using window functions (ROW_NUMBER, LAG) to: (1) rank stocks by daily price change within each ticker, (2) calculate the price difference from the previous day using LAG, (3) identify the date when each stock crossed above its 30-day moving average. Return ticker, date, closing_price, price_change_from_previous_day, and momentum_signal (1 if above 30-day MA, 0 otherwise). Use a CTE to pre-calculate the 30-day moving average._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Scoring
  _Download NSW Road Crash Data and clean it for analysis. Tasks: (1) Load the CSV and handle missing values in crash_severity, vehicle_type, and weather_condition columns (document your strategy), (2) standardise date formats and extract crash_hour from timestamp, (3) create a risk_score column (0-100) based on severity level, number of vehicles involved, and whether pedestrians were present, (4) remove duplicate records based on crash_id and timestamp, (5) export the cleaned dataset as a new CSV. Document any data quality issues found (e.g., impossible times, negative vehicle counts)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-04.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis Pipeline
  _Build an end-to-end pipeline: (1) Use Python to fetch or load Melbourne pedestrian count data, clean hourly counts (handle nulls, outliers, duplicates), and aggregate to daily totals by sensor location, (2) Load cleaned data into a SQLite database with tables for sensors and daily_counts, (3) Write SQL queries to find: top 5 busiest sensors by average daily count, day-of-week patterns (which days have highest traffic), and sensors with unusual spikes (counts > 2 standard deviations from their mean), (4) Export the top 10 anomalous days as a CSV. Provide both Python script and SQL queries._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-05-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
