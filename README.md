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
| 📅 Last Sync | 2026-09-16 12:03 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Ranking with Window Functions
  _Using ASX 200 historical stock price data, write a query that ranks each stock by its 30-day price momentum (percentage change from 30 days ago to most recent). Use window functions (LAG, ROW_NUMBER, RANK) to calculate the momentum for each stock, partition by ticker symbol, order by date. Then rank all stocks by momentum in descending order. Return the top 10 and bottom 10 performers with their ticker, current price, price 30 days ago, momentum percentage, and overall rank. Use a CTE to stage the momentum calculations before ranking._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-09-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Profile Generation
  _Download the NSW Road Crash Data from the NSW government open data portal. Load the CSV into a pandas DataFrame. Clean the data by: (1) handling missing values in severity and location columns, (2) standardizing date formats to ISO 8601, (3) removing duplicate crash records based on crash ID, (4) converting categorical columns (severity, road type) to lowercase and removing leading/trailing whitespace. Create a new column 'fatality_rate' as the ratio of fatalities to total casualties per crash. Export a cleaned CSV file and generate a summary report showing: total crashes, crashes by severity category, top 5 roads by crash frequency, and average fatality rate by severity level._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-16.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Health Trend Analysis Pipeline
  _Build an end-to-end data pipeline: (1) Download Great Barrier Reef monitoring data (coral health indicators, temperature, bleaching events) from AIMS. (2) Use Python/pandas to clean the data: standardize location names, handle missing temperature readings using forward-fill, convert date columns, filter for the last 10 years of records. (3) Export the cleaned data to a SQL database (SQLite or PostgreSQL). (4) Write SQL queries to calculate: (a) year-over-year bleaching event trends using window functions (LAG to compare year-on-year counts), (b) identify reef zones with the steepest health decline using linear regression coefficients (calculate slope per zone using a CTE), (c) correlation between water temperature anomalies and bleaching severity. (5) Export results as a final CSV report with zone name, trend direction, and risk classification (low/medium/high)._
  📦 Dataset: `Great Barrier Reef monitoring data — aims.gov.au`
  📁 Submit as: `quest3_2026-09-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
