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
| 📅 Last Sync | 2026-07-06 11:57 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Momentum Ranking
  _Using ASX 200 historical price data, write a query with window functions to calculate: (1) the 30-day price change percentage for each stock using LAG, (2) rank stocks by momentum within each sector using RANK(), and (3) identify stocks that hit a new 52-week high in the last 30 days. Return the top 10 momentum gainers with their sector, current price, 52-week high, and momentum rank. Use a CTE to pre-calculate the 52-week high for performance._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (contains crash records with datetime, location, vehicle type, severity). Clean the dataset by: (1) handling missing values in crash severity and location fields (document your strategy), (2) parsing datetime columns correctly, (3) creating new features: hour of day, day of week, and a binary flag for severe crashes (fatality or hospitalisation). Export the cleaned dataset to CSV. Provide a summary report showing before/after row counts, missing data percentages, and the distribution of your new features._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-06.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline: (1) Use Python to load Australian Weather observations data (temperature, rainfall, pressure by station and date). Clean missing values using forward-fill for time series, then calculate 30-day rolling averages per station. (2) Load the cleaned data into a local SQLite database. (3) Write a SQL query with window functions (ROW_NUMBER, LAG) to identify temperature anomalies: flag any day where temperature deviates >2 standard deviations from the 30-day rolling average for that station. (4) Return the top 20 anomalies ranked by severity with station name, date, actual temp, rolling avg, and deviation. Export results to CSV._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
