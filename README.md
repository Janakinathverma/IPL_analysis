# 🏏 IPL Data Analytics Project (2008–2025)

A complete Data Analytics project built using **NumPy, Pandas, SQL, and Matplotlib** on IPL ball-by-ball dataset.

---

## 📂 Project Structure

IPL/
│
├── data/
│   └── IPL.csv   (Download manually – see below)
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── main.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── utils.py
│
├── sql/
│   └── queries.sql
│
├── outputs/
│   ├── plots/
│   └── reports/
│
├── requirements.txt
└── README.md

---

## 📊 Dataset

This project uses the IPL Ball-by-Ball dataset (2008–2025).

You must download it manually from Kaggle:

🔗 https://www.kaggle.com/code/arbazkhan971/indian-premier-league-analysis-2008-2025/input

### 📥 Steps to Download:

1. Go to the link above.
2. Download the dataset (IPL.csv).
3. Create a folder named `data` inside the project.
4. Place the file inside:

IPL/data/IPL.csv


⚠ The dataset is ignored in `.gitignore` to avoid uploading large files.

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd IPL
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the project
cd src
python main.py
📈 Features Implemented
✔ Total matches played
✔ Matches per season
✔ Top teams by wins
✔ Toss impact analysis
✔ Ball-level to match-level aggregation
✔ Clean modular architecture
✔ SQL queries
✔ Visualization module

🛠 Tech Stack
Python

NumPy

Pandas

SQL

Matplotlib

Seaborn

🔮 Future Improvements
Player-level analytics

Strike rate & economy rate

Feature engineering for ML

Predictive modeling

Streamlit dashboard

👤 Author
Janaki Nath Verma
BTech Graduate | Data Analytics & ML Aspirant