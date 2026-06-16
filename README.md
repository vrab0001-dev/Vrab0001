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
| 📅 Last Sync | 2026-06-16 12:35 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking
  _Using ASX 200 historical price data, write a SQL query with window functions to rank stocks by 30-day price momentum. Calculate the percentage change from 30 days ago using LAG(), then use RANK() to rank all stocks by this momentum metric within each date partition. Include the stock symbol, date, closing price, price 30 days ago, momentum percentage, and momentum rank. Filter to only the most recent date in your dataset and order by rank ascending. This tests your understanding of LAG() for time-series analysis and RANK() for competitive ranking._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data from the NSW Open Data portal. Build a Python script using pandas that: (1) loads the CSV and inspects missing values and data types; (2) removes rows where critical columns (crash date, location, injury count) are missing; (3) converts date columns to datetime format; (4) standardizes location names to title case; (5) creates a new column 'hour_of_day' extracted from the time field; (6) removes duplicate rows based on all columns; (7) generates a summary report showing row counts before/after cleaning, missing value percentages, and data type validation. Output the cleaned dataset to a new CSV and print the summary report to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-16.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using Australian Bureau of Meteorology weather observation data (or Kaggle equivalent): (1) Load the CSV in Python and clean it — handle missing temperature values by forward-filling within each station, remove outlier temperatures using IQR method, and ensure date columns are datetime format. (2) Export the cleaned data to a temporary CSV or SQLite database. (3) Write SQL to calculate monthly average temperature and monthly standard deviation for each weather station using window functions (AVG() OVER, STDDEV() OVER). (4) Identify anomalies: months where the average temperature is more than 1.5 standard deviations above or below the historical mean for that station using a CTE. (5) Return station name, month, average temperature, anomaly flag, and deviation magnitude. Use Python to visualize the anomalies (bar chart or heatmap by station and month). This tests end-to-end data pipeline skills combining cleaning, SQL analytics, and visualization._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
