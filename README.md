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
| 📅 Last Sync | 2026-09-03 11:49 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) the 5-day moving average of closing price for each stock, (2) the rank of each stock by daily percentage change within its sector, and (3) identify the day each stock hit its 52-week high. Use ROW_NUMBER(), LAG(), and RANK() window functions partitioned by stock ticker and ordered by date. Return: ticker, date, close_price, moving_avg_5day, daily_pct_change_rank, days_since_52week_high. Filter results for the top 10 ASX stocks by market cap in the last 90 days._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download the NSW Road Crash Data (contains crash records with location, severity, vehicle type, weather conditions). Build a Python pandas script to: (1) handle missing values in severity and weather columns using mode imputation, (2) standardise postcode formats and geocode to LGA (Local Government Area), (3) remove duplicate records based on crash ID and timestamp, (4) create a categorical column binning crashes into severity levels (fatal, serious injury, other injury, non-injury), (5) export a cleaned CSV grouped by LGA showing crash count, average severity score, and top 3 vehicle types involved per LGA. Include data validation checks (e.g., warn if >20% of rows removed)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-03.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Scoring Engine
  _Integrate Australian Weather observations (Bureau of Meteorology) with the Australian Wildfire dataset (Kaggle). (1) In Python, load both datasets and merge on date and location (nearest weather station to fire record). Clean temperature, humidity, wind speed, and rainfall data. (2) Engineer features: calculate a fire risk score using the formula (temp × wind_speed) / (humidity × rainfall_mm + 1). (3) Load cleaned data into a local SQLite database with two tables: weather_stations and fire_incidents. (4) Write SQL queries to: identify the top 10 locations with highest average fire risk scores in the past 5 years, rank states by total incidents in high-risk weather conditions (temp > 35°C, humidity < 30%, wind > 40 km/h), and flag any anomalies (e.g., fires occurring in impossible weather). (5) Export summary report as CSV: state, risk_level, incident_count, avg_fire_risk_score, weather_pattern._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology) + Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-09-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
