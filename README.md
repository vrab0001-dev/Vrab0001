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
| 📅 Last Sync | 2026-11-22 14:49 AEDT |

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
- [ ] 🗄️ **SQL Quest:** ASX 200 Volatility Rankings with Window Functions
  _Using ASX 200 historical price data, calculate the 30-day rolling standard deviation of daily returns for each stock using window functions. Rank stocks by volatility within each month using ROW_NUMBER(). Then use a CTE to identify the top 5 most volatile stocks each month. Your output should show: stock_code, month, volatility_rank, rolling_std_dev, and average_closing_price for that month. Order by month descending, then rank ascending._
  📦 Dataset: `ASX 200 Historical Prices — Kaggle`
  📁 Submit as: `quest1_2026-11-22.sql`
- [ ] 🐍 **Python Quest:** NSW Road Crash Data Cleaning & Aggregation Pipeline
  _Download NSW Road Crash Data and build a cleaning script that: (1) removes rows with missing crash_date or location coordinates, (2) standardises speed_zone values to uppercase and handles typos (e.g. '50 km/h', '50kmh', '50KM/H' all become '50'), (3) creates a new column crash_hour extracted from crash_time, (4) filters to crashes from 2020 onwards only, (5) exports a cleaned CSV with columns: crash_id, crash_date, crash_hour, speed_zone, location, severity. Write your script to handle at least 3 common data quality issues and log how many rows were removed at each step._
  📦 Dataset: `NSW Road Crash Data — data.nsw.gov.au`
  📁 Submit as: `quest2_2026-11-22.py`
- [ ] ⚡ **Combined Quest:** Great Barrier Reef Monitoring: SQL Analysis + Python Reporting
  _Part 1 (SQL): Using Great Barrier Reef monitoring data, write a query that calculates: coral_bleaching_percentage by reef_site and monitoring_year, using LAG() to show year-over-year change in bleaching percentage, and RANK() to identify the top 10 most affected reefs across all years. Part 2 (Python): Import this SQL result into pandas and create a summary report that: (1) identifies reefs with worsening trends (bleaching increased for 3+ consecutive years), (2) calculates the average rate of change in bleaching percentage per reef, (3) exports a markdown report with headers, tables, and key findings. Combine the SQL output and Python analysis into one final CSV showing reef_site, year, bleaching_pct, yoy_change, and trend_direction._
  📦 Dataset: `Great Barrier Reef Monitoring Data — aims.gov.au`
  📁 Submit as: `quest3_2026-11-22.py`
<!-- VRAB_QUESTS_END -->

---

### 📖 ABOUT
Data engineering learner building real projects from real data.
Currently raiding Australian government datasets and automating everything in sight.

> *"The weakest hunter can still clear the dungeon — if they keep showing up."*
