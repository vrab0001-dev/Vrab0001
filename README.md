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
| 📅 Last Sync | 2026-05-06 11:29 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates for each stock: (1) the 30-day moving average of closing price using a window function, (2) the rank of each stock by total trading volume within its sector using RANK(), and (3) the percentage change from the previous day's close using LAG(). Filter for the top 20 stocks by volume in the last 30 days and order by sector and rank. Expected output: stock_code, sector, close_price, moving_avg_30d, volume_rank, pct_change_from_prev_day._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Classification Pipeline
  _Download the NSW Road Crash Data (contains messy, inconsistent severity codes, missing postcodes, and date formatting issues). Build a pandas script that: (1) standardises the Severity column (map variants like 'Fatal', 'FATAL', 'F' to canonical values), (2) fills missing Postcode values using the Suburb-to-Postcode lookup you create from non-null rows, (3) converts Date columns to datetime format and extracts Day of Week, (4) removes duplicate crash records (same location, date, time), and (5) exports a clean CSV. Log the number of rows removed/standardised at each step. Expected output: clean_crashes.csv with 5+ quality metrics printed._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-06.py`
- [ ] ⚡ **Combined (Python + SQL) Quest:** Australian Wine Production ETL: Load, Transform, and Trend Analysis
  _Extract data from the Australian Wine Production dataset (available from Wine Australia / Kaggle). (1) Use Python/pandas to load the raw CSV, clean region names (standardise case, remove extra spaces), validate production volumes (remove negative/zero values), and handle missing vintage years by forward-filling. (2) Export the cleaned data to a SQLite database. (3) Write SQL queries to: calculate year-over-year production growth by region using window functions (LAG), identify the top 5 regions by average production volume over the last 10 years using CTEs, and rank wine varieties by total production. (4) Generate a summary report (CSV) showing region, variety, 5-year trend (increasing/stable/decreasing), and YoY growth %. Expected output: SQLite database + cleaned_wine_data.csv + wine_analysis_report.csv._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia / Kaggle`
  📁 Submit as: `quest3_2026-05-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
