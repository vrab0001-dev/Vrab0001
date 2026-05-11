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
| 📅 Last Sync | 2026-05-11 11:55 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates for each stock: (1) the 30-day moving average of closing price using a window function, (2) the rank of each stock by percentage gain over the last 90 days, and (3) identify which stocks are in the top 10% performers. Use a CTE to first calculate the percentage gains, then apply ROW_NUMBER() and RANK() window functions to rank stocks within each sector. Return stock symbol, current price, 30-day moving average, 90-day gain %, and performance rank. Expected output: 20-50 rows showing ranked stocks with their moving averages._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Feature Engineering
  _Download the NSW Road Crash Data (available on data.nsw.gov.au). Write a Python script using pandas that: (1) loads the CSV and identifies missing values, data type inconsistencies, and duplicate records; (2) cleans datetime columns and standardises location data; (3) creates new features such as 'crash_severity_score' (combining injury type and number of vehicles), 'time_of_day_category' (morning/afternoon/night/early_morning), and 'weather_impact_flag' (1 if weather was a contributing factor, 0 otherwise); (4) exports the cleaned dataset to a new CSV file. Document your data quality findings in comments. Expected output: cleaned CSV with 5+ new feature columns and a summary of records removed/fixed._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-11.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: SQL Analysis + Python Export
  _Create a data pipeline combining Python and SQL: (1) Using Python, download and parse the Australian wine production statistics dataset (Wine Australia). Clean the data to standardise region names, vintage years, and production volumes. (2) Load the cleaned data into a local SQLite database using pandas `to_sql()`. (3) Write SQL queries to: calculate total production volume by wine region and vintage using GROUP BY with HAVING clause to filter regions producing >1M litres, rank regions by production using ROW_NUMBER(), and identify year-on-year production trends using LAG() window function. (4) Use Python to fetch query results and generate a summary report (CSV) showing top 5 regions, production trends, and growth rates. Expected output: cleaned SQLite database + CSV report with regional rankings and 5-year production trends for top wine regions._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia`
  📁 Submit as: `quest3_2026-05-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
