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
| 📅 Last Sync | 2026-10-13 15:15 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 20-day moving average and identifies momentum shifts. Use window functions (ROW_NUMBER, LAG, AVG OVER) to rank each company's daily price change percentages within their own partition, then identify the top 10 companies with the strongest upward momentum in the last 30 trading days. Your output should include: company name, current price, 20-day moving average, price change percentage, and momentum rank. Use a CTE to first calculate the moving averages, then apply window functions on top._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download the NSW Road Crash Data (contains crash location, date, severity, vehicle type, weather conditions). Write a Python pandas script that: (1) loads the CSV, (2) handles missing values in the 'Weather' and 'Speed_Zone' columns using forward fill, (3) standardises the 'Severity' column (convert to title case and remove leading/trailing spaces), (4) filters crashes from the last 5 years only, (5) groups by Local Government Area (LGA) and crash severity, counting total crashes per combination, (6) exports a cleaned summary CSV with columns: LGA, Severity, Crash_Count, sorted by LGA ascending then Crash_Count descending. Include data quality checks (row counts before/after filtering) in print statements._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-13.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Trend Analysis End-to-End
  _Build a complete data pipeline using Python and SQL. (1) Using Python and pandas, download or load the Australian wine production dataset by region and vintage year. Clean the data: standardise region names (title case), handle any missing vintage years by forward-filling within each region, remove outlier values (production volumes > 3 standard deviations from the region mean). Export the cleaned data to a CSV. (2) Load this cleaned CSV into a SQL database (SQLite or PostgreSQL). (3) Write a SQL query using window functions and CTEs to: calculate the year-over-year production change percentage for each region, rank regions by growth rate, and identify the top 5 regions with highest average growth over the last 10 years. Your final SQL output should show: Region, Avg_YoY_Growth_Percent, Growth_Rank, and Total_Production_10Yr. Include both the Python script and the SQL query in your submission._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-10-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
