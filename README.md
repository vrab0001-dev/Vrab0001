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
| 📅 Last Sync | 2026-08-06 11:19 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns & Moving Averages
  _Using the ASX 200 historical prices dataset, write a query that calculates the daily percentage return for each stock, then uses a window function to compute the 20-day moving average of returns. Rank stocks by their most recent moving average return (highest to lowest). Include columns: date, stock_code, daily_return_pct, ma_20_day_return, rank. Filter for the top 10 stocks by rank on the most recent date in the dataset. Use a CTE to calculate returns first, then a second CTE for the moving average._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download the NSW Road Crash Data (available as CSV from NSW Open Data). Write a Python script using pandas that: (1) loads the crash data, (2) handles missing values in severity and injury_type columns by imputing with 'Unknown', (3) converts date columns to datetime format, (4) removes duplicate crash records based on crash_id, (5) creates a new column 'month_year' from the date field, (6) exports a cleaned CSV file. Then create a summary DataFrame grouping crashes by month_year and severity level, showing crash count and average number of vehicles involved. Save the summary as a separate CSV._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-06.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Data Pipeline
  _Build an end-to-end pipeline: (1) Use Python/pandas to load the Australian Weather observations dataset (Bureau of Meteorology / Kaggle jsphyg version), clean temperature and rainfall columns (handle missing values, convert to numeric), and filter for observations from the last 5 years. Export to a local SQLite database. (2) Write SQL queries to: identify the station with the highest average daily temperature, calculate monthly total rainfall using window functions (LAG to compare month-over-month change), and rank the top 5 wettest months across all stations. (3) Export the final SQL results to CSV with columns: station_name, month, total_rainfall_mm, rainfall_change_pct, rank. Ensure your Python script and SQL queries are modular and documented._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle jsphyg)`
  📁 Submit as: `quest3_2026-08-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
