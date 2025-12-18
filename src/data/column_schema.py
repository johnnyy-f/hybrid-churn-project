from pandas.api.types import CategoricalDtype

COLUMN_DTYPES = {
    "customerID": "string",
    "gender": "category",
    "SeniorCitizen": "category",
    "Partner": "category",
    "Dependents": "category",
    "tenure": "int64",
    "PhoneService": "category",
    "MultipleLines": "category",
    "InternetService": "category",
    "OnlineSecurity": "category",
    "OnlineBackup": "category",
    "DeviceProtection": "category",
    "TechSupport": "category",
    "StreamingTV": "category",
    "StreamingMovies": "category",
    "Contract": CategoricalDtype(
        categories=["Month-to-month", "One year", "Two year"],
        ordered=True,
    ),
    "PaperlessBilling": "category",
    "PaymentMethod": CategoricalDtype(
        categories=["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
        ordered=False,
    ),
    "MonthlyCharges": "float64",
    "TotalCharges": "float64",
    "Churn": "category",
}
