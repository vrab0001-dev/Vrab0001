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
| 📅 Last Sync | 2026-05-01 11:51 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query that ranks each stock by its percentage gain over the last 90 days within each sector. Use ROW_NUMBER() and LAG() window functions to calculate the price change from 90 days ago to the most recent closing price. Return: stock_code, sector, current_price, price_90_days_ago, percentage_gain, rank_in_sector. Order by sector and rank. This tests your understanding of window functions, date arithmetic, and partitioning._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation
  _Download the NSW Road Crash Data (CSV format) from the NSW open data portal. Write a Python script using pandas to: (1) Handle missing values in the 'Injury Level' column by imputing with the mode per Local Government Area; (2) Standardise the 'Road Type' column by converting to title case and removing leading/trailing whitespace; (3) Create a new column 'crash_severity_score' based on injury level (Fatal=5, Serious injury=4, Other injury=2, Non-injury=1); (4) Export a cleaned CSV and a summary report showing crash counts by Local Government Area and severity score. Ensure your script is reproducible and includes comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-01.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Pipeline: Python ETL + SQL Analytics
  _Build an end-to-end pipeline using Australian Bureau of Meteorology weather observations: (1) Python: Load the weather CSV, clean temperature and rainfall columns (remove outliers beyond 3 standard deviations, handle missing values with linear interpolation), group by station and month, calculate monthly averages, and export to a clean CSV. (2) SQL: Load the cleaned data into a database table. Write a CTE-based query that identifies months where temperature was in the top 10% warmest and rainfall was in the bottom 10% driest (i.e., drought-like conditions) for each station. Return station_name, month, avg_temp, avg_rainfall, and a flag 'anomaly_detected'. (3) Python: Read the SQL results and generate a simple text report listing all anomalies by state. This quest integrates file I/O, data cleaning, window functions, and reporting._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
