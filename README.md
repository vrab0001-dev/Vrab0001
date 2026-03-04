# ⚡ [ SYSTEM STATUS: ONLINE ]

### 👤 PLAYER: Vrab0001
### 🌏 REGION: Australia / India

---

<!-- VRAB_SYSTEM_STATS_START -->
**Status:** ACTIVE 🟢

| Stat | Value |
|------|-------|
| 🎖️ Title | Data Cadet |
| ⚡ Level | 1 |
| 💠 Total XP | 7 +1 XP today |
| 📅 Last Sync | 2026-03-04 12:24 AEDT |

**XP Progress:** `██████████████░░░░░░ 7/10 XP`

### 🛠️ SKILLS UNLOCKED
- 🗄️ **SQL**
- 🧹 **Data Cleaning**
- 🏗️ **Data Modelling**
- 🐍 **Python**
<!-- VRAB_SYSTEM_STATS_END -->

---

### 📜 DAILY QUEST LOG

<!-- VRAB_QUESTS_START -->
- [x] 🗄️ **SQL Quest:** ASX 200 Stock Performance Ranking with Moving Averages
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate the 20-day and 50-day moving averages for each stock's closing price, (2) Rank stocks by their most recent price gain/loss percentage within the last 30 days using ROW_NUMBER(), (3) Use a CTE to identify only stocks where the 20-day MA is above the 50-day MA (bullish signal), and (4) Return the top 10 stocks by momentum with columns: stock_code, current_price, price_change_pct, rank_by_momentum, ma_20, ma_50. Order by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Factor Extraction
  _Download NSW Road Crash Data (from data.nsw.gov.au). Write a Python/pandas script to: (1) Load the crash CSV and inspect for missing values and data types, (2) Clean the data by handling nulls in the 'Severity' and 'Crash_Type' columns (document your strategy), (3) Create three new features: 'Is_Weekend' (True if crash occurred on Saturday/Sunday), 'Speed_Zone_Risk' (categorize speed zones as Low/Medium/High), and 'Light_Condition_Risk' (encode daylight/dusk/night), (4) Remove duplicate records based on Crash_ID, (5) Export a cleaned CSV with all original columns plus the three new features. Print a summary: total records before/after cleaning, percentage of missing values per column, and distribution of your new features._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-04.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Impact Assessment Pipeline
  _Build an end-to-end data engineering workflow: (1) Download the Australian Wildfire dataset (Kaggle). (2) In Python/pandas: Load the CSV, clean date columns, remove invalid lat/long coordinates (outside Australia's bounds: -44 to -10 latitude, 112 to 154 longitude), and calculate fire size categories ('Small' <1000 ha, 'Medium' 1000-10000 ha, 'Large' >10000 ha). Save to a cleaned CSV. (3) Create a SQLite database from the cleaned CSV. (4) Write SQL queries to: Find the top 5 states by total area burned (sum of hectares) across all years, Calculate year-over-year percentage change in fire count for each state, Identify the month with highest fire frequency using window functions (RANK). (5) Return results as three separate outputs (state rankings, YoY change table, monthly frequency analysis). Document your cleaning decisions and any data quality issues found._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-03-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Indian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*