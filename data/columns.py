# Creating a single source of truth of column names for the pipeline
NUMERIC_COLS = ["tenure","MonthlyCharges","TotalCharges"]
CATEGORICAL_COLS = [
    "gender","Partner","Dependents","PhoneService","MultipleLines",
    "InternetService","OnlineSecurity","OnlineBackup","DeviceProtection",
    "TechSupport","StreamingTV","StreamingMovies","Contract",
    "PaperlessBilling","PaymentMethod", "SeniorCitizen"
]
TARGET_COL = "Churn"
DROP_COLS = ["customerID"]
