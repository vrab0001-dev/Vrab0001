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
| 📅 Last Sync | 2026-10-24 13:16 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their year-to-date percentage gain. Calculate: (1) ROW_NUMBER() to rank stocks by YTD return, (2) LAG() to find the previous month's closing price for each stock, (3) a CTE to pre-calculate monthly returns, and (4) RANK() to handle ties. Filter for stocks in the Technology sector only. Output should show: stock_code, company_name, ytd_return_percent, previous_month_close, rank_by_ytd_return, and row_number. Order by rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-24.sql`
- [ ] 🐍 **Python Quest:** Clean and Transform NSW Road Crash Data for Analysis
  _Download the NSW Road Crash Data (CSV format) from data.nsw.gov.au. Write a Python/pandas script to: (1) load the dataset and identify missing values using isna() and describe(), (2) handle null values in the 'Crash Year', 'Severity', and 'Local Government Area' columns (use forward fill for time-series or drop as appropriate), (3) create a new column 'crash_hour_category' that bins the 'Crash Hour' into periods (night: 22-05, morning: 06-11, afternoon: 12-17, evening: 18-21), (4) standardise text columns (trim whitespace, convert to lowercase), and (5) export the cleaned dataset to a new CSV file. Print a summary report showing row counts before/after cleaning and the distribution of crash_hour_category._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-24.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends: SQL Analysis + Python Automation
  _You have access to Australian Weather Observations from the Bureau of Meteorology (available on Kaggle). Task: (1) In Python, load the weather CSV, clean temperature and rainfall columns (handle outliers using IQR method, remove rows with temp > 60°C or < -50°C), group by month and state, and calculate mean_temp, max_temp, total_rainfall. Export to a staging CSV. (2) Load the cleaned data into SQLite (or your SQL database). (3) Write a SQL query using CTEs and window functions to: identify the month with the highest average temperature for each state, calculate a 3-month rolling average of rainfall for Victoria, and rank all state-months by temperature anomaly (actual temp minus state's historical average). (4) Export the final query results to CSV. Expected output: state, month, mean_temp, rolling_avg_rainfall, temp_anomaly, rank_by_anomaly._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
