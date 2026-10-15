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
| 📅 Last Sync | 2026-10-15 13:08 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Volatility Rankings with Window Functions
  _Using ASX 200 historical prices dataset, calculate daily percentage change for each stock using LAG window function. Then use ROW_NUMBER to rank stocks by volatility (standard deviation of percentage changes) within each month. Finally, identify the top 3 most volatile stocks per month using a CTE. Your output should show: month, rank, stock_code, volatility_score, and average_daily_change. Filter for 2024 data only._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-15.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data and perform comprehensive data cleaning: handle missing values in severity, speed_zone, and weather columns; standardise date formats; remove duplicate crash records; validate latitude/longitude bounds for NSW (between -28.0 to -34.0 and 140.0 to 154.0). Engineer new features: crash_hour (extract from time), is_nighttime (between 18:00-06:00), and weather_category (group rare weather types into 'Other'). Output a cleaned CSV with 15+ columns. Document all transformations in comments._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-15.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis Pipeline
  _Part 1 (Python): Fetch or load Australian wine production statistics by region and vintage year. Clean the data: handle missing production volumes, standardise region names (remove whitespace/case inconsistencies), remove outliers using IQR method on production volume. Export to a CSV named 'wine_clean.csv'. Part 2 (SQL): Load the cleaned data into a database table. Write a query using CTEs and window functions to: (1) calculate 3-year rolling average production per region, (2) rank regions by total production volume, (3) identify regions with year-on-year growth exceeding 10%. Output: region, vintage, production_volume, rolling_avg_3yr, region_rank, yoy_growth_pct. Limit results to top 20 regions by total production._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com or agriculture.gov.au`
  📁 Submit as: `quest3_2026-10-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
