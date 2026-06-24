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
| 📅 Last Sync | 2026-06-24 12:01 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Tracker with Window Functions
  _Using ASX 200 historical stock prices, calculate the 20-day moving average price and momentum rank (ROW_NUMBER) for the top 10 most volatile stocks. Create a CTE that identifies stocks where the closing price exceeded their 20-day moving average, then rank these by volatility (standard deviation of daily returns) in descending order. Output: stock_code, current_price, moving_avg_20day, volatility_rank, days_above_ma. Filter for the last 6 months of trading data only._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-06-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Download NSW Road Crash Data and clean it systematically: handle missing values in Crash_Severity, Injury_Count, and Speed_Zone columns (document your strategy for each); standardise suburb names to title case; remove duplicate crash records based on Crash_ID; convert date columns to datetime format. Then create a new risk_score column calculated as: (injury_count * 0.6) + (severity_category_encoded * 0.4), where severity is numerically encoded (Non-injury=1, Other injury=2, Serious injury=3, Fatality=4). Export the cleaned dataset to CSV with metadata (rows processed, nulls handled, duplicates removed) as a summary comment at the top of the file._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-24.py`
- [ ] ⚡ **Python + SQL Quest:** Australian Weather Patterns ETL Pipeline
  _Extract Australian Bureau of Meteorology weather observation data (or Kaggle equivalent) covering at least 3 Australian cities over 12 months. Use Python (pandas) to: load the CSV, clean temperature/humidity/rainfall columns (handle outliers, missing values), aggregate daily data into weekly summaries (mean temp, max temp, total rainfall, average humidity). Create a Python script that writes this cleaned, aggregated data to a SQL database (SQLite is fine). Then query using SQL to find: which city had the highest average weekly rainfall, which week saw the greatest temperature swing (max_temp - min_temp), and use LAG() to identify consecutive weeks where rainfall exceeded 50mm. Output a summary table: city, week_ending_date, avg_temp, max_rainfall_consecutive_weeks._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-06-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
