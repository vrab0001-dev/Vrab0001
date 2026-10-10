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
| 📅 Last Sync | 2026-10-10 14:04 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Rankings with Window Functions
  _Using the ASX 200 historical prices dataset, write a SQL query with window functions to rank stocks by their year-to-date percentage gain. For each stock, calculate: (1) ROW_NUMBER() ranking by YTD gain, (2) LAG() to show the previous day's closing price, (3) a running sum of daily volume traded over the past 30 days using ROWS BETWEEN. Filter for the top 20 performers. Your output should include: stock_code, current_price, ytd_gain_percent, rank, previous_close, and 30day_volume_sum. Expected output: ~20 rows showing ASX leaders._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-10-10.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning and Risk Score Calculation
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python/pandas script to: (1) load the CSV, (2) handle missing values in columns like 'Severity', 'Speed_Zone', and 'Weather_Condition' by imputing or dropping as appropriate, (3) standardise text fields (remove extra spaces, convert to title case), (4) create a new 'risk_score' column (0-100) based on Severity weight (Fatal=100, Serious=75, Other=25) and Weather_Condition (Rain/Fog +20 points), (5) export cleaned data to a new CSV. Your output CSV should have all original columns plus 'risk_score' and a 'data_quality_flag' column marking rows with imputed values._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-10-10.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production ETL: Python Ingestion to SQL Analytics
  _Integrate data from the Australian wine production statistics (Wine Australia) with a SQL analysis layer. (1) In Python: Write a script to fetch or load wine production CSV data, clean vintage years, standardise region names (remove special chars, lowercase), and handle null production volumes by forward-filling or interpolating. Save as 'wine_clean.csv'. (2) Load this into a SQL database (SQLite or PostgreSQL). (3) Write a SQL query with CTEs to: identify the top 5 regions by total production volume over the last 10 years, calculate year-on-year growth rate using LAG(), rank regions by consistency (lowest std_dev of production), and combine into a single result showing region, total_volume, yoy_growth_percent, and consistency_rank. Expected output: 5 rows with regional insights._
  📦 Dataset: `Australian Wine Production Statistics — Wine Australia (wineaustralia.com data exports)`
  📁 Submit as: `quest3_2026-10-10.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
