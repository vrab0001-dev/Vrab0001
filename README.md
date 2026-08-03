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
| 📅 Last Sync | 2026-08-03 11:28 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Volatility Analysis with Window Functions
  _Using ASX 200 historical prices, write a SQL query with window functions to calculate: (1) the 20-day moving average of closing prices for each stock, (2) the daily percentage change ranked by magnitude within each stock, and (3) identify the date each stock hit its 52-week high. Use ROW_NUMBER() or RANK() to handle ties, and LAG() to compute percentage changes. Output should show stock symbol, date, closing price, 20-day moving average, percentage change rank, and 52-week high date. Filter for the top 10 ASX 200 stocks by market cap._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-03.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation
  _Download NSW Road Crash data and write a Python/pandas script to: (1) handle missing values in the 'Injury Level' and 'Speed Zone' columns by imputing with mode, (2) standardise the 'Local Government Area' column (trim whitespace, convert to title case), (3) create a new feature 'crash_hour' extracted from the datetime column, (4) remove duplicate crash records based on crash ID and timestamp, and (5) aggregate crashes by LGA and hour to produce a summary CSV showing total crashes, injuries, and fatalities per LGA-hour combination. Export the cleaned dataset and summary to CSV files._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-03.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Severity Pipeline
  _Build an end-to-end data pipeline: (1) In Python, load Australian Wildfire dataset (from Kaggle) and use pandas to clean the data: remove rows with missing fire duration, standardise location names, and convert date columns to datetime format. Create a feature 'fire_severity_score' = (acres burned / 1000) * (duration in days). (2) Export cleaned data to a CSV. (3) In SQL, load the CSV into a table and write a query using CTEs to: (i) rank fires by severity score within each Australian state using RANK(), (ii) calculate the cumulative burned acres by state ordered by date using SUM() window function, (iii) identify the top 5 most severe fire seasons (group by year) and include fire count and total acres burned. Output final results showing state, year, fire rank, cumulative acres, and seasonal metrics._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-08-03.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
