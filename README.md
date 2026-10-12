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
| 📅 Last Sync | 2026-10-12 13:59 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate the 20-day moving average and price momentum (current price - price 20 days ago) for the top 5 most volatile stocks. Use ROW_NUMBER() to rank stocks by volatility (standard deviation of daily returns), then LAG() to compare current close price with the close price from 20 trading days prior. Return stock ticker, date, close price, 20-day moving average, momentum value, and volatility rank. Order by date descending within each stock._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (CSV format). Write a Python script using pandas to: (1) handle missing values in Severity and Road Type columns by imputing with mode; (2) standardise date formats to YYYY-MM-DD; (3) remove duplicate records based on Crash ID; (4) create a new feature 'hour_of_day' extracted from Crash Time; (5) filter crashes where Severity is 'Fatal' or 'Serious injury'; (6) save the cleaned dataset to a new CSV. Output a summary report showing original row count, final row count, and top 5 postcodes by fatal/serious crash frequency._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-12.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis Pipeline
  _Build a data pipeline: (1) Load Melbourne pedestrian counting data (CSV from Melbourne Open Data Portal); (2) Use Python/pandas to clean the data: convert timestamps, remove sensor anomalies (counts > 50,000 per hour), and aggregate hourly counts to daily totals by sensor location; (3) Export cleaned data to a CSV intermediate file; (4) Create a SQL query that ranks sensors by average daily foot traffic using window functions (RANK() OVER (ORDER BY avg_daily_count DESC)), calculates a 7-day rolling average using LAG(), and identifies peak traffic days (top 10% by count); (5) Return sensor name, location, daily average, rolling average, traffic rank, and flag for peak days. Document your data quality issues found and how you resolved them._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-10-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
