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
| 📅 Last Sync | 2026-05-29 12:00 AEDT |

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
  _Using ASX 200 historical prices dataset, calculate a 7-day moving average of closing prices and identify the top 5 stocks by momentum (price change percentage over last 30 days). Use window functions ROW_NUMBER() and LAG() to rank stocks by momentum within each date partition. Return stock symbol, date, closing price, 7-day moving average, and 30-day momentum rank. Filter for the last trading date in your dataset only._
  📦 Dataset: `ASX 200 historical prices — Kaggle`
  📁 Submit as: `quest1_2026-05-29.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Load NSW Road Crash Data and perform the following: (1) Clean missing values in crash severity, location coordinates, and vehicle count columns using appropriate strategies (drop or impute). (2) Standardise location names to title case and remove duplicates. (3) Create a new feature: time_of_day (Morning 6-12, Afternoon 12-18, Evening 18-24, Night 0-6) from the crash time field. (4) Export cleaned data to a new CSV file with only crashes from the last 2 years. Log the data quality metrics (% missing before/after, row count reduction) to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-05-29.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Insights: Python ETL + SQL Analytics
  _Part 1 (Python): Download Melbourne pedestrian counting data. Clean the dataset by removing null sensor readings, standardising sensor location names, and converting timestamps to datetime format. Aggregate hourly foot traffic by sensor location and hour of day. Save to a local SQLite database in a table named 'pedestrian_traffic'. Part 2 (SQL): Query the SQLite database to find: (a) Top 3 sensors by average daily foot traffic, (b) Hour of day with highest traffic across all sensors (using GROUP BY and window functions), (c) Calculate percentage change in traffic for each sensor comparing peak hour to off-peak hour (0-6 AM). Return results as three separate result sets with clear labels._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-05-29.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
