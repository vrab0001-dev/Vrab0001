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
| 📅 Last Sync | 2026-06-21 12:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** AFL Momentum: Win Streaks and Form Ranking
  _Using AFL match results data, write a query with window functions to: (1) Calculate a rolling 5-game win/loss streak for each team using ROW_NUMBER and PARTITION BY team, (2) Rank teams by their current form (last 10 games win percentage) using RANK() and CTE, (3) Identify the longest consecutive win streak in the entire dataset using LAG() to detect streak breaks. Return: team name, current streak length, current streak type (W/L), form rank, and all-time longest streak. Order by form rank ascending._
  📦 Dataset: `AFL match results — Kaggle (search: AFL tables Australia)`
  📁 Submit as: `quest1_2026-06-21.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Scoring
  _Download NSW Road Crash Data (2020-2025). Using pandas: (1) Handle missing values in crash severity, vehicle count, and injury columns (document your strategy), (2) Standardise location names (remove extra spaces, fix case inconsistencies), (3) Create a new 'crash_risk_score' column (0-100) based on: severity (40% weight), number of vehicles involved (30%), number of injuries (30%). (4) Group by local government area (LGA) and calculate mean risk score, crash frequency, and injury rate per 1000 crashes. (5) Export cleaned dataset and LGA summary to CSV files. Print the top 5 highest-risk LGAs._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-21.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Using Bureau of Meteorology historical weather observations (or Kaggle equivalent): (1) In Python/pandas: load daily temperature and rainfall data for a single Australian city (e.g. Sydney, Melbourne, Perth) from 2015-2025, handle missing values via forward fill, calculate 30-day rolling mean and standard deviation for temperature. (2) Flag anomalies: any day where temperature is >2 std devs from rolling mean OR rainfall is in top 5% for the month. Export anomaly dataset to CSV. (3) In SQL: load the anomaly CSV, create a query to: count anomalies by year and month, calculate the percentage of anomalous days per month, use a CTE to identify months with >15% anomalies. Return: year, month, anomaly count, anomaly percentage, anomaly_severity (high/medium/low based on percentage thresholds). Output ordered by year DESC, month DESC._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology or Kaggle (search: Australian weather data)`
  📁 Submit as: `quest3_2026-06-21.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
