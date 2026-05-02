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
| 📅 Last Sync | 2026-05-02 11:28 AEDT |

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
  _Using ASX 200 historical prices dataset, calculate the 20-day moving average and identify stocks that have gained >5% in the last 10 trading days. Use window functions (ROW_NUMBER, LAG) to rank stocks by momentum within each sector. Return the top 10 stocks by percentage gain, including: stock symbol, current price, 20-day moving average, percentage gain over 10 days, and sector rank. Use a CTE to calculate the 10-day change first, then join to sector data._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-02.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (contains crash records with location, severity, vehicle type, injuries). Clean the dataset by: (1) handling missing values in injury counts and crash type columns, (2) standardising location names (remove extra whitespace, lowercase), (3) converting date columns to datetime format, (4) filtering out records with severity='Unknown'. Then aggregate crashes by local government area (LGA) and crash type, counting incidents and total injuries. Export a cleaned CSV with LGA, crash type, incident count, and total injuries. Bonus: Create a second CSV ranking LGAs by total injuries._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-02.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Anomaly Detection
  _Task: (1) In Python, load Australian Weather observations dataset (Bureau of Meteorology). Clean temperature and rainfall columns (handle -999 missing values, outliers). Calculate monthly averages for temperature and rainfall by station. Export cleaned monthly aggregates to CSV. (2) In SQL, import the cleaned data and identify temperature anomalies: for each station, find months where temperature deviated >2 standard deviations from the station's historical mean. Return station name, month, recorded temperature, station mean, deviation in std devs, and anomaly flag. Use a window function (AVG, STDDEV_POP) over station partitions. (3) Combine results: create a Python script that reads the SQL output and generates a summary report showing which stations had the most anomalies in the past 5 years._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle by jsphyg)`
  📁 Submit as: `quest3_2026-05-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
