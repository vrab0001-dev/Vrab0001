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
| 📅 Last Sync | 2026-10-11 13:35 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a query that calculates a 20-day rolling average price and identifies the rank of each stock by price momentum (percentage change from 20-day low to current price). Use window functions ROW_NUMBER() and LAG() to compute daily percentage changes, then rank stocks within each date partition. Filter for the top 10 momentum gainers on the most recent trading date. Expected output: stock symbol, current price, 20-day moving average, momentum rank, and percentage gain._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Scoring
  _Download NSW Road Crash Data (Motor Accident data) from data.nsw.gov.au. Write a Python script using pandas to: (1) load and inspect the CSV for missing values and data types; (2) clean datetime columns and standardise suburb names (remove extra spaces, lowercase); (3) create a derived 'severity_score' column (1-5 scale) based on injury type and number of vehicles involved; (4) export the cleaned dataset to a new CSV with only complete rows. Expected output: cleaned CSV with at least 5000 rows, no null values in key columns, and a new severity_score column with values 1-5._
  📦 Dataset: `NSW Road Crash Data (Motor Accident data) — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-11.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies: Python ETL to SQL Analytics
  _Using Australian Weather observations dataset (from Bureau of Meteorology or Kaggle jsphyg collection): (1) Write a Python script to load daily temperature and rainfall CSV files, calculate monthly anomalies (deviation from 30-year average), and load cleaned data into a SQLite database with tables for 'stations', 'daily_observations', and 'monthly_anomalies'. (2) Write SQL queries to: identify the 5 stations with highest temperature anomalies in the past 12 months, rank months by rainfall deficit, and generate a summary view showing anomaly trends by state/territory. Expected output: SQLite database with 3 normalised tables, Python script handling data transformation, and 3 SQL queries producing ranked anomaly reports._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
