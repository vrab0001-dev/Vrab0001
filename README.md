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
| 📅 Last Sync | 2026-05-27 12:07 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates for each stock: (1) the 30-day moving average of closing price using LAG, (2) the rank of each stock by year-to-date percentage return using RANK() OVER, (3) identify stocks that hit a new 52-week high in the last trading day using ROW_NUMBER and window functions. Return stock ticker, date, closing price, 30-day MA, YTD rank, and a boolean flag indicating new 52-week high. Filter for the top 20 performers only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Enrichment Pipeline
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas that: (1) loads the raw CSV, (2) identifies and handles missing values (document strategy for each column), (3) standardises date formats and location names, (4) removes duplicate records based on crash ID and timestamp, (5) creates new features: day_of_week, hour_of_day (if time available), severity_category (from injury counts), (6) validates data integrity (no negative values, dates within reasonable range), (7) exports cleaned dataset to a new CSV with a summary report showing rows before/after cleaning and missing value counts._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-27.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection & Trend Analysis
  _Combine Python and SQL to analyse Bureau of Meteorology weather observations. (1) In Python: load the CSV dataset, clean temperature and rainfall columns (handle missing values, remove outliers beyond 3 standard deviations), create monthly aggregates (mean temp, total rainfall, station ID), and export to a clean CSV. (2) In SQL: load the cleaned data and write a query using CTEs and window functions to: identify months where temperature was in the top 10% warmest for that station historically, calculate 12-month rolling average rainfall, rank stations by temperature volatility (std dev), and flag any month where rainfall exceeded the 90th percentile. Return station_id, month, temp_rank, rolling_avg_rainfall, volatility_rank, and anomaly_flag._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle jsphyg dataset)`
  📁 Submit as: `quest3_2026-05-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
