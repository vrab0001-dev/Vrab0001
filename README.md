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
| 📅 Last Sync | 2026-09-24 11:56 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Ranking with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility within each month using ROW_NUMBER() and RANK(). Return the top 10 most volatile stocks per month along with their volatility score, rank, and the previous month's volatility using LAG(). Expected output: month, stock_code, volatility_score, rank_in_month, previous_month_volatility._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-09-24.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Standardisation
  _Download NSW Road Crash Data (data.nsw.gov.au). Clean and transform the dataset by: (1) handling missing values in crash_severity and location columns, (2) standardising date formats to YYYY-MM-DD, (3) extracting suburb and postcode from address strings using regex, (4) flagging outliers in injury_count (values >50), (5) creating a new column crash_hour from timestamp. Export cleaned data to CSV. Expected output: cleaned_crashes.csv with 8-10 columns, no nulls in critical fields, consistent data types._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-09-24.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection Pipeline
  _Build a data pipeline: (1) Extract Australian Weather observations data (Bureau of Meteorology dataset on Kaggle). (2) Use Python/pandas to load, clean temperature and rainfall columns, and calculate monthly averages by station and year. (3) Save cleaned data to a CSV. (4) Load into SQL and use CTEs + window functions to calculate 10-year rolling averages and identify months where temperature exceeded the rolling average by >2 standard deviations. (5) Return: station_name, month, year, actual_temp, rolling_avg, deviation_in_stdev, anomaly_flag (Y/N). Export final results to anomalies.csv._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg Australian Weather)`
  📁 Submit as: `quest3_2026-09-24.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
