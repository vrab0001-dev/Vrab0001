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
| 📅 Last Sync | 2026-04-17 11:21 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 30-day rolling average closing price for each stock using AVG() OVER a window, (2) Rank stocks by their year-to-date percentage gain using RANK() OVER, (3) Use LAG() to find the price change from the previous trading day for each stock, (4) Filter to show only the top 10 stocks by YTD gain and include columns: stock_code, current_price, price_30d_avg, ytd_rank, prev_day_change. Expected output: 10 rows with window function calculations visible._
  📦 Dataset: `ASX 200 Historical Data — Kaggle`
  📁 Submit as: `quest1_2026-04-17.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Aggregation Pipeline
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas to: (1) Load the CSV and inspect for missing values, duplicates, and data type mismatches, (2) Clean the 'crash_date' column and convert to datetime format, (3) Remove rows with missing latitude/longitude coordinates, (4) Create a new column 'severity_category' by binning injury counts into 'Minor', 'Moderate', 'Severe' categories, (5) Aggregate crash counts by local government area (LGA) and severity category, (6) Export a cleaned summary CSV with columns: LGA, severity_category, crash_count, avg_vehicles_involved. Expected output: CSV file with 20+ rows showing crash statistics by region and severity._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-17.py`
- [ ] ⚡ **Combined Quest:** AIHW Health Expenditure Trend Analysis Pipeline
  _Working with AIHW health expenditure data, build a Python + SQL pipeline: (1) In Python, load the health expenditure CSV, validate year columns, and reshape from wide to long format (year, category, expenditure_amount), (2) Clean currency values (remove '$' and commas), convert to numeric, and handle missing data by forward-filling within categories, (3) Export cleaned data to a CSV, (4) Load into SQLite, (5) Write a SQL query with a CTE to calculate year-over-year expenditure growth % by category using LAG() window function, (6) Create a second CTE to identify categories where growth exceeded 5% in the last 3 years, (7) Final SELECT combining both CTEs to show: category, year, expenditure, yoy_growth_pct, exceeded_threshold (boolean). Expected output: SQL result set with 15+ rows showing health spending trends and growth flags._
  📦 Dataset: `AIHW Health Expenditure Data — aihw.gov.au`
  📁 Submit as: `quest3_2026-04-17.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
