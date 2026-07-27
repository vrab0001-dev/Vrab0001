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
| 📅 Last Sync | 2026-07-27 11:46 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Tracker with Window Functions
  _Using ASX 200 historical price data, calculate a 30-day rolling average price and identify stocks that have gained >5% over the last 30 days. Use window functions ROW_NUMBER() and LAG() to rank stocks by momentum within each sector. Return the top 10 stocks by momentum gain, showing: stock_code, sector, current_price, price_30_days_ago, momentum_pct, row_number_by_sector. Use a CTE to calculate the rolling average first, then a main query to rank and filter._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Score Automation
  _Download NSW Road Crash Data (or use local CSV). Clean the dataset by: (1) handling missing values in Severity, Location_Latitude, Location_Longitude columns; (2) standardising date formats to YYYY-MM-DD; (3) removing duplicate crash records by Crash_ID; (4) creating a new Risk_Score column (0-100) based on Severity level and number of vehicles involved using pandas apply(); (5) exporting the cleaned dataset to a new CSV file. Document any data quality issues found in a summary report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-27.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a data pipeline: (1) In Python, load Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) from CSV; (2) use pandas to calculate monthly averages and detect anomalies (values >2 standard deviations from the mean) per location; (3) create a SQL table schema and insert cleaned data with anomaly flags into SQLite; (4) write a SQL query using window functions to find the top 5 locations with the most temperature anomalies in the last 12 months, ranked by anomaly frequency. Output: Python script + SQL file + anomaly report (CSV)._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
