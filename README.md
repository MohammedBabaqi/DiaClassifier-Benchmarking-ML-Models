# DiaClassifier

This repository contains an end-to-end Machine Learning project focused on **Diabetes Classification**. The project moves from Exploratory Data Analysis (EDA) and data preprocessing to model benchmarking, deployment via a **FastAPI** backend, and a user-friendly **Streamlit** dashboard.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-informational.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-informational.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)

DiaClassifier is an end-to-end machine learning project designed to predict diabetes using multiple classification models.

## 📌 Project Overview

The goal of this project is to predict the likelihood of diabetes in patients based on medical features and lifestyle indicators. Given the medical nature of the task, the pipeline emphasizes **Recall** and **ROC-AUC** to minimize false negatives.

### Key Components:

- **Notebooks**: Comprehensive EDA, class balancing using **SMOTE**, and benchmarking of 5+ ML models.
- **API (FastAPI)**: A high-performance backend serving the best-performing model.
- **GUI (Streamlit)**: An interactive web interface for real-time predictions.

---

## 📊 Dataset Description

The dataset includes medical and lifestyle features for over 250,000 patients.

| Feature           | Description                                         |
| :---------------- | :-------------------------------------------------- |
| `Diabetes_binary` | **Target Variable** (0 = No Diabetes, 1 = Diabetes) |
| `HighBP`          | High Blood Pressure status                          |
| `HighChol`        | High Cholesterol status                             |
| `BMI`             | Body Mass Index                                     |
| `Smoker`          | Smoking history                                     |
| `GenHlth`         | General health self-rating (1-5)                    |
| `Age`             | Age group category                                  |
| ...               | _And more (Physical Activity, Heart Disease, etc.)_ |

---

## 🚀 Machine Learning Pipeline

1. **Exploratory Data Analysis**: Identification of core predictors like `BMI`, `HighBP`, and `GenHlth`.
2. **Preprocessing**:
   - Handling class imbalance using **SMOTE**.
   - Feature selection based on correlation analysis.
3. **Model Benchmarking**:
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (SVM)
   - Decision Tree
   - Naive Bayes
4. **Optimization**: Automated hyperparameter tuning using `RandomizedSearchCV`.

---

## 🛠️ Tech Stack

- **Languages**: Python 🐍
- **ML Frameworks**: Scikit-Learn, Pandas, NumPy
- **API**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **Visualization**: Seaborn, Matplotlib

---

## 📂 Project Structure

```bash
.
├── Data/               # Raw and processed datasets
├── notebooks/          # ML Pipeline development & Benchmarking
├── api/                # FastAPI backend implementation
├── app/                # Streamlit GUI implementation
├── model/              # Saved model artifacts (.pkl / .joblib)
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MohammedBabaqi/DiaClassifier-Benchmarking-ML-Models.git
   cd Diabetes-Classification
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**:

   ```bash
   uvicorn api.main:app --reload
   ```

4. **Launch the Streamlit App**:
   ```bash
   streamlit run app/main.py
   ```

---

## 📈 Results

The models were evaluated on Accuracy, Precision, Recall, and F1-Score. While Logistic Regression provided high interpretability, ensemble methods or optimized SVM/KNN models showed significant improvements in capturing diabetic patterns after SMOTE application.

---

## 🛡️ License

Distributed under the MIT License. See `LICENSE` for more information.

---
