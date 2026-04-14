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
| 📅 Last Sync | 2026-04-14 11:21 AEDT |

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
  _Using ASX 200 historical price data, calculate the 20-day rolling standard deviation (volatility) for the top 5 most traded stocks by volume. Use a CTE to first rank stocks by total trading volume over the entire period, then apply a window function to compute rolling volatility. Return: stock symbol, date, closing price, 20-day rolling volatility, and rank of volatility within that stock's history. Order by stock and date. Focus on stocks with complete data across the full period to avoid NULL values._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (CSV format). Clean the dataset by: (1) handling missing values in Severity, Speed_Zone, and Road_Type columns using mode imputation for categorical and median for numeric, (2) standardizing date formats and extracting day_of_week and hour_of_day as new features, (3) removing duplicate crash records based on Crash_ID, (4) creating a binary feature 'is_fatal' (1 if Severity='Fatal', else 0). Save the cleaned dataset as 'nsw_crashes_cleaned.csv'. Provide a summary report: original vs cleaned row count, columns with missing values before/after, and distribution of the new 'is_fatal' feature._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-14.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Anomaly Detection Pipeline
  _Build a Python + SQL pipeline using Australian Bureau of Meteorology weather observations data. Step 1 (Python): Load the CSV, clean temperature and rainfall columns, calculate monthly rolling averages using pandas, and export to a local SQLite database. Step 2 (SQL): Query the database to identify temperature anomalies—define anomalies as months where temperature deviates more than 2 standard deviations from the 10-year mean for that month/location. Use window functions (AVG, STDDEV_POP) in a CTE. Step 3: Return results with location, month, actual_temp, mean_temp, stddev, and anomaly_flag. Export results back to CSV. Deliverables: cleaned CSV, SQLite database schema, SQL query file, and final anomaly results CSV._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-04-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
