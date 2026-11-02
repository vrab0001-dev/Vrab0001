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
| 📅 Last Sync | 2026-11-02 14:02 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, calculate the 5-day and 20-day moving averages for each stock using window functions (AVG() OVER). Then identify stocks where the 5-day MA crossed above the 20-day MA in the last 30 days. Rank these 'golden cross' signals by the magnitude of the price gap. Return: stock_code, date, price_5day_ma, price_20day_ma, gap_percentage, rank_by_gap. Use a CTE to structure the moving average calculations, then filter for crossovers in your main query._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-02.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Severity Classification
  _Download the NSW Road Crash Data from the NSW open data portal. Load the CSV into pandas. Clean the dataset: handle missing values in 'Crash Type' and 'Severity' columns (document your strategy), standardise date formats, remove duplicate records by Crash ID. Create a new column 'severity_score' (1-5 scale) based on the 'Severity' field and number of vehicles involved. Export the cleaned dataset to a new CSV file with a timestamp in the filename. Write a summary report (3-5 sentences) documenting: rows removed, columns with highest missing %, and distribution of your new severity_score column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-02.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomalies Pipeline: Python to SQL Analysis
  _Part A (Python): Download Australian Weather observations dataset (Bureau of Meteorology via Kaggle). Load daily temperature and rainfall data for the last 12 months. Calculate 30-year climate normals (monthly averages) for each location. Identify anomalies: days where temperature deviated >2 standard deviations from the normal. Export anomalies to a CSV with columns: station_id, date, temperature, normal_temp, deviation_std, rainfall. Part B (SQL): Load the anomalies CSV into a database table. Write a query using ROW_NUMBER() and LAG() to identify consecutive anomaly days (3+ consecutive days with deviation >2 SD) by station. Return: station_id, anomaly_start_date, anomaly_end_date, duration_days, max_deviation. Rank anomalies by severity (max_deviation) within each station. Expected output: top 5 most severe anomaly events across all stations._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle)`
  📁 Submit as: `quest3_2026-11-02.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
