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
| 📅 Last Sync | 2026-11-05 14:58 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Ranking with Window Functions
  _Using ASX 200 historical stock price data, write a query that calculates for each stock: (1) the cumulative return from the earliest date to most recent date using window functions, (2) rank stocks by return percentile using RANK() and PERCENT_RANK(), (3) identify the date each stock hit its 52-week high using ROW_NUMBER(), and (4) calculate the 30-day moving average of closing price using AVG() with ROWS BETWEEN. Filter for the top 20 performers by return and order by stock symbol. Expected output: stock_symbol, cumulative_return_pct, return_rank, date_52week_high, moving_avg_30day._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Load NSW Road Crash Data from data.nsw.gov.au. Perform the following data cleaning tasks: (1) handle missing values in injury_type and crash_type columns (choose appropriate strategy: drop, forward-fill, or mode-impute based on missingness %), (2) standardise datetime columns to ISO format, (3) remove duplicate records based on crash_id and date combination, (4) create new features: crash_hour (extracted from time), day_of_week, is_weekend flag, and severity_category (bin injury counts into Low/Medium/High), (5) detect and handle outliers in speed_limit and vehicle_count using IQR method. Save cleaned dataset to CSV with data quality report showing row counts before/after and missing % per column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-05.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Build an end-to-end data pipeline: (1) Extract temperature and rainfall data from Bureau of Meteorology / Kaggle weather dataset for 5 major Australian cities over the past 5 years. (2) Use Python/pandas to load, clean, and calculate rolling 30-day average temperatures and cumulative monthly rainfall. Export to a staging table in SQLite. (3) Write SQL queries with CTEs to: identify months where temperature exceeded 2 standard deviations above the 5-year mean (anomalies), rank cities by anomaly frequency, and calculate the YoY (year-over-year) change in average annual rainfall using LAG() window function. (4) Output a final report showing: city, anomaly_month, temp_deviation_stddev, rainfall_yoy_change_pct, and anomaly_rank_by_city. Document your data quality checks._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-11-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
