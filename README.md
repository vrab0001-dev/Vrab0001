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
| 📅 Last Sync | 2026-04-27 11:27 AEDT |

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
  _Using ASX 200 historical prices dataset, calculate 20-day and 50-day moving averages for each stock using window functions. Identify stocks where the 20-day MA crossed above the 50-day MA (bullish signal) in the last 30 days. Use a CTE to calculate both moving averages in one pass, then filter for crossover events. Return stock ticker, date of crossover, price at crossover, and the two MA values. Order by date descending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleanup and Feature Engineering
  _Download NSW Road Crash Data from data.nsw.gov.au. Clean the dataset by: (1) removing rows with >40% missing values, (2) standardizing date formats and extracting day of week + hour of day, (3) handling categorical variables (crash type, severity) by filling missing values with mode, (4) removing duplicate crash records based on location + datetime. Create a new feature: 'crash_severity_score' (1-5 scale based on injury count). Export cleaned data to CSV. Document all transformations applied._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-27.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring: Data Pipeline from Download to Insights
  _Download coral bleaching monitoring data from AIMS (Australian Institute of Marine Science). (Python) Clean the dataset: parse observation dates, standardize location coordinates, handle missing bleaching percentages using interpolation by location. Load cleaned data into a local SQLite database with two tables: 'sites' (location metadata) and 'observations' (bleaching records). (SQL) Write a query using window functions (ROW_NUMBER, LAG) to identify the worst bleaching events per site—show the top 5 sites by maximum bleaching percentage, the date of worst event, and month-over-month bleaching change. Return results ordered by severity. Document your pipeline in a short README._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-04-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
