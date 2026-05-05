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
| 📅 Last Sync | 2026-05-05 11:45 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Top Performers: Window Functions Challenge
  _Using the ASX 200 historical stock prices dataset, write a SQL query with window functions to: (1) Calculate the 20-day moving average for each stock's closing price using ROW_NUMBER and AVG() OVER a window; (2) Rank stocks by their price change percentage within each sector using RANK(); (3) Use LAG() to find the day-over-day price change; (4) Filter for stocks in the top 3 of their sector by performance. Return: stock_code, sector, current_price, moving_avg_20day, rank_in_sector, price_change_pct. Order by sector, rank. This tests your understanding of window functions, partitioning, and analytical queries._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download the NSW Road Crash Data (CSV format) from data.nsw.gov.au. Write a Python/pandas script to: (1) Load the dataset and identify missing values, data types, and anomalies; (2) Clean date/time columns, standardise categorical values (e.g., crash_type, severity); (3) Remove duplicates and handle outliers (e.g., impossible injury counts); (4) Create new features: day_of_week, hour_of_day from datetime, crash_severity_score; (5) Aggregate crashes by suburb and severity level; (6) Export cleaned data to a new CSV. Expected output: a clean CSV with 8+ columns, no null values in key fields, and a summary report (print row counts before/after cleaning, number of duplicates removed)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-05.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Python ETL + SQL Analysis
  _End-to-end data engineering task: (1) Download Australian Weather observations data (Bureau of Meteorology dataset via Kaggle). (2) Use Python/pandas to load, clean, and transform: parse dates, handle missing temperature/rainfall values, standardise location names, filter for the last 12 months, create monthly_avg_temp and monthly_total_rainfall columns. (3) Load cleaned data into a SQLite database (create weather_observations table). (4) Write SQL queries to: identify the 5 hottest and 5 wettest locations; calculate month-over-month temperature change using LAG(); rank locations by rainfall consistency (lowest variance = most consistent). (5) Export results to CSV. Deliverables: cleaned CSV, SQLite .db file, SQL query file, and results CSV with rankings._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle jsphyg)`
  📁 Submit as: `quest3_2026-05-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
