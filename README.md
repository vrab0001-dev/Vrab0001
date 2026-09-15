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
| 📅 Last Sync | 2026-09-15 12:11 AEDT |

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
  _Using ASX 200 historical stock price data, calculate the 20-day moving average and identify stocks with the highest price momentum (percentage change from 20-day MA). Use window functions ROW_NUMBER() and LAG() to rank stocks by momentum within each trading week, and identify the top 5 momentum gainers. Your output should include: stock symbol, closing price, 20-day MA, momentum percentage, and week rank. Use a CTE to calculate the MA first, then apply window functions in the main query._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-09-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download NSW Road Crash Data and build a Python script using pandas that: (1) removes rows with missing severity or crash type; (2) standardises date formats to YYYY-MM-DD; (3) creates a new column 'time_period' (Morning 6-12, Afternoon 12-18, Evening 18-24, Night 24-6); (4) removes duplicate crash records based on crash ID and date; (5) exports a cleaned CSV with crash counts by local government area and time period, sorted by total crashes descending. Include error handling for file I/O and data validation._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-15.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline: (1) Use Python/pandas to load Bureau of Meteorology weather observations for 2024 (temperature, rainfall, humidity); clean missing values using forward-fill or interpolation; calculate 7-day rolling averages for temperature; (2) Create a SQL schema and INSERT cleaned data into a local database; (3) Write SQL queries using window functions to identify temperature anomalies (values >2 std dev from monthly mean) and rank them by severity within each month; (4) Export anomaly results with station name, date, temperature, and anomaly rank. Expected output: CSV file of ranked temperature anomalies with explanatory notes on which stations showed unusual patterns._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology (Kaggle jsphyg version)`
  📁 Submit as: `quest3_2026-09-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
