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
| 📅 Last Sync | 2026-08-18 10:31 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility Analysis with Window Functions
  _Using ASX 200 historical stock price data, calculate the 30-day rolling standard deviation of daily returns for each stock symbol. Use window functions (specifically PARTITION BY and ORDER BY with a frame clause) to compute this efficiently. Then rank stocks by their volatility (highest first) and show the top 10 most volatile stocks along with their average closing price over the entire dataset. Use a CTE to first calculate daily returns, then apply window functions in the main query._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (contains crash records with multiple attributes like date, location, severity, vehicle type). Write a Python script using pandas to: (1) handle missing values in the 'Severity' and 'Speed Zone' columns, (2) standardise date formats, (3) remove duplicate records based on crash ID, (4) create a new column 'Hour_of_Day' extracted from the crash time, (5) filter crashes from the last 5 years only, (6) export the cleaned dataset to a new CSV file. Include data quality checks before and after cleaning (row counts, null counts, data types)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-18.py`
- [ ] ⚡ **Combined Quest:** Australian Weather & Agriculture Yield Correlation Study
  _Combine Bureau of Meteorology weather observation data with ABARES crop production data. Write a Python script to: (1) load and clean both CSV files, (2) aggregate monthly rainfall and temperature by Australian state, (3) aggregate crop yield data by state and crop type, (4) merge the datasets on state and month/year. Then write SQL queries to: (1) calculate the correlation between total monthly rainfall and wheat yield by state using a window function approach, (2) identify which state-crop combination shows the strongest positive relationship with temperature using a CTE and analytical functions, (3) rank states by average yield-to-rainfall ratio. Export final results to CSV and summarise key findings in a text file._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle; ABARES Crop Production Data — agriculture.gov.au`
  📁 Submit as: `quest3_2026-08-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
