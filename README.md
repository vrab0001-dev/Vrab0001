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
| 📅 Last Sync | 2026-05-31 12:08 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a query that calculates the 30-day price momentum for each stock. Use window functions (ROW_NUMBER, LAG) to find the price 30 days ago, compute the percentage change, and rank stocks by momentum within each date partition. Return the top 10 momentum gainers for the most recent trading date in your dataset. Include stock symbol, current price, price 30 days ago, momentum percentage, and momentum rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-31.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Normalisation
  _Download the NSW Road Crash Data and clean it for analysis. Tasks: (1) Handle missing values in severity, crash type, and location columns using appropriate strategies (deletion, imputation, or flags). (2) Standardise date/time formats and extract year, month, day of week features. (3) Normalise location names (postcodes, suburbs) to remove duplicates caused by typos or inconsistent casing. (4) Create a summary CSV showing crash counts by severity and day of week. Output: cleaned dataset (CSV) and a data quality report (txt) documenting all transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-31.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build an end-to-end pipeline using Australian Weather observations data. (1) Use Python/pandas to load weather data (temperature, rainfall, wind speed) and resample to monthly aggregates by station. (2) Detect anomalies: calculate z-scores for each variable and flag months where abs(z-score) > 2.5. Export flagged anomalies to CSV. (3) Load the anomaly CSV into SQL and write a query using CTEs to rank stations by frequency of anomalies in the past 5 years, identify the top 5 most anomalous stations, and count anomalies by month across all stations. Return: Python script, anomaly CSV file, and SQL query with results showing station rankings and monthly anomaly trends._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-05-31.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
