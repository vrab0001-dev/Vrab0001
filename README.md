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
| 📅 Last Sync | 2026-06-20 12:07 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Volatility Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of daily returns for the top 10 companies by market cap. Use window functions (ROW_NUMBER, LAG) to compute daily percentage returns, then rank stocks by volatility. Your output should show: Company symbol, date, closing price, daily return %, 30-day rolling volatility, and volatility rank. Filter for the last 6 months of data and order by date descending then volatility rank ascending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-20.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Incident Categorisation
  _Download the NSW Road Crash Data from data.nsw.gov.au. Load the CSV and perform the following: (1) Handle missing values in the 'Severity' and 'Crash Type' columns by investigating patterns—use mode imputation where appropriate, document nulls elsewhere; (2) Standardise location data by converting all suburb names to title case and removing leading/trailing whitespace; (3) Create a new 'Time_of_Day' column that categorises 'Crash Time' into 'Night' (20:00-05:59), 'Morning' (06:00-11:59), 'Afternoon' (12:00-17:59), 'Evening' (18:00-19:59); (4) Export the cleaned dataset to a new CSV with a timestamp suffix. Document data quality issues found (row count before/after, % missing per column)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-20.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a Python + SQL pipeline using Australian Weather observations (Bureau of Meteorology data on Kaggle). Step 1 (Python): Load monthly temperature and rainfall CSV data. Clean by removing duplicates on (station_id, date), handle missing temps/rainfall with forward-fill method. Create a 'Month_Year' column and calculate 30-year climatological normals (1990-2020 average) per station per month. Export cleaned data and normals to two separate CSVs. Step 2 (SQL): Load both CSVs into a local SQLite database. Write a query using CTEs to identify anomalies: months where actual temperature >2°C above normal OR rainfall >150% of normal. Your output should show: station_id, month_year, actual_temp, normal_temp, deviation, actual_rainfall, normal_rainfall, anomaly_type, ranked by severity (largest deviation first). Include only the last 5 years of data._
  📦 Dataset: `Australian Weather Observations (1990-2024) — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-06-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
