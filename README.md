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
| 📅 Last Sync | 2026-07-29 11:22 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Tracking
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to identify the top 10 stocks by 30-day price momentum. Calculate: (1) closing price change over the last 30 trading days using LAG(), (2) percentage change ranking within each stock using ROW_NUMBER(), (3) trading volume trend using a 7-day moving average with ROWS BETWEEN. Filter for stocks with average daily volume > 1M shares. Return stock ticker, current price, 30-day % change, volume trend, and rank. Use a CTE to isolate the last 30 days of data before performing calculations._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Enrichment
  _Download NSW Road Crash Data (CSV format) from data.nsw.gov.au. Write a Python pandas script to: (1) handle missing values in crash severity, location, and vehicle type columns (document your imputation strategy), (2) standardize date formats and extract year/month/day-of-week features, (3) geocode suburb names to identify high-risk postcodes, (4) create a binary 'fatal_crash' column from severity classifications, (5) remove duplicate records based on crash ID and timestamp, (6) export a cleaned dataset with new feature columns. Provide a data quality report showing row counts before/after cleaning and missing data percentages._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-29.py`
- [ ] ⚡ **Combined Quest:** Australian Weather & Wildfire Correlation Pipeline
  _Combine two datasets: Australian Weather observations (Bureau of Meteorology / Kaggle) and Australian Wildfire dataset (Kaggle). (1) Use Python/pandas to clean both datasets: standardize date formats, handle missing temperature/rainfall values, and filter for fire season months (Sep–Mar). (2) Load the cleaned data into SQLite. (3) Write SQL queries with window functions to: identify locations where wildfire incidents occurred within 7 days of temperature spikes >35°C AND rainfall <10mm, rank fire frequency by state using RANK(), calculate the 14-day rolling average of max temperature before each fire using window frames. (4) Export results showing fire location, incident date, preceding weather conditions, and risk ranking. Document any data quality issues discovered during Python cleaning._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology (Kaggle); Australian Wildfire dataset — Kaggle`
  📁 Submit as: `quest3_2026-07-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
