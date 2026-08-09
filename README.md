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
| 📅 Last Sync | 2026-08-09 10:46 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns Volatility Analysis
  _Using ASX 200 historical price data, calculate the daily percentage return for each stock, then use a window function (ROW_NUMBER and LAG) to compute the 30-day rolling standard deviation of returns for the top 10 most volatile stocks. Include a CTE to first identify stocks with price data spanning at least 200 days. Output should show: stock_code, trading_date, daily_return, rolling_volatility_30d, volatility_rank. Order by trading_date DESC and volatility_rank ASC. Challenge: use PARTITION BY to isolate calculations per stock, and handle NULL values from LAG appropriately._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Severity Mapping
  _Download NSW Road Crash Data (CSV format). Your task: (1) Load the dataset and identify missing values across all columns; (2) Create a data cleaning function that removes rows where critical fields (crash_date, location, injury_severity) are NULL; (3) Standardise location names to title case and remove leading/trailing whitespace; (4) Create a new column 'severity_category' that maps injury severity codes to human-readable labels (e.g., 'Fatal', 'Serious Injury', 'Minor Injury', 'Non-Injury'); (5) Export the cleaned dataset to a new CSV file with timestamp in filename. Use pandas and include a summary report showing: original row count, cleaned row count, rows removed, and value counts for severity_category._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-09.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Count Trend Analysis Pipeline
  _Build a Python script that: (1) loads Melbourne pedestrian counting sensor data (CSV); (2) uses pandas to resample hourly counts to daily totals and compute a 7-day rolling average; (3) identifies the top 5 sensor locations by total pedestrian volume; (4) exports cleaned data to CSV. Then, create a SQL query that: (5) imports the cleaned CSV into a temporary table; (6) uses window functions (ROW_NUMBER, LAG, LEAD) to identify consecutive days where a sensor's count dropped >30% from the previous day (potential sensor malfunction); (7) generates a report showing: sensor_id, location, date, daily_count, previous_day_count, pct_change, anomaly_flag. Combine both scripts in one Python file where SQL runs on the processed data. Expected output: anomaly report CSV and a summary of suspicious sensor days._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-08-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
