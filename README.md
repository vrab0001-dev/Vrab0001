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
| 📅 Last Sync | 2026-11-19 15:49 AEDT |

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
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility within each month using ROW_NUMBER(). Identify the top 5 most volatile stocks in the latest month and show their current price, average return, and volatility ranking. Expected output: table with stock symbol, price, avg_daily_return, rolling_std_dev, and volatility_rank columns, ordered by volatility rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (contains crash reports with missing values, inconsistent date formats, and duplicate entries). Write a Python script using pandas to: (1) standardise datetime columns to ISO format, (2) handle missing values in location and severity columns with appropriate strategies, (3) remove duplicate crash records based on crash ID and timestamp, (4) create a new column categorising crash severity as 'Fatal', 'Serious Injury', 'Other Injury', or 'Non-Injury', (5) export cleaned data to CSV. Expected output: cleaned CSV file with 90%+ data completeness, no duplicates, and new severity category column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-19.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL Pipeline
  _Build an end-to-end pipeline combining Python and SQL: (1) Use Python with pandas to scrape/load Australian wine production statistics by region and vintage year (from Wine Australia or Kaggle wine dataset). Clean the data by removing outliers (using IQR method), standardising region names, and handling missing vintage years. (2) Load cleaned data into a SQL database (SQLite or PostgreSQL). (3) Write SQL queries to: calculate 5-year rolling average production by region using window functions, rank regions by average production volume using RANK(), and identify regions with the highest year-over-year production growth. Expected deliverables: (a) Python ETL script, (b) SQL schema creation script, (c) 3 analytical SQL queries with results showing top 10 regions by rolling average production, regional rankings, and growth leaders._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia or Kaggle`
  📁 Submit as: `quest3_2026-11-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
