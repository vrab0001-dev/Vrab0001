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
| 📅 Last Sync | 2026-04-30 11:49 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 20-day price momentum for each stock. Create a query that: (1) uses ROW_NUMBER() to rank stocks by momentum within each trading week; (2) uses LAG() to compare current close price with price 20 days ago; (3) filters for only the top 10 momentum gainers in the most recent trading week; (4) returns stock symbol, current price, 20-day return percentage, and ranking. Order by momentum descending. This tests your understanding of window functions and time-series analysis._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-04-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data (contains crash reports with timestamps, locations, severity, vehicle types). Write a Python script using pandas to: (1) load the CSV and inspect for missing values, duplicates, and data type mismatches; (2) clean datetime columns and extract hour-of-day and day-of-week features; (3) standardise location names (remove whitespace, convert to title case); (4) create a severity category column (convert numeric codes to 'Fatal', 'Serious Injury', 'Other Injury', 'Non-Injury'); (5) export the cleaned dataset to a new CSV. Document any data quality issues found. Expected output: cleaned CSV with 8+ columns including engineered features._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-30.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Analysis: Trend Detection Pipeline
  _Build an end-to-end data engineering workflow: (1) Download AIHW health expenditure data (annual spending by state and service type); (2) Use Python/pandas to load, clean, and reshape the data into a tall format (state, year, service_type, expenditure); (3) Load the cleaned data into a SQL database (SQLite is fine); (4) Write a SQL query with CTEs to: calculate year-on-year expenditure change by state and service type, rank states by growth rate, identify the top 3 fastest-growing service categories nationally. (5) Export results showing state, service_type, expenditure_2024, expenditure_2023, growth_percentage, and growth_rank. Document your data pipeline steps in comments._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-04-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
