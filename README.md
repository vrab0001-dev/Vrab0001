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
| 📅 Last Sync | 2026-07-07 11:53 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a query that ranks stocks by their year-to-date percentage gain. For each stock, calculate: (1) the closing price on the most recent date, (2) the closing price on 2026-01-01, (3) the percentage change, (4) a rank among all stocks by percentage gain using ROW_NUMBER(), and (5) a running cumulative count of stocks by sector ordered by gain descending. Use a CTE to calculate the start-of-year and end-of-period prices separately, then JOIN them. Return the top 20 performing stocks with all calculated columns. Expected output: stock symbol, sector, start price, end price, % gain, rank, cumulative count._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-07.sql`
- [ ] 🐍 **Python Quest:** Clean and Standardise NSW Road Crash Data
  _Download or load the NSW Road Crash Data (contains crash severity, vehicle types, weather conditions, postcodes). Your task: (1) Handle missing values in the 'Weather Condition' column by replacing with 'Unknown'; (2) Standardise all text columns (Severity, Vehicle_Type) to title case; (3) Extract the year and month from the crash date into separate columns; (4) Remove duplicate rows based on Crash_ID; (5) Create a new column 'Speed_Zone_Category' that bins speed zones into 'Low' (<=50), 'Medium' (51-80), 'High' (81+); (6) Export the cleaned dataset to a CSV file with timestamp in filename. Validate the output by printing row counts before/after cleaning and checking for remaining nulls in critical columns._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-07.py`
- [ ] ⚡ **Combined Quest:** Energy Demand Peak Analysis Pipeline
  _Build an end-to-end pipeline using AEMO electricity demand data: (1) In Python, load the AEMO electricity demand CSV, clean column names (remove spaces, standardise to snake_case), and parse timestamps. Group by date and state, calculate daily peak demand and average demand. Save to a cleaned CSV. (2) Load the cleaned CSV into a SQL database (SQLite or similar). (3) Write a SQL query that identifies for each state: the date with highest peak demand in 2026, the average daily peak demand per month, and a LAG() window function showing month-over-month peak demand change. (4) Export results showing state, month, peak demand, monthly average, and month-over-month change. Expected output: 6-8 rows per state showing trends across available months in 2026._
  📦 Dataset: `AEMO Electricity Demand Data — aemo.com.au`
  📁 Submit as: `quest3_2026-07-07.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
