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
| 📅 Last Sync | 2026-10-30 14:15 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Ranking with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query that calculates a 30-day price momentum for each stock. Use window functions (LAG, ROW_NUMBER) to rank stocks by momentum within each date partition. Include: stock symbol, date, closing price, 30-day price change percentage, and momentum rank (1=highest gain). Filter to only the last 10 trading days and return the top 5 momentum gainers for each day. Bonus: Use a CTE to pre-calculate the 30-day moving average for comparison._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-30.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Incident Classification
  _Download the NSW Road Crash Data (CSV format) from data.nsw.gov.au. Write a Python/pandas script that: (1) cleans datetime columns and handles missing values in injury counts and speed zones, (2) creates a new 'severity_category' column (Fatal, Serious Injury, Other Injury, Non-Injury) based on the injury counts, (3) identifies and flags outlier coordinates (crashes recorded outside NSW bounds), (4) exports a cleaned dataset to CSV with a summary report showing record counts per severity category and missing data percentages by column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-30.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis Pipeline
  _End-to-end task: (1) Use Python/pandas to download and clean the ABARES wine production dataset (or wine production CSV from Wine Australia). Handle missing regions, standardise vintage years, and convert volume/value columns to numeric types. Export cleaned data to a SQLite database. (2) In SQL, create a query that ranks wine-producing regions by total production volume, calculates year-over-year growth percentage using LAG window function, and identifies which regions have consistent growth (>5% growth in last 3 years). Return the top 10 regions with growth trends. (3) Generate a summary report (Python) showing regions with accelerating production and those in decline._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia / ABARES`
  📁 Submit as: `quest3_2026-10-30.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
