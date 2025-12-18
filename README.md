# Telco Customer Churn Prediction & Business Impact Analysis

## Overview of the Project
This project was initiated to display strong Data Science capabilities. Here we look to identify the main drivers of customer churn for a telecommunications provider (dataset which was obtained via Kaggle - https://www.kaggle.com/datasets/blastchar/telco-customer-churn). Through exploring various machine learning models and techniques, this analysis provides actionable insights that would from a business perspective help retention teams design targeted strategies, to reduce the loss from declining **Customer Lifetime Value (CLV)**.

This project highlights strong data science capabilities that moves beyond just creating a simple "black-box" prediction model. Final notebooks Model Evaluation and Model Explainability (In-progress) focus on **Model Explainability**, bridging the gap between the production of high-performance algorithms and practical business reasons, which can explain areas of investigation where focus can be done to work on reducing churn.

---

## Project Architecture
The project is structured into a modular, end-to-end data science pipeline:

1.  **Exploratory Data Analysis (EDA):** Data ingestion, cleaning, and validation using `Pandera` to ensure schema integrity.
2.  **Feature Engineering:** Transforming raw features into high-quality predictive variables, including handling categorical encoding and scaling.
3.  **Model Training:** Establishing baseline performance using Logistic Regression, Random Forest, XGBoost, and LightGBM.
4.  **Hyperparameter Tuning:** Optimizing models using cross-validation and `Optuna` to maximize predictive power.
5.  **Model Evaluation:** Final assessment on the test set using ROC AUC, F1-Score, and Brier Score to ensure model reliability.
6.  **Model Explainability (Still in-progress):** Utilises SHAP (SHapley Additive exPlanations) to interpret global and local churn drivers for business stakeholders.

---

## Technical Stack
* **Languages:** Python 3.13.9
* **Data Handling:** Pandas, NumPy, Parquet (for efficient data storage)
* **Validation:** Pandera (Schema enforcement)
* **Machine Learning:** Scikit-learn, XGBoost, LightGBM
* **Explainability:** SHAP, Permutation Importance
* **Optimization:** Optuna / GridSearch
* **Deployment Tools:** Joblib (Model serialisation)

---

## Key Insights & Business Impact

### Global Drivers of Churn
* **High-Risk Factors to improve:** Customers on **Month-to-month contracts** and those using **Fiber Optic service** (especially when paired with high monthly charges) were identified as the most likely to churn.
* **Factors of focus to retain customers:** **Long-term contracts (Two-year)** and **high tenure** are the strongest predictors of customer loyalty.

### Model Performance
* **Champion Model:** **XGBoost** emerged as the top-performing model, achieving the highest **ROC AUC** when compared with the other models.
* **Strategic Focus:** The model was evaluated to minimise **False Negatives**, prioritizing the identification of at-risk customers even at the cost of slight False Positives, as the cost of customer acquisition far exceeds the cost of retention incentives.

---

## Recommendations
Based on the draft version of **Model Explainability**, the following actions are recommended:
1.  **Contract Transfer:** Target month-to-month customers with personalised incentives to move to stable, long-term contracts.
2.  **Internet Service Investigation:** Investigate the Fiber Optic offering's value proposition, as it currently correlates with high churn.
3.  **Loyalty Reinforcement:** Proactively reward high-tenure customers to maintain their "protective" status and prevent competitive poaching.

---
##  Future Roadmap & Enhancement Plans
I am currently iterating on this project to evolve it from the current research/model development analysis into a production-ready system, to display capabilities. 

### 1. Code Quality & Maintainability (Current Focus)
To ensure this repository meets professional software engineering standards, I am in the process of:
* **Refactoring Notebook 06:** Tidying up the Explainability logic for better modularity.
* **Linting & Formatting:** Implementing `Flake8`, `isort`, and `Black` across all scripts and notebooks to ensure PEP8 compliance and consistent import ordering.

### 2. Cloud Deployment & MLOps (GCP)
To demonstrate competence in cloud architecture and maintainability:
* **Vertex AI Integration:** Transitioning the training pipeline to Google Cloud Platform (GCP).
* **Model Serving:** Deploying the champion XGBoost model as a REST API using FastAPI and Docker.
* **CI/CD:** Implementing GitHub Actions to run automated schema validation and linting on every push.

### 3. Advanced Modeling & Monitoring
* **Drift Detection:** Implementing monitoring to detect data/concept drift post-deployment.
* **Automated Retraining:** Setting up a pipeline that triggers retraining when model performance dips below a specific Brier Score threshold.

---

## Project Structure
```text
├── data/               # Raw and processed parquet files
├── models/             # Serialised joblib models (Baseline & Tuned)
├── notebooks/          
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_tuning.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_model_explainability.ipynb
├── src/data            # Python modules for data loading and validation
│   ├── column_schema.py
│   ├── load_data.py
│   └── schema_validation.py
│   └── type_utils.py
└── README.md           
└── requirements.txt     
