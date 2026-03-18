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
| 📅 Last Sync | 2026-03-18 16:19 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Average Momentum Rank
  _Using ASX 200 historical price data, calculate the 20-day rolling average for each stock's closing price. Then rank stocks within each date by their rolling average momentum (current rolling avg vs previous day's rolling avg). Use a CTE to structure rolling averages, then a window function to rank by momentum. Filter for the top 10 stocks by positive momentum on the most recent date in your dataset. Expected output: date, stock_symbol, close_price, rolling_avg_20d, momentum_change, momentum_rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Severity Profiling
  _Download NSW Road Crash Data from data.nsw.gov.au (CSV format). Clean the dataset by: (1) handling missing values in crash severity and road type columns (document your strategy), (2) standardising datetime formats for crash_date, (3) removing duplicate crash records based on crash_id, (4) creating a new column 'time_of_day' categorising crashes into Morning (6-12), Afternoon (12-18), Evening (18-24), Night (0-6). Generate a summary showing crash count and mean number of persons injured by severity level and time_of_day. Output cleaned dataset to CSV and summary statistics to JSON._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-18.py`
- [ ] ⚡ **Combined Quest:** Cricket Australia Venue Performance ETL Pipeline
  _Build a Python script that: (1) reads Cricket Australia match results data (from Kaggle), (2) cleans player names and venue names (handle inconsistent spacing, capitalization), (3) loads cleaned data into a SQLite database with two tables: matches (match_id, venue, date, result) and performances (match_id, player_name, runs, wickets). Then write SQL queries to: (a) rank venues by total runs scored across all matches using ROW_NUMBER, (b) calculate each player's career performance metrics (total runs, total wickets, matches played) and identify their best performance using RANK() partitioned by player. Export final SQL results to CSV. Expected deliverable: SQLite db file + Python ETL script + SQL analysis script + output CSVs._
  📦 Dataset: `Cricket Australia Test & ODI Match Results — Kaggle`
  📁 Submit as: `quest3_2026-03-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
