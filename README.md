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
| 📅 Last Sync | 2026-08-25 10:33 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using ASX 200 historical stock price data, calculate a 30-day rolling average price for each stock ticker and rank stocks by their current price relative to their 30-day average (momentum score). Use window functions ROW_NUMBER() and LAG() to identify the top 10 stocks with highest positive momentum and the bottom 10 with negative momentum on the most recent trading date. Return: ticker, current_price, avg_price_30d, momentum_rank, and price_change_from_avg. Filter for stocks with at least 30 trading days of data._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download NSW Road Crash Data (contains messy timestamps, missing values, and inconsistent location formats). Write a Python/pandas script that: (1) standardises datetime columns to ISO format; (2) removes rows with null crash_severity; (3) cleans suburb names by trimming whitespace and converting to title case; (4) extracts hour_of_day from crash timestamp; (5) aggregates crashes by hour_of_day and severity level to identify peak danger periods; (6) exports cleaned dataset and summary report as CSV files. Document data quality issues found and resolution steps taken._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-25.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Create an end-to-end pipeline using Bureau of Meteorology weather observations data: (1) Use Python/pandas to load raw weather CSV, clean temperature and rainfall columns (handle missing values, convert units), and calculate monthly statistics (mean temp, total rainfall); (2) Load cleaned data into a SQL database (SQLite or PostgreSQL); (3) Write SQL query using CTEs to identify months where temperature was >2 standard deviations above the 10-year average OR rainfall was >2 standard deviations below average for each location; (4) Return: location, month, anomaly_type, actual_value, expected_range, severity_score. (5) Export results and create a summary showing which locations experienced most anomalies in the past 5 years._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology via Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-08-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
