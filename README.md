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
| 📅 Last Sync | 2026-10-17 12:53 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Rankings with Running Averages
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of daily returns for each stock. Rank stocks by volatility within each month using RANK() and ROW_NUMBER() window functions. Use a CTE to compute daily returns (close - previous close / previous close), then a second CTE to calculate rolling volatility. Return the top 5 most volatile stocks per month, showing ticker, month, volatility rank, and rolling std dev. Filter for 2025 data only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download NSW Road Crash data from data.nsw.gov.au (or equivalent CSV export). Write a Python script using pandas to: (1) handle missing values in crash severity, location, and date columns; (2) standardise datetime formats; (3) remove duplicate crash records based on crash ID and timestamp; (4) extract new features (day of week, hour of day from datetime); (5) categorise suburbs into regions; (6) aggregate crash counts by region, severity, and day of week; (7) export the cleaned and aggregated dataset to CSV and JSON formats. Include data quality checks (row counts before/after cleaning, null counts per column) printed to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-17.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis: Trend Detection and Reporting
  _Use the Melbourne pedestrian counting dataset (Melbourne Open Data Portal). Step 1 (Python): Load hourly pedestrian count data, clean missing values using forward fill where appropriate, and create a pandas DataFrame with columns: sensor_id, date, hour, count, day_of_week, is_weekend. Step 2 (SQL): Create a database table from your cleaned CSV. Write SQL queries using LAG() and LEAD() window functions to detect traffic anomalies (hours where count deviates >2 standard deviations from the monthly mean). Use a CTE to compute rolling 7-day average traffic per sensor. Step 3 (Python): Query results back into pandas, generate a summary report showing: top 3 busiest sensors, bottom 3 quietest sensors, and a list of detected anomaly dates/times with explanations (e.g., public holiday, weekend spike). Save report as markdown or JSON._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-10-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
