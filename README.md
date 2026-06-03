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
| 📅 Last Sync | 2026-06-03 12:35 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Moving Average Ranking
  _Using ASX 200 historical stock prices, calculate the 20-day and 50-day moving averages for each stock ticker. Use a CTE to define the moving averages, then use window functions (ROW_NUMBER and RANK) to rank stocks by their current price relative to both moving averages within each date. Return the top 10 stocks closest to their 50-day MA on the most recent date in the dataset, ordered by rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data and build a pandas cleaning script that: (1) handles missing values in crash location and time columns; (2) standardises injury severity categories (case inconsistencies); (3) converts date/time columns to datetime format; (4) removes duplicate rows based on crash ID; (5) creates a new column for crash hour extracted from time; (6) exports the cleaned dataset to CSV. Document any data quality issues found in a summary report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-03.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Hotspot Analysis
  _Combine Python and SQL to analyse Australian Bureau of Meteorology weather observations: (1) Use Python/pandas to load weather data (temperature, rainfall, location) and clean it (standardise location names, handle missing rainfall values, filter to last 12 months); (2) Save cleaned data to a local SQLite database; (3) Write SQL queries to identify the top 5 hottest locations by average maximum temperature, then use window functions (LAG/LEAD) to detect consecutive days of temperature spikes (>2°C increase day-on-day); (4) Create a summary report showing which regions experienced the most rapid temperature increases._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-06-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
