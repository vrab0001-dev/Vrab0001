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
| 📅 Last Sync | 2026-11-27 16:39 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Rankings with Window Functions
  _Using ASX 200 historical price data, calculate the 20-day rolling standard deviation of daily returns for each stock. Use window functions (PARTITION BY ticker, ORDER BY date) to rank stocks by volatility within each month. Return the top 5 most volatile stocks per month, including ticker, date, closing price, rolling volatility, and volatility rank. Use a CTE to first calculate daily percentage returns, then another CTE for the rolling standard deviation._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-27.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data (contains crash records with location, severity, vehicle type, weather conditions). Clean the dataset by: (1) handling missing values in severity and weather columns (impute with mode or drop as appropriate), (2) standardising location strings to title case, (3) converting date columns to datetime format, (4) creating new features: crash_hour from timestamp, severity_category (binning injury counts), and weather_risk_score. Output a cleaned CSV with 10+ columns ready for analysis. Document your data quality assumptions in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-27.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Impact Analysis Pipeline
  _Build a data pipeline combining Python and SQL: (1) In Python, download Australian Wildfire dataset (Kaggle), clean fire duration data, convert hectares burned to standardised numeric format, and filter for fires in 2020-2024. Export to CSV. (2) In SQL, load the cleaned data, calculate cumulative hectares burned by state using window functions (SUM() OVER PARTITION BY state ORDER BY date), identify the fire season (months with peak activity) for each state, and rank states by total area burned across the period. Return a summary table: state, fire_season_months, total_hectares_burned, rank. Use CTEs to structure your query clearly._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-11-27.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
