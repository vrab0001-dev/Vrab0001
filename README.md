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
| 📅 Last Sync | 2026-09-22 12:10 AEDT |

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
  _Using ASX 200 historical price data, create a CTE that calculates the 30-day price change percentage for each stock. Then use window functions (ROW_NUMBER and RANK) to rank stocks by momentum within each sector. Include a LAG function to show the previous day's closing price for comparison. Filter for stocks with at least 20 trading days of data in the last month. Output should show: stock_code, sector, current_price, previous_close, price_change_pct, momentum_rank_in_sector, and trading_day_count. Order by sector and momentum_rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-22.sql`
- [ ] 🐍 **Python Quest:** Bureau of Meteorology Data Cleaning Pipeline
  _Download Australian Weather observations data (daily maximum temperature, rainfall, wind speed across multiple stations). Write a Python script using pandas to: (1) handle missing values strategically (forward-fill for temperature, zero for rainfall if no rain recorded), (2) detect and flag outliers using IQR method for each weather variable, (3) convert date strings to datetime objects, (4) create new features: day_of_week, is_weekend, rolling_7day_avg_temp. (5) Export cleaned data to CSV with a timestamp suffix. Document which rows were flagged as outliers and why. Expected output: cleaned CSV with 10+ columns and summary statistics showing data quality improvements._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (BOM) / Kaggle jsphyg`
  📁 Submit as: `quest2_2026-09-22.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Risk Analysis Pipeline
  _Build an end-to-end pipeline: (1) In Python, download NSW Road Crash Data, clean it by removing rows with null crash_date or location, standardise crash_severity categories (replace variations with canonical values), and engineer features: hour_of_day (from time), day_of_week, is_night (hour >= 18 or hour < 6). (2) Export cleaned data to CSV. (3) In SQL, load this CSV into a temporary table and write a query using CTEs to: calculate crash frequency by hour_of_day and day_of_week, use ROW_NUMBER to identify top 5 highest-risk time slots, calculate a running total of crashes by day_of_week using window functions. (4) Create a second CTE that ranks suburbs/locations by crash severity (count of severe/fatal crashes). Output: two result sets—one showing peak risk times with frequency metrics, one showing top 10 risky locations. Expected insight: identify if crashes cluster at specific times or locations._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-09-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
