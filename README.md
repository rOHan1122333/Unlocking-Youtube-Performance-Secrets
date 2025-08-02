Unlocking-YouTube-Performance-Secrets/


 1. Project Folder Structure
├── 📁 scripts/
│   ├── feature.py
│   ├── heatmap.py
│   ├── pairplot_analysis.py
│   ├── Predicmodeling.py
│   ├── test_imports.py
│   ├── test_process.py
│   ├── train.py
│   └── visualization.py
│
├── 📁 data/
│   └── youtube_channel_data.csv
├── youtube peformance.pbix
├── README.md

2. Execution Workflow for the Project
 Unlocking YouTube Performance Secrets
A complete data-driven analytics and visualization project using **Python (EDA + modeling)** and **Power BI** to decode YouTube channel performance and drive insights.
## 📁 Project Structure


3.youtube peformance.pbix ← Final Power BI dashboard
## 🔄 Workflow & Execution Order
Run these scripts in order for full functionality:

1. `test_imports.py` — Load data, inspect structure & null values  
2. `test_process.py` — Clean & parse durations in ISO format  
3. `pairplot_analysis.py` — Visualize pairwise variable relations  
4. `heatmap.py` — Analyze correlation matrix (numeric-only)  
5. `visualization.py` — Histogram for revenue distribution  
6. `feature.py` — Train Random Forest and plot top 15 features  
7. `Predicmodeling.py` — Ensure clean data + feature-target split  
8. `train.py` — Final model build + evaluation (MSE, R²)

---

## 📊 Power BI Dashboard

- File: `youtube performance.pbix`
- Includes:
  - 📈 KPI Cards (Views, Revenue, Watch Time)
  - 📊 Monthly Revenue Trend
  - 🧭 Traffic Source Distribution
  - 🏆 Top 10 Videos by CTR/Views
- Screenshot previews in `/screenshots/`

---

## 🧰 Tools Used

- Python (Pandas, Seaborn, Scikit-learn, Matplotlib)
- Power BI
- CSV dataset (`youtube_channel_data.csv`)

---

## ✨ Insights Extracted

- Feature importance showed **Views**, **Subscribers**, and **Average View %** are key drivers of revenue.
- Power BI dashboard enabled rich visual storytelling for decision-makers.
- The modeling process evaluated revenue predictions using regression.

---








