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
| 📅 Last Sync | 2026-04-05 11:17 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Performance Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate: (1) the 30-day rolling average price for each stock, (2) the rank of stocks by daily percentage change within each date, and (3) the cumulative return from the first trading day to each subsequent day per stock. Use ROW_NUMBER() and LAG() to identify stocks that hit new 52-week highs on any given date. Return the top 10 stocks by cumulative return over the dataset period, ordered by date and stock symbol._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Standardisation
  _Download NSW Road Crash Data (contains crash location, vehicle details, injury severity, dates). Write a Python/pandas script to: (1) handle missing values in crash_type and injury_severity columns (document your strategy), (2) standardise location data (remove whitespace, convert to title case, validate suburb names against a reference list if available), (3) parse date columns and extract year/month/day/day_of_week, (4) create a new feature: crash_density_score based on frequency of crashes per suburb, (5) export cleaned data to CSV. Include data validation checks and a summary report showing rows dropped and data quality metrics._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-05.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using Australian Weather observations dataset (Bureau of Meteorology on Kaggle), build an end-to-end pipeline: (1) Use Python/pandas to load weather data (temperature, rainfall, humidity), clean missing values, and calculate monthly aggregates (mean temp, total rainfall, mean humidity) by station and month. (2) Export cleaned aggregates to a CSV. (3) Load into SQL and create a CTE-based query that identifies weather anomalies: stations where monthly temperature was >2 standard deviations from the 10-year historical mean for that month, or rainfall was <10th percentile. (4) Rank anomaly severity using window functions (RANK() by magnitude of deviation). Return the top 20 anomalies with station name, date, observed value, expected range, and anomaly rank. Document any data quality issues encountered._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg dataset)`
  📁 Submit as: `quest3_2026-04-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
