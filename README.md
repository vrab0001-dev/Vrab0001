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
| 📅 Last Sync | 2026-06-05 12:06 AEDT |

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
  _Using ASX 200 historical price data, calculate the 10-day moving average and identify stocks where the current price exceeded their 30-day high. Use window functions ROW_NUMBER() and LAG() to rank days by price change within each stock ticker, then filter for days where the price broke above the previous month's maximum. Return ticker, date, close price, 10-day moving average, and the price difference from the 30-day high, ordered by largest positive breakout._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Score Pipeline
  _Download NSW Road Crash Data (contains crash severity, location, time, vehicle types). Clean the dataset by handling missing values in Severity and Crash_Type columns (remove rows with >50% missing, impute others with mode). Create a new feature called 'crash_risk_score' (0-100) based on: severity level (40% weight), number of vehicles involved (35% weight), and time of day risk factor (25% weight, with night hours 22:00-05:00 weighted higher). Export the cleaned and enriched dataset as a CSV file with a timestamp in the filename. Display summary statistics showing distribution of risk scores by severity level._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-05.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Part 1 (Python): Load Australian Bureau of Meteorology weather observations (temperature, rainfall, pressure). Clean the data by removing outliers using the IQR method for each state. Create a pandas DataFrame with columns: date, state, temperature_anomaly (actual minus 10-year average), rainfall_anomaly, and anomaly_severity (Low/Medium/High based on z-score). Export to CSV. Part 2 (SQL): Import the cleaned data into a database. Write a SQL query using CTEs to: (1) calculate the average anomaly_severity by state, (2) rank states by frequency of 'High' severity anomalies using RANK(), (3) use a window function to show the running count of high-severity days per state ordered by date. Return state, rank, average_severity, and high_anomaly_count for the top 5 most anomalous states._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
