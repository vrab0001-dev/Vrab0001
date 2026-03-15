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
| 📅 Last Sync | 2026-03-15 16:27 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility & Momentum Tracker
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation (volatility) and 14-day momentum (price change %) for each stock. Use window functions ROW_NUMBER() and LAG() to identify the top 5 most volatile stocks on the latest date. Order results by volatility descending. Expected output: stock ticker, latest close price, 30-day volatility, 14-day momentum, rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Pipeline
  _Download NSW Road Crash Data (CSV). Clean the dataset by: (1) removing rows with >30% missing values, (2) standardising date columns to YYYY-MM-DD format, (3) handling categorical inconsistencies in crash type and severity columns (e.g. 'Fatal' vs 'FATAL'), (4) creating a derived 'risk_score' column (weighted combination of speed limit, number of vehicles, and fatality count). Export cleaned data to a new CSV. Deliverable: cleaned CSV + Python script with docstrings explaining each cleaning step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-15.py`
- [ ] ⚡ **Combined Quest:** Weather Patterns & Wildfire Correlation Analysis
  _Combine Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) with Australian Wildfire dataset. (1) In Python/pandas: load both CSVs, merge on date and location (nearest weather station), and create a 'fire_risk_index' = (temperature - 20) * (100 - humidity) / rainfall. (2) In SQL: load the enriched data into a local database, partition by region and month, use ROW_NUMBER() and LAG() to detect unusual spikes in fire risk, calculate month-over-month change %. (3) Export final results showing region, month, fire_risk_index, anomaly flag, and trend direction. Deliverable: Python script + SQL query + output CSV with anomalies flagged._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle) + Australian Wildfire Dataset (Kaggle)`
  📁 Submit as: `quest3_2026-03-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
