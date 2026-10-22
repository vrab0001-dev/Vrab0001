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
| 📅 Last Sync | 2026-10-22 13:12 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Average & Momentum Ranking
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate a 20-day rolling average of closing prices for each stock ticker; (2) Use ROW_NUMBER() to rank stocks by their price momentum (current price vs 20-day avg) within each date; (3) Use a CTE to filter only the top 10 momentum gainers per trading day; (4) Return ticker, date, close_price, rolling_avg_20d, and momentum_rank. Ensure your query handles NULL values gracefully and orders results by date DESC, then momentum_rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Score Calculation
  _Download the NSW Road Crash Data (available as CSV). Write a Python/pandas script to: (1) Load the dataset and inspect data types, missing values, and duplicates; (2) Clean crash severity categories by standardising text (trim whitespace, consistent casing); (3) Handle missing values in speed_zone_posted and severity columns using forward-fill or domain logic; (4) Create a new 'safety_score' column (0–100 scale) based on injury_count, vehicle_count, and severity; (5) Export the cleaned dataset to a new CSV file. Document any assumptions you make about data imputation._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-22.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Trend Analysis & Export Report
  _Integrate Python and SQL: (1) Use Python/pandas to fetch or load the Australian wine production statistics dataset (by region and vintage year). Clean column names, standardise region names (handle spelling variations), and convert production volumes to consistent units (tonnes). Save to a local SQLite database using SQLAlchemy. (2) In SQL, write a query using CTEs and window functions to: calculate 5-year rolling average production by region; use RANK() to identify top-3 producing regions per decade; compute year-over-year growth % using LAG(). (3) Export results to CSV with columns: region, year, production_tonnes, rolling_avg_5yr, region_rank, yoy_growth_pct. Document your data quality decisions in a brief markdown comment within the Python script._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia / ABS`
  📁 Submit as: `quest3_2026-10-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
