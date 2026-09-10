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
| 📅 Last Sync | 2026-09-10 11:49 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Daily Returns & Momentum Ranking
  _Using ASX 200 historical price data, write a query that calculates daily percentage returns for each stock, then ranks stocks by their 20-day rolling average return using window functions. Use ROW_NUMBER() to identify the top 10 and bottom 10 performers for each date. Include columns: date, ticker, close_price, daily_return_pct, rolling_20day_avg_return, rank_within_date. Filter for the last 90 days of data. Expected output: ranked daily performer table showing momentum shifts._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Geospatial Aggregation
  _Download NSW Road Crash Data (contains missing values, inconsistent date formats, and duplicates). Using pandas: (1) standardise all date columns to YYYY-MM-DD format, (2) handle missing values in 'Severity' and 'Crash Type' columns by imputation or removal with justification, (3) remove exact duplicate rows, (4) create a new 'Month_Year' column, (5) group crashes by Local Government Area (LGA) and severity level, counting incidents per LGA-Severity combination, (6) export cleaned data to CSV with clear column names. Document your data quality issues found and how you resolved them._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-10.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Dashboard Data Pipeline
  _Build a mini ETL pipeline: (1) In Python, load Australian Wildfire dataset (Kaggle), clean the data (handle missing lat/lon, standardise date formats, remove outliers in fire size), and export to a CSV named 'cleaned_fires.csv'. (2) Create a SQL schema with a fires table (fire_id, date, latitude, longitude, estimated_area_hectares, state, severity). (3) Write a SQL query using window functions and CTEs to: identify the Top 5 most severe fire seasons by state (using LAG to compare year-over-year fire frequency), calculate a 'Fire Risk Score' (severity rank * fire count) for each state per season, and rank states by risk. (4) Output a summary table: state, fire_season_year, total_fires, avg_area_hectares, fire_risk_score, risk_rank. Expected outcome: actionable insights into which Australian states face escalating wildfire risk trends._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-09-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
