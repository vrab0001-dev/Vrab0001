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
| 📅 Last Sync | 2026-06-02 12:29 AEDT |

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
  _Using the ASX 200 historical prices dataset, calculate a 20-day rolling average price for each stock symbol. Then rank stocks within each trading week by their price momentum (current price minus 20-day rolling average), using ROW_NUMBER() to identify the top 3 momentum gainers each week. Include columns: symbol, trading_date, close_price, rolling_avg_20d, momentum, weekly_rank. Filter for the last 12 weeks of data and order by trading_date descending, then weekly_rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-02.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation
  _Download the NSW Road Crash Data (from data.nsw.gov.au). The dataset contains multiple crash records with missing values, inconsistent date formats, and categorical variables. Write a pandas script to: (1) clean date columns and convert to datetime; (2) handle missing values in 'crash_severity' and 'crash_type' by filling with 'Unknown'; (3) standardise location names to title case; (4) create a summary CSV showing total crashes, injuries, and fatalities by Local Government Area (LGA) for the last 2 years of available data; (5) export the cleaned summary to 'nsw_crashes_summary.csv'. Include error handling for file I/O._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-02.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: ETL and Analytical Query
  _Part A (Python): Download Australian Bureau of Meteorology weather observations (available on Kaggle via jsphyg). Write a pandas script to: extract data for 3 major Australian cities (Sydney, Melbourne, Brisbane), clean temperature and rainfall columns (handle missing values), and load the cleaned data into a SQLite database with a table named 'weather_observations' (columns: city, observation_date, max_temp_c, min_temp_c, rainfall_mm). Part B (SQL): Write a CTE-based query to find for each city: the average max temperature per month, the month with highest rainfall, and a running 7-day average of rainfall. Use window functions (AVG() OVER) to calculate the running average. Output: city, month, avg_max_temp, rainfall_total, rainfall_7day_avg, ranking of wettest months by city using RANK()._
  📦 Dataset: `Australian Weather Observations — Kaggle (jsphyg) and Bureau of Meteorology`
  📁 Submit as: `quest3_2026-06-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
