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
| 📅 Last Sync | 2026-06-13 12:06 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum Analysis with Window Functions
  _Using the ASX 200 historical prices dataset, calculate a 10-day moving average and identify momentum shifts for each stock. Create a CTE that ranks stocks by their price change velocity (current price vs 10-day MA). Use window functions ROW_NUMBER() and LAG() to detect when a stock crosses above or below its moving average. Output the top 5 stocks with strongest upward momentum and bottom 5 with downward momentum for the most recent trading date. Include columns: stock_code, current_price, ma_10day, price_velocity, momentum_rank._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-13.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download the NSW Road Crash Data and perform comprehensive data cleaning. Tasks: (1) Handle missing values in severity and crash type columns using appropriate strategies; (2) Parse datetime columns and extract hour-of-day, day-of-week, and season features; (3) Standardise location data by removing duplicates and fixing inconsistent suburb names; (4) Create a new feature 'crash_severity_score' by encoding severity levels numerically; (5) Filter crashes from 2023-2025 only and export cleaned dataset to CSV. Produce a data quality report showing null counts before/after cleaning and value distributions for key features._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-13.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Analysis: Data Pipeline End-to-End
  _Build a mini data pipeline: (1) In Python/pandas, download or load Australian wine production statistics (regions, varieties, vintage years, production volume). Clean the data: handle missing vintage years, standardise region names, convert production volumes to consistent units (tonnes). (2) Create a SQLite database and load the cleaned data into a 'wine_production' table. (3) Write SQL queries to: identify the top 3 wine regions by total production across all years, calculate year-over-year growth rate for the largest producer using window functions (LAG), rank wine varieties by volume for vintage 2023. (4) Export results to CSV. Document your schema design and data transformations. Expected output: cleaned CSV, SQLite DB file, 3 result CSVs from SQL queries._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com / Kaggle`
  📁 Submit as: `quest3_2026-06-13.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
