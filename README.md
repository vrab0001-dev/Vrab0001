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
| 📅 Last Sync | 2026-09-09 11:53 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility using ROW_NUMBER() and identify the top 5 most volatile stocks in the last 90 days. Use a CTE to calculate daily returns (Close - Previous Close / Previous Close) with LAG(), then another CTE for rolling volatility. Return: stock_code, company_name, avg_volatility_30d, rank, and date_range_analysed. Sort by rank ascending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Missing Value Imputation
  _Download the NSW Road Crash Data (contains crash reports with location, severity, weather conditions, vehicle types). Write a pandas script to: (1) identify all missing values and data types; (2) remove rows where Crash_Severity is null; (3) fill Weather_Condition nulls with mode by Crash_Month; (4) standardise Location names (strip whitespace, convert to title case); (5) create a new feature Crash_Hour from Crash_Time; (6) export cleaned data to CSV. Document your cleaning decisions in comments. Expected output: cleaned_nsw_crashes.csv with no null values in critical columns._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-09.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: Load, Clean, Analyse & Report
  _Build a mini data pipeline: (1) Use Python to download/load Australian wine production statistics (vintage year, region, grape variety, production volume, quality rating). (2) Clean the data: handle missing values, standardise region names, validate numeric columns. (3) Load cleaned data into a local SQLite database with proper schema (tables: wines, regions, production_facts). (4) Write SQL queries to find: top 5 regions by total production volume (past 10 years), average quality rating by grape variety, year-on-year production growth rate using LAG(). (5) Export results to CSV. Deliverables: Python script (load + clean), SQL schema file, query results CSV, and a brief summary of key insights (2-3 sentences)._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com data or Kaggle equivalent)`
  📁 Submit as: `quest3_2026-09-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
