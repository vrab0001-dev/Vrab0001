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
| 📅 Last Sync | 2026-10-19 13:08 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Ranking
  _Using ASX 200 historical price data, calculate the 30-day price change percentage for each stock. Use a CTE to compute the opening price 30 days ago and the most recent closing price for each ticker. Then use ROW_NUMBER() windowed function to rank stocks by momentum (highest to lowest % gain) within each month. Return the top 10 gainers and bottom 10 losers for the most recent complete month in the dataset. Include ticker, price change %, rank, and the calculation date._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-19.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data (CSV format). Clean the dataset by: (1) removing rows with missing crash location coordinates, (2) standardising the Crash_Type column to title case and removing leading/trailing whitespace, (3) converting datetime columns to proper datetime objects, (4) filtering for crashes in the last 5 years only. Then aggregate the cleaned data to calculate total crashes, fatalities, and severity distribution by Local Government Area (LGA). Export results to a new CSV file with LGA, total_crashes, total_fatalities, and severity_breakdown columns. Document any data quality issues found._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-19.py`
- [ ] ⚡ **Combined Quest:** AFL Match Performance Pipeline
  _Build an end-to-end pipeline: (1) In Python, load AFL match results dataset (Kaggle), clean team names (fix case inconsistencies), and calculate each team's win-loss record, average points scored, and average points conceded for the last 2 completed seasons. Save to a SQLite database table named 'team_stats'. (2) In SQL, query this table to identify the top 5 most improved teams (by win percentage increase year-on-year) and the top 3 defensive teams (lowest average points conceded). (3) Return a final result showing team name, previous season win %, current season win %, improvement %, and defensive ranking. Document your Python data transformations in comments._
  📦 Dataset: `AFL Match Results — Kaggle`
  📁 Submit as: `quest3_2026-10-19.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
