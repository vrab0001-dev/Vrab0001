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
| 📅 Last Sync | 2026-03-24 12:02 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Rolling Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their 30-day rolling average return. Calculate ROW_NUMBER() partitioned by stock ticker ordered by rolling average return descending. Include columns: ticker, date, closing_price, 30_day_rolling_avg, price_change_pct, and rank_within_period. Filter results to show only the top 10 performing stocks for the most recent date in the dataset. Use a CTE to first calculate the rolling averages, then apply the ranking in a second CTE._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Casualty Analysis
  _Download the NSW Road Crash Data from the NSW open data portal. Load the CSV file using pandas. Identify and handle missing values in casualty count columns. Standardise date formats to YYYY-MM-DD. Remove duplicate records based on crash ID and timestamp. Create a new column 'severity_category' that classifies crashes as 'Fatal' (fatalities > 0), 'Serious' (hospitalised > 0), or 'Minor' (property damage only). Export the cleaned dataset to a new CSV file. Document all data quality issues found and transformations applied in a markdown report._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-24.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using the Australian Bureau of Meteorology weather observations dataset (or jsphyg's Kaggle version): (1) Load historical temperature and rainfall data into a pandas DataFrame. Clean the data by handling missing values and outliers using IQR method. (2) Create a SQLite database and load the cleaned data into a 'weather_observations' table. (3) Write a SQL query using window functions (LAG, LEAD) to calculate daily temperature anomalies compared to a rolling 30-day average. Identify dates where temperature deviated more than 2 standard deviations from the rolling mean. (4) Use Python to query the results, visualise the anomalies in a simple plot (using matplotlib), and export anomalous dates to a CSV for further investigation. Expected output: cleaned CSV, SQLite database, anomaly report CSV, and a line chart showing temperature trends with anomalies highlighted._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-03-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
