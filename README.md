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
| 📅 Last Sync | 2026-10-25 13:03 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using ASX 200 historical stock price data, calculate a 30-day rolling average price and identify momentum shifts for each stock. Write a query using window functions (AVG() OVER, ROW_NUMBER() OVER) to: (1) compute the 30-day moving average for each stock ordered by date, (2) rank stocks by their price change percentage in the last 7 days, (3) flag stocks where the current price crosses above/below the 30-day MA. Return stock symbol, date, close price, 30-day MA, price change %, and rank. Use a CTE to organize the window function logic cleanly._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data (injury crashes from the past 3 years). Use pandas to: (1) clean the dataset by handling missing values in severity, location, and vehicle type columns, (2) standardize datetime formats for crash dates, (3) create new features: time_of_day (peak vs off-peak hours), crash_type (multi-vehicle vs single), and location_category (urban vs rural based on postal code mapping), (4) remove duplicates and validate data integrity. Export the cleaned dataset to a new CSV file. Document any data quality issues found and your handling decisions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-25.py`
- [ ] ⚡ **Combined Quest:** COVID-19 Vaccination Progress Dashboard Data Pipeline
  _Build a mini ETL pipeline: (1) In Python, fetch and clean the COVID-19 Australia vaccination dataset (handle missing states, date formatting, and vaccination type inconsistencies), (2) load the cleaned data into a local SQLite database with appropriate schema (state, date, vaccine_type, doses_administered, population_eligible), (3) in SQL, write queries to calculate: cumulative vaccination rates by state, weekly dose administration trends using window functions, and states lagging behind the national average. (4) Export final analytical results to CSV. Combine both scripts into a single Python file that orchestrates the entire pipeline with error handling and logging._
  📦 Dataset: `COVID-19 Australia Dataset — Kaggle`
  📁 Submit as: `quest3_2026-10-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
