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
| 📅 Last Sync | 2026-09-18 11:54 AEDT |

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
- [ ] 🗄️ **SQL Quest:** NSW Road Crash Severity Trends with Window Functions
  _Using NSW Road Crash Data, write a query that ranks crashes by severity (injury count) within each Local Government Area (LGA) and month. Calculate a 3-month rolling average of crash counts per LGA using window functions (ROW_NUMBER, RANK, LAG). Identify the top 5 LGAs with the highest average crash severity over the last 12 months. Output should include: LGA name, month, crash count, severity rank within LGA, 3-month rolling average, and overall rank across all LGAs._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest1_2026-09-18.sql`
- [ ] 🐍 **Python Quest:** AIHW Health Expenditure Data Cleaning & Pivot Pipeline
  _Download or load AIHW health expenditure dataset (CSV format). Your task: (1) Clean the dataset by handling missing values, standardising state name abbreviations to full names, and removing duplicates. (2) Convert expenditure columns from string format (with currency symbols and commas) to numeric. (3) Transform the data from long to wide format, pivoting by health service category (e.g., hospitals, primary care, mental health) as columns and states as rows. (4) Calculate year-on-year percentage growth for each state and service category. Export the cleaned and pivoted dataset to a new CSV file with meaningful headers._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest2_2026-09-18.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring: ETL Pipeline with SQL Analytics
  _Build an end-to-end data engineering pipeline: (1) Using Python/pandas, load Great Barrier Reef monitoring data (coral bleaching observations, temperature readings, site coordinates). Clean the data: parse dates, validate coordinate ranges (Australia only), handle missing depth/temperature values by interpolation, and standardise reef site names. (2) Create a SQLite database with normalized tables: sites (reef_id, site_name, location, region), observations (observation_id, reef_id, date, bleaching_severity, water_temp), and measurements (measurement_id, observation_id, metric_type, value). (3) Write SQL queries to: (a) Find the top 5 reefs with highest average bleaching severity in the last 12 months; (b) Calculate monthly average water temperature per region; (c) Identify reefs where temperature exceeded 30°C and correlate with bleaching events using a window function (LAG to compare consecutive months). Output: cleaned CSV, normalized SQLite database, and a results CSV with the 3 query outputs._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-09-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
