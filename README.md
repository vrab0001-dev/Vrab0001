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
| 📅 Last Sync | 2026-11-07 14:31 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) the 30-day moving average of closing price for each stock, (2) the daily price change rank within each stock (highest gain = rank 1), and (3) identify the date when each stock hit its 52-week high. Use ROW_NUMBER() and LAG() window functions. Filter for the top 10 stocks by trading volume. Return columns: stock_code, date, close_price, moving_avg_30d, price_change_rank, weeks_52_high_date. Order by stock_code and date._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data (available from NSW Open Data portal). Write a Python pandas script to: (1) handle missing values in crash severity and contributing factors columns (document your strategy), (2) create new features: crash_hour from datetime, is_weekend boolean, severity_category (ordinal encoding: minor/moderate/serious/fatal), (3) standardise location data by removing duplicates and normalising suburb names to title case, (4) export cleaned dataset to CSV with summary statistics (total crashes, crashes by severity, top 5 suburbs). The script should be robust and handle edge cases like malformed dates._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-07.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: SQL Aggregation + Python Export
  _Build a data pipeline using Australian wine production statistics (ABARES or Wine Australia data). Step 1 (SQL): Write a query to aggregate wine production by region and vintage year, calculate year-over-year growth using LAG() window function, and identify the top 3 regions by average production volume over the last 5 years. Step 2 (Python): Read the SQL query results, use pandas to create: (a) a pivot table showing region vs. vintage with production volumes, (b) a bar chart visualization of top regions, (c) export a summary report as CSV with regions, average production, growth trend, and recommendations for high-growth regions. Combine both steps in a single Python script that executes SQL and processes results._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com) or ABARES (agriculture.gov.au)`
  📁 Submit as: `quest3_2026-11-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
