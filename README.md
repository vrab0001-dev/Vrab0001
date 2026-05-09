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
| 📅 Last Sync | 2026-05-09 11:46 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Rolling Average Momentum
  _Using ASX 200 historical prices dataset, calculate a 20-day rolling average for the top 5 companies by trading volume. Use window functions (AVG() OVER with ROWS BETWEEN) to compute the rolling average, then identify days where the closing price exceeded the rolling average by more than 2%. Return company name, date, closing price, rolling average, and percentage difference, ordered by company and date. This tests your mastery of window functions with frame specifications and analytical queries._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-05-09.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning Pipeline
  _Download NSW Road Crash Data (contains crash records with missing values, inconsistent date formats, and categorical encoding issues). Build a Python script using pandas to: (1) parse datetime columns correctly, (2) handle missing values in injury_severity and crash_type columns using appropriate strategies, (3) standardize location data (remove leading/trailing spaces, convert to title case), (4) create a new feature crash_hour_category binning time_of_crash into 'peak' (7-9am, 4-6pm) vs 'off-peak', (5) export cleaned data to CSV. Document your decisions for handling missing values._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-09.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Health Monitoring Pipeline
  _Integrate Python and SQL to analyze Great Barrier Reef monitoring data. Step 1 (Python): Download AIMS coral health monitoring dataset; clean it by removing incomplete records, standardizing site names, and converting water temperature to Celsius if needed. Save to a local SQLite database using pandas.to_sql(). Step 2 (SQL): Query the database to find the top 3 reef sites with the highest average coral bleaching percentage over the last 5 years; use a CTE to calculate yearly averages, then rank sites by the most recent year's severity. Return site_name, year, bleaching_percentage, and a rank. Step 3: Write a short summary showing which reefs are degrading fastest._
  📦 Dataset: `AIMS Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-05-09.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
