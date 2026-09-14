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
| 📅 Last Sync | 2026-09-14 12:03 AEDT |

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
  _Using ASX 200 historical prices dataset, calculate the 20-day moving average, daily percentage change, and rank stocks by momentum (highest positive change in last 5 days). Create a CTE for daily returns, then use ROW_NUMBER() and LAG() window functions to identify the top 10 stocks with the strongest upward momentum. Output should include stock symbol, current price, 20-day moving average, momentum rank, and the date range analysed._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-14.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Enrichment Pipeline
  _Download NSW Road Crash Data from data.nsw.gov.au. Clean the dataset by handling missing values in crash severity, weather conditions, and road type columns. Standardise date formats, categorise crash severity into bins (Minor, Moderate, Severe, Fatal), and create a new feature: crash density per LGA (Local Government Area). Export the cleaned dataset to CSV and provide summary statistics showing crashes by severity, top 5 LGAs by crash count, and temporal patterns (crashes by day of week and hour)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-14.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Incident Risk Assessment Pipeline
  _Build an end-to-end pipeline: (1) Load Australian Wildfire dataset from Kaggle containing fire incidents, latitude, longitude, fire size, and dates. (2) Use Python/pandas to clean data, handle missing coordinates, and aggregate fires by month and state. Create a risk score column (high fires = high risk). (3) Load this cleaned data into a SQL database. (4) Write SQL queries using CTEs and window functions to: identify the top 3 states with increasing fire frequency trend (use LAG to compare month-over-month), calculate 3-month rolling average of fire incidents by state, and rank months by total burned area with cumulative sums. Output a summary report with state-level risk rankings and temporal trends._
  📦 Dataset: `Australian Wildfire Incidents — Kaggle`
  📁 Submit as: `quest3_2026-09-14.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
