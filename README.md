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
| 📅 Last Sync | 2026-09-12 11:53 AEDT |

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
  _Using the ASX 200 historical prices dataset, calculate a 30-day rolling average price for each stock, then rank stocks by their current price relative to their 30-day average (momentum score). Use window functions ROW_NUMBER() and LAG() to identify the top 10 momentum gainers and the bottom 10 momentum losers as of the most recent trading date. Expected output: a ranked table showing stock symbol, current price, 30-day average, momentum percentage, and rank within gainers/losers categories._
  📦 Dataset: `ASX 200 Historical Stock Data — Kaggle`
  📁 Submit as: `quest1_2026-09-12.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download the NSW Road Crash Data (includes crash details, injuries, locations, dates). Load the CSV into pandas and perform the following: (1) handle missing values in severity and crash type columns using appropriate imputation, (2) extract hour of day and day of week from crash datetime, (3) create a severity risk score (0-10) based on injury count and severity level, (4) filter for crashes in Sydney LGAs only, (5) export the cleaned dataset to a new CSV with meaningful column names. Expected output: a cleaned CSV with 5+ new features and documented data quality improvements._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-12.py`
- [ ] ⚡ **Python + SQL Quest:** Weather Analysis Pipeline: Load, Clean, and Query
  _Build a data engineering pipeline: (1) use Python/pandas to download or load Australian weather observations (Bureau of Meteorology dataset), clean temperature, rainfall, and humidity columns (handle outliers, nulls, unit conversions), and load the data into a local SQLite database; (2) write a SQL query that calculates the average temperature and total rainfall by month and location for the past 12 months, and identifies which locations experienced the most extreme temperature variance; (3) export results to CSV. Expected output: a populated SQLite database, a working Python script with error handling, and a results CSV showing monthly aggregations ranked by temperature variance._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-09-12.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
