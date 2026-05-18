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
| 📅 Last Sync | 2026-05-18 12:03 AEDT |

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
  _Using ASX 200 historical price data, calculate the 10-day moving average and identify momentum shifts. Write a query using window functions (ROW_NUMBER, LAG, AVG OVER) to: 1) Compute the 10-day moving average closing price for each stock, 2) Calculate the day-over-day price change percentage using LAG, 3) Rank stocks by momentum (price change) within each trading day, 4) Filter for only days where momentum shifted from positive to negative or vice versa. Return stock symbol, date, closing price, 10-day MA, price change %, and momentum rank. Use a CTE to structure the calculation stages._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data and perform comprehensive data cleaning: 1) Identify and handle missing values (document your strategy for each column), 2) Standardise date/time formats and extract hour-of-day and day-of-week features, 3) Parse location data and create a severity classification column (Critical/Serious/Minor based on injury counts), 4) Remove duplicate records based on crash ID and timestamp, 5) Export cleaned dataset as CSV with a data quality report showing record counts before/after cleaning and missing value percentages. Write your script in pandas with clear comments explaining each transformation step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-18.py`
- [ ] ⚡ **Combined Quest:** AFL Match Performance Pipeline: Python ETL to SQL Analytics
  _Build a mini data pipeline: 1) Use Python/pandas to scrape or load AFL match results dataset (2023-2024 season), clean team names, standardise date formats, and calculate derived metrics (points differential, win/loss streak, home vs away performance), 2) Export to CSV, then load into a SQL database (SQLite or PostgreSQL), 3) Write a SQL query using window functions to rank teams by current win streak and calculate their season statistics (wins, losses, points for/against, win percentage), 4) Identify the top 3 teams with the highest momentum (best recent form using LAG/LEAD over last 5 matches). Output a final summary table showing team rank, name, win streak, season win%, and momentum score._
  📦 Dataset: `AFL Match Results — Kaggle (afltables.com historical data)`
  📁 Submit as: `quest3_2026-05-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
