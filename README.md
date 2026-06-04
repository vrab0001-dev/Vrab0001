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
| 📅 Last Sync | 2026-06-04 12:31 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Analysis
  _Using ASX 200 historical price data, write a query with window functions to calculate: (1) the 20-day rolling average price for each stock, (2) the rank of each stock by daily percentage change within its sector, (3) LAG and LEAD functions to show previous day's close and next day's open. Filter for the top 10 stocks by market cap and order results by date and stock ticker. Expected output: date, ticker, close_price, rolling_20day_avg, daily_pct_change, rank_in_sector, prev_day_close, next_day_open._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-06-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data. Write a Python/pandas script to: (1) clean missing values in crash_severity, crash_type, and location columns, (2) standardise date format to YYYY-MM-DD, (3) remove duplicate records based on crash_id, (4) parse suburb/postcode into separate columns, (5) flag and handle outliers in fatality counts, (6) generate a summary CSV showing crash count by suburb and severity level. Expected output: cleaned dataset as CSV and a summary report with top 10 crash-prone suburbs._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-04.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Health Monitoring Pipeline
  _Build an end-to-end data engineering pipeline: (1) Use Python/pandas to load Great Barrier Reef monitoring data (coral health observations, temperature, bleaching events), clean it (handle missing values, validate date ranges, standardise location names), and export to a SQL-ready CSV. (2) Create a SQL schema with tables for monitoring_sites, observations, and bleaching_events. (3) Write an INSERT query to load cleaned data, then a complex analytical query using CTEs and window functions to: calculate the 12-month rolling average temperature per site, rank sites by bleaching risk (count of bleaching events / observation frequency), identify sites with worsening trends (LAG function to compare year-on-year health scores). Expected output: cleaned data file, schema definition, and analytical query results showing risk-ranked sites with trend analysis._
  📦 Dataset: `Great Barrier Reef monitoring data — aims.gov.au`
  📁 Submit as: `quest3_2026-06-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
