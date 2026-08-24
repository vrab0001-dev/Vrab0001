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
| 📅 Last Sync | 2026-08-24 10:33 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Volatility Analysis with Window Functions
  _Using ASX 200 historical price data, calculate the 20-day rolling standard deviation of daily returns for each stock. Use a CTE to first compute daily percentage changes (LAG function), then apply window functions to calculate rolling volatility across the window frame. Filter for stocks with volatility > 3% and rank them by volatility within each month. Expected output: stock_code, date, daily_return, rolling_volatility, volatility_rank, month. This demonstrates window frame specification and CTEs for financial analysis._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Injury Classification Pipeline
  _Download NSW Road Crash Data and build a Python pandas script that: (1) handles missing values in 'Severity' and 'Speed Limit' columns using domain-appropriate strategies, (2) standardises location data (suburb names to title case, removes duplicate whitespace), (3) creates a new categorical column 'Injury_Risk' (Low/Medium/High) based on injury counts and speed limit, (4) exports cleaned data to CSV and logs data quality metrics (null counts before/after, unique values per categorical column). Expected output: cleaned CSV file + data_quality_report.txt with before/after comparisons._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-24.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: SQL Analytics + Python Validation Pipeline
  _Using Australian Bureau of Meteorology weather observations dataset: (1) Write SQL to identify the top 5 weather stations with the highest average daily temperature variance (using window functions to compute daily min/max and variance within 30-day rolling windows), rank them by state. (2) Export results to CSV via Python. (3) Build a Python validation script that reads the CSV, cross-checks station names against a reference list (create a small reference CSV or hardcode known stations), flags any data quality issues (missing coordinates, duplicate station entries), and generates a summary report showing data completeness % by state. (4) Re-import validated results into a SQLite database table for archival. Expected outputs: initial_analysis.csv, validation_report.txt, archived_weather_analysis.db with one validated table._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (via Kaggle: jsphyg/weather-australia)`
  📁 Submit as: `quest3_2026-08-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
