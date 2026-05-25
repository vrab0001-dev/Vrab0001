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
| 📅 Last Sync | 2026-05-25 12:07 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Ranking with Window Functions
  _Using ASX 200 historical price data, calculate the daily percentage return for each stock. Then use window functions to rank stocks by return within each date, and add a column showing the 5-day moving average of returns for each stock. Use ROW_NUMBER() OVER (PARTITION BY date ORDER BY return DESC) to rank daily performers, and LAG() to calculate the moving average. Filter for stocks that ranked in the top 10 on any given day in the last 30 days of data. Output should include: stock_code, date, closing_price, daily_return_pct, rank_by_date, five_day_avg_return._
  📦 Dataset: `ASX 200 Historical Stock Data — Kaggle`
  📁 Submit as: `quest1_2026-05-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data from data.nsw.gov.au. Load the CSV and perform the following: (1) Handle missing values in injury severity and crash type columns using forward fill within date groups; (2) Create a new feature 'time_of_day' that categorizes crash_time into 'early_morning' (0-6), 'morning_peak' (6-10), 'afternoon' (10-17), 'evening_peak' (17-19), 'night' (19-24); (3) Remove duplicate crash records based on crash_id and date; (4) Create a summary CSV with: count of crashes by time_of_day and suburb, average injured_count by severity level. Use pandas and ensure output is clean, sorted, and saved as 'nsw_crash_summary.csv'._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-25.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: Load, Clean, Aggregate & Query
  _Work with Australian Weather observations dataset. Step 1 (Python): Load the raw CSV, clean temperature and rainfall columns (convert to numeric, handle missing values), filter for the 5 major Australian cities (Sydney, Melbourne, Brisbane, Perth, Adelaide), and resample daily data to monthly averages. Save the cleaned monthly data to a SQLite database in a table named 'monthly_weather'. Step 2 (SQL): Query the SQLite database to find: (1) The month with the highest average temperature in each city (2024 onwards); (2) Cities with a rainfall trend (using LAG and comparing current month to previous month) increasing in the last 6 months; (3) A CTE that calculates the 3-month rolling average of temperature for each city, then identify anomalies (temperatures exceeding 2 standard deviations from the rolling average). Output all three result sets._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle jsphyg)`
  📁 Submit as: `quest3_2026-05-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
