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
| 📅 Last Sync | 2026-11-23 15:27 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Ranking with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility within each month using ROW_NUMBER(). Then use a CTE to identify the top 5 most volatile stocks for each month in the dataset. Expected output: month, rank, stock_symbol, volatility_score, with stocks sorted by volatility descending within each month._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-23.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Pipeline
  _Download NSW Road Crash Data (contains crash records with location, severity, vehicles involved). Clean the dataset: handle missing values in severity columns, standardise location formats, remove duplicate crash records. Create a new column 'crash_risk_score' by normalising severity level (1-5 scale) and weighting by number of vehicles involved. Export cleaned data to CSV with the risk score. Expected output: cleaned CSV with at least 500 records, no nulls in key columns, risk_score column with values 0-100._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-23.py`
- [ ] ⚡ **Combined Quest:** Weather-Driven Energy Demand Correlation Analysis
  _Task Part 1 (Python): Download Australian Weather observations (temperature, humidity, rainfall) and AEMO electricity demand data. Clean both datasets, align by date and state/region, resample to daily averages. Part 2 (SQL): Load cleaned data into SQLite. Write a query using window functions (LAG, LEAD) to calculate the correlation between temperature changes and peak demand changes for each state. Use a CTE to rank states by strength of correlation. Expected output: SQL result showing top 5 states with strongest weather-demand correlation, including correlation coefficient, average lag period, and trend direction (positive/negative)._
  📦 Dataset: `Australian Weather Observations (Bureau of Meteorology / Kaggle) + AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-11-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
