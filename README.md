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
| 📅 Last Sync | 2026-05-07 11:48 AEDT |

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
  _Using ASX 200 historical stock price data, calculate the 20-day moving average price and rank stocks by their momentum (current price vs 20-day MA). Use window functions ROW_NUMBER() and LAG() to identify the top 10 gainers in the last trading month. Return: stock symbol, current price, 20-day MA, momentum percentage, and rank. Order by momentum descending. Bonus: use a CTE to pre-aggregate daily closing prices before applying window functions._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Scoring
  _Download NSW Road Crash Data (contains crash details, severity, location, time). Write a pandas script that: (1) cleans missing values in 'severity' and 'traffic_control' columns using mode imputation; (2) converts datetime columns to proper datetime format; (3) creates a new 'risk_score' column (0-100) based on severity, number of vehicles, and presence of speed camera; (4) removes duplicate crash records by location and timestamp; (5) exports cleaned data to CSV. Log the number of rows removed at each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-07.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Python-to-SQL ETL Pipeline
  _Write a Python script that: (1) reads Australian Bureau of Meteorology weather observation data (CSV format, contains station ID, date, temperature, rainfall, humidity); (2) cleans outliers (e.g., temperature > 50°C or < -20°C); (3) aggregates to monthly statistics (mean temp, total rainfall) by station; (4) exports to a staging CSV. Then write SQL queries against the cleaned data to: (5) identify the top 5 stations with highest average monthly temperature in the last 12 months; (6) calculate year-over-year rainfall change; (7) use a CTE to rank stations by weather volatility (std dev of monthly temp). Return a final summary report with insights._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
