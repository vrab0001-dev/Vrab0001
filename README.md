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
| 📅 Last Sync | 2026-11-28 16:17 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Ranking with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility within each month using ROW_NUMBER(). Identify the top 5 most volatile stocks in the most recent month. Expected output: columns for stock ticker, month, volatility rank, 30-day std dev, and closing price. Use a CTE to calculate daily returns (percentage change from previous day) before computing rolling statistics._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash data and clean it systematically: handle missing values in Crash Severity and Weather Condition columns (document your strategy), standardise date formats, remove duplicate records based on crash ID, and create new features including time-of-day categories (early morning 00-06, morning 06-12, afternoon 12-18, evening 18-24) and day-of-week. Output a cleaned CSV with all original columns plus new engineered features. Document any rows removed and reasoning in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-28.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL Pipeline
  _Build a mini ETL pipeline: (1) Use Python/pandas to fetch or load Australian wine production statistics by region and variety, clean column names (remove spaces, standardise case), handle any missing production volumes by forward-filling or regional averages, and export to a staging CSV. (2) Create a SQL schema with tables for regions, wine varieties, and production records. (3) Write a Python script to load the cleaned CSV into SQLite or PostgreSQL. (4) Write a SQL query using window functions to calculate year-over-year production growth per region and identify which regions increased production most significantly. Expected deliverables: cleaned CSV, SQL schema DDL, Python loader script, and analytical query results showing top growth regions._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com data)`
  📁 Submit as: `quest3_2026-11-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
