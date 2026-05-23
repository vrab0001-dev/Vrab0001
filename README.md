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
| 📅 Last Sync | 2026-05-23 11:53 AEDT |

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
  _Using NSW Road Crash Data, write a query that ranks each crash by severity (injury count) within each Local Government Area (LGA) per month. Use ROW_NUMBER() to identify the top 3 most severe crashes per LGA per month. Then use LAG() to compare each crash's severity to the previous crash in that LGA (ordered by date). Finally, create a CTE that calculates the 3-month rolling average of total injuries per LGA. Output: LGA, Month, Crash_Rank, Severity_vs_Previous_Crash, Rolling_Avg_Injuries. Expected outcome: identify crash hotspots and trends within your state._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest1_2026-05-23.sql`
- [ ] 🐍 **Python Quest:** AIHW Health Expenditure Data Cleaning & Aggregation
  _Download or load the AIHW health expenditure dataset (by state and service type). The data likely contains missing values, inconsistent formatting, and duplicate records. Task: (1) Clean the data by handling nulls, standardising state names to title case, converting expenditure columns to numeric type; (2) Remove duplicate rows; (3) Use pandas to aggregate total expenditure by state and service type; (4) Calculate year-over-year percentage change for each service type; (5) Export the cleaned and aggregated dataset to a new CSV file with clear column names. Expected output: a production-ready CSV with 6-8 columns including State, Service_Type, Total_Expenditure, YoY_Percent_Change._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest2_2026-05-23.py`
- [ ] ⚡ **Combined Quest:** AFL Match Performance Pipeline: Extract, Clean, Analyse
  _End-to-end task: (1) Load AFL match results dataset (Kaggle or afltables.com). (2) Use Python/pandas to clean the data: standardise team names, convert scores to numeric, handle any missing date fields, create a new column 'margin' (points difference). (3) Export the cleaned data to a CSV. (4) Load the cleaned CSV into a SQL database or query it directly. (5) Write a SQL query using window functions to: calculate cumulative wins per team across seasons, rank teams by win percentage in each season, and use LAG to identify consecutive losses for each team. (6) Output: Team, Season, Wins, Win_Percentage, Season_Rank, Consecutive_Losses. Expected outcome: a dataset ready for sports analytics dashboards._
  📦 Dataset: `AFL Match Results — Kaggle or afltables.com`
  📁 Submit as: `quest3_2026-05-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
