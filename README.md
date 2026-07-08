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
| 📅 Last Sync | 2026-07-08 11:24 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to calculate: (1) a 20-day moving average of closing price for each stock, (2) the rank of each stock by price change percentage within each month, (3) identify stocks that hit new 52-week highs. Use CTEs to structure your query clearly. Expected output: a result set showing stock ticker, date, close price, 20-day MA, monthly rank, and a boolean flag for 52-week high. Filter for the last 6 months of data._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-07-08.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python/pandas script to: (1) handle missing values in crash severity, location, and vehicle type columns using appropriate strategies (drop, forward-fill, or mode), (2) create new features: crash_hour from timestamp, severity_category (group severity levels), day_of_week, (3) detect and flag outliers in crash count by location using IQR method, (4) export a cleaned CSV with consistent column naming (snake_case). Document your data quality decisions with comments. Expected output: a cleaned CSV file ready for analysis._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-07-08.py`
- [ ] ⚡ **Combined Quest:** ABARES Crop Production Analytics Pipeline
  _Build a data engineering pipeline combining Python and SQL: (1) In Python, fetch or load the ABARES crop production data (wheat, barley, canola, etc. by state and year), clean column names, handle missing production values, and load it into a SQLite database. (2) In SQL, write a query using window functions to calculate year-over-year production change percentage by crop and state, identify the top 3 growing crops nationally, and rank states by total production using RANK(). (3) Export results as a CSV showing crop, state, year, production, YoY change %, and national rank. Expected output: a complete Python script + SQL query + output CSV demonstrating full ETL workflow._
  📦 Dataset: `ABARES Crop Production Data — agriculture.gov.au`
  📁 Submit as: `quest3_2026-07-08.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
