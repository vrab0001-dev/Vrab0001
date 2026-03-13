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
| 📅 Last Sync | 2026-03-13 16:04 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Price Momentum with Window Functions
  _Using ASX 200 historical price data, calculate the daily percentage change for each stock, then use window functions to rank stocks by momentum within each date partition. Specifically: (1) Calculate daily % change using LAG to access previous close price; (2) Use ROW_NUMBER to rank stocks by % change (descending) per trading date; (3) Filter for top 5 and bottom 5 performers per date; (4) Add a 7-day moving average of closing price using ROWS BETWEEN. Output should show Date, Stock Symbol, Close Price, Daily % Change, Daily Rank, and 7-Day MA. Use CTEs to structure the query logically._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-03-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Severity Pipeline
  _Download NSW Road Crash Data (contains crash records with missing values, inconsistent date formats, and categorical noise). Build a data cleaning script that: (1) Loads the CSV and inspects data types, null counts, and unique values; (2) Standardises datetime columns to ISO format; (3) Handles missing values in Severity and Speed Limit columns using forward-fill and mode imputation respectively; (4) Removes duplicate crash records (keep first occurrence); (5) Creates a new column 'Crash_Severity_Category' by binning Severity into 'Minor', 'Moderate', 'Severe' using pd.cut(); (6) Exports cleaned data to a new CSV. Log any rows dropped and show before/after data quality metrics._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-13.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL: Load, Clean, and Query
  _Create an end-to-end ETL pipeline using Python and SQL. Phase 1 (Python): Download Australian wine production statistics (region, vintage year, production volume, wine type). Clean the data by: standardising region names (title case), converting production volumes to numeric (handle 'ML' units), removing outliers using IQR method, and exporting to CSV. Phase 2 (SQL): Load the cleaned CSV into a local SQLite database table 'wine_production'. Write a CTE-based query that: (1) Calculates total production volume by wine type and year; (2) Uses RANK() to rank wine types by production within each year; (3) Calculates year-over-year growth % for each wine type using LAG; (4) Filters for wine types in top 3 globally. Output should include Wine_Type, Year, Total_Volume, Rank, and YoY_Growth. Include both the Python script and SQL query in your submission._
  📦 Dataset: `Australian wine production statistics — wineaustralia.com or Kaggle`
  📁 Submit as: `quest3_2026-03-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
