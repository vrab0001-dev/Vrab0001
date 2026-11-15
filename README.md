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
| 📅 Last Sync | 2026-11-15 14:31 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility Analysis
  _Using ASX 200 historical price data, calculate the 20-day rolling standard deviation of daily returns for each stock ticker. Use a window function with PARTITION BY ticker and ORDER BY date to compute rolling volatility. Include ticker, date, closing price, daily return percentage, and the 20-day rolling volatility. Filter for stocks with at least 100 trading days of data. Order results by ticker and date. Expected output: a time-series view showing how volatility changes over time for each security._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-11-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Enrichment
  _Download NSW Road Crash Data (contains crash details, injuries, vehicle types, road conditions). Clean the dataset by: (1) removing rows with >30% missing values per record, (2) standardizing date/time formats, (3) converting categorical columns (crash type, road condition, severity) to consistent casing and removing leading/trailing spaces, (4) creating new features: day_of_week from crash date, hour_of_day from time, severity_category (group injury counts into 'minor', 'moderate', 'severe'), (5) detecting and handling outliers in latitude/longitude (keep only NSW bounds). Export cleaned data to CSV. Expected output: a clean, enriched CSV file with no duplicates, proper data types, and 3+ new derived columns._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-15.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Peak Hour Detection Pipeline
  _End-to-end data engineering task: (1) Extract Melbourne pedestrian counting data from the Melbourne Open Data Portal (sensor IDs, hourly counts, locations). (2) Use Python/pandas to clean the data: handle missing values with forward-fill (max 2 consecutive), validate counts are non-negative, standardize location names. (3) Create a Python script to load cleaned data into a local SQLite database with tables: sensors (sensor_id, location, latitude, longitude) and hourly_counts (sensor_id, datetime, count). (4) Write SQL queries to: identify the top 5 peak hours (hour of day, 0-23) across all sensors by average pedestrian count, and rank sensors by their busiest hour. (5) Export results to CSV: one file for peak hours, one for sensor rankings. Expected output: SQLite database, 2 result CSVs, and documented Python script showing data pipeline logic._
  📦 Dataset: `Melbourne pedestrian counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-11-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
