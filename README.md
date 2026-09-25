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
| 📅 Last Sync | 2026-09-25 12:13 AEDT |

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
  _Using ASX 200 historical price data, calculate a 20-day rolling average price and identify momentum shifts. For each stock, use ROW_NUMBER() to rank trading days, LAG() to compare current close price against the previous day, and a CTE to filter only days where price momentum changed direction (from gaining to losing or vice versa). Return stock symbol, date, close price, 20-day rolling average, and momentum direction. Order by stock and date. This tests your understanding of window functions, CTEs, and complex analytical queries._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-09-25.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Severity Classification
  _Download NSW Road Crash Data (injury data). Write a pandas script that: (1) loads the CSV and inspects for missing values, duplicates, and data type inconsistencies, (2) handles missing severity classifications by imputing based on casualty count logic, (3) standardises location names by removing extra whitespace and converting to title case, (4) creates a new 'severity_category' column using pd.cut() to bin crash severity into Low/Medium/High based on injury count, (5) exports a cleaned CSV. Document your data quality issues found and decisions made in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-25.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Trends Pipeline: SQL + Python
  _Build a mini data pipeline: (1) Download Australian Weather observations data (Bureau of Meteorology from Kaggle). (2) Use Python/pandas to load the CSV, clean temperature and rainfall columns (remove outliers beyond 3 standard deviations), and export to a local SQLite database. (3) Write SQL queries to calculate: monthly average max temperature, total rainfall per location, and identify the top 5 hottest days across all locations. (4) Use a CTE to rank locations by average annual temperature and RANK() to show ties. (5) Export results back to CSV. This tests end-to-end data engineering: ingestion, cleaning, storage, querying, and export._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology (Kaggle)`
  📁 Submit as: `quest3_2026-09-25.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
