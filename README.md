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
| 📅 Last Sync | 2026-08-05 11:22 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum Ranking
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their 7-day price momentum. Calculate the percentage change from 7 days ago using LAG(), then rank companies within each date partition by momentum (descending). Include columns: company_code, date, close_price, price_7_days_ago, momentum_pct, momentum_rank. Filter for the last 30 days of data and return top 10 performers. Use a CTE to calculate momentum first, then rank in the main query._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-05.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download the NSW Road Crash Data from data.nsw.gov.au and use pandas to: (1) Load the CSV and identify missing values by column; (2) Clean the data by removing rows where critical fields (crash_date, severity, location) are null; (3) Standardise the severity column (convert to uppercase and strip whitespace); (4) Create a new column crash_month from crash_date; (5) Aggregate crashes by crash_month and severity, counting incidents; (6) Export a cleaned summary CSV showing monthly crash counts by severity level. Expected output: a cleaned CSV with at least 12 rows (one per month) and 3 columns (month, severity, count)._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-05.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Peak Hour Analysis Pipeline
  _Build an end-to-end pipeline: (1) Use Python/pandas to load Melbourne pedestrian counting data from Melbourne Open Data Portal; (2) Parse the timestamp column and extract hour and day_of_week; (3) Clean any null sensor_id or count values; (4) Export cleaned data to a CSV file; (5) Load this CSV into SQLite or your local database; (6) Write SQL to find the top 5 sensors by average pedestrian count during peak hours (8–9am and 5–6pm) on weekdays only; (7) Include columns: sensor_id, sensor_name, peak_hour, avg_count, day_of_week. Return results sorted by avg_count descending. Document both the Python and SQL scripts._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-08-05.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
