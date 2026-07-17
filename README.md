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
| 📅 Last Sync | 2026-07-17 11:25 AEDT |

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
  _Using the ASX 200 historical prices dataset, calculate the 20-day moving average and 50-day moving average for the top 5 most traded stocks. Use window functions (AVG() OVER) to compute these rolling averages. Then identify stocks where the 20-day MA crossed above the 50-day MA in the last 30 days of your dataset. Return the stock symbol, date of crossover, closing price, and both moving average values. Order by date descending._
  📦 Dataset: `ASX 200 Historical Stock Data — Kaggle`
  📁 Submit as: `quest1_2026-07-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Incident Severity Pipeline
  _Download the NSW Road Crash Data from data.nsw.gov.au. The dataset contains messy crash records with missing values, inconsistent date formats, and categorical fields. Write a Python script using pandas to: (1) standardise date columns to ISO format, (2) fill missing speed limits with the median for each road type, (3) create a new 'severity_category' column by binning injury counts into 'Minor' (1-2), 'Moderate' (3-5), and 'Severe' (6+), (4) remove duplicate records based on crash ID and timestamp, and (5) export the cleaned dataset as a CSV. Print summary statistics (row count before/after, missing values by column) before and after cleaning._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-17.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL: Extract, Clean, Analyse
  _Retrieve Australian wine production statistics data (by region and vintage year). Using Python, load the raw CSV, clean it (handle missing regions, standardise vintage formats, remove invalid production volumes), and insert the cleaned records into a SQLite database with a schema: wines(id, region, vintage, production_volume_litres, wine_type, quality_rating). Then write a SQL query using CTEs and window functions to: (1) rank regions by total production volume, (2) calculate year-over-year growth in production for each region, (3) identify the vintage year with highest average quality rating per region. Return region, vintage, production_volume, yoy_growth_percent, and region_rank. Save both the cleaned CSV and the SQL results to separate output files._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia or Kaggle`
  📁 Submit as: `quest3_2026-07-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
