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
| 📅 Last Sync | 2026-08-26 10:34 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Ranking with Moving Averages
  _Using the ASX 200 historical prices dataset, write a query with window functions to: (1) Calculate a 20-day moving average of closing prices for each stock; (2) Rank stocks by their latest closing price relative to their 20-day moving average (showing which are trading above/below); (3) Use a CTE to identify the top 10 stocks with the largest positive deviation from their moving average in the last trading month. Return stock symbol, latest close, 20-day MA, deviation percentage, and rank. Order by deviation descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-26.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas to: (1) Load the CSV and inspect for missing values, duplicates, and data types; (2) Clean the dataset by handling nulls in crash severity and location columns; (3) Standardise location names (remove extra spaces, convert to title case); (4) Create new features: crash_hour (extracted from time), season (derived from month), and is_fatal (boolean from severity); (5) Filter crashes from 2023 onwards; (6) Export cleaned data to a new CSV. Print summary statistics before/after cleaning (row count, null counts by column)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-26.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection & Storage
  _Use the Australian Weather Observations dataset (Bureau of Meteorology, available via Kaggle as jsphyg's dataset). (1) In Python: Load weather data (temperature, rainfall, humidity for multiple Australian cities). Clean the data by removing outliers (e.g., temperatures >50°C or <-20°C). Calculate rolling 7-day mean temperature and identify days where actual temp deviates >5°C from the rolling mean (anomaly flag). Export cleaned data with anomaly flags to CSV. (2) In SQL: Load the cleaned CSV into a SQLite/PostgreSQL table. Write a query using CTEs and window functions to rank cities by frequency of temperature anomalies in the last 90 days, calculate the percentage of anomalous days per city, and return the top 5 cities with highest anomaly percentage alongside average deviation magnitude._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle by jsphyg)`
  📁 Submit as: `quest3_2026-08-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
