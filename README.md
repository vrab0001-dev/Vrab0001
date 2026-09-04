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
| 📅 Last Sync | 2026-09-04 11:43 AEDT |

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
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify momentum shifts for each stock. Write a query using window functions (ROW_NUMBER, LAG, AVG OVER) to: (1) rank stocks by the largest positive price change in the last 30 days, (2) calculate the 20-day moving average for each stock's closing price, (3) identify the first day each stock crossed above its 20-day MA. Return stock symbol, date, closing price, 20-day MA, and momentum rank. Use a CTE to isolate the last 90 days of data before processing._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-09-04.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download NSW Road Crash Data (from NSW Open Data) in CSV format. Write a Python/pandas script to: (1) load the dataset and handle missing values (document your strategy for each column), (2) standardise datetime columns to ISO 8601 format, (3) extract features: hour of day, day of week, and crash severity category from available columns, (4) remove duplicate records based on crash ID, (5) create a CSV output with cleaned data and a summary report showing row counts before/after, missing value percentages by column, and unique values in categorical columns. Ensure your script is reproducible and includes comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-04.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production: Extract, Clean, and Analytical Query
  _Create an end-to-end data pipeline: (1) source Australian wine production statistics (by region and year) from Wine Australia data or Kaggle, (2) write a Python script using pandas to load, clean (handle missing regions/years, standardise column names, convert volumes to consistent units), and export to a SQLite database with appropriate schema (tables: regions, vintages, production_volumes), (3) write SQL queries to find: the top 3 wine-producing regions by total volume (all time), regions with year-over-year production growth in the last 5 years, and a ranked list of regions by average production per vintage. Output: cleaned CSV, SQLite .db file, and a SQL script with all three analytical queries._
  📦 Dataset: `Australian wine production statistics — Wine Australia or Kaggle`
  📁 Submit as: `quest3_2026-09-04.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
