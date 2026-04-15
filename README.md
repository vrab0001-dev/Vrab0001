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
| 📅 Last Sync | 2026-04-15 11:18 AEDT |

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
  _Using ASX 200 historical stock price data, calculate the 20-day moving average for each stock ticker. Then rank stocks by their current price relative to their 20-day moving average (percentage above/below). Use window functions (ROW_NUMBER, AVG OVER) to identify the top 10 momentum gainers and bottom 10 momentum losers within each sector or industry group. Output should include ticker, current price, 20-day MA, momentum percentage, and rank within sector. This requires CTEs for the moving average calculation and window functions for ranking._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-04-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data from the NSW government open data portal. Load the CSV into pandas and perform: (1) handle missing values in 'Weather Condition' and 'Light Condition' columns by imputing with mode; (2) parse the 'Crash Date' column to extract year, month, day_of_week; (3) create a new feature 'severity_score' by categorising crashes as Critical (fatality), Serious (hospitalisation), or Minor based on injury types; (4) filter crashes occurring in Sydney Local Government Areas only; (5) export the cleaned dataset to a new CSV with all original columns plus engineered features. Document any data quality issues found._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-15.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analytics Pipeline
  _Create an end-to-end data pipeline: (1) Python task: Download Australian wine production statistics by region and vintage year. Clean the data (handle missing values, standardise region names, convert volume to consistent units). Create a CSV with columns: Region, Vintage, Production_Litres, Varietal. (2) SQL task: Load this cleaned CSV into a database table. Write a query using window functions to calculate year-over-year production growth percentage for each region, and identify which region had the largest production decline in any single year. Include a CTE to compute 3-year rolling average production per region. Output the top 5 regions by average production and their volatility (standard deviation) across the decade._
  📦 Dataset: `Australian wine production statistics — wineaustralia.com (Wine Australia data)`
  📁 Submit as: `quest3_2026-04-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
