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
| 📅 Last Sync | 2026-07-11 11:23 AEDT |

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
  _Using ASX 200 historical price data, calculate the 20-day price momentum for each stock by computing the percentage change from 20 trading days ago to today. Use window functions (LAG, ROW_NUMBER) partitioned by stock ticker and ordered by date. Rank stocks by momentum within each sector using RANK() OVER. Identify the top 5 and bottom 5 performers. Output should include: ticker, date, closing_price, price_20_days_ago, momentum_percent, sector, and momentum_rank. Filter for the most recent trading date only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (contains messy, real-world crash incident records). Write a Python script using pandas to: (1) load the CSV and identify missing values, data type inconsistencies, and duplicates; (2) standardise location names (trim whitespace, convert to title case); (3) convert date columns to datetime; (4) categorise severity into Safe/Minor/Moderate/Severe based on injury counts; (5) create a summary CSV showing crash frequency by local government area (LGA) and severity category; (6) generate a report listing data quality issues found and rows removed. Output: cleaned_crashes.csv and data_quality_report.txt._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-11.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline: (1) Load Australian weather observations (temperature, rainfall, wind speed) from Bureau of Meteorology or Kaggle dataset; (2) use Python/pandas to calculate rolling 30-day mean and standard deviation for each weather station and metric; (3) identify anomalies (values >2 std deviations from rolling mean); (4) export anomalies to a CSV with station_id, date, metric, recorded_value, rolling_mean, z_score; (5) load this CSV into a SQL database (SQLite or PostgreSQL); (6) write a SQL query using CTEs to rank stations by anomaly frequency and calculate the percentage of anomalous readings per station; (7) output a final ranked table showing top 10 stations with most volatile weather patterns. Document your anomaly threshold choice._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-07-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
