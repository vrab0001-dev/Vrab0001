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
| 📅 Last Sync | 2026-03-23 16:46 AEDT |

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
  _Using the ASX 200 historical prices dataset, calculate the 10-day and 30-day moving averages for the top 5 most traded stocks by volume. Use window functions (AVG() OVER) to compute these moving averages partitioned by stock ticker and ordered by date. Then identify which stocks had the biggest price momentum (current price vs 30-day MA) on the most recent date. Return: ticker, date, close_price, ma_10day, ma_30day, momentum_percentage. Order by momentum_percentage DESC._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-23.sql`
- [ ] 🐍 **Python Quest:** Australian Weather Data Cleaning & Missing Value Imputation
  _Download or use the Australian Weather observations dataset (Bureau of Meteorology). Load a CSV with temperature, humidity, rainfall, and wind speed data from multiple Australian cities across 2024-2025. Clean the data by: (1) identifying and documenting missing values per column, (2) removing rows with >30% missing data, (3) imputing missing temperature values using forward-fill then backward-fill per city, (4) imputing rainfall with 0 where appropriate, (5) removing outliers >3 standard deviations from mean per city. Output: a clean CSV with row counts before/after, missing value counts per column before/after, and a summary report showing data quality improvements._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology or Kaggle (jsphyg)`
  📁 Submit as: `quest2_2026-03-23.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Data: Injury Severity Trends & Root Cause Analysis Pipeline
  _Using NSW Road Crash Data (data.nsw.gov.au): (1) In Python/pandas: Load the crash dataset, clean date/time fields, convert crash_severity to numeric categories (1=non-injury, 2=other injury, 3=serious injury, 4=fatality). Handle missing speed_zone, weather, and road_type values. Save cleaned data to a SQLite database. (2) In SQL: Create a CTE that ranks crashes by severity within each LGA (Local Government Area) and month. Use ROW_NUMBER() to identify the top 3 most dangerous months per LGA. Then aggregate: for each LGA and severity level, count crashes and calculate average number of vehicles involved. Return: lga, month, severity_rank, crash_count, avg_vehicles_involved, severity_label. (3) Combine: use Python to read SQL results and generate a markdown report with insights on which LGAs had worsening trends and which weather/road conditions were most common in high-severity crashes._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-03-23.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
