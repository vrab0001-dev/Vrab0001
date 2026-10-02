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
| 📅 Last Sync | 2026-10-02 12:52 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 30-day rolling average price for each stock ticker, ranks stocks by their current price momentum (price change from 30 days ago), and identifies the top 10 stocks with the highest positive momentum. Use window functions (AVG() OVER, ROW_NUMBER(), LAG()) and CTEs to structure the query. Your output should include: ticker, current_date, current_price, price_30_days_ago, momentum_percentage, and momentum_rank. Filter for data from the last quarter only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-02.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download the NSW Road Crash Data (contains crash details, injury severity, locations, dates). Write a Python script using pandas that: (1) loads the CSV, (2) handles missing values in location and injury severity columns by forward-filling or dropping as appropriate, (3) standardises location names (strip whitespace, convert to lowercase), (4) creates a new column for crash severity classification (fatal, serious injury, non-injury based on injury counts), (5) aggregates crashes by Local Government Area (LGA) and severity level, (6) exports the cleaned dataset to a new CSV. Include error handling for file I/O and data validation checks. Output should show total crashes per LGA with breakdown by severity._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-02.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: SQL Analysis with Python Data Preparation
  _Use the Australian Weather observations dataset (Bureau of Meteorology). Step 1 (Python): Load raw weather CSV files, clean temperature and rainfall columns (handle missing values, convert units if needed), validate date formats, filter for the last 12 months of data from a single state (e.g., NSW or Victoria), and export to a cleaned CSV. Step 2 (SQL): Import the cleaned data into a database. Write a query using window functions to calculate: (a) monthly average temperature and rainfall per station, (b) rank each station by rainfall consistency (lowest standard deviation = most consistent), (c) identify stations where the current month's rainfall is above the 12-month rolling average. Return: station_name, month, avg_temp, total_rainfall, rainfall_rank, is_above_avg. Present top 5 stations with most consistent rainfall patterns._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-10-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
