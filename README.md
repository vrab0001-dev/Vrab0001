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
| 📅 Last Sync | 2026-06-10 12:06 AEDT |

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
  _Using the ASX 200 historical prices dataset, calculate the 30-day price momentum for each stock. Use window functions (ROW_NUMBER, LAG) to: 1) Rank stocks by momentum within each date partition, 2) Calculate the percentage change from 30 days prior using LAG, 3) Identify which stocks are in the top 10 momentum gainers on the most recent date in your dataset. Return stock symbol, date, close price, 30-day momentum percentage, and momentum rank. Order by date DESC and rank ASC._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-06-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Classification
  _Download or load the NSW Road Crash Data from data.nsw.gov.au. Clean the dataset by: 1) Handling missing values in injury severity and crash type columns, 2) Standardising suburb names (uppercase, remove extra whitespace), 3) Converting date columns to datetime format, 4) Creating a new categorical column 'injury_risk_level' that maps injury counts to 'low' (0-1), 'medium' (2-3), 'high' (4+), 5) Removing duplicate records based on crash ID and date. Export the cleaned dataset to a new CSV file with record counts before/after cleaning printed to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-10.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Detection Pipeline
  _Build an end-to-end pipeline using Python and SQL: 1) Use pandas to load Australian Weather observations (Bureau of Meteorology dataset from Kaggle), 2) Clean temperature and rainfall columns, handle missing values, standardise location names, 3) Create a Python script that calculates monthly average temperature and rainfall per location, 4) Load cleaned data into a SQLite database, 5) Write a SQL query using CTEs to identify locations where average temperature in the current month is >2 standard deviations above the 5-year rolling mean, 6) Return location, date, actual temp, rolling mean temp, and deviation in standard deviations. Document each step with comments and save the SQLite database file._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle (jsphyg)`
  📁 Submit as: `quest3_2026-06-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
