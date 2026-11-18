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
| 📅 Last Sync | 2026-11-18 15:56 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Momentum Rank — Window Functions Challenge
  _Using ASX 200 historical price data, calculate a 30-day rolling average price for each stock ticker. Then use ROW_NUMBER() and RANK() window functions to rank stocks by their momentum (current price vs rolling average) within each date partition. Find the top 5 momentum gainers for the most recent date in your dataset. Expected output: ticker, date, closing_price, 30day_avg, momentum_rank, momentum_percentile._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-18.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (contains crash records with location, severity, vehicle type, weather conditions). Write a Python/pandas script to: (1) handle missing values in severity and weather columns (impute or drop strategically), (2) standardise vehicle type categories (consolidate similar types), (3) extract crash hour from datetime, (4) create a severity score (1-5 scale), (5) export cleaned data to CSV. Document your cleaning decisions in comments. Expected output: a clean CSV with 10+ columns ready for analysis._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-18.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Analysis — Python ETL + SQL Analytics
  _Part A (Python): Download Australian Wildfire dataset (Kaggle). Use pandas to clean and standardise location data (latitude/longitude), date fields, and fire size/severity columns. Create a CSV with enriched data: fire_id, state, region, date, size_hectares, severity_level, season (derived from date). Part B (SQL): Load your cleaned CSV into a database. Write a query using CTEs to: (1) calculate fire frequency by state and season, (2) find the top 3 states with largest average fire size, (3) rank seasons by total fires using ROW_NUMBER(). Join results to show correlation between season and severity. Expected output: a report showing seasonal wildfire patterns by state with rankings._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-11-18.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
