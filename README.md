# 📊 Retail Sales Forecasting & Inventory Optimization

## 🚀 Project Overview
This project predicts retail product demand using Machine Learning and optimizes inventory decisions using supply chain logic.

It combines:
- Demand Forecasting
- Feature Engineering
- Inventory Optimization (EOQ, Safety Stock, Reorder Point)

---

## 🧠 Problem Statement
Retail businesses often struggle with:
- Stockouts (loss of sales)
- Overstocking (high holding cost)

This project solves it by predicting demand and recommending optimal inventory levels.

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

---

## 📊 Features
- Time-series feature engineering (lag, rolling mean)
- Random Forest model for demand prediction
- Inventory optimization:
  - Safety Stock
  - Reorder Point
  - Economic Order Quantity (EOQ)

---

## 📈 Results

### 🔹 Model Performance
- MAE: 3.22 (low error indicates good prediction accuracy)

### 🔹 Forecast vs Actual
![Forecast](images/actual_vs_predicted.png)

---

## 📦 Inventory Output

| Metric | Value |
|------|------|
| Demand | ~35 units |
| Safety Stock | ~18 units |
| Reorder Point | ~53 units |
| EOQ | ~2500 units |

---

## 📁 Project Structure
Retail-Sales-Forecasting/
│
├── data/
├── notebooks/
│ └── eda_analysis.ipynb
├── src/
│ ├── model.py
│ ├── features.py
│ ├── inventory.py
├── outputs/
├── images/
└── main.py

---

## 🎯 Key Learnings
- Time-series feature engineering
- Model evaluation using MAE
- Real-world inventory optimization logic
- End-to-end ML pipeline development

---

## 💡 Future Improvements
- Use advanced models (XGBoost, LSTM)
- Add real-world datasets
- Build dashboard (Power BI / Streamlit)

---

## 👨‍💻 Author
Hardik Basavaraj Hipparagi