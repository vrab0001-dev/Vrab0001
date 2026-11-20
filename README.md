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
| 📅 Last Sync | 2026-11-20 15:40 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Trading Signal
  _Using ASX 200 historical price data, calculate a 20-day moving average and identify trading signals. Write a query using window functions (ROW_NUMBER, LAG) and CTEs to: (1) Calculate the 20-day moving average for each stock using AVG() OVER (PARTITION BY ticker ORDER BY date ROWS BETWEEN 19 PRECEDING AND CURRENT ROW), (2) Use LAG to compare current close price to previous close, (3) Flag 'BUY' when price crosses above MA and 'SELL' when it crosses below MA, (4) Rank signals by signal strength (momentum). Return top 10 stocks with strongest buy signals in the last 30 days. Output: ticker, date, close_price, moving_avg_20, signal_type, momentum_rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-20.sql`
- [ ] 🐍 **Python Quest:** Clean & Standardise Australian Weather Data
  _Download or load Australian Bureau of Meteorology weather observations (daily min/max temperature, rainfall, wind speed for a major city like Sydney). Your task: (1) Handle missing values intelligently—use forward fill for temperature, interpolation for rainfall, (2) Standardise date format to YYYY-MM-DD, (3) Convert temperature from Celsius to Fahrenheit in a new column, (4) Create a 'weather_category' column (Hot >30°C, Warm 20-30°C, Cool 10-20°C, Cold <10°C), (5) Remove outliers using IQR method on temperature, (6) Export cleaned data to CSV with proper column naming (snake_case). Output: cleaned CSV with 7+ columns, no NaN values in critical fields, 100+ rows minimum._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (BoM) / Kaggle (jsphyg collection)`
  📁 Submit as: `quest2_2026-11-20.py`
- [ ] ⚡ **Combined Quest:** NSW Road Crash Analysis: Data Pipeline
  _Build an end-to-end pipeline combining Python and SQL. (1) Python: Load NSW Road Crash Data (CSV from data.nsw.gov.au), clean it—standardise location formats, handle missing severity/injury counts, convert date/time columns, deduplicate records. Output cleaned CSV. (2) SQL: Create a table from cleaned data, then write a query using window functions to: Calculate crash frequency by Local Government Area (LGA) with ROW_NUMBER() to rank LGAs, use LAG() to compare month-over-month crash changes, create a CTE to identify high-risk locations (top 10% by severity-weighted incidents). Calculate severity index: (fatal_count * 5) + (serious_count * 2) + (other_count * 1). Return: LGA, crash_count, severity_index, rank, month_change_pct, risk_category (High/Medium/Low). Bonus: Identify day-of-week patterns using GROUP BY and window functions._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest3_2026-11-20.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
