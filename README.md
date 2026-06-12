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
| 📅 Last Sync | 2026-06-12 12:13 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 5-day moving average and price momentum (current price vs 5 days ago) for each stock. Use window functions (AVG() OVER and LAG()) to find the top 10 stocks by momentum on the most recent trading date. Include stock symbol, current price, 5-day moving average, momentum percentage, and ranking by momentum. Order by momentum descending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Calculation
  _Download the NSW Road Crash Data (contains crash records with location, severity, weather conditions, road type). Clean the dataset by: (1) handling missing values in weather and road condition columns, (2) standardising suburb/postcode formats, (3) converting date strings to datetime objects, (4) removing duplicates based on crash ID. Then create a new column 'crash_risk_score' (1-10) based on severity level and weather conditions. Export the cleaned dataset to a new CSV file with only essential columns: crash_id, date, suburb, severity, weather, road_type, crash_risk_score._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-12.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes: Data Pipeline & Analysis
  _Build a data engineering pipeline: (1) In Python, fetch or load the Australian Weather Observations dataset (Bureau of Meteorology historical data from Kaggle). Clean the data by handling missing temperature/rainfall values, standardising station names, and converting timestamps. (2) Load the cleaned data into a SQL database (SQLite or local schema). (3) Using SQL, find the top 5 stations with the highest temperature variance (max - min) in the past 12 months, calculate monthly average rainfall for each station, and identify anomalies (temperatures or rainfall >2 standard deviations from mean). (4) Export results to CSV showing station name, state, temperature variance, average rainfall, and count of anomalies detected._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-06-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
