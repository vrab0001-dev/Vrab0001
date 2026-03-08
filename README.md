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
| 📅 Last Sync | 2026-03-08 16:00 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 30-day moving average price for each stock using LAG or frame clauses; (2) Rank stocks by their YTD percentage gain using RANK() OVER (ORDER BY gain DESC); (3) Identify the top 5 stocks with the highest volatility (standard deviation of daily returns) using window functions and CTEs. Return stock ticker, current price, 30-day MA, YTD rank, and volatility rank. Order by volatility rank descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (contains crashes, vehicles, persons tables). Write a Python/pandas script to: (1) Load all three CSV files; (2) Clean missing values in critical columns (crash_date, latitude, longitude, accident_type); (3) Standardise date formats and remove duplicates; (4) Merge the tables on crash_id; (5) Create a summary CSV with crashes grouped by Local Government Area (LGA), showing total crashes, fatalities, and injuries per LGA; (6) Identify and flag the top 10 dangerous LGAs. Output: cleaned_crashes.csv and lga_summary.csv with quality metrics (rows before/after cleaning)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-08.py`
- [ ] ⚡ **Combined Quest:** Bureau of Meteorology Weather Data Pipeline with SQL Analytics
  _Write a Python script to: (1) Download Australian Weather observations (daily data for 3 major cities: Sydney, Melbourne, Brisbane) from BoM Kaggle dataset; (2) Clean temperature, rainfall, and humidity columns (handle missing values, convert units if needed); (3) Load the cleaned data into a local SQLite database with a schema including date, city, temp_max, temp_min, rainfall, humidity; (4) Write SQL queries to: calculate rolling 7-day average temperature per city using window functions, identify days with extreme weather (temp > 35°C or rainfall > 50mm), rank cities by average annual rainfall using RANK(). Output: (a) SQLite database file, (b) Python preprocessing script with validation checks, (c) SQL results as CSV showing top 10 hottest days and rainfall rankings._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-03-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
