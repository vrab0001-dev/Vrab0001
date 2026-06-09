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
| 📅 Last Sync | 2026-06-09 11:54 AEDT |

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
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to: (1) Calculate the 20-day moving average for each stock using LAG, (2) Rank stocks by their price momentum (current price vs 20-day MA) using RANK() PARTITION BY sector, (3) Identify the top 3 gainers and bottom 3 losers per sector over the last 60 trading days. Return columns: stock_code, sector, current_price, moving_avg_20, momentum_percentage, rank_in_sector. Use a CTE to calculate the moving average first, then window functions for ranking. Expected output: 6-12 rows showing top and bottom performers by sector._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Score Pipeline
  _Download NSW Road Crash Data (contains crash records with location, severity, weather, road conditions). Build a Python pandas script to: (1) Load the CSV and handle missing values (impute weather data with mode, drop records missing crash_id), (2) Create a crash_risk_score column (0-100) combining severity_level (40%), number_of_vehicles (30%), speed_zone (20%), weather_condition (10%), (3) Standardise location names (strip whitespace, convert to title case), (4) Export cleaned data to a new CSV with columns: crash_id, location, crash_date, risk_score, severity_level. Add a summary report showing: total crashes, crashes by severity, average risk score, top 5 high-risk locations. Expected output: cleaned CSV file + printed summary statistics._
  📦 Dataset: `NSW Road Crash Data — NSW Open Data Portal`
  📁 Submit as: `quest2_2026-06-09.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns & Agricultural Yield Correlation
  _Combine Bureau of Meteorology weather observations with ABARES crop production data to investigate seasonal relationships. Step 1 (Python): Load monthly weather data (temperature, rainfall) and annual crop yields by region. Clean both datasets: handle missing weather values using forward-fill, standardise region names, convert dates to consistent format. Merge datasets on region and year. Step 2 (SQL): Create a table from the merged data. Write a query using CTEs to: (1) Calculate rolling 3-month average rainfall and temperature per region, (2) Use LAG() to compare current year's climate metrics vs prior year, (3) Calculate Pearson correlation between avg_rainfall and crop_yield per region, (4) Rank regions by yield volatility (std dev of yield over 10 years). Step 3 (Python): Read SQL results back, create visualisation (scatter plot: rainfall vs yield per region, colour-coded by correlation strength). Expected output: correlation analysis table, volatility ranking, and multi-region scatter plot showing climate-yield relationships._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology/Kaggle (jsphyg) + ABARES crop production data — agriculture.gov.au`
  📁 Submit as: `quest3_2026-06-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
