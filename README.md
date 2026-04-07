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
| 📅 Last Sync | 2026-04-07 11:15 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 30-day rolling standard deviation of daily returns for each stock ticker. Rank stocks by volatility within each month using ROW_NUMBER() and RANK() window functions. Return the top 5 most volatile stocks per month, showing ticker, date, closing price, 30-day volatility, and volatility rank. Use a CTE to calculate daily returns first, then another CTE for the rolling standard deviation. Filter results for the last 6 months of available data._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-07.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download or load the NSW Road Crash Data (available from data.nsw.gov.au). Clean the dataset by: (1) handling missing values in Crash_Type, Speed_Zone, and Weather columns using appropriate strategies; (2) converting datetime columns to proper datetime objects; (3) removing duplicate records based on Crash_ID; (4) creating new features: hour_of_day (extracted from crash time), is_fatal (binary from Severity), and road_condition_category (grouping weather into Clear/Wet/Fog/Other). Output a cleaned CSV with all original columns plus new features. Provide a summary report showing row counts before/after cleaning and missing value percentages._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-07.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis Pipeline
  _Build an end-to-end pipeline using Python and SQL: (1) Extract Melbourne pedestrian counting data (from Melbourne Open Data Portal) covering the last 12 months; (2) Use Python/pandas to clean the dataset—handle missing sensor readings, convert timestamps to Australian Eastern time, and aggregate hourly counts by sensor location; (3) Save cleaned data to a local SQLite database; (4) Using SQL, calculate for each sensor location: total monthly pedestrian traffic, day-of-week patterns (using CASE statements), peak hours (using window functions LAG/LEAD to identify traffic spikes), and month-over-month growth rate using LAG(); (5) Create a summary table ranking sensors by average daily traffic and identify the top 3 busiest locations by month. Output results as CSV with sensor name, month, traffic metrics, and growth percentage._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-04-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
