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
| 📅 Last Sync | 2026-04-29 11:49 AEDT |

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
  _Using ASX 200 historical price data, calculate daily percentage returns for each stock. Then use window functions (ROW_NUMBER, LAG) to rank stocks by their 5-day momentum (average return over last 5 days). For each date in your dataset, show the top 10 and bottom 10 performers by momentum. Use a CTE to calculate rolling averages. Expected output: date, stock_code, close_price, daily_return_pct, 5day_avg_return, momentum_rank._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Risk Scoring
  _Load NSW Road Crash data and perform comprehensive data cleaning: handle missing values in crash_type, severity, and location fields; standardise datetime formats; remove duplicate records; validate latitude/longitude coordinates are within NSW bounds. Then create a risk_score column (1–10) based on severity and presence of injuries. Group by local government area (LGA) and generate summary statistics: total crashes, average risk_score, percentage involving fatalities. Export cleaned data and summary report as CSV files._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-29.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Patterns: Data Pipeline & Trend Analysis
  _Build a Python script that loads Australian Bureau of Meteorology weather observations (temperature, rainfall, humidity). Clean the data: remove outliers (e.g. temperatures >60°C or <-60°C), handle missing values via forward-fill for consecutive days, standardise station names. Load cleaned data into a SQLite database. Then write SQL queries to: (1) Calculate 30-day rolling average temperature by station using window functions; (2) Identify stations where rainfall exceeded 90th percentile for their region; (3) Rank stations by temperature volatility (std dev) within each state. Export results showing station, region, metric, and rank._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology / Kaggle`
  📁 Submit as: `quest3_2026-04-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
