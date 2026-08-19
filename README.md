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
| 📅 Last Sync | 2026-08-19 10:32 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum Analysis
  _Using ASX 200 historical stock prices, calculate for each stock: (1) the daily percentage change, (2) a 5-day moving average of closing price using window functions, (3) rank stocks by momentum (% change) within each trading date, (4) identify stocks that crossed above their 5-day MA on any given day. Use CTEs to break down the logic. Return: date, stock_code, close_price, pct_change, ma_5day, momentum_rank, crossed_ma (boolean). Filter to top 20 movers by momentum rank per date._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-19.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning & Aggregation
  _Download Australian Bureau of Meteorology observations (or use a weather dataset from Kaggle). Clean the dataset by: (1) handling missing temperature/rainfall values (document your imputation strategy), (2) converting date strings to datetime, (3) removing duplicate station records, (4) standardising column names to snake_case. Then aggregate daily data to monthly summaries per station: mean temp, max temp, total rainfall, observation count. Export cleaned daily data and monthly summary to separate CSV files. Document all cleaning decisions in comments._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest2_2026-08-19.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Hotspot Pipeline
  _Build a data pipeline: (1) In Python/pandas: load NSW Road Crash Data, clean injury severity codes, geocode suburb names, handle missing coordinates, create a crash severity score (0-10 based on injuries/fatalities). (2) In SQL: load cleaned data into a local database. Write a query using window functions to rank suburbs by crash frequency over rolling 12-month windows, identify trend (increasing/decreasing crashes YoY), and flag hotspots (top 10% by injury severity). (3) Output: CSV with suburb, crash_count, severity_score, rank, trend_direction, is_hotspot. Bonus: visualise top 5 hotspots as a simple text-based chart in Python._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-08-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
