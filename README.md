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
| 📅 Last Sync | 2026-03-19 16:15 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility Analysis
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for the top 5 most volatile stocks. Use a CTE to first calculate daily percentage changes, then apply ROW_NUMBER() PARTITION BY stock_code to rank stocks by volatility. Finally, use a window function to compute the rolling 30-day standard deviation. Return stock_code, date, daily_return, and rolling_volatility ordered by date descending, volatility descending. This teaches you CTEs, window functions, and financial metrics calculation._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-03-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (contains injury crashes with detailed attributes). Build a Python script using pandas that: (1) loads the CSV and inspects for missing values, (2) standardises date columns to datetime format, (3) removes duplicates based on crash_id, (4) creates a new column 'severity_category' by binning injury count into Low/Medium/High/Critical, (5) filters for crashes in Sydney region only, (6) exports cleaned data to a new CSV. Document the data quality issues found and rows removed at each step. Expected output: cleaned CSV with 5+ new insights printed to console about crash patterns._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-19.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Extremes Data Pipeline
  _Create an end-to-end pipeline combining Python and SQL. Step 1 (Python): Download Australian Weather observations (Bureau of Meteorology dataset on Kaggle). Load CSV, clean temperature and rainfall columns (handle missing values, convert to numeric), and create a 'extreme_event' flag for days where temp > 95th percentile OR rainfall > 95th percentile. Save to a staging CSV. Step 2 (SQL): Load staging CSV into a SQLite database. Write a query using window functions (LAG/LEAD) to identify consecutive days of extreme events, count streak lengths, and identify the state with the longest heat/rain streak. Return state, streak_length, start_date, end_date, event_type. This teaches you full data engineering workflow: extract, transform, load, analyse._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-03-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
