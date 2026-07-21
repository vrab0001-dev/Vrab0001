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
| 📅 Last Sync | 2026-07-21 11:23 AEDT |

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
  _Using ASX 200 historical stock price data, calculate a 20-day moving average and identify stocks with the strongest momentum. Use window functions (ROW_NUMBER, LAG) to: 1) Calculate the 20-day moving average price for each stock, 2) Rank stocks by percentage change from their 20-day average (highest to lowest), 3) Identify the top 10 stocks with largest positive divergence from moving average on the latest date. Return stock symbol, current price, 20-day MA, percentage divergence, and rank. Use a CTE to structure the moving average calculation, then apply ranking in the main query._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Classification
  _Download NSW Road Crash Data and perform comprehensive data cleaning: 1) Handle missing values in crash location, severity, and vehicle type columns (document your strategy for each), 2) Standardise date/time formats and extract hour-of-day and day-of-week features, 3) Create a severity score (1-5 scale) based on injury count and crash type, 4) Remove duplicate records based on crash ID and timestamp, 5) Generate a summary report showing crash frequency by severity, time of day, and top 5 locations. Export cleaned dataset as CSV and severity summary as JSON._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-21.py`
- [ ] ⚡ **Combined Quest:** AEMO Electricity Demand Anomaly Detection Pipeline
  _Build a data pipeline combining Python and SQL: 1) In Python, fetch or load AEMO hourly electricity demand data for the last 90 days, clean missing values using forward-fill, and calculate rolling 7-day average and standard deviation using pandas, 2) Identify anomalies where demand exceeds mean + 2.5*std_dev, flag these records with anomaly_score, and export to CSV, 3) Load the CSV into a SQL database, 4) In SQL, use window functions (LAG, LEAD) to identify consecutive anomaly hours, calculate duration of anomaly clusters, and rank the top 10 most severe anomaly clusters by maximum demand spike. Return cluster ID, start time, end time, duration (hours), peak demand, and severity rank._
  📦 Dataset: `AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-07-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
