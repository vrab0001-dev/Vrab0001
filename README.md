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
| 📅 Last Sync | 2026-09-26 12:18 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 20-day rolling average closing price for each stock ticker. Then use window functions (ROW_NUMBER and RANK) to rank stocks by their current price relative to their 20-day moving average within each date partition. Specifically: 1) Calculate a CTE with LAG to get previous closing prices, 2) Build another CTE to compute the 20-day moving average, 3) Rank stocks on each date by (current_price - moving_average) / moving_average as a momentum score. Return the top 10 stocks by momentum rank for the most recent date in the dataset, showing ticker, date, price, moving_average, momentum_score, and rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-26.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data (contains crash locations, severity, vehicle types, timestamps). Write a Python script using pandas to: 1) Load the CSV and handle missing values in the 'Severity' and 'Speed Zone' columns (choose appropriate strategies: drop, fill, or flag), 2) Parse datetime columns correctly, 3) Remove duplicate crash records based on crash ID and timestamp, 4) Create new features: 'hour_of_day' from the crash timestamp and 'is_weekend' boolean flag, 5) Filter to crashes from the last 12 months only, 6) Aggregate to produce a summary CSV showing crash count and average severity by hour_of_day and speed_zone. Output the cleaned dataset and the summary file with clear column names._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-26.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring ETL: Load, Transform, Analyse
  _Build a mini ETL pipeline using Python and SQL: 1) Use Python + pandas to extract Great Barrier Reef monitoring data (reef health metrics, temperature, coral bleaching observations). Clean the data by handling missing location coordinates, standardizing date formats, and removing outlier temperature readings (e.g., > 35°C). Save the cleaned data to a local SQLite database with two tables: 'reef_observations' (location, date, temperature, health_score) and 'bleaching_events' (location, date, bleaching_severity). 2) Write SQL queries to: a) Find the top 5 reef locations with the highest average temperature over the past 3 years, b) Use a CTE to calculate the month-over-month change in health_score for each location, c) Rank bleaching events by severity within each location and return only the top 2 per location. Output the SQL results as a summary report showing location-level trends._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-09-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
