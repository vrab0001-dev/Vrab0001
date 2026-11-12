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
| 📅 Last Sync | 2026-11-12 15:40 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using ASX 200 historical prices, calculate the 20-day moving average and identify momentum shifts. Write a query using window functions (ROW_NUMBER, LAG) to: 1) Compute closing price moving average for each stock, 2) Calculate day-over-day price change, 3) Rank stocks by momentum (highest positive change) within each date partition, 4) Flag when a stock crosses its 20-day MA (going above or below). Return the top 10 momentum leaders for the most recent date in the dataset, showing stock symbol, date, close price, MA20, price change %, and momentum rank._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-11-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash Data (accident records with location, severity, vehicle type). Write a Python/pandas script to: 1) Load the CSV and inspect for missing values, duplicates, and data types, 2) Clean crash severity categories (standardise text case, handle nulls), 3) Extract suburb/LGA from location strings, 4) Create a risk score (1-100) based on crash count, injury severity, and fatality rate by suburb, 5) Export cleaned dataset with risk scores to a new CSV. Output should include a summary report showing data quality metrics (% missing, duplicates removed, records processed)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-12.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline using Bureau of Meteorology weather observations. Step 1 (Python): Load daily temperature/rainfall data for a major Australian city (Sydney, Melbourne, Brisbane), clean missing values via interpolation, and calculate 30-year climate normals (mean, std dev per date). Step 2 (SQL): Create a temp table of daily observations and load cleaned data. Write a CTE-based query to identify anomalies: days where temperature or rainfall deviates >2 standard deviations from the 30-year normal. Step 3 (Python): Query results back and visualise anomalies in a summary CSV showing date, observed value, normal value, deviation %, and anomaly flag. Process at least 5 years of historical data._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-11-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
