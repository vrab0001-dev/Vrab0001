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
| 📅 Last Sync | 2026-06-18 12:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Trading Volume Leaders with Ranking
  _Using ASX 200 historical price data, write a query that: (1) calculates the average daily trading volume for each stock over the last 90 days, (2) ranks stocks by volume using ROW_NUMBER() and RANK() window functions to identify the top 10 most actively traded securities, (3) includes a CTE to filter only stocks with a closing price above $10, and (4) returns columns: stock_code, company_name, avg_daily_volume, volume_rank, and price_rank. Order by volume_rank ascending. Explain the difference between ROW_NUMBER() and RANK() in your result comments._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Time Series Preparation
  _Download NSW Road Crash Data (contains crash severity, location, datetime, vehicle types). Using pandas: (1) load the CSV and inspect for missing values and data types, (2) clean the datetime column and extract year, month, day_of_week as separate columns, (3) standardise location names (remove extra whitespace, convert to title case), (4) filter crashes with severity='Fatal' or 'Serious Injury' only, (5) create a new column 'time_period' categorising crashes as 'peak_hours' (7-9am, 4-6pm weekdays) or 'off_peak', (6) export the cleaned dataset to a new CSV file. Print summary statistics before and after cleaning (row counts, null counts, unique values)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-18.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: ETL & Analytics
  _Create an end-to-end data engineering workflow: (1) In Python, fetch/load Australian wine production statistics data (by region and vintage year), clean inconsistent vintage labels (e.g., '2023' vs '23'), handle missing production volumes by forward-filling or interpolating where appropriate, and export to a staging CSV. (2) Load the cleaned CSV into a SQL database (SQLite or PostgreSQL). (3) Write SQL queries to: calculate year-on-year production change by region using LAG() window function, identify the top 5 regions by total production over the last 10 years using a CTE, and rank regions by production growth trend. (4) Export results to a summary CSV with columns: region, total_production, yoy_change_percent, growth_rank. Document your assumptions about missing data handling._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com) or Kaggle`
  📁 Submit as: `quest3_2026-06-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
