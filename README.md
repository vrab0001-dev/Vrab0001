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
| 📅 Last Sync | 2026-04-28 11:46 AEDT |

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
  _Using ASX 200 historical price data, write a query that calculates the 20-day moving average price for each stock, ranks stocks by their current price relative to their 20-day average (highest performers first), and identifies stocks where price crossed above their moving average in the last 5 trading days. Use window functions (AVG() OVER, ROW_NUMBER(), LAG()) and CTEs to structure your solution. Expected output: stock ticker, current price, 20-day moving average, momentum rank, and crossover flag (Y/N)._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-04-28.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data (contains messy, incomplete records with inconsistent date formats, missing postcodes, and duplicate entries). Write a Python script using pandas that: (1) standardises date columns to YYYY-MM-DD format, (2) removes duplicate crash records based on crash ID and timestamp, (3) handles missing postcodes by forward-filling from the same local government area, (4) creates a severity category column (Minor/Moderate/Severe/Fatal based on injury count), (5) exports a cleaned CSV with row counts before/after cleaning logged to console._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-04-28.py`
- [ ] ⚡ **Combined Quest:** Australian Weather Anomaly Detection & Storage Pipeline
  _Create an end-to-end pipeline: (1) Use Python + pandas to load Australian Bureau of Meteorology daily weather observations for the past 90 days, (2) calculate monthly temperature anomalies (deviation from 30-year historical mean — assume you have a reference CSV with mean temps by month/location), (3) identify days where temperature exceeded mean + 2 standard deviations, (4) create a cleaned dataset with anomaly flags and confidence scores, (5) write a SQL query to load this data into a staging table and generate a summary report showing: location, anomaly count, max temperature spike, and affected date range. Output: (a) cleaned CSV, (b) SQL INSERT statements, (c) anomaly summary report._
  📦 Dataset: `Australian Weather Observations — Bureau of Meteorology (Kaggle: jsphyg)`
  📁 Submit as: `quest3_2026-04-28.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
