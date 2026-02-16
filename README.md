
# 🏏 IPL Data Analytics Project (2008–2025)

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) 
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas) 
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange)

An end-to-end data analytics pipeline that transforms raw ball-by-ball IPL data into actionable cricketing insights. This project covers the entire lifecycle from data cleaning to SQL-based querying and automated visualization.

---

## 📂 Project Structure

```text
IPL/
├── data/           # (User-provided) Raw ball-by-ball CSV
├── notebooks/      # Exploratory Data Analysis (EDA) & Prototyping
├── src/            # Modular Python Codebase
│   ├── main.py             # Execution Entry Point
│   ├── data_cleaning.py    # Handling missing values & team renaming
│   ├── analysis.py         # Computational logic (Win rates, Toss impact)
│   ├── visualization.py    # Plot generation (Seaborn/Matplotlib)
│   └── utils.py            # Helper functions
├── sql/            # Analytical queries for database integration
├── outputs/        # Generated PNG plots and summary reports
└── requirements.txt

```

---

## 📊 Dataset Information

Due to file size limits on GitHub (**102MB**), the raw dataset is not included in this repository.

**Link:** [IPL Ball-by-Ball Dataset (2008–2025) - Kaggle](https://www.kaggle.com/code/arbazkhan971/indian-premier-league-analysis-2008-2025/input)

### 📥 Manual Setup:

1. Download `IPL.csv` from the link above.
2. Create a `/data` folder in the project root.
3. Place the file inside: `IPL/data/IPL.csv`.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd IPL

```

### 2️⃣ Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```

### 3️⃣ Run the Analysis

```bash
cd src
python main.py

```

---

## 📈 Analysis Features

* **Ball-to-Match Aggregation:** Converts 200,000+ rows of delivery data into high-level match summaries.
* **Toss Impact Analysis:** Investigates the statistical advantage of winning the toss across 18 seasons.
* **Seasonal Trends:** Tracks the evolution of total runs and match frequency per year.
* **Team Performance:** Ranks franchises based on historical win percentages.
* **Automated Visualization:** Generates and saves plots directly to the `outputs/plots/` folder.

---

## 🛠 Tech Stack

| Tool | Usage |
| --- | --- |
| **Python** | Primary programming language |
| **Pandas / NumPy** | Data manipulation and numerical computation |
| **SQL** | Analytical querying and data filtering |
| **Matplotlib / Seaborn** | Statistical data visualization |

---

## 🔮 Future Improvements

* **Advanced Player Stats:** Calculation of strike rates and economy rates.
* **Machine Learning:** Predictive modeling for win probability.
* **Interactive UI:** Developing a live dashboard using **Streamlit**.

---

## 👤 Author

**Janaki Nath Verma** *BTech Graduate | Data Analytics & ML Aspirant*

```
