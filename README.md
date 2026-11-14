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
| 📅 Last Sync | 2026-11-14 14:51 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate the 30-day price momentum for each stock. Rank stocks by momentum within each sector. Use ROW_NUMBER() to identify the top 3 performers per sector, and LAG() to compare current price against 30 days prior. Return columns: date, ticker, sector, current_price, price_30_days_ago, momentum_percentage, sector_rank. Filter for the most recent trading date only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (2020–2025). Clean the dataset by: (1) handling missing values in crash_type and severity columns (document your strategy), (2) standardising location data (removing extra whitespace, converting to title case), (3) creating new features: hour_of_day (from crash_time), is_fatal (binary from severity), and region (grouping LGA into broader NSW regions). Export the cleaned dataset as 'nsw_crashes_cleaned.csv' with 8–10 rows of sample output printed to console showing your transformations._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-14.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production & Export Analysis Pipeline
  _Build a Python + SQL pipeline: (1) In Python, fetch or load Australian wine production statistics (by region and vintage year). Clean the data, handle any missing production volumes, and load it into a SQLite database table called 'wine_production'. (2) In SQL, write a query using CTEs to calculate: total production by region, year-over-year growth rate (using LAG()), and the top 3 regions by average export volume. (3) Export results to 'wine_analysis_report.csv' with columns: region, year, production_volume, yoy_growth_pct, export_volume. Document your data cleaning decisions in comments within the Python script._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com) or ABS agriculture data`
  📁 Submit as: `quest3_2026-11-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
