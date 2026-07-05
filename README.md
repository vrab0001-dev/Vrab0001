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
| 📅 Last Sync | 2026-07-05 11:50 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) daily percentage change for each stock, (2) 7-day moving average of closing price using LAG/LEAD, (3) rank stocks by momentum (highest % gain in last 30 days), (4) identify stocks that crossed above their 30-day moving average. Use CTEs to build the moving averages first, then join for final ranking. Output should show date, stock symbol, close price, % change, 7-day MA, 30-day MA, and momentum rank. Filter to top 20 stocks by volume._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-05.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning and Temperature Anomaly Detection
  _Download a month of Australian Bureau of Meteorology weather observations (or use the Kaggle Australian Weather dataset). Create a pandas script to: (1) load CSV and handle missing values (forward fill for temperature, drop rows with missing date), (2) convert date column to datetime, (3) calculate daily temperature anomaly (actual temp minus 30-year average for that day — you can simulate the average or hardcode reasonable values), (4) identify extreme weather days (temp > 95th percentile or < 5th percentile), (5) group by state and calculate mean anomaly, (6) export cleaned dataset with anomaly flag to new CSV. Include data validation checks and print summary statistics._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest2_2026-07-05.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: SQL Aggregation + Python Reporting
  _Using NSW Road Crash Data: (1) Write SQL to aggregate crashes by local government area (LGA), crash type (head-on, rear-end, etc.), and severity (fatal, serious injury, other injury). Include a window function to rank LGAs by crash count and calculate month-over-month change. Export results to CSV. (2) Load the SQL output in Python/pandas and create a data quality report: check for null values, duplicate crash IDs, date range coverage. (3) Generate a summary CSV grouped by LGA showing: total crashes, fatal count, average severity score (1-3 scale), rank, and month-on-month trend (% change). (4) Create a simple visualization (bar chart) of top 10 LGAs by crash count and save as PNG. Expected output: cleaned data CSV, quality report (text/JSON), and chart._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-07-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
