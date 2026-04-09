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
| 📅 Last Sync | 2026-04-09 11:06 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using ASX 200 historical price data, calculate a 30-day rolling average and identify stocks that have gained >5% in the last 10 trading days. Use window functions (AVG() OVER, ROW_NUMBER() OVER) and a CTE to rank stocks by momentum. Return the top 10 stocks with highest 10-day gain percentage, including: ticker symbol, current price, 30-day average price, 10-day gain %, and rank. Filter for stocks with trading volume >1M shares on the latest date._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Severity Pipeline
  _Download NSW Road Crash Data (2020-2025). Clean the dataset by: (1) handling missing values in Severity, Speed_Limit, Weather_Condition columns using forward-fill or mode imputation, (2) standardising date formats and extracting hour-of-day from crash_time, (3) removing duplicate crash records based on Location + DateTime, (4) categorising crashes into Severity buckets (Fatal, Serious Injury, Other Injury), (5) exporting cleaned data to a CSV file with summary statistics showing crash count by Severity, Day_of_Week, and Hour. Use pandas and validate data quality (null counts, duplicates, data types) before export._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-09.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Hotspot Detection Pipeline
  _Build an end-to-end pipeline: (1) Python: Load Australian Bureau of Meteorology weather observation data (temperature, humidity, rainfall). Clean dates, handle missing values, and aggregate daily max temperature by station. (2) SQL: Create a table from the cleaned CSV. Use window functions (LAG, ROW_NUMBER) to find stations with highest temperature increase over the last 7 days. Identify 'hotspots' where max_temp increased by >3°C in 7 days. (3) Export a final report (CSV) showing: station_name, location_state, last_7day_temp_increase, ranking_by_increase, current_max_temp. Include only stations from NSW, VIC, and QLD with complete 7-day records. Document the cleaning steps and assumptions made._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle jsphyg dataset)`
  📁 Submit as: `quest3_2026-04-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
