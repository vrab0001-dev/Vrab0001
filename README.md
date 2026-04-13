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
| 📅 Last Sync | 2026-04-13 11:22 AEDT |

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
  _Using ASX 200 historical stock price data, calculate a 30-day moving average and identify the top 10 stocks with the highest positive momentum (current price vs 30-day average). Use window functions (AVG() OVER) to compute rolling averages partitioned by ticker symbol ordered by date. Return ticker, date, closing price, 30-day moving average, and momentum percentage. Filter for the most recent trading month only and order by momentum descending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data (contains crash records with dates, locations, crash types, severity). Clean the dataset by: (1) handling missing values in severity and crash_type columns, (2) parsing date columns into datetime format, (3) extracting hour of day and day of week from crash timestamps, (4) standardizing location names (trim whitespace, convert to title case), (5) creating a binary 'fatal_crash' feature where severity = 'Fatal'. Export the cleaned dataset to a new CSV file with all transformations applied. Document any rows removed due to data quality issues._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-13.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end data engineering workflow: (1) Use Python/pandas to load Australian Bureau of Meteorology weather observations dataset (temperature, rainfall, humidity by station and date). Clean the data: handle missing values, standardize units, remove outliers using IQR method. (2) Load cleaned data into a SQL database or create a CSV intermediate. (3) Write SQL query using CTEs to calculate: (a) monthly average temperature per station, (b) deviation from 10-year historical average, (c) rank stations by temperature anomaly. Return: station_name, month, avg_temp, historical_avg, anomaly_degrees, anomaly_rank. Focus on identifying stations with unusual weather patterns in the past 12 months._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-04-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
