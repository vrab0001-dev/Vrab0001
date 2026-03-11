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
| 📅 Last Sync | 2026-03-11 16:01 AEDT |

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
  _Using ASX 200 historical stock price data, calculate the 10-day moving average and identify price momentum for each stock. Use window functions (ROW_NUMBER, LAG) to: (1) rank stocks by their price change over the last 30 days in descending order; (2) calculate the percentage change from the previous day for each stock; (3) identify stocks that have increased for 3+ consecutive days. Return stock code, current price, 10-day moving average, momentum rank, and consecutive gain count. Filter results to show only top 20 momentum gainers._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-03-11.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Safety Score Calculation
  _Load NSW Road Crash Data (a CSV with crash records including date, location, severity, speed limit, weather, vehicle type). Clean the dataset by: (1) handling missing values in weather and speed_limit columns (use mode for weather, median for speed_limit); (2) standardizing location names (lowercase, trim whitespace); (3) removing duplicate crash records based on date, location, and time; (4) converting date to datetime format. Then calculate a crash safety score (0-100) per suburb based on frequency, average severity (higher severity = lower score), and speed limit violations. Export cleaned data and suburb safety scores to separate CSV files._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-03-11.py`
- [ ] ⚡ **Combined Quest:** Australian Wildfire Risk Analysis Pipeline
  _Build an end-to-end pipeline: (1) Download Australian Wildfire dataset (Kaggle) containing fire incidents with date, location (state/postcode), burned area, and weather conditions. (2) Use Python/pandas to clean the data: parse dates, standardize state names, remove outliers (burned area > 99th percentile), and create severity tiers (Low/Medium/High/Catastrophic based on burned area quartiles). (3) Export cleaned data to a SQLite database. (4) Write SQL queries to: identify the top 5 states by total burned area in the last 10 years; calculate average burned area per incident by season; use a CTE to rank months by fire frequency and find the peak fire season. (5) Return results showing state-level risk profiles and seasonal trends._
  📦 Dataset: `Australian Wildfire Dataset — Kaggle`
  📁 Submit as: `quest3_2026-03-11.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
