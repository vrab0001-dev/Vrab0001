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
| 📅 Last Sync | 2026-03-16 16:58 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns & Volatility Ranking
  _Using ASX 200 historical price data, write a SQL query with window functions to: (1) Calculate daily percentage returns for each stock using LAG(), (2) Compute a 20-day rolling volatility (standard deviation of returns) using window frames, (3) Rank stocks by volatility using RANK() OVER (ORDER BY volatility DESC), (4) Identify the top 10 most volatile stocks and their average returns over the last 90 days using CTEs. Return: stock_symbol, current_price, daily_return_pct, volatility_20d, volatility_rank, avg_return_90d._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (traffic incidents with injury severity, location, vehicle type, weather conditions). Build a Python script using pandas to: (1) Handle missing values in severity and location columns (document strategy), (2) Standardise date formats and extract year/month/day, (3) Clean and categorise vehicle types (consolidate similar types), (4) Remove duplicates based on crash_id and timestamp, (5) Create a summary CSV with crash counts by: local government area, severity level, and month. Output: cleaned_crashes.csv and summary_by_lga_severity_month.csv. Include data quality report (rows removed, null percentages before/after)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-16.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production: Trend Analysis Pipeline
  _End-to-end task: (1) Extract Australian wine production data by region and varietal (source: Wine Australia statistics or ABS agriculture data). (2) Use Python/pandas to load the CSV, clean region names (remove extra spaces, standardise case), handle missing production volumes, and create a year-on-year growth percentage column. (3) Load cleaned data into a SQLite database with schema: regions(region_id, region_name), varietals(varietal_id, varietal_name), production(year, region_id, varietal_id, volume_tonnes, growth_pct). (4) Write SQL queries to: identify the top 3 growing varietals per region using ROW_NUMBER(), calculate 5-year CAGR for each region using window functions and CTEs, rank regions by total production volume. (5) Export results to production_trends.csv. Expected output: cleaned data, populated SQLite database, and analytical results._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia / ABS`
  📁 Submit as: `quest3_2026-03-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
