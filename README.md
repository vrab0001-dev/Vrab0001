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
| 📅 Last Sync | 2026-08-04 11:18 AEDT |

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
  _Using ASX 200 historical stock prices, calculate the 30-day rolling standard deviation of daily returns for the top 10 stocks by market cap. Use window functions (ROW_NUMBER, LAG) to compute daily percentage changes, then rank stocks by volatility. Output should include: stock_symbol, current_price, volatility_rank, rolling_std_dev, and the date range analysed. Filter for the last 90 trading days only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash Data (contains severity, location, time, vehicle type). Write a pandas script to: (1) handle missing values in crash_severity and speed_zone columns using forward-fill then mode imputation, (2) create a risk_score column (0-100) based on crash_severity (0-40 pts), number_of_vehicles (0-30 pts), and pedestrian_involvement (0-30 pts), (3) standardise suburb names (strip whitespace, title case), (4) export cleaned dataset to CSV with only rows where risk_score > 50, sorted by risk_score descending. Document your data quality decisions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-04.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring: SQL Analysis + Python Report Generation
  _Combine Great Barrier Reef monitoring data (temperature, coral health, bleaching events by location/date) with SQL and Python: (1) Use SQL with CTEs to identify reef zones with sustained temperature anomalies (>2°C above 10-year median) for more than 8 consecutive weeks, and calculate bleaching event frequency per zone. (2) Write Python to query results, create a summary dataframe grouping by zone and year, calculate trend (improving/declining/stable), and generate a markdown report listing high-risk zones with actionable insights. Export both the SQL query results (CSV) and the markdown report._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-08-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
