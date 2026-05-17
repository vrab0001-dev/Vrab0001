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
| 📅 Last Sync | 2026-05-17 11:53 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using ASX 200 historical price data, calculate the 5-day and 20-day moving averages for each stock using window functions. Then identify stocks where the 5-day MA crossed above the 20-day MA (bullish signal). Use ROW_NUMBER() to rank stocks by percentage gain over the last 30 days within each sector. Return the top 10 stocks with the most recent crossover date, including: stock symbol, sector, current price, 5-day MA, 20-day MA, crossover date, and 30-day gain rank. Use a CTE to structure the moving averages, then another CTE to identify crossovers._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data from data.nsw.gov.au. Clean the dataset by: (1) handling missing values in crash severity, location, and weather columns; (2) standardizing date formats to YYYY-MM-DD; (3) removing duplicate crash records based on crash ID and timestamp; (4) converting coordinates to float and filtering invalid GPS data (lat outside -43.6 to -10.6, lon outside 113 to 154); (5) creating new features: hour_of_day (from time), day_of_week (from date), and severity_category (grouping severity levels). Export the cleaned dataset to a CSV file with all transformations applied. Document any rows removed and reasons why._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-17.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Dashboard Pipeline
  _Create an end-to-end pipeline: (1) In Python, load the Australian Wildfire dataset (Kaggle) and clean it by removing rows with missing fire size, date, or location. Create features: month, season (based on hemisphere), fire_size_category (Small/Medium/Large/Extreme based on hectares burned). (2) Export cleaned data to a CSV. (3) In SQL, load the CSV into a temp table. Use window functions to: calculate monthly fire count and total hectares burned per state/territory, rank months by severity (RANK() OVER), and identify the month with highest fire risk per state using ROW_NUMBER(). (4) Write a query that uses a CTE to find the top 5 most dangerous month-state combinations historically, including: state, month, avg_fires, total_hectares_burned, and danger_rank. Return results ordered by danger rank._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-05-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
