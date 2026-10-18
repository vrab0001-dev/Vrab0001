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
| 📅 Last Sync | 2026-10-18 12:51 AEDT |

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
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 5-day rolling average closing price for each stock, (2) the rank of stocks by daily percentage change within each date, and (3) identify the top 10 stocks with the highest cumulative gains over the last 30 days using LAG and SUM window functions. Output should include stock symbol, date, closing price, 5-day moving average, daily percentage rank, and 30-day cumulative gain percentage. Use a CTE to organize intermediate calculations._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data and build a Python pandas script to: (1) handle missing values in crash severity, location (latitude/longitude), and vehicle type columns using appropriate strategies (drop, forward-fill, or median imputation), (2) standardize date-time formats and extract temporal features (day of week, hour of day, season), (3) detect and remove duplicate crash records based on crash ID and timestamp, (4) validate data quality by flagging records with impossible values (e.g., negative speeds, invalid coordinates outside NSW bounds), and (5) export a cleaned CSV with a data quality report showing rows removed and transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-18.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Health Trend Analysis Pipeline
  _Build an end-to-end data engineering workflow: (1) In Python, fetch or load Great Barrier Reef monitoring data (coral coverage, water temperature, bleaching events) from AIMS, clean it using pandas (handle missing temporal data, standardize site names, convert measurements to consistent units), and export to a CSV. (2) In SQL, load this cleaned data into a table and create a query using window functions (ROW_NUMBER, AVG window) to: identify reef sites with declining coral health trends, calculate year-over-year change in coral coverage by site using LAG, rank reef sites by health deterioration rate, and flag sites requiring urgent intervention (coverage drop >5% annually). (3) Combine results: export the flagged high-risk sites with their trend metrics back to Python and generate a summary report (CSV and simple text summary) identifying the 5 most at-risk reefs and their trajectory._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-10-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
