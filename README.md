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
| 📅 Last Sync | 2026-08-01 11:30 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Stock Performance Ranking with Moving Averages
  _Using the ASX 200 historical prices dataset, write a query that calculates the 20-day and 50-day moving averages for each stock symbol, then ranks stocks by their current price relative to the 50-day moving average (highest premium first). Use window functions ROW_NUMBER() or RANK() to assign rankings within each stock, and a CTE to pre-calculate the moving averages. Return: symbol, date, close_price, ma_20, ma_50, premium_percentage, and rank. Filter for the last 60 days of data only._
  📦 Dataset: `ASX 200 Historical Stock Prices — Kaggle`
  📁 Submit as: `quest1_2026-08-01.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download the NSW Road Crash Data from data.nsw.gov.au. Write a Python script using pandas that: (1) loads the CSV, (2) handles missing values in Crash_Severity and Speed_Zone columns by filling with mode, (3) removes duplicate crash records based on Crash_ID, (4) creates a new column 'Day_Of_Week' from the Crash_Date, (5) filters for crashes in 2024-2025 only, (6) exports a cleaned CSV with summary statistics printed to console showing total crashes, crashes by severity, and crashes by day of week. Expected output: cleaned CSV file + console output with 5+ key metrics._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-08-01.py`
- [ ] ⚡ **Combined Quest:** Melbourne Pedestrian Traffic Analysis: Peak Hours & Location Clustering
  _Combine Python and SQL to analyze Melbourne pedestrian counting data. Step 1 (Python): Load the pedestrian counting CSV from Melbourne Open Data Portal, clean datetime columns, filter for 2024 data, and export a staging table as CSV with columns: sensor_id, sensor_name, date, hour, pedestrian_count. Step 2 (SQL): Load the staged CSV, use window functions LAG() and LEAD() to identify peak hours (top 10% traffic by hour for each sensor), use a CTE to calculate average hourly traffic per sensor, then write a query that returns the top 5 sensors with highest average traffic and their peak hours. Expected deliverable: Python script + SQL query + output showing top sensors ranked by average pedestrian volume with peak hour times._
  📦 Dataset: `Melbourne Pedestrian Counting — Melbourne Open Data Portal`
  📁 Submit as: `quest3_2026-08-01.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
