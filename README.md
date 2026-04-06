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
| 📅 Last Sync | 2026-04-06 11:17 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Ranking with Moving Average
  _Using ASX 200 historical price data, write a query that calculates daily percentage returns for each stock, then uses window functions to rank stocks by returns within each date partition. Additionally, compute a 7-day moving average of closing prices for each stock ordered by date. Use a CTE to isolate high-volatility stocks (those ranking in top 10% by absolute return on any given day). Return: stock_code, trading_date, daily_return_pct, return_rank, moving_avg_7day, volatility_flag. Order by trading_date DESC, return_rank ASC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (motor vehicle crashes from data.nsw.gov.au). Load the CSV into pandas and perform: (1) Handle missing values in crash_type, weather_condition, and severity columns using forward-fill within each local government area; (2) Create a new feature 'crash_hour_bin' grouping time_of_crash into 6-hour buckets (Night, Morning, Afternoon, Evening); (3) Remove outliers in speed_zone using IQR method; (4) Generate a summary DataFrame showing crashes per local_government_area, crash_hour_bin, and severity. Export cleaned data to CSV and summary stats to JSON. Include data quality report showing % missing before/after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-06.py`
- [ ] ⚡ **Python + SQL Quest:** COVID-19 Australia Vaccination Trend Analysis Pipeline
  _Build an end-to-end pipeline: (1) Extract COVID-19 Australia vaccination data (from Kaggle COVID-19 dataset or data.gov.au). (2) Use pandas to clean and transform: calculate daily vaccination rate (doses/100k population), resample to weekly averages, identify peaks and troughs. (3) Create a SQLite database with tables for raw_vaccinations and weekly_summaries. (4) Write SQL queries to find: the state with highest peak vaccination rate, weeks with >20% week-over-week growth, cumulative doses by state. (5) Export results showing state, week_ending_date, weekly_doses_per_100k, growth_rate_pct, rank_by_state. Validate data integrity: ensure no negative vaccination rates, dates are sequential, population figures are consistent._
  📦 Dataset: `COVID-19 Australia Dataset — Kaggle or data.gov.au`
  📁 Submit as: `quest3_2026-04-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
