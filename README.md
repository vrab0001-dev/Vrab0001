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
| 📅 Last Sync | 2026-09-13 11:46 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Moving Average Crossover Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate the 20-day and 50-day moving averages for the top 5 most volatile stocks. Identify crossover points where the 20-day MA crosses above or below the 50-day MA. Use CTEs to structure the query and window functions (AVG() OVER, LAG()) to detect crossover signals. Return stock ticker, date, both moving averages, and a signal column indicating 'BULLISH_CROSS' or 'BEARISH_CROSS'. Order by stock and date._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Enrichment
  _Download NSW Road Crash Data (contains messy datetime formats, missing suburb names, and inconsistent severity classifications). Write a Python/pandas script that: (1) standardizes all datetime columns to ISO format; (2) fills missing suburb values by geocoding coordinates to NSW LGA if available, otherwise marks as 'UNKNOWN'; (3) reclassifies severity into standardized categories (FATAL, SERIOUS_INJURY, OTHER_INJURY, NON_INJURY); (4) removes duplicate records based on crash ID and timestamp; (5) exports a cleaned CSV with added columns for day_of_week, hour_of_day, and month. Document any rows dropped and why._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-13.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Coral Health Trend Report
  _Retrieve Great Barrier Reef monitoring data (bleaching events, temperature anomalies, and species health scores by reef zone and year). Use Python/pandas to: (1) clean and merge temperature anomaly data with bleaching event records; (2) calculate year-over-year health score trends by reef zone; (3) identify zones with declining health (negative slope over 5+ years). Export results to CSV. Then write SQL queries to: (1) use window functions (ROW_NUMBER, LAG) to rank reef zones by severity of decline; (2) create a CTE that identifies 'at-risk' zones (health < 40 AND declining); (3) generate a summary showing zone name, latest health score, trend direction, and risk level. Combine Python output with SQL analysis to produce a final report CSV with actionable insights for each reef zone._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-09-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
