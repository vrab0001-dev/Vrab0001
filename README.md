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
| 📅 Last Sync | 2026-06-15 12:32 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Top Performers: Rank Daily Gainers with Running Average
  _Using the ASX 200 historical prices dataset, write a query that ranks stocks by daily percentage gain (Close - Open) / Open * 100 for each trading date. Use a CTE to calculate daily gains, then apply ROW_NUMBER() OVER (PARTITION BY date ORDER BY daily_gain DESC) to rank stocks per day. Include a second window function LAG() to calculate the 5-day moving average of each stock's closing price. Filter for the top 10 gainers on the most recent trading date in your dataset. Expected output: stock_code, date, daily_gain_percent, rank_for_day, five_day_moving_avg._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-15.sql`
- [ ] 🐍 **Python Quest:** Clean & Standardise Australian Weather Data for Analysis
  _Download or load the Australian Weather observations dataset (Bureau of Meteorology historical data). Your task: (1) Handle missing values in temperature, rainfall, and wind speed columns using appropriate imputation (mean for temp/wind, zero for no-rain days); (2) Standardise date formats to ISO 8601 (YYYY-MM-DD); (3) Remove duplicate rows based on station_id + date; (4) Convert temperature from Celsius to Fahrenheit in a new column; (5) Create a new column 'weather_category' that bins rainfall into 'Dry' (<1mm), 'Light' (1-10mm), 'Moderate' (10-50mm), 'Heavy' (>50mm); (6) Export cleaned data to cleaned_weather_au.csv. Document any data quality issues found (% missing, duplicates removed, outliers detected)._
  📦 Dataset: `Australian Weather observations — Bureau of Meteorology / Kaggle (jsphyg weather dataset)`
  📁 Submit as: `quest2_2026-06-15.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: Load, Clean, Aggregate & Rank by Risk
  _End-to-end data engineering task: (1) Use Python/pandas to load NSW Road Crash Data from data.nsw.gov.au. Clean the dataset: standardise location names (remove extra whitespace, uppercase consistency), convert date columns to datetime, remove rows with missing severity or location data, flag and count invalid coordinates (outside NSW bounds). Export to crashes_cleaned.csv. (2) In SQL, import the cleaned CSV and write a query using CTEs and window functions: calculate crash frequency, injury rate (injuries / crash_count), and fatality rate by local government area (LGA). Use ROW_NUMBER() to rank LGAs by fatality rate (highest risk first). Include a CASE statement to flag high-risk areas (fatality_rate > state average). Return: LGA, crash_count, injury_count, fatality_count, injury_rate, fatality_rate, risk_flag, rank_by_fatality. (3) Document the data pipeline: how many rows were cleaned/removed in Python, and which LGAs are flagged as high-risk in SQL output._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-06-15.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
