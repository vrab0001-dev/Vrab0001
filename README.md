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
| 📅 Last Sync | 2026-08-20 10:32 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Moving Averages
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their 30-day moving average performance. Calculate ROW_NUMBER() partitioned by stock ticker ordered by moving average gain/loss. Use a CTE to compute the 30-day moving average price for each stock, then rank them. Return the top 10 stocks with highest moving average gains and bottom 10 with losses, including columns: ticker, date, closing_price, 30day_moving_avg, price_vs_ma, and rank. This tests your understanding of window functions (ROW_NUMBER, AVG() OVER), CTEs, and analytical queries._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-08-20.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Analysis
  _Download the NSW Road Crash Data from data.nsw.gov.au. Use pandas to: (1) load the CSV and inspect for missing values and data types; (2) clean the dataset by handling nulls in crash_severity and location columns; (3) standardise the datetime column to YYYY-MM-DD format; (4) create a new feature called 'crash_hour' extracted from the time field; (5) filter crashes with injury_count > 0; (6) export a cleaned CSV with only relevant columns (crash_id, date, location, severity, injury_count, crash_hour). Write clear comments explaining each transformation step. Expected output: a cleaned CSV file ready for analysis._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-20.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Python ETL to SQL Analytics
  _Load the Australian Weather observations dataset (from Bureau of Meteorology via Kaggle). Step 1 (Python): Use pandas to extract temperature and rainfall data, group by month and state, calculate mean_temperature and total_rainfall per month. Clean any outliers (e.g., temperature > 50°C or < -20°C) by removing rows. Save the aggregated data to a CSV. Step 2 (SQL): Create a table from the CSV and write a query using window functions to identify the top 3 months with highest rainfall per state using RANK() OVER (PARTITION BY state ORDER BY total_rainfall DESC). Also calculate the month-over-month temperature change using LAG(). Return state, month, rainfall, temperature, and temp_change columns. This combines ETL pipeline design with advanced SQL analytics._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology (Kaggle: jsphyg)`
  📁 Submit as: `quest3_2026-08-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
