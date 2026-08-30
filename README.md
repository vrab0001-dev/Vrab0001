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
| 📅 Last Sync | 2026-08-30 12:05 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum with Window Functions
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify momentum shifts. Write a query using window functions (ROW_NUMBER, LAG, and a CTE) to: 1) Create a CTE that calculates the 20-day moving average for each stock's closing price, ordered by date. 2) Use LAG to compare today's price against yesterday's price and calculate daily percentage change. 3) Rank stocks by their 20-day momentum (highest average gain first) using ROW_NUMBER partitioned by stock symbol. Return the top 10 stocks with strongest upward momentum on the most recent trading date, including: stock symbol, closing price, 20-day moving average, daily % change, and momentum rank._
  📦 Dataset: `ASX 200 Historical Stock Data — Kaggle`
  📁 Submit as: `quest1_2026-08-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Hotspot Mapping
  _Download NSW Road Crash Data (contains crash locations, severity, vehicle types, timestamps). Write a Python/pandas script to: 1) Clean the dataset by handling missing values in critical columns (latitude, longitude, crash severity). 2) Remove duplicate crash records based on location and timestamp. 3) Filter for crashes with severity >= 'Serious Injury' in the last 2 years. 4) Standardise postcode formats and identify the top 15 postcodes by crash frequency. 5) Export a cleaned CSV with columns: crash_id, postcode, severity, date, vehicle_count, cleaned_location_description. The script should log all cleaning operations (rows dropped, values imputed, duplicates found)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-30.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Ranking Pipeline
  _Build an end-to-end pipeline combining Python and SQL. Task: 1) Use Python/pandas to load Australian wine production statistics data (by region and year). Clean the data: standardise region names (remove whitespace, fix inconsistent capitalization), handle missing production volumes by forward-filling within regions, remove outlier years with zero production. 2) Export the cleaned data to a CSV. 3) Create a SQL query that: loads the cleaned CSV, calculates year-over-year production growth percentage for each region using window functions (LAG), ranks regions by production volume in the most recent year (ROW_NUMBER), and identifies which regions had consistent growth (>5% YoY for 3+ consecutive years). 4) Output: region name, latest production volume, YoY growth %, production rank, and a flag indicating consistent-growth regions. Expected output: a CSV with top 20 regions by consistency of growth._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-08-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
