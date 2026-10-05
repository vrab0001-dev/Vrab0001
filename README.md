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
| 📅 Last Sync | 2026-10-05 13:44 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Ranking
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 20-day rolling average price for each stock, (2) the rank of each stock by price change percentage within each month, and (3) identify stocks that were in the top 10 performers for 3+ consecutive months. Use ROW_NUMBER(), RANK(), and LAG() functions. Output should show stock ticker, date, rolling_avg_price, monthly_rank, and consecutive_top10_months._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Hotspot Detection
  _Download NSW Road Crash Data (2020-2025). Write a Python/pandas script to: (1) clean the dataset by handling missing values in location, crash type, and injury severity columns; (2) standardise date formats and geocode suburb names; (3) identify the top 15 crash hotspots by frequency and severity score (weighted by injury count); (4) export a cleaned CSV with hotspot classifications (High/Medium/Low risk). Handle duplicates, invalid coordinates, and data type conversions. Expected output: cleaned_crashes.csv with hotspot_risk column added._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-05.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends & Agricultural Impact Pipeline
  _Build an end-to-end pipeline: (1) Load Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity) for major agricultural regions (2020-2026). (2) Use Python/pandas to clean weather data, handle missing observations, and calculate monthly aggregates (avg temp, total rainfall, drought severity index). (3) Load ABARES crop production data for matching regions/years. (4) Create a SQL database with two tables: weather_monthly and crop_production. (5) Write a SQL query with CTEs to correlate rainfall anomalies with crop yield changes, identifying which crops are most sensitive to drought. Output: a summary table showing crop_type, region, rainfall_anomaly_pct, yield_change_pct, and correlation_strength. Use at least one CTE and one window function._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle jsphyg) + ABARES Crop Production Data — agriculture.gov.au`
  📁 Submit as: `quest3_2026-10-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
