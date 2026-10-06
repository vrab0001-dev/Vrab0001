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
| 📅 Last Sync | 2026-10-06 14:36 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum: ROW_NUMBER & LAG Window Functions
  _Using the ASX 200 historical prices dataset, calculate the daily price momentum for the top 10 most traded stocks. For each stock, use ROW_NUMBER() to rank trading days chronologically, then LAG() to compute the percentage change from the previous day's closing price. Filter for records where the price change exceeds 2% (positive or negative). Return: Stock symbol, trading date, closing price, previous day's close, and percentage change. Order by stock symbol and date. This tests your understanding of window functions and temporal analysis._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-06.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data: Cleaning & Severity Classification
  _Download the NSW Road Crash Data (data.nsw.gov.au). Load the CSV and perform the following data cleaning and transformation tasks: (1) Handle missing values in injury_type and severity columns by filling with 'Unknown'. (2) Standardise all text columns to lowercase. (3) Remove duplicate rows based on crash_id. (4) Create a new column 'severity_score' that assigns numerical scores (1-5) based on the severity category. (5) Extract the month and year from the crash_date column into separate columns. (6) Export the cleaned dataset to a new CSV file. Validate your work by printing row counts before/after cleaning and value_counts() for the new severity_score column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-06.py`
- [ ] ⚡ **Combined Quest:** Bureau of Meteorology Data: Python ETL → SQL Analytics
  _Retrieve Australian weather observations data (Bureau of Meteorology via Kaggle: Australian Weather observations by jsphyg). (1) Using Python/pandas: Load the CSV, clean temperature and rainfall columns (handle missing/outlier values), and create a new feature 'temp_anomaly' that flags days where max_temperature exceeds the station's 90th percentile. Export to a temporary cleaned CSV. (2) Create a SQL database schema with a 'weather_observations' table. Load the cleaned CSV into the database. (3) Write a SQL query using CTEs to: Calculate the rolling 7-day average temperature for each weather station, identify the top 5 stations with the highest anomaly frequency, and return station name, anomaly count, and 7-day avg temp for each. Verify your results by comparing Python and SQL outputs for at least one station._
  📦 Dataset: `Australian Weather Observations — Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-10-06.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
