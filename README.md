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
| 📅 Last Sync | 2026-05-10 11:47 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate 30-day moving average and identify stocks where the closing price has risen for 5+ consecutive trading days. Use ROW_NUMBER() and LAG() to detect consecutive gains. Return stock ticker, date, closing price, 30-day MA, and consecutive gain streak count. Filter for streaks of 5+ days only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data. Write a Python script using pandas to: (1) handle missing values in crash severity and location columns (impute or drop as appropriate); (2) standardise datetime formats; (3) extract hour of day and day of week from crash timestamp; (4) create a severity category column (map numeric codes to 'Fatal', 'Serious Injury', 'Other Injury', 'Non-Injury'); (5) remove duplicate records based on crash ID and timestamp; (6) export cleaned dataset to CSV. Document all transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-10.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using Bureau of Meteorology temperature and rainfall observations dataset: (1) Load CSV data with pandas, clean missing values and outliers using IQR method; (2) Calculate monthly mean temperature and total rainfall by station; (3) Load cleaned data into SQLite database with station metadata; (4) Write SQL query using CTEs to identify stations where current month's temperature is >2 standard deviations above the 10-year historical average; (5) Return station name, location (state), current month temp, historical mean, and anomaly magnitude. Document the entire workflow from raw CSV to final anomaly report._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle jsphyg collection)`
  📁 Submit as: `quest3_2026-05-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
