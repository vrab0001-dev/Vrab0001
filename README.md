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
| 📅 Last Sync | 2026-09-20 12:03 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Average Volatility Tracker
  _Using ASX 200 historical price data, write a SQL query with window functions to calculate the 20-day rolling average closing price and volatility (standard deviation) for the top 5 most traded stocks by volume. Use ROW_NUMBER() to rank stocks, LAG() to access previous closing prices, and a CTE to pre-filter high-volume stocks. Return stock symbol, date, closing price, 20-day rolling average, and rolling volatility, ordered by stock and date. Expected output: 5 stocks × ~252 trading days of rolling metrics._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-20.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Geocoding Pipeline
  _Download NSW Road Crash Data (data.nsw.gov.au). Write a Python/pandas script to: (1) load the CSV and inspect missing values, data types, and duplicates; (2) clean date columns to datetime format and standardise location names (remove extra whitespace, convert to title case); (3) filter crashes with severity='Fatal' or 'Serious injury' from the last 5 years; (4) create a new column 'hour_of_day' extracted from crash time; (5) group by hour_of_day and count crashes, then export as a new CSV. Expected output: cleaned dataset and summary CSV showing crash frequency by hour._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-20.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis: Python ETL + SQL Analytics
  _Challenge: Extract, transform, and analyse Australian wine production statistics. (1) Use Python/pandas to fetch or load wine production data (by region, vintage year, varietal), clean any inconsistencies (standardise region names, handle missing volumes), and load into a local SQLite database with two tables: wines (region, varietal, vintage, volume_produced, price_index) and regions (region_name, state, latitude, longitude). (2) Write SQL queries to: (a) use a CTE to rank top 3 varietals by total volume produced across all regions; (b) use ROW_NUMBER() and LAG() to identify year-on-year growth trends for the top producing region; (c) calculate cumulative production volume by vintage year using a window function. Expected output: populated SQLite database + 3 SQL result sets showing rankings, trends, and cumulative metrics._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com or Kaggle`
  📁 Submit as: `quest3_2026-09-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
