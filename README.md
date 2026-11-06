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
| 📅 Last Sync | 2026-11-06 14:56 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using ASX 200 historical stock price data, calculate the 20-day moving average and identify stocks where the current price has crossed above their moving average (bullish signal). Use window functions (AVG() OVER and LAG()) to compute rolling averages and detect crossovers. Rank the top 10 stocks by momentum (price - moving_average) and include their current price, 20-day MA, and crossover date. Output should show: stock_symbol, current_price, moving_avg_20d, momentum_score, crossover_date, rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Hotspot Detection
  _Download NSW Road Crash Data and clean it for analysis. Tasks: (1) Remove rows with missing critical fields (crash_type, severity, location). (2) Standardise date formats to YYYY-MM-DD. (3) Extract suburb/postcode from address strings using regex or string methods. (4) Create a severity_category column (fatal=1, serious=2, other=3). (5) Identify top 15 crash hotspots (by frequency) and export to CSV with columns: location, crash_count, avg_severity, percentage_fatal. Use pandas and Python's datetime module._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-06.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Pattern Analysis: SQL + Python Pipeline
  _Build an end-to-end pipeline using Australian Weather observations data. (1) In Python: Load raw weather CSV, clean temperature and rainfall columns (handle missing values, convert units if needed), and export cleaned data to a SQL database or temporary table. (2) In SQL: Use CTEs and window functions to calculate: monthly average temperatures by station, identify months with anomalies (>2 std devs from annual mean), rank stations by rainfall volatility (using STDDEV_POP OVER), and detect consecutive dry periods (3+ days with <1mm rain using LAG/LEAD). (3) Back in Python: Query results, create a summary report showing: station_name, anomaly_months, volatility_rank, longest_dry_spell_days. Export final report to CSV and create a simple text summary of key findings._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-11-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
