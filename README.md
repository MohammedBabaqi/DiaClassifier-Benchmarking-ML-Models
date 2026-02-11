# 🩺 DiaClassifier: Advanced Diabetes Risk Intelligence


[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-informational?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Models-orange)](https://xgboost.readthedocs.io/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker&logoColor=white)](https://www.docker.com/)

**DiaClassifier** is a professional-grade end-to-end machine learning ecosystem designed for precision diabetes risk assessment. By leveraging state-of-the-art classification algorithms, class-balancing techniques (SMOTE), and model calibration, DiaClassifier transforms clinical metrics into actionable diagnostic insights.

---

## 📌 Project Overview

The goal is to predict whether a patient has diabetes based on medical features and lifestyle indicators. This project identifies the optimal pipeline for predictive accuracy and clinical reliability by benchmarking multiple ML models against various feature configurations.

DiaClassifier's core philosophy is **Recall-First Detection**: we prioritize minimizing false negatives to ensure at-risk patients are flagged for clinical review.

---

## 📊 Dataset Description & Source

The system is trained on a high-fidelity dataset featuring medical and lifestyle indicators for over 250,000 patients.

| Column            | Description         | Values / Meaning              |
| :---------------- | :------------------ | :---------------------------- |
| `Diabetes_binary` | **Target Variable** | 0 = No diabetes, 1 = Diabetes |
| `HighBP`          | High Blood Pressure | 0 = No, 1 = Yes               |
| `HighChol`        | High Cholesterol    | 0 = No, 1 = Yes               |
| `BMI`             | Body Mass Index     | Continuous numeric value      |
| `Smoker`          | Smoking History     | 0 = No, 1 = Yes               |
| `GenHlth`         | General Health      | 1 = Excellent → 5 = Poor      |
| `PhysActivity`    | Physical Activity   | 0 = No, 1 = Yes               |
| `Age`             | Age Group           | 1 = 18–24 → 13 = 80+          |

**🔗 Dataset Source:** [Kaggle: Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv)

---

## 🏗️ System Architecture

The project is architected as a decoupled micro-service environment:

1.  **Analytical Engine**: A high-performance XGBoost classifier optimized for class imbalance (SMOTE) and calibrated (`CalibratedClassifierCV`) for reliable probability estimation.
2.  **FastAPI Backend**: A production-ready REST API built with Pydantic for strict data validation and efficient model orchestration.
3.  **Streamlit Dashboard**: A "Pro-Grade" native UI featuring intuitive input grouping, real-time metrics, and visual probability delta analysis.
4.  **Containerization**: Fully Dockerized stack with professional folder organization and Docker Compose support.

---

## 📂 Project Structure

```text
.
├── api/                    # 🚀 FastAPI Backend
│   ├── main.py             # API Entry point & Routes
│   ├── schemas.py          # Pydantic Data Validation models
│   └── model_utils.py      # Model Loading & Logic
├── app/                    # 🎨 Streamlit Frontend
│   └── main.py             # Native Dashboard Implementation
├── model/                  # 🧠 ML Artifacts
│   └── diabetes_bundle.pkl # Pre-trained & Calibrated Model Pipeline
├── notebooks/              # 🔬 Research & Development
│   └── diabetes_classification_multiple_model_pipline.ipynb
├── docker/                 # 🐳 Containerization & Compose
│   ├── Dockerfile          # Multi-port image definition
│   ├── .dockerignore       # Slim image optimization
│   └── docker-compose.yml  # 🏗️ Orchestration (Professional setup)
├── start_all.py            # ⚡ One-click Local Runner
├── requirements.txt        # 📦 Dependencies (Optuna, SHAP, etc.)
└── .gitignore              # 🧹 Project Cleanliness (pycache excluded)
```

---

## 📸 Interface ScreenShot

![screenshot](/images/screenshot.png)
_Professional native Streamlit interface featuring intuitive grouping and real-time risk assessment metrics._

---

## 🚀 Getting Started

### 1. Local Development (Manual)

```bash
# Install dependencies
pip install -r requirements.txt

# Launch both API and UI
python start_all.py
```

### 2. Docker Deployment (Recommended)

Deploy on any machine with zero local configuration:

```bash
# Using Docker Compose (from project root)
docker-compose -f docker/docker-compose.yml up --build

# Or Manual Build
docker build -t diaclassifier -f docker/Dockerfile .
docker run -p 8000:8000 -p 8501:8501 diaclassifier
```

---

## 🧬 Data Science Results

The models were evaluated using **Recall**, **Accuracy**, and **ROC-AUC Score**. The `XGBoost (Medical++ Optimized)` model emerged as the top performer.

| Model                   | Accuracy | Recall | F1-Score | ROC-AUC |
| :---------------------- | :------: | :----: | :------: | :-----: |
| **XGBoost (Optimized)** |  0.833   | 0.833  |  0.833   |  0.833  |
| Logistic Regression     |  0.800   | 0.750  |  0.774   |  0.800  |

---

## 🛡️ License & Acknowledgments

Distributed under the MIT License. Created by **Mohammed Babaqi**.

### 🔗 Connect

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/MohammedBabaqi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/mohammedbabaqi/)

---

_Disclaimer: This tool is for educational and screening assistance and should not replace professional medical diagnosis._
