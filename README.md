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
| 📅 Last Sync | 2026-07-26 11:28 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Top Performers: Rank Stocks by Rolling 30-Day Returns
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate each stock's rolling 30-day return (percentage change from close price 30 days ago to current close). Rank stocks daily by their rolling return using ROW_NUMBER() PARTITION BY date. Filter to show only the top 5 performers for each date in the last quarter of data. Include columns: date, ticker, close_price, rolling_30day_return, daily_rank. Use a CTE to calculate the rolling return, then a second CTE to rank. Expected output: 75-90 rows (assuming ~20-25 trading days per quarter × 5 top stocks)._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-26.sql`
- [ ] 🐍 **Python Quest:** Clean NSW Road Crash Data: Standardise Locations and Handle Missing Values
  _Download the NSW Road Crash Data (data.nsw.gov.au). Load the CSV into pandas and perform comprehensive data cleaning: (1) Standardise the 'Suburb' and 'Local Government Area' columns to title case and remove leading/trailing whitespace. (2) Handle missing values in 'Speed Limit' by filling with the median speed limit grouped by road type. (3) Parse the 'Crash Date' column into a proper datetime format. (4) Remove duplicate rows based on crash ID. (5) Create a new column 'Severity_Category' by binning injury counts into 'Minor', 'Moderate', 'Severe'. Export the cleaned dataset to a new CSV file. Report: number of rows removed as duplicates, number of null values filled, and summary statistics of the cleaned data._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-26.py`
- [ ] ⚡ **Combined Quest:** Energy Generation Mix Analysis: Python ETL + SQL Analytics
  _Part 1 (Python): Download AEMO electricity demand and generation data. Use pandas to reshape the dataset from wide to long format (columns to rows), clean timestamp columns, and extract fuel source type. Handle missing values by forward-filling within each state and fuel source. Export to a clean CSV. Part 2 (SQL): Load the cleaned CSV into a database. Write a query using CTEs and window functions to: (1) Calculate each state's generation percentage by fuel source per month. (2) Use LAG() to find month-over-month percentage change for renewable energy (wind + solar combined). (3) Identify which state had the highest renewable generation growth rate over the dataset period. Include columns: state, month, renewable_pct, mom_change_pct, growth_rank. Expected output: 10-15 rows showing top-performing states._
  📦 Dataset: `AEMO Electricity Demand and Generation Data — aemo.com.au`
  📁 Submit as: `quest3_2026-07-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
