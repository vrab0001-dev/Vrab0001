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
| 📅 Last Sync | 2026-07-02 12:02 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Monthly Performance Ranking with Window Functions
  _Using ASX 200 historical stock price data, write a SQL query with window functions to: (1) Calculate the monthly percentage change for each stock (closing price end of month vs start of month), (2) Rank stocks by performance within each month using RANK() or ROW_NUMBER(), (3) Identify the top 5 and bottom 5 performers each month, (4) Use a CTE to calculate the 3-month rolling average of monthly returns for the top 10 stocks. Output should show stock symbol, month, percentage change, rank within month, and 3-month rolling average. Expected output: 15-20 rows per month showing ranked stocks with rolling metrics._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-02.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning and Seasonal Aggregation
  _Download or load Australian Bureau of Meteorology weather observations data (daily temperature, rainfall, humidity for multiple cities). Create a Python/pandas script to: (1) Clean the data by handling missing values, outliers, and data type conversions, (2) Extract date components and assign seasons (winter/spring/summer/autumn based on Southern Hemisphere), (3) Group by city and season to calculate mean temperature, total rainfall, and humidity statistics, (4) Identify anomalous days (temperature > 2 standard deviations from seasonal mean), (5) Export cleaned data to a new CSV with a data quality report (% missing, % outliers removed). Expected output: cleaned CSV with seasonal metrics and a summary text file showing data quality statistics._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg collection)`
  📁 Submit as: `quest2_2026-07-02.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: Data Pipeline with Python ETL and SQL Analytics
  _Build a complete data engineering pipeline using NSW Road Crash Data: (1) Use Python/pandas to extract, clean, and validate crash records (handle missing values in crash type, location, injury severity), standardise location coordinates, and remove duplicates, (2) Load the cleaned data into a SQLite or PostgreSQL database with appropriate schema (crashes table with crash_id, date, location, severity, vehicle_count, etc.), (3) Write SQL queries to answer: What are the top 10 crash hotspots (by coordinate clustering)? What is the monthly trend in crash severity over the past 2 years? Which day of week has the highest crash frequency? Which crash types result in the most injuries? (4) Use a SQL CTE to calculate a 'risk score' for each location based on frequency and severity, (5) Export the top 20 high-risk locations back to Python as a CSV. Expected output: populated database, 4 analytical query results, risk score CSV with location details and rankings._
  📦 Dataset: `NSW Road Crash Data — NSW Open Data Portal (data.nsw.gov.au)`
  📁 Submit as: `quest3_2026-07-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
