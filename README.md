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
| 📅 Last Sync | 2026-03-07 15:45 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Rankings
  _Using ASX 200 historical price data, write a query with window functions to calculate: (1) the 30-day rolling average price for each stock, (2) the rank of each stock by daily percentage change within its sector, and (3) identify stocks that hit a new 52-week high on any given date. Use ROW_NUMBER() or RANK() to number consecutive days where a stock outperformed its sector average. Output should show date, stock ticker, closing price, 30-day moving average, sector rank, and a flag indicating 52-week high._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Classification
  _Download NSW Road Crash Data (contains crash records with injury severity, vehicle type, location, weather). Clean the dataset by: (1) handling missing values in injury_type and weather_condition columns using appropriate strategies, (2) standardising location names (remove duplicates caused by spelling variations), (3) creating a new derived column that classifies crashes as 'Fatal', 'Serious Injury', 'Other Injury', or 'Non-Injury' based on max_injury_level, (4) removing duplicate crash records based on crash_id and date, (5) exporting the cleaned dataset to CSV. Use pandas and provide a data quality report showing rows removed and transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-07.py`
- [ ] ⚡ **Combined Quest:** Australian Agricultural Export Pipeline Analysis
  _Pipeline task: (1) Python: Download ABARES crop production data and livestock slaughter statistics. Clean both datasets, harmonise commodity names, and merge them into a single denormalised table showing year, commodity, production_volume, and product_type (crop or livestock). Export to CSV and load into a local SQLite database. (2) SQL: Query the database to find: the top 5 commodities by total production volume across all years, year-over-year growth rate for each commodity (using LAG window function), and identify which commodities showed consistent growth (positive growth for 3+ consecutive years). Use a CTE to calculate growth rates and a second CTE to identify consistency patterns. Output should show commodity name, avg_annual_growth_rate, and consistency_score._
  📦 Dataset: `ABARES Crop Production Data & ABS Livestock Slaughter Data — agriculture.gov.au and abs.gov.au`
  📁 Submit as: `quest3_2026-03-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
