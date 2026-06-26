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
| 📅 Last Sync | 2026-06-26 12:05 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Price Momentum with Window Functions
  _Using ASX 200 historical stock price data, calculate a 30-day rolling average and identify momentum shifts. For each stock, use ROW_NUMBER() to rank days by price change percentage, then use LAG() to compare current price against the previous day. Create a CTE that filters only stocks where the 30-day rolling average has increased by more than 5% in the last week. Output: stock symbol, date, current price, 30-day MA, price change %, and momentum rank. Order by momentum rank descending._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-06-26.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation
  _Download NSW Road Crash Data from data.nsw.gov.au. The dataset contains messy crash records with missing values, inconsistent location formats, and duplicate entries. Your task: (1) Load the CSV, identify and handle missing values in severity and crash type columns; (2) standardise suburb/postcode formatting; (3) remove exact duplicates and near-duplicates (same location, date, time); (4) create a new feature 'time_of_day' (Morning 6-12, Afternoon 12-18, Evening 18-24, Night 0-6); (5) export a cleaned CSV and generate a summary report showing record count before/after cleaning, missing value percentages by column, and top 5 crash locations._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-06-26.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis Pipeline
  _Build an end-to-end data pipeline: (1) Download Melbourne pedestrian counting data (sensors across the city). (2) Use Python/pandas to load, clean, and transform the data: handle missing hourly counts, aggregate to daily totals by sensor location, create a feature for day-of-week and hour-of-day patterns. (3) Export cleaned data to a CSV. (4) Load the cleaned data into SQL and write a query using window functions (RANK, LAG, ROW_NUMBER) to: identify peak pedestrian hours, detect anomalies (days where foot traffic was 50%+ below the rolling 7-day average), and rank sensors by total foot traffic. Output a report showing top 10 sensors, peak hours, and anomaly dates flagged for investigation._
  📦 Dataset: `Melbourne Pedestrian Counting System — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-06-26.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
