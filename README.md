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
| 📅 Last Sync | 2026-08-16 10:33 AEDT |

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
  _Using ASX 200 historical stock price data, calculate the 30-day rolling volatility (standard deviation of daily returns) for the top 10 most volatile stocks. Use a CTE to compute daily percentage changes, then apply window functions (ROW_NUMBER, LAG) to rank stocks by volatility. Return stock symbol, current price, volatility score, and volatility rank. Order by rank ascending. Expected output: 10 rows with stock identifiers and volatility metrics._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-16.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Feature Engineering
  _Download NSW Road Crash Data and perform: (1) Handle missing values in injury severity and crash type columns using mode imputation; (2) Create a new feature 'crash_hour_category' (morning peak 6-9am, afternoon peak 3-6pm, night 10pm-5am, other); (3) Remove duplicate records based on crash ID and timestamp; (4) Filter for crashes involving at least 2 vehicles; (5) Export cleaned dataset as CSV with row count validation. Expected output: cleaned CSV file with minimum 80% data retention and new categorical column._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-16.py`
- [ ] ⚡ **Combined Quest:** Australian Wine Production Pipeline: Extract, Clean, Load
  _Build a data pipeline: (1) Use Python/pandas to download or load Australian Wine Production Statistics (by region and vintage year); (2) Clean the data by standardizing region names (title case), removing rows with zero production, and validating vintage years (1980-2024); (3) Create a Python script that connects to a local SQLite database; (4) Load cleaned data into a 'wine_production' table; (5) Write a SQL query using window functions to calculate year-over-year production growth rate by region and rank regions by growth. Return top 5 fastest-growing regions with their growth percentages and rank. Expected output: populated SQLite database and a query result showing regional growth rankings._
  📦 Dataset: `Australian Wine Production Statistics — wineaustralia.com`
  📁 Submit as: `quest3_2026-08-16.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
