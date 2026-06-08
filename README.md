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
| 📅 Last Sync | 2026-06-08 12:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Rank
  _Using ASX 200 historical stock prices, write a query with window functions to calculate the 30-day rolling average price for each stock, then rank stocks by their rolling average within each date partition. Use ROW_NUMBER() or RANK() to identify the top 10 performers on the latest trading date. Include company name, date, closing price, 30-day rolling average, and rank. Order by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data and build a pandas data cleaning script that: (1) removes duplicate records based on crash ID, (2) converts date columns to datetime format, (3) fills missing severity values with 'Unknown', (4) standardises location names to title case, (5) filters crashes from 2023 onwards only, (6) exports the cleaned dataset to a new CSV file. Print summary statistics (total crashes, date range, severity distribution) before and after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-08.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Use Australian Weather observations dataset. (1) In Python/pandas: load weather data, calculate monthly average temperature and rainfall for each station, clean missing values using forward-fill, export to a staging CSV. (2) In SQL: load the staging file, use window functions (LAG, LEAD) to calculate month-over-month temperature change, identify anomalies where temperature change exceeds 2 standard deviations from the mean, and rank anomalies by severity. (3) Export final results showing station name, date, temperature, temperature_change, and anomaly_rank. Task demonstrates full ETL pipeline: extract → clean → transform → analyse._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
