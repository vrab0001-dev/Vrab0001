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
| 📅 Last Sync | 2026-05-26 11:58 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a query that ranks stocks by their 30-day percentage gain using window functions. For each stock in your dataset, calculate: (1) ROW_NUMBER() partitioned by stock_code ordered by date descending to identify the most recent price, (2) LAG() to get the price from 30 days ago, (3) percentage gain as ((current_price - price_30_days_ago) / price_30_days_ago * 100), and (4) RANK() to rank stocks by this percentage gain. Filter to show only the top 10 best and bottom 10 worst performers. Expected output: stock_code, company_name, current_price, price_30_days_ago, percentage_gain, performance_rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-26.sql`
- [ ] 🐍 **Python Quest:** Clean and Standardise NSW Road Crash Data
  _Download or load the NSW Road Crash Data and perform comprehensive data cleaning: (1) identify and handle missing values in critical columns (crash_severity, vehicle_type, weather_condition), (2) standardise text fields to title case and remove leading/trailing whitespace, (3) convert date columns to datetime format, (4) remove duplicate records based on crash_id, (5) create a new column 'is_fatal' as a boolean flag where severity equals 'Fatal', (6) export the cleaned dataset to a CSV file named 'nsw_crashes_cleaned.csv'. Document your cleaning decisions in comments. Expected output: a valid CSV file with no null values in critical columns and consistent formatting._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-26.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Load, Clean, and Analyse Monthly Trends
  _Complete a full data engineering pipeline: (1) In Python, load Australian Weather observations data (use Bureau of Meteorology or Kaggle's jsphyg dataset), clean temperature and rainfall columns (handle missing values, convert to numeric types, remove outliers using IQR method), and aggregate data to monthly averages by location, then export to CSV. (2) In SQL, load this cleaned CSV, create a table, and write a query using CTEs and window functions to: calculate 12-month rolling average of temperature for each location, rank locations by their most recent month's rainfall, and identify any months where temperature exceeded the location's historical average by >2 standard deviations. Expected output: (a) cleaned CSV file, (b) SQL results showing location, month, rolling_avg_temp, rainfall_rank, and anomaly_flag._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg dataset)`
  📁 Submit as: `quest3_2026-05-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
